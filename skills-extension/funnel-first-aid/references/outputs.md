---
type: Skill Reference
title: Outputs
description: The outputs funnel-first-aid must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`funnel-first-aid` delivers a structured first-aid request for an ad-hoc plant process issue and a routing decision with a written reason. The skill is not done until the requester has been told and no cost or connection has been promised.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| First-aid request | `assets/first-aid-request.md`, filled | Next skill in the route (travels with the request) | Complete, or lists exactly what is missing; problem restated S.M.A.R.T.; plant owner named by role |
| Data check and scenario | Section 4 of the form | `mi-data-availability` | Signal readability and period recorded; scenario A or B classified |
| Route with reason | Section 5 of the form | `dept-intake` (recurring need), Analytical Support or Lane 1 self-service (one-off), `deploy-cybersec` (new connectivity), information-integration lane (data gap) | Route chosen from the routing table with a written reason |
| Closing message to the requester | Reply to the requester | Plant requester | States what was routed where and why |

## Handoff

- **Also receives from:** `funnel-workshop`: Follow-up list and summary.
- **Receives from:** `dept-intake` (a demand classified as ad hoc), or the plant requester directly through the ad-hoc request channel.
- **Next in the flow:** `dept-intake` then `funnel-use-case` for a recurring need; `mi-data-availability` for the data check; `deploy-cybersec` for new connectivity; `dept-decision-rights` for cost. Proposed on steps i1 and 21 of `docs/new-state/process.yaml`.
- **Stops here when:** the plant cannot name a question or an owner (back to the requester with the missing items), the need is outside the lean standardized footprint (refuse and say why), or the data is not readable (mark a data gap, never interpolate). No price indication is quoted as an offer and nothing is connected or installed.
