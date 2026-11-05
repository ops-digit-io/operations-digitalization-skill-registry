#!/usr/bin/env python3
"""Walk the six availability steps against the real sources, and say which step failed.

    python3 check_availability.py --plant Mako --signals TotalPartCounter,MachineState
    python3 check_availability.py --plant Karben --machine "Lean Cell" --json
    python3 check_availability.py --plant Qingdao --report

The point of this script is not to say "available" or "not available". It is to say **which
of the six steps the request dies at**, because the failures at steps 2, 4 and 5 look
identical from a dashboard and are entirely different problems with different owners.

Sources, and what each can actually answer:

  Machine List                   steps 1-3: does the plant have the machine, is it
                                 integrated, by which method
  Connector Overview            step 3: is there a connector for that PLC and protocol
  Node-RED corpus               step 4: which signal names are demonstrably flowing at
                                 that plant today
  -- nothing here --             step 5: fitness for use. No source in the bundle carries
                                 granularity, freshness or completeness per signal. The
                                 script says so rather than implying a verdict.

Exit code: 2 if any step BLOCKS, 1 if any step is unproven, 0 if all six are answered.
"""

from __future__ import annotations

import argparse
import csv
import json
import pathlib
import re
import sys
import unicodedata
from collections import Counter, defaultdict

SEV = {"BLOCKER": 0, "WARN": 1, "INFO": 2}
ICON = {"BLOCKER": "✗", "WARN": "!", "INFO": "·"}

# How a Node-RED instance code maps to a plant, and how that mapping was established.
# `topic` - proved by a CT/... MQTT topic segment inside the flows.
# `machines` - proved by machine names shared with that plant's Machine List rows.
# `prefix` - the code is the start of the plant name.
# `abbreviation` - a consonant abbreviation with no corroborating evidence in the bundle.
# Anything not listed here is reported as unmapped rather than guessed at.
INSTANCE_PLANT: dict[str, tuple[str, str]] = {
    "cal":  ("Caluire", "prefix"),
    "car":  ("Carei", "prefix"),
    "ccn":  ("Changchun", "abbreviation"),
    "cshz": ("Changshu", "topic"),
    "del":  ("Delicias", "prefix"),
    "dol":  ("DolneVestenice", "prefix"),
    "krb":  ("Karben", "machines"),
    "mak":  ("Mako", "machines"),
    "mty":  ("Monterrey", "abbreviation"),
    "pogz": ("PontaGrossa", "machines"),
    "qda":  ("Qingdao", "topic"),
    "som":  ("Somersworth", "machines"),
    "spr":  ("SunPrairie", "topic"),
    "sub":  ("Subotica", "machines"),
    "tsaz": ("Timisoara", "machines"),
    "vac":  ("Vac", "prefix"),
    "wth1": ("Waltershausen", "abbreviation"),
    "wth2": ("Waltershausen", "abbreviation"),
    "wth3": ("Waltershausen", "abbreviation"),
    "wth4": ("Waltershausen", "abbreviation"),
}
NOT_A_PLANT = {"mpee"}          # the department's own test instance

# A PLC vendor or protocol to the connector that speaks it. Names are the Connector
# Overview's own labels; the match is on `input_protocol` and `vendor` where populated.
# SFT-SIMATIC S7-Connector is deliberately absent: it is Productive and DO NOT USE, because
# it does not support cyber-security compliant communication to the PLC.
VENDOR_HINT = {
    "siemens": ("DTQ-S7-Connector", "DTQ-TIA-Connector", "DTQ-S7-NET-Connector"),
    "sinumerik": ("DTQ-SINUMERIK-Connector",),
    "simotion": ("DTQ-SIMOTIOND-Connectors",),
    "rockwell": ("DTQ-ALLENBRADLEY-ROCKWELL-Connector",),
    "allen bradley": ("DTQ-ALLENBRADLEY-ROCKWELL-Connector",),
    "beckhoff": ("DTQ-Beckhoff-Connector",),
    "b&r": ("DTQ-B&R-Connector",),
    "bachmann": ("DTQ-Bachmann-Connector",),
    "engel": ("DTQ-Engel EMI-Connector",),
    "omron": ("DTQ-OMRON FINS-Connector",),
    "keyence": ("DTQ-KEYENCECAM-Connector", "DTQ-RS232-Connector"),
    "piovan": ("DTQ-PIOVAN-Connector",),
    "optris": ("DTQ-IROPTRIS-Connector",),
    "zwick": ("DTQ-ZWICK-Connector",),
}
PROTOCOL_HINT = {
    "modbus": ("DTQ-MODBUS-Connector",),
    "opc": ("DTQ-OPCUA-Connector", "SFT-OPC-Suite"),
    "profinet": ("DTQ-S7-Connector", "DTQ-TIA-Connector"),
    "ethercat": ("DTQ-EthercatIO-Connector",),
    "rs232": ("DTQ-RS232-Connector",),
}

# The OPC UA direct connector reaches any OPC UA server — a machine's own embedded one, or
# the Central Aggregation Server — so it is the standing fallback wherever a vendor's native
# connector does not exist. B&R and Bachmann are the live proof: both native connectors are
# Idea/NOT AVAILABLE, and machines across the two families may be integrated anyway, mostly
# recorded as `Central OPCUA Aggregation Server`.
OPCUA_DIRECT = "DTQ-OPCUA-Connector"
OPCUA_FALLBACK_VENDORS = ("b&r", "bachmann", "engel")


def norm(s: str) -> str:
    d = unicodedata.normalize("NFD", s or "")
    d = "".join(c for c in d if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "", d.lower())


class Finding(dict):
    pass


class Verdict:
    def __init__(self) -> None:
        self.steps: list[dict] = []

    def step(self, n: int, name: str, severity: str, message: str, fix: str = "",
             evidence: str = "") -> None:
        self.steps.append({"step": n, "name": name, "severity": severity,
                           "message": message, "fix": fix, "evidence": evidence})

    def counts(self) -> Counter:
        return Counter(s["severity"] for s in self.steps)

    def exit_code(self) -> int:
        c = self.counts()
        return 2 if c["BLOCKER"] else 1 if c["WARN"] else 0


def load_nodes(kg: pathlib.Path) -> list[dict]:
    path = kg / "_knowledge/90-Sources/generated/kg_nodes.csv"
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found. Pass --kg <path to the ops-knowledge-graph checkout>.")
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def flow_signals(kg: pathlib.Path) -> dict[str, set[str]]:
    """Signal names demonstrably present per plant, mined from the flow corpus.

    A name appearing in a deployed flow is the strongest evidence in the bundle that the
    signal exists at that plant — stronger than the Machine List, which says a machine is
    integrated without saying which of its points are published.
    """
    docs = kg / "_knowledge/node-red-auto-docs/docs"
    out: dict[str, set[str]] = defaultdict(set)
    if not docs.exists():
        return out
    for d in sorted(docs.iterdir()):
        if not d.is_dir():
            continue
        m = re.match(r"ct-oesl-([a-z0-9]+)-nodered", d.name)
        if not m or m.group(1) in NOT_A_PLANT:
            continue
        mapped = INSTANCE_PLANT.get(m.group(1))
        if not mapped:
            out["__unmapped__"].add(d.name)
            continue
        plant = mapped[0]
        for f in d.glob("*.json"):
            try:
                text = f.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            # signal names appear as node names, topic tails and payload keys
            for tok in re.findall(r"[A-Za-z][A-Za-z0-9]{4,40}", text):
                if re.search(r"[a-z][A-Z]", tok) or tok.istitle():
                    out[plant].add(tok)
    return out


def resolve_plant(name: str, nodes: list[dict]) -> tuple[str | None, list[str]]:
    plants = sorted({n["label"] for n in nodes if n["type"] == "Plant"})
    want = norm(name)
    exact = [p for p in plants if norm(p) == want]
    if exact:
        return exact[0], plants
    near = [p for p in plants if want and (want in norm(p) or norm(p).startswith(want))]
    return (near[0] if len(near) == 1 else None), plants


def analyze(kg: pathlib.Path, plant_in: str, machine_q: str | None,
            signals: list[str]) -> tuple[Verdict, dict]:
    v = Verdict()
    nodes = load_nodes(kg)
    plant, plants = resolve_plant(plant_in, nodes)
    ctx: dict = {"plant_input": plant_in, "plant": plant, "signals": signals}

    if not plant:
        v.step(0, "plant", "BLOCKER",
               f"'{plant_in}' is not a plant in the Machine List.",
               fix="One of: " + ", ".join(plants))
        return v, ctx

    machines = [n for n in nodes if n["type"] == "Machine" and n.get("plant") == plant]
    if machine_q:
        q = norm(machine_q)
        machines = [m for m in machines if q in norm(m.get("label", ""))]
    ctx["machine_count"] = len(machines)

    # ── step 1 · does a machine produce it ─────────────────────────────────────
    if not machines:
        v.step(1, "machine exists", "BLOCKER",
               f"No machine at {plant}" + (f" matching '{machine_q}'" if machine_q else "")
               + " in the Machine List.",
               fix="If the machine is real, the Machine List is wrong and that is the first "
                   "fix. If it is not, this is a measurement gap, not a data gap — say so.")
        return v, ctx
    v.step(1, "machine exists", "INFO",
           f"{len(machines)} machine(s) in scope at {plant}.",
           evidence="Machine List")

    # ── step 2 · is it integrated ──────────────────────────────────────────────
    status = Counter((m.get("integration_status") or "").strip() or "«blank»" for m in machines)
    integrated = status.get("INTEGRATED", 0)
    blank = status.get("«blank»", 0)
    ctx["status"] = dict(status)
    if integrated == 0:
        v.step(2, "integrated", "BLOCKER",
               "No machine in scope is INTEGRATED — " + ", ".join(
                   f"{k}: {n}" for k, n in status.most_common()),
               fix="Route to od-equipment-integration (assessment route). This is an integration "
                   "request, not a data request, and it belongs to a different lane.",
               evidence="Machine List integration_status")
    elif blank:
        v.step(2, "integrated", "WARN",
               f"{integrated} of {len(machines)} INTEGRATED, but {blank} row(s) carry no "
               "status at all.",
               fix="A blank status is not 'not integrated' — it is unknown. Count the "
                   "blank rows on the live list; do not read one as a no.",
               evidence="Machine List integration_status")
    else:
        v.step(2, "integrated", "INFO",
               f"{integrated} of {len(machines)} INTEGRATED.",
               evidence="Machine List integration_status")

    # ── step 3 · connector and concept ─────────────────────────────────────────
    conns = {n["label"]: n for n in nodes if n["type"] == "Connector"}
    vendors = Counter((m.get("plc_vendor") or "").strip() for m in machines if m.get("plc_vendor"))
    protos = Counter((m.get("network_protocol") or "").strip() for m in machines if m.get("network_protocol"))
    methods = Counter((m.get("integration_method") or "").strip() for m in machines if m.get("integration_method"))
    ctx["vendors"], ctx["protocols"], ctx["methods"] = dict(vendors), dict(protos), dict(methods)

    def usable(name: str) -> bool:
        c = conns.get(name)
        if not c:
            return False
        return (c.get("utilization") or "").strip().upper() == "USE" and \
               (c.get("status") or "").strip() != "Idea"

    # Protocol hints are a property of the plant's network, not of one vendor, so they are
    # kept apart: mixing them in let a usable Modbus or OPC connector elsewhere on site mask
    # the fact that a vendor's own connector is unavailable.
    proto_hits = sorted({c for proto in protos
                         for key, names in PROTOCOL_HINT.items() if key in proto.lower()
                         for c in names if c in conns})

    covered, uncovered, viaopc = [], [], []
    for vendor, n in vendors.items():
        native = sorted({c for key, names in VENDOR_HINT.items() if key in vendor.lower()
                         for c in names if c in conns})
        if not native:
            uncovered.append((vendor, n, []))
        elif any(usable(h) for h in native):
            covered.append((vendor, n, [h for h in native if usable(h)]))
        elif any(k in vendor.lower() for k in OPCUA_FALLBACK_VENDORS) and usable(OPCUA_DIRECT):
            viaopc.append((vendor, n, native))
        else:
            uncovered.append((vendor, n, native))

    if viaopc:
        v.step(3, "connector", "WARN",
               "; ".join(f"{ven} ({n} machine(s)): native {', '.join(h)} is NOT AVAILABLE"
                         for ven, n, h in viaopc)
               + f" — reachable via {OPCUA_DIRECT} instead.",
               fix="Confirm the machine exposes an OPC UA server, or that it is already on the "
                   "Central Aggregation Server. Do not report this as a connector gap: machines of "
                   "this vendor family may be integrated today without their native connector.",
               evidence="Connector Overview + Machine List integration_method")

    NOT_A_VENDOR = {"s7.schnitt.", "mra", "asi", "pma", "eos"}
    junk = [(ven, n) for ven, n, _ in uncovered if ven.strip().lower() in NOT_A_VENDOR]
    uncovered = [u for u in uncovered if u[0].strip().lower() not in NOT_A_VENDOR]
    if junk:
        v.step(3, "connector", "WARN",
               "plc_vendor holds a non-vendor value on "
               + ", ".join(f"{n} machine(s) ({ven!r})" for ven, n in junk)
               + (" — 'S7.Schnitt.' is an interface note, not a vendor."
                  if any(ven.strip().lower() == "s7.schnitt." for ven, _ in junk)
                  else " — these are not manufacturers."),
               fix="Fix the Machine List row. Until then these machines cannot be matched "
                   "to a connector at all, which reads as a gap that is not one.",
               evidence="Machine List plc_vendor")

    if uncovered:
        unbuilt = [(ven, n, h) for ven, n, h in uncovered if h]
        unknown = [(ven, n) for ven, n, h in uncovered if not h]
        if unbuilt:
            v.step(3, "connector", "BLOCKER",
                   "; ".join(f"{ven} ({n} machine(s)): {', '.join(h)} is not available"
                             for ven, n, h in unbuilt),
                   fix="The connector is on the roadmap, not in the platform. Log it as a "
                       "barrier and route it — do not scope a use case behind it.",
                   evidence="Connector Overview status and utilization")
        if unknown:
            v.step(3, "connector", "BLOCKER",
                   "No connector in the Overview speaks: " + ", ".join(
                       f"{ven} ({n} machine(s))" for ven, n in unknown),
                   fix=f"Ask what the controller exposes before declaring a gap — if it serves "
                       f"OPC UA, {OPCUA_DIRECT} reaches it today. Otherwise this is connector "
                       "development, with long lead times.",
                   evidence="Connector Overview")

    if covered:
        # A connector existing is not one you may use: only those marked USE are, others are
        # NOT AVAILABLE or DO NOT USE. Only usable ones reach this line.
        v.step(3, "connector", "INFO",
               "; ".join(f"{ven} → {', '.join(h[:2])}" for ven, _, h in covered[:4]),
               evidence="Connector Overview")
    site = sorted({c for proto in protos
                   for key, names in PROTOCOL_HINT.items() if key in proto.lower()
                   for c in names if c in conns and usable(c)})
    if site:
        v.step(3, "connector", "INFO",
               "Protocol-level routes available on site: " + ", ".join(site)
               + ". These follow the network, not the vendor.",
               evidence="Machine List network_protocol + Connector Overview")

    if not methods:
        v.step(3, "concept", "WARN",
               "No integration_method recorded on any machine in scope.",
               fix="Many rows carry none (count them live). Without it the ingress variant is unknown, "
                   "and the three variants have different signal availability.",
               evidence="Machine List integration_method")

    # ── step 4 · is the signal standardized and flowing ────────────────────────
    present = flow_signals(kg)
    unmapped = present.pop("__unmapped__", set())
    ctx["unmapped_instances"] = sorted(unmapped)
    have = present.get(plant, set())
    have_norm = {norm(x) for x in have}
    ctx["flow_signal_count"] = len(have)

    if not signals:
        v.step(4, "signal flowing", "WARN",
               "No signals given, so step 4 was not asked."
               + (f" {len(have)} distinct name(s) are flowing at {plant} today."
                  if have else f" No flow corpus for {plant}."),
               fix="Pass --signals to get a per-signal verdict. Availability is per signal, "
                   "not per machine.")
    elif not have:
        v.step(4, "signal flowing", "WARN",
               f"No Node-RED instance maps to {plant}, so the corpus can neither confirm nor "
               "deny that these signals flow.",
               fix="Unproven is not absent. Check the edge platform directly and record the "
                   "answer — do not report this as a data gap.",
               evidence="Node-RED corpus")
    else:
        # A flow names a signal as `datapointTotalPartCounter` or `TotalPartCounter_sv`
        # as often as bare, so containment either way is the evidence, not equality.
        def flowing(s: str) -> bool:
            n = norm(s)
            # One-way containment only. A flow token may be more specific than the signal
            # name (datapointTotalPartCounter proves TotalPartCounter), never less: matching
            # the other way lets a generic "Pressure" token confirm "OvenPressure".
            return bool(n) and any(n in h for h in have_norm)

        found = [s for s in signals if flowing(s)]
        missing = [s for s in signals if not flowing(s)]
        if found:
            v.step(4, "signal flowing", "INFO",
                   f"Flowing at {plant} today: {', '.join(found)}.",
                   evidence=f"Node-RED corpus, {len(have)} distinct names at {plant}")
        if missing:
            v.step(4, "signal flowing", "BLOCKER",
                   f"Not found in any flow at {plant}: {', '.join(missing)}.",
                   fix="Confirm against the edge platform before reporting absent — a signal "
                       "can be published without a flow consuming it. If it is genuinely "
                       "absent, this is od-signal-standardization's problem, not analytics'.",
                   evidence="Node-RED corpus")

    # ── step 5 · fit for use ───────────────────────────────────────────────────
    v.step(5, "fit for use", "WARN",
           "Not answerable from the bundle. Granularity, freshness and completeness per "
           "signal are recorded in no source here.",
           fix="Check Databricks and the Azure Storage Account directly. This step is the "
               "one most often assumed, and a wrong assumption here is discovered after the "
               "analysis is delivered.")

    # ── step 6 · does something already answer it ──────────────────────────────
    lib = [n for n in nodes if n["type"] == "LibraryUseCase"]
    stories = [n for n in nodes if n["type"] == "UserStory" and n.get("plant") == plant]
    terms = {norm(s) for s in signals} if signals else set()
    hits = [n for n in lib + stories
            if terms and any(t and t in norm(n.get("label", "") + n.get("target_text", ""))
                             for t in terms)]
    ctx["library_hits"] = [n.get("label") for n in hits[:8]]
    if hits:
        v.step(6, "already exists", "WARN",
               f"{len(hits)} existing item(s) mention these signals — e.g. "
               + "; ".join(str(n.get("label"))[:60] for n in hits[:3]),
               fix="Adoption is what the department is short of, not templates. Check "
                   "od-use-case-standardization before scoping a build.",
               evidence="LibraryUseCase + this plant's use cases")
    else:
        v.step(6, "already exists", "INFO",
               f"Nothing in the library or {plant}'s {len(stories)} use case(s) matches.",
               evidence="LibraryUseCase + this plant's use cases")
    return v, ctx


def emit_report(v: Verdict, ctx: dict) -> None:
    plant = ctx.get("plant") or ctx["plant_input"]
    print(f"# Data availability verdict — {plant}\n")
    if ctx.get("signals"):
        print(f"**Signals asked for:** {', '.join(ctx['signals'])}\n")
    worst = v.exit_code()
    headline = {2: "**Not supportable as asked.**", 1: "**Partly supportable.**",
                0: "**Supportable.**"}[worst]
    print(f"{headline} The step it turns on is named below — steps 2, 4 and 5 look identical "
          "from a dashboard and are different problems with different owners.\n")
    print("| # | Step | Verdict | What was found | Route |")
    print("|---|---|---|---|---|")
    for s in v.steps:
        print(f"| {s['step']} | {s['name']} | {ICON[s['severity']]} {s['severity']} | "
              f"{s['message']} | {s['fix'] or '—'} |")
    print("\n## Sources used\n")
    print("| Source | What it answered | Limit |")
    print("|---|---|---|")
    print(f"| Machine List | steps 1–3 · {ctx.get('machine_count', 0)} machine(s) in scope | "
          "rows with no integration status are 'not recorded', not 'no' |")
    print(f"| Connector Overview | step 3 · vendors {', '.join(ctx.get('vendors', {})) or '—'} | "
          "the match is on vendor and protocol, not on the machine |")
    print(f"| Node-RED corpus | step 4 · {ctx.get('flow_signal_count', 0)} name(s) at {plant} | "
          "a flow proves presence, never absence |")
    print("| — | step 5 | no source in the bundle carries fitness for use |")
    print(f"| Library + use cases | step 6 · {len(ctx.get('library_hits', []))} hit(s) | "
          "matches on name, so a differently-named twin is missed |")
    print("\n## What has to be checked outside the bundle\n")
    print("- Step 5 in full: granularity, freshness, completeness, in Databricks and the "
          "Azure Storage Account.")
    print("- Any step 4 BLOCKER, against the edge platform, before it is reported as absent.")
    if ctx.get("unmapped_instances"):
        print(f"- {len(ctx['unmapped_instances'])} Node-RED instance(s) map to no plant and "
              f"were excluded: {', '.join(ctx['unmapped_instances'])}.")
    print("\n## Decision\n\n⟨supportable as asked · supportable with a named reduction · "
          "route to another lane · refuse with a reason⟩")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(add_help=False, description=__doc__)
    ap.add_argument("--plant", required=False)
    ap.add_argument("--machine")
    ap.add_argument("--signals", default="")
    ap.add_argument("--kg", default="../ops-knowledge-graph")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("-h", "--help", action="store_true")
    try:
        ns = ap.parse_args(argv[1:])
    except SystemExit:
        return 2
    if ns.help or not ns.plant:
        print(__doc__)
        return 0

    kg = pathlib.Path(ns.kg).expanduser()
    if not kg.is_absolute():
        kg = (pathlib.Path.cwd() / kg).resolve()
    signals = [s.strip() for s in ns.signals.split(",") if s.strip()]
    try:
        v, ctx = analyze(kg, ns.plant, ns.machine, signals)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if ns.json:
        print(json.dumps({"context": ctx, "steps": v.steps}, indent=2, ensure_ascii=False))
        return v.exit_code()
    if ns.report:
        emit_report(v, ctx)
        return v.exit_code()

    print(f"\n=== {ctx.get('plant') or ns.plant}"
          + (f" · {ns.machine}" if ns.machine else "")
          + (f" · {', '.join(signals)}" if signals else ""))
    for s in sorted(v.steps, key=lambda x: (x["step"], SEV[x["severity"]])):
        print(f"  {ICON[s['severity']]} step {s['step']} {s['name']:16s} {s['message']}")
        if s["fix"]:
            print(f"      → {s['fix']}")
    c = v.counts()
    print(f"    {c['BLOCKER']} blocker · {c['WARN']} unproven · {c['INFO']} ok")
    return v.exit_code()



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
