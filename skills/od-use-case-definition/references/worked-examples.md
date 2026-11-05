---
type: Skill Reference
title: Worked examples
description: Three illustrative use cases (invented, with placeholder values) carried through the four phases - a complete record, one correctly stopped before Control, and a minimal-but-correct standard case.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [use-case-support-service, examples]
derived_from:
  - personal vault, Graph/Use Cases/*.md, read 2026-09-17 (pattern source only; the examples below are invented)
generated: { by: claude-code/1, at: 2026-09-17T00:00:00Z }
---

# Worked examples

**Illustrative.** All plants, machines, tags and thresholds below are invented placeholders. They show the *shape* of a good
record; they are not records of real use cases. Pattern source: the use-case notes in the vault.

## 1 · Alarm Notification — <plant A>

Non-standard, cross-process. Delivered: `PRODUCTIVE`, daily utilization.

| Phase | On record |
|---|---|
| Collect | Business process: Daily Gemba, Troubleshooting, Utilization Improvement, Activity Tracking. |
| Analyse | *"<Oven> stays at operating temperature with no chain movement, leaking energy without anyone noticing. <Autoclaves> can interrupt their curing cycles silently. Without context on the interrupted step or elapsed time, operators cannot decide if the load is salvageable or must be scrapped."* |
| Assess | Blockers: *"Need to validate the exact PLC tag names and step-chain integers for <machine X> and <machine Z> (logic confirmed for <machine Y>)."* Machine Blockers: *"No signals from IT network are accessible from Node-RED."* Machines named individually. Tool: `<tool>`. |
| Control | *"Trigger when <TEMP_OK> = TRUE and <Chain_Running> = FALSE for more than <n> minutes."* Output asset: Analytics Workflow. |

Every phase answers with something a different engineer could act on without a follow-up
question — exact thresholds, named machines, blockers with their current state named per
machine ("confirmed for Y", not yet for X and Z).

## 2 · Analytics at <process step> — <plant B>

Non-standard, unique. Status: `IDEA`, `PRIO<n>`.

| Phase | On record |
|---|---|
| Collect | Targets: Quality Losses. Service line: Analytical Support Service. |
| Analyse | *"Parts are processed on different stations; destructive testing is done at <process step>; <process step> might be the root cause for leaking parts in the downstream test."* |
| Assess | Blockers: *"Tag list for process values needs to be analysed \| available tags are not sufficient, further process know-how needed."* Machine Blockers: *"<Process> postponed >> no machines planned to be integrated."* |
| Control | Did not proceed. |

See `references/patterns.md` § *A blocked use case is a finding, not a failure* — the
diagnosis is real and specific; Control didn't happen because Assess found a precondition
(the machine was never scheduled for integration) that this skill has no authority to fix.

## 3 · <Line pair> — <plant C>

Standard, cross-process. Delivered: `IMPLEMENTED` → `PRODUCTIVE`, daily utilization.

| Phase | On record |
|---|---|
| Collect | Business process: Daily Gemba, Utilization Improvement. |
| Analyse | *"OEE Dashboard - for <line A> and <line B>."* |
| Assess | Two machines named (`<machine A>`, `<machine B>`). |
| Control | Capability epic: OEE Calculation. Tool: `<tool>`. |

See `references/patterns.md` § *Match effort to category* — the objective is one line
because OEE Calculation's objective, KPI set and requirements are already fixed by the
template; this instance only had to say which lines.
