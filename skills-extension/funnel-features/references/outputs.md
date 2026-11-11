---
type: Skill Reference
title: Outputs
description: The outputs funnel-features must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`funnel-features` delivers the feature definition of one accepted requirement: one epic with at least two stories that stand alone, and the handoff file the next stage reads. The skill is not done until the epic check shows zero blockers.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Epic with background | `assets/epic-and-stories.md`, filled (worked example: `assets/epic-and-stories.example.md`) | `od-benefit-calculation`, `od-prototype-poc` | Background names today with role and hour, the moment of use, the decision it changes and what it is not for; epic statement names a role and an outcome particular to this plant; both axes (capability, process) recorded |
| At least two user stories | Stories in the same file | `od-prototype-poc` | Each story has its own background, signals with verdict, Given/When/Then including one use-in-a-real-shift criterion, blockers and dependencies; none is cut by technical layer |
| Epic check result | `python3 scripts/check_epic.py` run on the file | Digital-Business-Value-Engineer (DBVE) | Zero blockers (exit 0 or 1; exit 2 means not ready) |
| Handoff file | The filled epic file, handed over | `od-benefit-calculation`, `od-prototype-poc` | Written before the next stage starts; the reasoning stays visible |

## Handoff

- **Receives from:** `od-requirements-breakdown` (the accepted requirement and its handoff). `od-context` is read first.
- **Next in the flow:** `od-benefit-calculation` (step 24) and `od-prototype-poc` (step 23). The skill is proposed on step 22 of `docs/new-state/process.yaml`.
- **Stops here when:** the requirement's handoff is not accepted, or the epic has one story only (one story that will not split is a story, not an epic), or the check shows blockers. A generated "so that" sentence that fits another plant's epic is not an outcome.
