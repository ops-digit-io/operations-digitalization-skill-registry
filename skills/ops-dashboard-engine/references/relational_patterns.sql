-- ============================================================================
-- relational_patterns.sql — SQL for relational fact + dimension models
--
-- HARD RULES (see SKILL.md):
--   1. Use Grafana macros for time. Default to $__timeFilter() in WHERE
--      and $__timeGroup()/$__timeGroupAlias() in SELECT. Raw $__timeFrom()/
--      $__timeTo() are allowed only for window clipping, generate_series
--      bounds, and interval-overlap WHERE clauses (each justified inline).
--   2. Every query must run on PostgreSQL AND DuckDB. No time_bucket(),
--      no DISTINCT ON, no bool::int casts. Use CAST(x AS INTEGER) explicitly.
--      Window clipping inside SELECT is the canonical raw-bound exception.
--
-- Read this when archetype = relational.
-- ============================================================================
--
-- These patterns work for any relational ops domain — downtime, production
-- orders, quality checks, energy bills, work orders, etc. The worked example
-- here is downtime (interval-shaped fact with start_time / end_time), but the
-- structures generalize.
--
-- For interval-shaped facts (events with duration), see Sections A–F.
-- For point-shaped facts (events with a single timestamp), see Section G.

-- ============================================================================
-- ASSUMED EXAMPLE SCHEMA (downtime as worked example — adapt to user's actual)
-- ============================================================================
--
-- downtime_incidents (
--   id                   bigint primary key,
--   start_time           timestamptz,
--   end_time             timestamptz,        -- nullable: NULL means ongoing
--   machine_id           bigint references machines,
--   reason_id            bigint references downtime_reasons,
--   reported_by_id       bigint references users,
--   account_id           bigint references accounts,
--   is_archived          boolean,
--   is_auto_detected     boolean,
--   is_auto_closed       boolean,
--   affected_item        text,
--   notes                text
-- );
--
-- machines           (id, name, type, is_ignored, ...)
-- downtime_reasons   (id, name, severity, parent_reason_id, is_archived, is_active, account_id)
-- users              (id, first_name, last_name)
-- accounts           (id, name)
--
-- The patterns below assume this shape. For production-orders, quality, energy,
-- the structure is identical — rename the fact table and adjust the FKs.


-- ============================================================================
-- THE TWO NON-NEGOTIABLE PATTERNS FOR INTERVAL-SHAPED FACTS
-- ============================================================================

-- Pattern A: coalesce nullable end_time
-- Use when ongoing events should contribute their elapsed time so far.
-- For purely historical analytics use `WHERE end_time IS NOT NULL` instead.

EXTRACT(EPOCH FROM (COALESCE(di.end_time, NOW()) - di.start_time)) / 60.0 AS duration_min


-- Pattern B: window clipping. Use in EVERY duration-summing query.
-- Without clipping, partially-overlapping events inflate totals.
-- Justified raw-bound use (Rule 1 exception): clipping inside SELECT cannot
-- be expressed via $__timeFilter(); both LEAST/GREATEST work in PG and DuckDB.

SUM(EXTRACT(EPOCH FROM (
  LEAST(COALESCE(di.end_time, NOW()), $__timeTo()::timestamptz)
  - GREATEST(di.start_time, $__timeFrom()::timestamptz)
))) / 60.0 AS clipped_minutes

-- Plus the matching WHERE to drop fully-outside events. This explicit two-
-- column compare cannot be expressed by $__timeFilter() — it needs to look at
-- start_time AND end_time independently.
-- WHERE di.start_time   <  $__timeTo()::timestamptz
--   AND COALESCE(di.end_time, NOW()) >= $__timeFrom()::timestamptz


-- ============================================================================
-- A. CANONICAL ANALYST-TIER WHERE CLAUSE
-- Wires every variable. Adapt column names to the actual schema.
-- ============================================================================

WHERE di.is_archived = false
  AND $__timeFilter(di.start_time)
  AND di.machine_id IN ($machine)
  AND di.account_id IN ($account)
  AND ((di.reason_id IN ($reason)) OR di.reason_id IS NULL)
  AND ('$severity' = 'all' OR CAST(dr.severity AS TEXT) = '$severity')
  AND ($auto_detected = -1
       OR CAST(di.is_auto_detected AS INTEGER) = $auto_detected)   -- portable bool→int
  AND EXTRACT(EPOCH FROM (COALESCE(di.end_time, NOW()) - di.start_time)) / 60.0
        >= $min_duration_min


-- ============================================================================
-- B. KPI QUERIES — single-value stats
-- ============================================================================

-- Total downtime (window-clipped, in minutes)
SELECT
  SUM(EXTRACT(EPOCH FROM (
    LEAST(COALESCE(di.end_time, NOW()), $__timeTo()::timestamptz)
    - GREATEST(di.start_time, $__timeFrom()::timestamptz)
  ))) / 60.0 AS downtime_min
FROM downtime_incidents di
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
-- Interval-overlap WHERE (justified raw-bound use; cannot use $__timeFilter):
WHERE di.start_time   <  $__timeTo()::timestamptz
  AND COALESCE(di.end_time, NOW()) >= $__timeFrom()::timestamptz
  -- + canonical WHERE clause from section A


-- Incident count
SELECT COUNT(*) AS incidents
FROM downtime_incidents di
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
WHERE $__timeFilter(di.start_time)
  -- + canonical WHERE clause


-- MTTR — Mean Time To Repair (closed incidents only)
SELECT AVG(EXTRACT(EPOCH FROM (di.end_time - di.start_time))) / 60.0 AS mttr_min
FROM downtime_incidents di
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
WHERE di.end_time IS NOT NULL
  AND $__timeFilter(di.start_time)
  -- + canonical WHERE clause


-- MTBF — Mean Time Between Failures (window/n approximation)
-- Raw-bound use here is justified: the window length itself is the metric,
-- and it must reflect the user's selected dashboard time range.
WITH per_machine AS (
  SELECT
    di.machine_id,
    COUNT(*) AS n,
    EXTRACT(EPOCH FROM ($__timeTo()::timestamptz - $__timeFrom()::timestamptz)) / 60.0
      AS window_min
  FROM downtime_incidents di
  LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
  WHERE $__timeFilter(di.start_time)
    -- + canonical WHERE clause
  GROUP BY di.machine_id
)
SELECT AVG(window_min / NULLIF(n, 0)) AS mtbf_min FROM per_machine;


-- P95 incident duration
-- Note: PERCENTILE_CONT works in both PG and DuckDB.
SELECT
  PERCENTILE_CONT(0.95) WITHIN GROUP (
    ORDER BY EXTRACT(EPOCH FROM (di.end_time - di.start_time)) / 60.0
  ) AS p95_min
FROM downtime_incidents di
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
WHERE di.end_time IS NOT NULL
  AND $__timeFilter(di.start_time)
  -- + canonical WHERE clause


-- Unassigned percentage (data quality KPI)
-- Portable: use CASE inside SUM, not (cond)::int.
WITH t AS (
  SELECT di.reason_id
  FROM downtime_incidents di
  LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
  WHERE $__timeFilter(di.start_time)
    -- + canonical WHERE clause
)
SELECT CASE WHEN COUNT(*) = 0 THEN 0
            ELSE ROUND(100.0 *
                       SUM(CASE WHEN reason_id IS NULL THEN 1 ELSE 0 END)
                       / COUNT(*), 1)
       END AS unassigned_pct
FROM t;


-- ============================================================================
-- C. TIME SERIES — for Grafana time series panels (format: time_series)
-- Returns columns: time, metric, value
-- ============================================================================

-- Stacked downtime minutes by reason, window-clipped.
-- Bucketing via $__timeGroup() — never time_bucket(). Works on PG and DuckDB.
SELECT
  $__timeGroup(di.start_time, $__interval) AS time,
  COALESCE(dr.name, 'Unassigned')          AS metric,
  SUM(EXTRACT(EPOCH FROM (
    LEAST(COALESCE(di.end_time, NOW()), $__timeTo()::timestamptz)
    - GREATEST(di.start_time, $__timeFrom()::timestamptz)
  ))) / 60.0 AS value
FROM downtime_incidents di
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
WHERE di.start_time   <  $__timeTo()::timestamptz
  AND COALESCE(di.end_time, NOW()) >= $__timeFrom()::timestamptz
  -- + canonical WHERE clause
GROUP BY 1, 2
ORDER BY 1;


-- Daily fleet downtime with zero-fill (manager view, fixed window)
-- generate_series + LEFT JOIN replaces time_bucket_gapfill (DuckDB-incompatible).
-- Both generate_series(timestamptz, timestamptz, INTERVAL) and date_trunc()
-- behave identically on PG and DuckDB.
WITH days AS (
  SELECT generate_series(
    date_trunc('day', NOW() - INTERVAL '13 days'),
    date_trunc('day', NOW()),
    INTERVAL '1 day'
  ) AS day
)
SELECT
  d.day AS time,
  COALESCE(ROUND(SUM(EXTRACT(EPOCH FROM (
    LEAST(COALESCE(di.end_time, NOW()), d.day + INTERVAL '1 day')
    - GREATEST(di.start_time, d.day)
  ))) / 3600.0, 1), 0) AS "Downtime hours"
FROM days d
LEFT JOIN downtime_incidents di
  ON di.is_archived = false
  AND di.start_time   <  d.day + INTERVAL '1 day'
  AND COALESCE(di.end_time, NOW()) >= d.day
  AND di.account_id IN ($account)
GROUP BY d.day
ORDER BY d.day;


-- Rolling 7-day MTTR
-- date_trunc() is portable; window functions work on both engines.
WITH daily AS (
  SELECT
    date_trunc('day', di.start_time) AS day,
    AVG(EXTRACT(EPOCH FROM (di.end_time - di.start_time))) / 60.0 AS mttr_min
  FROM downtime_incidents di
  LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
  WHERE di.end_time IS NOT NULL
    AND $__timeFilter(di.start_time)
    -- + canonical WHERE clause
  GROUP BY 1
)
SELECT
  day AS time,
  AVG(mttr_min) OVER (ORDER BY day ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)
    AS "MTTR 7d rolling [min]"
FROM daily
ORDER BY day;


-- ============================================================================
-- D. PARETO — non-pivoted, for ECharts (format: table)
-- Returns columns: metric (text), value (number)
-- ============================================================================

SELECT
  m.name || ' :: ' || COALESCE(dr.name, 'Unassigned') AS metric,
  ROUND(SUM(EXTRACT(EPOCH FROM (
    LEAST(COALESCE(di.end_time, NOW()), $__timeTo()::timestamptz)
    - GREATEST(di.start_time, $__timeFrom()::timestamptz)
  ))) / 60.0, 1) AS value
FROM downtime_incidents di
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
LEFT JOIN machines m          ON m.id  = di.machine_id
WHERE di.start_time   <  $__timeTo()::timestamptz
  AND COALESCE(di.end_time, NOW()) >= $__timeFrom()::timestamptz
  -- + canonical WHERE clause
GROUP BY 1
ORDER BY value DESC;


-- ============================================================================
-- E. RANKING TABLES — analyst tier
-- ============================================================================

-- Machine ranking by total downtime
SELECT
  m.name AS machine,
  COUNT(*) AS incidents,
  ROUND(SUM(EXTRACT(EPOCH FROM (COALESCE(di.end_time, NOW()) - di.start_time)))
        / 60.0, 1) AS total_min,
  ROUND(AVG(EXTRACT(EPOCH FROM (COALESCE(di.end_time, NOW()) - di.start_time)))
        / 60.0, 1) AS avg_min,
  ROUND(MAX(EXTRACT(EPOCH FROM (COALESCE(di.end_time, NOW()) - di.start_time)))
        / 60.0, 1) AS worst_min
FROM downtime_incidents di
JOIN machines m ON m.id = di.machine_id
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
WHERE $__timeFilter(di.start_time)
  -- + canonical WHERE clause
GROUP BY m.name
ORDER BY total_min DESC;


-- Reason hierarchy roll-up (uses parent_reason_id)
SELECT
  COALESCE(parent.name, child.name, 'Unassigned') AS reason_group,
  COUNT(*) AS incidents,
  ROUND(SUM(EXTRACT(EPOCH FROM (COALESCE(di.end_time, NOW()) - di.start_time)))
        / 60.0, 1) AS total_min,
  ROUND(AVG(EXTRACT(EPOCH FROM (COALESCE(di.end_time, NOW()) - di.start_time)))
        / 60.0, 1) AS avg_min
FROM downtime_incidents di
LEFT JOIN downtime_reasons child  ON child.id  = di.reason_id
LEFT JOIN downtime_reasons parent ON parent.id = child.parent_reason_id
LEFT JOIN downtime_reasons dr     ON dr.id     = di.reason_id
WHERE $__timeFilter(di.start_time)
  -- + canonical WHERE clause
GROUP BY reason_group
ORDER BY total_min DESC;


-- ============================================================================
-- F. MANAGER-TIER PATTERNS — fixed windows, week-over-week deltas
-- ============================================================================

-- Action board: this week vs last week + top reason per machine.
-- Top reason uses ROW_NUMBER() OVER (PARTITION BY ...) instead of DISTINCT ON
-- (DISTINCT ON is Postgres-only; ROW_NUMBER works on both engines).
WITH
this_week AS (
  SELECT di.machine_id,
         SUM(EXTRACT(EPOCH FROM (
           LEAST(COALESCE(di.end_time, NOW()), NOW())
           - GREATEST(di.start_time, NOW() - INTERVAL '7 days')
         ))) / 3600.0 AS hours,
         COUNT(*) AS incidents
  FROM downtime_incidents di
  WHERE di.is_archived = false
    AND di.start_time   <  NOW()
    AND COALESCE(di.end_time, NOW()) >= NOW() - INTERVAL '7 days'
    AND di.account_id IN ($account)
  GROUP BY di.machine_id
),
prev_week AS (
  SELECT di.machine_id,
         SUM(EXTRACT(EPOCH FROM (
           LEAST(COALESCE(di.end_time, NOW()), NOW() - INTERVAL '7 days')
           - GREATEST(di.start_time, NOW() - INTERVAL '14 days')
         ))) / 3600.0 AS hours
  FROM downtime_incidents di
  WHERE di.is_archived = false
    AND di.start_time   <  NOW() - INTERVAL '7 days'
    AND COALESCE(di.end_time, NOW()) >= NOW() - INTERVAL '14 days'
    AND di.account_id IN ($account)
  GROUP BY di.machine_id
),
reason_totals AS (
  SELECT
    di.machine_id,
    COALESCE(dr.name, 'Unassigned') AS reason,
    SUM(EXTRACT(EPOCH FROM (COALESCE(di.end_time, NOW()) - di.start_time))) AS reason_seconds
  FROM downtime_incidents di
  LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
  WHERE di.is_archived = false
    AND di.start_time >= NOW() - INTERVAL '7 days'
    AND di.account_id IN ($account)
  GROUP BY di.machine_id, COALESCE(dr.name, 'Unassigned')
),
top_reason AS (
  SELECT machine_id, reason
  FROM (
    SELECT
      machine_id, reason,
      ROW_NUMBER() OVER (PARTITION BY machine_id ORDER BY reason_seconds DESC) AS rn
    FROM reason_totals
  ) ranked
  WHERE rn = 1
)
SELECT
  m.name AS machine,
  ROUND(CAST(COALESCE(t.hours, 0) AS NUMERIC), 1) AS hours_this_week,
  ROUND(CAST(COALESCE(p.hours, 0) AS NUMERIC), 1) AS hours_last_week,
  ROUND(CAST(COALESCE(t.hours, 0) - COALESCE(p.hours, 0) AS NUMERIC), 1) AS delta_hours,
  COALESCE(t.incidents, 0) AS incidents,
  COALESCE(tr.reason, '—') AS top_reason
FROM machines m
LEFT JOIN this_week t   ON t.machine_id  = m.id
LEFT JOIN prev_week p   ON p.machine_id  = m.id
LEFT JOIN top_reason tr ON tr.machine_id = m.id
WHERE m.is_ignored = false
  AND (t.hours IS NOT NULL OR p.hours IS NOT NULL)
ORDER BY hours_this_week DESC;


-- ============================================================================
-- G. POINT-SHAPED FACTS (events with single timestamp, no duration)
-- For quality checks, transactions, completed parts, audit logs
-- ============================================================================

-- Point-shaped facts use $__timeFilter(timestamp_col) directly. No window
-- clipping needed because there's no duration to clip.

-- Events per time bucket
SELECT
  $__timeGroup(qc.checked_at, $__interval) AS time,
  qc.result                                AS metric,
  COUNT(*)                                 AS value
FROM quality_checks qc
WHERE $__timeFilter(qc.checked_at)
  AND qc.machine_id IN ($machine)
  AND qc.account_id IN ($account)
GROUP BY 1, 2
ORDER BY 1;


-- Pareto by category for point-shaped facts
SELECT
  COALESCE(dt.name, 'Unknown') AS metric,
  COUNT(*)                     AS value
FROM quality_checks qc
LEFT JOIN defect_types dt ON dt.id = qc.defect_type_id
WHERE $__timeFilter(qc.checked_at)
  AND qc.machine_id IN ($machine)
  AND qc.account_id IN ($account)
GROUP BY 1
ORDER BY value DESC;


-- ============================================================================
-- H. DRILL-DOWN DETAIL TABLE
-- ============================================================================

SELECT
  di.start_time,
  di.end_time,
  m.name AS machine,
  COALESCE(dr.name, 'Unassigned') AS reason,
  COALESCE(CAST(dr.severity AS TEXT), 'unset') AS severity,
  ROUND(EXTRACT(EPOCH FROM (COALESCE(di.end_time, NOW()) - di.start_time))
        / 60.0, 1) AS duration_min,
  CASE WHEN di.is_auto_detected THEN 'auto' ELSE 'manual' END AS source,
  CASE WHEN di.is_auto_closed   THEN 'auto' ELSE 'manual' END AS closure,
  COALESCE(u.first_name || ' ' || u.last_name, '—') AS reported_by,
  di.affected_item,
  di.notes
FROM downtime_incidents di
LEFT JOIN machines m          ON m.id  = di.machine_id
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
LEFT JOIN users u             ON u.id  = di.reported_by_id
WHERE $__timeFilter(di.start_time)
  -- + canonical WHERE clause
ORDER BY duration_min DESC
LIMIT 500;
