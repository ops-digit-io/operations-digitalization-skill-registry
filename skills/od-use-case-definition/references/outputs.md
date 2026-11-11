---
type: Skill Reference
title: Outputs
description: The outputs od-use-case-definition must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-use-case-definition` delivers one defined use case: a filled protocol that a plant engineer who was not in the room can
read to see what was decided, why, and what is open. A title is not a definition.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Filled definition protocol | `assets/use-case-definition-protocol.md`, one per use case, four phases | `od-requirements-breakdown`, `od-data-availability-check`, `od-benefit-calculation`; Plant ME | All four control points are met: demand logged against the plant roadmap, use case scoped with a clear objective, system assessment complete, business case and priority agreed with Plant ME |
| Use-case record fields | Fields in the protocol and the use case record | `od-benefit-calculation`, `od-handover-and-adoption` | Plant, material family and process group, capability, category, output asset, utilization expectation, named plant owner and every known dependency are filled; an unknown field is marked unknown |
| Benefit statement | Section of the protocol | `od-benefit-calculation` | Business benefit (not the technical enabler) stated and classified tangible/intangible and cashable/non-cashable; rejected options named; the business or process change and who confirms it named |
| Data-source split and dependencies | Section of the protocol | `od-data-availability-check` | Machine(s) named or confirmed none; data points split by source (machine, checklist or manual, system) per process step; dependencies recorded on the record |

## Handoff

- **Also receives from:** `od-governance-cadence`: Use-case sprint plan and review.
- **Also receives from:** `od-event-object-modelling`: Event definition canvas.
- **Receives from:** `od-use-case-intake-triage` (the accepted plant demand, a SMART statement and the plant owner).
- **Next in the flow:** `od-requirements-breakdown` and `od-data-availability-check` (step 22), then `od-prototype-poc`
  (step 23) and `od-benefit-calculation` (step 24). The skill's own handoff names `od-equipment-integration` (with business
  case and requirement breakdown, via `od-use-case-standardization` first) and `od-handover-and-adoption` (step 26).
- **Stops here when:** the need is not one need (split it), no business case can be named (refuse per intake and return it
  to the demand owner), a library entry matches (take it through `od-use-case-standardization`), or the machine is not
  connected (no use case yet; integration request).
