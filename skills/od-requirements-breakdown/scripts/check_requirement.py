#!/usr/bin/env python3
"""Check a requirement document for completeness before it crosses a lane boundary.

    python3 check_requirement.py REQUIREMENT.md [--lane use-case|integration|project|analytical]
    python3 check_requirement.py REQUIREMENT.md --json

Reads the markdown requirement produced from `references/requirement-template.md` and
reports what is missing, what is a placeholder, and what would fail intake.

The checks encode the portfolio's own failure pattern: what gets asked for in a meeting
is populated, and what needs a conversation with the operator is not. `savings_eur` is
filled on 100% of 650 use cases; `targets` on 9%; `methods` and `utilization` on none.

Exit code: 2 if any BLOCKER, 1 if any WARN, 0 otherwise.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter

# section heading -> (canonical key, required, what it is)
SECTIONS = {
    "identity":            (r"^#+\s*(§?1\b|identity)", True,  "Identity"),
    "problem":             (r"^#+\s*(§?2\b|key problem|major issue)", True, "Key Problem / Major Issue"),
    "target":              (r"^#+\s*(§?3\b|use case target|target overview)", True, "Use Case Target Overview"),
    "standard":            (r"^#+\s*(§?4\b|standard baseline)", True, "Standard baseline"),
    "signals":             (r"^#+\s*(§?5\b|tags of interest|signal)", True, "Tags of Interest"),
    "acceptance":          (r"^#+\s*(§?6\b|acceptance criteria)", True, "Acceptance criteria"),
    "blocking":            (r"^#+\s*(§?7\b|blocking points)", False, "Blocking points"),
    "systemfit":           (r"^#+\s*(§?8\b|system fit)", False, "System fit"),
    "value":               (r"^#+\s*(§?9\b|value)", False, "Value"),
    "traces":              (r"^#+\s*(§?10\b|traces to)", True, "Traces to"),
}

LANE_EXTRA = {
    "use-case":   (r"handover packet",       "Handover packet to Information Integration"),
    "integration":(r"equipment requirement", "Equipment requirement"),
    "project":    (r"project scope baseline","Project scope baseline"),
    "analytical": (r"request scope",         "Request scope"),
}

PLACEHOLDER = re.compile(r"⟨[^⟩]*⟩")
TECH_WORDS = re.compile(
    r"\b(dashboard|grafana|node-?red|power ?bi|app\b|report\b|database|sql|mqtt|sensor|"
    r"kamera|camera|screen|tool\b|software|system)\b", re.I)
SEV = {"BLOCKER": 0, "WARN": 1, "INFO": 2}
ICON = {"BLOCKER": "✗", "WARN": "!", "INFO": "·"}


def split_sections(text: str) -> dict[str, str]:
    """Map canonical section key -> its body text."""
    lines = text.splitlines()
    heads: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        if not line.lstrip().startswith("#"):
            continue
        low = line.lower()
        for key, (pat, _, _) in SECTIONS.items():
            if re.search(pat, low):
                heads.append((i, key))
                break
        else:
            heads.append((i, f"_other_{i}"))
    out: dict[str, str] = {}
    for n, (idx, key) in enumerate(heads):
        end = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
        out.setdefault(key, "")
        out[key] += "\n".join(lines[idx + 1:end]).strip() + "\n"
    return out


def analyze(path: str, lane: str | None):
    text = open(path, encoding="utf-8").read()
    low = text.lower()
    sec = split_sections(text)
    findings: list[dict] = []

    def add(s, c, m, fix=""):
        findings.append({"severity": s, "check": c, "message": m, "fix": fix})

    # required sections present and non-empty
    for key, (_, required, label) in SECTIONS.items():
        body = sec.get(key, "").strip()
        if key not in sec:
            add("BLOCKER" if required else "WARN", "missing-section",
                f"§ {label} is absent.",
                fix="A requirement missing sections 1-6 or 10 is not ready to hand over.")
        elif not body or body in {"-", "tbd", "TBD"}:
            add("BLOCKER" if required else "WARN", "empty-section",
                f"§ {label} has a heading and no content.")

    # placeholders left in required sections
    for key in ("identity", "problem", "target", "signals", "acceptance", "traces"):
        body = sec.get(key, "")
        ph = PLACEHOLDER.findall(body)
        if ph:
            add("WARN", "placeholder-left",
                f"§ {SECTIONS[key][2]} still carries {len(ph)} placeholder(s): "
                + ", ".join(sorted(set(ph))[:4]),
                fix="⟨…⟩ is legitimate for a genuine unknown, but not in the sections a "
                    "receiving lane has to act on.")

    # the problem statement must not name a technology
    prob = sec.get("problem", "")
    hits = sorted(set(m.group(0).lower() for m in TECH_WORDS.finditer(prob)))
    if hits:
        add("BLOCKER", "solution-as-problem",
            f"§ Key Problem names a technology: {', '.join(hits[:5])}.",
            fix="If the sentence names a technology it is a solution, not a problem. "
                "Rewrite it as what goes wrong operationally today.")

    # the target must name a moment / consumer
    tgt = sec.get("target", "")
    MOMENT = re.compile(r"gemba|shift|escalat|daily|weekly|per (run|batch|cycle)|"
                        r"when |at the line|handover|review", re.I)
    if tgt.strip() and not MOMENT.search(tgt):
        add("WARN", "no-consuming-moment",
            "§ Use Case Target Overview does not name when anyone would look at this.",
            fix="Name the moment in the day it belongs to. A use case attached to no moment "
                "is the one that ends up recorded as utilization NEVER.")

    # signals table
    sig = sec.get("signals", "")
    rows = [l for l in sig.splitlines() if l.strip().startswith("|") and l.count("|") >= 4]
    def is_header(row: str) -> bool:
        cells = [c.strip().lower() for c in row.strip().strip("|").split("|")]
        return cells[:2] in (["signal", "direction"], ["signal", "dir"]) or (
            len(cells) > 1 and cells[0] == "signal" and "direction" in cells)

    body_rows = [r for r in rows if not re.search(r"^\|[\s\-:|]+\|$", r.strip())
                 and not is_header(r)]
    if sig.strip() and not body_rows:
        add("BLOCKER", "no-signals-listed",
            "§ Tags of Interest has no signal rows.",
            fix="The signal list is what decides whether this can be built at all.")
    else:
        if body_rows and not re.search(r"\bout\b", sig, re.I):
            add("WARN", "no-output-signal",
                "No signal is marked as an output (direction `out`).",
                fix="If this use case produces a derived value, that data point must be "
                    "registered on the edge platform before anything publishes to it.")
        if body_rows and not re.search(r"\b(yes|no)\b", sig, re.I):
            add("WARN", "signal-existence-unverified",
                "No signal carries an exists-yes/no verdict.",
                fix="Verify with od-data-availability-check rather than assuming.")

    # acceptance criteria must be testable
    acc = sec.get("acceptance", "")
    ac_lines = [l for l in acc.splitlines() if re.match(r"\s*(AC-?\d|[-*]\s|\d+\.)", l)]
    if acc.strip() and not ac_lines:
        add("BLOCKER", "acceptance-not-itemised",
            "§ Acceptance criteria is prose, not testable statements.")
    if acc.strip() and not re.search(r"real shift|not a demonstration|named .*(owner|role)|"
                                     r"plant owner", acc, re.I):
        add("WARN", "no-adoption-criterion",
            "No acceptance criterion requires use in a real shift by a named plant role.",
            fix="This is the department's own handover rule. Without it, delivered and in "
                "use get conflated - the IMPLEMENTED vs PRODUCTIVE gap.")

    # value: a figure without a reliability label
    val = sec.get("value", "")
    if re.search(r"[€$]\s?[\d,.]*\d|\b(eur|euro|usd)\b\s*[\d,.]*\d|"
                 r"[\d,.]*\d\s*(k€|k\b|eur|euro)\b", val, re.I) and not re.search(
            r"calculation|estimation|not yet assessed", val, re.I):
        add("BLOCKER", "figure-without-reliability",
            "§ Value states a figure with no reliability label.",
            fix="Label it CALCULATION (with its methodology) or ESTIMATION, or write "
                "'not yet assessed'. Tracked is not proven.")

    # traces
    tr = sec.get("traces", "")
    if tr.strip() and not re.search(r"roadmap", tr, re.I):
        add("WARN", "no-roadmap-link",
            "§ Traces to does not reference a plant roadmap item.",
            fix="A request with no roadmap link and no nameable business case is refused "
                "at intake.")

    # lane-specific section
    if lane:
        pat_label = LANE_EXTRA.get(lane)
        if not pat_label:
            add("INFO", "unknown-lane",
                f"Unknown lane '{lane}'. Known: {', '.join(LANE_EXTRA)}")
        else:
            pat, label = pat_label
            if not re.search(pat, low):
                add("BLOCKER", "missing-lane-section",
                    f"Lane '{lane}' requires § {label}, which is absent.",
                    fix="The lane variant is what the receiving side actually consumes.")

    return findings


LANES = ("use-case", "integration", "project", "analytical")


def main(argv):
    import argparse
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("files", nargs="*")
    ap.add_argument("--lane", type=str.lower, choices=LANES)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("-h", "--help", action="store_true")
    try:
        ns = ap.parse_args(argv[1:])
    except SystemExit:
        return 2
    if ns.help or not ns.files:
        print(__doc__)
        return 0
    args, as_json, lane = ns.files, ns.json, ns.lane
    worst, out = 0, []
    for path in args:
        try:
            findings = analyze(path, lane)
        except Exception as exc:  # noqa: BLE001
            print(f"{path}: could not check — {exc}", file=sys.stderr)
            worst = max(worst, 1)
            continue
        c = Counter(f["severity"] for f in findings)
        worst = max(worst, 2 if c["BLOCKER"] else 1 if c["WARN"] else 0)
        if as_json:
            out.append({"file": path, "lane": lane, "findings": findings})
            continue
        print(f"\n=== {path}" + (f"  [lane: {lane}]" if lane else ""))
        if not findings:
            print("    ready to hand over")
        for f in sorted(findings, key=lambda x: SEV[x["severity"]]):
            print(f"  {ICON[f['severity']]} {f['severity']:7s} {f['check']}")
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
