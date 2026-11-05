---
type: Skill Reference
title: Dashboard JSON sample 2026-11
description: A sample of 20 dashboard JSON exports spread over the 19 plant locations - their real structure, data sources and the nine query patterns found - with the sampling method stated so nobody mistakes it for a census.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [analytical-support-service, practice, dashboard]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Dashboard JSON sample, read 2026-11-05

**This is a sample, not a census.** `Dashboard Exports/dashboards/` holds 8,280 JSON files (counted
2026-11-05; the same number as the specs of 2026-11-03; 94 of them are `run.json`) for 1,010 unique
dashboards, about 8 files per dashboard because runs repeat and early runs kept a `raw/` copy. They were
**not** opened one by one. The population-level numbers in
[`dashboard-estate-baseline.md`](dashboard-estate-baseline.md) come from the generated inventory
(`specs/data/dashboard-inventory.jsonl`); this file shows what a dashboard looks like inside,
from 20 of them.

## Method

- Population: dashboards in the inventory with at least 5 panels and 3 queries, outside the
  `Tools` folder (the platform tools are class A and have their own card in the families
  catalogue).
- Draw: one dashboard from each of the 19 locations by a fixed random seed, plus one more drawn
  from the rest of the population (a second Carei dashboard). Newest run copy of each.
- Read: panel types, data source types, template variables, refresh, time range, schema
  version, and the first query of the first panel(s). UUIDs in queries were replaced by
  `<uuid>`; no host name or user id is quoted.
- Limit: 20 of 1,010 is 2%. A pattern seen once says "this exists", not "this is common"; the
  frequencies for the whole estate are in the baseline file.

## The 20 dashboards

"Queries" is the number of targets with query text. "Data source" is the type of the target's data
source in the JSON (`default` = a target without an explicit type; `pg11` = the Grafana 11
PostgreSQL type). "Literal UUIDs" is the inventory's count of `uuid = '<literal>'` predicates.

| Plant | Dashboard | Folder (end) | Panels | Queries | Data source (targets) | Variables (first) | Refresh / range | Literal UUIDs | Schema |
|---|---|---|--:|--:|---|---|---|--:|--:|
| Caluire | Thin Tube - Process Values | Villeurbanne - Thin Tube | 8 | 8 | postgres 2, default 6 | database | off / now-3h | 8 | 36 |
| Carei | Extrusion Lines - Andon Board | 00.Carei - Production Overview | 97 | 64 | postgres 64 | - | 15m / now-6h | 52 | 36 |
| Changchun | Helium03 | 03_For Analysis | 25 | 40 | postgres 40 | database, CycleTimeSetting | off / fixed date | 40 | 36 |
| Changshu | a QC-laboratory first-sample result board (Chinese title) | In Use - Section 2 | 12 | 34 | influxdb 110 | - | 5s / now-18h | 0 | 40 |
| Delicias | Autoclave 2 | Production | 10 | 15 | postgres 15 | datasource, delta, hora, horas | 1m / now/d+6h | 13 | 36 |
| Dolne Vestenice | BMW KL34 - Level 2 - Production Overview (obsolet) | Assembly - KL34 | 21 | 17 | postgres 17 | - | off / now-24h | 17 | 36 |
| Hannover Stöcken | KKA_Martin | KKA | 8 | 20 | postgres 20 | datasource, bucket | 10s / now-12h | 28 | 36 |
| Karben | DEV - HDEP/HDES WKZTs | Halle 4 - HDEP / HDES | 39 | 39 | postgres 39 | - | off / now-24h | 39 | 36 |
| Mako | Autoclave 4-10-13-17 - Shopfloor | Vulcanization Area | 32 | 48 | postgres 48 | datasource, delta | off / now-6h | 44 | 36 |
| Monterrey | Hourly production_T1 SD L2 | Playlists | 10 | 13 | postgres 6, default 7, expression 2 | datatron, plc, partcounter, machine ... | off / now/d+7h | 4 | 36 |
| Northeim | VIM - Maschinen Übersicht (absolute Werte) | Automaten Center | 66 | 286 | postgres 286 | - | 1m / now-1h | 280 | 36 |
| Qingdao | MachineStatus Timeline 101 | In Use | 23 | 20 | postgres 13, datasource 7 | - | off / now/d+7h | 12 | 36 |
| Somersworth | Scrap Overview | Process Values | 20 | 29 | postgres 29 | datatron, device, delta, partnumber ... | off / now-12h | 22 | 36 |
| Subotica | Paper Form Records | Building 1 | 16 | 17 | postgres 13, default 4 | equipment, workplace, shift, partnumber ... | off / now-24h | 0 | 36 |
| Sun Prairie | Cover 3 ME | Manufacturing Engineering | 25 | 10 | influx input 28, expression 2 | Machine, datapoint | 5s / now-1h | 0 | 32 |
| Testcenter | Extrusion-204 (Quackito test) | General | 26 | 58 | postgres 58 | datasource | off / fixed date | 58 | 36 |
| Timisoara | Helium Recovery/Seiler Container | Production Line Dashboards | 36 | 41 | postgres 41 | - | 1m / now-6h | 35 | 36 |
| Vac | B8X1 - PCB | Hall 3 - Finished Product Manufacturing (ERS) - BMW SFL | 9 | 21 | postgres 16, default 5 | datasource, datatron, device, mode ... | off / fixed date | 13 | 36 |
| Waltershausen | Endbearbeitung 3 / 4 | WTH2 - Hall 10 & 10a/PC 38/Production Overview | 11 | 14 | pg11 12, postgres 2 | - | off / now-6h | 14 | 39 |
| Carei | 99_Curing_Oven_Dynamic | Hall 3 - Silicon Area | 19 | 21 | postgres 21 | datasource, delta, area, datatron ... | 1m / now-2d | 0 | 36 |

## What the sample shows

1. **17 of 20 read the PostgreSQL-type source; 2 read InfluxDB (Changshu, Sun Prairie); 1 is
   mixed with expression targets.** Consistent with the estate counts (136 InfluxDB inputs).
2. **16 of 20 bind signals by literal UUID.** The four without are Changshu and Sun Prairie
   (InfluxDB, bound by `CT/...` topic), Subotica (paper-form records from a relational table,
   bound by variables) and the Carei dynamic oven dashboard (bound through the registry variables
   `datatron`, `plc`, `area`). The estate figure is 498 of 1,010 dashboards.
3. **Schema versions follow the platform:** 17 at 36, Waltershausen 39, Changshu 40, Sun Prairie 32.
4. **The dashboards that bind by variable are the generic ones** (a tag picker, an oven picker, a
   machine picker) - the only way one dashboard serves many machines.
5. **Leftover queries sit behind text panels.** Two sampled dashboards (Mako autoclave, Timisoara
   helium recovery) carry a text-panel target of the form `SELECT systime AS "time", value_double
   FROM telemetry WHERE $__timeFilter(systime) ORDER BY 1` with **no UUID predicate**. A text
   panel does not run it (inference); if the panel were changed to a table it would read every
   signal in the time window. 2,231 targets in 181 dashboards have no query text at all (SPEC-03
   S-07).
6. **A test copy exists:** the Testcenter dashboard "Extrusion-204 (Quackito test)" has 58 literal
   UUIDs and a `datasource` variable - evidence of how the alternative source is being tried.
7. **Names carry the lifecycle:** "(obsolet)" in a title, `DEV` in a title (Karben, the dashboard
   with most literal UUIDs in the estate, 811), a `03_For Analysis` folder.

## The nine query patterns

Masked as found. `<uuid>` is a literal data-point id; `$x` is a Grafana variable.

| ID | Pattern (shape) | Seen in | Note |
|---|---|---|---|
| Q1 | `SELECT time_bucket('$__interval', systime) AS "time", value_string AS "label" FROM telemetry WHERE $__timeFilter(systime) AND uuid = '<uuid>' AND is_delta IN ('t','f') GROUP BY 1,2 ORDER BY 1 DESC LIMIT 1` | Caluire, Carei, Qingdao, Waltershausen | latest value in the window; the value column is chosen per signal (`value_string`, `value_bool::integer`, or a COALESCE) |
| Q2 | `SELECT time_bucket('1s', systime) AS "time", COALESCE(value_double, value_integer, value_bool::integer) AS "Cycle Time" FROM telemetry WHERE $__timeFilter(systime) AND uuid = '<uuid>' AND is_delta IN ('t') AND value_integer < 60000 GROUP BY 1,2 ORDER BY 1` | Changchun, Dolne Vestenice | a fixed bucket (`1s`) and a plausibility cut-off written into the query |
| Q3 | `SELECT (COALESCE(value_double, value_integer::double precision)) / 10 AS value FROM telemetry WHERE $__timeFilter(systime) AND uuid IN ('<uuid>') ORDER BY systime DESC LIMIT 1` | Hannover Stöcken | **the scale factor is in the panel** (divide by 10) |
| Q4 | `SELECT t.systime AS "time", CASE t.uuid WHEN '<uuid>'::uuid THEN '54 WKZT 1' WHEN '<uuid>'::uuid THEN '57 WKZT' ... END AS name ... FROM telemetry t` | Karben | **the label of each UUID is written in the SQL** - the signal-to-name mapping lives in the query |
| Q5 | `SELECT UPPER(datatrons.name) AS __text, datatrons.id AS __value FROM datatrons WHERE datatrons.id IN ($datatron)`; `SELECT regexp_replace(devices.name, ' - PLC', '') AS __text, STRING_AGG(devices.id::text, ',') AS __value FROM devices WHERE devices.datatron_id IN ($datatron) AND devices.id IN ($plc) GROUP BY __text` | Somersworth, Carei dynamic, Northeim | variable queries over the registry: the way to bind without a literal UUID |
| Q6 | InfluxQL: `SELECT "valueFloat" FROM "<measurement>" WHERE ("topic"::tag = 'CT/OESL/AS/CHN/CSHZ/<machine>/<leaf>') AND $timeFilter`; or `SELECT first("valueBool") FROM "<measurement>" WHERE ("topic" = 'CT/OESL/NA/USA/SPR/Cover/Cover_1/Line_Running') ORDER BY time DESC LIMIT 10` | Changshu, Sun Prairie | signal bound by topic path; two dialects of query |
| Q7 | `SELECT downtime_reason AS reason, SUM(total_downtime_min) AS total_downtime FROM paper_form_downtime_bending_v2 WHERE $__timeFilter(timestamp_local) AND workplace IN ($workplace) AND machine IN ($equipment) AND shift IN ($shift) AND partnumber IN ($partnumber) GROUP BY ...` | Subotica | a relational form table, filtered by variables; no UUID |
| Q8 | `WITH status_changes AS (SELECT systime, value_bool::integer AS status, LAG(systime) OVER (ORDER BY systime) AS prev_time FROM telemetry WHERE systime >= CURRENT_DATE + INTERVAL '5 hours 45 minutes' - INTERVAL '1 hour' * $time_offset AND systime < CURRENT_DATE + INTERVAL '13 hours 45 minutes' - ...)` | Vac | **the shift window (05:45 to 13:45) is a literal in the SQL**; the time picker is bypassed (the `now()`/`CURRENT_DATE` family: 670 queries in 67 dashboards) |
| Q9 | `SELECT TO_CHAR($__timeFrom()::timestamp, 'DD-') \|\| CASE TO_CHAR($__timeFrom()::timestamp, 'MM') WHEN '01' THEN 'Enero' WHEN '02' THEN 'Febrero' ... END` | Monterrey | localisation (Spanish month names) done in SQL |

## Reading the patterns

- **Q1 to Q3 are the same thing three times**: read one signal, pick a value column, bucket by
  time. The choices that differ between them (value column, bucket width, scale, cut-off) are
  exactly the four things `od-signal-standardization` asks to be stored with the signal
  (`assets/signal-binding-sheet.md`: value type, unit, scale, collection method).
- **Q4 and Q8 hide configuration in SQL**: a label per UUID, a shift window. Both belong in a
  lookup, a variable or the flow config.
- **Q5 and Q7 are the healthy ones**: the dashboard asks the registry or a form table which
  machine to show, and nothing machine-specific is typed.
- **Q6 needs its own rule**: an InfluxDB dashboard is only as stable as the `CT/...` topic path.
- For build mechanics use the vendored skill's SQL patterns (`relational_patterns.sql`,
  `timeseries_patterns.sql`); this file tells you what the plants have done instead.
