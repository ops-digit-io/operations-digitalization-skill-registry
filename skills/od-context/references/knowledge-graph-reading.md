---
type: Skill Reference
title: Knowledge graph reading
description: How to read the node kinds of the operations knowledge graph (regions, material families, process groups, capabilities, cluster tags, the Andon and Gemba escalation cluster), what the graph is and is not, and how its descriptions are marked by provenance.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, context, knowledge-graph]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Knowledge graph reading

Derived from the vault's delivered-work note on the graph, its node notes and the research notes behind the descriptions. No
counts of nodes, plants or use cases are carried: they change with each rebuild; read them from the graph. Own synthesis is marked
`PROPOSAL`; unknowns are `<...>`.

## What the graph is

One graph of the whole operations digitalization estate, with a viewer for exploring it by location, process, capability, cluster
tag, scalability and impact. It is built by a staged script pipeline from the SharePoint list exports and served read-only.

| It is | It is not |
|---|---|
| A read surface that joins the use-case list, the savings table and the machine list without a manual join | A system of record |
| The basis of the portfolio cuts and the cluster tagging | A place to correct data: **corrections made in it reach no one** |
| Rebuildable from the lists | Fresher than the last rebuild |

Consequence: a question like "which plants have capability X" is a **lookup**, answered with the rebuild date; a correction goes to
the SharePoint list (see `od-context`, "Where the truth lives"). A viewer that depends on a network fetch at open time can fail
silently (an earlier viewer rendered blank when its content source was unreachable): prefer self-contained exports when you hand a
graph to someone.

## Node kinds and how they relate

| Node kind | Meaning | Reads as | Trap |
|---|---|---|---|
| **Region** | Group of plants | Comparable lens for portfolio and conversion from use case to daily practice | Region totals come from the portfolio analysis; `PROPOSAL`: treat a conversion contrast between regions as a hypothesis about practice, not a ranking of effort |
| **Plant** | One site | Carries its use cases, machines, tools | Per-plant status is read live, never from a skill |
| **Material family** | Metal, plastic, rubber, assembly: every process group belongs to exactly one | The process context a use case inherits | Choosing the family by product name rather than process |
| **Process group** | A physical process within a family (forming, moulding, extrusion, welding, vulcanization; automated versus non-automated splits) | Tells you which signals exist and which dashboards fit | Catch-all "others" groups are generic by construction |
| **Capability (cross-plant template)** | A digital capability defined once and instantiated per plant (Andon board, process values, OEE calculation, machine alerts, cycle time, downtime reporting, recipe values, manual and process quality data, analytics, other) | What is defined versus how far each plant's instance has got | "Defined" is not "adopted": what varies between plants is progress, not definition |
| **Cluster tag** | A portfolio grouping across capabilities (real-time monitoring, Andon and escalation, SPC, manual data digitization, downtime and alerts, predictive maintenance, recipe and traceability, energy, analytics, generative and agentic AI, digital twin, other) | The unit in which standards, KPI sets and checklists are written | `PROPOSAL`: do not assume a use case maps to exactly one cluster; check how the tagging was done <to confirm> |
| **Use case / epic** | The plant-level record and its decomposition | The unit counted by the Scorecard | Counts depend on the filter; see `od-scorecard-reporting` |

Cluster standards and acceptance criteria are in `od-use-case-standardization` and `od-acceptance-test`; capability templates and
placement rules are in `od-analytics-asset-build/references/capability-templates-and-placement.md`. This file only tells you how to
move between node kinds.

## Reading a capability or cluster node

Each node note is short: one definition sentence, one sentence on what makes it hard, the members, then (for clusters) the verified
external references. Read in this order:

1. The definition: what is physically or digitally done.
2. The design constraint: e.g. for the Andon and Gemba cluster, the signal must be raisable by hand and automatically from the
   machine; the logic is two-step (the first signal asks for help without stopping the line, the second stops it if nobody came);
   escalation tiers each have a time-boxed response; every event is logged, because only the log makes later improvement analysis
   possible.
3. The reason it is a cluster: where the case for one cross-plant standard is strongest, because it replaces a different whiteboard
   at each site.
4. The references: key, tier, what was opened, what is safe to claim, what was not verified. Cite by key.

## Provenance of the descriptions

Template descriptions in the graph come from three sources and should be tagged accordingly:

| Provenance | Meaning | How far to trust |
|---|---|---|
| Source system verbatim | Text typed in the lists by a plant or the team | As reliable as the list; check the version history |
| Domain knowledge | Standard manufacturing and Industry 4.0 terminology written because the template nodes carry no free text anywhere in the source system | Textbook level; consistent across references; not a statement about a plant |
| Public benchmark | Published third-party figures used as a stand-in for "how comparable organisations do this" | Directional; see `references/provenance-and-source-catalogue.md` |

Two kinds of domain-knowledge entry are weaker than the rest: names that look like product-line or brand names rather than process
terms (inferred from the name pattern; ask the owner whether the description fits) and catch-all groups. Never present such a
description as something a plant reported.

## Procedure: answer a portfolio question from the graph

1. Name the node kind the question is about (capability, family, region, cluster).
2. Query the graph or the underlying lists; note the rebuild date.
3. If the answer differs from the Scorecard, the Scorecard wins (see `od-scorecard-reporting`, "Sources, and which one wins"); say
   which filter the graph used.
4. If you find an error, write the correction request for the list owner; do not patch the graph.

## AI agent operating notes

- **May do:** walk from a plant to its capabilities and clusters, list instances of a template and their phases, compare a use case
  with the cluster standard, draft correction requests for the lists.
- **Inputs:** the graph or its export, the rebuild date, the node kind.
- **Evidence to cite:** node id, rebuild date, reference key for any external statement.
- **Human gate:** corrections to the lists are made by their owners; external statements are quoted only with their tier.
- **Hands over to:** `od-use-case-standardization` (cluster standard), `od-portfolio-and-savings-analysis` (cuts),
  `od-context-freshness` (stale rebuild).
