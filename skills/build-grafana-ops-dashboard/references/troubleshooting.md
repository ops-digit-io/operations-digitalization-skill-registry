# Troubleshooting — common errors and fixes

> **Reminder.** Two hard rules from `SKILL.md` apply to every query in this skill:
>
> 1. Use Grafana macros for time (`$__timeFilter`, `$__timeGroup`, `$__interval`). Raw `$__timeFrom()/$__timeTo()` only for window clipping, `generate_series` bounds, and interval-overlap WHERE clauses.
> 2. Every query must run on PostgreSQL **and** DuckDB. No `time_bucket()`, no `bool::int`, no `DISTINCT ON`, no `regr_*()`. Use the portable equivalents.
>
> Most of the errors below are caused by violating one of these rules.

## SQL errors (both archetypes)

### `pq: operator is not unique: unknown - unknown`

**Cause:** Grafana's `$__timeTo()` and `$__timeFrom()` macros expand to **string literals**. PostgreSQL can't subtract two strings — many `-` operators exist, none for text, planner gives up.

**Fix:** Cast both macros to `timestamptz`.

```sql
-- Wrong:
EXTRACT(EPOCH FROM ($__timeTo() - $__timeFrom()))

-- Right:
EXTRACT(EPOCH FROM ($__timeTo()::timestamptz - $__timeFrom()::timestamptz))
```

Apply the cast every time you compare or arithmetic-on a Grafana time macro. The same fix applies to `LEAST(..., $__timeTo())` and `GREATEST(..., $__timeFrom())`.

Better still: ask whether the raw macro is needed at all. Most time-range filters should use `$__timeFilter(column)` and most bucketing should use `$__timeGroup(column, $__interval)` — neither needs casting. See the next entry.

Alternative when only the difference between bounds is needed: use `${__unixEpochTo}` / `${__unixEpochFrom}` which expand to integers and need no cast:

```sql
(${__unixEpochTo} - ${__unixEpochFrom}) / 60.0 AS window_min
```

---

### Same query works in dev (DuckDB) but fails in Grafana (Postgres) — or vice versa

**Cause:** Postgres-only or DuckDB-only syntax slipped in. Common culprits:

| Symptom | Probably… |
|---|---|
| `function time_bucket(...) does not exist` (PG without Timescale) | Use `$__timeGroup(col, $__interval)` |
| `Parser Error: syntax error at or near "DISTINCT"` (DuckDB) | Replace `DISTINCT ON` with `ROW_NUMBER() OVER (PARTITION BY ...) = 1` |
| `Cannot cast BOOLEAN to INTEGER using ::` (DuckDB) | Replace `bool_col::int` with `CAST(bool_col AS INTEGER)` |
| `function regr_slope does not exist` (DuckDB) | Use the manual least-squares CTE pattern in `timeseries_patterns.sql` |
| `LATERAL` query returns wrong rows (DuckDB) | Replace LATERAL nearest-neighbor with bucketed inner-join |
| `Could not interpret EXTRACT field "epoch"` (DuckDB) | Use uppercase: `EXTRACT(EPOCH FROM ...)` |
| Mysterious type mismatch on a UUID compare | Cast both sides: `CAST(col AS TEXT) = '...'` |

**Diagnostic:** open Inspect → Query in Grafana, copy the rendered SQL, paste into a bare DuckDB CLI (or psql) and run. Whichever fails reveals the offending construct.

**Audit before delivery:** grep your panel SQL for `time_bucket`, `DISTINCT ON`, `::int`, `regr_`, `LATERAL`. Each hit is a portability bug.

---

### `IN ($var)` returns no rows when "All" is selected

**Cause:** Grafana expands an empty multi-select to `IN ()` which is invalid SQL. Or the variable hasn't loaded yet.

**Fix:** Either set `includeAll: true` on the variable definition (Grafana auto-expands "All" to all values), or use the optional-filter pattern. For multi-select variables that may legitimately be empty, add a default value or change the panel to handle empty gracefully.

---

### `IN ($var)` hides all NULL-foreign-key rows

**Cause:** `IN (1, 2, 3)` does not match `NULL`. Filtering by any specific category silently drops every row where the foreign key is NULL.

**Fix:** OR the NULL case:

```sql
AND ((di.reason_id IN ($reason)) OR di.reason_id IS NULL)
```

This applies whenever you filter on a nullable foreign key.

---

## SQL errors (relational archetype)

### Numbers don't match between two panels

Almost always one of:

1. **Window clipping inconsistency** — one panel uses `LEAST/GREATEST`, the other doesn't. The unclipped one inflates partially-overlapping events.
2. **Coalesce inconsistency** — one panel does `COALESCE(end_time, NOW())`, the other excludes ongoing events with `WHERE end_time IS NOT NULL`.
3. **Time-filter inconsistency** — one panel uses `$__timeFilter(start_time)`, the other does interval-overlap on both columns. Use the macro for point-in-time filters and the explicit two-column compare only when you need duration overlap.
4. **WHERE clause divergence** — different panels apply different filters. Check that every panel uses the same canonical WHERE.

Pull both queries side by side, diff the WHERE and SUM/AVG expressions character-by-character.

---

### MTBF returns NULL or extreme values

**Cause:** Window/n approximation, where n=0 (no events) divides by zero.

**Fix:** `NULLIF(n, 0)` — divide by null instead of zero, AVG silently skips it.

```sql
AVG(window_min / NULLIF(n, 0))
```

Also: if a machine had only 1 event in a 30-day window, MTBF = 30 days, which dominates the fleet average. Consider a minimum-event threshold for inclusion.

---

## SQL errors (timeseries archetype)

### Query returns zero rows but you know the signal exists

The most common cause is **wrong UUID quoting**. The `:raw` modifier is non-negotiable:

```sql
-- Wrong — Grafana double-quotes the UUID:
WHERE uuid = '$signal_var'

-- Wrong — looks right but quoting is fragile:
WHERE uuid = $signal_var

-- Right:
WHERE uuid = (${signal_var:raw})
```

Without `:raw`, the variable expansion adds quotes around an already-quoted string, and Postgres compares `uuid` to the string `"'<uuid>'"` (quotes included). No error, just zero rows.

**Verify by opening Inspect → Query** — read the actual SQL Grafana sent and check the literal looks like `'<uuid>'` not `''<uuid>''` or `"'<uuid>'"`.

---

### Wrong values returned — counter looks wrong

**Cause:** `is_delta` filter mismatch. State signals (temperature, speed, position) need `is_delta IN ('t', 'f')`. Delta/event signals (counter increments, edge transitions) need `is_delta = 't'` only.

If you include both for a counter, you double-count by reading both the increment events AND the cumulative state samples.

**Quick diagnostic:** add `is_delta` to the SELECT and see what values come back. If you see both 't' and 'f' rows, decide which the signal actually is.

---

### Numeric averages are wrong (always integer)

**Cause:** Integer truncation. `value_integer` is `bigint`, and dividing bigint by anything truncates to int.

**Fix:** Cast to `numeric` before averaging — and use `CAST(... AS NUMERIC)` for portability across PG and DuckDB:

```sql
-- Wrong — truncates:
AVG(COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER))) / 10

-- Right:
AVG(COALESCE(
  CAST(value_double  AS NUMERIC),
  CAST(value_integer AS NUMERIC),
  CAST(CAST(value_bool AS INTEGER) AS NUMERIC)
)) / 10
```

(If you previously wrote `value_bool::integer`, replace it with `CAST(value_bool AS INTEGER)` — see the portability section.)

---

### `time_bucket` errors with "function does not exist"

**Cause:** `time_bucket` is a TimescaleDB-only function. Plain PostgreSQL without the TimescaleDB extension doesn't have it, and DuckDB doesn't have it either. Per Rule 2 of this skill, queries that need to run on both engines cannot use it.

**Fix:** Use Grafana's `$__timeGroup` macro, which expands per datasource and works on both PG and DuckDB:

```sql
-- TimescaleDB-only (DON'T USE IN GRAFANA QUERIES):
time_bucket('1 minute', systime)

-- Portable (always use this):
$__timeGroup(systime, $__interval)        -- bucket size from panel width
$__timeGroup(systime, '1m')               -- explicit fixed bucket
$__timeGroupAlias(systime, $__interval)   -- same, aliases to "time"
```

The only legitimate `time_bucket()` use in this skill is inside DDL for TimescaleDB continuous aggregates (which only exist on Postgres anyway). See `timeseries_patterns.sql` performance notes.

---

### Bitwise CTE fails on DuckDB-over-Parquet adapter

**Cause:** The DuckDB adapter that translates PostgreSQL queries for Parquet files in blob storage doesn't always handle CTEs with bitwise operators well.

**Fix:** Inline the bitwise expressions in the main query without the CTE, or push the bit decoding upstream into ts-shape before storing.

---

### Linear-regression query errors with "function regr_slope does not exist"

**Cause:** PostgreSQL has built-in regression aggregates (`regr_slope`, `regr_intercept`, `regr_r2`). DuckDB does not.

**Fix:** Use the portable manual least-squares CTE pattern in `timeseries_patterns.sql` (LINEAR REGRESSION section). It computes the same numbers using only `AVG`, `SUM`, and `COUNT` — which work on both engines.

---

## Grafana panel errors

### ECharts panel renders blank

**Diagnostic flow:**

1. **Open panel → Inspect → Data tab.** What columns are returned?
2. **Compare to what the JS expects.** Templates read columns by name — `metric`, `value`, `bucket`, `incidents`, etc.
3. **If columns are wrong:** rename in SQL or update the JS column-lookup.
4. **If no rows at all:** the WHERE clause filtered everything out. Common causes:
   - `$severity` left at "critical" with no critical rows
   - `$reason` empty multi-select
   - Time range too narrow
   - For timeseries: `:raw` modifier missing, UUID quoted twice
5. **If rows exist but chart is blank:** the JS may be silently swallowing the data. The defensive splash screens ("No data" / "Unexpected data shape") help here — if you see a blank panel instead of a splash, strip the splashes and check console for JS errors.

---

### ECharts panel pivots wrong with `time_series` format

**Cause:** Older ECharts JS templates assumed Grafana would auto-pivot `(time, metric, value)` rows into separate columns named after the metrics. This works with dense data but fails with sparse data or with sufficient distinct metrics.

**Fix:** Use `format=table` and a non-pivoted query that returns `metric` (text) and `value` (number) columns directly. The JS then iterates rows, not pivoted columns. See `ECHARTS_PARETO_JS` in `references/echarts_templates.js`.

---

### Stat panel shows N/A or NULL

Three causes ranked by likelihood:

1. **Query returned NULL** — happens when summing over no rows, or when `COALESCE(end_time, NOW())` is missing (relational) or the COALESCE chain in `value_*` lookup misses (timeseries).
2. **Wrong column type** — Stat panel's `reduceOptions.fields` is set to a non-numeric column.
3. **`reduceOptions.calcs` set to wrong calc** — defaults to `lastNotNull`, which works for time series but fails for single-row table results. For single-row stats, leave it as `lastNotNull` and ensure the query returns one row, one column.

---

### Panel works in editor but not in dashboard

**Cause:** Variables haven't loaded yet when the panel renders, or the variable depends on another that hasn't resolved.

**Fix:** Check variable `refresh` setting. Set query variables to `refresh: 1` ("On Dashboard Load") or `refresh: 2` ("On Time Range Change"). For chained variables, ensure the dependency is declared correctly.

---

### Dashboard import fails with "Unknown panel type"

**Cause:** A required plugin is not installed on the target Grafana instance. The bilibala-echarts-panel must be installed separately.

**Fix:** Either install the plugin (`grafana-cli plugins install volkovlabs-echarts-panel` or the bilibala equivalent), or rewrite ECharts panels as native Grafana time series / bar gauge / pie chart panels. The `__requires` block in the dashboard JSON declares plugin dependencies — Grafana checks them at import time.

---

## Variable definition errors

### Variable always shows "loading" or empty options

- **Check the SQL** in the variable definition. Run it directly against the database — if it errors there, the variable will silently fail in Grafana.
- **Variable depends on `$account` but `$account` isn't loaded** — set the variable's `refresh` to "On Dashboard Load" and order the variables so dependencies come first in the templating list.
- **Variable returns rows but no options appear** — ensure SQL columns are aliased exactly `__text` and `__value`. Other names (`text`, `value`, `name`, `id`) won't be picked up.

---

## Performance issues

### Dashboard takes >5 seconds to load

In rough order of impact:

1. **Add indexes.**
   - Relational: `(start_time)`, `(machine_id, start_time)`, `(reason_id)`.
   - Timeseries: `(uuid, systime DESC)` is essential — without it, every query scans the whole table.
2. **TimescaleDB hypertables (Postgres only):** make the fact table a hypertable on `start_time` / `systime` if not already. DuckDB equivalent: Parquet partitioning by date.
3. **Continuous aggregates (Postgres only):** for trend panels at multi-month ranges, materialize hourly buckets.
   - Relational: aggregate by `(reason_id, machine_id, hour_bucket)`.
   - Timeseries: aggregate by `(uuid, hour_bucket)` with avg/min/max/count.
   - Grafana panels query the aggregate using `$__timeGroup(bucket, $__interval)` — never `time_bucket()` in the panel SQL.
4. **Reduce ECharts payload:** if a panel returns thousands of rows that get aggregated client-side, move the aggregation into SQL.
5. **Limit drill-down tables:** `LIMIT 500` is plenty. More than that doesn't get scrolled anyway.

---

## When in doubt

The single highest-value debugging action is **opening the panel's Inspect → Query** tab and reading the actual SQL Grafana sent to the database. Variable substitution mistakes account for the majority of "why doesn't this work" cases, and the rendered SQL shows exactly what the database saw.

For timeseries archetype specifically: also look at the rendered UUID literal. If it has weird quoting, `:raw` is missing.

For cross-engine bugs: paste the rendered SQL into both `psql` and the `duckdb` CLI. Whichever errors reveals the non-portable construct.

---

## First-time DuckDB setup verification

Rule 1 in this skill (Grafana macros for time) only works on DuckDB if the DuckDB Grafana datasource plugin actually expands the macros — and not all DuckDB plugins do. Before delivering the first dashboard against a new DuckDB datasource, run this one-time probe to confirm.

### The probe

Create a one-panel dashboard with a `time_series` query targeting any small table on the DuckDB datasource:

```sql
SELECT
  $__timeGroupAlias(systime, $__interval) AS time,
  COUNT(*) AS samples
FROM telemetry
WHERE $__timeFilter(systime)
GROUP BY 1
ORDER BY 1;
```

Open Inspect → Query and read the rendered SQL.

### What to look for

**Macros expanded ✓** — the rendered SQL has actual SQL where the macros were:

```sql
SELECT
  date_trunc('minute', systime) AS time,    -- $__timeGroupAlias expanded
  COUNT(*) AS samples
FROM telemetry
WHERE systime >= '2026-05-01 00:00:00' AND systime < '2026-05-06 00:00:00'  -- $__timeFilter expanded
GROUP BY 1
ORDER BY 1;
```

The exact form of the expansion varies by plugin (some use `date_trunc`, some use `time_bucket`, some use `date_bin`), but the key check is: the dollar-prefixed macros are gone, replaced with real SQL.

**Macros NOT expanded ✗** — the rendered SQL still shows the literal macro text:

```sql
SELECT
  $__timeGroupAlias(systime, $__interval) AS time,
  COUNT(*) AS samples
FROM telemetry
WHERE $__timeFilter(systime)
...
```

If you see this, the plugin doesn't support macros and Rule 1 collapses for this datasource. The dashboard SQL must fall back to manual time bounds:

```sql
WHERE systime >= $__timeFrom()::timestamptz
  AND systime <  $__timeTo()::timestamptz
```

(`$__timeFrom` and `$__timeTo` are usually supported even when the higher-level macros aren't, because they're the simplest form — pure string substitution.)

### What to do with the result

- **Macros work →** proceed normally per the skill's rules. No changes needed.
- **Macros don't work →** flag this for the user. They should either upgrade the DuckDB plugin to a version that supports macros, or you'll need to author dashboard SQL with manual bounds. Pick one and document it in the dashboard description.

This probe takes 2 minutes and saves hours of "why is the panel showing all data instead of the time range I picked" debugging downstream.

---

## DuckDB-specific gotchas beyond macros

A few engine differences worth knowing even when macros work cleanly:

- **`PERCENTILE_CONT` interpolation** can produce values that differ in the last digit between PG and DuckDB on small samples. Round to 1 decimal in panels showing percentiles.
- **NULL ordering** in window functions defaults differently. Specify `NULLS FIRST` or `NULLS LAST` explicitly when ordering matters.
- **String concatenation with NULLs** — DuckDB's `||` returns NULL if either operand is NULL (same as PG). Wrap in `COALESCE` if you want empty-string behavior.
- **Date arithmetic with `INTERVAL`** — both engines handle `ts + INTERVAL '1 day'` correctly, but `ts + 1` (treating numbers as days) works on DuckDB and not PG. Always use the `INTERVAL` form.
