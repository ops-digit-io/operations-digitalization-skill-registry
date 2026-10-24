---
type: Skill Reference
title: Worked examples
description: Three real use cases carried through the four phases - a complete record, one correctly stopped before Control, and a minimal-but-correct standard case.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [use-case-support-service, examples]
derived_from:
  - personal vault, Graph/Use Cases/Alarms Notifications.md, Analytics at Brazing.md, 402-403 Lines.md, read 2026-09-17
generated: { by: claude-code/1, at: 2026-09-17T00:00:00Z }
---

# Worked examples

Names, plants and figures are as recorded; nothing here is invented.

## 1 · Alarms Notifications — Delicias

Non-standard, cross-process. Delivered: `PRODUCTIVE`, daily utilization.

| Phase | On record |
|---|---|
| Collect | Business process: Daily Gemba, Troubleshooting, Utilization Improvement, Activity Tracking. |
| Analyse | *"LAX Oven stays at operating temperature with no chain movement, leaking energy without anyone noticing. Autoclaves 2, 3 & 4 can interrupt their curing cycles silently. Without context on the interrupted step or elapsed time, operators cannot decide if the load is salvageable or must be scrapped."* |
| Assess | Blockers: *"Need to validate the exact PLC tag names and step-chain integers for Autoclaves 2 and 4 (logic confirmed for Autoclave 3)."* Machine Blockers: *"No signals from IT network are accessible from Node-RED."* Four machines named. Tool: Data Science Factory. |
| Control | *"Trigger when TEMP_OK = TRUE and Chain_Running = FALSE for more than 10 minutes."* Output asset: Analytics Workflow. |

Every phase answers with something a different engineer could act on without a follow-up
question — exact thresholds, named machines, blockers with their current state named per
machine ("confirmed for Autoclave 3", not yet for 2 and 4).

## 2 · Analytics at Brazing — Karben

Non-standard, unique. Status: `IDEA`, `PRIO3`.

| Phase | On record |
|---|---|
| Collect | Targets: Quality Losses. Service line: Analytical Support Service. |
| Analyse | *"Aluminium Parts are brazed on different stations (round tables); Destructive Testing is done at Brazing Process; Brazing might be the Root Cause for Leaking parts during the Helium Process."* |
| Assess | Blockers: *"Tag List for Process Values needs to be analysed \| available Tags are not sufficient, further Process Knowhow needed."* Machine Blockers: *"Flame Brazing postponed >> No brazing machines planned to be integrated."* |
| Control | Did not proceed. |

See `references/patterns.md` § *A blocked use case is a finding, not a failure* — the
diagnosis is real and specific; Control didn't happen because Assess found a precondition
(the machine was never scheduled for integration) that this skill has no authority to fix.

## 3 · 402/403 Lines — Qingdao

Standard, cross-process. Delivered: `IMPLEMENTED` → `PRODUCTIVE`, daily utilization.

| Phase | On record |
|---|---|
| Collect | Business process: Daily Gemba, Utilization Improvement. |
| Analyse | *"OEE Dashboard - for 402&403 Lines."* |
| Assess | Two machines named (AC402, AC403 Rubber extrusion). |
| Control | Capability epic: OEE Calculation. Tool: MSB 4.0. |

See `references/patterns.md` § *Match effort to category* — the objective is one line
because OEE Calculation's objective, KPI set and requirements are already fixed by the
template; this instance only had to say which lines.
