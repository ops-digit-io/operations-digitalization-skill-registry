---
type: Skill Reference
title: Worked examples
description: Three illustrative use cases (invented, with placeholder values) carried through the four phases - a complete record, one correctly stopped before Control, and a minimal-but-correct standard case.
resource: ../SKILL.md
status: stable
tags: [use-case-support-service, examples]
---

# Worked examples

**Illustrative.** All plants, machines, tags and thresholds below are invented placeholders. They show the *shape* of a good
record; they are not records of real use cases. Pattern source: the use-case notes in the knowledge base.

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
| Collect | Targets: Quality Losses. Origin: ad-hoc analytics (the retired Analytical Support Service), now Lane 2 once it recurs. |
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

## 4 · A complete fictional example, in words: from idea to next step

**Fictional.** Every plant, number and role below is invented to show how the ten questions of `assets/idea-check.md` (`../assets/idea-check.md`) are answered and what the one-page summary looks like. None of it is a record of a real use case or a company figure. Do not copy any figure into a ledger, a business case or a deck.

A shift lead at fictional Plant F thinks the hourly part counts on line 3 should not be written on paper.

| Question | Answer in the shift lead's words |
|---|---|
| 1. Done already? | "I asked the key user at the neighbouring plant and looked in the library: a counting screen exists there, but nobody has recorded a decision to share it. So I cannot just take it." (Not catalogued: this goes on to Lane 2, with the neighbouring plant's screen as the closest precedent.) |
| 2. One need? | "Line 3's hourly counts are only known after the shift." (One sentence, no "and".) |
| 3. When and how often? | "At the hourly check and at shift handover, every shift." |
| 4. Today / instead | "Today the count is written on a board and typed into a spreadsheet at shift end, so a slow hour is seen the next day. It should be visible during the hour." |
| 5. Where, when, who | "Line 3 and not line 4, which has a counter on its machine. Every shift. The line operators and I." |
| 6. Why? | "Why on paper? The machine does not publish counts. Why not? Nobody asked for the signal when it was installed. Why not now? The controller is not connected." (Stops at something actionable.) |
| 7. Who acts differently | "I, as shift lead, would react within the hour; the area owner would confirm in the daily review that I did." |
| 8. Data and machine | "The count comes from the line 3 controller. It is not connected today." (So the first step is a connection: Lane 3, branch 3b, before any screen.) |
| 9. Tried and alternatives | "A bigger paper board did not help. Alternatives: do nothing; or only measure the slowest machine." |
| 10. Size | "Twelve minutes per shift is spent on the paper count (fictional estimate, my own watch, not measured). Three shifts. Unknown: the cost per hour: I will ask plant Controlling." |

**One-page summary (fictional).**

| | |
|---|---|
| Idea | Show line 3's hourly part count during the hour, without paper. |
| Plant and line | Plant F, line 3 |
| Moment and frequency | Hourly check and shift handover, every shift |
| Today / should be | Counted on paper, seen next day / visible during the hour |
| Who acts, who confirms | Shift lead / area owner in the daily review |
| Data and machine | Line 3 controller; **not connected** |
| Already exists? | A similar screen at a neighbouring plant; no recorded decision to share it |
| Size and source | 12 minutes per shift, three shifts (fictional, estimate, own watch); cost per hour unknown, ask plant Controlling |
| Next step | Lane 2 (a new recurring need) with a connection request (Lane 3, branch 3b) as the first dependency |

What happens next: the DBVE runs the full questionnaire with the shift lead, the data check confirms the signal, and a business case is built (`bc-build`, "First estimate in five steps" gives the rough range the shift lead can already make).

