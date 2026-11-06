---
type: Skill Reference
title: Task chain and tool use
description: The lane's recurring tasks as a trigger chain (what starts each, what it needs, which tool, what it leaves, which task and metric it feeds), and why each tool has the access it has. Basis for pre-filling and ticket creation.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [lane, use-case-support-service, tasks]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Task chain and tool use - Use Case Support Service

Derived from the lane's skills, tasks and metrics notes and the operating-context note. The lane notes exist so a machine can
pre-fill and open tickets automatically; this file turns the task list into a chain. Template routing is in
`lane-templates.md`; the flow blocks and chain steps are in `process-chain-practice.md`. No targets, counts or dates. Own synthesis
is marked `PROPOSAL`; unknowns are `<...>`.

## 1. The recurring tasks as a chain

| Task | Starts when | Needs | Tool | Leaves behind | Feeds |
|---|---|---|---|---|---|
| Use Case Definition Workshop | Plant onboarding, or a new demand wave | Plant file, ritual candidates, library match | Use-case library (SharePoint), standard agenda | Defined use cases with problem, user, ritual | Prioritization, benefit calculation |
| Benefit / savings calculation | A use case is prioritized | Baseline, expected change, basis | Benefit-calculation method | Saving basis row | Business case, tracked savings |
| Use Case Integration Workshop | A use case is ready for integration | Business case, requirement breakdown, data availability verdict | Integration workshop agenda; data platform (read) | Integration plan, roles, utilization table started | Hand-off to Information Integration |
| Use-case impact evaluation | The use case is live | Utilization evidence, saving basis | Scorecard utilization view; `od-handover-and-adoption` test | Impact statement, adoption record | Utilization metric, retro |
| Scorecard update | On request or on the department's own schedule | Current lists and reports | Scorecard (Power BI) | Updated figures with read date | Reporting on request |
| Process First-Aid Kit request | Ad-hoc plant process issue | Plant question, data status | `<template to confirm>` | Quick answer or a routed definition | Analytical lane, or definition |

**Chain rule.** Each task's output is the next task's required input. A task started without its input produces a placeholder;
route back instead (`od-barrier-triage`).

`PROPOSAL`: when an agent opens a ticket for one of these tasks, it pre-fills **Starts when**, **Needs** (with the source of each
item and its read date) and **Leaves behind** as the definition of done, and names the next task as the follow-up.

## 2. Why each tool has the access it has

| Tool | Access | Why that access |
|---|---|---|
| Data platform (Databricks to Azure Storage Account, Parquet) | read | Written by the edge offload; this lane consumes, never writes source data |
| IIoT Edge Platform | read / deploy | Data acquisition and app deployment are owned by the integration lane for the machine side; this lane only deploys what is approved |
| Manufacturing Service Bus | read / write, scope `<to confirm>` | Enabler of use-case data exchange; write scope is unconfirmed, so assume read until confirmed |
| Dashboards and Power BI | read / author | Impact visualization and the Scorecard; authoring is allowed, publishing externally is human-approved |
| Use-case library and SharePoint | read / write | The write surface for definitions, agendas and templates |
| Process diagnostics and analytics tooling | read | Insight support; changing a model is the analytical lane's job |
| Benefit-calculation method | author | The lane owns benefit calculations |
| Data pipelines | write, with the integration engineer | Standardization of signals is a joint task; never alone |

## 3. Operating-context seams this lane crosses

| Partner kind | Seam | Mode | Effect on the chain |
|---|---|---|---|
| OPEX / continuous-improvement | Digital use cases support OPEX methods | Tandem | Definition and impact evaluation are done together |
| Plant ME and teams | Demand, rollout, adoption | Consultation | The plant owner confirms ritual, adoption |
| Cyber Security / OT | Connection sign-off, bundling | Consultation | A gate before integration |
| IT / ERP | The MES dependency | Information | Tell, do not wait |
| Manufacturing Engineering (automation) | Insight-based control ideas | Consultation | Optional input at definition |

## 4. Metric hooks

| Task | Metric it moves | How |
|---|---|---|
| Integration workshop | Integrated use cases | Counted when integration is recorded |
| Impact evaluation | Utilization rate | Utilization is read from the use-case record |
| Definition and benefit calculation | Value delivery cycle (not captured) | Start of the cycle if it is ever defined |

How to read each metric: `od-scorecard-reporting/references/metric-reading-guide.md`.

## AI agent operating notes

- **May do:** open and pre-fill the task tickets above, check the "Needs" column against the record, draft agendas and the impact
  statement, list use cases whose next task has no owner.
- **Evidence to cite:** list names with read date; template name.
- **Human gate:** commitments (investment, connection approval) stay with the OD lead and Cyber Security.
- **Hands over to:** `od-information-integration-service` with the business case and requirement breakdown.
