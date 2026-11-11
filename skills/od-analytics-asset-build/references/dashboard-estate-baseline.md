---
type: Skill Reference
title: Dashboard estate baseline
description: How to read and measure the plant Grafana estate (platforms, data sources, query patterns, lifecycle, churn) from the dashboard exports, and which patterns to expect. Guidance only - it holds no counts, shares or per-plant tables; measure them live.
resource: ../SKILL.md
status: draft
tags: [analytical-support-service, practice, dashboard]
---
# Dashboard estate baseline

Read this before you promise a plant a dashboard, a copy of one, or a migration. It is the
OD-side knowledge that `build-grafana-ops-dashboard` (vendored, generic) cannot carry: **what the
plant Grafana instances typically contain and read, and how to find out for the plant in front of
you.**

**This file holds no figures.** Sizes, shares, per-plant rows and dated counts change with every
export. Count them on the current export (section 1) and quote a number only with its export date.
Proposals in the specs (requirements E-, D-, S-, F-) are proposals, not decisions; the specs are
AI-drafted and were not reviewed by a human when read.

## 1. How to measure the estate (obtain, do not quote)

Source: `Dashboard Exports/specs` (SPEC-00 to SPEC-04) and `specs/data/dashboard-inventory.jsonl`
in the department knowledge base; dashboard JSON under `Dashboard Exports/dashboards/`; change reports under
`Dashboard Exports/reports/`. Counting rule of the source: for each (location, uid) only the newest
run is used. Always state which export run a count comes from.

| Question | Field or filter to read in the inventory | How to interpret |
|---|---|---|
| Which locations were exported at all? | distinct `location` | A plant missing here may simply not be exported; ask the export owner whether it runs a Grafana |
| How many unique dashboards? | distinct (location, uid); distinct uid separately | The two bases differ because the same uid exists in several plants; do not mix them |
| How big are dashboards? | panels per dashboard (rows excluded): median, upper percentile, maximum | The median is the normal case; a very large maximum is a copy-by-hand pattern |
| Which data sources are read? | data source type and name per target, per location | See section 4 for what to expect |
| Is a signal bound by literal UUID or by variable? | `uuid = '<literal>'` predicates vs `uuid = $var` / registry join | Literal binding is the migration cost |
| How live is a dashboard? | `version`, last-saved date | Staleness is **not** evidence of non-use: the exports carry no views |
| Lifecycle | folder names, tags, title words (draft, copy, test, old) | Status often lives in folder names only |
| Churn | change reports: created and changed per period | Bulk imports dominate "created"; read the per-plant split before inferring activity |

Two inventories are easy to confuse: the screenshot inventory (family notes, a snapshot taken on
capture days) and the JSON export (every dashboard, newest run). They cover different bases and
different dates; do not add them. Title matching between them is partial, so family notes describe
only part of the estate.

**Usage is unknown.** Do not retire or reject a dashboard on age alone.

## 2. Per plant: what to look up before you build

For the plant in question, read its row in the inventory and answer:

| Item | Where | Why it matters |
|---|---|---|
| Grafana server version | location metadata / `run.json` | Plugin ids and schema versions differ between versions |
| PostgreSQL-type source plugin id | data source `type` | `postgres` on older servers vs `grafana-postgresql-datasource` on Grafana 11-class servers; dashboards cannot be copied across without checking the id |
| Names of its data source inputs | data source name per target | Names differ by plant (see section 4); import needs the right binding |
| Does it bind by UUID or by topic/variable? | predicates in queries | Decides how fragile a copy is |
| Lifecycle-named folders | folder paths | `dev`, `ZZ - ...`, `Trashbin`, `Testcenter` are places not to copy from |
| Schema version vs reported server version | dashboard JSON `schemaVersion` | A mismatch means the server version is mis-reported or the dashboard came from elsewhere; a human must confirm before any bulk import |

## 3. Platforms and what they imply

- **Expect more than one platform generation.** Most plants run one server generation; a few run
  older or newer ones. The PostgreSQL data source type id differs between generations.
  *Inference (SPEC-01 F1):* check the plugin id before copying a dashboard between plants.
- **Schema versions do not always match the server.** Treat a mismatch as a question to resolve,
  not as proof of either.
- **Plugin dependency.** The community ECharts panel and the clock panel are install dependencies
  on every server that opens the dashboard. Measure how many panels use them on the current
  export before relying on them.

## 4. The local data source: what to expect (answer to the open point in `build-grafana-ops-dashboard/OD-INTEGRATION.md`)

That note leaves open "the local datasource each plant's Grafana reads - engine, and whether it is
uniform across sites". The exports answer it qualitatively:

| Question | Finding |
|---|---|
| Engine of the telemetry source | A PostgreSQL-type source with a table `telemetry`; the queries use `time_bucket`, a function the engine of these dashboards provides. *Inference:* the export does not name the database product; ⟨confirm - data team⟩ |
| Uniform across sites? | **No.** Expect three families of source: PostgreSQL-type `telemetry` and `ConfigRepo` at most locations; InfluxDB at a few locations; a small number of Prometheus and MSSQL inputs. Measure which locations use which |
| Same source name everywhere? | **No.** The telemetry source appears under more than one name, and an alternative source (`Quackito`; what it is: ⟨open⟩) appears in the data-source variable. Dashboards cope with a variable that filters by name, for example `/Telemetry\|Quackito/` |
| Is DuckDB in use? | Not seen in the specs. The portability rule in the vendored skill is therefore not exercised by the estate; it stays as written (the OD note's own conclusion) |
| Cross-plant analytics layer | Not Grafana. Local Grafana reads local data; the cross-plant platform is Databricks/Azure Storage (already stated in `SKILL.md`) |

So the **timeseries archetype** of the vendored skill (UUID-keyed long format) is the shape of the
PostgreSQL-type estate; InfluxDB dashboards read by `topic` tag and are a separate case (below).

## 5. How the estate reads data (patterns to recognise)

**Time-series table `telemetry`.** Columns the queries use: `systime`, `uuid`, `value_double`,
`value_integer`, `value_bool`, `value_string`, and `is_delta`. The `is_delta` flag shows up in
several spellings (`'t'`, `$delta`, `true`, `'f'`, `TRUE`, `True`, `$isDelta`, `'true'`); pick one
and expose it as the `$delta` variable.

| Pattern | Consequence |
|---|---|
| Signal named by a literal UUID in SQL | A re-created data point breaks every dashboard that holds the old one; the same UUID recurs across dashboards and sometimes across plants. This is the main migration cost |
| Signal bound through a variable | The pattern to keep |
| Empty binding `uuid = ''` | Returns nothing, says nothing; find them by grep |
| `COALESCE(value_double, value_integer, value_bool::integer)` | The query does not know the type of the signal; state the type in the signal record |
| Time macros (`$__timeFilter`, `$__timeFrom`) | Follow the time picker: keep |
| `now()` or interval literals | Ignore the time picker; legitimate only with a note |
| `time_bucket` fixed width vs `$__interval` | Fixed buckets over- or under-sample when the range changes |
| Scaling and unit decided in the panel | The same signal can differ across dashboards; keep unit and scale with the signal |

**Registry (`ConfigRepo`).** The `DTQ - ...` tool dashboards join `data_points.uuid` -> `devices` ->
`datatrons`, and `devices` -> `device_types` (name, make, model, class, JSON schemas). The registry
knows datatron, device and device type per UUID and carries no plant, machine, unit or scale (as
seen from the queries).

**Other tables.** Downtime tables (`downtime_incidents`, `downtime_reasons`, `machines`), paper-form
downtime tables, tables named `oesl-...` read with `SELECT *`, and an `emes` schema on MSSQL appear
at individual plants. Find them with a grep on the current export.

**InfluxDB dashboards.** No UUID predicates. They address the signal by the `CT/...` topic path in a
`topic` tag and read a value field (`valueFloat`, `valueBool`) from a measurement; measurement names
differ between plants. A renamed topic breaks them just as a changed UUID breaks the PostgreSQL ones
(see `od-signal-standardization`, `field-signal-vocabulary.md`).

## 6. How dashboards are built (what to expect and what to fix)

| Aspect | Typical observation |
|---|---|
| Panel mix | stat panels dominate, followed by timeseries, text, ECharts, table, piechart, state-timeline, gauge; legacy `graph` and `table-old` still occur |
| Stat panels | many have no title; many carry several threshold steps |
| Untitled panels / empty queries | occur in a noticeable share of dashboards (leftover text-panel targets) |
| Default time range | mixed: hours-long for trend boards, minutes for status boards; some shift-aligned (`now/d+7h`) |
| Refresh | most off; a minority at 5 s or 1 min |
| Variables | `datasource`, `datatron`, `delta`, `device`, `plc`, `machine` (and a capitalised `Machine` duplicate) |
| Documentation | descriptions are rare on dashboards and panels |
| Reuse | library panels are almost unused; dashboard links are uncommon |
| Language | titles in several languages (Chinese, German, Spanish, Romanian, Hungarian); do not translate silently |

Measure each row on the current export when you need a number.

## 7. Lifecycle and churn

Status lives in folder names only (patterns: `dev`, `Migrated`, `In Use (old!)`, `ZZ - WIP`,
`ZZ - Tools`, `archive`/`_archive`, `Trashbin`, `ZZ -Deprecated`, `ZZ Testing`, `03_For Analysis` as a
work stage). Titles carry draft/copy/test words. Tags are rarely a status.

Change reports are generated from the newest run per location. Read them as: created dashboards are
dominated by bulk imports at a few plants, so a large "created" figure is not new design work.
Person identifiers in those reports are not reproduced.

## 8. What to do with this

1. Before building, look up the plant's row (section 2): Grafana version, source names and whether
   its dashboards bind by UUID or by topic.
2. Check whether the plant already has a family (`dashboard-families-catalogue.md`).
3. Bind new panels through a variable or lookup, never a literal UUID, and use the time macros.
4. Treat `Testcenter`, `dev`, `ZZ - ...` and `Trashbin` as places not to copy from.
5. If the dashboard must cross plants, it does not belong on a local instance.

## Open

- ⟨What `Quackito` is and whether it replaces `Telemetry` - data team (SPEC-02 Q4).⟩
- ⟨Definition of `is_delta` - data team (SPEC-02 Q2).⟩
- ⟨Whether the newest Grafana generation is the target platform or an exception - OD lead (SPEC-01 Q1).⟩
- ⟨Who owns the central dashboard repository and the signal record - OD lead (SPEC-04 Q3).⟩
- ⟨Column types, keys, indexes and retention of `telemetry` - needs a schema dump; the DTQ
  "Database Tables and Fields" dashboard can produce one (SPEC-02 Q1).⟩

## Sources

`Dashboard Exports/specs/` SPEC-00 to SPEC-04 and `specs/data/`;
`Dashboard Exports/reports/`; `Knowledge base Gap Analysis - SharePoint and Grafana Full Text.md`;
`Graph/Use Case Views/Dashboard Use Cases - Overview.md`. Read 2026-11-05; used for patterns only.
