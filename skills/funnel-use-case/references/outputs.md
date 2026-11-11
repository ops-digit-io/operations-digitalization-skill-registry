---
type: Skill Reference
title: Outputs
description: The outputs funnel-use-case must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`funnel-use-case` delivers one defined use case: a filled protocol that a plant engineer who was not in the room can
read to see what was decided, why, and what is open. A title is not a definition.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Filled definition protocol | `assets/use-case-definition-protocol.md`, one per use case, four phases | `funnel-requirements`, `mi-data-availability`, `bc-build`; Plant ME | All four control points are met: demand logged against the plant roadmap, use case scoped with a clear objective, system assessment complete, business case and priority agreed with Plant ME |
| Use-case record fields | Fields in the protocol and the use case record | `bc-build`, `deploy-handover` | Plant, material family and process group, capability, category, output asset, utilization expectation, named plant owner and every known dependency are filled; an unknown field is marked unknown |
| Benefit statement | Section of the protocol | `bc-build` | Business benefit (not the technical enabler) stated and classified tangible/intangible and cashable/non-cashable; rejected options named; the business or process change and who confirms it named |
| Data-source split and dependencies | Section of the protocol | `mi-data-availability` | Machine(s) named or confirmed none; data points split by source (machine, checklist or manual, system) per process step; dependencies recorded on the record |

## Handoff

- **Also receives from:** `dept-governance`: Use-case sprint plan and review.
- **Also receives from:** `ops-event-model`: Event definition canvas.
- **Receives from:** `dept-intake` (the accepted plant demand, a SMART statement and the plant owner).
- **Next in the flow:** `funnel-requirements` and `mi-data-availability` (step 22), then `funnel-prototype`
  (step 23) and `bc-build` (step 24). The skill's own handoff names `mi-equipment` (with business
  case and requirement breakdown, via `catalog-standardization` first) and `deploy-handover` (step 26).
- **Stops here when:** the need is not one need (split it), no business case can be named (refuse per intake and return it
  to the demand owner), a library entry matches (take it through `catalog-standardization`), or the machine is not
  connected (no use case yet; integration request).
