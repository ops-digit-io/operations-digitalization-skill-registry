---
type: Skill Reference
title: Outputs
description: The outputs od-first-aid-kit must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-first-aid-kit` delivers a structured first-aid request for an ad-hoc plant process issue and a routing decision with a written reason. The skill is not done until the requester has been told and no cost or connection has been promised.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| First-aid request | `assets/first-aid-request.md`, filled | Next skill in the route (travels with the request) | Complete, or lists exactly what is missing; problem restated S.M.A.R.T.; plant owner named by role |
| Data check and scenario | Section 4 of the form | `od-data-availability-check` | Signal readability and period recorded; scenario A or B classified |
| Route with reason | Section 5 of the form | `od-use-case-intake-triage` (recurring need), Analytical Support or Lane 1 self-service (one-off), `od-cybersec-gate` (new connectivity), information-integration lane (data gap) | Route chosen from the routing table with a written reason |
| Closing message to the requester | Reply to the requester | Plant requester | States what was routed where and why |

## Handoff

- **Also receives from:** `od-workshop-facilitation`: Follow-up list and summary.
- **Receives from:** `od-use-case-intake-triage` (a demand classified as ad hoc), or the plant requester directly through the ad-hoc request channel.
- **Next in the flow:** `od-use-case-intake-triage` then `od-use-case-definition` for a recurring need; `od-data-availability-check` for the data check; `od-cybersec-gate` for new connectivity; `od-decision-routing` for cost. Proposed on steps i1 and 21 of `docs/new-state/process.yaml`.
- **Stops here when:** the plant cannot name a question or an owner (back to the requester with the missing items), the need is outside the lean standardized footprint (refuse and say why), or the data is not readable (mark a data gap, never interpolate). No price indication is quoted as an offer and nothing is connected or installed.
