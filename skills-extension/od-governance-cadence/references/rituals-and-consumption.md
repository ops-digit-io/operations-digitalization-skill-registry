---
type: Skill Reference
title: Rituals and consumption
description: The recurring formats in which the function's output is actually consumed (daily Gemba, shift checks, escalation, portfolio review, rollout waves), how to find the ritual behind a use case, and how the plant rituals relate to the department's own ladder of routines from shift to round.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, cadence, gemba]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Rituals and consumption

Derived from the vault note on department rituals and the lane and operating-context notes. Method only: counts of use cases,
utilization splits and review totals in the source are not reproduced; look them up on the live lists. Own synthesis is marked
`PROPOSAL`; unknowns are `<...>`.

## The principle

**A dashboard that is not read inside a recurring format is a dashboard nobody reads.** The rituals below are the consumers of what
the function builds. Before a use case is defined, built or counted as delivered, name the ritual that will consume it. This is the
same rule `od-analytics-asset-build` applies at build time; here it is stated from the plant's side.

## The plant rituals

| Ritual | What it is | What the asset must do for it | What to ask the plant |
|---|---|---|---|
| **Daily Gemba** | The shop-floor walk. The largest single consumer of what the function builds. Needs current numbers at the line, not a report assembled afterwards | Be current at the line, readable standing up, same layout on every line that is walked | Who walks, at what time, which board do they stop at, what do they do when a number is red |
| **Shift checks** | A supervisor checks a figure (output, speed, availability) at fixed points in the shift and talks to the operators when the goal is missed. Recorded in the plant's own standard procedure | Fit or replace a defined standard procedure; show the same figure the procedure names, at the checking moments | What is the written procedure, how often is the check, who is spoken to, where is the result written down today |
| **Escalation** | Andon signalling, two-step by design: the first signal asks for help without stopping the line, the second stops it if unresolved. Tiers are defined, each with a time-boxed response | Raise by hand and automatically from the machine; route to the tier; **log every event**, not only display it | What are the tiers, who answers each, how long may each take, where do events go afterwards |
| **Portfolio review (sprint review)** | Where a tracked saving becomes a proven one | Provide the use-case record, the utilization evidence and the saving basis the review needs | Which rows are due, what evidence is missing |
| **Rollout waves** | Work is batched into phases tied to named plant projects, not delivered continuously | Carry the phase on the use-case record so the wave can be planned and reported | Which wave is the plant in, what does the wave already include |

The Andon pattern in particular is the case for one cross-plant standard: what it replaces is a different whiteboard at every site.
The standard's definition, KPI set and requirements checklist belong to `od-use-case-standardization`; this file only says why the
ritual matters.

## Finding the ritual behind a use case

Work through these in order and stop when one is answered with a named person and a time.

1. Is there a standard procedure that names the figure? Then the use case supports or replaces that procedure - say which.
2. Is there a recurring meeting (daily Gemba, shift handover, production meeting, process-improvement meeting) where the figure is
   discussed? Name the meeting, its level, its chair.
3. Is there an escalation tier that the signal should feed? Name the tier and the response time-box.
4. None of the three: **it is a dashboard without an action owner.** Do not build it; take it back to definition
   (`od-use-case-definition`, `od-analytics-asset-build/references/process-chain-practice.md`).

## Utilization follows the ritual

The utilization frequencies recorded on use cases are dominated by the daily rhythm; the daily walk is visible in the data.
Consequence for reading a utilization record: a use case recorded as used rarely, or never, usually has no ritual, not a bad
screen. Ask for the ritual first, redesign second. The utilization columns to collect are in
`od-handover-and-adoption`; the utilization review is in `od-scorecard-reporting`.

## The ladder of routines

The plant rituals sit at the bottom of a ladder that the department's own routines continue (rungs on request or on the department's own schedule; none is a mandatory fixed meeting). Use the ladder to decide where a
recurring question belongs.

| Rung | Plant side | Department side | Owner skill |
|---|---|---|---|
| Per shift | Shift checks, escalation tiers | none (plant owned) | plant owner |
| Daily | Gemba walk | none | plant owner |
| Weekly to sprint | Sprint working session | use-case sprint | `references/sprint-runbook.md` |
| Monthly | Utilization review, portfolio review | scorecard update, retrospective | `od-scorecard-reporting`, `od-retro` |
| Quarterly | Roadmap check | context-layer review, SWOT and strategy check, freshness sweep | `od-context-freshness`, `od-context` |
| Round | Regional community call | CoP; ODEC only as a historical source | `references/forums-and-roadmap.md` |

`PROPOSAL`: when a plant raises a recurring complaint that spans rungs (a board that is correct but ignored), route it to the lowest
rung that has an owner: first the plant ritual, then the sprint, then the utilization review. Only a pattern across plants goes to a round.

## Pitfalls

- Counting a use case as delivered when its ritual is "to be defined". It will show up later as low utilization.
- Designing the screen for the report reader (seated, after the fact) when the ritual is standing at the line.
- Displaying an escalation without logging it: the log is the only thing that makes the improvement analysis possible afterwards.
- Confusing a rollout wave with a delivery date for a single plant; the wave batches several plants and several tools.
- Treating shift-check habits as noise. They are the standard procedure the solution has to fit.

## AI agent operating notes

- **May do:** list, for a use case, which ritual is recorded and which of the three finding questions is unanswered; draft the question
  list for the plant; check that an Andon-type use case records tiers, time-boxes and an event log; flag use cases with a utilization
  record but no ritual.
- **Inputs:** the use-case record (process, utilization method, frequency, related meeting), the plant's standard procedures if
  available, the phase field.
- **Evidence to cite:** list and field names, read date.
- **Human gate:** the plant process owner confirms the ritual and the action owner; the agent never infers a ritual from the
  asset type.
- **Hands over to:** `od-use-case-definition` (ritual named), `od-analytics-asset-build` (design for the ritual), `od-handover-and-adoption`
  (utilization method).
