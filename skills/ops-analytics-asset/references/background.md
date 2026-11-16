---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## The references are the substance

**This skill does not re-derive Grafana build mechanics.** `ops-dashboard-engine` already
owns the SQL patterns, the manager/analyst/operations tiers, the variable wiring and the
ECharts templates in depth — this skill is the layer above it: which asset type, for which
ritual, validated against what, handed off to whom. Once the asset type is "Dashboard," go
straight to that skill's Step 0.

## Example

Fictional example (all values invented for illustration):

If it fails: when validation fails or the smell checks in step 3 fail, do not call the asset built; fix it or close it as "dashboard without an action owner". Rendering is not the same as correct.

## Outputs and hand-off: the text before outputs.yaml

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
