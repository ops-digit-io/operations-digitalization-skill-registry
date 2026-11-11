-- ============================================================================
-- timeseries_patterns.sql — SQL for UUID-keyed long-format telemetry
-- (ts-shape / UMH / OPC-UA bridge / MQTT historian schemas)
--
-- HARD RULES (see SKILL.md):
--   1. Use Grafana macros for time. Default to $__timeFilter() in WHERE
--      and $__timeGroup()/$__timeGroupAlias() in SELECT. Raw $__timeFrom()/
--      $__timeTo() are allowed only for window clipping, generate_series
--      bounds, and interval-overlap WHERE clauses.
--   2. Every query must run on PostgreSQL AND DuckDB. No time_bucket(),
--      no bool::int casts, no Postgres-only regr_*() — use the portable
--      equivalents shown here.
--
-- Read this when archetype = timeseries.
-- ============================================================================

-- ----------------------------------------------------------------------------
-- ASSUMED SCHEMA (adapt names to user's actual table)
-- ----------------------------------------------------------------------------
-- CREATE TABLE telemetry (
--   systime         timestamptz NOT NULL,   -- the timestamp (event time)
--   uuid            uuid        NOT NULL,   -- which signal/sensor
--   value_double    double precision,       -- analog reading
--   value_integer   bigint,                 -- counter, integer state
--   value_bool      boolean,                -- digital flag
--   value_string    text,                   -- string label (partnumber, status)
--   is_delta        char(1)                 -- 't' = event/delta, 'f' = state
-- );
-- CREATE INDEX ON telemetry (uuid, systime DESC);


-- ============================================================================
-- THE READ PATTERN — apply to every value extraction
-- ============================================================================

-- The polymorphic value column means you always read all four. COALESCE picks
-- whichever is populated for this signal type.
--
-- Use CAST(value_bool AS INTEGER) — the Postgres `value_bool::integer` shorthand
-- is rejected by DuckDB in some contexts. CAST is portable across both.

COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) AS value

-- For string signals (partnumbers, status labels), use value_string explicitly.
-- For numeric averaging, cast to numeric (or DOUBLE in DuckDB — both accept
-- NUMERIC) to avoid integer truncation:
COALESCE(
  CAST(value_double  AS NUMERIC),
  CAST(value_integer AS NUMERIC),
  CAST(CAST(value_bool AS INTEGER) AS NUMERIC)
)

-- The is_delta filter:
--   is_delta IN ('t', 'f')   -- include both state samples AND event/delta rows
--   is_delta = 't'           -- ONLY events/deltas (counters, edge transitions)
--   is_delta = 'f'           -- ONLY state samples (continuous values)
-- When in doubt: state values like temperature, speed, position use ('t','f').
-- Delta values like "OK part counter increment" use 't' only.


-- ============================================================================
-- VARIABLE INJECTION FOR UUIDs
-- ============================================================================

-- Always use the :raw modifier to avoid Grafana quoting the UUID as a string.
-- Also wrap in parens — convention from existing dashboards.

uuid = (${signal_var:raw})

-- Variable definition for the dropdown:
SELECT name AS __text, uuid AS __value
FROM signal_metadata
WHERE machine_id IN ($machine)        -- if metadata has machine FK
ORDER BY name;


-- ============================================================================
-- READ A SINGLE SIGNAL AS A TIME SERIES (the most common query)
-- Returns: time, value — Grafana auto-renders as a line/bar chart.
-- Format: time_series
-- ============================================================================

SELECT
  systime AS "time",
  COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) AS "Signal Display Name"
FROM telemetry
WHERE
  $__timeFilter(systime)
  AND uuid = (${signal_var:raw})
  AND is_delta IN ('t', 'f')
ORDER BY 1;


-- ============================================================================
-- BUCKETED AGGREGATE (for stat panels and trend overlays)
--
-- ALWAYS use $__timeGroup() — never time_bucket(). $__timeGroup expands per
-- datasource (PostgreSQL → date_bin/date_trunc, DuckDB plugin → date_trunc),
-- so the same SQL works on both engines. time_bucket() is TimescaleDB-only.
-- ============================================================================

-- Average per bucket (interval comes from $__interval, set by panel width)
SELECT
  $__timeGroupAlias(systime, $__interval) AS time,
  AVG(COALESCE(
    CAST(value_double  AS NUMERIC),
    CAST(value_integer AS NUMERIC),
    CAST(CAST(value_bool AS INTEGER) AS NUMERIC)
  )) AS "Avg"
FROM telemetry
WHERE $__timeFilter(systime)
  AND uuid = (${signal_var:raw})
  AND is_delta = 't'
GROUP BY 1
ORDER BY 1;

-- Need a fixed bucket size? Pass an explicit interval string — still through
-- the macro, still portable:
--   $__timeGroup(systime, '1m')     -- 1-minute buckets, ignores panel width

-- Single overall average for a Stat panel (no bucket)
SELECT
  AVG(COALESCE(
    CAST(value_double  AS NUMERIC),
    CAST(value_integer AS NUMERIC),
    CAST(CAST(value_bool AS INTEGER) AS NUMERIC)
  )) AS "Avg Value"
FROM telemetry
WHERE $__timeFilter(systime)
  AND uuid = (${signal_var:raw})
  AND is_delta = 't';

-- Latest value
SELECT
  COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) AS "Current Value"
FROM telemetry
WHERE uuid = (${signal_var:raw})
  AND is_delta IN ('t', 'f')
ORDER BY systime DESC
LIMIT 1;


-- ============================================================================
-- JOIN TWO SIGNALS ON TIME BUCKET
-- Use when comparing or correlating two parameters.
-- ============================================================================

-- Tight alignment: bucket both signals to the same interval and inner-join.
WITH a AS (
  SELECT $__timeGroup(systime, '1s') AS ts,
         COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) AS val
  FROM telemetry
  WHERE $__timeFilter(systime)
    AND uuid = (${signal_a:raw})
    AND is_delta IN ('t', 'f')
),
b AS (
  SELECT $__timeGroup(systime, '1s') AS ts,
         COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) AS val
  FROM telemetry
  WHERE $__timeFilter(systime)
    AND uuid = (${signal_b:raw})
    AND is_delta IN ('t', 'f')
)
SELECT
  a.ts AS time,
  a.val AS "Signal A",
  b.val AS "Signal B"
FROM a INNER JOIN b ON a.ts = b.ts
ORDER BY a.ts;

-- Loose alignment: signal samples don't share exact timestamps. The Postgres
-- pattern uses LEFT JOIN LATERAL, which DuckDB also supports — but the syntax
-- inside (especially correlated subqueries) is more brittle on DuckDB.
-- Portable alternative: bucket both signals to the same coarse interval and
-- inner-join (preferred). Only fall back to LATERAL when the bucket trick
-- loses too much resolution.
--
-- Bucketed loose-alignment pattern (portable):
WITH a AS (
  SELECT $__timeGroup(systime, '5s') AS ts,
         AVG(COALESCE(
           CAST(value_double  AS NUMERIC),
           CAST(value_integer AS NUMERIC),
           CAST(CAST(value_bool AS INTEGER) AS NUMERIC)
         )) AS val
  FROM telemetry
  WHERE $__timeFilter(systime)
    AND uuid = (${signal_a:raw})
    AND is_delta IN ('t', 'f')
  GROUP BY 1
),
b AS (
  SELECT $__timeGroup(systime, '5s') AS ts,
         AVG(COALESCE(
           CAST(value_double  AS NUMERIC),
           CAST(value_integer AS NUMERIC),
           CAST(CAST(value_bool AS INTEGER) AS NUMERIC)
         )) AS val
  FROM telemetry
  WHERE $__timeFilter(systime)
    AND uuid = (${signal_b:raw})
    AND is_delta IN ('t', 'f')
  GROUP BY 1
)
SELECT a.ts AS time, a.val AS "Signal A", b.val AS "Signal B (averaged)"
FROM a LEFT JOIN b ON a.ts = b.ts
ORDER BY a.ts;


-- ============================================================================
-- COUNTER RESET HANDLING (production counters that reset to 0)
-- Window functions (LAG, SUM OVER) work on both PG and DuckDB.
-- ============================================================================

-- Detect resets and compute monotonically-increasing total
WITH raw AS (
  SELECT
    systime,
    COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) AS val,
    LAG(COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)))
      OVER (ORDER BY systime) AS prev_val
  FROM telemetry
  WHERE $__timeFilter(systime)
    AND uuid = (${counter_signal:raw})
    AND is_delta = 't'
),
deltas AS (
  SELECT
    systime,
    val,
    CASE
      WHEN prev_val IS NULL OR val < prev_val THEN val   -- reset detected
      ELSE val - prev_val
    END AS delta
  FROM raw
)
SELECT
  systime AS time,
  SUM(delta) OVER (ORDER BY systime) AS "Cumulative count"
FROM deltas
ORDER BY systime;


-- ============================================================================
-- STATE DURATION (sum time spent in each state value)
-- Use for "time machine spent in state X" — running, idle, fault, etc.
-- The window-clipping pattern (LEAST/GREATEST with raw $__timeTo/From bounds)
-- is the same justified exception as in the relational archetype.
-- ============================================================================

WITH state_changes AS (
  SELECT
    systime,
    COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) AS state,
    LEAD(systime) OVER (ORDER BY systime) AS next_systime
  FROM telemetry
  WHERE $__timeFilter(systime)
    AND uuid = (${state_signal:raw})
    AND is_delta IN ('t', 'f')
),
durations AS (
  SELECT
    state,
    SUM(EXTRACT(EPOCH FROM (
      LEAST(COALESCE(next_systime, NOW()), $__timeTo()::timestamptz)
      - GREATEST(systime, $__timeFrom()::timestamptz)
    ))) / 60.0 AS minutes_in_state
  FROM state_changes
  -- Interval-overlap WHERE — justified raw-bound use:
  WHERE systime < $__timeTo()::timestamptz
    AND COALESCE(next_systime, NOW()) >= $__timeFrom()::timestamptz
  GROUP BY state
)
SELECT
  CAST(state AS TEXT) AS state,
  ROUND(CAST(minutes_in_state AS NUMERIC), 1) AS "Minutes"
FROM durations
ORDER BY minutes_in_state DESC;

-- This pattern — derive intervals from successive state samples, then clip them
-- to the Grafana window with LEAST/GREATEST — is the timeseries equivalent of
-- the relational `start_time/end_time` pattern. Same window-clipping rules apply.


-- ============================================================================
-- THRESHOLD / RANGE MAPPING (continuous signal → categorical state)
-- Example: speed signal where >20 = Running, <=20 = Not Running
-- ============================================================================

SELECT
  $__timeGroupAlias(systime, '1m') AS time,
  CASE
    WHEN COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) > 20 THEN 'Running'
    ELSE 'Not Running'
  END AS state,
  COUNT(*) AS samples
FROM telemetry
WHERE $__timeFilter(systime)
  AND uuid = (${speed_signal:raw})
  AND is_delta IN ('t', 'f')
GROUP BY 1, 2
ORDER BY 1;

-- For total time in each state, leverage the 1-minute bucketing trick: each
-- bucketed row represents one minute, so COUNT(*) = minutes.
WITH bucketed AS (
  SELECT
    $__timeGroup(systime, '1m') AS bucket,
    COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) AS val
  FROM telemetry
  WHERE $__timeFilter(systime)
    AND uuid = (${speed_signal:raw})
    AND is_delta IN ('t', 'f')
)
SELECT
  CASE WHEN val > 20 THEN 'Running' ELSE 'Not Running' END AS state,
  COUNT(*) AS minutes
FROM bucketed
GROUP BY 1;


-- ============================================================================
-- BITWISE FLAG DECODING (PLC packed flags into a single integer)
-- Useful for digital input/output groups, alarm bitmasks
--
-- Bitwise & operates on integers in both PG and DuckDB.
-- ============================================================================

WITH t AS (
  SELECT systime, value_integer AS v
  FROM telemetry
  WHERE $__timeFilter(systime)
    AND uuid = (${packed_flags_signal:raw})
    AND is_delta IN ('t', 'f')
)
SELECT
  systime AS time,
  CASE WHEN (v & 1)   > 0 THEN 1 ELSE 0 END AS "Bit 0: Position OK",
  CASE WHEN (v & 2)   > 0 THEN 1 ELSE 0 END AS "Bit 1: Tool Present",
  CASE WHEN (v & 4)   > 0 THEN 1 ELSE 0 END AS "Bit 2: Fault Active",
  CASE WHEN (v & 8)   > 0 THEN 1 ELSE 0 END AS "Bit 3: Cycle Complete",
  CASE WHEN (v & 16)  > 0 THEN 1 ELSE 0 END AS "Bit 4: Spare 1",
  CASE WHEN (v & 32)  > 0 THEN 1 ELSE 0 END AS "Bit 5: Spare 2",
  CASE WHEN (v & 64)  > 0 THEN 1 ELSE 0 END AS "Bit 6: Spare 3",
  CASE WHEN (v & 128) > 0 THEN 1 ELSE 0 END AS "Bit 7: Spare 4"
FROM t
ORDER BY time DESC;

-- Note: the CTE-with-bitwise pattern can fail on a DuckDB-over-Parquet adapter
-- (translation issues). If targeting that, inline the value column without
-- the CTE.


-- ============================================================================
-- SHIFT-CLIPPED AGGREGATES (only count data inside production shift windows)
-- ============================================================================

-- Filter samples to weekday hours 06:00–14:00 and count not-running minutes.
-- EXTRACT(HOUR FROM ...) and EXTRACT(DOW FROM ...) work on both engines.
-- Note: keep EXTRACT field names UPPERCASE — DuckDB requires it.
WITH bucketed AS (
  SELECT
    $__timeGroup(systime, '1m') AS bucket,
    COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) AS val
  FROM telemetry
  WHERE $__timeFilter(systime)
    AND uuid = (${speed_signal:raw})
    AND is_delta IN ('t', 'f')
    AND EXTRACT(HOUR FROM systime) >= 6
    AND EXTRACT(HOUR FROM systime) < 14
    AND EXTRACT(DOW  FROM systime) BETWEEN 1 AND 5    -- Mon–Fri
)
SELECT
  CAST(bucket AS DATE)              AS "Date",
  COUNT(*) FILTER (WHERE val < 20)  AS "Not Running (min)",
  COUNT(*) FILTER (WHERE val >= 20) AS "Running (min)"
FROM bucketed
GROUP BY CAST(bucket AS DATE)
ORDER BY CAST(bucket AS DATE);

-- For more sophisticated shift logic (DST-aware, multi-shift, calendar-driven),
-- consider doing the clipping in ts-shape (ShiftClipper / ShiftConfig) before
-- materializing to a continuous aggregate, then querying that.


-- ============================================================================
-- RATE OF CHANGE / DERIVATIVE
-- LAG window functions work in both PG and DuckDB.
-- ============================================================================

WITH samples AS (
  SELECT
    systime,
    COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) AS val,
    LAG(systime) OVER (ORDER BY systime) AS prev_t,
    LAG(COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)))
      OVER (ORDER BY systime) AS prev_val
  FROM telemetry
  WHERE $__timeFilter(systime)
    AND uuid = (${signal_var:raw})
    AND is_delta IN ('t', 'f')
)
SELECT
  systime AS time,
  CASE
    WHEN prev_t IS NULL THEN NULL
    WHEN systime = prev_t THEN NULL
    ELSE (val - prev_val) / EXTRACT(EPOCH FROM (systime - prev_t))
  END AS "Rate per second"
FROM samples
ORDER BY systime;


-- ============================================================================
-- LINEAR REGRESSION FOR ETA / TREND PROJECTION
-- Useful for predicting "when will this counter reach 0" — spool depletion,
-- battery drain, fluid levels, etc.
--
-- IMPORTANT: PostgreSQL's regr_slope / regr_intercept / regr_r2 aggregates
-- DO NOT exist in DuckDB. The portable version below computes the same
-- least-squares regression by hand using only AVG, SUM, and COUNT — works
-- on both engines.
-- ============================================================================

WITH joined AS (
  SELECT
    EXTRACT(EPOCH FROM $__timeGroup(systime, '1s')) AS t_sec,
    COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) AS val
  FROM telemetry
  WHERE systime > NOW() - INTERVAL '5 minutes'
    AND uuid = (${signal_var:raw})
    AND is_delta IN ('t', 'f')
),
stats AS (
  SELECT
    AVG(t_sec)                        AS t_mean,
    AVG(val)                          AS v_mean,
    SUM(t_sec * val)                  AS sum_tv,
    SUM(t_sec * t_sec)                AS sum_tt,
    SUM(val   * val)                  AS sum_vv,
    COUNT(*)                          AS n
  FROM joined
),
regression AS (
  SELECT
    -- slope = (n*Σtv - Σt*Σv) / (n*Σtt - (Σt)^2)
    --       = (Σtv - n*t_mean*v_mean) / (Σtt - n*t_mean^2)
    CASE WHEN (sum_tt - n * t_mean * t_mean) = 0 THEN NULL
         ELSE (sum_tv - n * t_mean * v_mean)
            / (sum_tt - n * t_mean * t_mean)
    END AS slope,
    v_mean AS v_mean,
    t_mean AS t_mean,
    sum_tt, sum_vv, sum_tv, n
  FROM stats
),
fit AS (
  SELECT
    slope,
    v_mean - slope * t_mean AS intercept,
    -- r² = (n*Σtv - Σt*Σv)^2 / ((n*Σtt - (Σt)^2)(n*Σvv - (Σv)^2))
    CASE
      WHEN (sum_tt - n * t_mean * t_mean) = 0
        OR (sum_vv - n * v_mean * v_mean) = 0 THEN NULL
      ELSE (sum_tv - n * t_mean * v_mean)
         * (sum_tv - n * t_mean * v_mean)
         / NULLIF((sum_tt - n * t_mean * t_mean)
                * (sum_vv - n * v_mean * v_mean), 0)
    END AS r_squared,
    n AS sample_count
  FROM regression
),
current_state AS (
  SELECT val AS current_val, t_sec AS current_t
  FROM joined
  ORDER BY t_sec DESC
  LIMIT 1
)
SELECT
  cs.current_val            AS current_value,
  f.slope * 60.0             AS slope_per_minute,
  f.r_squared                AS fit_quality,
  CASE
    WHEN f.slope < 0 AND f.sample_count >= 10
    THEN -cs.current_val / f.slope / 60.0
    ELSE NULL
  END                        AS eta_minutes,
  CASE
    WHEN f.slope < 0 AND f.sample_count >= 10
    THEN TO_TIMESTAMP(-f.intercept / f.slope)
    ELSE NULL
  END                        AS eta_timestamp
FROM current_state cs, fit f;

-- Note: slope is dy/dt (val per second), so a negative slope means decreasing
-- value. Double-check sign before trusting any ETA estimate.


-- ============================================================================
-- KPI QUERIES — single-value stats for the timeseries archetype
-- ============================================================================

-- Total events (e.g. counter increments) in window
SELECT COUNT(*) AS event_count
FROM telemetry
WHERE $__timeFilter(systime)
  AND uuid = (${counter_signal:raw})
  AND is_delta = 't';

-- Sum of incremented values (e.g. total OK parts produced)
SELECT
  SUM(COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER))) AS total
FROM telemetry
WHERE $__timeFilter(systime)
  AND uuid = (${counter_signal:raw})
  AND is_delta = 't';

-- Min / Max / P95 of a state signal
SELECT
  MIN(COALESCE(CAST(value_double AS NUMERIC), CAST(value_integer AS NUMERIC))) AS min_val,
  MAX(COALESCE(CAST(value_double AS NUMERIC), CAST(value_integer AS NUMERIC))) AS max_val,
  PERCENTILE_CONT(0.95) WITHIN GROUP (
    ORDER BY COALESCE(CAST(value_double AS NUMERIC), CAST(value_integer AS NUMERIC))
  ) AS p95_val
FROM telemetry
WHERE $__timeFilter(systime)
  AND uuid = (${signal_var:raw})
  AND is_delta = 'f';


-- ============================================================================
-- PERFORMANCE NOTES FOR TIMESERIES ARCHETYPE
-- ============================================================================

-- 1. The compound index (uuid, systime DESC) is essential. Without it, every
--    query scans the whole table.
--
-- 2. For TimescaleDB hypertables (Postgres only): chunk_time_interval should
--    match query granularity. 1-day chunks for sub-minute data, 1-week for
--    minute data. DuckDB has no equivalent — use Parquet partitioning instead.
--
-- 3. Continuous aggregates (TimescaleDB / Postgres only) pay off enormously
--    here: materialize hourly buckets per (uuid, time_bucket), then trend
--    panels read from the aggregate. This is one of the FEW places where
--    time_bucket() appears in this skill — it's DDL the user runs once on
--    Postgres, NOT a query expression that needs to portable.
--    Example:
--      CREATE MATERIALIZED VIEW telemetry_1h
--      WITH (timescaledb.continuous) AS
--      SELECT uuid,
--             time_bucket('1 hour', systime) AS bucket,
--             AVG(COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER))) AS avg_val,
--             COUNT(*) AS samples
--      FROM telemetry
--      WHERE is_delta IN ('t', 'f')
--      GROUP BY uuid, bucket;
--
--    Querying this aggregate from Grafana still uses $__timeGroup(bucket, ...)
--    in the dashboard SQL — never time_bucket() in Grafana panel queries.
--
-- 4. For Parquet-on-blob via DuckDB adapter: complex CTEs sometimes fail to
--    translate. Test each query against the actual datasource. Fallback is to
--    inline subqueries instead of CTEs and avoid window functions where
--    possible.
--
-- 5. The :raw modifier on UUID variables is non-negotiable. Without it, the
--    UUID gets quoted as a string literal twice and the comparison fails
--    silently (no error, just zero rows).
--
-- 6. UUID type compatibility: DuckDB has a UUID type but is stricter about
--    text↔uuid implicit conversions. If you ever need to compare a UUID to a
--    text literal not coming through Grafana variable expansion, cast both
--    sides explicitly: `CAST(uuid AS TEXT) = '...'`.
