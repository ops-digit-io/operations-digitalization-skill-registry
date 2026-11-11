---
type: Skill Reference
title: Outputs
description: The outputs mi-equipment must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`mi-equipment` decides how machines get connected: per plant or wave (Route A) and per machine (Route B). It
delivers a route, a connector, a sequence position and a record of barriers, never a connection made by an agent.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Plant readiness brief | `assets/plant-readiness-brief.md`, filled before either route | Plant ME, Plant IT | Plant row, flags and plant-only questions are filled from the Machine List and Tool Overview |
| Assessment protocol (Route A) | `assets/assessment-protocol.md`, one per plant or wave | Plant ME, Plant IT; then Route B per machine | Inventory and roadmap agreed; each machine in scope carries concept, connector and sequence position; barriers logged; investment planned; Cyber Security gate identified |
| Guidance protocol (Route B) | `assets/guidance-protocol.md`, one per machine | `mi-signals`, `deploy-acceptance`, `mi-flow` | Gates 0 to 4 recorded in order; concept, connector, sequence position, logged barriers and Cyber Security status stated |
| Records updated | Machine List, Machine CV and Edge Device List | MPEE OD (informed) | All three updated; `INTEGRATED` set only after `deploy-acceptance` passes |
| Investment for approval | Sized investment from Route A step 6 | `dept-decision-rights` | Investment sized and taken through integration investment planning |

## Handoff

- **Also receives from:** `funnel-evaluation`: Sequenced gaps with owner.
- **Also receives from:** `catalog-systems`: System match record.
- **Receives from:** `dept-context` and `mi-data-availability` (Machine List export, accepted or planned use cases, roadmap, readiness matrix); on Route B, a Route A inventory row for the machine. For step 1b3, the approved cost template from `dept-decision-rights` (step 1b2).
- **Next in the flow:** `mi-signals` (tag list, PLC program version, Machine CV), `mi-flow` (pipeline, step 3b4) and `deploy-acceptance` (step 3b6). Steps in `process.yaml`: 1b3, 3b4, 3b5 (also 3a.2 for a self-developed app).
- **Stops here when:** no route exists (log the barrier and escalate into the roadmap, never omit the machine silently), a guide branch is `TODO` (say which, take the other platform's route if written, else escalate to the IIAE), or Cyber Security sign-off is missing (the machine waits for go-live). Only a human connects a machine; never mark `INTEGRATED` before acceptance passes.
