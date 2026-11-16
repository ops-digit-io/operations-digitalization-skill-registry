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

`funnel-features` delivers the feature definition of one accepted requirement: one epic with at least two stories that stand alone, and the handoff file the next stage reads. The skill is not done until the epic check shows zero blockers.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Epic with background | `assets/epic-and-stories.md`, filled (worked example: `assets/epic-and-stories.example.md`) | `bc-build`, `funnel-prototype` | Background names today with role and hour, the moment of use, the decision it changes and what it is not for; epic statement names a role and an outcome particular to this plant; both axes (capability, process) recorded |
| At least two user stories | Stories in the same file | `funnel-prototype` | Each story has its own background, signals with verdict, Given/When/Then including one use-in-a-real-shift criterion, blockers and dependencies; none is cut by technical layer |
| Epic check result | `python3 scripts/check_epic.py` run on the file | Digital-Business-Value-Engineer (DBVE) | Zero blockers (exit 0 or 1; exit 2 means not ready) |
| Handoff file | The filled epic file, handed over | `bc-build`, `funnel-prototype` | Written before the next stage starts; the reasoning stays visible |

## Handoff

- **Receives from:** `funnel-requirements` (the accepted requirement and its handoff). `dept-context` is read first.
- **Next in the flow:** `bc-build` (step 24) and `funnel-prototype` (step 23). The skill is proposed on step 22 of `docs/new-state/process.yaml`.
- **Stops here when:** the requirement's handoff is not accepted, or the epic has one story only (one story that will not split is a story, not an epic), or the check shows blockers. A generated "so that" sentence that fits another plant's epic is not an outcome.

## Sources used in the improvement run

- None beyond the existing skill material; no vault or archive claim was added.
