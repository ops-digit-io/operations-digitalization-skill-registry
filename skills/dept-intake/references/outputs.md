---
type: Skill Reference
title: Outputs
description: The outputs dept-intake must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`dept-intake` delivers a one-line triage record for each request: accepted into exactly one lane, or refused with a reason and a route. It is the entrance to the process flow.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Triage record | One line per request, as in "Output of a triage" | The lane's entry skill: `catalog-usecase` (Lane 1), `funnel-use-case` (Lane 2), `funnel-requirements` (Lane 3), `funnel-first-aid` (first-aid request) | Channel, exactly one lane, owner role, trigger satisfied, definition of done, priority basis (`UNKNOWN` is allowed), expected gate, known blockers |
| Expected gate | Field in the triage record | `dept-decision-rights` | The gate is named at intake with its owner |
| Refusal | Reply to the demand owner | Demand owner | Gives the reason and the route (owning function); a refusal is returned, not dropped |
| System-fit flag | Note in the triage record | `invest-screen` | Raised whenever the ask implies a system outside the lean footprint |

## Handoff

- **Also receives from:** `comms-followup`: Routed reactions.
- **Receives from:** the request through one of the four channels (workshops, digital investment projects, COP, ad-hoc analytics or first-aid kit); `dept-context` for terms and lanes.
- **Next in the flow:** step i1 to `invest-screen` where needed, then `catalog-usecase` (Lane 1), `funnel-use-case` (Lane 2, step 21), `funnel-requirements` (Lane 3, step 31) or `funnel-first-aid`.
- **Stops here when:** the request belongs to another function, has no plant-roadmap link or nameable business case, fails the SMART test, or needs a system outside the lean footprint. Return it to the demand owner with the reason and the route. Never record a priority that was inferred.
