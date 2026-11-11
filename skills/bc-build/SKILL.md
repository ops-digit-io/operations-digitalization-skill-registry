---
name: bc-build
description: >-
  Build the value side of an OD business case and keep the savings ledger honest: grounded figures, bankable vs assumed value, saving rows. Not for the capital request (bc-capital-request) or costs.
license: MIT
metadata:
  id: bc-build
  aliases: [od-benefit-calculation]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: [lane-2, lane-3]
  new_state_lane: "Lane 2 (24), Lane 3 front-end (33)"
  new_state_step: "Business case (value and cost), assessment, ranking; Business case, prioritization, capital request"
  department_names: ["bc-build", "bc-assess", "bc-value-model", "business-case-builder", "business-case-assessor", "bc-assess"]
  owner_role: Digital-Business-Value-Engineer (DBVE)
  tags: [practice, use-case-support-service]
  authority_level: draft on the business case; recommend on prioritization; never assert proven
  status: stable
  requires: [dept-context]
  composes: [dept-decision-rights, bc-portfolio, bc-cost, bc-capital-request]
  okf:
    type: Agent Skill
    title: Benefit calculation and savings
    tags: [practice, use-case-support-service]
---

# Benefit calculation and savings

Read `dept-context` first.

## Purpose

Builds and records the value side of an OD business case and keeps the savings ledger honest: saving rows with amount, year, category, rationale and methodology, tracked kept apart from proven. Use it when a use case is prioritized and needs a business case, when a saving needs recording or defending, or when a savings figure is about to leave the department.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Inputs and output

- **Inputs**: the business rationale (which operational loss disappears, where), sourced drivers and volumes from the area owner, plant Controlling for rates, and the cost side from `bc-cost`.
- **Output**: the value backbone ([`assets/business-case-backbone.md`](assets/business-case-backbone.md)) and one saving row per mechanism, with reliability, dependency and an assessment verdict.

## First estimate in five steps (for anybody with an idea)

You can make a rough estimate of what an idea might be worth before OD is involved. It is a **labelled range for your own understanding**, not a figure to publish, and it never goes on the savings ledger by itself. Terms (lever, baseline, bankable, tracked, proven) are explained in the vocabulary of `dept-context`.

1. **Name the loss, not the benefit.** Which operational loss would disappear (time, scrap, stops, rework), at which plant and in which process? A lever is a mechanism: "fewer hours spent reconstructing last shift" is one, "better visibility" is not. Common shapes: time recovered, earlier reaction, defects contained, output gained (only worth money if the extra units sell), a purchase avoided ([`references/savings-model.md`](references/savings-model.md)).
2. **Write it as value × driver.** For example: minutes saved per event × events per shift × shifts × working days × cost per hour. Name every factor.
3. **Source every factor, and tag it.** Ask the area owner for volumes and times, plant Controlling for the cost per hour, the machine list for machine counts; measure a few cycles yourself if nobody knows. Tag each factor `[input]` (from a source), `[assumption]` (your estimate: say why), `[market]` (a standard value used because none was given) or `[unknown]` (a crucial missing input: do not fill it with a guess).
4. **Give a range, not a point.** A conservative, a base and an optimistic value. A lever that rests on an `[unknown]` gets no number ("not banked") and becomes your first open question.
5. **Keep cost apart and ask for it.** Do not net a cost against the value. Ask OD for the cost side (`bc-cost`), and IT for the cost of running it: a project starts only with both. Then take your range to the DBVE; the ledger rules below apply only once saving rows are recorded.

**Fictional illustration of the arithmetic.** *This shows the method; the numbers are invented and are not a company figure. Never copy them into a ledger or a deck.* Fictional line F: 12 minutes saved per shift `[assumption]` × 3 shifts `[input]` × 220 working days `[assumption]` = 7,920 minutes = 132 hours a year; × a cost of 40 per hour `[market]` = 5,280 per year. Conservative (half the minutes): 2,640. Optimistic (one and a half times): 7,920. Cost to build and run: `[unknown]`, so no payback can be stated yet.

## The references are the substance

Each template, asset and other resource of this skill is listed here.

| File | Use it for |
|---|---|
| [`references/review-checklist.md`](references/review-checklist.md) | Why the methodology field is usually the one missing, the three fixes tried before the current one, and the smell test that follows from it |
| [`references/house-business-case-standard.md`](references/house-business-case-standard.md) | The department's own standard (bc-build, bc-assess, the shared value model): value-only backbone, grounding tags, expected / min / potential headline, lever register, de-banking, cost envelope, gated realization, and the OD x IT rules (bankable vs assumption-dependent, investment envelope, min viable rollout, max scale-out, TCO) |
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
`dept-decision-rights` for who owns each gate.

## Procedure

0. **Open the backbone** ([`assets/business-case-backbone.md`](assets/business-case-backbone.md)) and keep
   it value-only; ask `bc-cost` for the cost side. Tag every figure.
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
   policy (look up: `dept-decision-rights` and the OD lead).
7. Take the row to **SPRINT** if and when it is defensible. Only SPRINT makes it proven;
   OD asserting it does not.
8. **Separate bankable from assumption-dependent** and state the investment envelope, the minimum
   viable rollout and the maximum scale-out (OD x IT, 2026-09-11). No project starts without the
   value side here *and* the build and run cost from `bc-cost`.
9. **Assess before it goes on** (`bc-assess`, its rubric C1-C5 / D / E): grounded expected value, value
   and cost apart, every figure tagged, every de-banked lever an open question with an owner, gated
   milestones. Give the maturity verdict as a recommendation; the person who built the case does not
   sign it. Then `bc-capital-request` if money is needed.

## Definition of done

The business case and priority are agreed with Plant ME; every row carries an amount, a
year, a category, a business rationale, a reliability label, and — for a `CALCULATION` —
its methodology; any gate is recorded as a dependency with an owner. The backbone carries the
expected / min / potential headline with bankable and assumption-dependent value apart, the investment
envelope and the rollout scenarios, and an assessment verdict.

## Human gate and AI-agent notes

- **An agent may**: draft the backbone, write rows with their methodology, tag every figure, label a row `ESTIMATION` when the methodology is missing, and list open questions.
- **Stays with roles**: the DBVE owns the savings ledger; Plant ME agrees the priority; finance confirms a saving as proven through SPRINT; a person other than the case builder signs the maturity verdict. An agent never marks a row proven.

## Example

Fictional example (invented numbers, not a company figure):

```text
Row   : amount 5,280 per year (fictional), category time recovered, reliability CALCULATION
Method: 12 min x 3 shifts x 220 days x 40 per hour (inputs tagged)
Gate  : dependency ECR APPROVAL, owner = approval role
Report: tracked 5,280 | proven 0   (never summed)
```

If it fails: a `CALCULATION` row with no methodology fails the check and is relabelled `ESTIMATION`; an invalid or `[unknown]` factor gets no number.

## Do not

- Do not net value against cost, and do not release a figure without its grounding tag (input, assumption, market, unknown); see `references/process-chain-practice.md`.
- Do not average over two populations: split the estate by the variable that drives the economics first, and credit a lever only on the slice it can reach.
- Do not report a total that mixes tracked and proven euros.
- Do not fill a reliability field to make the ledger look complete; an empty field is
  honest, and a blank is better than a label nobody can defend.
- Do not invent savings or impact figures. Mark them **to-be-collected**.
- Do not read a missing figure as zero value - a use case without a figure was usually
  never assessed, rather than assessed at nothing.
