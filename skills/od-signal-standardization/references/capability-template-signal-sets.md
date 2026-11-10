---
type: Skill Reference
title: Capability template signal sets
description: For each use case capability template, the kinds of signals, template variables and data sources the existing dashboards typically read, the template's boundary, the blocker themes to expect and how to look up reference solutions - to be set against the requirement sets in the signal catalogue. No counts.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, technical, signals]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Signal sets per capability template

`signal-catalogue.md` ends with the **requirement sets** the analyser checks (`--capability`).
This file is the other half: **what the dashboards that exist for each template typically
read.** Use it to ask "does my machine expose what the typical dashboard of this template
reads?" before promising a copy of an existing solution.

**How to get the live picture.** Dashboard counts, panel counts, data-source split and
literal-UUID predicates per template change with every export. Read them from the dashboard
notes (`Dashboard Exports/Dashboard Notes`), the dashboard inventory
(`specs/data/dashboard-inventory.jsonl`) and the `Use Case Views` notes (one per template), and
name the export date. Dashboards join to a template through a linked use case; a share of
dashboards is `unplaced`, and a placement by keyword is an inference in the source, not a fact.
Nothing in the "reads" lines below is a requirement - the requirement sets are in
`signal-catalogue.md` and `standards.md`.

## How to use

1. Find the template of your use case (`od-use-case-standardization`; boundary rules R1 to R13 in
   `od-analytics-asset-build/references/capability-templates-and-placement.md`).
2. Compare the "reads" line with the machine's data-point list (analyser: `--cluster`).
3. Anything the dashboards read that the machine does not expose is a gap to route (PLC or
   edge configuration) - see Step 6 of `SKILL.md`.
4. For the template's blocker themes, read the `Blocker` and comment fields of its plant use
   cases and tally the themes live. Typical themes are: machine list or PLC access, missing
   scope or details, definitions still to be agreed, platform or data model not available,
   third-party system, additional hardware, cyber-security approval, capacity.

## The templates

### Andon Board

- **Boundary.** A visual board of the current status of a line, cell, area or plant: Andon and
  Gemba boards (levels 1 to 3), production overview, card view, output against target.
  Not alerts as messages, not the stop log, not the OEE figure itself.
- **Reads (kinds of labels and variables).** machine state, part number, total parts and OK/NOK
  counts, current and last cycle time, mode (auto, manual, fault), shift, and on extrusion
  boards process temperatures and speeds. Typical template variables: data source, edge device,
  delta, PLC, part number.
- **Data sources.** Mostly the telemetry source, plus the configuration repository and a
  separate use-case table (see `od-analytics-asset-build/references/dashboard-estate-baseline.md`).
- **Binding.** Expect most dashboards to carry literal UUIDs in SQL; count the predicates live.
- **Reference solutions.** Look them up in the template's `Use Case View` note.

### OEE Calculation

- **Boundary.** OEE or its components (availability, performance, quality) per machine, line
  or plant. Not the stop events behind availability, not cycle-time analysis.
- **Reads.** OEE and its A, P, Q components, average cycle time, total parts and job parts, shift
  start and end times, product name, output, rate. Typical variables: a cycle-time setting,
  database, machine mode and its values - the **standard time is a dashboard variable** here.
- **Data sources.** The telemetry source or a time-series database for some sites, not always the
  PLC telemetry source.
- **Binding.** Many dashboards with literal UUIDs; the family is concentrated at a few plants.
- **Reading against the catalogue.** The requirement set `oee` = `MachineStatus`,
  `TotalPartCounter`, `CycleTime`, `StandardSpeed`. The dashboards read a **cycle time setting**
  as a variable and shift times as labels, i.e. the ideal cycle time and the shift pattern live
  in the dashboard. Rule from `standards.md` (ISO 22400-2): agree the ideal cycle time and the
  micro-stop threshold before choosing signals, and store them with the signal, not the panel.
- **Blocker themes.** typically missing details or scope, definitions still to be agreed.

### Cycle Time

- **Boundary.** Cycle time, takt, loading time, step or throughput time against a standard.
  Not downtime, not the OEE performance figure as a whole.
- **Reads.** cycle time, last / worst / best / average cycle time, valid cycles, load counter,
  part-produced trigger and part counter, station step times, alert UUID sets. Typical
  variables: time interval, alert UUIDs, alert message, part counter, cycle time.
- **Binding.** Nearly all with literal UUIDs.
- **Reading against the catalogue.** Requirement set `cycle-time` = `CycleStart`, `CycleEnd`.
  The dashboards compute the duration themselves from the trigger and counter; the flow
  artefact "Cycle Time" exists to publish it once.
- **Blocker themes.** often none recorded.

### Downtime Reporting

- **Boundary.** Stop events with duration and reason, operator-entered or machine-detected,
  micro-stops, uptime. Not notifications, not the availability figure.
- **Reads.** incidents, total / average / longest duration, reason, machine, severity, an
  auto-detected flag, minimum and maximum duration; local-language variants of the same labels.
  Typical variables: machine, reason, severity, minimum duration, auto-detected. **Two designs
  coexist**: a relational incident table (incidents, reasons, machines) and state-change queries
  on telemetry alone.
- **Reading against the catalogue.** Requirement set `downtime` = `MachineStatus` only.
  The dashboards also need a **reason**, which is not a machine signal: it is entered by an
  operator or classified afterwards. Say who supplies it (SPEC-02 P7: no shared schema across
  plants, proposal D-08).
- **Blocker themes.** machine list / PLC access, platform, definitions to be agreed.

### Machine Alerts

- **Boundary.** Alarms, notifications and tolerance-deviation alerts to people or shown as an
  alert list: machine faults, Teams or SMS notifications, maintenance-due triggers.
- **Reads.** alert UUID set, message, state, station OK/NOK counts, last produced part time,
  calibration OK/NOK time, last alarm text.
- **Reading against the catalogue.** Requirement set `alerting` = `ErrorActive`, `AlertMessage`.
  In the flows alerting is mostly a **code-to-message lookup**; the dashboards read the alert
  UUIDs from a variable, so the list of alert points is configuration.
- **Blocker themes.** machine list / PLC access, definitions to be agreed (the same notification
  use case at several plants shows up several times: de-duplicate when tallying), third-party
  system.

### Process Values

- **Boundary.** Live machine and process parameters (temperatures, pressures, speeds,
  counters, energy and utility readings), process overviews per machine, line or oven. Not SPC,
  not set-value management, not cross-machine analysis. Energy monitoring belongs here; the
  analysis of usage and peaks is Analytics (rule R5).
- **Reads.** setpoint and actual pairs (`Setpoint`/`Actual`, speed setpoint / actual, min / max),
  program number, zone temperatures, conveyor speed, heat-up timestamps, mass temperature,
  extruder screw / head temperature and rotation. Typical variables: data source, delta, edge
  device, a generic data-point picker, program name.
- **Binding.** The one template where variable binding (a tag picker over `data_points`) is
  already common next to literal UUIDs.
- **Blocker themes.** machine list / PLC access, additional hardware, platform, cyber-security
  approval.
- **Reading.** Setpoint and actual are two signals on every dashboard of the family; this is the
  reason the catalogue keeps `_sv` apart. A family of dashboards that differ only by the
  machine or oven id is a case for one parameterised dashboard (SPEC-04 class B).

### Process Quality Data

- **Boundary.** Automated in-process quality: inline measurement, SPC and capability, vision
  inspection, test results, scrap counting, jidoka stops, per-part traceability. Not data typed
  by hand.
- **Reads.** upper / lower intervention limits, `PV`/`SV`, recipe and recipe ID, article number,
  last data-matrix code, checklists, OK / not-OK per cell. Typical variables: machine, part
  number, a delta flag. A second source family appears: the QFPR source and a lab-data source.
- **Binding.** About half with literal UUIDs; count live.
- **Blocker themes.** platform / data model, machine list / PLC access, missing scope, hardware.
- **Reading against the catalogue.** Requirement sets `tolerance` and `traceability`. The
  quality-and-limits family is the best-named in the estate (`signal-catalogue.md`); the
  dashboards confirm it by reading limits as signals.

### Manual Quality Data

- **Boundary.** Digitising what people record by hand: paper and Excel checklists, inspection
  sheets, lab result entry, calendars, records. Not automatic collection.
- **Reads.** entry fields rather than machine signals: action, responsible person, problem,
  customer (local-language quality and safety records), checklist fields, verdict, article.
  The data source is typically the use-case table or the configuration repository: the data is
  a **table written by a form**, not a signal.
- **Reading.** Standardisation here means a record schema (who, when, what, outcome), not a
  signal name. Route to `od-requirements-breakdown`.
- **Blocker themes.** missing scope, third-party system, hardware, platform, PLC access.

### Recipe Values

- **Boundary.** Recipes, specifications, parameter sets, change tracking, transfer of set values.
  Not actual process values.
- **Reads.** tool and parameter tables (tool name, parameter value, characteristic name, unit),
  before / after values of parameter changes, part number per machine. The source is mostly the
  QFPR relational model.
- **Reading.** The data model is a QFPR relational model, not telemetry. The `RecipeIDRunning`
  CT leaf is the only recipe signal on the flow side.

### Analytics

- **Boundary.** Reports and analyses across machines, lines or plants; KPI reporting, Power BI,
  forecasts, models, image analysis. Not live displays of one machine.
- **Reads.** Mostly the platform itself: edge device, device, device type, device class and
  make, command state, command step timestamps - these are the DTQ tool dashboards that read
  the signal registry, plus some Prometheus-input dashboards.
- **Reading.** Analytics dashboards are the **signal registry's** own consumers: they are the
  evidence of what the registry holds (edge device, device, device type, data points) and of
  what it lacks (SPEC-02: no plant, no machine id, no unit, no scale).
- **Blocker themes.** machine list / PLC access, third-party system, platform, scope.

### Other Use Cases

Catch-all (rule R11): platform and IT tools, AI helpers on documents, planning, device and
camera status. Blocker themes are dominated by "platform or data model not available" and
"missing details or scope". Not a pattern - do not build a signal set from it.

## What this file does not give

- The units, scales and collection methods of any of these signals (the data-point contract
  carries none; see Step 7 of `SKILL.md`).
- A requirement. Whether a given dashboard is *right* is a question for the use case owner.
- Anything for dashboards that are `unplaced` in the source (no template): read them by hand.

## Sources

`Work-OpsDigit-Knowledge/Graph/Use Case Views/` (the template `... - Use Case View` notes and
`template-standards.json`), `Dashboard Exports/Dashboard Notes/` and
`Dashboard Exports/specs/data/dashboard-inventory.jsonl`.
