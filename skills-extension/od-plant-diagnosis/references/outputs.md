---
type: Skill Reference
title: Outputs
description: The outputs od-plant-diagnosis must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-plant-diagnosis` delivers the gap diagnosis for a plant, its tier, and the plant and regional roadmap rows with status and call for action. It holds no plant figures; they come from the live lists. Tier assignment and roadmap approval are human.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Plant gap diagnosis record | `assets/plant-gap-diagnosis-record.md`, filled | OD lead with the regional lead | Fair comparison set stated; each gap placed on an Ishikawa branch with evidence and a confidence label; open unknowns listed with an owner role |
| Tier proposal | Tier section of the record | OD lead with the regional lead | Plant tiered first mover or fast follower with each criterion answered |
| Plant roadmap | `assets/plant-roadmap-template.md`, filled | `od-scorecard-reporting` | One row per workstream with owner role, target date, status colour and call-for-action text; no row green without named evidence |
| Regional roadmap | Regional roll-up table in the same asset | `od-scorecard-reporting` | Updated from the plant rows; reported per region against plan, not as a blended number |
| Decision and escalation items | Rows flagged in the roadmap | `od-decision-routing`, `od-risk-watch` | Tier or wave exceptions, resource requests and open risks (staffing, central IT commitment, key user loss) named with the rows that need a decision |

## Handoff

- **Receives from:** `od-plant-onboarding` (plant placed by starting profile, lists read on the day), `od-portfolio-and-savings-analysis` (savings by plant, tracked and proven apart), `od-equipment-integration` (barrier log), `od-cross-plant-compatibility` (compatibility verdict per plant).
- **Next in the flow:** `od-portfolio-and-savings-analysis` (tier as a capacity input and gap reasons at step 24), `od-scorecard-reporting` (call and strategy-round inputs), `od-cross-plant-compatibility` (a technical gap on a standard), `od-decision-routing`, `od-risk-watch`, `od-retro` (confirmed lessons).
- **Stops here when:** the facts are not read from the lists on the day, only zero reported saving is the evidence for "no potential" (only a human may decide that, after the scaling test), a row would be marked green without evidence, or a plant comparison would leave the department without approval.
