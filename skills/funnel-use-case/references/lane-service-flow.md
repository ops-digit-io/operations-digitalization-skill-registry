---
type: Skill Reference
title: Lane service flow
description: Detail of the Smart Factory Use Case Support Service lane around step 21 - error paths, wait states, recurring tasks, systems and access, autonomy and the lane metrics. SKILL.md keeps only the compact flow table.
resource: ../SKILL.md
status: stable
tags: [lane, use-case-support-service]
---
# Lane service flow - detail

Compact flow table, trigger and definition of done: `../SKILL.md`. Lane 2 steps 21 to 26 plus the
use-case half of Lane 1.

## Handover / rework rule

A use case that needs a new system or a new machine connection goes to Lane 3 (3a or 3b)
**with** its business case and requirement breakdown. It returns for rework if integration fails
acceptance testing, or if the use case is not adopted into the daily process.

## Error paths

- **Required system not deployed / operations concept missing** -> route to strategy as a
  tool-rollout decision; mark the use case blocked in the portfolio.
- **No nameable business case** -> refuse per intake and return to the demand owner.
- **Savings with no registered plant savings project or no baseline** -> the saving is a claim,
  not a result; register the project and fix the baseline before the next sprint review.
- **Machine not connected** -> no use case yet; open an integration request and record the dependency.
- **Integration fails acceptance** -> rework loop back to the Lane 3 hand-off ("Chaining out of Lane 2" in `../SKILL.md`).

## Wait states

Awaiting investment approval (OD lead / BA Operations) · awaiting Cyber Security sign-off
for an external machine connection · awaiting a decision on shared tooling or licensing,
Plant ME / Plant IT (resolved 2026-10-22, same counterpart as data-model/signal
standardization; see `dept-decision-rights`).

## Recurring tasks

| Task | Trigger | Template |
|---|---|---|
| Use Case Definition Workshop | Plant onboarding / new demand wave | See "Workshops" in SKILL.md |
| Use Case Integration Workshop | Use case ready for integration | See "Workshops" in SKILL.md |
| Benefit / savings calculation | Use case prioritized | OD Benefit Calculation template |
| Digitalization Scorecard update | On request or on the department's own schedule | Digitalization Scorecard (Power BI) |
| Use-case impact evaluation | Use case live | `deploy-handover`'s three-question test + `assets/handover-protocol.md` (resolved, see `lane-templates.md`) |
| Process First-Aid Kit request | Ad-hoc plant process issue | ⟨template to confirm; no dedicated template found anywhere in the registry⟩ |

## Systems and access

Data platform (Databricks / Azure Storage Account, Parquet): read, written by the edge
offload · IIoT Edge: read / deploy · MSB: read / write ⟨scope to confirm⟩ · OESL
Dashboards & Power BI: read / author · use-case library and SharePoint: read / write ·
process diagnostics and analytics tooling: read · benefit-calculation method: author ·
data pipelines: write, **with IIAE**. Reasons per tool: `task-chain-and-tool-use.md`.

## Autonomy

**May** read the data platform, the Scorecard and the use-case library; draft use-case
definitions, benefit calculations and prioritization proposals; assemble impact reports;
prepare workshop materials.
**May not** commit investment; approve equipment integration or an external machine
connection; change data models or system rollouts; publish externally.
**Guardrails**: never invent savings or impact figures, mark them to-be-collected; respect
Cyber Security sign-off before any connection action. Escalation: OD lead.

## Metrics for this lane

| Metric | Source | Target | Intervene from |
|---|---|---|---|
| Integrated use cases (year) | `OD-Report-Use_Case_Integration` · Actual vs. Target | Annual target as set in the Scorecard (look up there) | Actual below target-to-date |
| Integrated use cases per month | same · monthly bar | Monthly run-rate implied by the annual target | Month below the run-rate |
| Use-case utilization rate | Scorecard · Use Case Utilization | No fixed target, trend only (resolved 2026-10-22, see `metrics-scorecard`) | low-utilization share rising |
| Asset mix (Dashboard/Analytics/Report/App/Agent) | Use_Case_Integration · asset pie | No target, descriptive portfolio indicator | portfolio indicator |
| Value delivery cycle (demand -> live) | Not captured in any system today | No target, nothing to measure against yet | none |

## Coordinate, states and portfolio stages (detail)

- A capability is typically instantiated at nearly every plant; **instantiated is not delivered**
  (many capability-epic records group no use case; count live, see `patterns.md`).
- Three workflow states (development, implementation, handover) are tracked independently;
  handover consistently trails by about thirty use cases portfolio-wide: normal shape.
- Rollout phases `PHASE 1`..`PHASE 5` are named batches tied to a plant project, not queues.
- Portfolio stage-gate model (`00-core/12-portfolio.md`): `Captured -> Evaluated -> Assessed ->
  Planned/Implementation -> Handed over -> Effective`. Collect gives *Captured*, Analyse *Evaluated*,
  Assess the literal *Assessed*, Control moves a use case into *Planned*. A use case stuck at a
  stage has stalled in the matching phase: look there first.
