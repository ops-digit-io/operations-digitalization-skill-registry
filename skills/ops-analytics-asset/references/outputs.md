---
type: Skill Reference
title: Outputs
description: The outputs ops-analytics-asset must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`ops-analytics-asset` delivers the asset the plant actually opens (dashboard, report, analytics workflow, app or agent), validated and handed off with a filled protocol. The skill is not done until the asset and the protocol both exist.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Built and validated asset | The delivered dashboard, report, workflow, app or agent | Requester and plant owner | Passed the validation checklist; reconciled with the paper record for the same period; delivered and explained to the requester |
| Asset build protocol | `assets/asset-build-protocol.md`, filled | `deploy-acceptance`, `deploy-handover` | Records output asset, utilization expectation, named plant owner role and data path |
| Ritual, decision and action owner | Section of the protocol | Plant owner | All three named; if any is missing it is a "dashboard without an action owner" and is not built |
| Asset-type choice | Section of the protocol | `ops-dashboard-engine` (when the asset is a Dashboard) | Asset type chosen with a reason; ritual, tier and data model handed over rather than hand-built |

## Handoff

- **Also receives from:** `dept-governance`: Use-case sprint plan and review.
- **Also receives from:** `ops-event-model`: Archetype class, category, method, ETL list.
- **Receives from:** `mi-data-availability` (the verdict), `catalog-usecase` (the match record and template, step 1a2), the use case with its ritual, decision and action owner.
- **Next in the flow:** step 1a3 `catalog-guardrails` on Lane 1a; step 1b4 on Lane 1b; in Lane 2, step 23 `funnel-prototype`. Then `deploy-acceptance` and `deploy-handover`, which read the protocol.
- **Stops here when:** the data gap is real, the smell checks fail (no ritual, decision or action owner), validation fails, or the insight is a one-off. Close it as ad-hoc and do not industrialize. Publishing externally needs the responsible human, and an agent never marks the asset accepted before the paper reconciliation is signed.
