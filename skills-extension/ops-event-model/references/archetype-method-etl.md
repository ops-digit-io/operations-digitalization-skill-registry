---
type: Skill Reference
title: Archetype method etl
description: Cross-process, per-process and unique use cases and the action for each, the category to method to ETL job chain, data classes with their hubs, the data-model choice and what to ask of the data platform.
resource: ../SKILL.md
status: draft
tags: [all, practice]
---
# Archetype, method and ETL mapping

Source basis: decks on the library-to-archetype journey, on use-case standardization and on data-type
architecture, abstracted. Gaps are marked `<...>`, own synthesis `PROPOSAL`.

## Three classes and what to do

| Class | Meaning | Action |
|---|---|---|
| **Cross-process standard** | Independent of the core process; constraints exist (for example "cycle time not for continuous processes"); needs integration work because data models are not standardized | Start with priority: high value, scalable |
| **Per-process standard** | Depends on process values of one core process; fewest constraints; scales fastest | Start: medium priority |
| **Unique** | Depends on factory conditions, a legacy system or a one-off problem; not scalable beyond the site | Do not start; run an impact analysis first |

Custom (unique) cases: only if the expected value is very high, prototype first, and integrate into standard
systems before the case counts as mature. Ranking inside the list: generalization potential first, then saving
potential.

A fourth outcome is "just do": generic dashboard, notification or reaction-time cases that need no new
development. Check before assigning an archetype.

## Category to method to ETL job

A collected use case states a need, not a technical requirement. Fix that in this order:

1. **Category** (archetype): for example statistical process control, machine availability, downtime.
2. **Methods** of the category: SPC: descriptive statistics, outlier detection, trend detection. Availability:
   cycle times, setup, errors.
3. **Data-transformation job** per method (ETL or analytics container). When the methods have run and outputs
   exist, the use case is ready to use.
4. Several use cases share the methods of one category. Define the method once.

`PROPOSAL`: record, per category, a row with columns category, objects, events, methods, ETL jobs, owner role,
status. The decks give examples, not a catalogue.

## Data classes and hubs

| Class | Content | Default hub |
|---|---|---|
| Transactional | events, cycle time, counters, set values, limits, alarms; changes hard to propagate | service bus with OPC-UA |
| Time-series | curves, process values; changes easy to propagate | MQTT stream |
| Master data | ERP is the master for material, order and product master data; local systems (MES etc.) are derived and report back; a local master does not lead | leading system |

Routes to the platform: native or OPC-UA machine, aggregation server, or edge device; standardized and
non-standardized transactional and time-series each have their own interface choice. An edge device is needed for
vision or robots, full-traceability expectations (data loss means rejecting parts), high-resolution data from
process-critical sensors, inline measurement, or advanced analytics (see `mi-equipment`).

## Transformation pipeline split

Micro-batching or streaming from the broker for fresh data (roll-ups, statistics on process values, thresholds
from configuration) versus scheduled batch jobs (sync mapping files, build roll-ups). Choose per method; say
which signals need which.

## Data-model choice

- A general base data model fits greenfield, discrete, time-series-centric machines; brownfield with many
  controllers and continuous processes needed other models.
- Process-specific model, five steps: survey public standards and companion specifications; draft the in-house
  type extension; combine with the public standard and make an example instance for one machine; review with
  process engineering until release; instantiate per machine and roll out.
- Object-centric event log: cheap, public standard, relational (self-service dashboards work), flexible types
  and relations. Disadvantages: high abstraction, high transformation effort, subject-matter-expert effort per
  process, risk of chaos with bottom-up flexibility, no event-to-event relation.
- Choose after the object and event questions, not before. `<to confirm>` the platform decision with the
  data-platform owner.

## Data requirements for the data platform

For each use case, state: objects and identifiers with source; events (source or derived) with rule; time
resolution; relation to production metadata; data class and hub; leading system for master data; ETL jobs
(new or existing); retention if claims traceability applies; open gaps. Use
[`../assets/data-requirements-statement.md`](../assets/data-requirements-statement.md).

## Handoff package to build

Signal list with source (machine / checklist / system); error-number-to-message mapping; start/stop signals for
cycle time; first datasets; method and ETL list. A general ETL concept is a precondition: without it a notable
part of use cases cannot be executed.
