# portability_check.md — Verify queries on both engines before delivery

Rule 2 from `SKILL.md` says every query must run on PostgreSQL **and** DuckDB. This file describes how to test that — turning the rule from aspiration into a verifiable check.

The goal: find portability bugs at delivery time, not after the dashboard has been imported and someone hits a panel that errors.

---

## When to run this check

- **Always**, before delivery, if the dashboard is intended to run against both engines.
- After any non-trivial SQL edit — adding a new panel, changing a CTE shape, introducing a new function.
- Once per quarter on existing dashboards as a regression check.

The check takes roughly 10 minutes for a typical 15-panel dashboard. Skipping it means trusting that nothing slipped past the audit checklist, which is a worse trade than 10 minutes.

---

## What you need

- The dashboard JSON file
- A Postgres instance with the dashboard's schema and some representative data
- A DuckDB instance with the same schema and the same data (or close enough that row counts match within an order of magnitude)
- The `psql` and `duckdb` CLIs

If the data warehouses are large, sample down: a 1-million-row sample of `downtime_incidents` is plenty for portability checking. The point is to exercise the SQL shape, not to produce business-correct numbers.

---

## The procedure

### Step 1 — Pick representative panels

A 15-panel dashboard doesn't need 15 separate tests. Pick the panels that exercise distinct SQL shapes:

- **One stat panel** — exercises basic SELECT + window-clipping
- **One time-series panel** — exercises `$__timeGroup`, GROUP BY
- **One ECharts panel** — exercises CTEs and aggregation
- **One ranking table** — exercises JOINs and ORDER BY
- **One drill-down detail table** — exercises COALESCE, CASE, multi-table JOINs

Five queries cover the ground for most dashboards. If the dashboard has unusual SQL (recursive CTEs, regex, regression aggregates), add those panels too.

### Step 2 — Render the SQL through Grafana

Open each chosen panel → Inspect → Query. Copy the rendered SQL — the version with macros expanded by Grafana, with literal values substituted in for variables.

This is the SQL that actually hit the database. Test that, not the unexpanded source SQL — macro expansion is one of the things you're checking.

### Step 3 — Run on both engines

Save each query to a file: `panel_01.sql`, `panel_02.sql`, etc. Then run on each engine:

```bash
psql   -h pg-host -d ops -f panel_01.sql > panel_01.pg.txt
duckdb ops.duckdb < panel_01.sql        > panel_01.duck.txt
```

Diff the outputs:

```bash
diff panel_01.pg.txt panel_01.duck.txt
```

Three possible outcomes:

1. **Identical output.** Pass.
2. **Different but tolerable** (row order, NULL representation, decimal precision). Note it, move on.
3. **One side errors, the other succeeds.** Fail. This is what the check is designed to catch.

### Step 4 — Fix or document

For each failure:

- If the failure is a portability bug — `time_bucket()`, `DISTINCT ON`, `bool::int`, `regr_*`, lowercase `epoch` — fix the SQL per the rules in `SKILL.md` and re-run.
- If the failure is fundamental and can't be made portable (continuous-aggregate-only patterns, vendor-specific functions you genuinely need), mark the panel "Postgres-only" or "DuckDB-only" in the dashboard description. Better to be explicit than to silently break.

---

## Expected differences that are NOT portability bugs

Some output differences are normal and don't need fixing. Recognize them so you don't chase ghosts:

| Difference | Why | What to do |
|---|---|---|
| Row order varies on un-`ORDER BY`'d queries | Both engines pick whatever order the query plan produced | Add `ORDER BY` if order matters (it usually does for charts) |
| NULL renders as `(null)` in psql, empty in duckdb | CLI defaults differ | Cosmetic, ignore |
| Decimal precision differs by 1 digit on AVG / division | Different default precision rules | Wrap aggregates in `ROUND(..., n)` if reproducibility matters |
| Timezone display differs (`+02` vs `+02:00`) | Format defaults | Cosmetic, ignore |
| Boolean renders as `t`/`f` vs `true`/`false` | Output format defaults | Cosmetic; if a panel parses booleans, normalize with `CAST(... AS TEXT)` |
| Slight numeric differences in PERCENTILE_CONT on small samples | Different interpolation | If panels show percentiles, use larger samples or document the engine choice |

---

## Common bugs the check catches

Listed in rough frequency order from real dashboards:

1. **`bool_col::int`** somewhere in a derived metric. Fix: `CAST(bool_col AS INTEGER)`.
2. **`time_bucket()` snuck in** — usually copy-pasted from older TimescaleDB material. Fix: `$__timeGroup(col, $__interval)`.
3. **`DISTINCT ON`** in a "top N per group" query. Fix: `ROW_NUMBER() OVER (PARTITION BY ...) = 1` in a subquery.
4. **lowercase `epoch`** in `EXTRACT`. Fix: uppercase it.
5. **`regr_slope` / `regr_intercept` / `regr_r2`** in trend-projection panels. Fix: use the manual least-squares CTE in `timeseries_patterns.sql`.
6. **Implicit text↔uuid comparisons** that work in PG but error in DuckDB. Fix: cast both sides to text.
7. **`array_agg(x ORDER BY y)`** patterns that don't translate cleanly. Fix: pre-sort in a CTE, then `array_agg` without the ordered clause.

A clean dashboard hits zero of these. One or two slips through on most first deliveries.

---

## A concrete worked example

### Bug

```sql
SELECT
  m.name AS machine,
  SUM(CASE WHEN di.is_auto_detected::int = 1 THEN 1 ELSE 0 END) AS auto_count
FROM downtime_incidents di
JOIN machines m ON m.id = di.machine_id
WHERE $__timeFilter(di.start_time)
GROUP BY m.name
ORDER BY auto_count DESC;
```

### Run on Postgres

Returns rows. ✓

### Run on DuckDB

```
Binder Error: No function matches the given name and argument types
'cast(BOOLEAN AS INTEGER)' — note the explicit form is required.
```

### Fix

```sql
SELECT
  m.name AS machine,
  SUM(CASE WHEN CAST(di.is_auto_detected AS INTEGER) = 1 THEN 1 ELSE 0 END) AS auto_count
FROM downtime_incidents di
JOIN machines m ON m.id = di.machine_id
WHERE $__timeFilter(di.start_time)
GROUP BY m.name
ORDER BY auto_count DESC;
```

### Re-run on both

Identical output. ✓

---

## Automating the check

For dashboards under continuous development, a simple bash loop covers it. Save as `portability_check.sh` next to the dashboard JSON:

```bash
#!/usr/bin/env bash
set -euo pipefail
PANELS_DIR=${1:-./panels}
fail=0
for sql in "$PANELS_DIR"/*.sql; do
  name=$(basename "$sql" .sql)
  psql   -h "$PGHOST" -d "$PGDATABASE" -f "$sql" > "/tmp/$name.pg.txt"   2>"/tmp/$name.pg.err"   || true
  duckdb "$DUCKDB_FILE" < "$sql"                 > "/tmp/$name.duck.txt" 2>"/tmp/$name.duck.err" || true
  if [ -s "/tmp/$name.pg.err" ] || [ -s "/tmp/$name.duck.err" ]; then
    echo "FAIL: $name"
    head -5 "/tmp/$name.pg.err" "/tmp/$name.duck.err"
    fail=1
  fi
done
exit $fail
```

Run it before any commit that touches dashboard SQL. Failed delivery is more expensive than 10 seconds in CI.
