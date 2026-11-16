---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Outputs and hand-off: the text before outputs.yaml

`funnel-first-aid` delivers a structured first-aid request for an ad-hoc plant process issue and a routing decision with a written reason. The skill is not done until the requester has been told and no cost or connection has been promised.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| First-aid request | `assets/first-aid-request.md`, filled | Next skill in the route (travels with the request) | Complete, or lists exactly what is missing; problem restated S.M.A.R.T.; plant owner named by role |
| Data check and scenario | Section 4 of the form | `mi-data-availability` | Signal readability and period recorded; scenario A or B classified |
| Route with reason | Section 5 of the form | `dept-intake` (recurring need), One-off analysis (Lane 1 self-service), `deploy-cybersec` (new connectivity), information-integration lane (data gap) | Route chosen from the routing table with a written reason |
| Closing message to the requester | Reply to the requester | Plant requester | States what was routed where and why |

## Handoff

- **Also receives from:** `funnel-workshop`: Follow-up list and summary.
- **Receives from:** `dept-intake` (a demand classified as ad hoc), or the plant requester directly through the ad-hoc request channel.
- **Next in the flow:** `dept-intake` then `funnel-use-case` for a recurring need; `mi-data-availability` for the data check; `deploy-cybersec` for new connectivity; `dept-decision-rights` for cost. Proposed on steps i1 and 21 of `docs/new-state/process.yaml`.
- **Stops here when:** the plant cannot name a question or an owner (back to the requester with the missing items), the need is outside the lean standardized footprint (refuse and say why), or the data is not readable (mark a data gap, never interpolate). No price indication is quoted as an offer and nothing is connected or installed.

## Provenance moved out of SKILL.md

The service catalogue lists the Smart Factory Use Case Support Service "(incl. Process First-Aid Kit)"; the glossary calls it a "rapid diagnostic offering within Use Case Support Service", next to Ad-Hoc Analytics in the Analytical Support Service. The lane's recurring tasks list "Process First-Aid Kit request - ad-hoc plant process issue" with the template marked "to confirm", and two registry pages record that no dedicated template exists. The Analytical Support Service lane is retired in the new state; its procedure is kept as an absorbed mode (route name in the skill: one-off analysis).

## What is still open (open questions)

- Official first-aid template: not in any source. Supplier: DBVE.
- Central queue or mailbox for requests: "to confirm" in the intake document.
- Lead time and capacity for first-aid requests: all lane lead times are "to confirm". Supplier: OD lead.
- Who pays for devices and templates: which budget is not stated. Supplier: OD lead.
- Turnaround and promotion-rate trackers: named as missing.
- Closing rule: when a first-aid case counts as done (insight delivered, or insight understood).
- Whether the roadmap-link and business-case refusal rule of the intake document also applies to a first-aid request. Supplier: OD lead.
- The expansion of the acronym S.M.A.R.T. is not written out in the decks; the five-point test in the procedure is the deck wording.
- The sign-off of the first-aid request names the next skill, not a human role; who signs it is undecided.
