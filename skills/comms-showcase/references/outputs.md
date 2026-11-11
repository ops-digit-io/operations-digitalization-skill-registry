---
type: Skill Reference
title: Outputs
description: The outputs comms-showcase must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`comms-showcase` (step 41) delivers one verdict, go, hold or no, on whether a live, adopted use case may be told to
the rest of the company, and which claims it may carry.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Selection record with verdict | `assets/selection-record.md`, one per use case | `comms-brief` on a go; OD lead otherwise | One verdict (go, hold or no) with the reason; all six gate steps worked in order |
| Claims with evidence class | Claims section of the selection record | `comms-brief` | Each claim carries one class (`CALCULATION` with its method, `ESTIMATION`, or `not yet assessed`) and is worded as a result only with a registered plant savings project and baseline, else as a claim |
| Audiences | Audience section of the selection record | `comms-brief` | Audiences named, each with what it should do next |
| Plant owner consent | Written consent noted in the record | Plant owner | Owner agrees in writing to be named as the plant (not a person) and to the claims |
| Open points with owners | List in the selection record | OD lead | Each missing item on a hold has a named owner |

## Handoff

- **Receives from:** `deploy-handover` (handover record, `PRODUCTIVE` status and confirmed adoption), `bc-build` (savings status), and the plant owner.
- **Next in the flow:** `comms-brief` (step 42) on a go.
- **Stops here when:** the verdict is hold (adoption not confirmed, a needed figure still a claim, plant owner has not answered) or no (owner declines, use case not live, or the story needs a sensitive detail). Record the reason and the owner; do not retry through another channel.
