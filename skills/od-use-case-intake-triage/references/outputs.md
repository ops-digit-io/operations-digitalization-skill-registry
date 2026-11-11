---
type: Skill Reference
title: Outputs
description: The outputs od-use-case-intake-triage must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-use-case-intake-triage` delivers a one-line triage record for each request: accepted into exactly one lane, or refused with a reason and a route. It is the entrance to the process flow.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Triage record | One line per request, as in "Output of a triage" | The lane's entry skill: `catalog-usecase` (Lane 1), `od-use-case-definition` (Lane 2), `od-requirements-breakdown` (Lane 3), `od-first-aid-kit` (first-aid request) | Channel, exactly one lane, owner role, trigger satisfied, definition of done, priority basis (`UNKNOWN` is allowed), expected gate, known blockers |
| Expected gate | Field in the triage record | `od-decision-routing` | The gate is named at intake with its owner |
| Refusal | Reply to the demand owner | Demand owner | Gives the reason and the route (owning function); a refusal is returned, not dropped |
| System-fit flag | Note in the triage record | `od-system-fit-check` | Raised whenever the ask implies a system outside the lean footprint |

## Handoff

- **Also receives from:** `od-showcase-followup`: Routed reactions.
- **Receives from:** the request through one of the four channels (workshops, digital investment projects, COP, ad-hoc analytics or first-aid kit); `od-context` for terms and lanes.
- **Next in the flow:** step i1 to `od-system-fit-check` where needed, then `catalog-usecase` (Lane 1), `od-use-case-definition` (Lane 2, step 21), `od-requirements-breakdown` (Lane 3, step 31) or `od-first-aid-kit`.
- **Stops here when:** the request belongs to another function, has no plant-roadmap link or nameable business case, fails the SMART test, or needs a system outside the lean footprint. Return it to the demand owner with the reason and the route. Never record a priority that was inferred.
