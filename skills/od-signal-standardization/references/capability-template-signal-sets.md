---
type: Skill Reference
title: Capability template signal sets
description: For each of the 11 use case templates, what the dashboards in the export actually read - signals, template variables, data sources - plus the template's boundary, recorded blocker themes and reference solutions, to be set against the requirement sets in the signal catalogue.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, technical, signals]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Signal sets per capability template

`signal-catalogue.md` ends with the **requirement sets** the analyser checks (`--capability`).
This file is the other half: **what the dashboards that exist for each template read today.**
Use it to ask "does my machine expose what the typical dashboard of this template reads?"
before promising a copy of an existing solution.

**What is a count and what is a rule.** Every number is a count from the export of
2026-11-03/05 (see Sources); "dashboards" means unique (plant, uid) Grafana dashboards, joined
to a template by the dashboard notes (992 of 1,010 joined). The template of a dashboard comes
from a linked use case or, for 286 notes, is `unplaced`; a placement by keyword is an inference
in the source, not a fact. Nothing in the "reads" columns is a requirement - the requirement
sets are in `signal-catalogue.md` and `standards.md`.

## How to use

1. Find the template of your use case (`od-use-case-standardization`; boundary rules R1 to R13 in
   `od-analytics-asset-build/references/capability-templates-and-placement.md`).
2. Compare the "reads" column with the machine's data-point list (analyser: `--cluster`).
3. Anything the dashboards read that the machine does not expose is a gap to route (PLC or
   edge configuration) - see Step 6 of `SKILL.md`.

## The templates

### Andon Board (144 dashboards; median 21 panels)

- **Boundary.** A visual board of the current status of a line, cell, area or plant: Andon and
  Gemba boards (levels 1 to 3), production overview, card view, output against target.
  Not alerts as messages, not the stop log, not the OEE figure itself.
- **Reads (labels and variables seen).** machine state (`MachineState`), part number, total
  parts and OK/NOK (`OK_A`, `NG_A`, `OK_ALL`, `NG_ALL`, `Total Part`), current and last cycle
  time (`CT_A`, `CurrentCycleTime`, `Last Cycle Time`), mode (`Auto`, `Manual`, `Fault`), shift
  (`Turno`), process temperatures and speeds on extrusion boards. Variables: `datasource` 65,
  `datatron` 37, `delta` 28, `plc` 23, `partnumber` 16.
- **Data sources.** `TelemetryPLC` 104 dashboards, `ConfigRepo` 46, `Use-Cases` 24 (a
  separate use-case table, see `od-analytics-asset-build/references/dashboard-estate-baseline.md`).
- **Binding.** 122 of 144 dashboards carry literal UUIDs in SQL (4,156 predicates).
- **Blocker themes on the 134 plant use cases (keyword count in the source).** machine list, PLC
  access or connectivity 3; missing details or scope 3; third-party system 1; additional hardware 1.
- **Reference solutions named by the source.** Extrusion Line Andon Board Set (Halls 1-3), BBM
  Andon Board, Halle 4 Gemba Board.

### OEE Calculation (66 dashboards; median 16 panels)

- **Boundary.** OEE or its components (availability, performance, quality) per machine, line
  or plant. Not the stop events behind availability, not cycle-time analysis.
- **Reads.** `OEE`, `OEE A`, `OEE P`, `OEE Q` (also `OEE_APQ`, `OEE-A half`), average cycle time,
  total parts and job parts (`Jobparts`), shift start and end times, product name, `output`,
  `rate`. Variables: `CycleTimeSetting` 24, `database` 20, `machine_mode` and
  `machine_mode_values` 4 each - the **standard time is a dashboard variable** here.
- **Data sources.** `Telemetry` 34, `InfluxDB` 13 (the Chinese-site OEE dashboards read InfluxDB
  or the `Telemetry` source, not `TelemetryPLC`).
- **Binding.** 41 of 66 dashboards with literal UUIDs; Changchun (25 of the 66), Qingdao (17)
  and Changshu (14) hold most of the family.
- **Reading against the catalogue.** The requirement set `oee` = `MachineStatus`,
  `TotalPartCounter`, `CycleTime`, `StandardSpeed`. The dashboards read a **cycle time setting**
  as a variable and shift times as labels, i.e. the ideal cycle time and the shift pattern live
  in the dashboard. Rule from `standards.md` (ISO 22400-2): agree the ideal cycle time and the
  micro-stop threshold before choosing signals, and store them with the signal, not the panel.
- **Blocker themes.** missing details or scope 2; definitions still to be agreed 1; platform 1;
  PLC access 1; capacity 1.

### Cycle Time (22 dashboards; median 10 panels)

- **Boundary.** Cycle time, takt, loading time, step or throughput time against a standard.
  Not downtime, not the OEE performance figure as a whole.
- **Reads.** `Cycle Time`, `Last/Worst/Best/Average Cycle Time`, `Valid Cycles`, load counter,
  part-produced trigger and part counter (variables `partcounter`, `part_produced_trigger`,
  `cycletime`), station step times (`Zelle 1 IO`, `Zykluszeit`), alert UUID sets.
  Variables: `time_interval`, `alert_uuids`, `alert_message`.
- **Data sources.** `TelemetryPLC` 15, `ConfigRepo` 9.
- **Binding.** 20 of 22 with literal UUIDs; 503 predicates.
- **Reading against the catalogue.** Requirement set `cycle-time` = `CycleStart`, `CycleEnd`.
  The dashboards compute the duration themselves from the trigger and counter; the flow
  artefact "Cycle Time" (55 flows) exists to publish it once.
- **Blocker themes.** none recorded.
- **Reference solutions.** Assembly Line - Cycle Time Statistics per Module, Autoclave - Cycle
  Time, Loading Time and Process Parameter Detail, Automatic Bending - Cycle Time Analysis.

### Downtime Reporting (21 dashboards; median 14 panels)

- **Boundary.** Stop events with duration and reason, operator-entered or machine-detected,
  micro-stops, uptime. Not notifications, not the availability figure.
- **Reads.** `Incidents`, `Total [min]`, `Average [min]`, `Longest [min]`, `Reason`, `Machine`,
  severity, `auto_detected`, minimum and maximum duration; Spanish variants `Paro (min)`,
  `Eventos de paro`, `Duracion total de paros`. Variables: `machine` 8, `reason` 5, `severity` 5,
  `min_duration_min` 5, `auto_detected` 5. **Two designs coexist**: a relational incident table
  (`downtime_incidents`, `downtime_reasons`, `machines` - 7 dashboards, Mako, Testcenter,
  Subotica) and state-change queries on `telemetry` alone.
- **Data sources.** `TelemetryPLC` 9, `ConfigRepo` 8, `Datadash` 6.
- **Reading against the catalogue.** Requirement set `downtime` = `MachineStatus` only.
  The dashboards also need a **reason**, which is not a machine signal: it is entered by an
  operator or classified afterwards. Say who supplies it (SPEC-02 P7: no shared schema across
  plants, proposal D-08).
- **Blocker themes.** machine list / PLC access 1; platform 1; definitions to be agreed 1.
- **Reference solutions.** Downtime Dashboard (Delicias, inferred), Blow Molding Monitoring and
  Downtime (Somersworth, inferred), Downtime Reporting App with Machine Signals and Operator
  Labelling (Mako).

### Machine Alerts (30 dashboards; median 12 panels)

- **Boundary.** Alarms, notifications and tolerance-deviation alerts to people or shown as an
  alert list: machine faults, Teams or SMS notifications, maintenance-due triggers.
- **Reads.** alert UUID set (`alert_uuids`), message (`alert_message`), state, station OK/NOK
  counts, last produced part time, calibration OK/NOK time, last alarm text.
- **Data sources.** `TelemetryPLC` 19, `ConfigRepo` 10.
- **Reading against the catalogue.** Requirement set `alerting` = `ErrorActive`, `AlertMessage`.
  In the flows alerting is mostly a **code-to-message lookup** (32 flows named "Alerting"); the
  dashboards read the alert UUIDs from a variable, so the list of alert points is configuration.
- **Blocker themes (36 use cases).** machine list / PLC access 5; definitions to be agreed 4
  (three of them are one use case, the Teams notification, at three plants); third-party
  system 3.

### Process Values (199 dashboards; median 13 panels)

- **Boundary.** Live machine and process parameters (temperatures, pressures, speeds,
  counters, energy and utility readings), process overviews per machine, line or oven. Not SPC,
  not set-value management, not cross-machine analysis. Energy monitoring belongs here; the
  analysis of usage and peaks is Analytics (rule R5).
- **Reads.** setpoint and actual pairs (`Setpoint`/`Actual`, `Speed setpoint`/`Speed actual`,
  `Temperature_Setpoint`/`Actual_temperature`, `Min`/`Max`), program number, zone temperatures
  (`Actual Zone 1`, `heating_temperature_zone1_act`), conveyor speed, up-heat timestamps,
  mass temperature, extruder screw/head temperature and rotation (`EX1.Head.Temperature process
  value`, `Knitting Machine.Rotation process value`). Variables: `datasource` 113, `delta` 95,
  `datatron` 65, `datapoints` 41 (a generic tag picker), `program_name` 17.
- **Data sources.** `TelemetryPLC` 89, `ConfigRepo` 69, `InfluxDB` 23.
- **Binding.** 98 of 199 with literal UUIDs and 66 with a UUID variable - the only template
  where variable binding is already common (a tag picker over `data_points`).
- **Blocker themes (180 use cases).** machine list / PLC access 10; additional hardware 7;
  platform 3; cyber-security approval 2; third-party system 1.
- **Reading.** Setpoint and actual are two signals on every dashboard of the family; this is the
  reason the catalogue keeps `_sv` apart. The Carei silicone oven family is 19 dashboards that
  differ only by the oven id - a case for one parameterised dashboard (SPEC-04 class B).

### Process Quality Data (46 dashboards; median 7 panels)

- **Boundary.** Automated in-process quality: inline measurement, SPC and capability, vision
  inspection, test results, scrap counting, jidoka stops, per-part traceability. Not data typed
  by hand.
- **Reads.** `Upper/Lower` intervention limits (`Obere/Untere Eingriffsgrenze`), `PV`/`SV`,
  `Recipe`, `RecipeID`, article number, last data-matrix code, checklists, IO/NIO per cell.
  Variables: `machine` 12, `partnumber` 9, `isDelta` 5. A second source family appears:
  `QFPR - Productive` (12 dashboards; Waltershausen is the plant that declares it) and `LabData` (5).
- **Binding.** 26 of 46 with literal UUIDs (707 predicates).
- **Blocker themes (55 use cases).** platform / data model 12; machine list / PLC access 7;
  missing scope 5; hardware 3; capacity 1.
- **Reading against the catalogue.** Requirement sets `tolerance` and `traceability`. The
  quality-and-limits family is the best-named in the estate (`signal-catalogue.md`); the
  dashboards confirm it by reading limits as signals.

### Manual Quality Data (12 dashboards; median 11 panels)

- **Boundary.** Digitising what people record by hand: paper and Excel checklists, inspection
  sheets, lab result entry, calendars, records. Not automatic collection.
- **Reads.** entry fields rather than machine signals: `Acción`, `Responsable`, `Problema`,
  `Cliente` (Spanish quality and safety records), Chinese checklist fields, `Verdict`, `Article`.
  Data source `Use-Cases` 7 and `ConfigRepo` 7: the data is a **table written by a form**, not a
  signal.
- **Reading.** Standardisation here means a record schema (who, when, what, outcome), not a
  signal name. Route to `od-requirements-breakdown`.
- **Blocker themes (46 use cases).** missing scope 4; third-party system 2; hardware 1;
  platform 1; PLC access 1.

### Recipe Values (13 dashboards; median 4 panels)

- **Boundary.** Recipes, specifications, parameter sets, change tracking, transfer of set values.
  Not actual process values.
- **Reads.** tool and parameter tables (`Werkzeugname`, `Parameterwert`, `Name Merkmal`,
  `Einheit`), before/after values of parameter changes (`values_before`, `values_after`), part
  number per blow-moulding machine (`partnumber_bm01` ...). Source `QFPR - Productive` 9 of 13.
- **Reading.** The data model is a QFPR relational model, not telemetry. The `RecipeIDRunning`
  CT leaf (4 uses) is the only recipe signal on the flow side.

### Analytics (142 dashboards; median 3 panels)

- **Boundary.** Reports and analyses across machines, lines or plants; KPI reporting, Power BI,
  forecasts, models, image analysis. Not live displays of one machine.
- **Reads.** Mostly the platform itself: `datatron`, `device`, `device_type`, device class and
  make, command state, `command_steps_created_at` - these are the DTQ tool dashboards that read
  the signal registry (`ConfigRepo` 90 dashboards), plus 12 Prometheus-input dashboards.
- **Reading.** Analytics dashboards are the **signal registry's** own consumers: they are the
  evidence of what the registry holds (datatron, device, device type, data points) and of what it
  lacks (SPEC-02: no plant, no machine id, no unit, no scale).
- **Blocker themes (29 use cases).** machine list / PLC access 6; third-party system 3;
  platform 2; scope 1.

### Other Use Cases (18 dashboards; median 4 panels)

Catch-all (rule R11): platform and IT tools, AI helpers on documents, planning, device and
camera status. 73 plant use cases; blocker themes dominated by "platform or data model not
available" (10) and "missing details or scope" (9). Not a pattern - do not build a signal set
from it.

## What this file does not give

- The units, scales and collection methods of any of these signals (the data-point contract
  carries none; see Step 7 of `SKILL.md`).
- A requirement. Whether a given dashboard is *right* is a question for the use case owner.
- Anything for the 286 `unplaced` dashboards (median 9 panels, 4,966 literal predicates in 126
  of 279 joined) - these include 46 dashboards that read InfluxDB.

## Sources

`Work-OpsDigit-Knowledge/Graph/Use Case Views/` (the 11 `... - Use Case View` notes and
`template-standards.json`), `Dashboard Exports/Dashboard Notes/` (1,010 notes) and
`Dashboard Exports/specs/data/dashboard-inventory.jsonl`, all read 2026-11-05.
