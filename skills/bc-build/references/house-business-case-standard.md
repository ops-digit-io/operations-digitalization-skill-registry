---
type: Skill Reference
title: House business case standard
description: "The department's own business-case standard (bc-build / bc-assess house rules and the shared value model): value-only backbone, grounding tags, expected / min / potential headline, lever register, contribution matrix, de-banking, cost envelope, gated value realization, scaling; plus the OD x IT business-case rules of 2026-09-11."
resource: ../SKILL.md
status: draft
tags: [business-case, value-model, department-standard, lane-2, lane-3]
---
# House business case standard

This registry's business-case chain maps onto the department's: **value** (`bc-build` + the shared
`bc-value-model`) is this skill; **cost** (`bc-cost`, the investment estimate) is `bc-cost`;
the **assessment verdict** (`bc-assess`) is the last step of this skill; the **capital request**
(`bc-capital-request`, eCR) is `bc-capital-request`. One value model, used by all four. Governance
stays separate from build: whoever builds the case does not sign it.

## The backbone

- **One living markdown backbone per case** (`assets/business-case-backbone.md`), edited by several
  people. The deck is a view compiled from it, never a second truth.
- **Value only.** Cost lives in the separate investment estimate and is never netted into the value
  headline.

## Grounding — every figure carries a tag

| Tag | Means |
|---|---|
| `[input]` | From the interview, mock-up or source |
| `[assumption]` | Our estimate |
| `[market]` | A market or standard value carried because none was provided; flagged, never left blank, added to the open items |
| `[unknown]` | A crucial missing input we refuse to fake |

## Headline

`~ EXPECTED <EUR> / plant / yr (min <floor> / potential <upside>)`. *Expected* is the grounded,
bankable value; *potential* adds any lever that is not banked yet. Rollout across sites is future
potential and never merged into the headline.

## Value calculation

- Every figure is **value × driver**, and every driver is one an area owner or Controlling can source
  (machines in the first area, cost per machine-hour, minutes per line). Averages of the first
  implementation area.
- **Lever register.** Every euro has a stable ID: H1, H2… for hard (high-confidence,
  employee-independent) levers, O1, O2… for optional levers. No lump sums; an unsplittable bundle is
  split illustratively and labelled so.
- **Hard and optional levers are never summed into one headline.**
- **Contribution matrix**: lever × conservative / base / optimistic, with a confidence per lever.
- **De-banking rule.** A high-impact lever resting on a crucial `[unknown]` gets no banked number: a
  ring-fenced sensitivity, labelled *not banked*, turned into the top open question.
- **Cost envelope.** While cost is unknown, state the one-time spend that still pays back within the
  department's payback horizon at each tier's value. When the investment estimate lands, the envelope
  becomes a payback.
- **Confidence map**: impact × confidence; the bankable value sits in the grounded region.

## Value realization

Gate the rollout (baseline at G0 → go-live → operating routine → prove and sustain → scale) and mark the
gate at which each lever's value unlocks, with the make-or-break condition per gate. Dates are set after
approval.

## Scaling

The saving factor is one plant, built bottom-up from the first implementation. Lead with the first
implementation; full rollout (per-plant value × sites from the machine and plant registers) is the
optimistic ceiling, shown as future potential.

## OD x IT rules (2026-09-11)

- **Bankable versus assumption-dependent.** Separate direct, bankable impact from benefits that depend
  on many assumptions. State the actionable impact, its dependencies and the **investment envelope**,
  so cases compare on value and opportunity cost.
- **No start without both sides.** A project does not begin without an estimate of business impact
  *and* of the cost to build and to operate it (`bc-cost`).
- **Rollout scenarios.** State a **minimum viable rollout** and a **maximum scale-out** scenario, the
  resources needed, cloud consumption and the longer-term **total cost of ownership**. Defining min and
  max deployment per use case is an open action item (OD lead and IT): mark ⟨to confirm⟩ until it is.
- **Cost transparency is IT's to give first.** IT carries cloud and run cost centrally today; ask IT for
  the cost drivers rather than estimating them silently, and keep infrastructure contracts central (no
  internal invoicing).

## Assessment verdict (bc-assess)

Before the case goes on, score it and give a maturity-gate verdict: is the expected value grounded, are
value and cost apart, does every figure carry a tag, is each de-banked lever an open question with an
owner, are the milestones gated. The department's rubric (core gates and criteria) lives in its
`bc-assess` package; until it is transcribed here, run these checks, record the verdict as
`recommend`, and attach the ranked open questions (normalized influence, grouped into blocks that one
conversation can close).
