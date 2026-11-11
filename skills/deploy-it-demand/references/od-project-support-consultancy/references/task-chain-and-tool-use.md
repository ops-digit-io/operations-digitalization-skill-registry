---
type: Skill Reference
title: Task chain and tool use
description: The consultancy lane's recurring tasks as a trigger chain with tool access rationale and metric hooks, plus the shape of the business case used in the organisation-level initiative analysis (business case, process, technology and data, impact, strategic fit).
resource: ../procedure.md
status: draft
tags: [lane, project-support-consultancy, tasks, business-case]
---
# Task chain and tool use - Project Support and Application Consultancy

Derived from the lane's skills, tasks and metrics notes and the organisation-level project-initiatives analysis. Protocols per step
are in `composed-protocols.md`; project order, plan and status colours are in `process-chain-practice.md`. No targets, counts,
dates, or any effect-size or headcount figures from the initiatives analysis. Own synthesis is marked `PROPOSAL`; unknowns are `<...>`.

## 1. The recurring tasks as a chain

| Task | Starts when | Needs | Tool | Leaves behind | Feeds |
|---|---|---|---|---|---|
| Project kick-off with the OD team | A digital investment project is initiated | Project order, sponsor, scope | Kick-off agenda `<template to confirm>` | Roles, plan skeleton | Requirements breakdown |
| Requirements breakdown | Kick-off done | Targets, plant processes | Requirement specification `<template to confirm>` | Atomic, testable requirements | Application consultancy, acceptance criteria |
| Application consultancy session | Solution design needed | Requirements, system landscape | Manufacturing software suite (configure, scope `<to confirm>`), apps / app store (deploy) | Design decisions | Integration, rollout preparation |
| Integration project status | Weekly or at milestone | Tracker | Project tracker | Status colour, risks | Progress reporting |
| Acceptance test | The solution is ready | Requirements, protocol | Acceptance-test protocols (author) | Pass or rework | Handover |
| Progress and impact reporting | On request or on the department's own schedule | Equipment, applications, use-case figures | Department report, formerly the ODEC report (read / update) | Report with read date | Rounds |

**Chain rule.** Requirements before design; acceptance criteria written from the requirements, not after the build. Status colours
are owned by the project manager; the steering committee owns the order and the approvals.

## 2. Why each tool has the access it has

| Tool | Access | Why |
|---|---|---|
| Project method and tracker | read / update | The lane runs projects to acceptance |
| Manufacturing software suite | configure, scope `<to confirm>` | Application consultancy and rollout preparation; configuration is advisory until scope is confirmed |
| Apps / app store | deploy | Deploying approved manufacturing apps |
| Acceptance-test protocols | author | Verification is the lane's gate |
| Department reporting (formerly ODEC) | read / update | Reporting of progress and impact |
| Investment planning templates | author | Digital investment projects |

## 3. The business-case shape used for organisation-level initiatives

An organisation-level analysis structures each initiative as one business case with a fixed chain. Use it as a reading frame for
a business case this lane is asked to support (the investment inputs themselves are `bc-cost`).

| Block | Content |
|---|---|
| Business case | One sentence: the manual or reactive situation converted into a measured, live one |
| Process | The process family it sits in (plan to produce, source to pay, design to product, ...) |
| Necessary technology | Tagged with a **capability anchor**: **A** gemba management and telemetry (physical, shop floor) or **B** assistant and agentic (knowledge and transactional work), or both |
| Necessary data | The data that must exist, by name |
| Potential impact | Indicators; unit and direction stated |
| Strategic fit | Three lenses: **sizing** (does it correct an oversized overhead or reinforce an undersized capability), **USP** (does it strengthen differentiation), **sales** (does it protect or grow revenue) |

**How to use it.** Check that technology and data are named before the impact is believed; an impact with no named data is a wish.
Keep the anchor tag: it tells you whether this lane's shop-floor protocols apply (A) or whether the work belongs with the AI and
assistant skills (B).

**Caution.** The analysis is a top-down desk exercise. Its impact ranges and any staffing effects are **not** plant commitments and
are not carried in skills; a project this lane supports gets its numbers from the saving basis (`bc-build`).

## 4. Metric hooks

| Task | Metric it moves |
|---|---|
| Acceptance test | Integration projects to acceptance (not captured) |
| Integration project status | On-time delivery (not captured) |
| Progress and impact reporting | Equipment and applications progress; use-case impact |

How to read each: `metrics-scorecard/references/metric-reading-guide.md`.

## AI agent operating notes

- **May do:** pre-fill project tickets, draft the kick-off agenda and requirement breakdown, check each requirement is atomic and
  testable, compile the status table, draft the progress and impact report.
- **Evidence to cite:** tracker row, requirement id, protocol result, read date.
- **Human gate:** the steering committee approves the order and plan; the project manager owns status colour; investment is
  approved by the OD lead.
- **Hands over to:** `deploy-acceptance`, `deploy-handover`, `metrics-scorecard`.
