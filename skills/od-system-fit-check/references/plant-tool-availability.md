---
type: Skill Reference
title: Plant tool availability
description: Guidance, no figures. How to read the live Tool Overview for one plant (status codes, empty cells, rollout years), count the use cases that name a tool, and handle disagreement with workshop tables - for step 3 of the system fit check.
resource: ../SKILL.md
status: draft
tags: [all, practice]
---

# Plant tool availability — how to get it live

Step 3 of the check is "check this plant's actual availability, not the estate average". The
record is the Tool Overview (one note per tool, each with a "Rollout History" line and a
rollout table by plant). This file does not reproduce it: a copy is stale the day after the
export. It tells you how to read it and what traps to expect.

## Where the truth lives

- Knowledge base `Graph/Tools` notes (source: the `ToolOverview-List` export) and `Graph/Plants`
  rollout blocks. Note the export date every time you quote a cell.
- Use cases naming a tool: the use case links in the `UseCase-List` export.
- Machine-side readiness: `../../od-equipment-integration/references/plant-integration-status.md`.

## Reading a cell

Status: `AVAILABLE`, `ONGOING`, `STOPPED (MANAGEMENT DECISION)`, `PLANNED` (next year, not
started), `NOT AVAILABLE`. Plus a rollout year (may be missing) and a free-text comment.

| Cell | Read as |
|---|---|
| Available + year | In the record as available. Still confirm with the plant if the decision is high-stakes |
| Ongoing | **Not** available. Say so |
| Stopped | A recorded management decision; the reason is in the comment. A constraint on a new request for the same tool at the same plant; challenge via `od-decision-routing`'s tool or system rollout row |
| Planned | Not started |
| Not available | Say so, with the comment |
| No row for this plant | **Nobody recorded a decision.** Not the same as "not available". The answer is a question to the plant, not a finding |

## Traps to expect

1. **The tool a use case names is not the tool the plant has.** Use cases name tools
   aspirationally. Before accepting a use case that "uses" a tool, read the plant row.
2. **Version rows.** MDA/PDA, MSB and Energy Management exist in several versions with
   separate rows; read the right version. Where two forms of one tool note differ, take the
   union and say so.
3. **MES has very few rows.** This matches the non-bet; do not read a missing MES row as an
   oversight.
4. **Plants with no tool row at all** exist. For them "which tools are available" has no
   record. Ask the plant.
5. **Comments carry the real information:** stopped-because, handover with open topics,
   migration between hosting domains, "API might not be available", re-activation. Read them.
6. **The EMS discrepancy in `SKILL.md`.** The written non-bet position and the Energy
   Management rollout rows can disagree. Whether a "stopped" statement applies only to new
   plants is not stated in the notes read.
   ⟨Which of the two is the current department position. Who could supply it: OD lead.⟩

## How to count live

- Plants with a tool: filter the tool's rollout table by status; count distinct plants.
- Use cases naming a tool: count `UseCase-List` rows linked to the tool; split by use case
  status (idea / planned / implemented / productive) and by plant.
- Compare the two: a large gap between "plants that have it" and "plants whose use cases name
  it" is the signal of trap 1. Do not quote a count without its export date.

## Workshop tables versus the Tool Overview

The tables in `deployment-reality.md` are statements of one workshop
summary at one date; the Tool Overview is an export at another. They disagree in kind:
"ongoing" in a workshop but "available" later; a tool "ongoing, needed for multiple use cases"
in a workshop but without a row in the overview; a demo system deployed but "no use cases".

**Rule:** when table and workshop disagree, the verdict states both with their dates and asks
the plant. Neither wins by being newer.

## Using it in the check

1. Take the tool the need maps to (step 2 of the check).
2. Read the row for the plant, as above.
3. Note the machine side: a tool that needs machine data (MDA/PDA, MSB, RuleEngine) needs the
   plant's machines integrated.
4. Write the plant, the cell value and the export date into
   `../assets/system-fit-check.md`.

⟨Whether the Tool Overview is the department's reference for "available at plant", or the
workshop tool-availability tables. Who could supply it: OD lead.⟩

## Sources

- Knowledge base `Graph/Tools`, `Graph/Plants` rollout blocks.
- Registry reference `deployment-reality.md`.
