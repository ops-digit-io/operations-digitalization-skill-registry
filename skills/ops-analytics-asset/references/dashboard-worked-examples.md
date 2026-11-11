---
type: Skill Reference
title: Dashboard worked examples
description: Fourteen illustrative dashboard patterns (not real dashboards), each with the template it falls under, what it reads, and the one lesson it teaches for a new build; plus how to pick real examples from the dashboard notes. No plant names, sizes, versions or dates.
resource: ../SKILL.md
status: draft
tags: [analytical-support-service, practice, dashboard]
---
# Dashboard worked examples

**All examples below are illustrative.** They are patterns distilled from the dashboard notes in
`Dashboard Exports/Dashboard Notes`, with plant names, sizes, versions, dates and use-case
statuses removed. For a real, current example, pick one from the notes (section "Picking real
examples"), read its note and open its JSON.

## Picking real examples

Score each note on: strength of the use-case link (high/medium), machines linked, a description
recorded in Grafana, a moderate panel count, a non-lifecycle folder, a placed template, a
screenshot, note length. Spread the top candidates over plants and templates. The score is a
convenience, not a quality judgement; "richest" means *best documented*, not *best designed*. Where
a dashboard is a copy family (per-oven, per-cell) look at one. The notes are AI-drafted and
unreviewed. State the export run when you cite a dashboard.

Each pattern gives: **template / what it reads / lesson.**

## 1. Leak-test station board
- Process Values. Two chambers: cycle time min / average / max, pump states, recovery, pieces tested
  per hour, final-evacuation pressure with negative values excluded. Variables: `datasource`,
  `datatron`, `device`, `datapoints`, `delta`.
- **Lesson.** A generic description was copied in ("Process Value discovery dashboard for every
  connected equipment") and does not describe this board. Write the *issue solved* (SPEC-03 S-18).
  Bad values are filtered in panel titles ("excluding negative values") instead of in the signal.

## 2. Laser welding production board
- Andon Board. State, mode, part number, running / not running, hourly output, status statistics.
  **One variable per signal**: `part_produced_trigger`, `machine_status`, `cycle_time`, `partnumber`,
  `machine_running`, plus `area`, `datatron`, `plc`.
- **Lesson.** The cleanest signal contract: the variables *are* the signal list. A second cell is a
  change of variable values, not of SQL. A companion line-level board uses the same signals.

## 3. Three-tier injection moulding set
- Andon Board, three linked use cases (Level 1 Andon, Level 1 Card View, Level 2 Production
  Overview). Reads: cycle-speed gauge, state durations per shift, state, workplace, part number,
  mould, material, cycle count, hourly output, cycle time and its statistics.
- **Lesson.** The three-level pattern (card view, production overview, process values) with one
  signal set. A high version count says the dashboard is edited live, not provisioned from files
  (SPEC-01 F5).

## 4. Assembly cycle-time overview
- Cycle Time. Per module on a machine-layout picture: average / min / max / last cycle time,
  histogram and line chart. Variables only `min_val`, `max_val`, so signals are presumably bound by
  literal UUID.
- **Lesson.** A very large panel count because the pattern is repeated per module by hand. Over the
  panel limit of SPEC-03 S-05 and literal-UUID bound; a repeat-by-variable panel is the fix. The row
  "Machine Layout & Dashboard Description" is a good habit.

## 5. Downtime report on relational incident tables
- Downtime Reporting (may be filed as Andon Board). Reads: total downtime, incident count, MTTR,
  MTBF, P95 duration, unassigned share, auto-detected share, Pareto by machine stacked by reason,
  rankings, state timeline, day-of-week by hour heat map, duration histogram, incident table.
  Variables: `machine`, `reason`, `severity`, `min_duration_min`, `max_duration_min`, `auto_detected`.
- **Lesson.** The downtime design that SPEC-02 proposes as the shared schema. It mixes machine
  detection with an operator reason: the reason is a record, so `funnel-requirements` applies.
  Template placement is debatable by rule R9 - stop events are Downtime Reporting.

## 6. Per-oven copy family plus a dynamic version
- Process Values. Actual program name, temperature set point / actual / min / max and time series,
  conveyor speed set and actual, up-heat timestamps, period, starting temperature.
- **Lesson.** Many per-oven dashboards (some marked "(old)") next to a dynamic dashboard that selects
  the oven by variable and has zero literal UUIDs. Build the dynamic one first (SPEC-04 class B).

## 7. Shot-weight overview with a variable per machine
- Process Values. Shot weight per blow-moulding machine against limits with OK/NOK, a trend.
  Variables: `datatron`, `plc`, `delta`, `datapoints_red`, `partnumber`, and one
  `partnumber_<machine>` variable per machine.
- **Lesson.** One variable per machine is variable binding done halfway: many variables where one
  machine picker would do. The dashboard works; the copy to a second plant is the cost.

## 8. Drying hopper board
- Process Values. Drying hoppers: state, material level, last state change, receiver state, load
  counter, active set temperature versus process temperature.
- **Lesson.** One row repeated by hand per hopper gives a very large panel count. Units were
  Fahrenheit at a US plant while most of the estate is Celsius (SPEC-03); S-10 asks for one unit per
  quantity. State the unit in the signal record so a copy to another plant converts, not guesses.

## 9. Availability per machine
- Downtime Reporting by link (really OEE Calculation). OEE A / P / AP gauges, machine status duration
  as bar and pie, per-day durations (Setup, Planned loading time, Planned downtime, Breakdown,
  Manual operating), raw state-change table from the MQTT broker.
- **Lesson.** Saved with an absolute date range from years ago: it opens on old data. Check the
  default range (SPEC-03 S-14). OEE P and AP reading zero while A is plausible points at a missing
  standard time (see the OEE card in the families catalogue).

## 10. Autoclave Andon board with floor comments
- Andon Board. Two rows (active / inactive autoclaves); daily downtime and largest downtime per
  autoclave; floor comments with shift, user, severity and tags; Spanish labels.
- **Lesson.** A shift-aligned default range and a comment table that turns the board into a record:
  both are the right instinct. The autoclave list is typed per row, so adding one is a copy of
  panels. Active/inactive rows are the lifecycle of machines shown on the board itself.

## 11. Extrusion line focus-parameters board
- Placed as Analytics. Article, recipe number and name, family/material, dimension, line speed, dryer
  set and actual, dew point, extruder zones, melt temperature/pressure/speed, calibration-tank vacuum
  and temperature, ultrasonic measurement, knitting machine, preheating, second extruder, X-ray wall
  thickness and diameter, laser gauge, material drying, belt take-off.
- **Lesson.** A complete signal inventory of a plastic extrusion line in one place - useful as the
  checklist for the same line type at another plant. By rule R4 (equipment process dashboard =
  Process Values) the Analytics placement is a candidate for the placement review.

## 12. Hourly output with targets and traceability columns
- Andon Board. Actual and customer part number, hourly output for `$device`; query labels such as
  `Internal_Partnumber`, `Datamatrixcode`, `Cell_Name`, `Leakage_Result`, `Assembly_Result_Rating`.
  One variable per result column.
- **Lesson.** Per-part traceability next to hourly output with an operator count. The variables
  mirror the result record - a table schema disguised as variables. Several cells share the pattern:
  build one, vary the cell name.

## 13. Welding cell power board ahead of its use case
- Process Values (medium). A few panels: `Soll-Leistung` and `Ist-Leistung` (set and actual power) and
  their distribution, one block per cell.
- **Lesson.** A live process-value board ahead of its use case: the link to a delivered use case is
  weak. Also the smallest honest example of the setpoint/actual pair. German labels `Soll` / `Ist` are
  the plant's own.

## 14. Plant overview on the other data family
- Andon Board (medium). One tile per machine, grouped in rows by area, each bound by a
  `CT/OESL/<region>/<country>/<plant>/...` topic (leaf `Line_Running` in the sampled sibling); fast
  refresh; InfluxDB, no UUID, older Grafana server.
- **Lesson.** The plant-level status board on the other data family (InfluxDB, topic-bound). The `CT`
  topic path is the interface (`mi-flow`, `topic-conventions.md`).

## What the patterns have in common

1. Most good examples are linked to a use case that is delivered; some are ahead of their use case
   and the link is weak.
2. Prefer a relative default time range; shift- or day-aligned ranges are legitimate, an absolute
   range saved by accident is a defect.
3. The best contracts (2, 3) put the signal list in template variables; the worst copy a pattern by
   hand (4, 8).
4. Descriptions rarely name an owner role (SPEC-03 S-04); write one.
