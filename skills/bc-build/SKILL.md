---
name: bc-build
description: >-
  Builds the value side of an OD business case and keeps the savings ledger honest: sources and tags every figure, separates bankable from assumption-dependent value, writes one saving row per mechanism with its calculation methodology, and records dependencies. Use when a use case needs a business case, someone asks "what is this worth", "how do I calculate the saving", or "can we put this on the savings list", or a savings figure is about to leave the department. Never marks a saving proven. Not for costs (bc-cost), scoring a case (bc-assess), ranking use cases (bc-portfolio) or the capital request (bc-capital-request).
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

- Read `dept-context` first.
- Terms used throughout: **bankable** value (grounded, counted) versus **assumption-dependent** value (rests on an `[assumption]` or `[unknown]`, shown as range, not counted). Terms are defined in `dept-context`.

## Purpose

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.
- Builds and records the value side of an OD business case and keeps the savings ledger honest: saving rows with amount, year, category, rationale and methodology, tracked kept apart from proven.
- Use it when a use case needs a business case, when a saving needs recording or defending, or when a savings figure is about to leave the department.

## Inputs and output

- **Inputs**: the business rationale (which operational loss disappears, where), sourced drivers and volumes from the area owner, plant Controlling for rates, and the cost side from `bc-cost`.
- **Output**: the value backbone ([`assets/business-case-backbone.md`](assets/business-case-backbone.md)) and one saving row per mechanism, with reliability, dependency and an assessment verdict.

## Which path

| Situation | Path |
|---|---|
| Somebody has an idea and wants a rough range for themselves | First estimate (below); nothing goes on the ledger |
| A use case needs a business case or a ledger row | Procedure (below); the first estimate is its steps 1-3 in short form |

## First estimate in five steps (for anybody with an idea)

- It is a **labelled range for your own understanding**, not a figure to publish, and it never goes on the savings ledger by itself.

1. **Name the loss, not the benefit.** Which operational loss would disappear (time, scrap, stops, rework), at which plant and in which process?
   - A lever is a mechanism: "fewer hours spent reconstructing last shift" is one, "better visibility" is not.
   - Common shapes: time recovered, earlier reaction, defects contained, output gained (only worth money if the extra units sell), a purchase avoided ([`references/savings-model.md`](references/savings-model.md)).
2. **Write it as value × driver.** Example: minutes saved per event × events per shift × shifts × working days × cost per hour. Name every factor.
3. **Source every factor, and tag it.** Ask the area owner for volumes and times, plant Controlling for the cost per hour, the machine list for machine counts; measure a few cycles yourself if nobody knows.
   - `[input]` from a source; `[assumption]` your estimate, say why; `[market]` a standard value used because none was given; `[unknown]` a crucial missing input, never filled with a guess.
4. **Give a range, not a point.** A conservative, a base and an optimistic value, because a point value hides how uncertain it is.
   - A lever that rests on an `[unknown]` gets no number ("not banked") and becomes the first open question.
5. **Keep cost apart and ask for it.** Do not net a cost against the value.
   - Ask OD for the cost side (`bc-cost`) and IT for the running cost: a project starts only with both.
   - Then take the range to the DBVE; the ledger rules below apply only once saving rows are recorded.

```text
Fictional line F (invented numbers, not a company figure; never copy into a ledger or deck)
12 min saved per shift [assumption] x 3 shifts [input] x 220 working days [assumption]
  = 7,920 min = 132 h per year
132 h x 40 per hour [market] = 5,280 per year
Conservative (half the minutes): 2,640 | Optimistic (1.5x the minutes): 7,920
Cost to build and run: [unknown] -> no payback can be stated yet
```

## The rule this skill exists to enforce

- **Tracked is not proven, and the two are never added together.**

| Term | Meaning |
|---|---|
| **Tracked** | What OD has recorded on the ledger, whatever its firmness |
| **Proven** | Only rows that passed the SPRINT portfolio review and that finance has formally confirmed |

- Any figure leaving the department says which of the two it is, and states the date of the live read, because quoting the first without the second loses the audience that matters.
- The ledger is **visibly incomplete**: many rows record no reliability, many use cases carry no figure. Treat the tracked total as a floor on what has been captured.
- Report two live counts next to any total: rows with blank reliability, and use cases without a row.

## What a saving row carries

| Field | What goes in it |
|---|---|
| Amount, year, category | The figure and when it lands |
| Business rationale | *Why* this saves money, in business terms |
| **Calculation methodology** | The formula, separately, e.g. (illustrative) *"<n> machines / <shifts> shifts / <minutes> per entry / <days> days"* |
| Reliability | `CALCULATION` · `ESTIMATION` · not recorded (blank is allowed and honest) |
| Proven | Has finance formally confirmed it through SPRINT? |
| Automated | Generated by a tool or keyed in by a person |
| Dependency | What has to happen before the saving is real |

- The methodology field is separate from the rationale on purpose: it makes a figure checkable by somebody who was not in the room.
- A `CALCULATION` row without its methodology is an estimation wearing the wrong label.
- Reliability, proven and automated answer different questions (formula behind it? finance-confirmed? generated or keyed?). Never collapse them into one "confidence".

## Dependencies: what the money is waiting on

- Not every row records a dependency. Count them live (filter the dependency field for non-blank).
- Value in this function is rarely blocked by the build.

| Dependency | Meaning |
|---|---|
| `NO DEPENDENCY` | Nothing has to happen first; stated explicitly |
| `ECR APPROVAL` | Waiting on an approval decision (governance gate) |
| `ECR CREATION` | The eCR itself has not been written yet (governance gate) |
| `PLANT` | Waiting on something the plant must do |
| `MACHINE INTEGRATION` | Waiting on machine connectivity |
| `OTHERS` | Anything else; say what in the comment |

- When a saving is gated, **record the gate on the row** rather than quietly dropping the number; see `dept-decision-rights` for who owns each gate.
- Re-count the distribution on the live ledger before quoting it.

## Procedure

0. **Open the backbone** ([`assets/business-case-backbone.md`](assets/business-case-backbone.md)) and keep it value-only; ask `bc-cost` for the cost side. Tag every figure.
1. Establish the **business rationale**: which operational loss disappears, at which plant, in which process.
2. Quantify it as one or more **rows**, each with amount, year and category.
   - One row per distinct saving mechanism; do not net effects together.
   - Use the lever types and formulas of the savings model ([`savings-model.md`](references/savings-model.md)): `value x driver`, every driver sourced.
   - When the case comes out of the product funnel, follow its business-case stage ([`funnel-business-case.md`](references/funnel-business-case.md)) and read the handoff files of the requirement and prototype stages rather than re-asking.
3. Write the **calculation methodology** for each row. If you cannot, the row is an `ESTIMATION`; label it so rather than upgrading it.
4. Record the **dependency**, if any, and who owns it.
5. **Prioritization** is not done here: hand the value rows to `bc-portfolio`, which ranks use cases with Plant ME against the plant roadmap.
6. **eCR routing** is not done here: if money is needed, hand over to `bc-capital-request` (the approver follows the current approval policy; look up `dept-decision-rights`).
7. Take the row to **SPRINT** if and when it is defensible. Only SPRINT makes it proven; OD asserting it does not.
8. **Separate bankable from assumption-dependent** and state the investment envelope, the minimum viable rollout and the maximum scale-out (OD x IT, 2026-09-11). No project starts without the value side here *and* the build and run cost from `bc-cost`.
9. **Pre-assessment check**, repeat until every item holds, then hand to `bc-assess`:
   - [ ] Every figure carries `[input]`, `[assumption]`, `[market]` or `[unknown]`.
   - [ ] Every row has a methodology, or is labelled `ESTIMATION`.
   - [ ] No cost is netted into the value; no `[unknown]` lever is summed into the headline.
   - [ ] Every gate is a dependency with a named owner.
10. **Assess before it goes on** (`bc-assess`, rubric C1-C5 / D / E). The maturity verdict is a recommendation; the person who built the case does not sign it. Then `bc-capital-request` if money is needed.

## Definition of done

- The business case and priority are agreed with Plant ME; every row carries an amount, a year, a category, a business rationale, a reliability label, and for a `CALCULATION` its methodology.
- Any gate is recorded as a dependency with an owner.
- The backbone carries the expected / min / potential headline with bankable and assumption-dependent value apart, the investment envelope and the rollout scenarios, and an assessment verdict.

## Human gate and AI-agent notes

- **An agent may**: draft the backbone, write rows with their methodology, tag every figure, label a row `ESTIMATION` when the methodology is missing, and list open questions.
- **Stays with roles**: the DBVE owns the savings ledger; Plant ME agrees the priority; finance confirms a saving as proven through SPRINT; a person other than the case builder signs the maturity verdict. An agent never marks a row proven.

## Example

```text
Row   : amount 5,280 per year (fictional), category time recovered, reliability CALCULATION
Method: 12 min x 3 shifts x 220 days x 40 per hour (inputs tagged)
Gate  : dependency ECR APPROVAL, owner = approval role
Report: tracked 5,280 | proven 0   (never summed)
```

## Pitfalls

| Pitfall | Why it matters |
|---|---|
| Quoting a total that mixes tracked and proven euros | The audience reads the sum as confirmed money |
| Reading a missing figure as zero value | A use case without a figure was usually never assessed, not assessed at nothing |
| Averaging over two populations | A lever only reaches part of the estate; split by the variable that drives the economics first |
| Filling reliability so the ledger looks complete | An empty field is honest; a label nobody can defend is not |
| Upgrading a row to `CALCULATION` without the formula | Nobody outside the room can check it |
| Summing a lever that rests on an `[unknown]` | The headline then depends on a guess; show it as a range, not banked |
| Counting output gained as value | Extra units are only worth money if they sell |

## Do not

- Do not net value against cost, and do not release a figure without its grounding tag (input, assumption, market, unknown); see `references/process-chain-practice.md`.
- Do not average over two populations: split first, and credit a lever only on the slice it can reach.
- Do not report a total that mixes tracked and proven euros.
- Do not fill a reliability field to make the ledger look complete.
- Do not invent savings or impact figures. Mark them **to-be-collected**.
- Do not read a missing figure as zero value.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/savings-model.md`](references/savings-model.md) | Choosing a lever type or formula, driver sources and ranges for a row |
| [`references/house-business-case-standard.md`](references/house-business-case-standard.md) | Writing the backbone headline: grounding tags, expected / min / potential, lever register, de-banking, cost envelope, OD x IT rules |
| [`assets/business-case-backbone.md`](assets/business-case-backbone.md) | Starting a case: the backbone to fill, one per case |
| [`references/review-checklist.md`](references/review-checklist.md) | A row looks suspicious or the methodology field is empty: the smell test |
| [`references/funnel-business-case.md`](references/funnel-business-case.md) | The case comes out of the product funnel (requirement, feature book, prototype handoffs) |
| [`references/deck-structure.md`](references/deck-structure.md) | A deck is requested: the slide order |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Segmenting before averaging, banked floor versus potential, baseline first, the handoff to ranking and capital request |
| [`references/background.md`](references/background.md) | Context, rationale, hand-off and notes; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
