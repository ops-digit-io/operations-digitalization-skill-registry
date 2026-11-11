---
type: Skill Reference
title: Non-bets
description: The department's own choice architecture — what is deliberately not pursued, and the kill criteria attached to the bets that are, so a system-fit judgement can cite the actual policy rather than a remembered version of it.
resource: ../SKILL.md
status: stable
tags: [practice, system-fit]
---
# Non-bets — the choice architecture behind this check

An agent can only filter a request if it knows what is deliberately *not* pursued. This is
the department's own strategy document's own framing, not this skill's.

## The trade-offs behind every non-bet below

| Chosen | Against | Because |
|---|---|---|
| A limited number of systems with a small operational footprint | Broad tool coverage | Lean, stable operations via flexible internal/external resources |
| Highly standardized, modular deployments | Bespoke per-plant solutions | Agility and maintainability — one plant's solution is takeable by the next |
| Maximal value-add with lowest dependencies | Maximal feature coverage | Agile use-case development, leverage already-deployed Smart Factory software |

## The non-bets themselves

- **No standardized MES rollout across the estate, short/mid-term** — ERP/S4HANA-dependent,
  and the pilot bet's own kill criterion is explicit: *"Kill if MES value-add not
  demonstrated"* against the existing MES plants used to gauge it.
- **EMS rollout paused until operational criteria are resolved** — as written in the strategy. See
  `references/tool-boundaries.md` for the possible discrepancy with the tool catalogue, which can
  show WiriTec as rolled out and used for energy use cases. Confirm current
  status before citing either version as settled.
- **OD does not build automation solutions** (that is Manufacturing Engineering's scope) **or
  own energy/facility topics** (Facility Management & Green Production's scope) — a request
  that is really an automation-build or a facility/energy-ownership ask belongs to
  `od-use-case-intake-triage`'s refusal list before it ever reaches this check.
- **No broad tool proliferation** — the footprint stays small. A proposed new tool is a
  system-fit question even when it is not MES/EMS-shaped.

## What is written vs. what is checked here

The non-bets are written. **The judgement this skill exists for is not the list itself —
it is recognizing when a request that does not name any of these systems quietly needs one
anyway.** A request rarely says "give us an MES"; it says "we need live cross-process
scheduling with full order genealogy," which is the same thing in different words. See
`references/tool-boundaries.md`'s per-tool "is not" lines for how to recognize it.

## Sources

Internal evidence, read 2026-10-22/23: `_knowledge/
OperationsDigitalization-Department/00-core/02-strategy.md` (the non-bets, bets and kill
criteria, verbatim) and `_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md`
(P-02's own scope statement: *"Does this require a system outside the lean footprint?
Applies the deployment reality: MES on hold (ERP-dependent), MSB limited, MIL not
deployed, EMS stopped"*). Full citations in `SKILL.md`'s `metadata.derived_from`.
