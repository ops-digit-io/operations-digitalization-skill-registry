---
type: Skill Reference
title: Outputs
description: The outputs ops-dashboard-datatron must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`ops-dashboard-datatron` delivers a Grafana dashboard on the DATATRON telemetry schema, built from a catalogued template, plus the list of datapoint UUIDs that had to be enabled first. The QA checklist is the go-live gate.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Datapoint UUID list | List produced before the build starts | Plant (switches the signals on, via datapoint-enablement intake) | Every disabled signal the dashboard needs is listed by UUID before the build; no build rests on a disabled signal |
| Dashboard | Grafana dashboard built from the catalog entry's template through `ops-dashboard-engine` | Plant key user (self-service); `catalog-usecase` | Built on selected DATATRON tags with the proven query and variable patterns and scaled-PLC handling; nothing outside the template added locally |
| QA checklist result | Checklist pass recorded against the dashboard | Plant key user; `catalog-guardrails` | The QA checklist is passed; this is the objective go-live gate |
| Published example | Approved dashboard published to the use-case library | `catalog-usecase`; DBVE | Published as a reusable example only after the QA pass; publishing to a shared Grafana is human-approved |

## Handoff

- **Receives from:** `catalog-usecase` (the catalogued dashboard and its template), `catalog-guardrails` (the QA gate), `ops-dashboard-engine` (the generic Grafana JSON engine).
- **Next in the flow:** Lane 1 step 1a2 (apply template) and 1b4 (apply template and go live), and Lane 2 step 26 (implement and graduate); on 1b4 the dashboard is accompanied by `know-training`. A need the template does not cover goes to Lane 2 as a deviation.
- **Stops here when:** a required signal is disabled (list its UUID and stop), the QA checklist has not passed, or the need extends the catalogued template (route it to Lane 2, do not extend locally). Do not publish without the QA pass.
