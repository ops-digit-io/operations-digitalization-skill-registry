---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Where it sits in the chain

Small work does not need an order: a small change (few days of effort, budget available, standard
interface) goes through the ticket and change process; a project is what is larger, needs central budget
or a non-standard interface (`dept-decision-rights`). A small initiative uses the short form in
`assets/project-order.md` (`assets/project-order.md`).

## Outputs and hand-off: the text before outputs.yaml

`deploy-project-order` delivers the draft project order (PREQ) for a use case or system project, with the kick-off, milestone and closure forms. It drafts only; sponsor approval, budget and sign-off are human.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Project order (PREQ) | `assets/project-order.md`, filled, with the pre-send check run | Steering committee and sponsor | 30-second main target; budget estimate never blank; timing minimum; out-of-scope list; classified risks; named roles on both sides; unknowns written as `<...>`; approval documented with date |
| Flag list | List at the top of the draft | Project manager and sponsor | Every empty sponsor, lead, team, budget and out-of-scope field is listed, none filled by invention |
| Kick-off, milestone report and closure checklist | `assets/kickoff-milestone-closure.md`, filled | Steering committee | Kick-off yields a plan the steering committee approved; a milestone report at each milestone; closure checklist filled with "handover completed" answered yes or no |
| Risks with owner and due date | Risk section of the order | `dept-risk` | Every high risk has a treatment reflected in plan and budget |
| Lessons learned | Closure report entries (topic, experience, proven solution, originator) | `dept-retro` | Entries written at closure |
| Handover check | Closure checklist | `deploy-handover` | Handover check handed over at closure |

## Handoff

- **Receives from:** `funnel-use-case` (use case, scope, demand), `bc-portfolio`, `bc-build` (benefit rows with firmness), `bc-cost` and `bc-capital-request` (cost, option, funding gate), `dept-decision-rights`, `invest-screen` (tool decision, IT gate).
- **Next in the flow:** `bc-capital-request` (step 25, funding trail where money follows; also 33), OpenSpec IT demand (external) (step 3a4), `deploy-handover` (step 26, closure), `dept-retro`, `dept-risk`, `dept-decision-rights` for open questions to the steering committee.
- **Stops here when:** the work is a small change (few days of effort, budget available, standard interface), which goes through the ticket and change process with no order. Nothing is sent with a silent blank, and the order is not approved or signed by the skill.

## Sources of the chapter rules

- The references mark the registry's own rules as PROPOSAL; unmarked chapter rules are as the references state them.
- The pre-send check and the customer-mandated intake variant are PROPOSAL (this skill's own).
- Open question: the original source documents of the chapter rules are not named here; the department owner should add them.
