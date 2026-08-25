# performance.md — Making dashboards fast

A slow dashboard is a dashboard people stop opening. This file collects what makes ops dashboards fast and what to do when one isn't.

The two hard rules from `SKILL.md` (macros + PG/DuckDB portability) constrain SQL but don't constrain performance — every recipe below is compatible with both.

---

## Performance budgets

Set explicit targets before delivery. If a dashboard misses these, treat it as a defect.

| Tier | Initial load | Time-range change | Refresh interval |
|---|---|---|---|
| Manager | < 2 s | n/a (window is fixed) | ≥ 5 minutes |
| Analyst | < 5 s | < 3 s | ≥ 30 seconds |
| Operations | < 1 s | n/a (window is fixed) | 10–30 seconds |

These are budgets for the **whole dashboard**, not individual panels. A 20-panel analyst view at 250 ms per panel hits 5 s. That's the ceiling, not a target.

If a dashboard misses budget, you have three levers in this order: indexes, aggregates, query rewrites. Try them in that order; query rewrites are last because they're the most invasive and easiest to get wrong.

---

## Indexes — the highest-leverage fix

Most slow dashboards are slow for one reason: the database is doing a sequential scan because the index doesn't match the WHERE clause shape.

### Relational archetype

The fact table sees four common WHERE shapes. Index for them in this priority:

1. **Time-bounded scans on the primary timestamp** — almost every panel.
   ```sql
   CREATE INDEX ON downtime_incidents (start_time);
   CREATE INDEX ON downtime_incidents (start_time, end_time);  -- if you do interval-overlap
   ```

2. **Per-entity time-bounded scans** — drill-down and ranking panels.
   ```sql
   CREATE INDEX ON downtime_incidents (machine_id, start_time);
   ```

3. **Foreign-key joins** — automatic if the FK has a matching index, which Postgres does NOT create automatically.
   ```sql
   CREATE INDEX ON downtime_incidents (reason_id);
   CREATE INDEX ON downtime_incidents (account_id);
   ```

4. **Soft-delete filters** — included in the canonical WHERE on every panel.
   ```sql
   CREATE INDEX ON downtime_incidents (is_archived) WHERE is_archived = false;
   ```
   The partial index is much smaller than a full one and matches the only filter pattern that ever uses it.

### Timeseries archetype

The single most important index in the entire skill:

```sql
CREATE INDEX ON telemetry (uuid, systime DESC);
```

This is non-negotiable. Without it, every panel does a full-table scan filtered by uuid afterward, and a wide telemetry table is hundreds of millions of rows. With it, every panel does an index seek on uuid then a contiguous scan of the time slice — orders of magnitude faster.

Secondary indexes that pay off:

```sql
CREATE INDEX ON telemetry (systime DESC) WHERE is_delta = 't';
CREATE INDEX ON telemetry (systime DESC) WHERE is_delta = 'f';
```

These help the rare cross-uuid queries (e.g. "show me all events of any signal in the last 5 minutes" — debug panels, system overview).

### Verification

After adding an index, run `EXPLAIN ANALYZE` on the slow query before and after. You're looking for `Index Scan` to replace `Seq Scan` in the plan, and the per-row cost to drop. If it doesn't change, the index doesn't match the WHERE shape — common cause is column order in a multi-column index.

---

## Aggregate tables (Postgres / TimescaleDB only)

DuckDB doesn't have continuous aggregates the same way, so this section is Postgres-specific. The Grafana panel SQL stays portable — it just queries an aggregate table instead of the raw table when one exists.

### When an aggregate pays off

- Trends spanning months at hourly buckets — querying raw rows means scanning millions of samples per panel.
- KPIs computed across an entire fleet — one continuous aggregate maintained incrementally is cheaper than recomputing every refresh.
- Manager-tier dashboards that are read 100x for every write — pre-compute once.

### When NOT to use one

- Analyst-tier panels with arbitrary filters. Aggregates pre-compute one specific shape; panels that filter by reason, severity, etc. can't read from a single aggregate.
- Time ranges shorter than the bucket size. Querying a 1-hour aggregate for a 15-minute panel produces nonsense.
- Dashboards that need second-level resolution.

### Relational example

Hourly per-(machine, reason) downtime totals:

```sql
CREATE MATERIALIZED VIEW downtime_hourly
WITH (timescaledb.continuous) AS
SELECT
  time_bucket('1 hour', start_time) AS bucket,
  machine_id,
  reason_id,
  COUNT(*) AS incidents,
  SUM(EXTRACT(EPOCH FROM (COALESCE(end_time, NOW()) - start_time)) / 60.0) AS minutes
FROM downtime_incidents
WHERE is_archived = false
GROUP BY bucket, machine_id, reason_id;

SELECT add_continuous_aggregate_policy('downtime_hourly',
  start_offset => INTERVAL '7 days',
  end_offset   => INTERVAL '1 hour',
  schedule_interval => INTERVAL '1 hour');
```

Note: `time_bucket()` in the DDL is the *only* legitimate use in this skill — it's TimescaleDB's continuous-aggregate machinery, not portable query SQL.

The Grafana panel queries this aggregate using `$__timeGroup(bucket, $__interval)` like any other table. The panel SQL itself remains portable.

### Timeseries example

Hourly avg / min / max / count per UUID:

```sql
CREATE MATERIALIZED VIEW telemetry_1h
WITH (timescaledb.continuous) AS
SELECT
  uuid,
  time_bucket('1 hour', systime) AS bucket,
  AVG(COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER))) AS avg_val,
  MIN(COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER))) AS min_val,
  MAX(COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER))) AS max_val,
  COUNT(*) AS samples
FROM telemetry
WHERE is_delta IN ('t', 'f')
GROUP BY uuid, bucket;
```

Trend panels at multi-week ranges should read from `telemetry_1h` instead of `telemetry`. Drill-down panels at the second-level still read from `telemetry`.

---

## Hypertable chunk intervals

For TimescaleDB hypertables, `chunk_time_interval` controls how the underlying data is partitioned. Right-sizing it speeds up time-bounded queries because Postgres can prune entire chunks instead of scanning them.

Rule of thumb: chunks should be sized so that **a few chunks** cover the typical query time range. Not one — a few — so that pruning eliminates most data, but the query doesn't have to open hundreds of files.

| Sample frequency | Suggested chunk_time_interval |
|---|---|
| Sub-second (high-frequency PLC) | 6 hours to 1 day |
| Per-minute | 1 day to 1 week |
| Per-hour | 1 week |
| Per-day or coarser | 1 month |

Set it at hypertable creation:

```sql
SELECT create_hypertable('telemetry', 'systime',
  chunk_time_interval => INTERVAL '1 day');
```

Changing it later only affects new chunks; existing chunks keep their original size.

### DuckDB equivalent

DuckDB has no hypertables. The equivalent is Parquet partitioning when you write the underlying file:

```sql
COPY telemetry TO 'telemetry/' (FORMAT PARQUET, PARTITION_BY (year, month));
```

Then query with `read_parquet('telemetry/year=*/month=*/*.parquet')`. Partition pruning happens at the file-listing level. Match the partition granularity to the same rule of thumb above.

---

## Reducing payload to the browser

Even with fast SQL, large result sets choke ECharts.

- **Bucket aggressively.** A 1-hour panel with 1-minute buckets is 60 rows. With 1-second buckets, 3600. ECharts handles 60 fine; 3600 lags. Use `$__interval` so the bucket size scales with panel width — Grafana picks 1 row per visual pixel.
- **Limit drill-down tables.** `LIMIT 500` or less. Nobody scrolls past 500 rows.
- **Pre-aggregate Pareto charts.** A Pareto over 10,000 distinct categories is unreadable. Add `LIMIT 20` and an "Other" bucket if needed.
- **Avoid GROUP BY on high-cardinality strings without filtering first.** Group by 100k UUIDs returns 100k rows.

---

## Diagnostic flow when a dashboard is slow

1. **Identify the slow panel.** Open Inspect → Stats. Each panel shows its query duration. Sort by duration; the slowest one or two account for most of the dashboard time.

2. **Read the query.** Inspect → Query. Copy the rendered SQL.

3. **`EXPLAIN ANALYZE` the query.** Look for sequential scans, large row counts at intermediate steps, and operations whose actual time is much higher than estimated.

4. **Try the levers in order:**
   - Missing index? Add one.
   - Wide time range and aggregate exists? Switch the panel to query the aggregate.
   - Big intermediate row count? Push filters down (move WHERE before any aggregation in CTEs).
   - Window-clipping calculation evaluating against millions of rows? Pre-filter to overlapping rows first, clip in a CTE.

5. **Re-test.** Repeat from step 1. The previously second-slowest panel is now slowest.

6. **Stop when budget is met.** Don't over-optimize; budgets exist so you know when to stop.

---

## Performance anti-patterns

These show up repeatedly and each one costs an order of magnitude:

- **Computing duration in the WHERE clause.** `WHERE EXTRACT(EPOCH FROM (end_time - start_time)) / 60 > 5` — kills index use because the expression isn't sargable. Move the threshold filter to a HAVING after the aggregation, or store duration as a generated column.

- **Joining the fact table to itself for prev/next-row patterns.** Use `LAG()` / `LEAD()` window functions instead — one pass over the data instead of a self-join.

- **Selecting `*` from the fact table** in CTEs that only need 3 columns. Postgres can't always project away unused columns through CTEs and pulls everything.

- **`COUNT(DISTINCT col)` over high-cardinality columns** every refresh. If the answer doesn't change much (active machines this month), put it in a Stat panel with a long refresh interval, or cache it in a small lookup table updated nightly.

- **Querying raw telemetry for multi-month trends** when an hourly aggregate exists. Just switch the panel.

- **No `ORDER BY` on time series.** Grafana's renderer assumes ascending time. Without `ORDER BY 1` you sometimes get scribble lines.

- **Over-broad time ranges left as default.** Setting `from: now-90d` as the dashboard default is a hostile choice — every reload runs 90-day queries.
