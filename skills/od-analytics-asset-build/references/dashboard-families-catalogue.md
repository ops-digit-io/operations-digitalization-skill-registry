---
type: Skill Reference
title: Dashboard families catalogue
description: The 74 dashboard families of the screenshot inventory and the 17 cross-plant dashboard titles of the JSON export, with the class that says whether a family can be shared, and fourteen family cards listing what each shows, the signals it needs and the traps seen.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [analytical-support-service, practice, dashboard]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Dashboard families catalogue

**Before building a dashboard, find its family here.** A family is "the same thing shown for
different lines, machines, plants or versions". If one exists at another plant, adopt it
(`od-use-case-standardization`, and `SKILL.md` "When not to build").

**Two inventories, two counting bases - do not add them.**

| Inventory | What it counts | Basis |
|---|---|---|
| Screenshot inventory (Graph/Use Cases, "Dashboard Use Case" notes) | 481 dashboards in **74 families**; 149 inspected one by one, the rest assumed to follow the template of an inspected sibling | 19 capture runs 2026-02-04 to 2026-02-12; `dev` folder excluded; plants often *inferred* from folder names |
| JSON export (Dashboard Exports) | 1,010 unique dashboards; families by normalised title (578 keys) | exports of 2026-10-29 to 2026-11-03 |

Only 399 of 481 inventory titles are found in the export and 472 of the 1,010 exported
dashboards have no inventory title (title matching only). The family notes therefore describe
about half the estate. Everything in the cards is "AI-drafted from screenshots, not reviewed by
a human" in the source; a capture is a snapshot and panels that read "No data" show layout only.

## 1. Which families can be shared - the cross-plant titles (count, JSON export)

Dashboards are grouped by title (lower case, digits and punctuation removed). Two copies are
**query-identical** when the multiset of their queries is equal after masking UUID literals: that
says the data logic is the same, not the layout. Of 1,010: **748 dashboards (74%) have a family in one plant only,
34 in two plants, 228 in three or more (17 families).**

| Family (title) | Plants | Dashboards | Distinct query sets | Largest identical group | Class |
|---|--:|--:|--:|--:|---|
| DTQ - Datatron and Device Metadata | 18 | 18 | 1 | 18 | A |
| DTQ - Device Type and Datapoint Schema Specification | 18 | 18 | 1 | 18 | A |
| DTQ - Database Tables and Fields | 18 | 18 | 1 | 18 | A |
| DTQ - Count Datapoints by UUID, label in last n minutes | 17 | 17 | 1 | 17 | A |
| OESL - Location Organization and Asset Structure | 16 | 16 | 1 | 16 | A |
| DTQ - Monitoring Config Repo | 13 | 13 | 1 | 13 | A |
| uuid search | 3 | 3 | 1 | 3 | A |
| DTQ - Device Tag and UUID Overview | 18 | 18 | 4 | 15 | A, 3 variants to review |
| DTQ - Device Journal Overview | 16 | 16 | 2 | 9 | A, 1 variant to review |
| Processes All - Process Value Overview Numeric | 17 | 17 | 3 | 14 | B |
| Processes All - Process Value Overview Strings | 17 | 17 | 3 | 12 | B |
| Home | 19 | 20 | 7 | 13 | B |
| Operations Dashboard | 9 | 9 | 8 | 2 | C |
| Alert Dashboard | 6 | 6 | 5 | 2 | C |
| Andon Board | 6 | 6 | 6 | 1 | C |
| Extrusion Line | 3 | 6 | 6 | 1 | C |
| Extrusion | 3 | 10 | 10 | 1 | C |

- **A - central tool.** Same data logic everywhere; maintain once and deploy to all (proposal F-01).
- **B - template with parameters.** Mostly the same; understand the differences, then make them variables (F-03).
- **C - same name, different content.** A name does not mean a shared design: Andon Board exists in 6
  plants with 6 different query sets. Write one reference design per name (F-04).
- **D - plant-specific.** The 748; classify each into one of the 11 templates (F-05).

Classes and F- numbers are the proposals of SPEC-04 (draft for review), not decisions. The pilot
plants for class C are a decision for the owner (SPEC-04 Q2).

**Migration cost sits in few dashboards.** Half of the 16,452 literal-UUID predicates are in 73
dashboards (7%). The ten heaviest: Karben "DEV Zentralrechner-RFID" 811, Northeim "VIM -
Maschinen Übersicht (absolute Werte)" 280, Waltershausen "SPC Values - Extrusion Lines
Process" 205, Vac "Extrusion - Smooth Line" 188, Karben "Stations - Times HDES" 186, Dolne Vestenice
"Maplan 1K Injection Molding - Level 1 - Card View" 173, Karben "Stations - Times HDEP" 160,
Northeim "VIM - Maschinen Übersicht (Detail)" 160, Timisoara "Insula 14 - Time Study" 149,
Waltershausen "KraussMaffei ... Prozess & Produktion" 145 - together 2,457 predicates (15%).

## 2. The 74 screenshot-inventory families

Dashboards counted as "n (inspected)". Template is the one recorded on the family note. Language
is the language printed on the dashboards (not translated). Plants named are those printed or
inferred in the source note ("not identified" = no plant name on the dashboards).

Template counts over the 74 families: Process Values 21, Andon Board 17, Process Quality Data 11,
OEE Calculation 7, Cycle Time 5, Analytics 4, Machine Alerts 4, Downtime Reporting 2, Manual
Quality Data 1, Recipe Values 1, Other Use Cases 1. Language counts over families (a family may
have two): English 46, German 20, Chinese 16, Spanish 11, Romanian 4, Hungarian 1.

### Andon boards and Gemba displays (15 families)

| Family | Dashboards (inspected) | Plants named | Language | Template |
|---|--:|---|---|---|
| Extrusion Line Andon Board Set (Halls 1-3) | 41 (1) | Carei | English / German | Andon Board |
| Machine Status Timeline | 30 (1) | not identified | Chinese / English | OEE Calculation |
| AC Braiding Area OEE and Status Dashboard | 8 (2) | Qingdao | Chinese | Andon Board |
| Injection Molding Level 1 and Level 2 Dashboards | 8 (2) | not identified | English | Andon Board |
| Bending Cell Dashboards | 7 (2) | not identified | English | Andon Board |
| QFPR+ Shopfloor Boards (Chinese) | 7 (2) | Qingdao | Chinese | Andon Board |
| AC Braiding Area Andon Board | 5 (3) | Qingdao | Chinese / English | Andon Board |
| Desma Vulcanization Andon Board | 4 (1) | not identified | Chinese | Andon Board |
| Halle 4 Gemba Board (HDEP - HDES and Coolant Jacket) | 4 (1) | Karben | German | Andon Board |
| Plant Andon Board (Production Overview) | 4 (4) | Karben, Subotica, Timisoara | English / German | Andon Board |
| AC Line Status Widget (Chinese) | 2 (1) | not identified | Chinese | Andon Board |
| Autoclaves Andon Board | 2 (1) | not identified | Spanish | Andon Board |
| BBM Andon Board | 2 (1) | not identified | English | Andon Board |
| Extrusion Lines Andon Board | 1 (1) | Carei | English | Andon Board |
| Injection Molding Machine Status Overview | 1 (1) | DolneVestenice | English | OEE Calculation |

### Process-value monitoring (equipment and process parameters) (19 families)

| Family | Dashboards (inspected) | Plants named | Language | Template |
|---|--:|---|---|---|
| Silicone Curing Oven Monitoring | 19 (1) | Carei | English | Process Values |
| Vulcanization Parameter Monitoring | 14 (2) | not identified | Chinese / Spanish | Process Values |
| Autoclave Shopfloor and Process Values | 11 (3) | Carei | English / German | Process Values |
| Autoclave Process Monitoring | 9 (2) | not identified | Spanish / English | Process Values |
| Extrusion Line Process Values and Output | 9 (2) | not identified | English | Process Values |
| Halle 4 HDEP - HDES Station Monitoring | 9 (3) | Karben | German | Process Values |
| Helium Recovery Units Monitoring | 9 (2) | Timisoara | English / Romanian | Process Values |
| Thermoforming Process Monitoring | 9 (3) | Mako | English | Process Values |
| AC Extrusion Line Process Monitoring (Tube and Cover) | 8 (2) | Qingdao | Chinese / English | Process Values |
| Extrusion Line Process Values (Halls 1-3) | 8 (1) | Carei | English / German | Process Values |
| Bending, Forming, Rolling and Welding Line Dashboards | 7 (3) | not identified | English | Andon Board |
| Halle 4 Coolant Jacket Process Overview and Values | 7 (3) | Karben | German | Process Values |
| Plastics Material Conveying and Drying | 6 (3) | not identified | English | Process Values |
| Injection Molding Machine Monitoring | 4 (2) | not identified | German | Cycle Time |
| Mandrel Blow-Out Monitoring | 4 (1) | not identified | Chinese | Process Values |
| Process Value Overview and Actual vs Set Values | 2 (2) | Qingdao | English | Process Values |
| Tempering Process Monitoring | 2 (1) | Carei | English | Process Values |
| Curing LAX Oven Monitoring | 1 (1) | Delicias | English / Spanish | Process Values |
| Infrastructure Measurement Points | 1 (1) | Mako | English | Analytics |

### Quality, SPC and traceability (15 families)

| Family | Dashboards (inspected) | Plants named | Language | Template |
|---|--:|---|---|---|
| QFPR Feedback Dashboards (Scrap, SPC, Capability) | 10 (2) | not identified | German | Process Quality Data |
| QFPR Definition Dashboards (Checklists, Parameters, Tools) | 9 (2) | not identified | German | Recipe Values |
| AC Extrusion Line SPC (X-bar and R Charts) | 8 (2) | Qingdao | Chinese / English | Process Quality Data |
| Assembly Cell and Lab Pull-Test Dashboards | 8 (4) | not identified | German | Process Quality Data |
| Paperless Quality and Safety Records | 8 (3) | not identified | Spanish | Manual Quality Data |
| Blow Molding Process Changes, Scrap and Shot Weight | 5 (3) | not identified | English | Process Quality Data |
| TPV Extrusion Process and Quality | 5 (2) | not identified | German / English | Process Quality Data |
| BMW FAAR Assembly Cell Dashboards | 4 (3) | not identified | English | Andon Board |
| KL34 Assembly Monitoring (BMW) | 4 (3) | not identified | English | Cycle Time |
| Crimping Cell Dashboards | 3 (2) | not identified | English | Process Quality Data |
| Extrusion SPC Values | 3 (1) | not identified | German | Process Quality Data |
| Helium Leak Test Traceability | 3 (3) | Timisoara | English / Romanian / Spanish | Process Values |
| Industrial Process Engineering Analysis (AIS) | 3 (2) | not identified | German / English | Process Values |
| Mercedes G-Class BR465 Crimping Cell | 2 (2) | not identified | English / Hungarian | Andon Board |
| Quality Lab Moisture Testing | 1 (1) | not identified | German | Process Quality Data |

### OEE, availability, downtime and alerts (12 families)

| Family | Dashboards (inspected) | Plants named | Language | Template |
|---|--:|---|---|---|
| Vulcanizer OEE Dashboard | 9 (1) | not identified | Chinese | OEE Calculation |
| Plant Alert Dashboard | 8 (2) | Karben, Subotica, Timisoara | English | Machine Alerts |
| Operations Dashboard | 7 (2) | Timisoara, Subotica, Carei, Mako | English / Romanian | Cycle Time |
| Coating Machine OEE and Parameter Tracking | 6 (2) | not identified | Chinese | Process Values |
| Blow Molding Monitoring and Downtime | 5 (1) | not identified | English | Downtime Reporting |
| Downtime Dashboard | 5 (2) | not identified | Spanish / English | Downtime Reporting |
| Maintenance and Predictive Maintenance | 4 (3) | not identified | English | Machine Alerts |
| Availability per Machine | 3 (1) | Qingdao | English | OEE Calculation |
| Productive Time Overview | 3 (2) | Subotica, Timisoara | English | OEE Calculation |
| All Machine OEE-A Dashboard | 2 (1) | not identified | English | OEE Calculation |
| Machine Alert Dashboard | 2 (1) | Qingdao | Chinese | Machine Alerts |
| Injection Molding OEE and Parameter Dashboard | 1 (1) | not identified | Chinese | OEE Calculation |

### Platform, portals and housekeeping (8 families)

| Family | Dashboards (inspected) | Plants named | Language | Template |
|---|--:|---|---|---|
| Plant Portal and Navigation Dashboards | 18 (5) | not identified | English / Romanian / Chinese | Analytics |
| Sandbox and Test Dashboards | 17 (9) | not identified | Chinese / English | Other Use Cases |
| DTQ and Asset Structure Tool Dashboards | 8 (2) | not identified | English | Analytics |
| WIP, Deprecated and Testing Dashboards | 6 (1) | not identified | German | Process Values |
| Process Value Overview (Tools) | 4 (1) | not identified | English | Process Values |
| Edge Device and Camera Status | 3 (3) | Karben | English / German | Machine Alerts |
| BBM11 Inline Measurement (Deprecated) | 2 (1) | not identified | German | Process Quality Data |
| Superseded Halle 4 Drafts | 2 (1) | Karben | German | Cycle Time |

### Production output, cycle time and reporting (5 families)

| Family | Dashboards (inspected) | Plants named | Language | Template |
|---|--:|---|---|---|
| Hourly Production per Line | 10 (2) | not identified | Spanish | Andon Board |
| Daily and Weekly Production Reports | 5 (2) | not identified | German | Analytics |
| Test Bench Hourly Output and Database | 4 (2) | not identified | Spanish | Process Quality Data |
| Cycle Time and Cycle Counter Analysis | 3 (2) | not identified | English / Spanish | Cycle Time |
| Tesla Pentaport Hourly Output and Traceability | 3 (2) | not identified | Spanish | Process Quality Data |

## 3. Family cards - what each needs

Each card is a **reading of what the captured dashboards display**; "signals needed" are the
quantities shown, to be matched against `od-signal-standardization` names, not a requirement
written by a plant. Query patterns Q1 to Q9 are defined in
[`dashboard-json-sample-2026-11.md`](dashboard-json-sample-2026-11.md); "not inspected" means no
query of this family was opened.

### 3.1 Plant Andon Board (Production Overview) - class C, Andon Board
- **Shows.** A machine table per plant: state, program or part number, current and average cycle
  time, part counts (total, OK, NOK, planned), alerts, time of last part. Variants: Karben (BMW
  lean cell, coolant jacket, HDEP/HDES modules), Subotica (bending and forming), Timisoara (helium
  leak test, KUKA cell, crimping, laser welding), and a rubber board (autoclaves, extrusion lines,
  mandrel preparation, EBA 1 to 4 with target and actual metres, SAP number, product name).
- **Signals needed.** machine state, part number, cycle time, total/OK/NOK counters, alert count,
  last-part timestamp, operating mode (Automatic/Manual), shift totals.
- **Query pattern.** Q1 per tile and Q2 for trends; one UUID per tile (the Carei extrusion board
  sampled has 97 panels and 52 literal UUIDs).
- **Trap.** Every plant fills the same layout with its own machines: six plants, six query sets.
  Recipe cells read "bitte Rezept holen" - a recipe text the dashboard cannot fetch.

### 3.2 Operations Dashboard and Alert Dashboard - class C, Cycle Time / Machine Alerts
- **Shows.** Operations: a machine or station drill-down with part number, OK and NOK parts per
  interval, average cycle time, alert counts, an OK-versus-NOK bar history (a 15-minute table of
  ok/nok/total counter, average cycle time, average waiting time); the Subotica shopfloor variant
  is parts per machine and running versus not running. Alert: for one machine, the alert counter
  per reason (safety gates, bowl empty, accumulator overfilled, robot errors, laser data-matrix
  quality) as bar and donut, a table and a time-ordered log.
- **Signals needed.** part counter OK/NOK, cycle time, waiting time, machine running flag, alert
  code or text per event (a code-to-message lookup, as in the 32 "Alerting" flows).
- **Trap.** The Subotica shopfloor variant: all four panels "No data" with error markers in the
  capture; the Operations family sits at 9 plants with 8 different query sets.

### 3.3 Machine status timeline and OEE-A - Qingdao AC lines, Chinese vulcanizers
- **Shows.** A coloured status bar over 24 h (Running, Idle, Changeover, Replace Plate,
  Equipment), a state-share pie, an OEE A gauge, day/night plan versus actual, hourly output bars
  (30 dashboards for 10 lines, each in a current and a "New" version). Vulcanizer boards V103 to
  V118: product spec, latest takt (1,067 s in one capture), mould number, state timeline (setup
  or mould change, stopped, running), shift OEE-A gauges, cumulative output.
- **Signals needed.** machine status (string), production counter per shift, shift plan, start and
  end, standard time or takt.
- **Query pattern.** Q1 (string status, `LIMIT 1`) plus state-change durations; the OEE
  dashboards read a `CycleTimeSetting` variable (24 dashboards).
- **Traps.** Implausible values in captures (a tile at 1.7e38, an OEE-A of -13%); identical OEE
  figures (A 80.7%, Q 98.5%, P 0.0%) across unrelated dashboards, which points to a shared or
  templated source (Dashboard Use Cases - Overview, data-quality findings).

### 3.4 Extrusion line Andon set (Carei, Halls 1-3) - Andon Board, 41 dashboards
- **Shows.** For each of 8 lines, 5-6 boards: line data, inner-layer extruder, knitting machine,
  upper-layer extruder, cutting machine (line 1 also spraying). Tiles: status, line speed set and
  actual, mandrel/die/vacuum-nozzle preset versus actual, mix and lot number, extruder rotation,
  motor current, mass pressure and temperature, vacuum, a zone-temperature table (screw, feed
  roller, cylinders 1-3, head: set, min, actual, max, out-of-limit flags).
- **Signals needed.** per extruder zone: set value, actual, tolerance; line speed; preset versus
  actual tooling; material identifiers.
- **Trap.** Cutting machines "still have to be connected to provide metres and pieces"; line 4 is
  a template with a banner asking for the correct data points; several lines are marked (TODO).
  A copy-by-line family: the cost of changing one UUID is multiplied by 41.

### 3.5 Injection moulding Level 1 / 2 / 3 (Dolne Vestenice) - three tiers
- **Shows.** Level 1 card view per press (state Automatic/Setup/Stop/Manual, part number, mould,
  material, parts per shift current/previous, last cycle time); Level 2 production overview
  (state tile, workplace, part, cavities, cycle-speed gauge, state durations per shift 06-14 /
  14-22 / 22-06, hourly output, cycle-time statistics); Level 3 process values. Desma 2K
  (presses 351-361) and Maplan 1K (001-007).
- **Signals needed.** machine state, order number, material number, mould number, part number,
  production quantity, cycle time, injection-unit times (plastification, injection, dwell
  pressure) for both units, real cure time, part counter, injection counter - exactly the
  template variables of the Level 2 dashboard.
- **Why it matters.** The only family built as three linked levels of the same signals (compare
  SPEC-03 S-05: split above 40 panels). The Level 1 card view for Maplan is among the ten
  dashboards with the most literal UUIDs (173).

### 3.6 Hour-by-hour boards (Gemba board, hourly production per line) - Andon Board
- **Shows.** Halle 4 Gemba board (Karben): for yesterday and today, per shift (early, late, night)
  and hour 1-8, good parts coloured against target next to a fault-type pie; daily counter 06:00 to
  06:00; fault colour key (1 fault yellow, 2-3 orange, 4 or more red). Monterrey hourly
  production: a grid of line by hour coloured by scanned-OK pieces against an hourly target (green
  at or above 100%, yellow 80-99%, light red below 80%), one dashboard per line (nine variants in a
  `Playlists` folder), an hourly target per line (for example 80, 120, 125, 130).
- **Signals needed.** part counter OK/NOK, order and part number, hourly target (configuration,
  not a signal), shift boundaries, fault type.
- **Query pattern.** Q8 (shift windows in SQL) and Q9 (localised date text).
- **Trap.** The hourly target and the shift pattern live in the dashboard; a changed shift breaks
  every variant. Time filters are explained on the dashboard itself ("now-5min = today's board").

### 3.7 Autoclave boards (Carei, Delicias, Mako) - Process Values / Andon Board
- **Shows.** Shopfloor: running mode, heat-maintain time, cycles this shift, last cycle time (red
  above target), program number, set versus actual temperature and pressure, trends with limit
  lines. Process-value boards: temperature, condensate temperature, pressure per cycle, cycle and
  loading time, number of cycles. Delicias Andon: running or standby, cycles per shift, load times,
  active recipe, downtime in shift and day, active and inactive autoclave rows.
- **Signals needed.** mode, program number, temperature, pressure, condensate temperature, cycle
  counter, cycle start/end, load counter.
- **Trap.** One autoclave returned "No data" in a capture while its neighbours worked: check the
  machine before the dashboard.

### 3.8 Curing ovens (Carei: 19 per-oven dashboards; Delicias LAX) - Process Values
- **Shows.** Oven state, running program, temperature set point, actual and min/max corridor,
  conveyor speed set versus actual, heat-up timing (start, target reached, period, starting
  temperature). Delicias adds an energy strip (minutes on, hours on, energy in MWh, cost).
- **Signals needed.** program name or number, zone actual temperature, set point, min/max,
  conveyor speed set and actual, up-heat start and achieved timestamps - the same list as the
  template variables of the Carei oven dashboards (`program_name`,
  `heating_temperature_zone1_act`, `conveyer_speed_setpoint`, `upheat_time_hour`).
- **Design note.** 19 dashboards differing by oven id, 5 marked "(old)", plus a "Curing Oven
  Dynamic" dashboard that picks the oven by variable: the dynamic one is the pattern to keep
  (variable binding); the 19 are the cost it was meant to remove.

### 3.9 Downtime (Delicias, Mako, Somersworth, Subotica) - Downtime Reporting
- **Shows.** Delicias: accumulated downtime split into operator-selected categories (line idle,
  machine failure, staff out of cell, meal, missing staff/material/components, model change, 5S
  activities, briefing, non-conforming material, safety incident, plant evacuation) as pie, bar
  and heat strip; an autoclave board with recipe, average cycle, real cycles, downtime hours,
  efficiency and a floor-comment table filterable by shift, user, severity and tag. Mako: KPIs
  (total downtime, incident count, MTTR, MTBF, P95 duration, unassigned %, auto-detected %),
  Pareto by machine stacked by reason, machine and reason ranking, state timeline, day-of-week by
  hour heat map, duration histogram, incident table (top 500). Variables: machine, reason,
  severity, min and max duration, auto-detected.
- **Signals needed.** machine state (for detection) **and** an operator-entered reason, severity,
  comment and user - the second half is a record, not a signal.
- **Trap.** Two designs at two plants: Mako's relational incident tables and Delicias' category
  entry. SPEC-02 proposes one downtime schema (D-08) based on Mako's; that is a proposal.

### 3.10 Machine alerts and maintenance counters
See 3.2 for the alert dashboard. Qingdao's alarm analysis (last alarm text, count in period, pie
of alarm types, latest occurrence per type, full log, count time series, in Chinese) and the
Somersworth maintenance counters (a part-number by cycle-interval grid with red/yellow/green at
5,000 / 10,000 / 20,000 / 60,000 / 240,000 cycles; mould counter tables with reset history) are
the two other forms. Signals: alarm code or text with timestamp, cycle or part counter per tool.
In the source, "Industrial Notifications MS Teams" is one use case at three plants with
blockers on definitions, machine list and third-party system.

### 3.11 SPC and process quality - Process Quality Data
- **Shows.** Qingdao AC extrusion SPC (X-bar chart with UCL/LCL and range chart, orange markers
  for product or recipe changes, tooltip naming the recipe); Waltershausen extrusion SPC
  (operating-order timeline and trends of mandrel outer diameter, film wall thickness and film
  outer diameter against process value, set value, tolerance and intervention limits); TPV line
  failure analysis (tolerance-band violations per measuring device and part number) and
  layer-adhesion pull-off SPC.
- **Signals needed.** process value, set value, upper/lower tolerance, upper/lower intervention
  limit, recipe id, order number - the quality-and-limits family of the catalogue (`CurrentValue`,
  `Hard/SoftUpper/LowerLimit`, `LimitValue`).
- **Trap.** The Waltershausen SPC dashboard binds 205 literal UUIDs (third heaviest in the
  estate); Karben's "Stations - Times" boards bind 160 to 186 each.

### 3.12 Helium leak test and helium recovery (Timisoara, Monterrey)
- **Shows.** Per test station: chambers, cycle time (min, average, max), booster pump, mechanical
  pump, helium burp, helium recovery, pieces tested per hour, final-evacuation pressure per part
  excluding negative values. Recovery units: vessel pressures against start/stop thresholds,
  mixing station, helium and air flow, pressure, temperature; a portal page with helium
  consumption per shift (Romanian labels).
- **Signals needed.** per chamber: pressure phases, cycle time, accept and reject totals
  (`TotalAccepts`, `TotalRejects`, cumulative OK/NOK and hourly increment), pump states.
- **Trap.** "Excluding negative values" and "excluding values less than 10" appear in panel
  titles: the filtering of bad values is done in the panel, not in the signal.

### 3.13 Energy and utilities (Mako, Carei, Delicias, thermoforming)
- **Shows.** Mako infrastructure: kW per hour as bars with a trend and the total for two
  electrical measurement points and one gas point (m3), from a metering vendor's data.
  Thermoforming ovens: zone temperatures with tolerance lines (chain oven: 12 heating zones about
  160 C, tolerance 155 to 165 C) and average power in kW. Carei: extrusion line 7 and 8
  energy-management dashboards created 2026-10-12 and a chain-oven energy dashboard created
  2026-08-20 (change reports).
- **Signals needed.** energy (kW, kWh, m3) per measurement point, plus the production counter for
  normalisation (placement rule R5: monitoring is Process Values, usage analysis is Analytics).
- **Open.** The only verified external benefit basis for energy is the sub-metering source
  recorded in the Case Groups overview (R33); see `od-benefit-calculation`.

### 3.14 Platform tools and portals - classes A and B
- **Shows.** DTQ tools (class A, 9 titles at 13 to 18 plants): device journal with the command
  state ladder (01 created, 02 sent, 03 acknowledged, 04 processing, 05 received, 07 processed,
  08 done), device-type and datapoint schema specification, count of data points by UUID and label
  in the last n minutes, config-repo monitoring, tag and UUID overview. Process Value Overview
  (class B, 17 plants): numeric, string, Beckhoff and byte-array variants that plot one selected
  tag so engineers can check that a signal arrives. Plant portal: a department start screen
  (Production, Maintenance, Quality, Process, ESH, Automation, Lean) with link tiles.
- **Use.** The cheapest diagnostic at a plant: `DTQ - Count Datapoints by UUID, label in last n
  minutes` and the Process Value Overview answer "is the signal arriving?" before any flow is
  opened (see `od-node-red-flow-troubleshooting`).
- **Trap.** `Home` exists at 19 locations in 7 query sets; the Device Tag and UUID overview has 4.

## 4. Gaps in the catalogue

- 286 of 1,010 dashboard notes have no template placed and 338 have no use case found; a family
  is therefore not proof that a use case exists (link coverage: 76 high, 142 medium, 71 low, 383
  template-level pointers, 338 none).
- Captures with little or no live data (layout only): QFPR definition and feedback boards, Quality
  Lab Moisture Testing, BBM11 inline measurement, injection moulding machine monitoring, test
  bench and Tesla Pentaport boards, paperless quality, autoclave process monitoring, extrusion
  process values and output, Operations Dashboard, Mercedes crimping cell, AIS analysis, sandbox.
  Re-capture before relying on them.
- The captures date from 2026-02-04 to 2026-02-12, about nine months before the JSON export;
  folders and titles may have moved.
