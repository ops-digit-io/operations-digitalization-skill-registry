---
type: Skill Reference
title: Dashboard worked examples
description: Fourteen of the best-documented dashboards of the 1,010 dashboard notes, each with plant, template, size, the use case it serves, the signals and variables it reads, and the one lesson it teaches for a new build.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [analytical-support-service, practice, dashboard]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Dashboard worked examples

**How they were picked.** All 1,010 notes in `Dashboard Exports/Dashboard Notes` were read (front
matter and the generated sections) and scored: strength of the use-case link (high/medium),
machines linked, a description recorded in Grafana, 10 to 70 panels, a non-lifecycle folder, a
placed template, a screenshot, and note length. The top 80 were then spread over plants and
templates. The score is a convenience, not a quality judgement; "richest" means *best
documented*, not *best designed*. Where a dashboard is a copy family (19 Carei ovens, 9 Mako cells)
one is shown. The notes are AI-drafted and unreviewed; counts are as stated in each note,
exports of 2026-10-29 to 2026-11-03.

Each example gives: **plant / template / folder / size / version and last save**, then the use
case it is linked to (status as recorded), what it reads, and the lesson.

## 1. Helium_Leak_Test - Monterrey

- Process Values; folder `Production`; 23 panels, 28 queries; version 49, saved 2025-10-03.
- Use case "Assembly Helium Leak Test ProcessParameter" (high match, PRODUCTIVE; business process
  Activity Tracking). Dashboard family: Helium Leak Test Traceability.
- Reads: two chambers - cycle time min / average / max, pump states (booster, mechanical),
  helium burp and recovery, pieces tested per hour, final-evacuation pressure with negative
  values excluded. Query labels: `TotalRejects`, `TotalAccepts`, `AcumuladoOK`, `AcumuladoNOK`,
  `Incremento por hora`. Variables: `datasource`, `datatron`, `device`, `datapoints`, `delta`.
  Units: `s` (6), `pressurepsi` (2), `cc/sec` (1). Sections: Quality / Test Results; Process Data.
- **Lesson.** A generic description was copied in ("Process Value discovery dashboard for every
  connected equipment and processes") - it does not describe this board. Write the *issue
  solved* (SPEC-03 S-18). Bad values are filtered in panel titles ("excluding negative values").

## 2. Laser Welding - Production Dashboard - Timisoara

- Andon Board; folder `Laser Welding`; 10 panels, 12 queries; version 66, saved 2026-05-08;
  default 24 h, refresh 1 min.
- Use case "Hourly Output Machine Status" (high, IMPLEMENTED), plus "Process Values (847)"
  (PLANNED). Description recorded: "Dashboard with main production related information for
  the Laser Welding Process."
- Reads: state, mode, part number, tube number, running / not running, hourly output, status
  statistics. **One variable per signal**: `part_produced_trigger`, `machine_status`,
  `cycle_time`, `partnumber`, `tube_partnumber`, `machine_running`, plus `area`, `datatron`, `plc`.
- **Lesson.** The cleanest signal contract in the set: the variables *are* the signal list. A
  second laser-welding cell is a change of variable values, not of SQL. The companion "Laser
  Welding - Andon Board" (54 panels) is the same signals at line level.

## 3. Desma 2K Injection Molding - Level 2 - Production Overview - Dolne Vestenice

- Andon Board; folder `Desma 2k Presses`; 14 panels, 30 queries; version 118, saved 2026-06-10.
- Three linked use cases, Level 1 Andon (IMPLEMENTED), Level 1 Card View (PRODUCTIVE), Level 2
  Production Overview (PRODUCTIVE).
- Reads: cycle-speed gauge, machine state durations per shift, state, workplace, part number,
  mould, material, cycle count, hourly output, cycle time and its statistics. Variables:
  `machine_state`, `order_number`, `material_number`, `mould_number`, `production_quantity`,
  `cycle_time`, injection-unit plastification / injection / dwell-pressure times for both units,
  `real_cure_time`, `part_counter`, `injection_counter`.
- **Lesson.** The three-level pattern (card view, production overview, process values) with one
  signal set. 118 saved versions say it is edited live, not provisioned from files (SPEC-01 F5).

## 4. BMW KL34 - Cycle Time Overview - Dolne Vestenice

- Cycle Time; folder `Assembly - KL34`; **100 panels**, 75 queries, 3 rows; version 59, saved
  2025-11-28; unit `s` on 75 panels.
- Use case "BMW KL34 CycleTime Breakdown" (high, IMPLEMENTED; Utilization Improvement, Activity
  Tracking).
- Reads: per module (M10 to M100 on a machine-layout picture) average / min / max / last cycle
  time, histogram and line chart. Variables only `min_val`, `max_val`, so the signals are presumably bound by literal UUID (not checked).
- **Lesson.** 100 panels because the pattern is repeated per module by hand (33 stat, 25 text, 21
  histogram, 11 gauge, 10 timeseries). It is over the 40-panel line of SPEC-03 S-05 and uses
  literal UUIDs; a repeat-by-variable panel would be the fix. The row "Machine Layout &
  Dashboard Description" is a good habit.

## 5. Downtime Report_BMW_FAAR - Mako

- Andon Board per the link (it is a downtime app view); folder `Downtime App`; 14 panels,
  5 rows; created 2026-08-11, version 7.
- Use cases: Blue / Blue 2 / Blue 3 Cell PCB Board OPEX (high, IMPLEMENTED; Daily Gemba).
- Reads: total downtime, incident count, MTTR, MTBF, P95 duration, unassigned %, auto-detected %,
  Pareto by machine stacked by reason, rankings, state timeline, day-of-week by hour heat map,
  duration histogram, top-500 incidents. Variables: `machine`, `reason`, `severity`,
  `min_duration_min`, `max_duration_min`, `auto_detected`.
- **Lesson.** The only downtime dashboard on the relational incident tables (the Mako design that
  SPEC-02 proposes as the shared schema). It mixes machine detection with an operator reason:
  the reason is a record, so `od-requirements-breakdown` applies. Template placement
  (Andon Board) is debatable by rule R9 - this is Downtime Reporting.

## 6. 15_Anoflex_SO_15 - Carei (one of 19)

- Process Values; folder `Hall 3 - Silicon Area`; 19 panels, 21 queries; version 5, saved
  2026-05-12; refresh 1 min.
- Use cases "Anoflex Oven SO 15 17" and "Anoflex SO 15" (high, PRODUCTIVE; epic Rubber
  Vulcanization). Tags Rubber, Curing.
- Reads: actual program name, temperature set point / actual / min / max and time series, conveyor
  speed set and actual, up-heat start and achieved timestamps, period, starting temperature.
  Units `celsius` (7), `m/min` (3).
- **Lesson.** 19 per-oven dashboards, 5 marked "(old)", plus a "Curing Oven Dynamic" dashboard
  (`99_Curing_Oven_Dynamic`) that selects the oven by variable and has zero literal UUIDs. Build
  the dynamic one first (SPEC-04 class B).

## 7. Shot Weight Overview - Somersworth

- Process Values; folder `Process Values`; 33 panels, 44 queries; version 35, saved 2025-09-21;
  default 3 h.
- Use case "Automatic Material Shot Weight Reporting" (high, PRODUCTIVE; epic Plastic Blow
  Molding; non-standard, unique). Family: Blow Molding Process Changes, Scrap and Shot Weight.
- Reads: shot weight per blow-moulding machine against limits with OK/NOK, a trend. Variables:
  `datatron`, `plc`, `delta`, `datapoints_red`, `partnumber`, `partnumber_process_value` and
  **`partnumber_bm01` ... `partnumber_bm12`**.
- **Lesson.** One variable per machine is variable binding done halfway: twelve variables where
  one machine picker would do. The dashboard works; the copy to a second plant is the cost.

## 8. Drying Hopper Dashboard - Somersworth

- Process Values; folder `Plastics Material Conveying`; **154 panels, 154 queries** (96 stat, 29
  text, 29 ECharts); version 90, saved 2025-12-11; default 1 h.
- Use case "Drying Hopper Dashboard" (high, PRODUCTIVE). Tags Plastic, Treatment.
- Reads: drying hoppers - state, material level, last state change, receiver state, load counter,
  active set temperature versus process temperature. Units: `fahrenheit` (28), `percent` (12).
- **Lesson.** The largest panel count among the examples: one row "For Hopper:" repeated 154
  times by hand. Units are Fahrenheit (28 panels); Somersworth is a US plant, and the estate has 41
  `fahrenheit` panels against 1,026 `celsius` (SPEC-03). SPEC-03 S-10 asks for one unit per
  quantity; state the unit in the signal record so a copy to another plant converts, not guesses.

## 9. Availability per Machine - Qingdao

- Downtime Reporting per link (medium match to "Availability for Machines", IMPLEMENTED; Daily
  Gemba, Utilization Improvement); folder `In Use`; 14 panels, 26 queries; **version 1, created
  2026-05-22, default time range fixed to 2023-07-25 to 2023-08-04**.
- Reads: OEE A / P / AP gauges, machine status duration as bar and pie, per-day durations (Setup,
  Planned loading time, Planned downtime, Breakdown, Manual operating), raw state-change table
  from the MQTT broker (strings `Normal Operating`, `Break Down`).
- **Lesson.** Saved with an absolute 2023 range: it opens on 2023 data. Check the default range
  (SPEC-03 S-14). OEE P and AP read 0.00% in the capture while A reads 95.84% - a missing
  standard time (see the OEE card in the families catalogue).

## 10. Andon Board Autoclaves - Delicias

- Andon Board; folder `Production`; 59 panels (43 stat), 50 queries, 2 rows (Autoclaves Activas /
  Desactivadas); version 77, saved 2026-10-01; default `now/d+6h`, refresh 1 min.
- Use cases "Rubber AndonBoard Autoclaves" (IMPLEMENTED) and "Vulcanization Autoclaves Steps
  Visualization" (PRODUCTIVE), both medium matches; Spanish.
- Reads: daily downtime and largest downtime per autoclave (AC2 to AC7), floor comments with
  shift, user, severity and tags (labels `Turno`, `Usuario`, `Severidad`, `Etiquetas`,
  `Fecha de registro`).
- **Lesson.** A shift-aligned default range (`now/d+6h`) and a comment table that turns the board
  into a record: both are the right instinct. The autoclave list is typed per row, so adding
  AC8 is a copy of panels. Activa/Desactivada rows are the lifecycle of machines shown on the
  board itself.

## 11. TPV 1 - Focus Parameters - Waltershausen

- Placed as Analytics (medium); folder `WTH1 - Hall 135/PC35/TPV 1`; 55 panels (47 timeseries), 15
  rows, **127 queries**; version 71, saved 2026-10-08; German; tags process, engineering, Plastic,
  Extrusion.
- Use cases: TPV Line Vacuum Control Parameter Recommendation (IDEA), Zwick Pull-off Test TPV
  Layer Adhesion (PRODUCTIVE).
- Reads: article, recipe number and name, family/material, dimension, line speed, dryer set
  and actual, dew point, extruder 1 zones 0 to 8, melt temperature/pressure/speed, calibration-tank
  vacuum and temperature, ultrasonic measurement, knitting machine, preheating, extruder 2, X-ray
  wall thickness and diameter, laser gauge, material drying, belt take-off.
- **Lesson.** A complete signal inventory of a plastic extrusion line in one place - useful as the
  checklist for the same line type at another plant. By rule R4 (equipment process dashboard =
  Process Values) the Analytics placement is a candidate for the placement review (see
  `capability-templates-and-placement.md`).

## 12. Assembly BMW FAAR - Hourly Output with Targets - Mako

- Andon Board; folder `Assembly Area - BMW FAAR`; 6 panels, 17 queries, 1 row ("TARGETS - WITH
  NUMBER OF OPERATORS"); version 44, saved 2025-03-13.
- Use cases "Blue / Blue 2 / Blue 3 Cell PCB Board OPEX" (high, IMPLEMENTED; Daily Gemba).
- Reads: actual and customer part number, hourly output for `$device`; query labels
  `Internal_Partnumber`, `InternalPart_CellName_Combination`, `Datamatrixcode`, `Cell_Name`,
  `Machine_Station_Number`, `Leakage_Result`, `Leakage_Result_Rating`, `Assembly_Result_Rating`.
  **13 variables, one per result column.**
- **Lesson.** Per-part traceability (datamatrix, leak result, assembly result) next to hourly
  output with an operator count. The variables again mirror the result record - a table schema
  disguised as variables. Eight cells share the pattern: build one, vary the cell name.

## 13. Erlas Welding - Karben

- Process Values (medium); folder `Halle 4 - HDEP / HDES`; 6 panels (3 ECharts), 12 queries, 3 rows
  (Zelle 1 to 3); version 17, saved 2026-09-22; default 5 min.
- Use cases only IDEA-status (HDEP Laser Welding, Process Control, Weld Line Inspection).
- Reads: `Soll-Leistung` and `Ist-Leistung` (set and actual power) and their distribution.
- **Lesson.** A live process-value board ahead of its use case: the link to a delivered use case
  is weak. Also the smallest honest example of the setpoint/actual pair - one set, one actual,
  per cell. German labels `Soll` / `Ist` are the plant's own.

## 14. Plant Overview - Sun Prairie

- Andon Board (medium); folder `Area Managers`; 38 stat panels, 38 queries, 6 rows (Extrusion,
  Braiders, Covers, Cures, Packing, Mandrel Prep); **version 102, saved 2026-10-22**; default
  15 min, refresh 5 s; **Grafana 8.2.7, InfluxDB, no UUID**.
- Use case "Plant Overview" (PRODUCTIVE; Process-All, per process).
- Reads: one tile per machine - Extrusion 301 to 304, Braiders B37 to B48, Covers 1 to 4, Cures
  1 and 2, Packing 1 to 9, Mandrel Prep 1 to 7 - each bound by `CT/OESL/NA/USA/SPR/...` topic
  (leaf `Line_Running` in the sampled sibling).
- **Lesson.** The plant-level status board on the other data family (InfluxDB, topic-bound), at
  5 s refresh. The `CT` topic path is the interface (`od-node-red-flow-builder`,
  `topic-conventions.md`).

## What the fourteen have in common

1. Eleven of the fourteen are linked to a use case with status PRODUCTIVE or IMPLEMENTED (1 to 8,
   10, 12 and 14); examples 9, 10 and 11 are medium matches, and 13 links only to IDEA use cases.
2. 13 of 14 have a relative default time range; two are shift- or day-aligned (`now/d+7h`,
   `now/d+6h`); one (no. 9) is saved on an absolute 2023 range.
3. The best contracts (2, 3) put the signal list in template variables; the worst copy a pattern
   by hand 100 to 154 times (4, 8).
4. None of the descriptions read names an owner role (SPEC-03 S-04 is not measured in the estate;
   only 128 of 1,010 dashboards have any description).
