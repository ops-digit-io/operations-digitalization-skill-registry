---
type: Skill Reference
title: Library catalog
description: All 100 library use cases (proven reference solutions), grouped by capability with their real descriptions and, where recorded, the lean method behind them, so "check the library before specifying" is a menu instead of a pointer.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [use-case-support-service, library, elicited]
derived_from:
  - personal vault, Graph/Library Use Cases/*.md (100 pages), read 2026-09-17
generated: { by: claude-code/1, at: 2026-09-17T00:00:00Z }
---

# Library catalog

The Phase 3 (Assess) step "check the library before specifying" points at
`od-use-case-standardization`. This is what's actually in that library: 100 reference
solutions, each a real dashboard or app built at one plant and available as a starting
point for another. Read the closest match before drafting a new definition from scratch —
most of what a new use case needs has already been built once.

Where a `[Method]` tag appears, it's the lean/CI method the plant itself recorded behind
the solution — real vocabulary, not a classification imposed here (see § *Methods observed*
below). Twelve entries carry no capability link (`Unlinked`); check them anyway if nothing
in the matching capability group fits.

## Process Values (18)

- **Assembly_Lines_Critical_Parameters (Leak Test)** (Delicias) — Save all the critical parameters of each part that's tested on leak test probe Planned for all the assembly lines with this test
- **BM Machine Parameter Change Monitor** (Somersworth) — Monitors process parameter stability across a machine fleet by flagging any deviation from nominal settings — including ejection, die, speed, and positional parameters — with the exact timestamp of the change. Red-coded cells immediately direct supervisors to the affected machine and parameter.
- **Coating – Process Monitoring Dashboard** (Qingdao) — Monitors key coating process parameters — oven temperature, adhesive accumulator pressures, and spray times per applicator — against setpoint references over a 12-hour window.
- **Curing Oven – Temperature and Conveyor Speed Process Monitoring Dashboard** (Carei) [Visual Management] — Monitors setpoint vs. actual oven temperature and conveyor speed in real time, with min/max boundary tracking and continuous trend charts. Upheating duration, temperature achievement timestamp, and a conveyor status timeline provide full process context.
- **Curing_LAX_Oven Dashboard - Monitoring Energy** (Delicias) — Shows the current process variable of the oven; reduces time wasted with the oven turned on when it's not planned to work.
- **Extrusion Line – Availability, Line Speed and Process Parameter Dashboard** (Carei) [Visual Management] — Tracks operational status, line speed setpoint vs. actual, and extruder tooling and material configuration across a full 24-hour window, quantifying availability losses.
- **Helium Recovery Battery – Consumption and Pressure Monitoring Dashboard** (Timisoara) — Real-time helium consumption, battery pressure, bottle pressure, balloon fill level and concentration, with rolling consumption gauges supporting gas-loss minimization.
- **Helium Recovery System – Process Monitoring Dashboard** (Timisoara) — Real-time pressure, flow, temperature and helium concentration across a multi-vessel recovery system, with switchover thresholds per vessel stage.
- **Helium Test Monitoring** (Changchun) — Hourly shift yield, A/B chamber leak test data, vacuum values, helium parameters and set leak rates recorded for traceability; real-time detector data and equipment status for supervision.
- **IR Camera – Thermal Process Monitoring Dashboard** (Waltershausen) [No method reference] — Cycle-by-cycle thermal measurements across all radiance zones as a time-based heatmap, correlated with heating mirror position, welding path and joining force for root-cause analysis.
- **Machine Setup Parameter Tracking** (Changshu) — Machine parameter configuration, dashboards and digital checklists across vulcanization, injection molding, coating and assembly; dashboard auto-collects key process data from PLCs.
- **Oven – Heating and Cooling Zone Temperature Trend Dashboard** (Mako) [Visual Management] — Heating/cooling zone temperatures across a full shift window, capturing startup ramp-up and steady-state behavior for zone-to-zone consistency checks.
- **Plant Air Pressure** (Auburn) — Monitors plant and provides current Air Pressure in the plant.
- **Preheating and Cooling Unit – Zone Temperature and Cycle Monitoring Dashboard** (Mako) [Visual Management] — Heating/cooling zone temperatures against tolerance boundaries across a full shift, with per-cycle countdown charts to quantify out-of-range intervals.
- **Tempering Chamber – Process Parameter and Thermal Cycle Monitoring Dashboard** (Carei) — Real-time temperature, steam pressure and airflow for a tempering chamber, with upheating/process/cooling time breakdowns for full thermal-cycle visibility.
- **Vulcanization Autoclave – Process Quality and Parameter Monitoring Dashboard** (Waltershausen) [No method reference] — Actual vs. setpoint temperature and pressure against tolerance bands across multiple production orders, with quality-event timelines flagging out-of-tolerance intervals.

## Analytics (13)

- **Digitalized production data record** (Qingdao) — Change the paper record production data into a designed digitalized system. Recorded impact: ~5,000 sheets of paper saved yearly, 80 min/day of manual entry saved per shift leader.
- **First Part Inspection Traceability** (Changshu) — Digital checklists across vulcanization, injection molding, coating and assembly; operators archive inspection data digitally, reflected to shopfloor in real time.
- **Label Inventory Control – Leak Test Traceability Dashboard** (Monterrey) [Workplace Design] — Monitors the traceability gap between labels issued and parts validated as conforming, quantifying the delta from leak-test failures requiring SAP correction.
- **ME Shopfloor Dashboard** (Qingdao) — Real-time operating status of all braiding machines with status duration, for maintenance visibility and response speed.
- **Mold Cycle Counter Dashboard** (Somersworth) — Accumulated cycle counts per mold against tiered preventive-maintenance thresholds, color-coded by status, for prioritizing tooling interventions.
- **Multi-Line Production and Quality Dashboard** (Karben) — Real-time production/quality overview across multiple lines, OK/NOK per order/line/hour, with machine-state timelines exposing availability losses.
- **Plant Assembly Report** (Monterrey) [Gemba Management] — Hourly production of all connected machines in assembly plants, accumulated OK parts by line per day and across all machines per hour.
- **Plant data one-stop cockpit** (Qingdao) [Visual Management] — Power BI-based public data report plus a one-stop cockpit aggregating all data sources and legacy systems into one interface.
- **Press and Station Quality Monitoring Dashboard** (Karben) — Force/position distribution per press cycle alongside station-level NOK heatmaps, with histogram deviation detection for early process-shift identification.
- **Qingdao Plant Automated Machines Data Dashboard** (Qingdao) — Real-time monitoring of output performance with focus on machine status. Recorded impact: real-time transparency, ~120 min/day saved on manual PCB-board writing.
- **Quality Overview Dashboard** (Waltershausen) [Gemba Management] — Real-time OK/NOK counts across multiple assembly/pressing stations, color-coded gauges per station, with DMC traceability for the most recent unit.
- **Spraying System – Tank Level and Nozzle Throughput Monitoring Dashboard** (Carei) [Visual Management] — Real-time fill levels and throughput per nozzle against min/max limits, exposing deviations between nozzles before they cause coating defects.
- **TPOC Data digitalization** (Qingdao) [Visual Management] — Digitalized all TPOC tracking data and actions from Excel into Power BI. Recorded impact: data transparency, clear overview of TPOC targets, SPRINT savings and actions.

## Cycle Time (12)

- **Assembly Line – Cycle Time Statistics per Module Dashboard** (Dolne Vestenice) — Average/min/max/last cycle time plus a histogram per module across a multi-station line, exposing spread and outliers for bottleneck resolution.
- **Assembly_cell_monitoring** (unlinked plant) [Visual Management] — Real-time production monitoring: machine status, theoretical vs. current cycle time, parts produced per hour vs. theoretical, scrap and scrap rate.
- **Autoclave – Cycle Performance and Process Trend Comparison Dashboard** (Carei) [Visual Management] — Side-by-side view of two autoclaves across shifts, cycle times, loading times, temperature/pressure trends against control limits.
- **Autoclave – Cycle Time, Loading Time and Process Parameter Detail Dashboard** (Mako) [Gemba Management] — Per-cycle view of cycle/loading times with color-coded thresholds, correlated with temperature/pressure deviations for root-cause analysis.
- **Autoclave – Temperature, Pressure and Cycle Performance Monitoring Dashboard** (Carei) — Actual vs. setpoint temperature/pressure across a full shift, plus cycle count, last cycle time and heat-maintain time for stability analysis.
- **Automated Assembly - Production Overview** (Dolne Vestenice) — Shift-based output, takt time, OK/NOK quality across all stations; per-station cycle-time trends expose throughput deviations and bottlenecks.
- **Automatic Bending - Cycle Time Analysis** (Subotica) [Gemba Management] — Grafana dashboard for cycle-time stability/variability; scatter plot, histogram and heatmap support outlier and distribution-shift detection.
- **Injection Molding Presses – Real-Time Status and Shift Output Overview** (Dolne Vestenice) [Visual Management] — Consolidated card view of all presses — status, cycle time, temperature, shift output — color-coded for instant fleet-wide availability assessment.
- **Machine Performance Dashboard** (Waltershausen) [Gemba Management] — Machine state, cycle speed against target, hourly OK output, cumulative trend and per-cycle tracking, with state-duration breakdowns per shift.
- **Plant Production** (Auburn) — Real-time production data across multiple lines: cycle time, hourly/shift/daily production, current equipment status.
- **Rubber Vulcanization - Performance and Process Overview** (Mako) [Gemba Management] — Cycle output, cycle time and loading-time compliance across multiple autoclaves within a shift, with temperature/pressure trend charts.
- **Vulcanization Area – Autoclave Performance and Process Overview** (Mako) [Gemba Management] — Cycle count, cycle time, loading-time compliance, temperature and pressure across multiple autoclaves simultaneously within a shift.

## Downtime Reporting (10)

- **Bending Cell Area – Availability and Shift Output Overview** (Subotica) [Gemba Management] — Consolidated real-time status across all bending workplaces — feeder/bender state, per-shift output, accumulated downtime per unit.
- **Bending Cell – Availability and Hourly Output Dashboard** (Subotica) [Gemba Management] — Hourly output and cumulative availability for a bending cell, contrasting feeder vs. bending-machine running percentages to locate where losses originate.
- **Braider - Shift Downtime & Output Monitor** (Waltershausen) [Gemba Management] — Real-time overview for 6 braiding machines across 24h/3 shifts: meters produced, spool consumption, haul-off speed vs. target, downtime per shift.
- **Cover Display Board** (Sun Prairie) [Gemba Management] — Real-time run rate and quality data; also shows percent uptime for the current shift. Recorded impact: helped increase run rates ~5%; the shift supervisor now checks line speeds twice per shift against this display.
- **Efficiency in Autoclaves** (Delicias) — Downtime/uptime of autoclaves, cycles per step, average cycle time, comparison against standard loading/curing times.
- **End-of-Line Downtime Monitoring Dashboard** (Monterrey) — Registered downtime at the end-of-line station broken down by category, duration and entry frequency, Pareto-style for prioritizing loss reduction.
- **Fault Pareto and Machine State Dashboard** (Karben) — Fault categories ranked by occurrence with an 80% cumulative threshold line, plus per-machine state timelines and fault distribution by module.
- **Laser Welding Machine - Production Output Dashboard** (Timisoara) — Hourly output, cumulative production and availability, running vs. stopped time as a donut chart, mode bar exposing recurring interruption patterns.
- **Plantwide Equipment Status** (Sun Prairie) [Gemba Management] — Shows which lines are running or down. Recorded impact: gives shift supervisors line status at a glance.
- **Tubing Display Board** (Sun Prairie) [Gemba Management] — Real-time run rate and quality data; percent uptime for the current shift. Same recorded impact as Cover Display Board — ~5% run-rate increase from twice-per-shift supervisor checks.

## Andon Board (9)

- **AC Braiding Area Andon Board** (Qingdao) — Plant-floor overview of status, output, braiding speed, OEE and fault history across an entire braiding fleet, color-coded for stopped-machine detection.
- **Autoclaves Andon Board** (Delicias) — Consolidated real-time view across the autoclave fleet: cycle time, downtime accumulation, status, last loading time, average curing time.
- **BM Andon Board** (Somersworth) — Consolidated real-time view across an injection-molding fleet: cycle time, downtime, shot-weight status, purge count, alert frequency, OK/NOK flags.
- **Chang Shu _ SDS Andon Dashboard for BMW** (Changshu) [Gemba Management] — KPI overview of all machines for BMW projects (9 vulcanization, 1 injection, 1 coating, 1 assembly), auto-updated.
- **DTS BMW Andon Board** (Changshu) — Plant-floor consolidated view of availability, process temperatures and status across a full production area.
- **GEMBA Board – Shift Production Counter Dashboard** (Karben) — Hourly piece counts across three shifts over two days, color-coded quality indicators flagging fault-rate thresholds.
- **Gemba Board Transfluid** (Karben) — Shift-level quality and output in one view — OK/NOK counts, cycle time, downtime accumulation, hourly production rhythm.
- **Gemba L2** (Ostrava) [Gemba Management] — Gemba Level 2 board: daily plant performance, quality, action plan, scrap, feedback to operators and management.
- **Gemba Management Level 3** (Monterrey) [Gemba Management] — Replaced a paper/Excel L3 Gemba follow-up with inconsistent ownership and no automatic overdue-escalation; now a consolidated cross-department view.

## Process Quality Data (9)

- **Assembly-Testbenches-SPC** (Delicias) — Integration/standardization of BEV3 and CX Cell dashboards; per-day, per-machine targets compared against current production, OK/NOK, test-bench program number.
- **Extruder – Real-Time Process Parameter and Zone Temperature Dashboard** (Carei) — Rotation speed, mass pressures, vacuum levels and zone temperatures vs. setpoint, with side-by-side tooling-configuration verification.
- **Extrusion Line – Dimensional SPC Monitoring Dashboard** (Waltershausen) [Jidoka] — High-frequency dimensional measurements from two inline gauging sensors, rolling mean and control limits, exposing drift before non-conforming product accumulates.
- **Failure Analysis Dashboard** (Waltershausen) [Gemba Management] — Cross-dimensional quality failure analysis, failure types ranked by frequency per measurement category, correlated with part variants and sensor sources.
- **Leak Test Monitoring Dashboard** (Timisoara) — Leak-test pass/fail and raw sensor values per station, SPC boundary monitoring, per-station reject counts and yield summaries.
- **Pull-Off Strength – SPC Quality Monitoring Dashboard** (Waltershausen) [Jidoka] — Pull-off force SPC trend/histogram against the lower control limit, fracture-location breakdown, raw force data table for capability assessment.
- **Rubber Sheet Line – Production and Thickness Quality Dashboard** (unlinked plant) — Meters produced, line speed, utilization, production time across a multi-variant rubber sheet line; thickness measurements plotted against recipe-specific control limits.
- **SPC Dashboard Extrusion Line 3** (Delicias) — Grafana dashboard for real-time monitoring of Extrusion Line 3 process data and datapoint visualization.
- **Tube Extrusion Line Rubber – SPC Monitoring Dashboard** (Qingdao) — X-bar and R control charts for a critical rubber dimension, UCL/LCL boundaries, tooltip overlays with active-recipe context on anomaly points.

## Machine Alerts (8)

- **Alert Analysis Dashboard** (Somersworth) — Ranks active alert types by frequency for a specific machine (Pareto/donut charts), time-interval breakdown per occurrence.
- **Chain Oven – Multi-Zone Temperature and Energy Monitoring Dashboard** (Mako) [Visual Management] — Cooling/heating zone temperatures across all zones with tolerance boundaries and a dedicated alert chart; power consumption trended in parallel.
- **Cover Extrusion Line – Process Monitoring Dashboard** (Qingdao) — Setpoint vs. actual temperatures, vacuum pressure, output dimensions, line speed and utilization; alarm log records deviations with timestamps.
- **Drying Hopper Dashboard** (Somersworth) — Real-time status of drying hoppers — material level, operational state, set vs. actual temperature, alarm conditions — with low-fill warnings.
- **GSM_sms_alarm_monitoring** (Ostrava) [Total Productive Maintenance] — Watchdog for a PLC value out of limit; automatic SMS generated to responsible persons. Recorded impact: fast reaction loop for process defects.
- **Hopper Status Overview Dashboard** (Somersworth) — Drying hopper fleet status in real time across all units, with low-fill warnings and set-vs-actual temperature comparison.
- **MS Teams Notifications in Vulcanization** (Delicias) — Node-RED alarming layer on Delicias vulcanization equipment, pushing Teams notifications with escalation for two named alarms (LAX oven energy leak, autoclave cycle interruption). See [`worked-examples.md`](worked-examples.md) — this is the same use case as `Alarms Notifications`.
- **Spray Booth Safety Door Alert Dashboard** (Qingdao) — Alarm frequency/distribution for a specific safety-door event over 24h, error-code breakdown, timestamped occurrence log.

## OEE Calculation (8)

- **Automated Machines OEE Dashboard** (Changchun) — Real-time OEE-A, OEE-Q and hourly throughput plus machine status/cycle time, covering coupled equipment and NW automated machines.
- **Availability for Machines** (Qingdao) — Real-time OEE breakdown (availability/performance/combined) per machine, state-duration analysis, timestamped event log for full status-transition traceability.
- **Blowout Display Board** (Sun Prairie) [Gemba Management] — Real-time OEE data (Blowout line). Recorded impact: no direct cost savings, but supported OEE improvement over several years and helped sustain it — shift supervisors check OEE four times per shift.
- **Chang Shu _ SDS Vulcanization Dashboard** (Changshu) [Gemba Management] — Dashboard for vulcanization KPIs (OEE, cycle time, output/mold count). Recorded impact: daily monitoring.
- **Cover Extrusion Line – OEE and Production Dashboard** (Qingdao) — Shift-level OEE/output for an extrusion line, state timeline, availability gauge, idle-event counter (>15 min stops).
- **Inspection Line – OEE and Production Dashboard** (Changshu) — OEE availability and throughput with high-granularity state timeline across running/idle/changeover/maintenance states.
- **Mandrel Prep OEE Board** (Sun Prairie) [Gemba Management] — Real-time OEE for the Mandrel Prep department: running/down state, line speeds, product being run.
- **Production and OEE Dashboard** (Changshu) — 24-hour output and shift-level OEE availability for a cyclic machine, state timelines distinguishing running/setup/stop.

## Manual Quality Data (1)

- **Quality-Gauge_Management** (Monterrey) [No method reference] — Mendix app letting metrology/quality staff track each gauge's location and status (in-house/workshop/shop floor) via check-in/check-out, photo evidence and a return questionnaire — replacing paper tracking.

## Unlinked — no capability recorded (12)

- **6S Audits** (Sun Prairie) [5S] — Standards and documentation for 6S. Recorded procedure: a Microsoft Forms check against the 6S standard, per area. Recorded impact: helped improve 6S in the plant.
- **Automatic Press Centers Monitoring** (Subotica) — Structured monitoring of automatic press-center performance: machine status, production context, output tracking, correlated with production events and interruptions.
- **Department Weekly Attainment** (Auburn) — Real-time percentage of attainment against the departmental weekly target.
- **Excel VBA Macros implemented** (Qingdao) — Manual data operations replaced by VBA macros, one-button execution of repetitive tasks.
- **Hourly Output - OK and NOK parts** (Mako) [Gemba Management] — Actual hourly output per part variant over a 48-hour window, exposing variability and zero-production gaps.
- **LDC Monthly FC tools develop** (Qingdao) — Two rapid LDC estimators (C#/VBA) running core FC logic, with access-controlled fast forecast snapshots.
- **Logistics-OCR_Invoice_Agent** (unlinked plant) — Power Automate Cloud flow using OCR to extract charge-level cost data from logistics PDF invoices into SharePoint Excel; MVP ~10 invoices/month at $0 licensing.
- **OESL Manufacturing Image Browser** (Monterrey) [No method reference] — Interface to consult auto-backed-up images from TESLA SD/PP lines.
- **Production Assembly Cell – PCB Board** (Mako) [Gemba Management] — Shift-level hourly output vs. target per part variant, color-coded, zero-output intervals exposed within the shift timeline.
- **Production Attainment** (Auburn) — Real-time status of actual output against target.
- **Production Panel for Assembly Lines** (Monterrey) [Gemba Management] — Hour-by-hour output against daily target, color-coded bars flagging shortfall hours.
- **Vulcanisation profile** (Ostrava) [Visual Management] — Vulcanisation profile, PLC data. Recorded impact: product quality.

## Methods observed

Only 45 of 100 entries carry a method tag; the rest are unrecorded, not method-free. What's
actually tagged:

| Method | Count |
|---|--:|
| Gemba Management | 23 |
| Visual Management | 13 |
| No method reference (explicitly tagged as such) | 4 |
| Jidoka | 2 |
| 5S | 1 |
| Total Productive Maintenance | 1 |
| Workplace Design | 1 |

This is the department's own lean vocabulary, not one imposed here — use it when a use
case's method genuinely matches one of these, and leave the field blank rather than force
a tag onto a use case that doesn't fit any of them.
