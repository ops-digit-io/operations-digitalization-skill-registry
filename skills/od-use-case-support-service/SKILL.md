---
name: od-use-case-support-service
description: >-
  Run the Smart Factory Use Case Support Service lane end to end — collect plant
  use-case demand, define the use case with the plant, break down the requirement,
  build the OD benefit case, prioritize by value, hand to integration, then evaluate
  impact and adoption. Includes the Process First-Aid Kit. Use when a plant asks for a
  use case, a definition or integration workshop is requested, a use case needs
  prioritizing or a business case, or someone asks what happens to a use case between
  demand and daily use. Owner is the Digital-Business-Value-Engineer (DBVE).
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-use-case-support-service
  tier: lane
  lane: use-case-support-service
  owner_role: Digital-Business-Value-Engineer (DBVE)
  capacity: 2 DBVE roles
  authority_level: draft on definitions and reports; recommend on prioritization
  escalation: OD lead (Thomas Zipf) within the ODEC/COP window
  status: stable
  sources_read: 2026-08-10
  requires: [od-context]
  composes: [od-use-case-intake-triage, od-use-case-definition, od-benefit-calculation, od-use-case-standardization, od-handover-and-adoption, od-scorecard-reporting]
  derived_from:
    - ops-knowledge-graph/.../20-lanes/use-case-support-service/{playbook,skills,tasks,metrics,agent-brief}.md
    - ops-knowledge-graph/_knowledge/10-Department/Use case lifecycle.md
  okf:
    type: Agent Skill
    title: Smart Factory Use Case Support Service
    tags: [lane, use-case-support-service]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Smart Factory Use Case Support Service

Read `od-context` first.

**Trigger.** Plant use-case demand, or a request for a definition or integration
workshop.
**Definition of done.** Use case defined, prioritized, impact-evaluated and handed to
integration **with a business case**.
**Customer.** Plant ME / plant operations. **Lead time:** ⟨to confirm⟩.

## Happy path

| # | Step | Who | Control point |
|---|---|---|---|
| 1 | Collect plant use-case demand (workshop or request) | DBVE + Plant ME | Demand logged against the plant roadmap |
| 2 | Plant- and process-specific use-case definition; process diagnostics and analytical insight | both | Use case scoped with a clear objective |
| 3 | Break down the customer/process requirement; assess (legacy) MF IT systems | DBVE | System assessment complete — see `od-requirements-breakdown` |
| 4 | Plan the OD benefit calculation and business case; prioritize by value (savings / lead-time / cost avoidance) | both | Business case and priority agreed with Plant ME |
| 5 | Hand to Information Integration Service for equipment/solution integration | DBVE | Integration request accepted |
| 6 | System qualification and training; use-case execution support | DBVE | Use case running on the shopfloor |
| 7 | Evaluate impact; ensure adoption into the daily process | both | Impact evaluated; recipient confirms adoption |

Step 1 → `od-use-case-intake-triage`. Step 2 → `od-use-case-definition`. Step 4 →
`od-benefit-calculation`. Step 7 → `od-handover-and-adoption`. Before step 5, run
`od-use-case-standardization`: a use case that matches an existing library entry should
take it rather than be re-specified.

## Error paths

- **Required system not deployed / operations concept missing** → route to strategy as a
  tool-rollout decision; mark the use case blocked in the portfolio.
- **No nameable business case** → refuse per intake and return to the demand owner.
- **Integration fails acceptance** → rework loop back to step 5.

## Wait states

Awaiting investment approval (OD lead / BA Operations) · awaiting Cyber Security sign-off
for an external machine connection · awaiting a decision on shared tooling or licensing
⟨owner to confirm⟩.

## Recurring tasks

| Task | Trigger | Template |
|---|---|---|
| Use Case Definition Workshop | Plant onboarding / new demand wave | Standard Agenda — Use Case Workshop (SharePoint) |
| Use Case Integration Workshop | Use case ready for integration | Use Case Integration Workshop agenda |
| Benefit / savings calculation | Use case prioritized | OD Benefit Calculation template |
| Digitalization Scorecard update | Monthly / ODEC | Digitalization Scorecard (Power BI) |
| Use-case impact evaluation | Use case live | ⟨template — to confirm⟩ |
| Process First-Aid Kit request | Ad-hoc plant process issue | ⟨template — to confirm⟩ |

## Systems and access

Data platform — Databricks / Azure Storage Account, Parquet (read; written by the edge
offload) · IIoT Edge (read / deploy) · MSB (read / write ⟨scope to
confirm⟩) · OESL Dashboards & Power BI (read / author) · use-case library and SharePoint
(read / write) · process diagnostics and analytics tooling (read) · benefit-calculation
method (author) · data pipelines (write, **with IIAE**).

## Autonomy

**May** — read the data platform, the Scorecard and the use-case library; draft use-case definitions,
benefit calculations and prioritization proposals; assemble impact reports; prepare
workshop materials.
**May not** — commit investment; approve equipment integration or an external machine
connection; change data models or system rollouts; publish externally.
**Guardrails** — never invent savings or impact figures, mark them to-be-collected; respect
Cyber Security sign-off before any connection action.

## Metrics for this lane

| Metric | Source | Target | Intervene from |
|---|---|---|---|
| Integrated use cases (year) | `OD-Report-Use_Case_Integration` · Actual vs. Target | 153 (year) | IS below target-to-date — 101 vs 153 on 2026-08-10 |
| Integrated use cases per month | same · monthly bar | 12 / month (overshoot 14) | month below 12 |
| Use-case utilization rate | Scorecard · Use Case Utilization | ⟨to confirm⟩ | low-utilization share rising |
| Asset mix (Dashboard/Analytics/Report/App/Agent) | Use_Case_Integration · asset pie | ⟨to confirm⟩ | portfolio indicator |
| Value delivery cycle (demand → live) | ⟨system — to confirm⟩ | ⟨to confirm⟩ | ⟨threshold — to confirm⟩ |

## Handover / rework rule

The use case goes to Information Integration Service **with** its business case and
requirement breakdown. It returns for rework if integration fails acceptance testing, or
if the use case is not adopted into the daily process.
