---
type: Skill Reference
title: Dashboard estate baseline
description: What the plant Grafana estate looks like in the exports of 29 Oct to 3 Nov 2026 - size, platforms, data sources, query patterns, lifecycle and churn - and what it answers about the local Grafana data source that the OD integration note left open.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [analytical-support-service, practice, dashboard]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Dashboard estate baseline

Read this before you promise a plant a dashboard, a copy of one, or a migration. It is the
OD-side knowledge that `build-grafana-ops-dashboard` (vendored, generic) cannot carry: **what
the 19 plant Grafana instances actually contain and read.**

**Counts versus rules.** Every figure is a *count* from the exports read 2026-11-05, produced
and stated by `Dashboard Exports/specs` (SPEC-00 to SPEC-04, drafted 2026-11-03, "AI-drafted,
not reviewed by a human"), and by the dashboard notes and the change reports. Proposals in the
specs (requirements E-, D-, S-, F-) are quoted as proposals. Counting rule of the source: for
each (location, uid) only the newest run is used; 94 export runs, 8,280 JSON files, 19 locations,
runs of 2026-10-29 to 2026-11-03.

## 1. The estate in numbers (count, exports of 2026-10-29 to 2026-11-03)

| Measure | Value |
|---|--:|
| Locations exported | 19 |
| Unique dashboards (location, uid) | 1,010 (827 distinct uids) |
| Panels (rows excluded) | 17,961 |
| Queries / of which raw SQL | 24,422 / 19,900 |
| Dashboards with auto-refresh set | 315 (30%) |
| Dashboards with at least one tag | 572 (57%) |
| Dashboards with no template variable | 290 (29%) |
| Dashboards naming no data source input | 129 (13%) |
| Dashboards using more than one data source input | 246 (24%) |
| Median panels per dashboard / 90th percentile / maximum | 10 / 40 / 323 |
| Dashboards in a single plant | 748 (74%) |
| Dashboards whose title occurs in 3 or more plants | 228 (17 titles) |
| Dashboards in a lifecycle-named folder | 162 |
| Not saved for more than 180 days / 365 days | 456 / 285 |
| Dashboards at version 1 / 2-9 / 10-49 / 50+ | 155 / 407 / 321 / 127 |

Two other counts that are easy to mix up: the September screenshot inventory covers **481
dashboards in 74 families** (19 capture runs 2026-02-04 to 2026-02-12; `dev` folder left out; 149
inspected one by one); and the gap analysis of 2026-11-05 counts **827 dashboards** (latest run
per uid). Title matching finds 399 of the 481 inventory titles in the export and 472 of the 1,010
exported dashboards (47%) without an inventory title - the family notes describe about half the
estate.

**Usage is unknown.** The exports carry no views, so staleness is not evidence of non-use. Do
not retire a dashboard on age alone (SPEC-00 point 5).

## 2. Per plant (count)

| Plant | Grafana | Dashboards | Panels | Main data source inputs | Lifecycle-folder | Not saved >180 d | Literal UUID predicates |
|---|---|--:|--:|---|--:|--:|--:|
| Caluire | 8.5.22 | 29 | 345 | ConfigRepo 15, TelemetryPLC 12, InfluxDB 9 | 4 | 28 | 192 |
| Carei | 8.5.22 | 97 | 2,413 | TelemetryPLC 81, ConfigRepo 29, Datadash 19 | 0 | 32 | 2,358 |
| Changchun | 8.5.22 | 71 | 1,371 | Telemetry 58, ConfigRepo 10, InfluxDB-Dummy 9 | 23 | 7 | 1,785 |
| Changshu | 8.5.22 | 109 | 1,403 | InfluxDB 82, ConfigRepo 10, Telemetry 4 | 34 | 0 | 58 |
| Delicias | 8.5.22 | 50 | 538 | ConfigRepo 23, TelemetryPLC 23, Use-Cases 17 | 16 | 30 | 493 |
| Dolne Vestenice | 8.5.22 | 29 | 739 | ConfigRepo 14, TelemetryPLC 12, Datadash 5 | 0 | 13 | 895 |
| Hannover Stöcken | 8.5.22 | 18 | 309 | ConfigRepo 11, Telemetry 3, Datadash 1 | 0 | 10 | 383 |
| Karben | 8.5.22 | 57 | 1,988 | TelemetryPLC 24, ConfigRepo 12, Quackito 2 | 5 | 28 | 2,825 |
| Mako | 8.5.22 | 57 | 743 | ConfigRepo 25, TelemetryPLC 23, Use-Cases 9 | 0 | 43 | 806 |
| Monterrey | 8.5.22 | 67 | 584 | ConfigRepo 55, TelemetryPLC 34, Use-Cases 25 | 23 | 21 | 351 |
| Northeim | 8.5.22 | 16 | 286 | ConfigRepo 16, TelemetryPLC 6, Datadash 3 | 0 | 7 | 520 |
| Qingdao | 8.5.22 | 59 | 1,548 | Telemetry 36, ConfigRepo 8, Datadash 1 | 0 | 7 | 756 |
| Somersworth ("Sommersworth" in the folder) | 8.5.22 | 52 | 1,204 | ConfigRepo 34, TelemetryPLC 28, ContiTech 5 | 9 | 42 | 1,087 |
| Subotica | 8.5.22 | 27 | 422 | ConfigRepo 21, TelemetryPLC 14, Datadash 7 | 0 | 25 | 185 |
| Sun Prairie | **8.2.7** | 37 | 830 | ProdInfluxDB 35 | 4 | 13 | 0 |
| Testcenter (no plant note) | 8.5.22 | 15 | 112 | ConfigRepo 9, Telemetry 5, Datadash 4 | 0 | 14 | 78 |
| Timisoara | 8.5.22 | 71 | 1,124 | TelemetryPLC 56, ConfigRepo 16, Datadash 3 | 0 | 42 | 940 |
| Vac | 8.5.22 | 24 | 418 | ConfigRepo 14, TelemetryPLC 9, Use-Cases 4 | 0 | 14 | 562 |
| Waltershausen | **11.0.6** | 125 | 1,584 | TelemetryPLC 76, ConfigRepo 34, QFPR - Productive 20 | 44 | 80 | 2,178 |
| **Total** | | **1,010** | **17,961** | | **162** | **456** | **16,452** |

Plants that are in the machine list but are *not among the 19 exported locations* (for example Tlalnepantla, Ponta
Grossa, San Luis Potosi, Montemorelos) are not exported: ⟨which plants run a Grafana at all -
export owner⟩.

## 3. Platforms and what they imply

- **Two platforms, three versions.** 17 locations report Grafana 8.5.22; Sun Prairie 8.2.7;
  Waltershausen 11.0.6. The PostgreSQL data source type is `postgres` on 8.5.22 (881 inputs)
  and `grafana-postgresql-datasource` on Waltershausen (159 inputs, 115 dashboards).
  *Inference (SPEC-01 F1):* dashboards cannot be copied between these without checking the
  plugin id.
- **Schema versions do not always match the server.** 766 dashboards at `schemaVersion` 36, 100
  (all Waltershausen) at 39, 91 (all Changshu) at 40, 51 at 32. Changshu's 40 does not fit its
  reported 8.5.22 - a human must confirm before any bulk import into an 8.5.22 server.
- **Plugin dependency.** The community ECharts panel (`bilibala-echarts-panel`) is in 273
  dashboards (1,241 panels), 7% of all panels; the clock panel in 19. A plugin is an install
  dependency on every server.

## 4. Answer to the open point in `build-grafana-ops-dashboard/OD-INTEGRATION.md`

That note leaves open "the local datasource each plant's Grafana reads - engine, and whether it
is uniform across sites". The exports answer it as follows (counts, 2026-11-03):

| Question | Finding |
|---|---|
| Engine of the telemetry source | A PostgreSQL-type source with a table `telemetry` (653 dashboards, 18,375 queries); the queries use `time_bucket`, a function the engine of these dashboards provides. *Inference:* the export does not name the database product; ⟨confirm - data team⟩ |
| Uniform across sites? | **No.** Three families of source: PostgreSQL-type `telemetry` and `ConfigRepo` at 17 of 19 locations; InfluxDB at Changshu (82 dashboards), Sun Prairie (35), Caluire (9), Changchun (9), Qingdao (1) - 136 inputs; Prometheus 14 inputs in 10 locations; MSSQL 5 inputs in 5 dashboards (Waltershausen, schema `emes`) |
| Same source name everywhere? | **No.** The telemetry source is `TelemetryPLC` in 398 inputs, `Telemetry` in 110, and `Quackito` is an alternative named in the data-source variable (what it is: ⟨open⟩). Dashboards cope with a variable that filters by name, for example `/Telemetry|Quackito/` (230 dashboards) |
| Is DuckDB in use? | No DuckDB input appears in SPEC-01 or SPEC-02. The portability rule in the vendored skill is therefore not exercised by the estate; it stays as written (the OD note's own conclusion) |
| Cross-plant analytics layer | Not Grafana. Local Grafana reads local data; the cross-plant platform is Databricks/Azure Storage (already stated in `SKILL.md`) |

So the **timeseries archetype** of the vendored skill (UUID-keyed long format) is the shape of
the PostgreSQL-type estate; the InfluxDB dashboards (Changshu, Sun Prairie and others) read by
`topic` tag and are a separate case (below).

## 5. How the estate reads data (count)

**Time-series table `telemetry`.** Columns the queries use: `systime`, `uuid`, `value_double`,
`value_integer`, `value_bool`, `value_string` (12,227 / 12,673 / 10,966 / 2,281 queries) and
`is_delta` (13,819 queries, 586 dashboards; eight spellings: `'t'` 10,292, `$delta` 1,987, `true`
805, `'f'` 383, `TRUE` 159, `True` 152, `$isDelta` 107, `'true'` 54).

| Pattern | Count | Consequence |
|---|--:|---|
| Signal named by a literal UUID in SQL | 16,452 predicates, 498 dashboards, 6,590 distinct UUIDs | a re-created data point breaks every dashboard that holds the old one; 2,375 UUIDs appear in 2 or more dashboards, 67 in 2 or more plants |
| Signal bound through a variable | 1,533 predicates | the pattern to keep |
| Empty binding `uuid = ''` | 450 predicates, 49 dashboards | returns nothing, says nothing |
| `COALESCE(value_double, value_integer, value_bool::integer)` | 8,463 queries | the query does not know the type of the signal |
| Time macros (`$__timeFilter`, `$__timeFrom`) | 18,432 queries | follow the time picker |
| `now()` or interval literals | 670 queries in 67 dashboards | ignore the time picker |
| `time_bucket` fixed width / `$__interval` | 6,160 / 5,740 | fixed buckets over- or under-sample |
| Scaling and unit decided in the panel | units set on 7,041 of 17,961 panels (1,513 of them `none`) | the same signal can differ across dashboards |

**Registry (`ConfigRepo`).** The `DTQ - ...` tool dashboards join `data_points.uuid` ->
`devices` -> `datatrons`, and `devices` -> `device_types` (name, make, model, class, JSON
schemas). 157 dashboards in 18 locations do this. The registry knows datatron, device and device
type per UUID and carries no plant, machine, unit or scale (as seen from the queries).

**Other tables.** `downtime_incidents`, `downtime_reasons`, `machines` (7 dashboards at Mako,
Testcenter, Subotica); a paper-form downtime table (Subotica); tables named `oesl-...` read
with `SELECT *` (62 dashboards at 8 plants, Monterrey 24, Delicias 17, Mako 9); `emes` on MSSQL.

**InfluxDB dashboards.** 136 inputs; no UUID predicates. They address the signal by the `CT/...`
topic path in a `topic` tag and read a value field (`valueFloat`, `valueBool`) from a measurement
(the two sampled dashboards, one per plant, use different measurement names). A renamed topic breaks them just as a changed UUID
breaks the PostgreSQL ones (see `od-signal-standardization`, `field-signal-vocabulary.md`).

## 6. How dashboards are built (count)

| Aspect | Observed |
|---|---|
| Panel mix (17,961) | stat 9,573 (53%), timeseries 2,243, text 2,225, ECharts 1,241, table 898, piechart 506, state-timeline 450, gauge 266; legacy `graph` 46 and `table-old` 15 |
| Stat panels | 3,450 of 9,573 have no title; 2,989 have more than one threshold step |
| Untitled panels / empty queries | 4,494 / 2,231 targets in 181 dashboards |
| Default time range | `now-6h` 260 dashboards, `now-24h` 149, `now-5m` 87, `now-1h` 83; at least 31 shift-aligned (`now/d+7h`) |
| Refresh | off 695, 5 s 101, 1 min 94 |
| Variables | `datasource` 316, `datatron` 250, `delta` 180, `device` 145, `plc` 105, `machine` 56 and `Machine` 25 |
| Documentation | description on 128 dashboards (13%) and 1,736 panels (10%) |
| Reuse | 7 library panels in the whole estate; 73 dashboards with dashboard links |
| Language | 63 titles contain Chinese; many carry German, Spanish, Romanian or Hungarian |

## 7. Lifecycle and churn

Status lives in folder names only: `dev` 39, `Migrated` 34, `In Use (old!)` 23, `ZZ - WIP` 17,
`ZZ - Tools` 14, `archive`/`_archive` 13, `Trashbin` 9, `ZZ -Deprecated` 8, `ZZ Testing` 5.
Another 19 sit in `03_For Analysis` (a work stage). 32 titles carry a draft/copy/test word. The
most frequent tags are `K` 201, `Tools` 136, `Rubber` 128; none means a status.

Change reports (generated 2026-11-02 from the newest run per location): **202 dashboards created
and 102 changed between 2026-08-01 and 2026-10-31.** The created dashboards are dominated by
bulk imports - Changshu 100 (65 in August, 35 in September) and Changchun 43 (August) - and by
Monterrey 16, Qingdao 16, Mako 5, Hannover Stöcken 5. Person identifiers in those reports are
not reproduced here.

## 8. What to do with this

1. Before building, look up the plant's row in section 2: Grafana version, source names and
   whether its dashboards bind by UUID (Sun Prairie and Changshu do not).
2. Check whether the plant already has a family (`dashboard-families-catalogue.md`).
3. Bind new panels through a variable or lookup, never a literal UUID, and use the time macros.
4. Treat `Testcenter`, `dev`, `ZZ - ...` and `Trashbin` as places not to copy from.
5. If the dashboard must cross plants, it does not belong on a local instance.

## Open

- ⟨What `Quackito` is and whether it replaces `Telemetry` - data team (SPEC-02 Q4).⟩
- ⟨Definition of `is_delta` - data team (SPEC-02 Q2).⟩
- ⟨Whether Grafana 11 (Waltershausen) is the target platform or an exception - OD lead
  (SPEC-01 Q1).⟩
- ⟨Who owns the central dashboard repository and the signal record - OD lead (SPEC-04 Q3).⟩
- ⟨Column types, keys, indexes and retention of `telemetry` - needs a schema dump; the DTQ
  "Database Tables and Fields" dashboard can produce one (SPEC-02 Q1).⟩

## Sources

`Work-OpsDigit-Knowledge/Dashboard Exports/specs/` SPEC-00 to SPEC-04 and `specs/data/`;
`Dashboard Exports/reports/` (counts only); `Vault Gap Analysis - SharePoint and Grafana Full
Text.md`; `Graph/Use Case Views/Dashboard Use Cases - Overview.md`; `Slide Index - 29-Dashboarding_Tool_Evaluation`
(a 4-slide deck of 2023-11-27 titled "Tool Evaluation for Dashboarding: Grafana, Superset,
PowerBI"; slide text was not read in detail). All read 2026-11-05.
