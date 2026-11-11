"""
Worked example — timeseries archetype, manager tier.

Domain: machine state from PLC telemetry.
Audience: plant manager, weekly overview.
Question: which machines are spending the most time stopped this week?

Run this script to regenerate `timeseries_manager.json`.

Even though the underlying data is UUID-keyed long-format telemetry,
the manager view aggregates it down to machine-level KPIs and looks
similar in shape to the relational manager view.

Schema assumed (from references/timeseries_patterns.sql):
- telemetry (systime, uuid, value_double, value_integer, value_bool,
             value_string, is_delta)
- signal_metadata (uuid, name, machine_id, ...)
- machines (id, name, is_ignored, account_id, ...)
"""

import json, sys
sys.path.insert(0, "/home/claude/references")
from dashboard_builder import (
    stat, table_panel, echarts, timeseries, row, text,
    traffic_light, reverse_traffic_light,
    color_cell_override, width_override,
    var_query, build_dashboard,
)

# ---------------------------------------------------------------------------
# Variables — manager view: just the account
# ---------------------------------------------------------------------------
variables = [
    var_query("account", "Account",
              "SELECT name AS __text, id AS __value FROM accounts ORDER BY name",
              multi=False, include_all=False),
]

# ---------------------------------------------------------------------------
# Reusable shape — for "running" state signals across all machines.
# Assumes one signal per machine named exactly 'machine_state' with values
# 1=running, 0=stopped. Adapt to user's actual naming convention.
# ---------------------------------------------------------------------------

panels = []
pid = 100

# --- Row: KPIs ----------------------------------------------------------
panels.append(row(pid, "🎯 Fleet KPIs — last 7 days", 0)); pid += 1

# Stat: total stopped hours across the fleet, last 7 days.
# Pattern: derive intervals from successive state samples, sum the "stopped"
# windows clipped to the visible range. Manager-tier raw bound (NOW() based).
stopped_hours_sql = """\
WITH samples AS (
  SELECT
    s.machine_id,
    t.systime,
    COALESCE(t.value_double, t.value_integer, CAST(t.value_bool AS INTEGER)) AS state,
    LEAD(t.systime) OVER (PARTITION BY t.uuid ORDER BY t.systime) AS next_systime
  FROM telemetry t
  JOIN signal_metadata s ON s.uuid = t.uuid
  JOIN machines m ON m.id = s.machine_id
  WHERE s.name = 'machine_state'
    AND m.account_id IN ($account)
    AND m.is_ignored = false
    AND t.systime >= NOW() - INTERVAL '7 days' - INTERVAL '1 hour'
    -- one-hour pre-roll so the first interval inside the window has a start
    AND t.is_delta IN ('t', 'f')
)
SELECT
  ROUND(CAST(SUM(EXTRACT(EPOCH FROM (
    LEAST(COALESCE(next_systime, NOW()), NOW())
    - GREATEST(systime,                     NOW() - INTERVAL '7 days')
  ))) / 3600.0 AS NUMERIC), 1) AS hours
FROM samples
WHERE state = 0
  AND systime < NOW()
  AND COALESCE(next_systime, NOW()) >= NOW() - INTERVAL '7 days'"""

panels.append(stat(pid, "Total stopped time", 0, 1, 6, 5,
                   sql=stopped_hours_sql, unit="h",
                   thresholds=traffic_light(yellow=20, red=50))); pid += 1

# Stat: count of distinct machines that were stopped any time this week
machines_stopped_sql = """\
SELECT COUNT(DISTINCT s.machine_id) AS n
FROM telemetry t
JOIN signal_metadata s ON s.uuid = t.uuid
JOIN machines m ON m.id = s.machine_id
WHERE s.name = 'machine_state'
  AND m.account_id IN ($account)
  AND m.is_ignored = false
  AND t.systime >= NOW() - INTERVAL '7 days'
  AND t.is_delta IN ('t', 'f')
  AND COALESCE(t.value_double, t.value_integer, CAST(t.value_bool AS INTEGER)) = 0"""
panels.append(stat(pid, "Machines stopped at any point", 6, 1, 6, 5,
                   sql=machines_stopped_sql, unit="short",
                   thresholds=traffic_light(yellow=5, red=10))); pid += 1

# Stat: total event count (all transitions) — heuristic for system noise
event_count_sql = """\
SELECT COUNT(*) AS n
FROM telemetry t
JOIN signal_metadata s ON s.uuid = t.uuid
JOIN machines m ON m.id = s.machine_id
WHERE s.name = 'machine_state'
  AND m.account_id IN ($account)
  AND t.systime >= NOW() - INTERVAL '7 days'
  AND t.is_delta = 't'"""
panels.append(stat(pid, "State transitions", 12, 1, 6, 5,
                   sql=event_count_sql, unit="short",
                   description="Total state changes this week. Spikes can indicate sensor flapping.")); pid += 1

# Stat: data freshness — minutes since the most recent telemetry sample
freshness_sql = """\
SELECT
  ROUND(CAST(EXTRACT(EPOCH FROM (NOW() - MAX(t.systime))) / 60.0 AS NUMERIC), 1)
  AS minutes_stale
FROM telemetry t
JOIN signal_metadata s ON s.uuid = t.uuid
JOIN machines m ON m.id = s.machine_id
WHERE m.account_id IN ($account)
  AND m.is_ignored = false"""
panels.append(stat(pid, "Data staleness", 18, 1, 6, 5,
                   sql=freshness_sql, unit="m",
                   thresholds=traffic_light(yellow=5, red=15),
                   description="Minutes since the most recent sample. Above 15 means the pipeline is broken.")); pid += 1

# --- Row: machine ranking ----------------------------------------------
panels.append(row(pid, "🚨 Stopped time by machine — last 7 days", 6)); pid += 1

machine_rank_sql = """\
WITH samples AS (
  SELECT
    s.machine_id,
    t.systime,
    COALESCE(t.value_double, t.value_integer, CAST(t.value_bool AS INTEGER)) AS state,
    LEAD(t.systime) OVER (PARTITION BY t.uuid ORDER BY t.systime) AS next_systime
  FROM telemetry t
  JOIN signal_metadata s ON s.uuid = t.uuid
  JOIN machines m ON m.id = s.machine_id
  WHERE s.name = 'machine_state'
    AND m.account_id IN ($account)
    AND m.is_ignored = false
    AND t.systime >= NOW() - INTERVAL '7 days' - INTERVAL '1 hour'
    AND t.is_delta IN ('t', 'f')
),
clipped AS (
  SELECT
    machine_id,
    SUM(EXTRACT(EPOCH FROM (
      LEAST(COALESCE(next_systime, NOW()), NOW())
      - GREATEST(systime,                     NOW() - INTERVAL '7 days')
    ))) AS stopped_seconds
  FROM samples
  WHERE state = 0
    AND systime < NOW()
    AND COALESCE(next_systime, NOW()) >= NOW() - INTERVAL '7 days'
  GROUP BY machine_id
)
SELECT
  m.name AS "Machine",
  ROUND(CAST(COALESCE(c.stopped_seconds, 0) / 3600.0 AS NUMERIC), 1) AS "Stopped hours",
  ROUND(CAST(COALESCE(c.stopped_seconds, 0) / 3600.0 / (7 * 24) * 100 AS NUMERIC), 1)
    AS "% of week"
FROM machines m
LEFT JOIN clipped c ON c.machine_id = m.id
WHERE m.is_ignored = false
  AND m.account_id IN ($account)
ORDER BY "Stopped hours" DESC
LIMIT 15"""

panels.append(table_panel(pid, "Top stopped machines", 0, 7, 24, 9,
                           sql=machine_rank_sql,
    overrides=[
        color_cell_override("Stopped hours",
                            traffic_light(yellow=4, red=12), unit="h", width=160),
        color_cell_override("% of week",
                            traffic_light(yellow=2.5, red=10), unit="percent", width=140),
        width_override("Machine", 240),
    ])); pid += 1

# --- Row: trend --------------------------------------------------------
panels.append(row(pid, "📈 Daily fleet stopped time (last 14 days)", 16)); pid += 1

# Daily stopped hours zero-filled
trend_sql = """\
WITH days AS (
  SELECT generate_series(
    date_trunc('day', NOW() - INTERVAL '13 days'),
    date_trunc('day', NOW()),
    INTERVAL '1 day'
  ) AS day
),
samples AS (
  SELECT
    t.systime,
    COALESCE(t.value_double, t.value_integer, CAST(t.value_bool AS INTEGER)) AS state,
    LEAD(t.systime) OVER (PARTITION BY t.uuid ORDER BY t.systime) AS next_systime
  FROM telemetry t
  JOIN signal_metadata s ON s.uuid = t.uuid
  JOIN machines m ON m.id = s.machine_id
  WHERE s.name = 'machine_state'
    AND m.account_id IN ($account)
    AND m.is_ignored = false
    AND t.systime >= NOW() - INTERVAL '14 days' - INTERVAL '1 hour'
    AND t.is_delta IN ('t', 'f')
)
SELECT
  d.day AS time,
  COALESCE(ROUND(CAST(SUM(EXTRACT(EPOCH FROM (
    LEAST(COALESCE(samples.next_systime, NOW()), d.day + INTERVAL '1 day')
    - GREATEST(samples.systime, d.day)
  ))) / 3600.0 AS NUMERIC), 1), 0) AS "Stopped hours"
FROM days d
LEFT JOIN samples
  ON samples.state = 0
  AND samples.systime < d.day + INTERVAL '1 day'
  AND COALESCE(samples.next_systime, NOW()) >= d.day
GROUP BY d.day
ORDER BY d.day"""

panels.append(timeseries(pid, "Daily stopped hours — last 14 days",
                          0, 17, 24, 8, sql=trend_sql, unit="h")); pid += 1

# ---------------------------------------------------------------------------
# Build & save
# ---------------------------------------------------------------------------
dashboard = build_dashboard(
    title="Machine State — Manager View (Fleet)",
    panels=panels,
    variables=variables,
    refresh="5m",
    hide_timepicker=True,
)

OUT = "/home/claude/references/examples/timeseries_manager.json"
with open(OUT, "w") as f:
    json.dump(dashboard, f, indent=2)
print("wrote", OUT)
