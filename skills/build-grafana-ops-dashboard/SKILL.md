---
name: build-grafana-ops-dashboard
description: >
  Build production-grade Grafana JSON dashboards backed by SQL for operations
  data — manufacturing, IIoT, energy, quality, throughput. Supports two data
  model archetypes: relational (custom fact + dimension tables) and timeseries
  (UUID-keyed long-format telemetry like ts-shape / UMH conventions). Use when
  the user wants importable Grafana dashboards with proper time-window handling,
  dashboard variables, ECharts panels, and audience-tiered layouts (manager /
  analyst / operations). Trigger when the user mentions Grafana, dashboard JSON,
  TimescaleDB queries for visualization, ECharts panels, MTBF/MTTR/OEE/Pareto,
  or asks for "manager view" vs "analyst view" splits. Complements
  /build-dashboard (which produces self-contained HTML); use this skill instead
  when the deliverable is a Grafana .json file.
allowed-tools: Read Grep Glob Write Edit
metadata:
  argument_hint: "<domain> <schema or signal list>"
  id: build-grafana-ops-dashboard
  tier: technical
  lane: [analytical-support-service, use-case-support-service]
  scope: portable            # domain-generic; not derived from the OD knowledge graph
  origin: vendored           # body and references are the author's, unmodified
  owner_role: human:jakob.gabriel
  authority_level: author the dashboard; publishing to a shared Grafana is human-approved
  status: stable
  sources_read: 2026-08-25
  related: [od-analytics-asset-build, od-data-availability-check, od-handover-and-adoption]
  od_integration: skills/build-grafana-ops-dashboard/OD-INTEGRATION.md
  derived_from:
    - vendored from the author's build-grafana-ops-dashboard skill (uploaded 2026-08-25)
  okf:
    type: Agent Skill
    title: Grafana ops dashboard builder
    tags: [analytical-support-service, portable, technical, use-case-support-service]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# build-grafana-ops-dashboard — Grafana JSON for Operations Data

## When to use this skill vs `/build-dashboard`

| Output is… | Use |
|---|---|
| Self-contained `.html` file with embedded data, Chart.js | `/build-dashboard` |
| Importable Grafana `.json` with live SQL, ECharts panels, variables | **this skill** |

If unspecified, ask once. The two outputs are not interchangeable — Grafana queries a live database; HTML embeds a static snapshot.

---

## Hard rules — apply to every SQL query in this skill

These two rules are **non-negotiable** and override any pattern shown elsewhere in the references. If a reference snippet contradicts them, the rule wins.

### Rule 1 — Always use Grafana query macros for time

Every SQL query authored under this skill must use Grafana's built-in macros for time filtering and bucketing. Hand-rolled `WHERE ts BETWEEN $__timeFrom() AND $__timeTo()` is a bug — it bypasses macro expansion, breaks across datasources, and fails the portability rule below.

| Need | Use this | Not this |
|---|---|---|
| Time-range WHERE | `$__timeFilter(ts_column)` | `ts BETWEEN $__timeFrom() AND $__timeTo()` |
| Time bucketing in SELECT | `$__timeGroup(ts_column, $__interval)` | `time_bucket('1h', ts)` or `date_trunc('hour', ts)` |
| Time bucketing with `time` alias | `$__timeGroupAlias(ts_column, $__interval)` | manual `... AS time` |
| Bucket size | `$__interval` (auto from panel width) | hardcoded `'1 hour'` |
| Unix epoch bounds | `$__unixEpochFrom()` / `$__unixEpochTo()` | manual `EXTRACT(EPOCH FROM ...)` |

**The only legitimate uses of raw `$__timeFrom()` / `$__timeTo()`** are cases where a macro cannot express the operation:

- **Window clipping** with `LEAST` / `GREATEST` (Pattern C below) — macros don't expose individual bounds inside SELECT expressions
- **`generate_series` bounds** for zero-fill scaffolds when `$__timeGroup` isn't usable
- **Multi-column comparisons** like `start_time < $__timeTo() AND end_time >= $__timeFrom()` for interval-overlap WHERE clauses

In every such case, cast to `timestamptz`: `$__timeTo()::timestamptz`. Document in a SQL comment why the macro wasn't sufficient.

### Rule 2 — Every query must be PostgreSQL and DuckDB compatible

The same SQL string is sent to both engines via different Grafana datasources. Queries must parse and execute correctly on both. This forbids several common Postgres habits.

**Forbidden (Postgres-only or behaves differently in DuckDB):**

| Don't use | Use instead | Why |
|---|---|---|
| `time_bucket('1h', ts)` | `$__timeGroup(ts, $__interval)` | TimescaleDB-only function; not in vanilla Postgres or DuckDB |
| `time_bucket_gapfill(...)` | `generate_series` + `LEFT JOIN` (Pattern D) | TimescaleDB-only |
| `bool_col::int` | `CAST(bool_col AS INTEGER)` | DuckDB rejects implicit bool→int via `::` in some contexts |
| `DISTINCT ON (col)` | `ROW_NUMBER() OVER (PARTITION BY col ORDER BY ...) = 1` | Postgres-only syntax |
| `array_agg(... ORDER BY ...)` with complex sort | `array_agg(... )` over a pre-sorted CTE | Ordering inside aggregates differs |
| `interval '1 day'` (lowercase keyword) | `INTERVAL '1 day'` | DuckDB prefers uppercase; Postgres accepts both |
| `regexp_matches(...)` returning setof | `regexp_extract(...)` (DuckDB) / split via CTE | Set-returning regex differs |
| Implicit `text` ↔ `uuid` comparison | `uuid_col::text = '...'` on both sides | DuckDB is stricter about UUID types |
| `EXTRACT(epoch FROM …)` lowercase `epoch` | `EXTRACT(EPOCH FROM …)` uppercase | DuckDB requires uppercase field name |

**Safe in both (use freely):**

- `$__timeFilter()`, `$__timeGroup()`, `$__timeGroupAlias()`, `$__interval`, `$__unixEpochFrom/To()` — Grafana expands these per-datasource
- `date_trunc('hour', ts)`, `NOW()`, `CURRENT_TIMESTAMP`
- `COALESCE`, `LEAST`, `GREATEST`, `NULLIF`
- `CASE WHEN ... THEN ... ELSE ... END`
- `EXTRACT(EPOCH FROM (ts2 - ts1))`
- `generate_series(start, end, INTERVAL '1 day')`
- `::timestamptz`, `::date`, `::text`, `::numeric` casts
- `FILTER (WHERE ...)` clause on aggregates
- Window functions: `ROW_NUMBER`, `LAG`, `LEAD`, `SUM(...) OVER (...)`
- CTEs (`WITH ... AS`), recursive CTEs
- `||` for string concatenation
- `JOIN`, `LEFT JOIN`, `FULL OUTER JOIN`

**Cross-engine smell test:** if a query uses any TimescaleDB function (`time_bucket*`, `first()`, `last()`, hypertable-specific tooling), it will fail on DuckDB. Replace with macros or generic SQL. If portability genuinely cannot be achieved (e.g. continuous aggregates), call it out in a SQL comment and mark the panel "Postgres-only" in the dashboard JSON description.

**Audit step:** before delivery, mentally run each query against both dialects. Anything Timescale-specific → flag it.

---

## Step 0 — Confirm the schema before writing SQL

Most dashboard rebuilds happen because the first version was built on an assumption about the schema that turned out to be wrong. Before writing any SQL, confirm the basics. The full question bank is in `references/schema_interview.md`; the short version below covers the minimum.

When the user's first message gives you the schema in detail, skip ahead to Step 1. Otherwise, ask explicitly — once, up front, in one consolidated message — for the items below. Don't guess column names from convention.

The minimum to extract before writing the first query:

1. **Domain framing.** What question does this dashboard answer, and who reads it? (Determines tier — manager / analyst / operations.)
2. **Fact table identification.** Which table holds the operational data? Is it a custom relational fact table or a UUID-keyed long-format telemetry table? (Determines archetype.)
3. **Time semantics.** Which column is the canonical timestamp? What's its type (`timestamptz` vs naive `timestamp`)? Can it be NULL or future-dated?
4. **Interval semantics (relational only).** Is the fact interval-shaped (start_time / end_time) or point-shaped (single timestamp)? If interval, what does NULL `end_time` mean — ongoing or abandoned?
5. **Multi-tenancy column.** What's the `account_id` / `tenant_id` / `site_id`? Can the user belong to multiple tenants?
6. **Soft-delete and visibility flags.** Which boolean columns must always be filtered (`is_archived`, `is_active`, `is_ignored`, `is_deleted`)?
7. **KPI definitions.** What are the 3–5 KPIs the user expects, and what's the exact computation for each? "Total downtime" can mean different things — pin down the formula now.
8. **Expected order of magnitude** for each KPI. The user has an opinion ("MTTR is around 45 min for our fleet"); use it as a sanity check after the first draft.

For longer engagements or unfamiliar domains, run the full interview in `references/schema_interview.md` (29 questions across 9 blocks). For quick deliveries, the 8 above are sufficient.

If the user can't answer some of these, the missing answers are exactly the spots where the dashboard will fail later. Flag them explicitly in the response, don't paper over with assumptions.

---

## Step 1 — Identify the data model archetype FIRST

Before writing any SQL, determine which archetype the user's data follows. The two are fundamentally different and use different SQL patterns. Read `references/archetypes.md` for the full decision guide.

### Archetype A — Relational (custom schema)

The user has **domain-specific fact and dimension tables** designed for their use case.

Signs:
- Tables named for entities: `downtime_incidents`, `production_orders`, `quality_checks`, `energy_readings`
- Each fact row has typed columns: `start_time`, `end_time`, `machine_id`, `reason_id`, `quantity`
- Dimensions linked by foreign keys
- Often ORM-generated — Rails / Django / SQLAlchemy patterns visible (`is_archived`, `created_at`, `account_id`)

Use **`references/relational_patterns.sql`** for SQL examples.

### Archetype B — Timeseries (UUID-keyed long-format)

The user has **a single wide telemetry table** where every signal is one row, identified by UUID, with polymorphic value columns.

Canonical schema:

```
telemetry (
  systime         timestamptz,        -- the timestamp
  uuid            uuid,               -- which signal/sensor (the "what")
  value_double    double precision,
  value_integer   bigint,
  value_bool      boolean,
  value_string    text,
  is_delta        char(1)             -- 't' = delta/event, 'f' = state value
)
```

Signs:
- One fact table named `telemetry`, `metrics`, `signals`, `points`, or similar
- A `uuid` (or `signal_id` / `tag_id`) column identifies what's being measured
- Multiple `value_*` columns for different types
- ts-shape, UMH (Unified Manufacturing Hub), Benthos, OPC-UA bridges, MQTT historians all produce this shape
- `is_delta` distinguishes state values (continuous) from event values (discrete deltas)

Use **`references/timeseries_patterns.sql`** for SQL examples.

### Mixed environments

Some users have **both archetypes** — e.g. a relational `downtime_incidents` table (for human-classified events) alongside `telemetry` (for raw machine signals). Build separate queries against each, but normalize through the same dashboard layer (same variables, same time range, same visual conventions).

---

## Step 2 — Pick the dashboard tier(s)

Operations data rarely fits one dashboard. Three audiences, three layouts:

| Tier | Audience | Question | Filters | Panels |
|---|---|---|---|---|
| **Manager** | Plant managers, OPEX, executives | "Where do I send my attention this week?" | None except `$account` | 8–13, fixed window, traffic lights |
| **Analyst** | CI engineers, planners, analysts | "Why did this happen?" | Full filter set, time picker | 20–30+, drill-down, data quality |
| **Operations** | Shift leads, operators | "What's happening right now?" | None | Few, large fonts, live state |

Always ask which tier(s) before building. Don't default to all three. Read `references/dashboard_tiers.md` for the full design rules and example panel inventories.

---

## Step 3 — Apply the universal time-window patterns

These patterns apply **regardless of archetype** — they're about how Grafana time macros interact with PostgreSQL/DuckDB. They are written to honour the two hard rules above.

### Pattern A — Default: `$__timeFilter()` for the WHERE

This is the default time-range filter. It expands correctly on both Postgres and DuckDB datasources and adapts automatically to the panel's time range.

```sql
SELECT ...
FROM <fact_table>
WHERE $__timeFilter(ts_column)
  AND <other filters>
```

**Do not** write `WHERE ts BETWEEN $__timeFrom() AND $__timeTo()` — that bypasses macro expansion and is a Rule 1 violation.

### Pattern B — Bucketed trends: `$__timeGroup()`

Use `$__timeGroup()` (or `$__timeGroupAlias()` when you want the result column named `time` automatically) for any bucketed time series in a SELECT. The bucket size comes from `$__interval`, which Grafana derives from panel width.

```sql
SELECT
  $__timeGroupAlias(ts_column, $__interval) AS time,
  COUNT(*)                                  AS events
FROM <fact_table>
WHERE $__timeFilter(ts_column)
GROUP BY 1
ORDER BY 1;
```

Pin a specific bucket size only when the panel's semantics require it (e.g. shift-based aggregation). In that case, use `$__timeGroup(ts_column, '1h')` with an explicit interval string — still goes through the macro, still works on both engines.

### Pattern C — Window clipping (raw bounds, justified exception)

When summing duration of interval-shaped events against a Grafana time range, partially-overlapping events must be clipped to the visible portion. Otherwise an 8-hour stoppage in a 1-hour view contributes the full 8 hours. This is the **single most-overlooked bug** in homegrown ops dashboards.

`$__timeFilter()` cannot express clipping inside a SELECT expression, so this is a legitimate raw-bounds use. Cast both bounds to `timestamptz`:

```sql
SELECT
  SUM(EXTRACT(EPOCH FROM (
    LEAST   (COALESCE(end_time, NOW()), $__timeTo()::timestamptz)
    - GREATEST(start_time,                $__timeFrom()::timestamptz)
  ))) / 60.0 AS clipped_minutes
FROM downtime_incidents
WHERE start_time      <  $__timeTo()::timestamptz
  AND COALESCE(end_time, NOW()) >= $__timeFrom()::timestamptz
  AND <other filters>;
```

Notes:
- The WHERE here is intentionally **not** `$__timeFilter(start_time)` — that would drop events whose `start_time` precedes the window but whose duration overlaps it. Interval-overlap semantics require the explicit two-column compare.
- Both `LEAST` and `GREATEST` exist in Postgres and DuckDB ✓
- `EXTRACT(EPOCH FROM …)` works in both, with `EPOCH` uppercase

Use this in every duration-summing query. For relational archetype only — timeseries `value_*` rows don't have an `end_time`.

### Pattern D — Coalesce nullable end times (relational archetype only)

When a fact table has `start_time` / `end_time` and `end_time IS NULL` means "still ongoing":

```sql
EXTRACT(EPOCH FROM (COALESCE(end_time, NOW()) - start_time)) / 60.0 AS duration_min
```

Choose between:
- **Coalesce** = ongoing events contribute their elapsed time so far. Default for live/recent panels.
- **Exclude** (`WHERE end_time IS NOT NULL`) = ongoing events excluded. Use for averages, percentiles, MTTR over historical windows.

### Pattern E — Generate complete time series with zero-fill

When daily/hourly trends need zero rows for periods with no events (otherwise gaps mislead). DuckDB has no `time_bucket_gapfill`, so use `generate_series` + `LEFT JOIN` — works identically on both engines:

```sql
WITH buckets AS (
  SELECT generate_series(
    date_trunc('day', $__timeFrom()::timestamptz),
    date_trunc('day', $__timeTo()::timestamptz),
    INTERVAL '1 day'
  ) AS bucket
)
SELECT
  b.bucket            AS time,
  COALESCE(SUM(f.value), 0) AS value
FROM buckets b
LEFT JOIN <fact_table> f
  ON date_trunc('day', f.ts_column) = b.bucket
 AND $__timeFilter(f.ts_column)
GROUP BY b.bucket
ORDER BY b.bucket;
```

Note the macro use: `$__timeFilter` on the join, raw `$__timeFrom/To()::timestamptz` only inside `generate_series` (justified exception — macros don't fit there). Both `generate_series(timestamptz, timestamptz, INTERVAL)` and `date_trunc()` work in Postgres and DuckDB.

For finer buckets (hourly, 5-min), prefer `$__timeGroup()` over manual `date_trunc` unless you specifically need fixed boundaries that don't follow `$__interval`.

---

## Step 4 — Wire variables consistently

Every variable defined must be used in every relevant panel. Defining a variable and not wiring it is a bug. The full reference for variable types, refresh order, the three filter patterns, and the audit checklist is in **`references/variables.md`** — read that for any non-trivial variable wiring. The summary below covers the typical default sets per archetype.

### Relational archetype variables (typical)

```
$account            (query, single)        multi-tenant
$<entity>           (query, multi+all)     e.g. $machine, $line, $department
$<category>         (query, multi+all)     e.g. $reason, $defect_type
$severity           (custom, single+'all') optional severity filter
$min_duration_min   (textbox, default 0)   numeric threshold
$auto_detected      (custom, all/0/1)     source filter
```

### Timeseries archetype variables (typical)

```
$<signal_name>      (query, single+raw)    one variable per UUID needed
                    SELECT name AS __text, uuid AS __value FROM <signal_meta>
                    Use as: uuid = (${signal_name:raw})
$machine            (query, single)        if telemetry is tagged by machine
$bucket             (interval, custom)     1m, 5m, 15m, 1h
```

For timeseries, you typically want **one variable per signal** the dashboard cares about, sourced from a metadata table that maps UUID → human-readable name. If no metadata table exists, hardcode UUIDs in the query and document them in a markdown panel.

### Three reusable filter patterns (also in `variables.md`)

- **Optional sentinel:** `'$severity' = 'all' OR CAST(severity AS TEXT) = '$severity'` — requires "all" option in the variable
- **Integer escape:** `$auto_detected = -1 OR CAST(is_auto_detected AS INTEGER) = $auto_detected` — for tri-state custom variables; uses portable `CAST(... AS INTEGER)` not `::int`
- **NULL preservation:** `(reason_id IN ($reason)) OR reason_id IS NULL` — keeps unclassified rows visible despite filter

Audit before delivery: grep every panel's SQL for each defined variable. If a variable is missing from a panel where it's logically relevant, that's a bug.

---

## Step 5 — Generate JSON via the Python builder

Don't hand-write Grafana panel JSON. Read **`references/dashboard_builder.py`** first — it has helpers for every panel type (`stat`, `table_panel`, `echarts`, `timeseries`, `row`, `text`) plus override builders for table cell coloring, threshold builders, and variable factories.

```python
from dashboard_builder import (
    stat, table_panel, echarts, timeseries, row, text,
    traffic_light, gradient_gauge_override,
    var_query, var_custom, var_textbox, var_uuid_signal,
    build_dashboard,
)

panels = []; pid = 100
panels.append(row(pid, "🎯 KPIs", 0)); pid += 1
panels.append(stat(pid, "Total downtime", 0, 1, 4, 4,
                   sql=sql_total, unit="m",
                   thresholds=traffic_light(yellow=20, red=50))); pid += 1
# ... more panels

dashboard = build_dashboard(
    title="Downtime — Manager View",
    panels=panels,
    variables=[var_query("account", "ACCOUNT", account_sql, multi=False)],
    refresh="5m",
    hide_timepicker=True,
)
```

ECharts panels need two things: SQL must return `format: table` with named columns, and `getOption` JS reads columns by name. **`references/echarts_templates.js`** has 12 reusable templates: Pareto, donut, heatmap, comparison-bars, duration-histogram, gauge, state-timeline (Gantt-style), hourly-output (bar+target+cumulative), scatter-with-control-limits, KPI-card-grid, correlation-lines (dual axis), and stacked-area. Pick by intent — the chart-picking guide is at the bottom of the templates file. Always include the two defensive splash screens (No data / Unexpected data shape).

For timeseries archetype dashboards specifically, when the user gives you natural-language descriptions of signals plus a metadata catalog of UUIDs, read **`references/signal_matching.md`** to translate descriptions into specific UUIDs and panels.

---

## Step 6 — Audit checklist before delivering

- [ ] **JSON validates:** `python3 -c "import json; json.load(open('out.json'))"`
- [ ] **Archetype is consistent** — don't mix relational duration math (`COALESCE(end_time, NOW())`) into timeseries queries that don't have an `end_time`
- [ ] **Every defined variable is used in every relevant panel**
- [ ] **Every duration-summing query uses `LEAST/GREATEST` clipping** (relational only)
- [ ] **Time WHERE clauses use `$__timeFilter()`** — raw `$__timeFrom/To()` only in justified exceptions (clipping, generate_series, interval-overlap), each with a comment
- [ ] **Time bucketing uses `$__timeGroup()` / `$__timeGroupAlias()`** — no `time_bucket()`, no hardcoded `date_trunc('hour', …)` in SELECT for bucketing
- [ ] **Bucket size uses `$__interval`** unless a fixed interval is semantically required
- [ ] **Every raw `$__timeTo()` / `$__timeFrom()` is cast `::timestamptz`**
- [ ] **No TimescaleDB-only functions** (`time_bucket*`, `first()`, `last()`, `locf()`, hypertable management) — replaced with macros or generic SQL
- [ ] **No Postgres-only syntax** (`DISTINCT ON`, `bool_col::int`, lowercase `epoch`) — use portable equivalents
- [ ] **Boolean→integer casts use `CAST(x AS INTEGER)`** not `x::int`
- [ ] **UUID/text comparisons cast both sides** (`uuid_col::text = '...'`)
- [ ] **Every nullable-end-time case is explicit** (coalesce or exclude)
- [ ] **`OR <fk> IS NULL`** preserved wherever filtering on a nullable foreign key
- [ ] **Soft-delete flags** (`is_archived`, `is_active`, `is_ignored`) on every fact-table query
- [ ] **ECharts panels:** SQL `format` is `table`, JS reads columns by name, defensive splash screens included
- [ ] **Time series:** SQL `format` is `time_series`, returns `time` / `metric` / `value` columns
- [ ] **Manager-tier:** `timepicker.hidden = true`, refresh ≥ 5m, traffic-light thresholds set
- [ ] **Schema, plugin, Grafana versions** declared in `__requires`
- [ ] **Datasource UID** uses `${DS_NAME}` placeholder so import dialog asks once
- [ ] **Timeseries archetype:** `${var:raw}` syntax used for UUID variables to avoid quote escaping
- [ ] **Indexes match WHERE shapes** — see `references/performance.md` (the relational fact table has `(start_time)` and per-entity composite indexes; the telemetry table has `(uuid, systime DESC)`)
- [ ] **Performance budget met** — manager < 2s, analyst < 5s, operations < 1s on first load
- [ ] **Portability check passed** — at least 5 representative panels run cleanly on both PG and DuckDB CLIs (see `references/portability_check.md`)
- [ ] **Panel titles follow the convention** `[Tier] <Domain> — <Question>` for analyst dashboards (see `references/dashboard_tiers.md`)
- [ ] **Annotations and alerts** considered for operations / analyst tiers; if added, each has a named owner and a calibrated threshold (see `references/annotations_and_alerts.md`)

---

## Files in this skill

| File | Purpose | When to read |
|---|---|---|
| `SKILL.md` | This file — workflow and decision points | Always |
| `references/schema_interview.md` | Question bank for confirming the schema before writing SQL | Step 0 (full interview); short version is in this SKILL.md |
| `references/archetypes.md` | How to recognize and choose between relational and timeseries | Step 1 |
| `references/relational_patterns.sql` | SQL patterns for fact + dimension models (downtime as worked example) | When archetype = relational |
| `references/timeseries_patterns.sql` | SQL patterns for UUID-keyed long-format telemetry | When archetype = timeseries |
| `references/dashboard_tiers.md` | Manager / analyst / operations tier design rules and naming conventions | Step 2 |
| `references/variables.md` | Variable wiring reference — types, refresh order, filter patterns, audit checklist | Step 4 |
| `references/dashboard_builder.py` | Python helpers for generating Grafana 8.5 panel JSON | Step 5 |
| `references/echarts_templates.js` | 12 ECharts JS templates: Pareto, donut, heatmap, compare-bars, histogram, gauge, state-timeline, hourly-output, scatter-with-limits, KPI-grid, correlation, stacked-area | Step 5 |
| `references/annotations_and_alerts.md` | Annotations and panel-alert patterns for operations and analyst tiers | Step 5 (optional, depending on tier) |
| `references/signal_matching.md` | Translate natural-language descriptions + UUID catalog → specific UUIDs and panels | When archetype = timeseries and user gives descriptions, not UUIDs |
| `references/performance.md` | Indexes, aggregates, hypertable chunk intervals, performance budgets | Step 6 (audit), or any time the dashboard is slow |
| `references/portability_check.md` | Delivery-time procedure for verifying queries on both PG and DuckDB | Step 6 (audit), before final delivery |
| `references/troubleshooting.md` | Error → fix lookup, including DuckDB first-time setup verification | When debugging |
| `references/examples/` | Complete worked-example dashboards (manager + analyst views per archetype) | When you want a concrete model to imitate rather than building from patterns |
| `usage_guide.md` | End-to-end orchestration walkthrough — how to use this skill from a system prompt or Claude Code session | When invoking the skill end-to-end |

Read `archetypes.md` and the matching `*_patterns.sql` early. The other reference files are loaded on-demand based on the task — most relevant when their step is reached, except `troubleshooting.md` and `performance.md` which are pulled in reactively when something goes wrong.

> **Note for reference files:** the two hard rules at the top of this file (macros + PG/DuckDB portability) override anything in `relational_patterns.sql`, `timeseries_patterns.sql`, or `troubleshooting.md`. If a reference snippet uses `time_bucket()`, hardcoded `BETWEEN $__timeFrom() AND $__timeTo()`, or `::int` on a boolean, treat it as outdated and rewrite per the rules above.
