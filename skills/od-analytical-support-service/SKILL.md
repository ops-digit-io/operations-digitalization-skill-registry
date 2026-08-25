---
name: od-analytical-support-service
description: >-
  Run the Analytical Support Service lane — take an ad-hoc analytical or process-insight
  request (the Process First-Aid Kit), check data availability in the MDL, run process
  diagnostics, build the dashboard, report, analytics workflow or app, deliver and
  explain the insight, track utilization, and promote recurring high-value analytics into
  standard use cases. Use for any ad-hoc analytics request, a rapid process diagnosis, a
  question about whether the data exists to answer something, or a decision on whether a
  one-off analysis should be industrialized. Owner is the Digital-Business-Value-Engineer
  (DBVE).
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-analytical-support-service
  tier: lane
  lane: analytical-support-service
  owner_role: Digital-Business-Value-Engineer (DBVE) — ⟨named person to confirm⟩
  capacity: ⟨to confirm⟩
  authority_level: read-only on data sources; draft on assets and summaries; recommend on promotion
  escalation: Information Integration lane for data gaps; OD lead (Thomas Zipf) via COP otherwise
  status: stable
  last_verified: 2026-08-10
  requires: [od-context]
  composes: [od-data-availability-check, od-analytics-asset-build, od-portfolio-and-savings-analysis, od-scorecard-reporting]
  derived_from:
    - ops-knowledge-graph/.../20-lanes/analytical-support-service/{playbook,skills,tasks,metrics,agent-brief}.md
---

# Analytical Support Service

Read `od-context` first.

**Trigger.** An analytical request or an ad-hoc process-insight need.
**Definition of done.** Process diagnostics / analytical insight delivered.
**Customer.** Plant / OPEX / operations. **Scope:** regional. **Lead time:** ⟨to confirm⟩.

This lane is deliberately the fast one. Its job is an answer, not an industrialized
solution — and knowing which of the two is being asked for is step one.

## Happy path

| # | Step | Who | Control point |
|---|---|---|---|
| 1 | Analytical / ad-hoc request received (Process First-Aid Kit) | Plant / OPEX + DBVE | Request scoped |
| 2 | Check data availability in the MDL | both | Data present and fit for use |
| 3 | Process diagnostics and analytical process insight | DBVE | Insight validated |
| 4 | Build the asset — dashboard / report / analytics / app | both | Asset produced |
| 5 | Deliver insight and asset; explain it to the requester | Human | Requester understands the result |
| 6 | Track utilization; promote recurring value into a standard use case | both | Utilization recorded |

Step 2 → `od-data-availability-check`. Step 4 → `od-analytics-asset-build`. Step 6
promotion → hand to `od-use-case-support-service`.

## Error paths

- **Data not available in the MDL** → route to the Information Integration lane and mark
  it as a **data gap**. Do not approximate the missing data.
- **One-off insight with no recurring value** → close as ad-hoc; do **not** industrialize.
  Refusing to promote is a valid outcome of this lane.
- **Low utilization of a delivered asset** → review with the requester or retire it.

## Wait states

Awaiting data integration (dependency on the Information Integration lane) · awaiting
requester feedback or validation.

## Recurring tasks

| Task | Trigger | Template |
|---|---|---|
| Ad-hoc analytics / Process First-Aid | Plant or OPEX analytical request | ⟨template — to confirm⟩ |
| Data-availability check | Request scoped | MDL data-check ⟨template — to confirm⟩ |
| Dashboard / report build | Insight validated | Standard dashboard/report layout |
| Utilization review | Monthly | Scorecard · Use Case Utilization |
| Promote to standard use case | Recurring high-value analytics | Hand-off to Use Case Support lane |

## Systems and access

MDL (read) · Power BI / OESL Dashboards (author) · process diagnostics methods (apply) ·
ML models, labeling and training (build ⟨scope to confirm⟩) · analytics / report / app
assets (author) · Scorecard · Use Case Utilization (read / update) · Ad-Hoc Analytics and
Process First-Aid Kit (apply).

Asset mix actually delivered across the portfolio: Dashboard, Analytics, Report, App,
Agent — and dashboards dominate (173 of the 202 use cases that record an output asset).

## Autonomy

**May** — read the MDL and the Scorecard; run analytical queries; draft dashboards,
reports and insight summaries; track and report utilization; propose promoting recurring
analytics to standard use cases.
**May not** — write to production or source systems; publish an asset externally; commit
a use case to industrialization without the responsible human; present unvalidated
insight as fact.
**Guardrails** — never state a figure without a nameable source; **flag data gaps rather
than filling them**; respect data governance and access management on the MDL.

## Metrics for this lane

| Metric | Source | Target | Intervene from |
|---|---|---|---|
| Use-case utilization rate | Scorecard · Use Case Utilization | ⟨to confirm⟩ | low-utilization share rising |
| Analytics asset output | `OD-Report-Use_Case_Integration` · Use Case Asset | ⟨to confirm⟩ | output below plan |
| Ad-hoc turnaround (request → insight) | ⟨tracker — to collect⟩ | ⟨to confirm⟩ | turnaround rising |
| Promotion rate (ad-hoc → standard) | ⟨tracker — to collect⟩ | ⟨to confirm⟩ | value indicator |

## Handover / rework rule

Recurring, high-value analytics go to the Use Case Support lane to become standard use
cases. Assets return for rework if the insight is not usable or utilization stays low.
