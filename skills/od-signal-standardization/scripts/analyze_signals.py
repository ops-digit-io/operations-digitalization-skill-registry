#!/usr/bin/env python3
"""Analyse a machine's data-point list for standardization problems.

    python3 analyze_signals.py POINTS.json [--capability oee] [--json]
    python3 analyze_signals.py POINTS.csv  --capability cycle-time

Input is the data-point list for one machine or datatron — the shape the IIoT edge
platform returns from `/api/datatrons/{id}/data_points`, or a CSV with `uuid,label`
columns. Any JSON array of objects carrying `uuid` and `label` works.

What it checks, and why each one is here: every rule below was derived from the
260 distinct signal names in use across the flow estate, where the same concept is
named up to eight different ways. That variance is what stops one plant's solution
being taken by the next.

Exit code: 2 if any BLOCKER, 1 if any WARN, 0 otherwise.
"""

from __future__ import annotations

import csv
import json
import re
import sys
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

SEV_ORDER = {"BLOCKER": 0, "WARN": 1, "INFO": 2}
ICON = {"BLOCKER": "✗", "WARN": "!", "INFO": "·"}


def norm(s: str) -> str:
    """Compare names ignoring case, spaces, underscores and hyphens."""
    return re.sub(r"[\s_\-]+", "", (s or "")).lower()


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
        label = (r.get("label") or r.get("name") or r.get("Label") or "").strip()
        uuid = (r.get("uuid") or r.get("id") or r.get("UUID") or "").strip()
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
                fix=f"Rename to '{good}'. The estate carries 260 distinct signal names for "
                    "a far smaller set of concepts — eight for machine state alone — and that "
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
            if typo in low:
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
                    "catalogue has 260 observed names for a much smaller set of concepts.")

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


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    as_json = "--json" in argv
    cap = None
    if "--capability" in argv:
        i = argv.index("--capability")
        if i + 1 < len(argv):
            cap = argv[i + 1].lower()
            if cap in args:
                args.remove(cap)
    if not args:
        print(__doc__)
        return 0
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
        print(f"\n=== {rep.name}" + (f"  [capability: {cap}]" if cap else ""))
        for f in rep.sorted():
            print(f"  {ICON[f['severity']]} {f['severity']:7s} {f['check']}")
            print(f"      {f['message']}")
            if f["fix"]:
                print(f"      → {f['fix']}")
        print(f"    {c['BLOCKER']} blocker · {c['WARN']} warn · {c['INFO']} info")
    if as_json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    return worst


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
