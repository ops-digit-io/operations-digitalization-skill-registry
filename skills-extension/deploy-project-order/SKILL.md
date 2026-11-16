---
name: deploy-project-order
description: >-
  Drafts the project order (PREQ) a steering committee sends to a project team, then prepares the kick-off, milestone reports and closure report. Use when a use case or system has passed its business case and needs a project order, when an initiative sheet has an empty sponsor, budget or out-of-scope field, when a kick-off is due, or when a milestone or closure report is needed. Writes the main target as a 30-second message, keeps the budget filled, names the requesting and contracting sides, classifies risks and lays out the procurement milestone chain for a bought solution. Also covers a customer-mandated program. Drafts only: sponsor approval, budget and sign-off stay human. Not for sizing the benefit (bc-build), the capital request (bc-capital-request) or who may approve (dept-decision-rights).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: deploy-project-order
  aliases: [od-project-order]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: [lane-2, lane-3]
  new_state_lane: "Extension, deepens Lane 2 (25, 26), Lane 3 front-end (33), Lane 3a (3a4)"
  new_state_step: "Capital request if investment is needed; Implement, evaluate impact, ensure adoption, catalogue; Business case, prioritization, capital request; Build or integrate (3a.1 reuse, 3a.2 self-develop, 3a.3 external build, 3a.4 foreign app)"
  owner_role: human:jakob.gabriel
  authority_level: draft
  status: draft
  requires: [dept-context]
  composes: [bc-capital-request, dept-decision-rights, bc-cost, deploy-handover, dept-retro, dept-risk, funnel-workshop, mi-equipment]
  okf:
    type: Agent Skill
    title: Project order
    tags: [project-support-consultancy, practice, new-state, draft]
---

# Project order

## Purpose

- A project order (PREQ) is the steering committee's written request to a project team: what the project must achieve, by when, for how much, and who answers for it.
- This skill drafts it, prepares the kick-off that turns it into a project plan, and supplies the milestone and closure forms.
- It does not size the benefit (`bc-build`), package the capital request, called eCR (`bc-capital-request`), or decide who may approve (`dept-decision-rights`); it names them at the right point.
- Read `dept-context` first.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Inputs and output

- Inputs: the initiative one-pager or use-case record, benefit and cost rows with read dates, earlier project orders to reuse, the funding gate from `dept-decision-rights`.
- Output: the filled order (`assets/project-order.md`) with a flag list at the top, plus kick-off, milestone and closure forms (`assets/kickoff-milestone-closure.md`).
- Default form: the standard order. Switch to the short form only for a small initiative; add the extended chapters only for a larger or technical project.

## Where it sits in the chain

| Step | Role of this skill |
|---|---|
| 25 Capital request, 33 Business case and capital | The order is the project-side twin of the eCR: same scope, benefit and budget, written from the steering committee's view. Draft it from the same inputs; do not re-ask them. |
| 26 Implement and graduate, 3a4 to 3a6, 3b4 to 3b6 | Kick-off, milestone reports during the build, closure report at the end. |
| Spine | Lessons learned from closure feed `dept-retro`. |

## Procedure

- Copy this checklist into the draft and tick it:

```text
[ ] 1 project, not a small change   [ ] 2 inputs collected   [ ] 3 main target in one breath
[ ] 4 chapters filled               [ ] 5 risks classified   [ ] 6 both sides named
[ ] 7 procurement chain (if bought) [ ] 8 pre-send check clean or flagged   [ ] 9 approval by a human
```

1. **Is it a project?** A small change (few days of effort, budget available, standard interface) goes through the ticket and change process: no order. Larger, central budget or a non-standard interface: continue.
   - An unfamiliar field gets the limited-risk pattern (fund a first step, time-box it); open `references/roles-risks-procurement.md`.
2. **Collect inputs, ask nothing twice**, because the same facts already sit in earlier steps: use-case definition and demand (`funnel-use-case`), benefit rows (`bc-build`), cost side and option (`bc-cost`, `bc-capital-request`), tool decision and IT gate (`invest-screen`).
   - Reuse earlier projects for the history and lessons-learned chapters and cite which.
3. **Write the 30-second main target**: who does what for whom with which intention, phrased "at the end of the project we will have ...". If it needs more than one breath, the scope is not settled.
4. **Fill the chapters** (`references/order-structure.md`). Budget: always an estimate for internal effort, external support and consultancy, even for an internal project. Timing minimum: start, end, first version, first three milestones. Out of scope: write it, to avoid grey zones.
5. **Classify opportunities and risks** separately by probability times impact on scope, timing, financials and quality; every high risk gets a treatment whose effort is reflected in plan and budget. Always ask whether the team is available and trained.
6. **Name both sides.** Requesting: steering committee with sponsor. Contracting: project team with project manager. A missing sponsor, lead or team is stated as `<...>`, not invented.
7. **If a solution is bought,** lay out the procurement milestone chain and put the eCR in it (the eCR itself is `bc-capital-request`).
8. **Run the pre-send check** (end of `assets/project-order.md`): empty budget, sponsor, owner, out-of-scope, unclassified high risk. Fix or flag each, then run it again until it is clean or every finding is flagged; send nothing with a silent blank.
9. **Approval is a human gate**, documented (signature, e-signature or e-mail) with date. After approval: kick-off workshop, which yields the project plan and the schedule.
10. **During the project:** a milestone report at each milestone; the project manager sets the status light, the steering committee decides on changes. **At the end:** closure report and closure checklist; hand over to the line organisation (`deploy-handover`), lessons to `dept-retro`.

- If the driver is a customer mandate rather than savings, use the intake variant in `references/kickoff-and-reports.md`; it has its own KPI and is not forced through the savings test.

## Example: main target and pre-send check (fictional)

```text
Initiative: downtime dashboard for the press line at Plant North (fictional)
Main target: "At the end of the project the press line team at Plant North reads
  downtime by cause on one screen every shift, so they cut unplanned stops."
  Test: said aloud in one breath: yes.

Pre-send check result
[x] Budget: estimate given for internal effort and external support (value in the order)
[x] Timing: start, end, first version, three milestones
[ ] Out of scope: not written  -> flagged <out of scope, owner: project manager>
[ ] Sponsor: <sponsor, owner: OD lead>   -> flagged at the top of the draft
[x] High risk "line IT not available" has a treatment in plan and budget
[x] Each sub-target has at least three work packages
```

## Human gate and AI-agent notes

- An agent may draft the order from the one-pager and prior projects, fill chapters, propose the risk classification, build the procurement chain, assemble the milestone report from plan and actuals, draft the closure report and run the pre-send check.
- It must flag, never fill: an empty sponsor, lead, team, budget or out-of-scope. Write `<...>` and list them at the top.
- It cites the earlier project reused for history and lessons learned, and the source of every benefit and cost line.
- Humans decide: sponsor approval of the order, budget authorisation, steering-committee approval of the plan, any status change to red, closure sign-off. The agent proposes a status light; the project manager sets it.
- It hands over the draft plus the flag list to the project manager and sponsor, and the approved order to `bc-capital-request` where money follows.

## Handoff

| Receives | From |
|---|---|
| Use case, scope, owner, demand | `funnel-use-case`, `bc-portfolio` |
| Benefit rows with firmness | `bc-build` |
| Cost, option, funding gate | `bc-cost`, `bc-capital-request`, `dept-decision-rights` |
| Tool or system decision, IT gate | `invest-screen` |

| Hands on | To |
|---|---|
| Approved order and plan; funding trail | the project team; `bc-capital-request` |
| Open questions to the steering committee, cost of not deciding | `dept-decision-rights` (decision request) |
| Risks with owner and due date | `dept-risk` |
| Handover check at closure | `deploy-handover` |
| Lessons learned (topic, experience, proven solution, originator) | `dept-retro` |

## Still open

- `<Form and system of record for the order>`: the sources show the chapters, not where the order is stored.
- `<Approval limits>`: who may authorise what budget is `dept-decision-rights`; this skill does not set thresholds.
- The check against empty fields and the customer-program variant are this skill's proposals (marked PROPOSAL in the references).

## Pitfalls

- Blank budget "because it is internal": an empty field is read as zero cost and the project starts unfunded. Write an educated guess or `<...>` with an owner.
- Milestone report without items for approval prepared beforehand: the meeting becomes a discussion, not a decision.
- Costs shown only as actual: the committee reads forecast and difference.
- Closure without a handover answer: delivered is not adopted.
- Lessons learned written as complaints: write topic, what to keep or change, proven solution, originator.
- A sub-target with fewer than three work packages, or more than twelve sub-targets: the granularity is wrong.

## Do not

- Do not leave the budget blank, and do not state a sub-target without work packages behind it, because a target without work packages cannot be planned.
- Do not invent a sponsor, lead, team, approval or date; a made-up name reads as an approval that never happened.
- Do not approve, sign or commit budget; do not set the status light; both stay with the named humans.
- Do not present an earlier project's cost as this project's cost without saying so.
- Do not delete not-applicable chapters; hide them or move them to the back, so the next reader sees they were considered.

## Definition of done

- The order has a 30-second main target, a budget estimate (never blank), a timing minimum, an out-of-scope list, classified risks, named roles on both sides and a documented approval; unknowns are `<...>`, not invented.
- For the kick-off: a plan that the steering committee approved.
- For closure: the closure checklist is filled and "handover completed" is answered yes or no.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References and assets

| File | Open when |
|---|---|
| [`references/order-structure.md`](references/order-structure.md) | You fill the chapters (step 4), pick standard, short or extended form, or test the main target and sub-targets |
| [`references/roles-risks-procurement.md`](references/roles-risks-procurement.md) | You name both sides (step 6), classify risks (step 5), plan an unfamiliar field, or lay out the procurement chain (step 7) |
| [`references/kickoff-and-reports.md`](references/kickoff-and-reports.md) | A kick-off, milestone report or closure report is due (steps 9 and 10), or the driver is a customer mandate |
| [`assets/project-order.md`](assets/project-order.md) | You write the order or run the pre-send check |
| [`assets/kickoff-milestone-closure.md`](assets/kickoff-milestone-closure.md) | You prepare a kick-off agenda, milestone report or closure checklist |
| [`references/background.md`](references/background.md) | You want the context, the sources of the chapter rules or the full handoff text; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
