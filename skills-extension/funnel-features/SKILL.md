---
name: funnel-features
description: >-
  Turn an accepted requirement into its feature definition - one epic with a background and at least
  two user stories that stand alone, each with testable acceptance and a use-in-a-real-shift criterion -
  the department's funnel-features, stage 2 of the product funnel between od-requirements-breakdown and the
  business case and prototype. Writes the handoff file the next stage reads and runs the epic check
  before handover. Use at Lane 2 step 22 once the requirement is accepted, when stories need cutting, or
  when an epic must be checked before it goes into the backlog.
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
  sources_read: 2026-11-10
  requires: [od-context]
  composes: [od-requirements-breakdown, od-benefit-calculation, od-prototype-poc]
  derived_from:
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/lane-2-develop-new-use-case.md (step 2 od-requirements-breakdown -> funnel-features), OD_Skill_Naming_Convention.md, skills-inventory-and-roadmap.md (product-funnel chain: handoff files, human gates), read 2026-11-10"
    - "Split from od-requirements-breakdown (formerly od-requirements-breakdown), 2026-11-10"
  okf:
    type: Agent Skill
    title: Funnel features
    tags: [department-core, lane-2]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Funnel features

Read `od-context` first. Stage 2 of the department's product funnel (`od-requirements-breakdown` → **`funnel-features`**
→ `od-benefit-calculation` → `od-prototype-poc`). The funnel's pattern: each stage writes a **handoff file** the next stage
reads, a stage does not start until the human approves or the handoff file exists, and the reasoning stays
visible.

**Input:** the accepted requirement from `od-requirements-breakdown`. **Output:** one epic with at least two stories
([`assets/epic-and-stories.md`](assets/epic-and-stories.md); passing worked example:
[`assets/epic-and-stories.example.md`](assets/epic-and-stories.example.md), read it before the blank), checked by
`python3 scripts/check_epic.py MyEpic.md` (exit 2 blockers, 1 warnings, 0 ready).

## The epic

| Part | Rule |
|---|---|
| Background, what it is used for | Prose: today with role and hour named, the moment of use, the decision it changes, why now, what it is *not* for; survives the requester leaving |
| Epic statement | As ⟨named role⟩, we want ⟨capability⟩, so that ⟨outcome particular to this plant⟩ |
| Both axes | Capability epic and process epic recorded; a query on one axis misses part of the portfolio |
| At least two stories | Each with its own background, signals with verdict, Given/When/Then incl. one use-in-a-real-shift criterion, blockers, dependencies |
| Epic acceptance | What is only true across the whole epic, or "all stories accepted" if honest |

The estate's story layer is hollow (generated stories share one "so that" sentence, few carry acceptance); detail in `epic-and-user-stories.md`. A "so that" that fits another plant's epic is the generated one with new words.


## Procedure

1. Read the requirement's handoff; stop if it is not accepted.
2. Choose the epic axis ([`references/epic-and-user-stories.md`](references/epic-and-user-stories.md)) and write the background.
3. Cut at least two stories by moment and role or by existing signals, never by technical layer.
4. Give each story testable acceptance and a use-in-a-real-shift criterion.
5. Run the check; zero blockers before the handoff to `od-benefit-calculation` and `od-prototype-poc`.

## Do not

- Do not cut stories by technical layer.
- Do not reuse a generated "so that" sentence; one that fits another plant's epic is the generated one.
- Do not hand over an epic with one story; one story that will not split is a story, not an epic.
