---
type: Skill Reference
title: Outputs
description: The outputs od-rollout-training must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-rollout-training` delivers a training package and a competence checklist for one plant and one solution. The plant confirms competence; the skill never does.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Training package | `assets/training-package.md`, filled | Plant owner, trainer role | One plant, one solution, one rollout moment; plant roles named (roles only); modules chosen with a hands-on form on the real screen, machine or shift; durations, dates and trainers marked `⟨…⟩` unless a source gives them; readiness stated |
| Competence checklist | `assets/competence-checklist.md`, filled | `od-handover-and-adoption` | Each competence confirmed by the plant owner with evidence; no critical skill rests on one person |
| Readiness statement | Readiness section of the package | Plant owner | Acceptance passed, data path written down to the machine, sign-off gate answered, plant infrastructure live; otherwise stated as not ready and no training scheduled |
| Gap report | Open competences and single-person skills listed | OD lead via COP | Every competence that cannot be confirmed, or skill held by one person, is reported upward |

## Handoff

- **Receives from:** `od-acceptance-test` (accepted solution), `od-handover-and-adoption` (the three-question test and ADKAR content it links to), `od-cybersec-gate` (sign-off status).
- **Next in the flow:** `od-handover-and-adoption` (the completed checklist is its input for the Knowledge and Ability elements; used on steps 1a3, 1b4, 26 and 3a6), then the Scorecard utilization rate for Reinforcement. Gaps go to the OD lead via COP.
- **Stops here when:** the solution is not accepted yet, the plant infrastructure is not live (no training on a demo environment), or only one plant person can do a critical task. Training may cover the Cyber Security gate while sign-off is open, with no live connection exercise.
