---
type: Skill Reference
title: Task chain and tool use
description: The analytical lane's recurring tasks as a trigger chain (what starts each, what it needs, which tool, what it leaves, which task and metric it feeds), why each tool has the access it has, and when ad-hoc work is promoted.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [lane, analytical-support-service, tasks]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Task chain and tool use - Analytical Support Service

Derived from the lane's skills, tasks and metrics notes. Artefacts per step are in `composed-artefacts.md`; the method for ad-hoc
work is in `process-chain-practice.md`. No targets, counts or dates. Own synthesis is marked `PROPOSAL`; unknowns are `<...>`.

## 1. The recurring tasks as a chain

| Task | Starts when | Needs | Tool | Leaves behind | Feeds |
|---|---|---|---|---|---|
| Ad-hoc analytics / Process First-Aid | A plant or OPEX analytical request | The question, the process, the time window | Process diagnostics methods, data platform (read) | An answer with its assumptions, or a routed definition | Data-availability check, or promotion |
| Data-availability check | The request is scoped | Signal list, machine, period | Data platform check (verdict asset of `od-data-availability-check`) | A verdict: available, partly, not | Dashboard or report build; or a gap routed to integration |
| Dashboard / report build | The insight is validated | Verdict, ritual, action owner | Power BI / dashboards (author), standard layout | The asset and its protocol | Utilization review |
| Utilization review | Monthly | The Scorecard utilization view | Scorecard (read / update) | Rework or retire decision | Retro, promotion |
| Promote to standard use case | A recurring high-value analysis | Evidence of recurrence and value | Hand-off to the Use Case Support lane | A defined use case | Use Case Support lane |

**Chain rule.** Nothing is built before the availability verdict; nothing is promoted without recurrence evidence. A request that
arrives as "build me a dashboard" is returned to the question: what decision, which ritual, who acts?

## 2. Why each tool has the access it has

| Tool | Access | Why |
|---|---|---|
| Data platform | read | Global layer; analytics read, they do not write source data |
| Power BI / dashboards | author | This is the lane's delivery surface; external publishing is human-approved |
| Process diagnostics methods | apply | Analytical insight into process behaviour |
| Machine-learning models (labelling, training) | build, scope `<to confirm>` | Scope of model building unconfirmed; treat as proposal-only until confirmed |
| Analytics / report / app assets | author | Deliverable formats (dashboard, analytics, report, app, agent) |
| Scorecard utilization view | read / update | Track utilization of delivered assets |
| Ad-hoc analytics / First-Aid Kit | apply | Rapid response format; no template yet (`<to confirm>`) |

## 3. Ad-hoc versus industrialize

| Signal | Reading | Action |
|---|---|---|
| One-off question, no recurring value | Ad-hoc | Deliver the answer, close it, do not industrialize |
| Same question from several plants or periods | Recurring | Start the promotion check |
| Needs data that is not collected | Data gap | Route to integration; do not build on a proxy |
| An asset for this capability exists elsewhere | Adopt | Use the library entry |

`PROPOSAL`: record each ad-hoc request with request date, delivery date, whether data had to be waited for, and whether it recurred.
That single log makes the two "not captured" lane metrics (turnaround, promotion rate) computable; see
`od-scorecard-reporting/references/metric-reading-guide.md`.

## 4. Metric hooks

| Task | Metric it moves |
|---|---|
| Utilization review | Utilization rate (trend only) |
| Dashboard / report build | Analytics asset output |
| Ad-hoc analytics | Ad-hoc turnaround (not captured) |
| Promote to standard use case | Promotion rate (value indicator) |

## AI agent operating notes

- **May do:** pre-fill the availability check from a signal list, draft the layout and the protocol, compute the log fields above,
  flag recurring requests, draft the promotion proposal.
- **Evidence to cite:** data source, period, read date, verdict.
- **Human gate:** committing a use case to industrialization, publishing externally, presenting unvalidated insight as fact are
  human decisions.
- **Hands over to:** `od-use-case-definition` (promotion), `od-information-integration-service` (data gap).
