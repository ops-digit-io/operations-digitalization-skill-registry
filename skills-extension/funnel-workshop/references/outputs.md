---
type: Skill Reference
title: Outputs
description: The outputs funnel-workshop must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`funnel-workshop` delivers the things a Use Case Definition or Integration Workshop needs: agenda with pre-read, a filled capture sheet, and a follow-up list with a summary. All are drafts; the DBVE facilitates and the Plant ME owns the plant side.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Agenda and pre-read | `assets/workshop-agenda-and-preread.md`, sent before the workshop | Workshop audience; Plant ME | Purpose, audience and timeframe were agreed with the plant and the pre-read went out, with the reason for the chosen format order |
| Workshop capture sheet | `assets/workshop-capture-template.md`, filled during the workshop | `funnel-use-case`, `dept-intake`, `bc-portfolio` | Legible to someone who was not present; every demand is logged against the plant roadmap or returned with a reason; savings figures marked with their basis as pre-evaluation |
| Follow-up list and summary | `assets/workshop-follow-up-list.md` | Plant ME; `bc-build`, `mi-equipment`, `catalog-standardization`, `funnel-first-aid` by item type | Every item is routed and has an owner role and a date, or is marked "open"; the summary reached the Plant ME |
| Utilization follow-up | Item in the follow-up list (integration workshops) | Plant ME | The utilization session at the next visit is scheduled |

## Handoff

- **Receives from:** `dept-intake` (plant demand), `bc-portfolio` (use case list and case groups for the plant), `funnel-requirements` and `invest-screen` (Lane 3 front-end).
- **Next in the flow:** Lane 2 step 21 (define and diagnose, with `funnel-use-case`) and Lane 3 step 31 (requirements). Items go to `funnel-use-case` or `dept-intake`, `mi-equipment`, `bc-build` (savings calculated as a follow-up), `bc-portfolio` (ranking), `catalog-standardization`, `funnel-first-aid`.
- **Stops here when:** the plant has an ad-hoc process issue and no use case (use `funnel-first-aid`, not a workshop), or an item would commit investment, machine integration or an external connection in the room. Such decisions are made elsewhere; record the rollout dependency instead.
