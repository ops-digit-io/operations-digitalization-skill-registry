#!/usr/bin/env python3
"""Analyse a machine's data-point list for standardization problems.

    python3 analyze_signals.py POINTS.json [--capability oee] [--json]
    python3 analyze_signals.py POINTS.csv  --capability cycle-time
    python3 analyze_signals.py POINTS.json --cluster        # functional area + importance
    python3 analyze_signals.py POINTS.json --report > report.md   # the structured report

Input is the data-point list for one machine or datatron — the shape the IIoT edge
platform returns from `/api/datatrons/{id}/data_points`, or a CSV with `uuid,label`
columns. Any JSON array of objects carrying `uuid` and `label` works.

What it checks, and why each one is here: every rule below was derived from the
the signal names in use across the flow estate, where the same concept is
named in many different ways. That variance is what stops one plant's solution
being taken by the next.

Exit code: 2 if any BLOCKER, 1 if any WARN, 0 otherwise.
"""

from __future__ import annotations

import csv
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict

# ── the canonical vocabulary ────────────────────────────────────────────────
# Derived from the flow corpus. `canonical -> variants actually observed`.
CANONICAL: dict[str, list[str]] = {
    # counting & throughput
    "TotalPartCounter":      ["PartCounter", "SetupPartCounter", "TotalParts"],
    "PartProducedTrigger":   ["PartCounterTrigger", "PartTrigger"],
    "ShiftPartProduced":     ["ShiftPartCounter"],
    "TotalCycleCounter":     ["CycleCounter"],
    "ShiftCycleProduced":    ["ShiftCycleCounter"],
    # cycle & timing
    "CycleStart":            ["CycleStartValue"],
    "CycleEnd":              ["CycleEndTrigger"],
    "CycleTime":             ["CycleTimeNormalized", "EstimatedCycleTime"],
    "CycleTrigger":          [],
    "LoadingTime":           [],
    "ProcessTime":           [],
    # machine state
    "MachineMode":           ["MachineOperationMode"],
    "MachineModeNormalized": ["MachineStatusMapped"],
    "MachineStatus":         ["MachineState"],
    "MachineIsReleased":     [],
    "MachineSetup":          ["MachineModeSetup"],
    # process values
    "Pressure":              ["CompressorPressure"],
    "Temperature":           [],
    "MeltTemperature":       ["AverageMeltTempature", "AverageMeltTemperature"],
    "StandardSpeed":         ["BraidSpeedSV"],
    "HeatingProgram":        ["HeatingType"],
    # quality & limits
    "UpperTolerance":        [],
    "LowerTolerance":        [],
    "HardUpperLimit":        [],
    "SoftUpperLimit":        [],
    "HardLowerLimit":        [],
    "SoftLowerLimit":        [],
    "LimitValue":            [],
    "CurrentValue":          [],
    "EvaluationResult":      [],
    # identification
    "ToolId":                ["ToolIdContinuous", "ToolIdChanging", "ValueToolId"],
    "Partnumber":            ["InternalPartnumber", "SupplierPartnumber", "PartnumberGauge",
                              "NokPartnumber", "OkPartnumber", "ValuePartnumber"],
    "RecipeId":              ["ProgramID", "RecipeIDRunning"],
    # alerting
    "AlertMessage":          ["AdhocAlertMessage"],
    "ErrorActive":           ["ErrorActiveValue"],
}

VARIANT_OF = {v.lower(): c for c, vs in CANONICAL.items() for v in vs}
CANON_LOWER = {c.lower(): c for c in CANONICAL}

# Signals a capability needs before it can be built to the standard.
CAPABILITY_REQUIREMENTS: dict[str, list[str]] = {
    "oee":         ["MachineStatus", "TotalPartCounter", "CycleTime", "StandardSpeed"],
    "cycle-time":  ["CycleStart", "CycleEnd"],
    "downtime":    ["MachineStatus"],
    "part-count":  ["PartProducedTrigger"],
    "tolerance":   ["CurrentValue", "HardUpperLimit", "HardLowerLimit", "MachineMode"],
    "traceability":["ToolId", "Partnumber", "RecipeId"],
    "alerting":    ["ErrorActive", "AlertMessage"],
}

# Raw PLC addressing that leaked through instead of being given a name.
RAW_TAG = re.compile(
    r"^(_|db\d|dbw|dbd|dbx|m\d|%[imq]|i\d+\.\d|q\d+\.\d|tag\d|var\d|item\d)", re.I)
ADDRESS_LIKE = re.compile(r"^(DB\s*\d+|[A-Z]{1,3}\d+([.,]\d+)?|\d+)$", re.I)

TYPO_HINTS = {"tempature": "Temperature", "temperatur": "Temperature",
              "vocuum": "Vacuum", "vaccum": "Vacuum", "presure": "Pressure",
              "coutner": "Counter", "calulator": "Calculator", "acumulate": "Accumulate"}

# ── functional-area search patterns ─────────────────────────────────────────
# Order matters: identification before everything (ToolIdChanging), machine state
# before timing (MachineSetup). See references/clustering-signals.md.
AREA_PATTERNS: list[tuple[str, str]] = [
    ("identification", r"tool.?id|part.?numb|recipe|program.?id|serial|batch|order"),
    ("machine-state",  r"machine.?(mode|state|status)|released|setup|automatic|manual|fault|heartbeat"),
    ("cycle-timing",   r"cycle|(^|[^a-z])time|duration|loading|process.?time|step.?chain"),
    ("counting",       r"count|produced|output|pieces|pza|parts|volume|shot|per.?minute|meters|stück"),
    ("quality-limits", r"toleran|limit|spec|quality|nok|scrap|reject|failure|evaluation|deviation"),
    ("alerting",       r"alert|alarm|error|fault.?text|notification|warn|message|meldung"),
    ("energy",         r"energy|power|kwh|current|voltage|consumption|compressor|energie"),
    ("process-value",  r"pressure|temp|melt|speed|zone|diameter|vacuum|vocuum|screw|head|flow|"
                       r"level|torque|position|druck|heizung"),
]
SETPOINT = re.compile(r"_sv$|setpoint|set.?pt|sollwert|nominal", re.I)

# How many capability templates each area feeds — the coverage weight (method weight, not a count to quote).
AREA_COVERAGE = {
    "machine-state": 4, "counting": 4, "cycle-timing": 3, "quality-limits": 3,
    "process-value": 2, "identification": 2, "alerting": 2, "energy": 1, "unclassified": 0,
}
# Consumer-demand band per area (0 none, 1 low, 2 medium, 3 high). Re-derive it from the
# use-case portfolio (business_process counts) when the demand changes.
AREA_DEMAND = {
    "machine-state": 3, "counting": 3, "cycle-timing": 3, "quality-limits": 1,
    "process-value": 2, "identification": 1, "alerting": 2, "energy": 1, "unclassified": 0,
}

# ── multilingual tags ───────────────────────────────────────────────────────
# The estate spans plants in three regions, and tags arrive in the plant's
# language. All of these terms were found in the flow corpus or are the standard
# shop-floor term in a plant language. canonical=None means "signals a family,
# not a specific name" — the analyst still has to choose.
TERMS: dict[str, tuple[str, str, str | None]] = {
    # term (folded, lowercase)      language        canonical hint
    # --- German (Northeim, Waltershausen, Karben, Korbach, Hannover) --------
    "ruestzeit":       ("German", "SetupTime"), "ruestmonitor": ("German", None),
    "ruestvorgang":    ("German", None),        "ruesten":      ("German", "MachineSetup"),
    "stueckzahl":      ("German", "TotalPartCounter"),
    "zykluszeit":      ("German", "CycleTime"), "zyklus":       ("German", "CycleTime"),
    "druck":           ("German", "Pressure"),  "temperatur":   ("German", "Temperature"),
    "heizung":         ("German", "HeatingProgram"),
    "heizungsart":     ("German", "HeatingProgram"),
    "sollwert":        ("German", None),        "istwert":      ("German", None),
    "stoerung":        ("German", "ErrorActive"), "meldung":    ("German", "AlertMessage"),
    "betriebsart":     ("German", "MachineMode"), "zaehler":    ("German", "TotalPartCounter"),
    "geschwindigkeit": ("German", "StandardSpeed"),
    "extrusionslinie": ("German", None),        "kessel":       ("German", None),
    "werkzeug":        ("German", "ToolId"),
    # --- Spanish (Monterrey, Delicias, Tlalnepantla, Montemorelos, S.L.P.) --
    "pza":             ("Spanish", "TotalPartCounter"),
    "pieza":           ("Spanish", "TotalPartCounter"),
    "piezas":          ("Spanish", "TotalPartCounter"),
    "contador":        ("Spanish", "TotalPartCounter"),
    "ciclo":           ("Spanish", "CycleTime"),  "tiempo":     ("Spanish", None),
    "presion":         ("Spanish", "Pressure"),   "temperatura":("Spanish", "Temperature"),
    "velocidad":       ("Spanish", "StandardSpeed"),
    "alarma":          ("Spanish", "AlertMessage"), "falla":    ("Spanish", "ErrorActive"),
    "molde":           ("Spanish", "ToolId"),     "turno":      ("Spanish", None),
    "descarga":        ("Spanish", None),         "succion":    ("Spanish", None),
    # --- Portuguese (Ponta Grossa) -----------------------------------------
    "peca":            ("Portuguese", "TotalPartCounter"),
    "contagem":        ("Portuguese", "TotalPartCounter"),
    "pressao":         ("Portuguese", "Pressure"),
    "temperatura_pt":  ("Portuguese", "Temperature"),
    "velocidade":      ("Portuguese", "StandardSpeed"),
    "molde_pt":        ("Portuguese", "ToolId"),
    # --- French (Caluire, Rennes, Tanger) -----------------------------------
    "piece":           ("French", "TotalPartCounter"),
    "compteur":        ("French", "TotalPartCounter"),
    "cycle_fr":        ("French", "CycleTime"),
    "pression":        ("French", "Pressure"),
    "temperature_fr":  ("French", "Temperature"),
    "vitesse":         ("French", "StandardSpeed"),
    "defaut":          ("French", "ErrorActive"),
    "moule":           ("French", "ToolId"),
    "consigne":        ("French", None),
    # --- Romanian (Carei, Timisoara) ----------------------------------------
    "piesa":           ("Romanian", "TotalPartCounter"),
    "contor":          ("Romanian", "TotalPartCounter"),
    "presiune":        ("Romanian", "Pressure"),
    "viteza":          ("Romanian", "StandardSpeed"),
    "matrita":         ("Romanian", "ToolId"),
    "defect":          ("Romanian", "ErrorActive"),
    # --- Hungarian (Mako) ----------------------------------------------------
    "darab":           ("Hungarian", "TotalPartCounter"),
    "szamlalo":        ("Hungarian", "TotalPartCounter"),
    "nyomas":          ("Hungarian", "Pressure"),
    "homerseklet":     ("Hungarian", "Temperature"),
    # --- Slovak / Czech (Dolne Vestenice, Ostrava) ---------------------------
    "pocitadlo":       ("Slovak/Czech", "TotalPartCounter"),
    "tlak":            ("Slovak/Czech", "Pressure"),
    "teplota":         ("Slovak/Czech", "Temperature"),
    "porucha":         ("Slovak/Czech", "ErrorActive"),
    # --- Serbian latin (Subotica) -------------------------------------------
    "brojac":          ("Serbian", "TotalPartCounter"),
    "pritisak":        ("Serbian", "Pressure"),
    "temperatura_sr":  ("Serbian", "Temperature"),
}
# Chinese (Changshu, Qingdao, Changchun) — matched on the characters themselves.
CJK_TERMS: dict[str, tuple[str, str | None]] = {
    "设定值": ("Chinese", None),            # setpoint value -> the _sv modifier
    "存储":   ("Chinese", None),            # store / storage
    "流程":   ("Chinese", None),            # process / flow
    "计数":   ("Chinese", "TotalPartCounter"),
    "计数器": ("Chinese", "TotalPartCounter"),
    "周期":   ("Chinese", "CycleTime"),
    "压力":   ("Chinese", "Pressure"),
    "温度":   ("Chinese", "Temperature"),
    "速度":   ("Chinese", "StandardSpeed"),
    "状态":   ("Chinese", "MachineStatus"),
    "报警":   ("Chinese", "AlertMessage"),
    "故障":   ("Chinese", "ErrorActive"),
    "模具":   ("Chinese", "ToolId"),
    "班次":   ("Chinese", None),            # shift
}

# Tokens that prove a label is already English — stops "Temperature" being read
# as the German "Temperatur", and similar near-collisions.
ENGLISH_STOP = {
    "temperature", "pressure", "speed", "counter", "count", "cycle", "time",
    "status", "state", "mode", "tool", "part", "number", "alert", "alarm",
    "error", "setpoint", "value", "shift", "piece", "pieces", "process",
}

# Expand the dictionary with the accent-folded spelling of every term, because
# both Rüstzeit and Rustzeit occur in practice, and strip the _xx disambiguators.
def _build_lookup() -> dict[str, tuple[str, str | None]]:
    out: dict[str, tuple[str, str | None]] = {}
    for term, val in TERMS.items():
        base = term.split("_")[0]
        prev = out.get(base)
        if prev and prev[0] != val[0] and "/" not in prev[0]:
            # two languages spell it the same; name both rather than pick one
            val = (f"{prev[0]}/{val[0]}", prev[1] or val[1])
        elif prev:
            val = prev
        out[base] = val
        folded = (base.replace("ue", "u").replace("oe", "o")
                      .replace("ae", "a").replace("ss", "s"))
        if folded != base and len(folded) >= 4:
            out.setdefault(folded, out[base])
    return out


SCRIPTS = [("chinese", r"[一-鿿]"), ("cyrillic", r"[Ѐ-ӿ]"),
           ("japanese", r"[぀-ヿ]"), ("korean", r"[가-힯]"),
           ("greek", r"[Ͱ-Ͽ]"), ("arabic", r"[؀-ۿ]")]


_TERM_LOOKUP = _build_lookup()


def detect_script(label: str) -> str:
    for name, pat in SCRIPTS:
        if re.search(pat, label or ""):
            return name
    return "latin"


UMLAUT = str.maketrans({"ü": "ue", "ö": "oe", "ä": "ae", "ß": "ss",
                        "Ü": "ue", "Ö": "oe", "Ä": "ae"})


def tokens(label: str) -> set[str]:
    """Split a label into comparable word tokens.

    camelCase, snake_case, spaces and digits all separate. German umlauts are
    expanded (Rüstzeit -> ruestzeit) as well as accent-folded (rustzeit), because
    both spellings occur.
    """
    s = clean(label)
    out: set[str] = set()
    for variant in (fold(s), s.translate(UMLAUT)):
        spaced = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", variant)
        out |= {w for w in re.split(r"[^a-z]+", spaced.lower()) if w}
    return out


def translate_hint(label: str):
    """Return (term, language, canonical|None) if the label carries a local term.

    Returns None for anything already canonical or a known English variant — an
    English name must never be reported as a foreign one.
    """
    label = clean(label)
    if not label:
        return None
    for term, (lang, canon) in CJK_TERMS.items():
        if term in label:
            return term, lang, canon
    n = norm(label)
    if n in CANON_LOWER or n in VARIANT_OF:
        return None
    toks = tokens(label)
    for term, (lang, canon) in _TERM_LOOKUP.items():
        if term in toks and term not in ENGLISH_STOP:
            return term, lang, canon
    # The English guard applies only below: substring matching is what would read
    # the English "Temperature" as the German "Temperatur".
    if toks & ENGLISH_STOP:
        return None
    # Compounding languages (German, Hungarian) glue terms together:
    # Darabszamlalo, Zykluszeitmessung. Substring match, long terms only.
    flat = fold(clean(label)).lower().replace(" ", "")
    for term, (lang, canon) in _TERM_LOOKUP.items():
        if len(term) >= 5 and term in flat:
            return term, lang, canon
    return None


SEV_ORDER = {"BLOCKER": 0, "WARN": 1, "INFO": 2}
ICON = {"BLOCKER": "✗", "WARN": "!", "INFO": "·"}


def clean(s: str) -> str:
    """Unicode-normalise and strip invisible characters before anything else.

    Zero-width spaces and non-breaking spaces occur in the estate's own text and
    make two visually identical names compare unequal.
    """
    s = unicodedata.normalize("NFC", s or "")
    return "".join(ch for ch in s if unicodedata.category(ch) != "Cf").replace("\u00a0", " ").strip()


def fold(s: str) -> str:
    """Accent-fold for matching only: Rüstzeit -> rustzeit. Never for display."""
    d = unicodedata.normalize("NFD", s or "")
    return "".join(ch for ch in d if unicodedata.category(ch) != "Mn")


def norm(s: str) -> str:
    """Compare names ignoring case, spaces, underscores, hyphens and accents."""
    return re.sub(r"[\s_\-]+", "", fold(clean(s))).lower()


class Report:
    def __init__(self, name):
        self.name = name
        self.findings = []

    def add(self, sev, check, msg, fix=""):
        self.findings.append({"severity": sev, "check": check, "message": msg, "fix": fix})

    def sorted(self):
        return sorted(self.findings, key=lambda f: (SEV_ORDER[f["severity"]], f["check"]))

    def counts(self):
        return Counter(f["severity"] for f in self.findings)


def cell(row: dict, *names: str) -> str:
    """First non-empty value among `names`, case-insensitively.

    A tag export names its columns whatever the exporting tool felt like — `label`, `Label`,
    `Name`, `TagName`. Three call sites here used to read three different key sets, so a
    `uuid,Label` CSV analysed clean and then reported every signal as unnamed.
    """
    lower = {str(k).strip().lower(): v for k, v in row.items() if k is not None}
    for n in names:
        v = lower.get(n.lower())
        if v is not None and str(v).strip():
            return str(v)
    return ""


def load(path: str) -> list[dict]:
    if path.lower().endswith(".csv"):
        with open(path, encoding="utf-8-sig", newline="") as fh:
            return [dict(r) for r in csv.DictReader(fh)]
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if isinstance(data, dict):
        for key in ("data_points", "dataPoints", "items", "data"):
            if isinstance(data.get(key), list):
                return data[key]
        raise ValueError("JSON object carries no data-point array")
    if not isinstance(data, list):
        raise ValueError("expected a JSON array of data points")
    return data


def analyze(path: str, capability: str | None = None) -> Report:
    rows = load(path)
    rep = Report(path)
    if not rows:
        rep.add("BLOCKER", "empty", "No data points in the input.")
        return rep

    labels, uuids = [], []
    for r in rows:
        label = clean(cell(r, "label", "name", "tagname", "tag", "signal"))
        uuid = cell(r, "uuid", "id", "datapointid").strip()
        labels.append(label)
        uuids.append(uuid)

    # ── identity ────────────────────────────────────────────────────────────
    missing_uuid = sum(1 for u in uuids if not u)
    if missing_uuid:
        rep.add("BLOCKER", "missing-uuid",
                f"{missing_uuid} data point(s) carry no uuid. The uuid is the join key — "
                "a point without one cannot be filtered for in any flow.")
    dup_uuid = [u for u, c in Counter(u for u in uuids if u).items() if c > 1]
    if dup_uuid:
        rep.add("BLOCKER", "duplicate-uuid",
                f"{len(dup_uuid)} uuid(s) appear more than once: {', '.join(dup_uuid[:3])}")

    unnamed = sum(1 for l in labels if not l)
    if unnamed:
        rep.add("BLOCKER", "unnamed-point",
                f"{unnamed} data point(s) carry no label. An unnamed point is unusable — "
                "nothing downstream can say what it is.",
                fix="Name it from the canonical vocabulary before anyone builds on it.")

    # ── duplicate and colliding names ───────────────────────────────────────
    by_norm = defaultdict(list)
    for l in labels:
        if l:
            by_norm[norm(l)].append(l)
    for key, group in by_norm.items():
        if len(group) > 1 and len(set(group)) > 1:
            rep.add("BLOCKER", "name-collision",
                    f"Names differing only in case/spacing: {', '.join(sorted(set(group)))}",
                    fix="Pick one spelling. A consumer matching on the label will silently "
                        "miss the others.")
        elif len(group) > 1:
            rep.add("WARN", "duplicate-name",
                    f"'{group[0]}' appears {len(group)} times on the same machine.",
                    fix="Qualify each one (zone, axis, position) or merge them.")

    # ── conformance to the canonical vocabulary ─────────────────────────────
    unknown, variants = [], []
    for l in labels:
        if not l:
            continue
        n = norm(l)
        if n in CANON_LOWER:
            continue
        if n in VARIANT_OF:
            variants.append((l, VARIANT_OF[n]))
        else:
            unknown.append(l)

    for bad, good in variants:
        rep.add("WARN", "non-canonical-name",
                f"'{bad}' is a known variant of '{good}'.",
                fix=f"Rename to '{good}'. The estate carries many distinct signal names for "
                    "a far smaller set of concepts — machine state alone has many — and that "
                    "variance is why a second plant cannot take the first plant's solution.")

    raw = [l for l in unknown if RAW_TAG.match(l) or ADDRESS_LIKE.match(l)]
    for l in raw[:10]:
        rep.add("BLOCKER", "raw-plc-tag",
                f"'{l}' is a PLC address or raw tag name, not a signal name.",
                fix="Give it a name from the data model. A tag named for its data-block "
                    "address is a tag no other plant can match.")

    for l in unknown:
        low = l.lower()
        for typo, good in TYPO_HINTS.items():
            # "temperatur" is a substring of the correct "temperature", so a compound like
            # HeadTemperature matched the typo hint. If the right spelling is already there,
            # there is no typo.
            if typo in low and good.lower() not in low:
                rep.add("WARN", "likely-typo",
                        f"'{l}' looks like a misspelling of '{good}'.",
                        fix="A typo in a signal name propagates into every flow, topic and "
                            "dashboard that consumes it. Fix it at the source, and note that "
                            "renaming a live point is a breaking change.")
                break

    plain_unknown = [l for l in unknown if l not in raw]
    if plain_unknown:
        rep.add("INFO", "outside-catalogue",
                f"{len(plain_unknown)} name(s) are not in the canonical vocabulary: "
                + ", ".join(sorted(plain_unknown)[:8])
                + ("…" if len(plain_unknown) > 8 else ""),
                fix="Genuinely machine-specific signals are fine. But check first — the "
                    "catalogue has many observed names for a much smaller set of concepts.")

    # ── language ────────────────────────────────────────────────────────────
    langs = Counter()
    for l in labels:
        if not l:
            continue
        script = detect_script(l)
        if script != "latin":
            langs[script] += 1
        hit = translate_hint(l)
        if hit:
            term, lang, canon = hit
            sev = "WARN" if canon else "INFO"
            rep.add(sev, "local-language-name",
                    f"'{l}' contains {lang} term '{term}'"
                    + (f" — likely '{canon}'." if canon else "."),
                    fix=("Canonical names are English. Keep the local name as an alias in the "
                         "report and Machine CV, but the data-point label carries the canonical "
                         "name. Confirm the reading with the plant before renaming — never "
                         "machine-translate a signal name and use it directly."))
    for script, n in langs.items():
        rep.add("WARN", "non-latin-script",
                f"{n} label(s) in {script} script.",
                fix="Non-Latin labels do not survive every downstream consumer, and cannot be "
                    "matched against the canonical vocabulary. Transliterate and translate with "
                    "the plant, then record the original as an alias.")
    mixed = [l for l in labels
             if l and re.search(r"[A-Za-z]", l) and detect_script(l) != "latin"]
    if mixed:
        rep.add("BLOCKER", "mixed-script-name",
                f"{len(mixed)} label(s) mix scripts: " + ", ".join(mixed[:3]),
                fix="A mixed-script name is unmatchable and often a copy-paste artefact.")

    # ── capability coverage ─────────────────────────────────────────────────
    if capability:
        req = CAPABILITY_REQUIREMENTS.get(capability)
        if req is None:
            rep.add("INFO", "unknown-capability",
                    f"No requirement set for '{capability}'. Known: "
                    + ", ".join(sorted(CAPABILITY_REQUIREMENTS)))
        else:
            present = {norm(l) for l in labels if l}
            present |= {norm(VARIANT_OF[norm(l)]) for l in labels if norm(l) in VARIANT_OF}
            missing = [s for s in req if norm(s) not in present]
            if missing:
                rep.add("BLOCKER", "capability-gap",
                        f"'{capability}' needs {', '.join(req)}; missing: "
                        + ", ".join(missing),
                        fix="Until these exist the use case cannot be built to the standard. "
                            "Either the PLC does not expose them, or they are not configured "
                            "on the edge platform — different problems, different owners.")
            else:
                rep.add("INFO", "capability-covered",
                        f"'{capability}' has every signal it requires.")

    # ── scale ───────────────────────────────────────────────────────────────
    rep.add("INFO", "summary",
            f"{len(rows)} data points · {len(set(l for l in labels if l))} distinct names · "
            f"{len([l for l in labels if norm(l) in CANON_LOWER])} canonical · "
            f"{len(variants)} variants · {len(plain_unknown)} outside the catalogue")
    return rep


def classify(label: str) -> tuple[str, bool]:
    """Return (functional area, is_setpoint) for a signal name."""
    if not label:
        return "unclassified", False
    if RAW_TAG.match(label) or ADDRESS_LIKE.match(label):
        return "raw-tag", False
    setpoint = bool(SETPOINT.search(label))
    for area, pat in AREA_PATTERNS:
        if re.search(pat, label, re.I):
            return area, setpoint
    return "unclassified", setpoint


def importance(area: str, canonical: bool) -> int:
    """Coarse rank: coverage x4 + demand-band x3 + a bonus for being canonical."""
    cov = AREA_COVERAGE.get(area, 0) * 4
    band = AREA_DEMAND.get(area, 0)
    return cov + band * 3 + (2 if canonical else 0)


def cluster_report(rows: list[dict]) -> None:
    """Print the functional-area clustering and the standardize-first order."""
    buckets = defaultdict(list)
    for r in rows:
        label = clean(cell(r, "label", "name", "tagname", "tag", "signal"))
        area, sp = classify(label)
        buckets[area].append((label, sp, norm(label) in CANON_LOWER))

    ranked = sorted(
        buckets.items(),
        key=lambda kv: -importance(kv[0], any(c for _, _, c in kv[1])),
    )
    print("\n--- functional areas (standardize top-down) ---")
    for area, items in ranked:
        canon = sum(1 for _, _, c in items if c)
        sp = sum(1 for _, s, _ in items if s)
        score = importance(area, canon > 0)
        flag = "  ← BLOCKER: name these" if area == "raw-tag" else ""
        print(f"  [{score:3d}] {area:15s} {len(items):3d} signal(s), "
              f"{canon} canonical, {sp} setpoint{flag}")
        for label, s, c in sorted(items)[:6]:
            mark = "*" if c else ("~" if s else " ")
            print(f"          {mark} {label}")
        if len(items) > 6:
            print(f"            … and {len(items)-6} more")
    print("        * canonical   ~ setpoint")
    print("\n  Score = capability coverage x4 + consumer-demand band x3 + canonical bonus.")
    print("  Ranking is a starting point: business_process and targets are populated on only")
    print("  part of the use cases, so a low score means unknown demand, not no demand.")


ACTION = {"canonical": "use", "variant": "rename", "raw": "name it — BLOCKER",
          "unknown": "confirm or drop"}


def emit_report(path: str, rows: list[dict], findings: list[dict], capability: str | None) -> None:
    """Write the machine-derivable half of the signal analysis report.

    Sections a tool cannot know — how the machine works, which sources were used,
    the standard mapping, owners and dates — are emitted as ⟨…⟩ placeholders to be
    filled from the machine context. See references/machine-context.md and
    assets/signal-analysis-report.md.
    """
    print("# Signal Analysis — ⟨Machine⟩ ⟨(EQ id)⟩\n")
    print("| | |\n|---|---|")
    print("| **Plant** | ⟨plant⟩ |")
    print("| **Machine** | ⟨name⟩ ⟨(EQ id)⟩ · ⟨vendor⟩ ⟨PLC model⟩ |")
    print("| **Process group** | ⟨group⟩ · family ⟨Rubber / Plastic / Metal / Assembly⟩ |")
    print(f"| **Capability in scope** | {capability or '⟨capability, or inventory only⟩'} |")
    print("| **Analyst / date** | ⟨name⟩ · ⟨date⟩ |")
    blockers = sum(1 for f in findings if f["severity"] == "BLOCKER")
    verdict = "gaps block delivery" if blockers else "ready — confirm context sections"
    print(f"| **Overall verdict** | {verdict} |")
    print(f"| **Input** | `{path}` — {len(rows)} data points |")

    print("\n---\n\n## 1 · How the machine works\n")
    print("⟨Three or four sentences: what it makes, what one cycle is, where it waits, and")
    print("what makes a part good. If this cannot be written, the context is not yet")
    print("sufficient and everything below is a guess.⟩\n")
    print("**Cycle boundary.** ⟨what starts and ends a cycle, and which signal marks each⟩  ")
    print("**Wait states.** ⟨where it waits, and on what⟩  ")
    print("**Good-part definition.** ⟨what makes a part countable, and at which station⟩")

    print("\n## 2 · Sources used\n")
    print("| Source | Obtained | Contributed | Confidence |\n|---|---|---|---|")
    print(f"| Data-point list (`{path}`) | yes | the inventory below | Verified for existence |")
    for s, c in [("PLC program ⟨version⟩", "High"), ("Tag / symbol export", "High for existence, low for meaning"),
                 ("Sequence / flow chart", "Medium"), ("Layout", "Medium"),
                 ("Machine handbook", "Medium"), ("HMI observation", "Medium — high for importance"),
                 ("Proven instance at ⟨plant⟩", "Medium"), ("Operator / setter", "Low until confirmed")]:
        print(f"| {s} | ⟨yes/no⟩ | ⟨what it gave⟩ | {c} |")
    print("\n**Context situation:** ⟨full context · tag export only · handbook only · "
          "nothing but the machine · adopting a proven instance⟩")

    print("\n## 3 · Signal inventory\n")
    print("| Candidate (as found) | Lang | Canonical name | Area | Dir | Exists? | Unit | Collection | Action |")
    print("|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        label = clean(cell(r, "label", "name", "tagname", "tag", "signal"))
        uuid = cell(r, "uuid", "id", "datapointid").strip()
        area, sp = classify(label)
        n = norm(label)
        if n in CANON_LOWER:
            canon, kind = CANON_LOWER[n], "canonical"
        elif n in VARIANT_OF:
            canon, kind = VARIANT_OF[n], "variant"
        elif area == "raw-tag":
            canon, kind = "⟨name it⟩", "raw"
        else:
            canon, kind = "⟨confirm⟩", "unknown"
        exists = f"yes `{uuid[:8]}`" if uuid else "**no uuid**"
        marks = area + ("+setpoint" if sp else "")
        hint = translate_hint(label)
        lang = detect_script(label)
        lang = (hint[1] if hint else ("en" if lang == "latin" else lang))
        print(f"| `{label or '⟨unnamed⟩'}` | {lang} | {canon} | {marks} | in | {exists} | ⟨unit⟩ | "
              f"⟨transition / sample⟩ | {ACTION[kind]} |")
    print("\n**Legend — Action.** `use` already canonical · `rename` variant → canonical · "
          "`name it` raw PLC tag, blocker · `confirm or drop` outside the catalogue.")
    print("\n⟨Add a row per derived **output** signal this machine should publish, direction "
          "`out`, action `register on the edge platform`.⟩")

    print("\n## 4 · Functional areas and priority\n")
    print("```")
    cluster_report(rows)
    print("```")

    print("\n## 5 · Standard and data model\n")
    print("| | |\n|---|---|")
    print("| Cluster | ⟨C01…C12⟩ |")
    print("| Standard KPIs required | ⟨from the cluster KPI set — see references/standards.md⟩ |")
    print("| Public data model available | ⟨EUROMAP 77/83/84 · OPC UA for Machinery · PackML · none⟩ |")
    print("| Machine already exposes it? | ⟨yes — the integration route changes / no / not checked⟩ |")
    print("| State model | ⟨PackML mapping, or the raw code table with meanings⟩ |")
    print("| Deltas from the standard | ⟨only what this machine does differently⟩ |")

    print("\n## 6 · Capability coverage\n")
    if capability:
        req = CAPABILITY_REQUIREMENTS.get(capability, [])
        present = {norm(l) for l in (cell(r, "label", "name", "tagname", "tag", "signal") for r in rows)}
        present |= {norm(VARIANT_OF[p]) for p in list(present) if p in VARIANT_OF}
        miss = [s for s in req if norm(s) not in present]
        print("| Capability | Requires | Missing | Verdict |\n|---|---|---|---|")
        print(f"| {capability} | {', '.join(req) or '⟨unknown⟩'} | "
              f"{', '.join(miss) or '—'} | {'blocked' if miss else 'buildable'} |")
        if miss:
            print("\n| Missing signal | Cause | Owner |\n|---|---|---|")
            for s in miss:
                print(f"| {s} | ⟨PLC does not expose it / not configured on the edge platform / "
                      "no sensor exists⟩ | ⟨engineering / integration / investment⟩ |")
    else:
        print("⟨Run again with `--capability <name>` to fill this, or complete by hand.⟩")

    print("\n## 7 · Findings\n")
    if not findings:
        print("None.")
    else:
        print("| Severity | Finding | Detail | Fix |\n|---|---|---|---|")
        for f in sorted(findings, key=lambda x: SEV_ORDER[x["severity"]]):
            msg = f["message"].replace("|", "\\|").replace("\n", " ")
            fix = (f["fix"] or "—").replace("|", "\\|").replace("\n", " ")
            print(f"| {f['severity']} | `{f['check']}` | {msg} | {fix} |")

    print("\n## 8 · Recommended actions\n")
    print("| # | Action | Owner | Depends on | By |\n|---|---|---|---|---|")
    i = 0
    for f in sorted(findings, key=lambda x: SEV_ORDER[x["severity"]]):
        if f["severity"] == "INFO":
            continue
        i += 1
        print(f"| {i} | {f['message'].split('.')[0]} | ⟨owner⟩ | — | ⟨date⟩ |")
    if not i:
        print("| 1 | ⟨confirm the context sections above⟩ | ⟨owner⟩ | — | ⟨date⟩ |")
    print("\n**Renaming a live signal is a breaking change**, not a tidy-up. Any rename above "
          "needs its consumers listed and a migration, or the deviation recorded instead.")

    print("\n## 9 · Open questions\n\n- ⟨what could not be established, and who can answer it⟩")
    print("\n## 10 · Feeds\n")
    print("`od-requirements-breakdown` §5 Tags of Interest · `od-equipment-integration` (guidance route) · "
          "`od-node-red-flow-builder` flow config · the Machine CV")


CAPABILITIES = ("oee", "downtime", "cycle-time", "spc", "energy", "quality",
                "andon", "traceability", "maintenance", "recipe", "analytics")


def main(argv):
    import argparse
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--capability", type=str.lower)
    ap.add_argument("--cluster", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("-h", "--help", action="store_true")
    try:
        ns = ap.parse_args(argv[1:])
    except SystemExit:
        return 2
    if ns.help or not ns.files:
        print(__doc__)
        return 0
    args, as_json, do_cluster, do_report, cap = (
        ns.files, ns.json, ns.cluster, ns.report, ns.capability)
    if cap and cap not in CAPABILITIES:
        print(f"unknown capability '{cap}' — one of: {', '.join(CAPABILITIES)}", file=sys.stderr)
        return 2
    worst, out = 0, []
    for path in args:
        try:
            rep = analyze(path, cap)
        except Exception as exc:  # noqa: BLE001
            print(f"{path}: could not analyze — {exc}", file=sys.stderr)
            worst = max(worst, 1)
            continue
        c = rep.counts()
        worst = max(worst, 2 if c["BLOCKER"] else 1 if c["WARN"] else 0)
        if as_json:
            out.append({"file": path, "capability": cap, "findings": rep.sorted()})
            continue
        if do_report:
            emit_report(path, load(path), rep.sorted(), cap)
            continue
        print(f"\n=== {rep.name}" + (f"  [capability: {cap}]" if cap else ""))
        for f in rep.sorted():
            print(f"  {ICON[f['severity']]} {f['severity']:7s} {f['check']}")
            print(f"      {f['message']}")
            if f["fix"]:
                print(f"      → {f['fix']}")
        print(f"    {c['BLOCKER']} blocker · {c['WARN']} warn · {c['INFO']} info")
        if do_cluster:
            try:
                cluster_report(load(path))
            except Exception as exc:  # noqa: BLE001
                print(f"    clustering failed: {exc}", file=sys.stderr)
    if as_json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    return worst



def _run(argv: list[str]) -> int:
    """Wrap main so piping into `head` or `less` exits quietly instead of tracebacking."""
    try:
        return main(argv)
    except BrokenPipeError:
        try:
            sys.stdout.close()
        except BrokenPipeError:
            pass
        return 0
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(_run(sys.argv))
