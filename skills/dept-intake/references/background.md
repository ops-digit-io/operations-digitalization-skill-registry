---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Example

Fictional example (all values invented for illustration):

If it fails: a request that fails the SMART test or has no roadmap link is invalid for admission; return it to the demand owner with the reason and the route.

## Outputs and hand-off: the text before outputs.yaml

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

## Dates moved out of SKILL.md

- On 2026-10-22 the department confirmed that there is no central ticket queue or mailbox: the four channels are the whole intake.
- On 2026-10-22 the department confirmed that the priority rule (measurable value against the roadmap, aligned with strategic-plant scope) has no further written formalization.
- The old-to-new service-line crosswalk lives in `dept-context` (`references/background.md`).
