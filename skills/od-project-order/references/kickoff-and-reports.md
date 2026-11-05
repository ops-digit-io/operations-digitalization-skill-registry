---
type: Skill Reference
title: Kickoff and reports
description: The kick-off workshop structure, the milestone report, the closure report and checklist, traffic-light rules, the project phases, and the intake variant for a customer-mandated program.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [project-support-consultancy, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Kick-off, milestone and closure

## Project phases

Initiation (project order, organisation, approval); planning (objectives, work packages, schedule, risks,
plan approval); execution (control, progress, risk); closure (hand over to the line organisation, lessons
learned). There is an approval at each phase.

## Kick-off workshop

About two half-days. The output is the approved project plan with its schedule.

1. Welcome.
2. Project order recap.
3. Initial situation.
4. Objectives: opportunities and risks, classification, main target, sub-targets, success criteria.
5. Work breakdown, responsibilities, timing, milestones. For a migration or standardisation project add the
   proposed architecture or migration strategy.
6. Review structure: communication rules, parking lot, open questions to the steering committee.
7. Project organisation.
8. Approval; wrap-up and workshop assessment.

Preparation: send the order as pre-read; bring the filled risk list; bring the open questions to the
steering committee. For workshop mechanics see `od-workshop-facilitation`. The same plan skeleton serves any
multi-month standardisation project.

## Milestone report

Status light; milestone plan; objectives; timing; costs (plan, actual accumulated per milestone, forecast,
difference); five major risks each with countermeasure, owner, due date; lessons learned (topic,
experience, proven solution, originator); organisation changes; items for approval (prepared before the
meeting) and decisions (filled in during); approval.

## Closure report

The milestone content plus a **closure checklist**, including "handover completed: yes or no", and
approval signatures. The handover itself is run by `od-handover-and-adoption` (three-question test, utilisation
expectation); the closure report records the result. Lessons go to `od-retro`. A formal closure meeting can
also be an agenda item inside an integration workshop.

## Traffic-light rules

| Light | Meaning | Who acts |
|---|---|---|
| Red | Out of plan, result endangered, steering decision required | Steering committee |
| Yellow | Minor deviation, corrective action in place | Project team |
| Green | According to the approved plan | None |
| Grey | Not applicable or no data | Project manager says why |

An agent may propose a light from plan versus actual; the project manager sets it. Red always triggers a
decision request (`od-decision-routing`) with the cost of not deciding.

## Pitfalls and lessons

- Milestone report without "items for approval" prepared beforehand: the meeting becomes a discussion, not a decision.
- Costs shown only as actual; forecast and difference are what the committee reads.
- Lessons learned written as complaints; write topic, what to keep or change, the proven solution, the originator.
- Closure without a handover answer: delivered is not adopted.

## Intake variant: customer-mandated program

Source support is thin, so treat this as a variant to confirm with the OD lead.

- **Different driver.** A customer mandates a digital process-control framework with staged compliance
  targets; the case is not driven by savings. The business-case chapter is replaced by the mandate, its stages
  and the customer's deadlines.
- **Hard external deadline.** A customer audit outranks internal plans; do not take a customer-facing line
  down before the audit.
- **KPIs.** Compliance progress per stage and on-time submission, not savings. Savings may still be reported,
  separately.
- **Cost.** For customer-driven packages the cost is built bottom-up per plant (for example vision systems,
  connectivity per machine, use-case realisation) and divided proportionally across the participating plants;
  each use case carries an "on risk" flag for details and for budget.
- **Foundations first.** Show cyber assessment status, data protection and, for AI, that no customer data is
  used for model training, before the request goes up.
- **Blocked program.** One page with the technical, commercial (supplier) and customer situation, a timeline,
  what was shown to the customer, and the options with three separate deadlines: decision date,
  infrastructure-change deadline, customer deadline; plus the named people who can support local IT.
  PROPOSAL: use this as the escalation attachment to the decision request.
- `<Intake branch and owner>`: the chain has no branch for this driver; confirm where a mandated program enters.
