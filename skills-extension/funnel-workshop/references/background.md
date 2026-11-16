---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Outputs and hand-off: the text before outputs.yaml

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

## Provenance moved out of SKILL.md

The lane's recurring tasks list two workshops: the Use Case Definition Workshop (trigger: plant onboarding or a new demand wave; template "Standard Agenda - Use Case Workshop" on SharePoint) and the Use Case Integration Workshop (trigger: use case ready for integration; template "Use Case Integration Workshop agenda"). Both are intake channels: plant use-case demand is collected via these workshops. This skill produces the four things the plan asks for: agenda, pre-read, capture template, follow-up list.

## What is still open (open questions)

- Official integration workshop agenda template: the SharePoint template was not available; the skeleton in assets is distilled from past agendas. Supplier: DBVE.
- Lead times for scheduling, pre-read and the summary window: not set anywhere read. Supplier: OD lead.
- Attendance matrix per agenda item: in slide 2 of the deck; the text extraction loses empty cells, so it is not reproduced.
- What CBS stands for: the deck does not spell it out.
- Recorded outcomes of past workshops (which use cases went live afterwards): not traced. Supplier: DBVE, by filtering the live use case list on workshop source.
