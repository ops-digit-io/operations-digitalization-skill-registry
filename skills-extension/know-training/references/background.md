---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Status and sourcing of this skill

Status: draft, and the thinnest-sourced skill in the registry. The skill map calls this "the decentralization skill" and says it "is under-specified in the current Department OS and needs the most new content". The sources give the control point ("rollout-ready; plant trained"), a few training facts from call decks, and the plant roles. They do not give a training standard, a list of modules or a competence model. The skill assembles a package from what the neighbouring skills already teach, and every proposal that is not a recorded fact is labelled proposal.

Open question for the OD lead: obtain the real training formats and the competence standard, then replace the proposals in the module catalogue and the hand-down model.

## Outputs and hand-off: the text before outputs.yaml

`know-training` delivers a training package and a competence checklist for one plant and one solution. The plant confirms competence; the skill never does.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Training package | `assets/training-package.md`, filled | Plant owner, trainer role | One plant, one solution, one rollout moment; plant roles named (roles only); modules chosen with a hands-on form on the real screen, machine or shift; durations, dates and trainers marked `⟨…⟩` unless a source gives them; readiness stated |
| Competence checklist | `assets/competence-checklist.md`, filled | `deploy-handover` | Each competence confirmed by the plant owner with evidence; no critical skill rests on one person |
| Readiness statement | Readiness section of the package | Plant owner | Acceptance passed, data path written down to the machine, sign-off gate answered, plant infrastructure live; otherwise stated as not ready and no training scheduled |
| Gap report | Open competences and single-person skills listed | OD lead via COP | Every competence that cannot be confirmed, or skill held by one person, is reported upward |

## Handoff

- **Receives from:** `deploy-acceptance` (accepted solution), `deploy-handover` (the three-question test and ADKAR content it links to), `deploy-cybersec` (sign-off status).
- **Next in the flow:** `deploy-handover` (the completed checklist is its input for the Knowledge and Ability elements; used on steps 1a3, 1b4, 26 and 3a6), then the Scorecard utilization rate for Reinforcement. Gaps go to the OD lead via COP.
- **Stops here when:** the solution is not accepted yet, the plant infrastructure is not live (no training on a demo environment), or only one plant person can do a critical task. Training may cover the Cyber Security gate while sign-off is open, with no live connection exercise.
