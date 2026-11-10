"""
Worked example — relational archetype, manager tier.

Domain: machine downtime across a fleet.
Audience: plant manager, weekly Monday standup.
Question: where do I send my attention this week?

Run this script to regenerate `relational_manager.json`. The output is the
exact JSON that gets imported into Grafana.

This file is a complete, faithful application of the skill's rules:
- Every time WHERE uses $__timeFilter or interval-overlap (with comments)
- Every duration-summing query uses LEAST/GREATEST window clipping
- Every CAST is portable (CAST(x AS INTEGER), not ::int)
- No DISTINCT ON, no time_bucket, no regr_*, no Postgres-only constructs
- Manager-tier conventions: timepicker hidden, refresh 5m, traffic lights,
  fixed week-vs-prior-week windows
"""

import json, sys
sys.path.insert(0, "/home/claude/references")
from dashboard_builder import (
    stat, table_panel, echarts, timeseries, row, text,
    traffic_light, reverse_traffic_light,
    color_cell_override, gradient_gauge_override, width_override,
    var_query, build_dashboard,
)

# ---------------------------------------------------------------------------
# Variables — manager view has only one (multi-tenant)
# ---------------------------------------------------------------------------

ACCOUNT_SQL = """\
SELECT name AS __text, id AS __value
FROM accounts
ORDER BY name"""

variables = [
    var_query("account", "Account", ACCOUNT_SQL, multi=False, include_all=False),
]

# ---------------------------------------------------------------------------
# Reusable SQL fragments
# ---------------------------------------------------------------------------

# Window-clipped duration in minutes for the last 7 days. Justified raw-bound
# use: NOW() and NOW() - INTERVAL '7 days' literally bake the manager-tier
# fixed window into the query (timepicker is hidden).
CLIP_THIS_WEEK = """\
LEAST(COALESCE(di.end_time, NOW()), NOW())
- GREATEST(di.start_time,            NOW() - INTERVAL '7 days')"""

CLIP_PREV_WEEK = """\
LEAST(COALESCE(di.end_time, NOW()), NOW() - INTERVAL '7 days')
- GREATEST(di.start_time,            NOW() - INTERVAL '14 days')"""

CANONICAL_WHERE_THIS = """\
WHERE di.is_archived = false
  AND di.start_time   <  NOW()
  AND COALESCE(di.end_time, NOW()) >= NOW() - INTERVAL '7 days'
  AND di.account_id IN ($account)"""

CANONICAL_WHERE_PREV = """\
WHERE di.is_archived = false
  AND di.start_time   <  NOW() - INTERVAL '7 days'
  AND COALESCE(di.end_time, NOW()) >= NOW() - INTERVAL '14 days'
  AND di.account_id IN ($account)"""

# ---------------------------------------------------------------------------
# Panels
# ---------------------------------------------------------------------------

panels = []
pid = 100

# --- Row: KPIs ------------------------------------------------------------
panels.append(row(pid, "🎯 Fleet KPIs — last 7 days", 0)); pid += 1

# Stat: total downtime hours this week
sql_hours = f"""\
SELECT
  ROUND(CAST(SUM(EXTRACT(EPOCH FROM ({CLIP_THIS_WEEK}))) / 3600.0 AS NUMERIC), 1)
    AS hours
FROM downtime_incidents di
{CANONICAL_WHERE_THIS}"""
panels.append(stat(pid, "Total downtime", 0, 1, 4, 5,
                   sql=sql_hours, unit="h",
                   thresholds=traffic_light(yellow=20, red=50))); pid += 1

# Stat: incident count this week
sql_count = f"""\
SELECT COUNT(*) AS incidents
FROM downtime_incidents di
{CANONICAL_WHERE_THIS}"""
panels.append(stat(pid, "Incidents", 4, 1, 4, 5,
                   sql=sql_count, unit="short",
                   thresholds=traffic_light(yellow=15, red=40))); pid += 1

# Stat: MTTR (closed incidents only)
sql_mttr = f"""\
SELECT ROUND(CAST(
  AVG(EXTRACT(EPOCH FROM (di.end_time - di.start_time))) / 60.0
  AS NUMERIC), 1) AS mttr_min
FROM downtime_incidents di
WHERE di.is_archived = false
  AND di.end_time IS NOT NULL
  AND di.end_time   >= NOW() - INTERVAL '7 days'
  AND di.account_id IN ($account)"""
panels.append(stat(pid, "MTTR", 8, 1, 4, 5,
                   sql=sql_mttr, unit="m",
                   thresholds=traffic_light(yellow=45, red=90))); pid += 1

# Stat: % unclassified (data quality)
sql_unassigned = f"""\
WITH t AS (
  SELECT di.reason_id
  FROM downtime_incidents di
  {CANONICAL_WHERE_THIS}
)
SELECT CASE WHEN COUNT(*) = 0 THEN 0
            ELSE ROUND(100.0 *
                       SUM(CASE WHEN reason_id IS NULL THEN 1 ELSE 0 END)
                       / COUNT(*), 1)
       END AS unassigned_pct
FROM t"""
panels.append(stat(pid, "Unclassified", 12, 1, 4, 5,
                   sql=sql_unassigned, unit="percent",
                   thresholds=traffic_light(yellow=10, red=25),
                   description="Data quality KPI. Above 25% means reasons aren't being captured.")); pid += 1

# Stat: machines with >0 minutes of downtime
sql_affected = f"""\
SELECT COUNT(DISTINCT di.machine_id) AS n
FROM downtime_incidents di
{CANONICAL_WHERE_THIS}
  AND ({CLIP_THIS_WEEK}) > INTERVAL '0 minutes'"""
panels.append(stat(pid, "Machines affected", 16, 1, 4, 5,
                   sql=sql_affected, unit="short",
                   thresholds=traffic_light(yellow=5, red=10))); pid += 1

# Stat: WoW delta in hours
sql_delta = f"""\
WITH this_w AS (
  SELECT SUM(EXTRACT(EPOCH FROM ({CLIP_THIS_WEEK}))) / 3600.0 AS h
  FROM downtime_incidents di
  {CANONICAL_WHERE_THIS}
),
prev_w AS (
  SELECT SUM(EXTRACT(EPOCH FROM ({CLIP_PREV_WEEK}))) / 3600.0 AS h
  FROM downtime_incidents di
  {CANONICAL_WHERE_PREV}
)
SELECT ROUND(CAST(COALESCE(this_w.h, 0) - COALESCE(prev_w.h, 0) AS NUMERIC), 1)
  AS delta_hours
FROM this_w, prev_w"""
panels.append(stat(pid, "WoW delta (hours)", 20, 1, 4, 5,
                   sql=sql_delta, unit="h",
                   thresholds=reverse_traffic_light(yellow=0, green=-5),
                   description="Negative = improvement vs prior week.")); pid += 1

# --- Row: Action board ----------------------------------------------------
panels.append(row(pid, "🚨 Action board — where to send attention", 6)); pid += 1

# Top reason per machine using ROW_NUMBER (portable; no DISTINCT ON)
action_board_sql = f"""\
WITH this_week AS (
  SELECT di.machine_id,
         SUM(EXTRACT(EPOCH FROM ({CLIP_THIS_WEEK}))) / 3600.0 AS hours,
         COUNT(*) AS incidents
  FROM downtime_incidents di
  {CANONICAL_WHERE_THIS}
  GROUP BY di.machine_id
),
prev_week AS (
  SELECT di.machine_id,
         SUM(EXTRACT(EPOCH FROM ({CLIP_PREV_WEEK}))) / 3600.0 AS hours
  FROM downtime_incidents di
  {CANONICAL_WHERE_PREV}
  GROUP BY di.machine_id
),
reason_totals AS (
  SELECT
    di.machine_id,
    COALESCE(dr.name, 'Unassigned') AS reason,
    SUM(EXTRACT(EPOCH FROM (COALESCE(di.end_time, NOW()) - di.start_time))) AS r_seconds
  FROM downtime_incidents di
  LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
  {CANONICAL_WHERE_THIS.replace("WHERE ", "WHERE ")}
  GROUP BY di.machine_id, COALESCE(dr.name, 'Unassigned')
),
top_reason AS (
  SELECT machine_id, reason FROM (
    SELECT machine_id, reason,
           ROW_NUMBER() OVER (PARTITION BY machine_id ORDER BY r_seconds DESC) AS rn
    FROM reason_totals
  ) ranked
  WHERE rn = 1
)
SELECT
  m.name AS "Machine",
  ROUND(CAST(COALESCE(t.hours, 0) AS NUMERIC), 1) AS "Hours",
  ROUND(CAST(COALESCE(t.hours, 0) - COALESCE(p.hours, 0) AS NUMERIC), 1) AS "Δ vs prev wk",
  COALESCE(t.incidents, 0) AS "Incidents",
  COALESCE(tr.reason, '—') AS "Top reason"
FROM machines m
LEFT JOIN this_week t   ON t.machine_id  = m.id
LEFT JOIN prev_week p   ON p.machine_id  = m.id
LEFT JOIN top_reason tr ON tr.machine_id = m.id
WHERE m.is_ignored = false
  AND m.account_id IN ($account)
  AND (t.hours IS NOT NULL OR p.hours IS NOT NULL)
ORDER BY "Hours" DESC
LIMIT 10"""

panels.append(table_panel(pid, "Top 10 machines this week", 0, 7, 24, 9,
    sql=action_board_sql,
    overrides=[
        color_cell_override("Hours",       traffic_light(yellow=2, red=5),  unit="h", width=120),
        color_cell_override("Δ vs prev wk", reverse_traffic_light(yellow=0, green=-1), unit="h", width=140),
        width_override("Machine", 200),
        width_override("Top reason", 240),
    ])); pid += 1

# --- Row: trend ----------------------------------------------------------
panels.append(row(pid, "📈 Trend — fleet downtime by day (zero-filled)", 16)); pid += 1

# Daily zero-filled trend
daily_sql = f"""\
WITH days AS (
  SELECT generate_series(
    date_trunc('day', NOW() - INTERVAL '13 days'),
    date_trunc('day', NOW()),
    INTERVAL '1 day'
  ) AS day
)
SELECT
  d.day AS time,
  COALESCE(ROUND(CAST(SUM(EXTRACT(EPOCH FROM (
    LEAST(COALESCE(di.end_time, NOW()), d.day + INTERVAL '1 day')
    - GREATEST(di.start_time, d.day)
  ))) / 3600.0 AS NUMERIC), 1), 0) AS "Downtime hours"
FROM days d
LEFT JOIN downtime_incidents di
  ON di.is_archived = false
  AND di.start_time   <  d.day + INTERVAL '1 day'
  AND COALESCE(di.end_time, NOW()) >= d.day
  AND di.account_id IN ($account)
GROUP BY d.day
ORDER BY d.day"""

panels.append(timeseries(pid, "Daily fleet downtime — last 14 days", 0, 17, 24, 8,
                          sql=daily_sql, unit="h")); pid += 1

# ---------------------------------------------------------------------------
# Build & save
# ---------------------------------------------------------------------------

dashboard = build_dashboard(
    title="Downtime — Manager View (Fleet)",
    panels=panels,
    variables=variables,
    refresh="5m",
    hide_timepicker=True,
)

OUT = "/home/claude/references/examples/relational_manager.json"
with open(OUT, "w") as f:
    json.dump(dashboard, f, indent=2)
print("wrote", OUT)
