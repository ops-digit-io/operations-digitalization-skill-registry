---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Purpose and definition of done

Two plants can connect a similar number of machines on a similar system landscape and still show very
different savings. The decks' working rule: **equal integration effort with little or no saving points to
people and method, not to technology**. This skill makes that visible per plant, decides how much central
support the plant gets, and writes the plant's next steps into a roadmap that a call can track.

Done when: (1) the comparison set is fair (procedure step 1); (2) each gap is placed on an Ishikawa branch
with evidence and a confidence label; (3) the plant has a tier (first mover or fast follower) with each
criterion answered; (4) the plant roadmap has one row per workstream with status and a call-for-action cell;
(5) the regional roadmap is updated from the plant rows; (6) open unknowns are listed with an owner role.

## Where it sits in the chain

Proposed step ids for the registry: spine (plant onboarding, rhythm) and 24.

## Outputs and hand-off: the text before outputs.yaml

`dept-plant-diagnosis` delivers the gap diagnosis for a plant, its tier, and the plant and regional roadmap rows with status and call for action. It holds no plant figures; they come from the live lists. Tier assignment and roadmap approval are human.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Plant gap diagnosis record | `assets/plant-gap-diagnosis-record.md`, filled | OD lead with the regional lead | Fair comparison set stated; each gap placed on an Ishikawa branch with evidence and a confidence label; open unknowns listed with an owner role |
| Tier proposal | Tier section of the record | OD lead with the regional lead | Plant tiered first mover or fast follower with each criterion answered |
| Plant roadmap | `assets/plant-roadmap-template.md`, filled | `metrics-scorecard` | One row per workstream with owner role, target date, status colour and call-for-action text; no row green without named evidence |
| Regional roadmap | Regional roll-up table in the same asset | `metrics-scorecard` | Updated from the plant rows; reported per region against plan, not as a blended number |
| Decision and escalation items | Rows flagged in the roadmap | `dept-decision-rights`, `dept-risk` | Tier or wave exceptions, resource requests and open risks (staffing, central IT commitment, key user loss) named with the rows that need a decision |

## Handoff

- **Receives from:** `dept-plant-onboarding` (plant placed by starting profile, lists read on the day), `bc-portfolio` (savings by plant, tracked and proven apart), `mi-equipment` (barrier log), `catalog-compatibility` (compatibility verdict per plant).
- **Next in the flow:** `bc-portfolio` (tier as a capacity input and gap reasons at step 24), `metrics-scorecard` (call and strategy-round inputs), `catalog-compatibility` (a technical gap on a standard), `dept-decision-rights`, `dept-risk`, `dept-retro` (confirmed lessons).
- **Stops here when:** the facts are not read from the lists on the day, only zero reported saving is the evidence for "no potential" (only a human may decide that, after the scaling test), a row would be marked green without evidence, or a plant comparison would leave the department without approval.
