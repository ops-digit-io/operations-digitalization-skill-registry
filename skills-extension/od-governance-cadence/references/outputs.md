---
type: Skill Reference
title: Outputs
description: The outputs od-governance-cadence must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-governance-cadence` delivers the packs and records of the governance routines around the process chain: the round pack with its call for action, and the sprint plan with its review. It holds method only; dates, counts and plant statuses are read live. The skill is not done until the human gate has approved the pack.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Round pack | `assets/call-for-action-and-status.md`: agenda, plant status table, numbered call for action | OD lead (approves and sends) | Every status cell cites its source list and read date; one traffic light per round; OD lead has approved escalation wording and deadline |
| Follow-up log | Section 4 of the round pack | Owners named in `od-decision-routing`; `od-retro` (CoP feedback) | Q&A classified and routed to the owning service line; open homework chased; unresolved items carried with the label "carried" |
| Use-case sprint plan and review | `assets/sprint-plan-and-review.md`: preconditions, deliverable board, IT-issue log, sprint-end review | `od-use-case-definition`, `od-analytics-asset-build` | Expert for the process, baseline and agreed architecture and access are recorded before the start; a requirement beyond the timeframe is logged as an additional phase |
| Routed demand | The request sorted as small change, project or governance board | `od-decision-routing`, `it-demand-package` | Sorted with `od-use-case-intake-triage` first, then by the routing reference; owner named |

## Handoff

- **Receives from:** `od-scorecard-reporting` (live figures), `od-risk-watch` (risk readings), `od-decision-routing` (rights and escalation), `od-use-case-definition` (the use case entering a sprint).
- **Next in the flow:** the OD lead for packs; the owner named in `od-decision-routing` for routed requests; `od-retro` for round feedback; `od-risk-watch` for indicator gaps; `od-rollout-training` for the training programme. Proposed on step 23 of `docs/new-state/process.yaml`.
- **Stops here when:** a sprint lacks an expert for the process, a defined baseline or agreed architecture and access; the machine is not connected (a wave first); or an escalation, route, budget or priority would be decided by the agent. Recorded demand is not proven saving; ODEC is not a current forum.
