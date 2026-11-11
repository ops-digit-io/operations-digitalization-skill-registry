---
name: od-project-order
description: >-
  Draft the project order (PREQ) for a use case or system project and run it through kick-off, milestone reports and closure - write the main target as a 30-second message, never leave the budget blank, split requesting side (steering committee, sponsor) from contracting side (project team, project manager), classify opportunities and risks, lay out the procurement milestone chain for a bought solution, run the kick-off workshop, and close with a closure report and handover check. Includes the intake variant for a customer-mandated program. Drafts only: sponsor approval, budget and sign-off are human. Use when a use case or system has passed its business case and needs a project order, when an initiative has an empty sponsor, budget or out-of-scope field, when a kick-off is due, or when a milestone or closure report is needed.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-project-order
  tier: practice
  lane: [lane-2, lane-3]
  new_state_lane: "Extension, deepens Lane 2 (25, 26), Lane 3 front-end (33), Lane 3a (3a4)"
  new_state_step: "Capital request if investment is needed; Implement, evaluate impact, ensure adoption, catalogue; Business case, prioritization, capital request; Build or integrate (3a.1 reuse, 3a.2 self-develop, 3a.3 external build, 3a.4 foreign app)"
  owner_role: human:jakob.gabriel
  authority_level: draft
  status: draft
  requires: [od-context]
  composes: [od-capital-request, od-decision-routing, od-investment-input, od-handover-and-adoption, od-retro, it-demand-package, od-risk-watch, od-workshop-facilitation, od-equipment-integration]
  okf:
    type: Agent Skill
    title: Project order
    tags: [project-support-consultancy, practice, new-state, draft]
---

# Project order

Read `od-context` first.

A project order (PREQ) is the steering committee's written request to a project team: what the project
must achieve, by when, for how much, and who answers for it. This skill drafts it, prepares the kick-off
that turns it into a project plan, and supplies the milestone and closure forms. It does not size the
benefit (`od-benefit-calculation`), package the money request (`od-capital-request`) or decide who may
approve (`od-decision-routing`); it names them at the right point.

Done when: the order has a 30-second main target, a budget estimate (never blank), a timing minimum, an
out-of-scope list, classified risks, named roles on both sides and a documented approval; unknowns are
`<...>`, not invented. For the kick-off: a plan that the steering committee approved. For closure: the
closure checklist is filled and "handover completed" is answered yes or no.

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Where it sits in the chain

| Step | Role of this skill |
|---|---|
| 25 Capital request, 33 Business case and capital | The order is the project-side twin of the money request: same scope, benefit and budget, written from the steering committee's view. Draft it from the same inputs; do not re-ask them. |
| 26 Implement and graduate, 3a4 to 3a6, 3b4 to 3b6 | Kick-off, milestone reports during the build, closure report at the end. |
| Spine | Lessons learned from closure feed `od-retro`. |

Small work does not need an order: a small change (few days of effort, budget available, standard
interface) goes through the ticket and change process; a project is what is larger, needs central budget
or a non-standard interface (`od-decision-routing`). A small initiative uses the short form in
[`assets/project-order.md`](assets/project-order.md).

## References and assets

| File | Use it for |
|---|---|
| [`references/order-structure.md`](references/order-structure.md) | PREQ chapters, rules per chapter (30-second target, sub-targets, success criteria, budget, timing minimum, out of scope), standard and extended variant |
| [`references/roles-risks-procurement.md`](references/roles-risks-procurement.md) | Requesting vs contracting side, risk classification and treatment, the limited-risk funding pattern, the procurement milestone chain |
| [`references/kickoff-and-reports.md`](references/kickoff-and-reports.md) | Kick-off workshop structure, milestone report, closure report, traffic-light rules, the customer-mandated program variant |
| [`assets/project-order.md`](assets/project-order.md) | The order template with `<fields>` and a pre-send check |
| [`assets/kickoff-milestone-closure.md`](assets/kickoff-milestone-closure.md) | Kick-off agenda, milestone report and closure checklist |

## Procedure

1. **Is it a project?** Apply the small-change rule above. Smaller: no order, ticket route. Larger or in an
   unfamiliar field: continue; an unfamiliar field gets the limited-risk pattern (fund a first step, time-box it).
2. **Collect inputs, ask nothing twice.** From the earlier steps: use-case definition and demand
   (`od-use-case-definition`), benefit rows (`od-benefit-calculation`), cost side and option
   (`od-investment-input`, `od-capital-request`), tool decision and IT gate (`od-system-fit-check`). Reuse
   earlier projects for the history and lessons-learned chapters and cite which.
3. **Write the 30-second main target**: who does what for whom with which intention, phrased "at the end of
   the project we will have ...". If it needs more than one breath, the scope is not settled.
4. **Fill the chapters** ([`order-structure`](references/order-structure.md)). Budget: always an estimate for
   internal effort, external support and consultancy, even for an internal project. Timing minimum: start,
   end, first version, first three milestones. Out of scope: write it, to avoid grey zones.
5. **Classify opportunities and risks** separately by probability times impact on scope, timing, financials
   and quality; every high risk gets a treatment whose effort is reflected in plan and budget
   ([`roles-risks-procurement`](references/roles-risks-procurement.md)). Always ask whether the team is
   available and trained.
6. **Name both sides.** Requesting: steering committee with sponsor. Contracting: project team with project
   manager. A missing sponsor, lead or team is stated as `<...>`, not invented.
7. **If a solution is bought,** lay out the procurement milestone chain and put the eCR in it (the money
   request itself is `od-capital-request`).
8. **Run the pre-send check** (end of [`assets/project-order.md`](assets/project-order.md)): empty budget,
   sponsor, owner, out-of-scope, unclassified high risk. Fix or flag each; send nothing with a silent blank.
9. **Approval is a human gate**, documented (signature, e-signature or e-mail) with date. After approval:
   kick-off workshop, which yields the project plan and the schedule.
10. **During the project:** a milestone report at each milestone; the project manager sets the status light,
    the steering committee decides on changes. **At the end:** closure report and closure checklist; hand
    over to the line organisation (`od-handover-and-adoption`), lessons to `od-retro`.

If the driver is a customer mandate rather than savings, use the intake variant in
[`kickoff-and-reports`](references/kickoff-and-reports.md).

## Handoff contract

| Receives | From |
|---|---|
| Use case, scope, owner, demand | `od-use-case-definition`, `od-portfolio-and-savings-analysis` |
| Benefit rows with firmness | `od-benefit-calculation` |
| Cost, option, funding gate | `od-investment-input`, `od-capital-request`, `od-decision-routing` |
| Tool or system decision, IT gate | `od-system-fit-check`, `od-system-fit-check` |

| Hands on | To |
|---|---|
| Approved order and plan | the project team; the funding trail to `od-capital-request` |
| Open questions to the steering committee, cost of not deciding | `od-decision-routing` (decision request) |
| Risks with owner and due date | `od-risk-watch` |
| Handover check at closure | `od-handover-and-adoption` |
| Lessons learned (topic, experience, proven solution, originator) | `od-retro` |

## AI agent operating notes

- **Can do:** draft the order from the initiative one-pager and prior projects; fill chapters; propose the
  risk classification; build the procurement chain; assemble the milestone report from plan and actuals;
  draft the closure report; run the pre-send check.
- **Required inputs:** the initiative one-pager or use-case record, benefit and cost rows with read dates,
  earlier project orders to reuse, the funding gate from `od-decision-routing`.
- **Must flag, never fill:** empty sponsor, lead, team, budget, out-of-scope. Write `<...>` and list them at the top.
- **Evidence to cite:** the earlier project reused for history and lessons learned; the source of every benefit and cost line.
- **Human gate:** sponsor approval of the order, budget authorisation, steering-committee approval of the plan,
  any status change to red, closure sign-off. The agent proposes a status light; the project manager sets it.
- **Hand over:** the draft plus the flag list to the project manager and sponsor; the approved order to
  `od-capital-request` where money follows.

## Still open

- `<Form and system of record for the order>`: the sources show the chapters, not where the order is stored.
- `<Approval limits>`: who may authorise what budget is `od-decision-routing`; this skill does not set thresholds.
- The check against empty fields and the customer-program variant are this skill's proposals (marked PROPOSAL in the references).

## Do not

- Do not leave the budget blank, and do not state a sub-target without work packages behind it.
- Do not invent a sponsor, lead, team, approval or date.
- Do not approve, sign or commit budget; do not set the status light.
- Do not present an earlier project's cost as this project's cost without saying so.
- Do not delete not-applicable chapters; hide them or move them to the back.
