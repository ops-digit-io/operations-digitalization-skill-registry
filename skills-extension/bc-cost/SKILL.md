---
name: bc-cost
description: >-
  Prepares the cost side of an OD business case and the investment input pack: one-time build, licences and hardware, recurring run cost and multi-year TCO for the minimum viable rollout and the maximum scale-out, each figure with a source or an open marker, the gates the spend must pass, and the open items. Use when a roadmap is agreed and the plant asks "what does this cost and who approves it", an equipment assessment lists machines that need hardware, a standardized system needs its cost template, or a capital request needs its cost side. Prepares input only; never approves or commits spend. Not for the value side (bc-build) or the request itself (bc-capital-request).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: bc-cost
  aliases: [od-investment-input]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Lane 1b (1b2), Lane 2 (24), Lane 3 front-end (33)"
  new_state_step: "Cost template, approved by the plant budget owner; Business case (value and cost), assessment, ranking; Business case, prioritization, capital request"
  department_names: ["bc-cost", "cost-template"]
  owner_role: human:jakob.gabriel
  authority_level: recommend
  status: draft
  requires: [dept-context]
  composes: [mi-equipment, dept-decision-rights, bc-build, invest-screen, deploy-cybersec, bc-capital-request, catalog-usecase]
  okf:
    type: Agent Skill
    title: Investment input pack
    tags: [information-integration-service, practice, new-state, draft]
---

# Cost side and investment input pack

- Read `dept-context` first.
- Naming: the skill is `bc-cost`; its deliverables are the **investment input pack** (a wave), the **Lane 1b cost template**, and the **investment estimate** (one case); all three are "the cost side".
- Skills may prepare the input, never the approval: the decision stays central.

## Purpose and definition of done

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.
- Turn an agreed plan into a cost side the deciders can read in one sitting: what is bought, what it costs (each figure with its source), which gates it passes, what is still unknown.
- Done when every cost line has a figure with a source or an open marker, the gate route is named, open items are listed with who closes them, and the pack is handed over with a decision request.
- It is never "done" by approval: approval is not this skill's.

## Which product

| Situation | Produce | Template |
|---|---|---|
| An equipment assessment lists machines that need hardware; the roadmap is agreed with Plant ME / Plant IT | Wave pack (investment input pack) | [`assets/investment-input-pack.md`](assets/investment-input-pack.md) |
| A standardized system matched by `catalog-usecase` (Lane 1b) | Lane 1b cost template; the plant budget owner approves it | [`assets/investment-estimate.md`](assets/investment-estimate.md) |
| One use case or system needs a capital request (Lane 2, Lane 3) | Investment estimate, handed to `bc-capital-request` | [`assets/investment-estimate.md`](assets/investment-estimate.md) |

- Default when unsure: the investment estimate for one case; produce one product per invocation.

## The cost side of a business case

- The department splits a business case into a value backbone (`bc-build`) and a separate **investment estimate**, which feeds the assessment and the capital request (`house-business-case-standard.md` of `bc-build`).
- The estimate holds one-time build effort, licences and hardware, recurring run cost, multi-year **TCO**, for the **minimum viable rollout** and the **maximum scale-out** (OD x IT, 2026-09-11).
- Every figure is tagged `[quote]`, `[assumption]` or `[market]`; floor and upside come from named drivers, not a single point.
- Run cost is written for the stated operating model and for who runs it (build-and-run, OpenSpec IT demand (external)); cloud and run-cost drivers are asked from IT, which carries them centrally today.
- **Lane 1b cost template:** for a standardized system the estimate is the predictable, pre-priced template, not a full business case, approved by the plant budget owner (route with `dept-decision-rights`).

## Procedure

1. **Confirm the plan is agreed.** Wave pack: the roadmap is agreed with Plant ME / Plant IT (control point of step 1).
   - Template or estimate: the match record of `catalog-usecase` exists.
   - Cost cannot be planned for a scope that is still moving; if scope is open, stop and say which part.
2. **Run the demand filter.** Keep only machines or systems that an accepted or planned use case needs (`mi-equipment`, assessment step 2), because a `NOT INTEGRATED` machine nobody waits for is not a line in the pack.
3. **Check the footprint.** If any line is a system outside the lean footprint, run `invest-screen` first; a line that adds a tool is a tool-rollout decision, not an investment line (see [`approval-route.md`](references/approval-route.md)).
4. **Build the cost lines** from [`references/cost-lines.md`](references/cost-lines.md).
   - One row per line, each with a figure and a source, or `⟨not known: who can supply⟩`.
   - Do not average and do not fill from a similar plant without saying so.
   - Do not price internal effort unless the OD lead says so.
5. **Put the benefit side next to it.** Link the `bc-build` rows. Show **tracked** and **proven** euros separately and never add them. If no saving row exists, write "to be collected" and stop short of a payback figure.
6. **Name the gates.** Spend goes through eCR (approver per the current approval policy; look up `dept-decision-rights` and the OD lead).
   - The budget threshold of the digitalization investment planning decision is still `⟨to confirm⟩`; do not guess it.
   - Add Cyber Security / OT (`deploy-cybersec`) for any external connection, and IT demand if the item touches a platform OD does not own.
7. **Record the dependencies** on the use case or saving rows (`ECR APPROVAL`, `ECR CREATION`, `MACHINE INTEGRATION`), so the wait is visible.
8. **State the open items** and who can close them (section "Still open" of the pack).
9. **Pre-handover check** (repeat until all hold):
   - [ ] Every cost line has a figure with a source, or an open marker with a named supplier.
   - [ ] Every figure carries `[quote]`, `[assumption]` or `[market]`.
   - [ ] The gate route is named; dependencies are recorded.
   - [ ] No payback or threshold is stated that no source gives.
10. **Hand over.** Fill a decision request (`dept-decision-rights`, `assets/decision-request.md`): row "Digitalization investment planning", owner OD lead together with BA Operations, mode Consultation, approval yes, not reversible, `authority_level` `recommend`. For Lane 2 and Lane 3, pass the cost side to `bc-capital-request`.

## Example

```text
Investment estimate, "line-state board, 3 machines" (fictional values, not company figures)
| Line                         | Scenario    | Figure          | Tag          | Source / supplier            |
| Edge device (large) x1       | min viable  | 5,000           | [quote]      | supplier quote (IIAE)        |
| Cabinet work and network drop| min viable  | 1,200-2,000     | [assumption] | plant maintenance estimate   |
| Connector development        | max scale   | not known       | open marker  | who: IIAE                    |
| Hosting / run per year       | min viable  | not known       | open marker  | who: Plant IT (ask IT)       |
| Internal effort              | -           | not priced      | -            | OD lead has not asked for it |
Payback: not stated (no saving row recorded: "to be collected")
```

## Output

- The filled pack or estimate.
- Its cost table and gate table are the parts a decider reads first; everything else is traceability.

## Human gate and AI-agent notes

- **An agent may**: draft the pack or estimate, tag figures, list open items, and prepare the decision request.
- **Stays with roles**: the OD lead together with BA Operations decides; the plant budget owner approves a Lane 1b cost template; Cyber Security signs off external connections.
- The agent never approves, commits, orders or promises a budget.

## Still open

- `⟨Budget threshold of the digitalization investment planning decision⟩`: the decision-rights table leaves it open. Supplier: OD lead.
- `⟨Unit costs for edge devices, OT hardware, licences, connector development⟩`: none are recorded in the sources read. Supplier: IIAE, from supplier quotes.
- `⟨The "lightweight approval" limit for a Lane 1b standardized system⟩`: the Lane 1 file names the approver (the plant budget owner) but no amount.
- `⟨Confirmed template⟩` for the investment plan.

## Pitfalls

| Pitfall | Why it matters |
|---|---|
| Planning a wave without checking that the plant can execute, the layout is stable and controller patch status is on the plan | Budget is spent on a wave that slips |
| Pricing a return before a baseline exists | A payback on a guessed baseline misleads the decider; the first line is the measurement layer |
| Planning a wave around a medium or small edge device | The recorded guidance says no approved small device exists (`mi-equipment`, decision paths) |
| Listing a connection with no Cyber Security route as "ready to schedule" | It will wait on sign-off and block the wave |
| Filling a unit price from memory or a similar plant | It becomes a number nobody can trace |
| Treating the pack as an approval | Approval is central and human |

## Do not

- Do not plan a wave without checking that the plant can execute, the layout is stable and controller patch status is on the plan.
- Do not price a return before a baseline exists; the first line is the measurement layer.
- Do not approve, commit, order, allocate resources or promise a budget; the pack recommends.
- Do not invent or interpolate a threshold, a unit price or a payback; use `⟨…⟩` and name who supplies it.
- Do not add tracked and proven euros, or present a benefit as proven (`bc-build`).
- Do not plan a wave around the medium or small edge device.
- Do not include a connection that has no Cyber Security route as "ready to schedule".

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References and assets

| File | Open when |
|---|---|
| [`references/cost-lines.md`](references/cost-lines.md) | Building the cost lines: where each figure must come from and how to size a wave from the live machine records |
| [`references/approval-route.md`](references/approval-route.md) | Naming the gates: who decides what, the open threshold, the overlap in the ladder, the dependencies to record |
| [`assets/investment-input-pack.md`](assets/investment-input-pack.md) | Producing the wave pack |
| [`assets/investment-estimate.md`](assets/investment-estimate.md) | Producing the cost side of one business case or the Lane 1b template; never netted into the value headline |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Planning workflow, cost calculator before the project, staged scope, wave-decision checks |
| [`references/outputs.md`](references/outputs.md) | Checking each output's recipient and completion rule |
| [`references/background.md`](references/background.md) | Plan row, skill-map notes, where the cost side sits; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
