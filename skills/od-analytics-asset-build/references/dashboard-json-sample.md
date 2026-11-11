---
type: Skill Reference
title: Dashboard JSON sample
description: How to sample dashboard JSON exports to see their real structure, and the nine query patterns found (masked shapes) with what each tells a builder. Guidance only - no per-dashboard table, counts or plant names.
resource: ../SKILL.md
status: draft
tags: [analytical-support-service, practice, dashboard]
---
# Dashboard JSON sample

**A sample is not a census.** `Dashboard Exports/dashboards/` holds many JSON files per unique
dashboard (runs repeat, and early runs kept a `raw/` copy; `run.json` files are run metadata). They
are not meant to be opened one by one. Population-level numbers come from the generated inventory
(`specs/data/dashboard-inventory.jsonl`), see `dashboard-estate-baseline.md`;
this file shows what a dashboard looks like inside.

## Method (repeat it when you need a fresh look)

- Population: dashboards in the inventory with a few panels and queries at least, outside the
  `Tools` folder (the platform tools are class A and have their own card in the families catalogue).
- Draw: one dashboard from each location by a fixed random seed, plus one extra from the rest. Take
  the newest run copy of each.
- Read: panel types, data source types, template variables, refresh, time range, schema version, and
  the first query of the first panel(s). Replace UUIDs in queries by `<uuid>`; do not quote host
  names or user ids.
- Limit: a small sample says "this pattern exists", not "this is common"; frequencies for the whole
  estate come from the inventory, with the export date.

## What a sample of this kind tends to show

1. **Most dashboards read the PostgreSQL-type source; a minority read InfluxDB; a few mix
   expression targets.**
2. **Most bind signals by literal UUID.** The exceptions are InfluxDB dashboards (bound by `CT/...`
   topic), relational form-table dashboards (bound by variables) and dynamic dashboards bound through
   the registry variables `datatron`, `plc`, `area`.
3. **Schema versions follow the platform**; an outlier schema version is a question about the server.
4. **The dashboards that bind by variable are the generic ones** (a tag picker, an oven picker, a
   machine picker) - the only way one dashboard serves many machines.
5. **Leftover queries sit behind text panels.** A text-panel target such as `SELECT systime AS "time",
   value_double FROM telemetry WHERE $__timeFilter(systime) ORDER BY 1` with **no UUID predicate**
   is not run by a text panel (inference); if the panel were changed to a table it would read every
   signal in the time window. Targets with no query text at all are common (SPEC-03 S-07).
6. **A test copy of a production dashboard** (title with a source name such as "Quackito test") is
   evidence of how an alternative source is being tried.
7. **Names carry the lifecycle:** "(obsolet)" or `DEV` in a title, a `03_For Analysis` folder. The
   dashboards with the most literal UUIDs are often `DEV` boards.

## The nine query patterns

Masked as found. `<uuid>` is a literal data-point id; `$x` is a Grafana variable.

| ID | Pattern (shape) | Note |
|---|---|---|
| Q1 | `SELECT time_bucket('$__interval', systime) AS "time", value_string AS "label" FROM telemetry WHERE $__timeFilter(systime) AND uuid = '<uuid>' AND is_delta IN ('t','f') GROUP BY 1,2 ORDER BY 1 DESC LIMIT 1` | latest value in the window; the value column is chosen per signal (`value_string`, `value_bool::integer`, or a COALESCE) |
| Q2 | `SELECT time_bucket('1s', systime) AS "time", COALESCE(value_double, value_integer, value_bool::integer) AS "Cycle Time" FROM telemetry WHERE $__timeFilter(systime) AND uuid = '<uuid>' AND is_delta IN ('t') AND value_integer < 60000 GROUP BY 1,2 ORDER BY 1` | a fixed bucket (`1s`) and a plausibility cut-off written into the query |
| Q3 | `SELECT (COALESCE(value_double, value_integer::double precision)) / 10 AS value FROM telemetry WHERE $__timeFilter(systime) AND uuid IN ('<uuid>') ORDER BY systime DESC LIMIT 1` | **the scale factor is in the panel** (divide by 10) |
| Q4 | `SELECT t.systime AS "time", CASE t.uuid WHEN '<uuid>'::uuid THEN '<label 1>' WHEN '<uuid>'::uuid THEN '<label 2>' ... END AS name ... FROM telemetry t` | **the label of each UUID is written in the SQL** - the signal-to-name mapping lives in the query |
| Q5 | `SELECT UPPER(datatrons.name) AS __text, datatrons.id AS __value FROM datatrons WHERE datatrons.id IN ($datatron)`; `SELECT regexp_replace(devices.name, ' - PLC', '') AS __text, STRING_AGG(devices.id::text, ',') AS __value FROM devices WHERE devices.datatron_id IN ($datatron) AND devices.id IN ($plc) GROUP BY __text` | variable queries over the registry: the way to bind without a literal UUID |
| Q6 | InfluxQL: `SELECT "valueFloat" FROM "<measurement>" WHERE ("topic"::tag = 'CT/OESL/<region>/<country>/<plant>/<machine>/<leaf>') AND $timeFilter`; or `SELECT first("valueBool") FROM "<measurement>" WHERE ("topic" = 'CT/OESL/<region>/<country>/<plant>/<machine>/Line_Running') ORDER BY time DESC LIMIT 10` | signal bound by topic path; two dialects of query |
| Q7 | `SELECT downtime_reason AS reason, SUM(total_downtime_min) AS total_downtime FROM <paper_form_downtime_table> WHERE $__timeFilter(timestamp_local) AND workplace IN ($workplace) AND machine IN ($equipment) AND shift IN ($shift) AND partnumber IN ($partnumber) GROUP BY ...` | a relational form table, filtered by variables; no UUID |
| Q8 | `WITH status_changes AS (SELECT systime, value_bool::integer AS status, LAG(systime) OVER (ORDER BY systime) AS prev_time FROM telemetry WHERE systime >= CURRENT_DATE + INTERVAL '<shift start>' - INTERVAL '1 hour' * $time_offset AND systime < CURRENT_DATE + INTERVAL '<shift end>' - ...)` | **the shift window is a literal in the SQL**; the time picker is bypassed (the `now()`/`CURRENT_DATE` family) |
| Q9 | `SELECT TO_CHAR($__timeFrom()::timestamp, 'DD-') \|\| CASE TO_CHAR($__timeFrom()::timestamp, 'MM') WHEN '01' THEN 'Enero' WHEN '02' THEN 'Febrero' ... END` | localisation (Spanish month names) done in SQL |

## Reading the patterns

- **Q1 to Q3 are the same thing three times**: read one signal, pick a value column, bucket by time.
  The choices that differ between them (value column, bucket width, scale, cut-off) are exactly the
  four things `od-signal-standardization` asks to be stored with the signal
  (`assets/signal-binding-sheet.md`: value type, unit, scale, collection method).
- **Q4 and Q8 hide configuration in SQL**: a label per UUID, a shift window. Both belong in a lookup,
  a variable or the flow config.
- **Q5 and Q7 are the healthy ones**: the dashboard asks the registry or a form table which machine
  to show, and nothing machine-specific is typed.
- **Q6 needs its own rule**: an InfluxDB dashboard is only as stable as the `CT/...` topic path.
- For build mechanics use the vendored skill's SQL patterns (`relational_patterns.sql`,
  `timeseries_patterns.sql`); this file tells you what the plants have done instead.
