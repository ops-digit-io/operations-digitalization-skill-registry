---
type: Skill Reference
title: Procedure
description: Formerly the skill od-analytical-support-service, absorbed into od-first-aid-kit on 2026-11-10 to remove duplication against the department context. Run the Analytical Support Service lane — take an ad-hoc analytical or process-insight request (the Process First-Aid Kit), check data availability on the data platform, run process diagnostics, build the dashboard, report, analytics workflow or app, deliver and explain the insight, track utilization, and promote recurring high-value analytics into standard use cases. Use for any ad-hoc analytics request, a rapid process diagnosis, a question about whether the data exists to answer something, or a decision on whether a one-off analysis should be industrialized. Owner is the Digital-Business-Va
resource: ../../SKILL.md
status: stable
tags:
- analytical-support-service
- lane
- absorbed
---
# Analytical Support Service

> **Absorbed.** This was the skill `od-analytical-support-service`. It now runs as a mode of [`od-first-aid-kit`](../../SKILL.md) (merged 2026-11-10, see `log.md`). Its authority stays as it was: read-only on data sources; draft on assets and summaries; recommend on promotion.

Read `od-context` first.

**Trigger.** An analytical request or an ad-hoc process-insight need.
**Definition of done.** Process diagnostics / analytical insight delivered.
**Customer.** Plant / OPEX / operations. **Scope:** regional. **Lead time:** ⟨to confirm⟩.

This lane is deliberately the fast one. Its job is an answer, not an industrialized
solution — and knowing which of the two is being asked for is step one.

## The reference

| File | Use it for |
|---|---|
| [`references/task-chain-and-tool-use.md`](references/task-chain-and-tool-use.md) | The lane's recurring tasks as a trigger chain (starts when, needs, tool, leaves behind, feeds), why each tool has its access, metric hooks, ad-hoc versus industrialize |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | How ad-hoc work is run in practice: descriptive first, plausibility before models, the statements an analysis must carry, idea-collection and potential-analysis routes, handoff contract, agent notes |
| [`references/composed-artefacts.md`](references/composed-artefacts.md) | Which composed skill's real, built asset answers each step below, and what is still genuinely open rather than just unlinked |

## Happy path

| # | Step | Who | Control point |
|---|---|---|---|
| 1 | Analytical / ad-hoc request received (Process First-Aid Kit) | Plant / OPEX + DBVE | Request scoped — see `od-requirements-breakdown` |
| 2 | Check data availability on the data platform | both | Data present and fit for use |
| 3 | Process diagnostics and analytical process insight | DBVE | Insight validated |
| 4 | Build the asset — dashboard / report / analytics / app | both | Asset produced |
| 5 | Deliver insight and asset; explain it to the requester | Human | Requester understands the result |
| 6 | Track utilization; promote recurring value into a standard use case | both | Utilization recorded |

Step 2 → `od-data-availability-check`. Step 4 → `od-analytics-asset-build`. Step 6
promotion → hand to `od-use-case-definition`.

## Error paths

- **Data not available on the data platform** → route to the Information Integration lane and mark
  it as a **data gap**. Do not approximate the missing data.
- **One-off insight with no recurring value** → close as ad-hoc; do **not** industrialize.
  Refusing to promote is a valid outcome of this lane.
- **Low utilization of a delivered asset** → review with the requester or retire it.
- **Data too sparse, sample too small, or model quality too low** → say so and stop at the descriptive
  result; do not present explainability output as a finding. Any process conclusion goes to the
  process expert as "needs expert review" first.

## Wait states

Awaiting data integration (dependency on the Information Integration lane) · awaiting
requester feedback or validation.

## Recurring tasks

| Task | Trigger | Template |
|---|---|---|
| Ad-hoc analytics / Process First-Aid | Plant or OPEX analytical request | ⟨template — to confirm⟩ |
| Data-availability check | Request scoped | `od-data-availability-check`'s `assets/data-availability-verdict.md` |
| Dashboard / report build | Insight validated | Standard dashboard/report layout |
| Utilization review | Monthly | Scorecard · Use Case Utilization |
| Promote to standard use case | Recurring high-value analytics | Hand-off to Use Case Support lane |

## Systems and access

Data platform — Databricks / Azure Storage Account (read) · Power BI / OESL Dashboards (author) · process diagnostics methods (apply) ·
ML models, labeling and training (build ⟨scope to confirm⟩) · analytics / report / app
assets (author) · Scorecard · Use Case Utilization (read / update) · Ad-Hoc Analytics and
Process First-Aid Kit (apply).

Asset mix actually delivered across the portfolio: Dashboard, Analytics, Report, App,
Agent. Dashboards are typically the most common type; count the mix live in `OD-Report-Use_Case_Integration` · Use Case Asset before quoting it.

## Autonomy

**May** — read the data platform and the Scorecard; run analytical queries; draft dashboards,
reports and insight summaries; track and report utilization; propose promoting recurring
analytics to standard use cases.
**May not** — write to production or source systems; publish an asset externally; commit
a use case to industrialization without the responsible human; present unvalidated
insight as fact.
**Guardrails** — never state a figure without a nameable source; **flag data gaps rather
than filling them**; respect data governance and access management on the data platform.

## Metrics for this lane

| Metric | Source | Target | Intervene from |
|---|---|---|---|
| Use-case utilization rate | Scorecard · Use Case Utilization | No fixed target — trend only (confirmed 2026-10-22, `od-scorecard-reporting`) | low-utilization share rising |
| Analytics asset output | `OD-Report-Use_Case_Integration` · Use Case Asset | ⟨to confirm⟩ | output below plan |
| Ad-hoc turnaround (request → insight) | ⟨tracker — to collect⟩ | ⟨to confirm⟩ | turnaround rising |
| Promotion rate (ad-hoc → standard) | ⟨tracker — to collect⟩ | ⟨to confirm⟩ | value indicator |

## Handover / rework rule

Recurring, high-value analytics go to the Use Case Support lane to become standard use
cases. Assets return for rework if the insight is not usable or utilization stays low.
