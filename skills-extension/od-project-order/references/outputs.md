---
type: Skill Reference
title: Outputs
description: The outputs od-project-order must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-project-order` delivers the draft project order (PREQ) for a use case or system project, with the kick-off, milestone and closure forms. It drafts only; sponsor approval, budget and sign-off are human.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Project order (PREQ) | `assets/project-order.md`, filled, with the pre-send check run | Steering committee and sponsor | 30-second main target; budget estimate never blank; timing minimum; out-of-scope list; classified risks; named roles on both sides; unknowns written as `<...>`; approval documented with date |
| Flag list | List at the top of the draft | Project manager and sponsor | Every empty sponsor, lead, team, budget and out-of-scope field is listed, none filled by invention |
| Kick-off, milestone report and closure checklist | `assets/kickoff-milestone-closure.md`, filled | Steering committee | Kick-off yields a plan the steering committee approved; a milestone report at each milestone; closure checklist filled with "handover completed" answered yes or no |
| Risks with owner and due date | Risk section of the order | `od-risk-watch` | Every high risk has a treatment reflected in plan and budget |
| Lessons learned | Closure report entries (topic, experience, proven solution, originator) | `od-retro` | Entries written at closure |
| Handover check | Closure checklist | `od-handover-and-adoption` | Handover check handed over at closure |

## Handoff

- **Receives from:** `od-use-case-definition` (use case, scope, demand), `od-portfolio-and-savings-analysis`, `od-benefit-calculation` (benefit rows with firmness), `od-investment-input` and `od-capital-request` (cost, option, funding gate), `od-decision-routing`, `od-system-fit-check` (tool decision, IT gate).
- **Next in the flow:** `od-capital-request` (step 25, funding trail where money follows; also 33), `it-demand-package` (step 3a4), `od-handover-and-adoption` (step 26, closure), `od-retro`, `od-risk-watch`, `od-decision-routing` for open questions to the steering committee.
- **Stops here when:** the work is a small change (few days of effort, budget available, standard interface), which goes through the ticket and change process with no order. Nothing is sent with a silent blank, and the order is not approved or signed by the skill.
