---
type: Skill Reference
title: Outputs
description: The outputs dept-plant-onboarding must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`dept-plant-onboarding` delivers the onboarding path of one plant: the starting profile and a tracker that names, for each stage, the skill, the artefact and the deciding role. It is a route through existing skills and creates no new method.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Starting profile | Profile A, B, C or D recorded at the top of the tracker, read from the live plant record | OD lead, local key user | Region, machines recorded and integrated share noted with the read date; entry stage set from the profile |
| Onboarding path tracker | `assets/onboarding-path.md`, filled | OD lead, local key user | One row per stage (1 to 8) with skill, artefact, role, evidence and status; each stage has its artefact filed or an explicit reason it does not apply |
| Plant-side owner per lane | Owner roles in the tracker | OD lead | A plant-side owner is assigned for each lane the plant uses, or `⟨plant-side owner per lane⟩` is shown as open |
| Wait states | Status and evidence columns of the tracker | OD lead | Any stage that cannot start has its wait state recorded (investment approval, Cyber Security sign-off before go-live, decision on shared tooling); no stage is skipped |

## Handoff

- **Receives from:** `know-sharepoint-export` (the plant, machine and use-case lists), `dept-intake` (demands classified), `mi-equipment` (equipment assessment and barrier log).
- **Next in the flow:** `dept-plant-diagnosis` (tiering and roadmap when the plant enters scope), then the stage skills: `mi-equipment`, `dept-intake`, `catalog-usecase`, `deploy-handover`, `know-training`, and the routines `metrics-scorecard`, `dept-risk`, `dept-retro`.
- **Stops here when:** the plant is not recorded (stage 1 is the precondition for every comparison), or the stage order would be changed to meet a date. Record the wait state instead; a machine is never connected to an external system without Cyber Security / OT sign-off.
