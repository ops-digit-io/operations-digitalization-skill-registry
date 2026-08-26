---
type: Skill Reference
title: Sources
description: The five sources this check reads, what each can genuinely answer, how much of it is populated, and where each one stops.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [data-availability, sources]
generated: { by: claude-code/1, at: 2026-08-26T00:00:00Z }
---

# Sources

Five sources answer the six steps between them, and **not one of them answers step 5.** Knowing
where each stops is the whole skill: a check that reports "no data" when the source simply
does not record the answer has invented a gap.

## Machine List — 1,715 rows

Steps 1 to 3. Every row carries `plant`, `region` and `label`; everything else is partial:

| Field | Populated | What it decides |
|---|--:|---|
| `plc_vendor` | 92% | Which connector could speak to it |
| `plc_model` | 73% | Whether the vendor match is specific enough to act on |
| `integration_status` | **73%** | Step 2 — and the 27% blank is the trap below |
| `integration_priority` | 72% | When it will be integrated, if it is not |
| `integration_method` | 68% | Which of the three ingress variants, which changes what is available |
| `network_protocol` | 67% | The connector match again, from the other side |
| `integration_date` | 47% | Whether history exists as far back as an analysis needs |
| `integration_blockers` | **7%** | Why it is not integrated — almost never recorded |
| `documentation_available` / `documentation_link` | **0%** | Nothing. The fields exist on all 1,715 rows and are populated on none |

**The blank-status trap.** 821 rows are `INTEGRATED`, 395 `NOT INTEGRATED`, 48
`INTEGRATION ONGOING` — and **451 carry nothing at all**. A blank is not a no. Reading it as
one turns a quarter of the estate into a fabricated gap, and the fabricated gap gets routed
to a lane that then finds nothing to do.

**191 machines are `INTEGRATED` with no `integration_method`.** They were integrated by a
route nobody recorded, so the ingress variant — and with it what is actually published —
cannot be inferred from the row.

## Connector Overview — 26 connectors

Step 3, and it needs reading twice. A connector existing is not a connector you may use:

| | Count |
|---|--:|
| `Productive` and marked `USE` | **19** |
| `Idea` | 5 |
| `Development` | 2 |
| `NOT AVAILABLE` | 6 |
| `DO NOT USE` | 1 |

An `Idea` connector on a roadmap is not a route to data. Match on `input_protocol` and the
vendor, then check `status` and `utilization` before reporting the step as passed.

**A vendor field that is not a vendor.** `plc_vendor` holds `S7.Schnitt.` on 8 machines — a
German note meaning "S7 interface", not a manufacturer — plus `MRA` (7), `ASI` (4), `PMA` (3)
and `EOS` (1). Those machines match no connector, which reads as a connector gap and is a
data-entry gap. Fix the row; do not raise a barrier.

## Node-RED flow corpus — 825 flows across 53 instances

Step 4, and it is the only source in the bundle that says anything about an individual
**signal** rather than a machine. A signal name appearing in a deployed flow is strong
evidence it exists at that plant.

**A flow proves presence and never absence.** A signal can be published to the edge platform
with nothing consuming it, so "not in any flow" is a prompt to check the platform, not a
verdict. The script says `unproven`, not `absent`, and the difference matters: one is a
question for the platform, the other is a request to another lane.

**17 of 33 plants have flow evidence.** For the other 16 — including Northeim (87 machines),
Tlalnepantla (82), Auburn (60) and Rennes (58) — step 4 cannot be answered from the bundle at
all. See [`plant-instance-map.md`](plant-instance-map.md).

## Use case portfolio and reference library — 650 + 100

Step 6. Matching is on the name and the target text, so a use case that solves the same
problem under a different name is missed. The check is worth running anyway: **adoption is
what the department is short of, not templates.**

## Databricks and the Azure Storage Account

Step 5, and **nothing in the bundle stands in for them.** Granularity, freshness and
completeness per signal are recorded in no source here. This is the step most often assumed,
and the assumption is discovered after the analysis has been delivered.

The script reports step 5 as unproven every single time, deliberately. A tool that guessed
here would be worse than one that admits it cannot see.
