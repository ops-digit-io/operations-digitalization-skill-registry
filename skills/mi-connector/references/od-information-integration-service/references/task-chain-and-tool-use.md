---
type: Skill Reference
title: Task chain and tool use
description: The integration lane's recurring tasks as a trigger chain with tool access rationale, the signal-standardization rule, the readiness matrix and source-catalogue traps, and metric hooks.
resource: ../procedure.md
status: draft
owner: human:jakob.gabriel
tags: [lane, information-integration-service, tasks]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Task chain and tool use - Information Integration Service

Derived from the lane's skills, tasks and metrics notes and the ODEC fact triage. Handoffs per step are in `lane-handoffs.md`; the
lane rhythm is in `process-chain-practice.md`. No targets, counts, dates or per-plant status. Own synthesis is marked `PROPOSAL`;
unknowns are `<...>`.

## 1. The recurring tasks as a chain

| Task | Starts when | Needs | Tool | Leaves behind | Feeds |
|---|---|---|---|---|---|
| Equipment assessment and roadmap | A new plant or integration wave | Machine inventory, use cases, network picture | Assessment protocol (`mi-connector`) | Roadmap with priorities | Investment planning |
| Integration investment planning | The roadmap is agreed | Roadmap, cost basis | Investment plan `<template to confirm>` | Investment request | Execution |
| Machine integration execution | The investment is approved, Cyber Security cleared | Plan, connection design | Integration guidance protocol; IIoT edge platform (deploy / configure); connectors | A connected machine | Signal standardization |
| Signal standardization | A machine is connected | Signal list, machine standard | Signal standard spec; data pipelines (write) | Standardized signals consumable by every plant's instance of the capability | Acceptance test |
| Acceptance test | Integration complete | Requirements, protocol | Acceptance-test protocol | Pass or rework | Readiness matrix, report update |
| Equipment Integration report update | On request or on the department's own schedule | Machine list | Equipment Integration report (read / update) | Updated report with read date | Rounds |
| Readiness matrix update | A capability changes | Acceptance evidence | Scorecard readiness matrix (read / update) | Colour with evidence | Strategic-plant readiness |

**Chain rule.** A readiness cell turns to "available" only with an acceptance pass on record; an update without evidence is a
status claim, not a status (`od-scorecard-reporting/references/readiness-evidence.md`).

## 2. Why each tool has the access it has

| Tool | Access | Why |
|---|---|---|
| IIoT Edge Platform | deploy / configure | Data acquisition from equipment is this lane's core job |
| Data pipelines | write | Standardization of signals for the offload |
| Data platform (Databricks to Azure Storage Account, Parquet) | write via the offload only | Global layer; no direct writes |
| Manufacturing Service Bus | configure, scope `<to confirm>` | Machine and app data exchange; confirm scope before changing |
| Machine connectors and signal standards | configure | The reach into machines |
| Equipment Integration report | read / update | Tracking against target |
| Scorecard readiness matrix | read / update | System and capability readiness |
| Cyber Security / OT interface | consult | Connection sign-off is a gate, not a courtesy |

## 3. Signal standardization rule

Signals are aligned with machine and equipment standards and **must stay consumable by every plant's instance of the same
capability**. A signal that works in one plant's dashboard and not in another's has been standardized locally, not standardized.
Check by reading it from a second plant's template without editing the query.

## 4. Traps when reading records

- **A flattened readiness table.** When a readiness matrix comes from a text extraction, rows and columns can collapse into one list
  and the assignment of status to system is lost. Do not apply it; ask for the slide image or the live matrix. See
  `od-context-freshness/references/fact-triage-and-generated-registers.md`.
- **Repeated status slides** across calls are one status; use the newest.
- **Header-only slides** (a region name with no body) carry no status.
- **Source catalogue extracts** are automatic; open the original (`dept-os/references/provenance-and-source-catalogue.md`).
- **A platform name from an old deck** that the department no longer uses: follow the corrections in the context layer
  (`dept-os/references/swot-and-dependency-seams.md`, section 5).

## 5. Metric hooks

| Task | Metric it moves |
|---|---|
| Machine integration execution | Integrated equipment (year, per month) |
| Acceptance test | Acceptance and rework rate (not captured) |
| Readiness matrix update | System and capability readiness |

How to read each: `od-scorecard-reporting/references/metric-reading-guide.md`.

## AI agent operating notes

- **May do:** pre-fill assessment and acceptance protocols, check the equipment list against the report, draft readiness updates with
  the acceptance evidence attached, test a signal spec against a second plant's template.
- **Evidence to cite:** machine list and report read date, protocol result.
- **Human gate:** no machine connection, no investment approval, no change to signal standards, no external connection without
  Cyber Security / OT sign-off.
- **Hands over to:** `od-use-case-definition` and `od-first-aid-kit` with standardized data.
