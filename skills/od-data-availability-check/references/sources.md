---
type: Skill Reference
title: Sources
description: The five sources this check reads, what each can genuinely answer, which fields and patterns to expect, and where each one stops. Guidance only; counts and fill rates are read live.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [data-availability, sources]
generated: { by: claude-code/1, at: 2026-08-26T00:00:00Z }
---

# Sources

Five sources answer the six steps between them, and **not one of them answers step 5.** Knowing
where each stops is the whole skill: a check that reports "no data" when the source simply
does not record the answer has invented a gap. This file holds no counts; measure them live
on the current export and name its date.

## Machine List

Steps 1 to 3. Every row carries `plant`, `region` and `label`; everything else is partial.
Measure the fill rate per field and per plant (`machine-list-completeness.md`).

| Field | What it decides | Expect |
|---|---|---|
| `plc_vendor` | Which connector could speak to it | usually filled |
| `plc_model` | Whether the vendor match is specific enough to act on | often filled |
| `integration_status` | Step 2 - and the blanks are the trap below | has blanks |
| `integration_priority` | When it will be integrated, if it is not | partial |
| `integration_method` | Which of the three ingress variants, which changes what is available | partial |
| `network_protocol` | The connector match again, from the other side | partial |
| `integration_date` | Whether history exists as far back as an analysis needs | partial |
| `integration_blockers` | Why it is not integrated | almost never recorded |
| `documentation_available` / `documentation_link` | Nothing, if empty on every row | check whether anyone fills them |

**The blank-status trap.** Rows are `INTEGRATED`, `NOT INTEGRATED`, `INTEGRATION ONGOING` - and a
sizeable block carries nothing at all. A blank is not a no. Reading it as one turns part of the
estate into a fabricated gap, and the fabricated gap gets routed to a lane that then finds
nothing to do. Count the blanks live and report them as "not recorded".

**`INTEGRATED` with no `integration_method`.** Such machines were integrated by a route nobody
recorded, so the ingress variant - and with it what is actually published - cannot be inferred
from the row. Filter for it live.

## Connector Overview

Step 3, and it needs reading twice. A connector existing is not a connector you may use. Read
the `status` and `utilization` of each:

| State | Meaning |
|---|---|
| `Productive` and marked `USE` | May be used |
| `Idea` | A roadmap item, not a route to data |
| `Development` | Not yet usable |
| `NOT AVAILABLE` | Not usable |
| `DO NOT USE` | Explicitly excluded |

Match on `input_protocol` and the vendor, then check `status` and `utilization` before
reporting the step as passed.

**A vendor field that is not a vendor.** `plc_vendor` sometimes holds a note or an interface
name (for example `S7.Schnitt.`, a German note meaning "S7 interface") or an abbreviation of a
bus or product, not a manufacturer. Such machines match no connector, which reads as a
connector gap and is a data-entry gap. List the values that match no known manufacturer; fix
the row; do not raise a barrier.

## Node-RED flow corpus

Step 4, and it is the only source in the bundle that says anything about an individual
**signal** rather than a machine. A signal name appearing in a deployed flow is strong
evidence it exists at that plant.

**A flow proves presence and never absence.** A signal can be published to the edge platform
with nothing consuming it, so "not in any flow" is a prompt to check the platform, not a
verdict. The script says `unproven`, not `absent`, and the difference matters: one is a
question for the platform, the other is a request to another lane.

**Coverage is partial by plant.** Some plants have no Node-RED instance in the corpus; for
those, step 4 cannot be answered from the bundle at all. Derive the list live as described in
`plant-instance-map.md`.

## Use case portfolio and reference library

Step 6. Matching is on the name and the target text, so a use case that solves the same
problem under a different name is missed. The check is worth running anyway: **adoption is
what the department is short of, not templates.**

## Databricks and the Azure Storage Account

Step 5, and **nothing in the bundle stands in for them.** Granularity, freshness and
completeness per signal are recorded in no source here. This is the step most often assumed,
and the assumption is discovered after the analysis has been delivered.

The script reports step 5 as unproven every single time, deliberately. A tool that guessed
here would be worse than one that admits it cannot see.
