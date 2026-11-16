---
name: funnel-features
description: >-
  Turns an accepted requirement into a feature definition a backlog can take: one epic with a background
  and at least two user stories that stand alone, each with testable acceptance and a criterion for use
  in a real shift, plus an epic check before handover. Use when a requirement has been accepted and stories
  need cutting, when an epic or "so that" sentence reads like every other epic, or when an epic must be
  checked before it enters the backlog. Not for deriving the requirement itself (funnel-requirements),
  costing the value (bc-build) or proving the idea cheaply (funnel-prototype).
license: MIT
allowed-tools: Read Grep Glob Bash(python3 scripts/check_epic.py:*)
metadata:
  id: funnel-features
  tier: practice
  lane: [lane-2, lane-3]
  new_state_lane: "Lane 2 (22)"
  new_state_step: "Requirements, features and data check"
  department_names: ["funnel-features", "feature-funnel"]
  owner_role: Digital-Business-Value-Engineer (DBVE)
  authority_level: draft the epic and stories; run the check; the receiver accepts
  status: draft
  requires: [dept-context]
  composes: [funnel-requirements, bc-build, funnel-prototype]
  okf:
    type: Agent Skill
    title: Funnel features
    tags: [department-core, lane-2]
---
# Funnel features

- Read `dept-context` first.
- Position: Lane 2 step 22, after `funnel-requirements` and before `bc-build` and `funnel-prototype`.
- Pattern: each stage writes an **epic file** (the handoff) that the next stage reads, a stage does not start until the human approves or the epic file exists, and the reasoning stays visible.

## Inputs and output

- **Input:** the accepted requirement from `funnel-requirements`.
- **Output:** the epic file: one epic with at least two stories, from [`assets/epic-and-stories.md`](assets/epic-and-stories.md). Passing worked example: [`assets/epic-and-stories.example.md`](assets/epic-and-stories.example.md); read it before the blank.
- **Check:** `python3 scripts/check_epic.py MyEpic.md`. Exit 2: blockers (or file unreadable); 1: warnings; 0: ready.
- **Requirements:** Python 3.9 or newer, standard library only.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## The epic

| Part | Rule |
|---|---|
| Background, what it is used for | Prose: today with role and hour named, the moment of use, the decision it changes, why now, what it is *not* for; survives the requester leaving |
| Epic statement | As ⟨named role⟩, we want ⟨capability⟩, so that ⟨outcome particular to this plant⟩ |
| Both axes | Capability epic and process epic recorded; a query on one axis misses part of the portfolio |
| At least two stories | Each with its own background, signals with verdict, Given/When/Then incl. one use-in-a-real-shift criterion, blockers, dependencies |
| Epic acceptance | What is only true across the whole epic, or "all stories accepted" if honest |

- The estate's story layer is hollow: generated stories share one "so that" sentence and few carry acceptance (detail: `references/epic-and-user-stories.md`).
- A "so that" that fits another plant's epic is the generated one with new words.

## Procedure

1. Read the requirement's handoff; stop if it is not accepted, because stories written on a moving requirement are rewritten.
2. Choose the epic axis (`references/epic-and-user-stories.md`) and write the background.
3. **Cut stories by moment and role** (default): different people at different moments are different stories.
   - Alternative when signals decide: cut by signal availability, what exists today versus what waits on machine integration (`mi-data-availability`).
   - Never cut by technical layer.
4. Give each story testable acceptance and a use-in-a-real-shift criterion.
5. **Check loop.** Run `python3 scripts/check_epic.py MyEpic.md`, fix the blockers, run again until zero blockers; then read the warnings.
6. Hand the epic file to `bc-build` and `funnel-prototype`.

## Example (fictional)

```text
Epic:   As the shift leader of Plant A (fictional), we want hourly press downtime by reason,
        so that the 14:00 handover decides which press gets the maintenance slot.
Story 1 (moment and role: shift leader at handover; signals exist today)
        Given press 3 stopped twice this shift, When the leader opens the handover view at 13:50,
        Then both stops show reason and minutes. Real-shift criterion: used at three
        consecutive handovers without the clipboard.
Story 2 (process engineer at a quality escape; waits on a connectivity blocker)
        Depends on: machine integration of press 7.
Check:  0 blocker, 1 warn (story 2 has no signal verdict yet) -> add verdict, run again.
```

## Pitfalls

- **Cutting stories by technical layer** (connect, build flow, build dashboard). None is usable alone, so none can be accepted; they are tasks, not stories.
- **Reusing a generated "so that" sentence.** One that fits another plant's epic carries no outcome.
- **Handing over an epic with one story.** One story that will not split is a story, not an epic.
- **Leaving placeholders** (`⟨...⟩`) in the file. The check treats them as blockers, because they hide missing facts.
- **Skipping the use-in-a-real-shift criterion.** Acceptance in a test setup does not show the plant will use it.

## Human gate and AI-agent notes

- The agent drafts the epic and stories and runs the check; the receiver (`bc-build`, `funnel-prototype`) accepts, and the OD lead signs off.
- The agent never marks a requirement accepted and never invents the role, the hour or the decision the epic changes: ask the requester.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/epic-and-user-stories.md`](references/epic-and-user-stories.md) | Steps 2-4: choosing the axis, writing the background, cutting stories, acceptance, epic acceptance and sizing |
| [`assets/epic-and-stories.md`](assets/epic-and-stories.md) | You start a new epic file |
| [`assets/epic-and-stories.example.md`](assets/epic-and-stories.example.md) | Before writing: you want to see a passing epic |
| [`references/background.md`](references/background.md) | You need context, the required-output table or the handoff text; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
