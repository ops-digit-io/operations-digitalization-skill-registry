#!/usr/bin/env python3
"""Static analysis of an OESL Node-RED flow export.

    python3 analyze_flow.py FLOW.json [FLOW.json ...] [--json] [--quiet]

Takes the per-flow JSON as exported by node-red-auto-docs (`[tab, ...nodes]`) or a
raw Node-RED export (a bare node array), and reports what is wrong with it before
anyone opens the editor.

Every check below was derived from the corpus of 825 flows across 53 ct-oesl
instances — these are the failure modes that actually occur, not a generic lint.
Findings are ranked: BLOCKER breaks data, WARN degrades it, INFO is hygiene.

Exit code: 2 if any BLOCKER, 1 if any WARN, 0 otherwise.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict

UUID_RE = re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I)
SECRET_PATTERNS = [
    ("Teams/webhook URL", re.compile(r"https://[a-z0-9.-]*webhook[^\"'\s]{20,}", re.I)),
    ("Bearer token", re.compile(r"Bearer\s+[A-Za-z0-9._-]{20,}")),
    ("inline credential", re.compile(r"\"(?:password|passwd|token|apikey|api_key|secret)\"\s*:\s*\"[^\"]{6,}\"", re.I)),
]
CANONICAL_GROUPS = {
    "config flow",
    "set inputs for config flow",
    "functional flow",
    "mqtt connection and message decoding",
    "set message filters",
    "prepare and convert payload",
    "message encoding and connection",
}
VALUE_FIELDS = ["valueInteger", "valueString", "valueDouble", "valueBool", "valueBytes"]

SEV_ORDER = {"BLOCKER": 0, "WARN": 1, "INFO": 2}


class Report:
    def __init__(self, name: str) -> None:
        self.name = name
        self.findings: list[dict] = []

    def add(self, sev: str, check: str, msg: str, where: str = "", fix: str = "") -> None:
        self.findings.append(
            {"severity": sev, "check": check, "message": msg, "where": where, "fix": fix}
        )

    def sorted(self) -> list[dict]:
        return sorted(self.findings, key=lambda f: (SEV_ORDER[f["severity"]], f["check"]))

    def counts(self) -> Counter:
        return Counter(f["severity"] for f in self.findings)


def load(path: str):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, list) or not data:
        raise ValueError("not a Node-RED export (expected a non-empty JSON array)")
    head = data[0] if isinstance(data[0], dict) and "type" not in data[0] else None
    nodes = [n for n in (data[1:] if head else data) if isinstance(n, dict)]
    if head is None:
        tabs = [n for n in nodes if n.get("type") == "tab"]
        if tabs:
            head = tabs[0]
            nodes = [n for n in nodes if n.get("type") != "tab"]
    return head or {}, nodes, data


def label_of(node: dict) -> str:
    return (node.get("name") or "").strip() or f"<unnamed {node.get('type')} {node.get('id','')[:6]}>"


# ── checks ──────────────────────────────────────────────────────────────────

def check_documentation(rep, tab, nodes):
    if not (tab.get("info") or "").strip():
        rep.add("WARN", "no-flow-description",
                "The flow carries no description. Only 1% of the corpus does, and the "
                "generated documentation page has nothing to say the flow is for.",
                where="tab", fix="Write one paragraph in the tab's Description: what this "
                                 "produces, for which machine, consumed by which use case.")
    functional = [n for n in nodes if n.get("type") not in ("group", "comment")]
    unnamed = [n for n in functional if not (n.get("name") or "").strip()]
    if functional and len(unnamed) / len(functional) > 0.55:
        rep.add("WARN", "mostly-unnamed-nodes",
                f"{len(unnamed)} of {len(functional)} nodes are unnamed "
                f"({len(unnamed)/len(functional):.0%}). Across the corpus 63% of nodes "
                "carry a name, so this flow is well below the house standard.",
                fix="Name every node. `{{error.source.name}}` in the standard error "
                    "template resolves to this field, so an unnamed node produces an "
                    "error message identifying nothing.")
    groups = {g for g in ((n.get("name") or "").strip().lower()
                          for n in nodes if n.get("type") == "group") if g}
    unnamed_groups = [n for n in nodes if n.get("type") == "group" and not (n.get("name") or "").strip()]
    if unnamed_groups:
        rep.add("INFO", "unnamed-group",
                f"{len(unnamed_groups)} group(s) unnamed. 92% of corpus groups are named.")
    if groups:
        off = groups - CANONICAL_GROUPS
        known = groups & CANONICAL_GROUPS
        if known and off:
            rep.add("INFO", "non-canonical-group",
                    "Groups outside the canonical seven: " + ", ".join(sorted(off)),
                    fix="Use-case-specific groups are fine; the canonical names are what "
                        "make 825 generated pages comparable, so keep those spelled exactly.")


def check_config_discipline(rep, nodes):
    """UUIDs belong in the config change node, never in a function body."""
    config_uuids = set()
    for n in nodes:
        if n.get("type") == "change":
            for rule in n.get("rules") or []:
                if rule.get("pt") == "flow":
                    config_uuids.update(UUID_RE.findall(str(rule.get("to") or "")))
    for n in nodes:
        if n.get("type") != "function":
            continue
        body = n.get("func") or ""
        stray = {u for u in UUID_RE.findall(body)}
        if stray:
            rep.add("BLOCKER", "uuid-literal-in-function",
                    f"{len(stray)} UUID literal(s) hardcoded in a function body.",
                    where=label_of(n),
                    fix="Move them to the `Set flow config` change node and read with "
                        "flow.get(). Porting this flow to another machine must be one "
                        "change node, not a hunt through function bodies.")
    if not config_uuids:
        has_cfg = any(n.get("type") == "change" and any(
            (r.get("pt") == "flow") for r in (n.get("rules") or [])) for n in nodes)
        if not has_cfg:
            rep.add("WARN", "no-flow-config",
                    "No change node writes flow-scoped variables. The config group is "
                    "the single place a flow is bound to a machine.",
                    fix="Add the `config flow` group: inject 'Trigger once' → change "
                        "'Set flow config' → function 'Debug flow config' → debug.")


def check_systime_pair(rep, nodes):
    fns = [n for n in nodes if n.get("type") == "function"]
    bodies = {label_of(n): (n.get("func") or "") for n in fns}
    unpack = [k for k, v in bodies.items() if ">> 32n" in v and "0xFFFFFFFFn" in v]
    repack = [k for k, v in bodies.items() if "<< 32n" in v]
    has_encode = any(n.get("type") == "encode" for n in nodes)
    has_decode = any(n.get("type") == "decode" for n in nodes)
    if has_decode and not unpack:
        rep.add("BLOCKER", "systime-not-unpacked",
                "The flow decodes PLCPacketList but never unpacks sysTime.",
                fix="sysTime is packed (seconds<<32 | nanos), not epoch millis. Add the "
                    "standard `Convert sysTime (UTC timestamp)` function after the split.")
    if has_encode and not repack:
        rep.add("BLOCKER", "systime-not-repacked",
                "The flow encodes a PLCPacket but never re-packs sysTime. This encodes "
                "cleanly and corrupts every downstream timestamp — nothing errors.",
                fix="Add `Convert sysTime back (UTC timestamp)` before the encode node.")
    if unpack and has_encode and not repack:
        rep.add("BLOCKER", "systime-unpaired",
                f"sysTime is unpacked in {unpack[0]} but never re-packed.",
                fix="The two conversions are a pair. Never ship one without the other.")


def check_encode_shape(rep, nodes):
    if not any(n.get("type") == "encode" for n in nodes):
        return
    moved = False
    deleted_values = set()
    set_values = set()
    set_uuid_from = None
    for n in nodes:
        if n.get("type") != "change":
            continue
        for r in n.get("rules") or []:
            p, to, t = str(r.get("p") or ""), str(r.get("to") or ""), r.get("t")
            if t == "move" and to.startswith("payload.plcPackets"):
                moved = True
            if t == "delete":
                for vf in VALUE_FIELDS:
                    if p.endswith(vf):
                        deleted_values.add(vf)
            if t == "set":
                for vf in VALUE_FIELDS:
                    if p.endswith(vf):
                        set_values.add(vf)
                if p.endswith("payload.uuid"):
                    set_uuid_from = (r.get("tot"), to)
    if not moved:
        creates_list = any(
            "plcPackets" in (n.get("func") or "") for n in nodes if n.get("type") == "function")
        if not creates_list:
            rep.add("BLOCKER", "missing-plcpackets-wrap",
                    "Nothing moves payload into `payload.plcPackets[0]` before the encode.",
                    fix="PLCPacketList expects a repeated field. Without the move the "
                        "encode succeeds and decodes to nothing useful downstream.")
    leftover = set_values & deleted_values
    if len(set_values - deleted_values) > 1:
        rep.add("BLOCKER", "oneof-violation",
                "More than one measured_value field is set and not deleted: "
                + ", ".join(sorted(set_values - deleted_values)),
                fix="`measured_value` is a protobuf oneof — send exactly one. Delete the "
                    "others in `prepare for protob encoding`.")
    if set_uuid_from is None:
        rep.add("WARN", "output-uuid-not-set",
                "No change rule sets `payload.uuid` before the encode — the derived "
                "packet may be publishing under the *input* data point's identity.",
                fix="Set payload.uuid from the flow-config output UUID.")
    elif set_uuid_from[0] != "flow":
        rep.add("WARN", "output-uuid-not-from-config",
                f"`payload.uuid` is set from {set_uuid_from[0]!r}, not from flow config.",
                fix="Take the output UUID from the config group so the flow stays portable.")
    _ = leftover


def check_error_handling(rep, nodes):
    catches = [n for n in nodes if n.get("type") == "catch"]
    if not catches:
        rep.add("WARN", "no-catch",
                "No catch node. 446 of 825 flows in the corpus have one.",
                fix="Add the four-node pattern: catch → change 'get env variables of "
                    "flow' → template 'create error message' → debug.")
        return
    scoped = [c for c in catches if c.get("scope")]
    if scoped:
        rep.add("INFO", "catch-scoped",
                f"{len(scoped)} catch node(s) scoped to selected nodes rather than the "
                "whole flow — errors elsewhere go unreported.")
    env_used = any(
        "NR_FLOW_ID" in json.dumps(n.get("rules") or []) for n in nodes if n.get("type") == "change")
    if not env_used:
        rep.add("INFO", "error-message-lacks-flow-identity",
                "The error path does not resolve $env('NR_FLOW_ID') / NR_FLOW_NAME, so an "
                "error cannot be traced back to this flow without opening the editor.")


def check_secrets(rep, raw):
    blob = json.dumps(raw)
    for name, pat in SECRET_PATTERNS:
        hits = pat.findall(blob)
        if hits:
            rep.add("BLOCKER", "hardcoded-secret",
                    f"{len(hits)} literal {name}(s) in the flow JSON.",
                    fix="Use $env(...) / env.get() or Node-RED credentials. These "
                        "repositories are the documentation source and are cloned by the "
                        "doc generator. Rotate anything already committed.")


def check_streaming(rep, nodes):
    for n in nodes:
        if n.get("type") == "mqtt in" and any(m.get("type") == "decode" for m in nodes):
            dt = n.get("datatype")
            if dt not in ("buffer", "auto", "auto-detect", None, ""):
                rep.add("WARN", "mqtt-datatype-for-protobuf",
                        f"mqtt in datatype is {dt!r} but the flow decodes protobuf.",
                        where=label_of(n),
                        fix="Protobuf needs the raw bytes — use 'buffer' (or auto).")
    splits = [n for n in nodes if n.get("type") == "split"]
    joins = [n for n in nodes if n.get("type") == "join"]
    for s in splits:
        if str(s.get("arraySplt")) not in ("1", "None", "") and s.get("arraySpltType") == "len":
            rep.add("INFO", "unusual-split-size",
                    f"split arraySplt={s.get('arraySplt')}; the corpus splits one packet "
                    "at a time (640 of 648).", where=label_of(s))
    if joins and not splits:
        rep.add("INFO", "join-without-split",
                "A join without a split — confirm the message parts are set upstream.")
    for n in nodes:
        if n.get("type") == "rbe":
            prop = str(n.get("property") or "")
            if not prop or prop == "payload":
                rep.add("INFO", "rbe-on-whole-payload",
                        "rbe compares the whole payload; a changing timestamp defeats it.",
                        where=label_of(n),
                        fix="Point rbe at the value field, e.g. payload.valueInteger.")
    debugs = [n for n in nodes if n.get("type") == "debug" and n.get("active", True)]
    if len(debugs) > 6:
        rep.add("INFO", "many-active-debug-nodes",
                f"{len(debugs)} active debug nodes. They are a development aid; leaving "
                "them on at volume costs throughput.")


def check_wiring(rep, nodes):
    ids = {n["id"] for n in nodes if "id" in n}
    wired_to = set()
    for n in nodes:
        for outs in n.get("wires") or []:
            wired_to.update(outs)
    link_out = [n for n in nodes if n.get("type") == "link out"]
    link_in = [n for n in nodes if n.get("type") == "link in"]
    for lo in link_out:
        if not (lo.get("links") or []):
            rep.add("WARN", "orphan-link-out",
                    "link out node points at nothing — the branch dead-ends silently.",
                    where=label_of(lo))
    for li in link_in:
        if not (li.get("links") or []) and li["id"] not in wired_to:
            rep.add("INFO", "orphan-link-in",
                    "link in node has no source.", where=label_of(li))
    SPINE = ("decode", "encode", "mqtt out", "split")
    for n in nodes:
        if n.get("type") in ("group", "comment", "catch", "status", "inject", "mqtt in", "link in"):
            continue
        if n.get("id") not in wired_to and n.get("wires") is not None:
            if n.get("type") in SPINE:
                rep.add("WARN", "spine-severed",
                        f"A {n.get('type')} node on the main path has no inbound wire — "
                        "the pipeline is broken here and the flow moves no data.",
                        where=label_of(n),
                        fix="Re-wire the chain: mqtt in → decode → filter uuids → split → "
                            "convert sysTime … → convert back → encode → mqtt out.")
            else:
                rep.add("INFO", "unreachable-node",
                        "Node has no inbound wire and is not a source.", where=label_of(n))
    disabled = [n for n in nodes if n.get("d") is True]
    if disabled:
        rep.add("INFO", "disabled-nodes",
                f"{len(disabled)} node(s) disabled: " + ", ".join(label_of(n) for n in disabled[:5]))


def check_context(rep, nodes):
    """flow context is per-tab: a key read here must be written here.

    Reads inside `Debug flow config` are treated separately — that node is copied
    between flows and routinely echoes keys the new flow never uses, which is
    untidy rather than broken.
    """
    sets, gets = Counter(), Counter()
    echo_only = defaultdict(bool)
    for n in nodes:
        body = n.get("func") or ""
        is_echo = (n.get("name") or "").strip().lower() == "debug flow config"
        for m in re.finditer(r"flow\.set\(\s*[\"']([^\"']+)", body):
            sets[m.group(1)] += 1
        for m in re.finditer(r"flow\.get\(\s*[\"']([^\"']+)", body):
            key = m.group(1)
            gets[key] += 1
            echo_only[key] = echo_only.get(key, True) and is_echo
        for r in n.get("rules") or []:
            if r.get("pt") == "flow" and r.get("t") == "set":
                sets[str(r.get("p"))] += 1
            if r.get("tot") == "flow":
                key = str(r.get("to"))
                gets[key] += 1
                echo_only[key] = False
    unread = [k for k in sets if k not in gets]
    if unread:
        rep.add("INFO", "write-only-context",
                f"flow context written but never read: {', '.join(sorted(unread)[:6])}")
    real, echoes = [], []
    for k in gets:
        if k in sets:
            continue
        (echoes if echo_only.get(k) else real).append(k)
    if real:
        rep.add("WARN", "unset-context-read",
                "flow context read in the functional path but never written here: "
                + ", ".join(sorted(real)[:6])
                + ". flow context is per-tab, so it will be undefined at runtime.",
                fix="Set it in the `Set flow config` change node, or remove the read.")
    if echoes:
        rep.add("INFO", "stale-config-echo",
                "`Debug flow config` echoes keys this flow never sets: "
                + ", ".join(sorted(echoes)[:6])
                + ". Copied from another flow and not trimmed.",
                fix="Mirror exactly the variables `Set flow config` writes — that is the "
                    "node's whole purpose, and a stale echo makes a real misconfiguration "
                    "harder to spot at deploy.")


CHECKS = [
    ("documentation", lambda rep, tab, nodes, raw: check_documentation(rep, tab, nodes)),
    ("config", lambda rep, tab, nodes, raw: check_config_discipline(rep, nodes)),
    ("systime", lambda rep, tab, nodes, raw: check_systime_pair(rep, nodes)),
    ("encode", lambda rep, tab, nodes, raw: check_encode_shape(rep, nodes)),
    ("errors", lambda rep, tab, nodes, raw: check_error_handling(rep, nodes)),
    ("secrets", lambda rep, tab, nodes, raw: check_secrets(rep, raw)),
    ("streaming", lambda rep, tab, nodes, raw: check_streaming(rep, nodes)),
    ("wiring", lambda rep, tab, nodes, raw: check_wiring(rep, nodes)),
    ("context", lambda rep, tab, nodes, raw: check_context(rep, nodes)),
]

ICON = {"BLOCKER": "✗", "WARN": "!", "INFO": "·"}


def analyze(path: str) -> Report:
    tab, nodes, raw = load(path)
    rep = Report((tab.get("label") or path).strip() or path)
    for _, fn in CHECKS:
        fn(rep, tab, nodes, raw)
    return rep


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    as_json = "--json" in argv
    quiet = "--quiet" in argv
    if not args:
        print(__doc__)
        return 0
    worst = 0
    out = []
    for path in args:
        try:
            rep = analyze(path)
        except Exception as exc:  # noqa: BLE001 - report, do not crash the batch
            print(f"{path}: could not analyze — {exc}", file=sys.stderr)
            worst = max(worst, 1)
            continue
        c = rep.counts()
        worst = max(worst, 2 if c["BLOCKER"] else 1 if c["WARN"] else 0)
        if as_json:
            out.append({"flow": rep.name, "file": path, "findings": rep.sorted()})
            continue
        if quiet and not c["BLOCKER"] and not c["WARN"]:
            continue
        print(f"\n=== {rep.name}  [{path}]")
        if not rep.findings:
            print("    clean")
        for f in rep.sorted():
            where = f" ({f['where']})" if f["where"] else ""
            print(f"  {ICON[f['severity']]} {f['severity']:7s} {f['check']}{where}")
            print(f"      {f['message']}")
            if f["fix"]:
                print(f"      → {f['fix']}")
        print(f"    {c['BLOCKER']} blocker · {c['WARN']} warn · {c['INFO']} info")
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
