#!/usr/bin/env python3
"""Generate the skill map — a Mermaid picture of the registry and its build state.

    python3 scripts/build_skill_map.py            # write docs/skill-state-map.md
    python3 scripts/build_skill_map.py --check    # fail if the file on disk is stale

The build state is read from the filesystem, so the map cannot drift from what is actually
there. The lane grouping and the delivery order come from registry.yaml and from the
department's own playbooks; those are editorial and live in FLOW below.
"""

from __future__ import annotations

import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
import skillpaths as sp
OUT = ROOT / "docs" / "skill-state-map.md"

# Short labels: the node text, kept terse so the diagram stays readable.
LABEL = {
    "od-context": "OD context",
    "od-use-case-intake-triage": "Intake triage",
    "od-system-fit-check": "System fit check",
    "od-use-case-definition": "Use-case definition",
    "od-use-case-solution-evaluation": "Solution evaluation",
    "od-use-case-standardization": "Use-case standardization",
    "od-requirements-breakdown": "Requirements breakdown",
    "od-benefit-calculation": "Benefit calculation",
    "od-data-availability-check": "Data availability check",
    "od-equipment-integration": "Equipment integration",
    "od-signal-standardization": "Signal standardization",
    "od-node-red-flow-builder": "Node-RED flow builder",
    "od-node-red-flow-builder": "Node-RED troubleshooting",
    "od-analytics-asset-build": "Analytics asset build",
    "build-grafana-ops-dashboard": "Grafana dashboards",
    "od-portfolio-and-savings-analysis": "Portfolio and savings",
    "od-acceptance-test": "Acceptance test",
    "od-handover-and-adoption": "Handover and adoption",
    "od-scorecard-reporting": "Scorecard reporting",
    "od-sharepoint-list-export": "SharePoint export",
    "od-decision-routing": "Decision routing",
    "od-use-case-definition": "Use Case Support",
    "od-information-integration-service": "Information Integration",
    "od-project-support-consultancy": "Project Support",
    "od-analytical-support-service": "Analytical Support",
}

# The order work actually moves, per the four lane playbooks. Editorial, and the part of
# this file a person maintains.
FLOW: list[tuple[str, str, str]] = [
    ("od-use-case-intake-triage", "od-system-fit-check", "fit risk"),
    ("od-use-case-intake-triage", "od-requirements-breakdown", "accepted"),
    ("od-requirements-breakdown", "od-use-case-definition", "scoped"),
    ("od-requirements-breakdown", "od-data-availability-check", "signals named"),
    ("od-use-case-definition", "od-use-case-standardization", "library check"),
    ("od-use-case-definition", "od-use-case-solution-evaluation", "scoped"),
    ("od-use-case-solution-evaluation", "od-benefit-calculation", "fits as scoped"),
    ("od-data-availability-check", "od-equipment-integration", "not integrated"),
    ("od-data-availability-check", "od-signal-standardization", "not standardized"),
    ("od-equipment-integration", "od-signal-standardization", "connected"),
    ("od-signal-standardization", "od-node-red-flow-builder", "named signals"),
    ("od-node-red-flow-builder", "od-node-red-flow-builder", "when it breaks"),
    ("od-node-red-flow-builder", "od-analytics-asset-build", "data flowing"),
    ("od-analytics-asset-build", "build-grafana-ops-dashboard", "dashboards"),
    ("od-analytics-asset-build", "od-acceptance-test", "built"),
    ("od-node-red-flow-builder", "od-acceptance-test", "built"),
    ("od-acceptance-test", "od-handover-and-adoption", "accepted"),
    ("od-handover-and-adoption", "od-scorecard-reporting", "in use"),
    ("od-benefit-calculation", "od-portfolio-and-savings-analysis", "value"),
    ("od-sharepoint-list-export", "od-portfolio-and-savings-analysis", "the list"),
    ("od-portfolio-and-savings-analysis", "od-scorecard-reporting", "the numbers"),
    ("od-use-case-standardization", "od-decision-routing", "adopt or build"),
]

LANES = [
    ("UC", "Use Case Support", ["od-use-case-intake-triage", "od-system-fit-check",
                                "od-requirements-breakdown",
                                "od-use-case-definition", "od-use-case-solution-evaluation",
                                "od-use-case-standardization", "od-benefit-calculation"]),
    ("II", "Information Integration", ["od-data-availability-check",
                                       "od-equipment-integration",
                                       "od-signal-standardization",
                                       "od-node-red-flow-builder",
                                       "od-node-red-flow-builder"]),
    ("AS", "Analytical Support", ["od-analytics-asset-build", "build-grafana-ops-dashboard",
                                  "od-portfolio-and-savings-analysis",
                                  "od-sharepoint-list-export"]),
    ("PS", "Project Support and closing out", ["od-acceptance-test", "od-handover-and-adoption",
                                             "od-scorecard-reporting", "od-decision-routing"]),
]

# What is recommended next, and why. Editorial; keep it to three so it is a decision, not a
# backlog.
NEXT = {
    "od-acceptance-test": "**8 inbound — the most-composed skill in the registry, and the "
                          "thinnest at 468 words.** It is the gate between *delivered* and "
                          "*accepted*, which every lane's definition of done turns on",
    "od-use-case-standardization": "5 inbound · adoption is the shortfall the department "
                                   "names itself, and 100 library use cases already exist to "
                                   "check against",
    "od-handover-and-adoption": "5 inbound · the IMPLEMENTED-vs-PRODUCTIVE gap lives here, "
                                "and 129 use cases sit on the wrong side of it",
}


def state(skill_id: str) -> str:
    d = sp.skill_dir(skill_id)
    refs = len(list((d / "references").glob("*.md"))) if (d / "references").is_dir() else 0
    scripts = len(list((d / "scripts").glob("*.py"))) if (d / "scripts").is_dir() else 0
    if refs and scripts:
        return "deep"
    if refs:
        return "documented"
    return "stub"


def counts(states: dict[str, str]) -> dict[str, int]:
    out = {"deep": 0, "documented": 0, "stub": 0}
    for s in states.values():
        out[s] += 1
    return out


def render() -> str:
    registry = yaml.safe_load((ROOT / "registry.yaml").read_text(encoding="utf-8"))
    ids = [e["id"] for e in registry["skills"]]
    states = {i: state(i) for i in ids}
    inbound: dict[str, int] = {i: 0 for i in ids}
    for i in ids:
        fm = yaml.safe_load(
            (sp.skill_dir(i) / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[1])
        for c in ((fm.get("metadata") or {}).get("composes") or []):
            if c in inbound:
                inbound[c] += 1
    c = counts(states)
    placed = {s for _, _, members in LANES for s in members}
    unplaced = [i for i in ids if i not in placed and i not in
                ("od-context", "od-use-case-definition",
                 "od-information-integration-service", "od-project-support-consultancy",
                 "od-analytical-support-service")]

    L: list[str] = []
    L += ["---",
          "type: Map of Content",
          "title: Skill state map",
          "description: Every skill in the registry as one picture - which lane it serves, "
          "where it sits in the delivery order, how far it is built, and what is next.",
          "resource: ../registry.yaml",
          "status: stable",
          "owner: human:jakob.gabriel",
          "tags: [map, roadmap, navigation]",
          "generated: { by: claude-code/1, at: 2026-08-26T00:00:00Z }",
          "---", ""]
    L += ["# Skill state map", "",
          "<!-- Generated by scripts/build_skill_map.py — do not edit by hand. -->", "",
          f"**{len(ids)} skills.** {c['deep']} carry references and a runnable script, "
          f"{c['documented']} carry references, {c['stub']} are still a `SKILL.md` on its own.",
          "",
          "Boxes follow the order work actually moves through the four lanes. Colour is build "
          "state, not importance — a stub can be a perfectly good procedure that simply has no "
          "reference material or tooling behind it yet.", ""]

    L += ["```mermaid", "flowchart TD"]
    L += ["    ctx([\"OD context — read first\"])"]
    for key, title, members in LANES:
        L.append(f'    subgraph {key}["{title}"]')
        L.append("    direction TB")
        for m in members:
            label = LABEL.get(m, m)
            n = inbound.get(m, 0)
            tag = f"<br/>{n} inbound" if n else ""
            shape = f'["{label}{tag}"]'
            L.append(f"        {m.replace('-', '_')}{shape}")
        L.append("    end")
    for a, b, lbl in FLOW:
        L.append(f"    {a.replace('-', '_')} -->|{lbl}| {b.replace('-', '_')}")
    L.append("    ctx --> od_use_case_intake_triage")
    L.append("")
    L += ["    classDef deep fill:#1a7f4b,stroke:#0d5c34,color:#ffffff,stroke-width:2px;",
          "    classDef documented fill:#b8860b,stroke:#8a6508,color:#ffffff,stroke-width:2px;",
          "    classDef stub fill:#e8e8e8,stroke:#9a9a9a,color:#333333,"
          "stroke-dasharray:4 3;",
          "    classDef nxt stroke:#1f6feb,stroke-width:4px;",
          "    classDef ctx fill:#4b3fa8,stroke:#332a80,color:#ffffff,stroke-width:2px;"]
    for label in ("deep", "documented", "stub"):
        members = [i.replace("-", "_") for i in ids if states[i] == label
                   and i in placed]
        if members:
            L.append(f"    class {','.join(members)} {label};")
    nxt = [i.replace("-", "_") for i in NEXT if i in placed]
    if nxt:
        L.append(f"    class {','.join(nxt)} nxt;")
    L.append("    class ctx ctx;")
    L.append("```")

    L += ["", "| | Meaning |", "|---|---|",
          "| 🟩 **Deep** | References *and* a runnable script — the check can be executed, not "
          "just read |",
          "| 🟨 **Documented** | References carry the substance; no tooling yet |",
          "| ⬜ **Stub** | `SKILL.md` alone. A complete procedure, with nothing behind it |",
          "| 🔵 **Blue outline** | Recommended next |", ""]

    L += ["## Where it stands", "", "| Skill | Lane | State | Refs | Scripts | Inbound |",
          "|---|---|---|--:|--:|--:|"]
    lane_of = {m: title for _, title, members in LANES for m in members}
    order = {s: n for n, s in enumerate(
        [m for _, _, members in LANES for m in members])}
    rank = {"deep": 0, "documented": 1, "stub": 2}
    for i in sorted(ids, key=lambda x: (rank[states[x]], order.get(x, 99), x)):
        d = sp.skill_dir(i)
        refs = len(list((d / "references").glob("*.md"))) if (d / "references").is_dir() else 0
        scr = len(list((d / "scripts").glob("*.py"))) if (d / "scripts").is_dir() else 0
        icon = {"deep": "🟩", "documented": "🟨", "stub": "⬜"}[states[i]]
        lane = lane_of.get(i, "—")
        L.append(f"| [`{i}`](../{sp.folder_of(i)}/{i}/SKILL.md) | {lane} | {icon} {states[i]} | "
                 f"{refs} | {scr} | {inbound.get(i, 0)} |")

    L += ["", "## What is next, and why", ""]
    for i, why in NEXT.items():
        L.append(f"- **[`{i}`](../{sp.folder_of(i)}/{i}/SKILL.md)** — {why}")
    L += ["",
          "*Inbound* counts how many other skills name this one in `composes`. It is the "
          "cheapest proxy for what the rest of the registry is leaning on, and it is what "
          "picked the last two skills built.", ""]

    if unplaced:
        L += ["## Not on the map", "",
              "The four lane skills and " + ", ".join(f"`{u}`" for u in unplaced)
              + " are entry points rather than steps, so they carry no position in the "
                "delivery order.", ""]
    else:
        L += ["## Not on the map", "",
              "The four lane skills (`od-use-case-definition`, "
              "`od-information-integration-service`, `od-project-support-consultancy`, "
              "`od-analytical-support-service`) are entry points rather than steps: each one "
              "names the skills its lane calls, so they sit above this diagram rather than in "
              "it. All four are still stubs.", ""]
    return "\n".join(L)


def main(argv: list[str]) -> int:
    want = render()
    have = OUT.read_text(encoding="utf-8") if OUT.exists() else None
    if "--check" in argv:
        if have != want:
            print(f"stale: {OUT.relative_to(ROOT)}", file=sys.stderr)
            return 1
        print("skill map up to date")
        return 0
    OUT.write_text(want, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
