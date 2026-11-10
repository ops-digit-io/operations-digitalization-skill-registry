---
type: Skill Reference
title: Dashboard families catalogue
description: How to find a dashboard family before building, the four sharing classes (central tool, parameterised template, same name different content, plant-specific), the family groups, and fourteen qualitative family cards listing what each shows, the signals it needs and the traps seen. Guidance only - no counts, plant tables or per-dashboard figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [analytical-support-service, practice, dashboard]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Dashboard families catalogue

**Before building a dashboard, find its family.** A family is "the same thing shown for different
lines, machines, plants or versions". If one exists at another plant, adopt it
(`od-use-case-standardization`, and `SKILL.md` "When not to build").

This file holds no figures. The live list of families, titles, plants and counts is in the work
vault (`Graph/Use Cases`, the "Dashboard Use Case" family notes, and the JSON export under
`Dashboard Exports`). Re-count there and quote a number only with its source and date.

## 1. Where to look, and the two counting bases

| Inventory | What it is | Caveats |
|---|---|---|
| Screenshot inventory (`Graph/Use Cases`, "Dashboard Use Case" notes) | Dashboards grouped into families from screenshots; some inspected one by one, the rest assumed to follow the template of an inspected sibling | A capture is a snapshot; plants are often *inferred* from folder names; panels reading "No data" show layout only; `dev` folder excluded |
| JSON export (`Dashboard Exports`) | Every unique dashboard (location, uid) from the newest run; families by normalised title | Newer than the screenshots; folders and titles may have moved |

Title matching between the two is partial: the family notes describe only part of the estate, so
**absence of a family note is not proof that no family exists.** Everything in the cards below is
"AI-drafted from screenshots, not reviewed by a human" in the source.

## 2. Which families can be shared - the sharing classes

Dashboards are grouped by title (lower case, digits and punctuation removed). Two copies are
**query-identical** when the multiset of their queries is equal after masking UUID literals: that
says the data logic is the same, not the layout. Most dashboard titles exist in one plant only; a
smaller set of titles recurs across several plants. Re-compute with the inventory (group by
normalised title, count plants, count distinct query sets).

| Class | Meaning | What to do | Typical examples (by kind) |
|---|---|---|---|
| **A - central tool** | Same data logic everywhere | Maintain once and deploy to all (proposal F-01) | The `DTQ - ...` platform tools (device and datatron metadata, device-type schema, database tables, count of data points by UUID, config-repo monitoring, tag and UUID overview), the asset-structure tool, the UUID search |
| **B - template with parameters** | Mostly the same; variants differ | Understand the differences, then make them variables (F-03) | Process Value Overview (numeric, strings), `Home` |
| **C - same name, different content** | A name does not mean a shared design | Write one reference design per name (F-04) | Andon Board, Alert Dashboard, Operations Dashboard, Extrusion boards: several plants, several different query sets |
| **D - plant-specific** | Exists at one plant | Classify each into one of the capability templates (F-05) | Most dashboards |

Classes and F- numbers are the proposals of SPEC-04 (draft for review), not decisions. Which plants
pilot class C is a decision for the owner (SPEC-04 Q2).

**Migration cost sits in few dashboards.** Literal-UUID predicates are concentrated: a small
fraction of dashboards holds half of them, typically very large boards copied by hand per machine,
module or station. To find them, sort the inventory by literal-UUID predicates per dashboard and
look at the top of the list before you plan a migration or a bulk change.

## 3. Family groups (qualitative)

Template names are those recorded on the family note. Languages are those printed on the dashboards
(not translated).

| Group | What the families show | Usual template |
|---|---|---|
| Andon boards and Gemba displays | Per line, cell, hall or plant status boards: state, part, cycle time, counters, alerts; hour-by-hour boards against target | Andon Board (some OEE Calculation) |
| Process-value monitoring | Equipment and process parameters per oven, autoclave, extrusion line, press, thermoforming line, conveying and drying, helium recovery | Process Values |
| Quality, SPC and traceability | Feedback and definition dashboards, SPC (X-bar and R), pull-test, paperless records, per-part traceability, leak-test traceability, scrap and shot weight | Process Quality Data, Manual Quality Data, Recipe Values |
| OEE, availability, downtime and alerts | OEE per machine type, plant alert dashboards, operations dashboards, downtime dashboards, maintenance and predictive maintenance | OEE Calculation, Machine Alerts, Downtime Reporting, Cycle Time |
| Platform, portals and housekeeping | Navigation and portal dashboards, DTQ and asset-structure tools, sandbox and test dashboards, WIP and deprecated drafts, edge device and camera status | Analytics, Other Use Cases |
| Production output, cycle time and reporting | Hourly production per line, daily and weekly reports, test-bench output, cycle-time and counter analysis | Andon Board, Analytics, Cycle Time, Process Quality Data |

Families named after a customer program or a single machine are usually class D. Many families exist
in more than one language; check the printed language before reusing labels.

## 4. Family cards - what each needs

Each card is a **reading of what the captured dashboards display**; "signals needed" are the
quantities shown, to be matched against `od-signal-standardization` names, not a requirement written
by a plant. Query patterns Q1 to Q9 are defined in
[`dashboard-json-sample.md`](dashboard-json-sample.md).

### 4.1 Plant Andon Board (Production Overview) - class C, Andon Board
- **Shows.** A machine table per plant: state, program or part number, current and average cycle
  time, part counts (total, OK, NOK, planned), alerts, time of last part. Variants per process
  family (assembly cell, bending and forming, test station, rubber board with autoclaves, extrusion
  lines and mandrel preparation, with target and actual metres).
- **Signals needed.** machine state, part number, cycle time, total/OK/NOK counters, alert count,
  last-part timestamp, operating mode (Automatic/Manual), shift totals.
- **Query pattern.** Q1 per tile and Q2 for trends; one UUID per tile, so large boards carry many
  literal UUIDs.
- **Trap.** Every plant fills the same layout with its own machines: several plants, several query
  sets. Recipe cells may read a placeholder text because the dashboard cannot fetch the recipe.

### 4.2 Operations Dashboard and Alert Dashboard - class C, Cycle Time / Machine Alerts
- **Shows.** Operations: a machine or station drill-down with part number, OK and NOK parts per
  interval, average cycle time, alert counts, an OK-versus-NOK history (a table of ok/nok/total
  counter, average cycle time, average waiting time); a shopfloor variant shows parts per machine and
  running versus not running. Alert: for one machine, the alert counter per reason (safety gates,
  bowl empty, accumulator overfilled, robot errors, laser data-matrix quality) as bar and donut, a
  table and a time-ordered log.
- **Signals needed.** part counter OK/NOK, cycle time, waiting time, machine running flag, alert
  code or text per event (a code-to-message lookup, as in the "Alerting" flows).
- **Trap.** A variant captured with all panels "No data" and error markers; the Operations name is
  used at several plants with different query sets.

### 4.3 Machine status timeline and OEE-A - Chinese AC lines and vulcanizers
- **Shows.** A coloured status bar over 24 h (Running, Idle, Changeover, Replace Plate, Equipment), a
  state-share pie, an OEE A gauge, day/night plan versus actual, hourly output bars; typically a
  current and a "New" version per line. Vulcanizer boards: product spec, latest takt, mould number,
  state timeline (setup or mould change, stopped, running), shift OEE-A gauges, cumulative output.
- **Signals needed.** machine status (string), production counter per shift, shift plan, start and
  end, standard time or takt.
- **Query pattern.** Q1 (string status, `LIMIT 1`) plus state-change durations; the OEE dashboards
  read a `CycleTimeSetting` variable.
- **Traps.** Implausible values in captures (absurd magnitudes, negative OEE-A); identical OEE
  figures across unrelated dashboards, which points to a shared or templated source.

### 4.4 Extrusion line Andon set - Andon Board, copy-by-line family
- **Shows.** For each line, several boards: line data, inner-layer extruder, knitting machine,
  upper-layer extruder, cutting machine (one line also spraying). Tiles: status, line speed set and
  actual, mandrel/die/vacuum-nozzle preset versus actual, mix and lot number, extruder rotation,
  motor current, mass pressure and temperature, vacuum, a zone-temperature table (screw, feed roller,
  cylinders, head: set, min, actual, max, out-of-limit flags).
- **Signals needed.** per extruder zone: set value, actual, tolerance; line speed; preset versus
  actual tooling; material identifiers.
- **Trap.** Some machines "still have to be connected to provide metres and pieces"; one line may be
  a template with a banner asking for the correct data points; several are marked TODO. A
  copy-by-line family multiplies the cost of changing one UUID by the number of copies.

### 4.5 Injection moulding Level 1 / 2 / 3 - three tiers
- **Shows.** Level 1 card view per press (state Automatic/Setup/Stop/Manual, part number, mould,
  material, parts per shift current/previous, last cycle time); Level 2 production overview (state
  tile, workplace, part, cavities, cycle-speed gauge, state durations per shift, hourly output,
  cycle-time statistics); Level 3 process values. Two press types each with their own set.
- **Signals needed.** machine state, order number, material number, mould number, part number,
  production quantity, cycle time, injection-unit times (plastification, injection, dwell pressure)
  for both units, real cure time, part counter, injection counter - exactly the template variables of
  the Level 2 dashboard.
- **Why it matters.** The only family built as three linked levels of the same signals (compare
  SPEC-03 S-05: split when a dashboard grows past the panel limit). The Level 1 card view is among the
  dashboards with the most literal UUIDs.

### 4.6 Hour-by-hour boards (Gemba board, hourly production per line) - Andon Board
- **Shows.** A Gemba board: for yesterday and today, per shift (early, late, night) and hour, good
  parts coloured against target next to a fault-type pie; a daily counter running from shift start to
  shift start; a fault colour key. Hourly production: a grid of line by hour coloured by scanned-OK
  pieces against an hourly target (green at or above target, yellow slightly below, light red well
  below), one dashboard per line, an hourly target per line.
- **Signals needed.** part counter OK/NOK, order and part number, hourly target (configuration, not a
  signal), shift boundaries, fault type.
- **Query pattern.** Q8 (shift windows in SQL) and Q9 (localised date text).
- **Trap.** The hourly target and the shift pattern live in the dashboard; a changed shift breaks
  every variant. Time filters are explained on the dashboard itself.

### 4.7 Autoclave boards - Process Values / Andon Board
- **Shows.** Shopfloor: running mode, heat-maintain time, cycles this shift, last cycle time (red
  above target), program number, set versus actual temperature and pressure, trends with limit lines.
  Process-value boards: temperature, condensate temperature, pressure per cycle, cycle and loading
  time, number of cycles. Andon variant: running or standby, cycles per shift, load times, active
  recipe, downtime in shift and day, active and inactive autoclave rows.
- **Signals needed.** mode, program number, temperature, pressure, condensate temperature, cycle
  counter, cycle start/end, load counter.
- **Trap.** One autoclave can return "No data" while its neighbours work: check the machine before
  the dashboard.

### 4.8 Curing ovens - Process Values
- **Shows.** Oven state, running program, temperature set point, actual and min/max corridor,
  conveyor speed set versus actual, heat-up timing (start, target reached, period, starting
  temperature). A variant adds an energy strip (minutes on, hours on, energy, cost).
- **Signals needed.** program name or number, zone actual temperature, set point, min/max, conveyor
  speed set and actual, up-heat start and achieved timestamps - the same list as the template
  variables of the oven dashboards (`program_name`, `heating_temperature_zone1_act`,
  `conveyer_speed_setpoint`, `upheat_time_hour`).
- **Design note.** A per-oven copy family (some copies marked "(old)") next to a "Curing Oven
  Dynamic" dashboard that picks the oven by variable: the dynamic one is the pattern to keep
  (variable binding); the copies are the cost it was meant to remove.

### 4.9 Downtime - Downtime Reporting
- **Shows.** Variant 1: accumulated downtime split into operator-selected categories (line idle,
  machine failure, staff out of cell, meal, missing staff/material/components, model change, 5S
  activities, briefing, non-conforming material, safety incident, plant evacuation) as pie, bar and
  heat strip; an autoclave board with recipe, average cycle, real cycles, downtime hours, efficiency
  and a floor-comment table filterable by shift, user, severity and tag. Variant 2: KPIs (total
  downtime, incident count, MTTR, MTBF, P95 duration, unassigned share, auto-detected share), Pareto
  by machine stacked by reason, machine and reason ranking, state timeline, day-of-week by hour heat
  map, duration histogram, incident table. Variables: machine, reason, severity, min and max
  duration, auto-detected.
- **Signals needed.** machine state (for detection) **and** an operator-entered reason, severity,
  comment and user - the second half is a record, not a signal.
- **Trap.** Two designs at two plants: relational incident tables versus category entry. SPEC-02
  proposes one downtime schema (D-08) based on the relational one; that is a proposal.

### 4.10 Machine alerts and maintenance counters
See 4.2 for the alert dashboard. Two other forms: an alarm analysis (last alarm text, count in
period, pie of alarm types, latest occurrence per type, full log, count time series) and
maintenance counters (a part-number by cycle-interval grid with red/yellow/green against interval
thresholds; mould counter tables with reset history). Signals: alarm code or text with timestamp,
cycle or part counter per tool. In the source, "Industrial Notifications MS Teams" is one use case at
several plants with blockers on definitions, machine list and third-party system.

### 4.11 SPC and process quality - Process Quality Data
- **Shows.** An extrusion SPC (X-bar chart with UCL/LCL and range chart, markers for product or
  recipe changes, tooltip naming the recipe); an extrusion SPC with operating-order timeline and
  trends of mandrel outer diameter, film wall thickness and film outer diameter against process
  value, set value, tolerance and intervention limits; line failure analysis (tolerance-band
  violations per measuring device and part number) and layer-adhesion pull-off SPC.
- **Signals needed.** process value, set value, upper/lower tolerance, upper/lower intervention
  limit, recipe id, order number - the quality-and-limits family of the catalogue (`CurrentValue`,
  `Hard/SoftUpper/LowerLimit`, `LimitValue`).
- **Trap.** SPC boards tend to bind very many literal UUIDs each.

### 4.12 Helium leak test and helium recovery
- **Shows.** Per test station: chambers, cycle time (min, average, max), booster pump, mechanical
  pump, helium burp, helium recovery, pieces tested per hour, final-evacuation pressure per part
  excluding negative values. Recovery units: vessel pressures against start/stop thresholds, mixing
  station, helium and air flow, pressure, temperature; a portal page with helium consumption per
  shift.
- **Signals needed.** per chamber: pressure phases, cycle time, accept and reject totals
  (`TotalAccepts`, `TotalRejects`, cumulative OK/NOK and hourly increment), pump states.
- **Trap.** "Excluding negative values" and similar filters appear in panel titles: the filtering of
  bad values is done in the panel, not in the signal.

### 4.13 Energy and utilities
- **Shows.** Infrastructure: kW per hour as bars with a trend and the total for electrical
  measurement points and gas points, from a metering vendor's data. Thermoforming ovens: zone
  temperatures with tolerance lines and average power in kW. Extrusion-line and chain-oven
  energy-management dashboards are created from time to time (see the change reports).
- **Signals needed.** energy (kW, kWh, m3) per measurement point, plus the production counter for
  normalisation (placement rule R5: monitoring is Process Values, usage analysis is Analytics).
- **Open.** The only verified external benefit basis for energy is the sub-metering source recorded
  in the Case Groups overview; see `bc-build`.

### 4.14 Platform tools and portals - classes A and B
- **Shows.** DTQ tools (class A): device journal with the command state ladder (01 created, 02 sent,
  03 acknowledged, 04 processing, 05 received, 07 processed, 08 done), device-type and datapoint
  schema specification, count of data points by UUID and label in the last n minutes, config-repo
  monitoring, tag and UUID overview. Process Value Overview (class B): numeric, string, Beckhoff and
  byte-array variants that plot one selected tag so engineers can check that a signal arrives. Plant
  portal: a department start screen (Production, Maintenance, Quality, Process, ESH, Automation,
  Lean) with link tiles.
- **Use.** The cheapest diagnostic at a plant: `DTQ - Count Datapoints by UUID, label in last n
  minutes` and the Process Value Overview answer "is the signal arriving?" before any flow is opened
  (see `ops-pipeline`).
- **Trap.** `Home` and the tag/UUID overview exist at many locations in several query-set variants.

## 5. Gaps to expect when you use the catalogue

- Some dashboard notes have no template placed and some have no use case found; a family is
  therefore not proof that a use case exists. Re-measure link coverage (high / medium / low /
  template-level pointer / none) on the current notes.
- Captures with little or no live data (layout only) are unreliable as references: quality
  definition and feedback boards, lab tests, inline measurement, injection moulding monitoring, test
  bench boards, paperless quality, autoclave process monitoring, extrusion process values and
  output, Operations Dashboard, customer crimping cells, analysis boards, sandbox. Re-capture before
  relying on them.
- The captures are older than the JSON export; folders and titles may have moved.
