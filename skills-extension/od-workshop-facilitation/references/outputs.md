---
type: Skill Reference
title: Outputs
description: The outputs od-workshop-facilitation must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-workshop-facilitation` delivers the things a Use Case Definition or Integration Workshop needs: agenda with pre-read, a filled capture sheet, and a follow-up list with a summary. All are drafts; the DBVE facilitates and the Plant ME owns the plant side.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Agenda and pre-read | `assets/workshop-agenda-and-preread.md`, sent before the workshop | Workshop audience; Plant ME | Purpose, audience and timeframe were agreed with the plant and the pre-read went out, with the reason for the chosen format order |
| Workshop capture sheet | `assets/workshop-capture-template.md`, filled during the workshop | `od-use-case-definition`, `od-use-case-intake-triage`, `od-portfolio-and-savings-analysis` | Legible to someone who was not present; every demand is logged against the plant roadmap or returned with a reason; savings figures marked with their basis as pre-evaluation |
| Follow-up list and summary | `assets/workshop-follow-up-list.md` | Plant ME; `od-benefit-calculation`, `od-equipment-integration`, `od-use-case-standardization`, `od-first-aid-kit` by item type | Every item is routed and has an owner role and a date, or is marked "open"; the summary reached the Plant ME |
| Utilization follow-up | Item in the follow-up list (integration workshops) | Plant ME | The utilization session at the next visit is scheduled |

## Handoff

- **Receives from:** `od-use-case-intake-triage` (plant demand), `od-portfolio-and-savings-analysis` (use case list and case groups for the plant), `od-requirements-breakdown` and `od-system-fit-check` (Lane 3 front-end).
- **Next in the flow:** Lane 2 step 21 (define and diagnose, with `od-use-case-definition`) and Lane 3 step 31 (requirements). Items go to `od-use-case-definition` or `od-use-case-intake-triage`, `od-equipment-integration`, `od-benefit-calculation` (savings calculated as a follow-up), `od-portfolio-and-savings-analysis` (ranking), `od-use-case-standardization`, `od-first-aid-kit`.
- **Stops here when:** the plant has an ad-hoc process issue and no use case (use `od-first-aid-kit`, not a workshop), or an item would commit investment, machine integration or an external connection in the room. Such decisions are made elsewhere; record the rollout dependency instead.
