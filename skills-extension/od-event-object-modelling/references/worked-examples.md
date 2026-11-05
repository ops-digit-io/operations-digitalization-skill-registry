---
type: Skill Reference
title: Worked examples
description: Illustrative reductions of plant sentences to objects, events and archetypes, plus a cycle-time and a downtime case; invented, with placeholders.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Worked examples (illustrative)

All examples are illustrative, built from request patterns in the decks. Names are `<placeholders>`.

## 1 "Which carrier is in the oven now?"

| Canvas field | Content |
|---|---|
| Objects | carrier, `<part or serial>` |
| Events | carrier enters oven, carrier leaves oven |
| Time | live view |
| Signals | carrier id `<tag>` (object identifier), entry and exit `<tags>` (source events) |
| Relation | carrier to part: `<where is it recorded>`; if only a manual entry, it is a data gap |
| Class | `<per-process>` if the oven type recurs; `<unique>` if tied to one legacy system |

## 2 "All serials produced today with quality status"

Object: serial. Event: quality result recorded. Time: report on a cadence. The relation serial to time-series
comes from `<PLC serial signal or MES>`. Without it, no trace; route as a data gap to
`od-data-availability-check`. Same shape as "which order ran yesterday and how many defects" (object: order).

## 3 "Machine errors by station with reason code over time"

Object: station. Event: machine error (source event, boolean tag). Reason code needs the error-number-to-message
mapping. Class: cross-process (availability category: errors). Method: count and rank errors; ETL job:
`<roll-up per station and reason>`.

## 4 Cycle time

A transactional record gives a cycle time that looks too short. Use the time-series with an overridden
start/stop, built in an edge flow; then look at sequence features (for example unload) for the cause.
Event: cycle start and stop, derived. Method named before promising the analysis.

## 5 Downtime with operator input

Automatic detection by rule (good-part counter does not increment; stop longer than a threshold), pop-up to the
operator, reasons during the shift, rest completed at end of shift. Open questions before design: one tablet
for several machines? how is downtime closed with several operators? planning per machine or per cell? Category:
downtime. Hybrid capture applies.
