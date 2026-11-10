---
name: od-benefit-calculation
description: >-
  Build, assess and record the value side of an OD business case (the department's od-benefit-calculation and
  bc-assessment, one shared value model) and keep the savings ledger honest — a value-only backbone
  with grounded, tagged figures, an expected / min / potential headline, bankable value kept apart
  from assumption-dependent value, investment envelope, minimum viable rollout and maximum
  scale-out; write saving rows with their amount, year, category, business rationale and
  calculation methodology; classify each as calculation or estimation; record what the
  money is waiting on; and never merge tracked euros with finance-proven ones. Use when a
  use case is being prioritized and needs a business case, when a saving needs recording
  or defending, when someone asks what a use case or the portfolio is worth, or when a
  savings figure is about to leave the department.
license: MIT
metadata:
  id: od-benefit-calculation
  tier: practice
  lane: [lane-2, lane-3]
  new_state_lane: "Lane 2 (24), Lane 3 front-end (33)"
  new_state_step: "Business case (value and cost), assessment, ranking; Business case, prioritization, capital request"
  department_names: ["bc-build", "bc-assess", "bc-value-model", "business-case-builder", "business-case-assessor", "bc-assessment"]
  owner_role: Digital-Business-Value-Engineer (DBVE)
  authority_level: draft on the business case; recommend on prioritization; never assert proven
  status: stable
  sources_read: 2026-11-10
  requires: [od-context]
  composes: [od-decision-routing, od-portfolio-and-savings-analysis, od-investment-input, od-capital-request]
  derived_from:
    - "Work vault, OD Department Knowledge/OD-instance/30-skills/product-funnel-skills.zip (skills/business-case/SKILL.md, references/savings-model.md, deck-structure.md), read 2026-11-10"
    - ops-knowledge-graph/_knowledge/10-Department/Savings and value tracking.md
    - ops-knowledge-graph/_knowledge/10-Department/Decision rights.md
    - ops-knowledge-graph/.../20-lanes/use-case-support-service/{playbook,tasks}.md
    - personal vault, Work-OpsDigit-Knowledge/Split Slides/10-Workshops--2025-01-21-2.1-What_are_UseCases-Overview_Reporting_Bondaries*.pptx and --2024_04_04_Summary_Carei_SmartFactory_UseCase_Definition_Workshop*.pptx, read 2026-10-22 — resolves PHASE1-ELICITATION.md topic 3 (benefit-calculation review) from the department's own record.
    - "Work vault, OD Department Knowledge/OD-instance/Business-Cases (README, _template), OD_Skill_Naming_Convention.md, skills-inventory-and-roadmap.md, read 2026-11-10"
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/Transcripts/2026-09-11_OD-IT-alignment_meeting-notes.txt, read 2026-11-10"
  okf:
    type: Agent Skill
    title: Benefit calculation and savings
    tags: [practice, use-case-support-service]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---

# Benefit calculation and savings

Read `od-context` first.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/review-checklist.md`](references/review-checklist.md) | Why the methodology field is usually the one missing, the three fixes tried before the current one, and the smell test that follows from it |
| [`references/house-business-case-standard.md`](references/house-business-case-standard.md) | The department's own standard (od-benefit-calculation, bc-assessment, the shared value model): value-only backbone, grounding tags, expected / min / potential headline, lever register, de-banking, cost envelope, gated realization, and the OD x IT rules (bankable vs assumption-dependent, investment envelope, min viable rollout, max scale-out, TCO) |
| [`assets/business-case-backbone.md`](assets/business-case-backbone.md) | The backbone to fill, one per case |
| [`references/funnel-business-case.md`](references/funnel-business-case.md), [`references/savings-model.md`](references/savings-model.md), [`references/deck-structure.md`](references/deck-structure.md) | The department package's business-case stage of the product funnel (`bc-build`, master): building the value case from the requirement, feature book and prototype; the savings model (lever types, formulas, drivers, ranges); the deck order |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Segment before averaging, banked floor / potential / de-banked value, grounding tags, baseline first, the handoff to ranking and the capital request, and what an agent may draft |

A use case's value is recorded as **individual saving rows**, not as one number on the
use case. Count the rows and sum the amounts live on the savings ledger (look up: the OD
savings list, owned by the DBVE) - never quote a total from memory or from this skill.

## The rule this skill exists to enforce

**Tracked is not proven, and the two are never added together.**

- **Tracked** - what OD has recorded on the ledger, whatever its firmness.
- **Proven** - only the rows that passed the SPRINT portfolio review and that finance has
  formally confirmed.

Both are true statements about the same portfolio. Any figure leaving the department says
which of the two it is, and states the date of the live read. Quoting the first without the
second is the single easiest way to lose the audience that matters.

The ledger is also **visibly incomplete**: many rows record no reliability at all, and many
use cases carry no saving figure of any kind. Treat the tracked total as a **floor on what
has been captured**, not as a measure of what the portfolio is worth. To see how thin it is
today, filter the live ledger for blank reliability and for use cases without a row, and
report those two counts next to any total.

## What a saving row carries

| Field | What goes in it |
|---|---|
| Amount, year, category | The figure and when it lands |
| Business rationale | *Why* this saves money, in business terms |
| **Calculation methodology** | The formula, separately — e.g. (illustrative) *"<n> machines / <shifts> shifts / <minutes> per entry / <days> days"* |
| Reliability | `CALCULATION` · `ESTIMATION` · not recorded (blank is allowed and honest) |
| Proven | Has finance formally confirmed it through SPRINT? |
| Automated | Generated by a tool or keyed in by a person |
| Dependency | What has to happen before the saving is real |

The methodology field is separate from the business rationale on purpose: it is what
makes a figure checkable by somebody who was not in the room. A `CALCULATION` row without
its methodology is an estimation wearing the wrong label.

## Three separate claims about firmness

They answer different questions and are recorded separately:

1. **Reliability** — is there a formula behind it?
2. **Proven** — has finance formally confirmed it, through SPRINT?
3. **Automated** — was the row generated or keyed in?

Never collapse them into a single "confidence".

## Dependencies — what the money is waiting on

Not every row records a dependency (count them live: filter the dependency
field for non-blank). Value in this function is rarely blocked by the build. The values
in use:

| Dependency | Meaning |
|---|---|
| `NO DEPENDENCY` | Nothing has to happen first; stated explicitly |
| `ECR APPROVAL` | Waiting on an approval decision (governance gate) |
| `ECR CREATION` | The eCR itself has not been written yet (governance gate) |
| `PLANT` | Waiting on something the plant must do |
| `MACHINE INTEGRATION` | Waiting on machine connectivity |
| `OTHERS` | Anything else; say what in the comment |

Two of the values are governance gates and one is machine integration. Re-count the
distribution on the live ledger before quoting it. Two of the six are governance gates and one is machine integration. When a saving is
gated, **record the gate on the row** rather than quietly dropping the number — see
`od-decision-routing` for who owns each gate.

## Procedure

0. **Open the backbone** ([`assets/business-case-backbone.md`](assets/business-case-backbone.md)) and keep
   it value-only; ask `od-investment-input` for the cost side. Tag every figure.
1. Establish the **business rationale** — which operational loss disappears, at which
   plant, in which process.
2. Quantify it as one or more **rows**, each with amount, year and category. One row per
   distinct saving mechanism; do not net effects together. Use the lever types and formulas of the
   department's savings model ([`savings-model.md`](references/savings-model.md)): `value x driver`, every driver
   sourced. When the case comes out of the product funnel, follow its business-case stage
   ([`funnel-business-case.md`](references/funnel-business-case.md)) and read the handoff files of the
   requirement and prototype stages rather than re-asking.
3. Write the **calculation methodology** for each row. If you cannot, the row is an
   `ESTIMATION` — label it as such rather than upgrading it.
4. Record the **dependency**, if any, and who owns it.
5. Prioritize the use case by measurable value — savings, lead-time reduction, cost
   avoidance — against the plant roadmap, with Plant ME.
6. Route the spend through eCR; the approver for the amount follows the current approval
   policy (look up: `od-decision-routing` and the OD lead).
7. Take the row to **SPRINT** if and when it is defensible. Only SPRINT makes it proven;
   OD asserting it does not.
8. **Separate bankable from assumption-dependent** and state the investment envelope, the minimum
   viable rollout and the maximum scale-out (OD x IT, 2026-09-11). No project starts without the
   value side here *and* the build and run cost from `od-investment-input`.
9. **Assess before it goes on** (`bc-assessment`, its rubric C1-C5 / D / E): grounded expected value, value
   and cost apart, every figure tagged, every de-banked lever an open question with an owner, gated
   milestones. Give the maturity verdict as a recommendation; the person who built the case does not
   sign it. Then `od-capital-request` if money is needed.

## Definition of done

The business case and priority are agreed with Plant ME; every row carries an amount, a
year, a category, a business rationale, a reliability label, and — for a `CALCULATION` —
its methodology; any gate is recorded as a dependency with an owner. The backbone carries the
expected / min / potential headline with bankable and assumption-dependent value apart, the investment
envelope and the rollout scenarios, and an assessment verdict.

## Do not

- Do not net value against cost, and do not release a figure without its grounding tag (input, assumption, market, unknown); see `references/process-chain-practice.md`.
- Do not average over two populations: split the estate by the variable that drives the economics first, and credit a lever only on the slice it can reach.
- Do not report a total that mixes tracked and proven euros.
- Do not fill a reliability field to make the ledger look complete; an empty field is
  honest, and a blank is better than a label nobody can defend.
- Do not invent savings or impact figures. Mark them **to-be-collected**.
- Do not read a missing figure as zero value - a use case without a figure was usually
  never assessed, rather than assessed at nothing.
