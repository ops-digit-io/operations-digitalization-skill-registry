---
type: Skill Reference
title: Outputs
description: The outputs ops-dashboard-engine must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`ops-dashboard-engine` delivers an importable Grafana dashboard JSON backed by SQL, plus the audit that shows it is safe to import. The skill is not done until the file passes the Step 6 audit checklist and its recipient can import it without asking.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Dashboard JSON | One Grafana `.json` file generated with `references/dashboard_builder.py` (Step 5) | `deploy-handover`, plant key user | The JSON validates; the datasource UID is a `${DS_NAME}` placeholder; schema, plugin and Grafana versions are declared in `__requires` |
| Panel SQL | Queries inside the JSON | `ops-analytics-asset` (frame of the build) | Every query uses the Grafana time macros, is PostgreSQL and DuckDB compatible, and every defined variable is used in each relevant panel |
| Audit record | The Step 6 checklist, run before delivery | Plant key user who imports the file | Every checklist item is ticked or the exception is stated; portability passed on at least 5 representative panels on both PostgreSQL and DuckDB |
| Handover facts | Fields on the use-case record (per `OD-INTEGRATION.md`) | `deploy-handover` | Output asset, business process, utilization expectation and named plant owner are recorded |

## Handoff

- **Receives from:** `ops-analytics-asset` (the ritual the dashboard is read in, and the catalog template in Lane 1a with the `catalog-usecase` guardrails), `mi-data-availability` (the signal path machine to local datasource is walked before a panel is promised). The schema (Step 0) or signal list comes from the requester.
- **Next in the flow:** `deploy-handover`, then the plant owner. Proposed on step 1a2 (Apply template) of `docs/new-state/process.yaml`. Publishing to a shared Grafana instance is a human-approved action.
- **Stops here when:** the schema or archetype is not confirmed, a signal is not standardized or not available, the panel needs several plants at once (not a local dashboard), or a query fails the portability check. Do not show a tracked saving as proven and do not turn an absence into a zero.
