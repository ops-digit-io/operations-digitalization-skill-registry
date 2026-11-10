"""
Worked example — timeseries archetype, analyst tier.

Domain: signal-level investigation of one machine's PLC telemetry.
Audience: process engineer or controls engineer.
Question: what's a specific signal doing, and how does it correlate with another?

Run this script to regenerate `timeseries_analyst.json`.

This dashboard demonstrates the key timeseries patterns:
- UUID variables driven by a signal_metadata table, with :raw modifier
- $__timeFilter() / $__timeGroup() for portable bucketing
- COALESCE polymorphic value reads with CAST(value_bool AS INTEGER)
- State-duration computation with window-clipping
- Counter reset detection
- Two-signal correlation via bucketed inner join

Schema assumed (from references/timeseries_patterns.sql):
- telemetry (systime, uuid, value_*, is_delta)
- signal_metadata (uuid, name, machine_id, ...)
"""

import json, sys
sys.path.insert(0, "/home/claude/references")
from dashboard_builder import (
    stat, table_panel, echarts, timeseries, row, text,
    traffic_light,
    color_cell_override, width_override,
    var_query, var_uuid_signal, build_dashboard,
)

# ---------------------------------------------------------------------------
# Variables
# ---------------------------------------------------------------------------
variables = [
    var_query("account", "Account",
              "SELECT name AS __text, id AS __value FROM accounts ORDER BY name",
              multi=False, include_all=False),
    var_query("machine", "Machine", """
SELECT m.name AS __text, m.id AS __value
FROM machines m
WHERE m.is_ignored = false
  AND m.account_id IN ($account)
ORDER BY m.name""", multi=False, include_all=False),
    # UUID variables — one per signal of interest. Each picks a UUID by name
    # from signal_metadata, scoped to the selected machine.
    var_uuid_signal("state_signal", "State signal",
                    where_clause="AND machine_id IN ($machine) AND name LIKE '%state%'"),
    var_uuid_signal("counter_signal", "Counter signal",
                    where_clause="AND machine_id IN ($machine) AND name LIKE '%counter%'"),
    var_uuid_signal("temp_signal", "Temperature signal",
                    where_clause="AND machine_id IN ($machine) AND name LIKE '%temp%'"),
]

# ---------------------------------------------------------------------------
# Panels
# ---------------------------------------------------------------------------
panels = []
pid = 200

# --- Row: signal trace --------------------------------------------------
panels.append(row(pid, "📊 Signal trace — selected machine, selected window", 0)); pid += 1

# Raw signal trace
panels.append(timeseries(pid, "[Analyst] State — selected signal",
                          0, 1, 12, 8,
                          sql="""SELECT
  systime AS "time",
  COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) AS "Value"
FROM telemetry
WHERE $__timeFilter(systime)
  AND uuid = (${state_signal:raw})
  AND is_delta IN ('t', 'f')
ORDER BY 1""", unit="short")); pid += 1

# Bucketed average
panels.append(timeseries(pid, "[Analyst] Temperature — bucketed avg",
                          12, 1, 12, 8,
                          sql="""SELECT
  $__timeGroupAlias(systime, $__interval) AS time,
  AVG(COALESCE(
    CAST(value_double  AS NUMERIC),
    CAST(value_integer AS NUMERIC),
    CAST(CAST(value_bool AS INTEGER) AS NUMERIC)
  )) AS "Avg"
FROM telemetry
WHERE $__timeFilter(systime)
  AND uuid = (${temp_signal:raw})
  AND is_delta IN ('t', 'f')
GROUP BY 1
ORDER BY 1""", unit="celsius")); pid += 1

# --- Row: state duration ------------------------------------------------
panels.append(row(pid, "⏱️ State duration breakdown", 9)); pid += 1

# State duration table — derive intervals via LEAD, clip to window, sum
panels.append(table_panel(pid, "[Analyst] State — minutes in each state",
                          0, 10, 12, 8,
                          sql="""WITH state_changes AS (
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
      - GREATEST(systime,                    $__timeFrom()::timestamptz)
    ))) / 60.0 AS minutes_in_state
  FROM state_changes
  WHERE systime < $__timeTo()::timestamptz
    AND COALESCE(next_systime, NOW()) >= $__timeFrom()::timestamptz
  GROUP BY state
)
SELECT
  CASE state WHEN 1 THEN 'Running'
             WHEN 0 THEN 'Stopped'
             ELSE 'Other (' || CAST(state AS TEXT) || ')'
  END AS "State",
  ROUND(CAST(minutes_in_state AS NUMERIC), 1) AS "Minutes"
FROM durations
ORDER BY minutes_in_state DESC""",
    overrides=[width_override("State", 200)])); pid += 1

# Donut showing the same data
DONUT_JS = """\
let f = data.series[0]?.fields;
if (!f || f.length < 2) {
  return { title: { text: 'No data', left:'center', top:'middle',
                    textStyle:{color:'#888'}}};
}
const labels = f[0].values;
const values = f[1].values;
return {
  tooltip: { trigger: 'item' },
  legend:  { bottom: 0 },
  series: [{
    type: 'pie',
    radius: ['45%', '70%'],
    label: { formatter: '{b}\\n{d}%' },
    data: labels.map((n, i) => ({ name: n, value: values[i] })),
    itemStyle: { color: '#888' }
  }]
};
"""
panels.append(echarts(pid, "[Analyst] State — distribution donut",
                      12, 10, 12, 8,
                      sql="""WITH state_changes AS (
  SELECT
    systime,
    COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) AS state,
    LEAD(systime) OVER (ORDER BY systime) AS next_systime
  FROM telemetry
  WHERE $__timeFilter(systime)
    AND uuid = (${state_signal:raw})
    AND is_delta IN ('t', 'f')
)
SELECT
  CASE state WHEN 1 THEN 'Running'
             WHEN 0 THEN 'Stopped'
             ELSE 'Other'
  END AS metric,
  SUM(EXTRACT(EPOCH FROM (
    LEAST(COALESCE(next_systime, NOW()), $__timeTo()::timestamptz)
    - GREATEST(systime,                    $__timeFrom()::timestamptz)
  ))) / 60.0 AS value
FROM state_changes
WHERE systime < $__timeTo()::timestamptz
  AND COALESCE(next_systime, NOW()) >= $__timeFrom()::timestamptz
GROUP BY 1
ORDER BY value DESC""",
                      get_option_js=DONUT_JS)); pid += 1

# --- Row: counter -------------------------------------------------------
panels.append(row(pid, "🔢 Counter analysis (with reset detection)", 18)); pid += 1

# Cumulative production count from counter signal that may reset to 0
counter_sql = """WITH raw AS (
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
      WHEN prev_val IS NULL OR val < prev_val THEN val
      ELSE val - prev_val
    END AS delta
  FROM raw
)
SELECT
  systime AS time,
  SUM(delta) OVER (ORDER BY systime) AS "Cumulative count"
FROM deltas
ORDER BY systime"""
panels.append(timeseries(pid, "[Analyst] Counter — cumulative (reset-aware)",
                          0, 19, 24, 8, sql=counter_sql, unit="short")); pid += 1

# --- Row: correlation ---------------------------------------------------
panels.append(row(pid, "🔗 Two-signal correlation", 27)); pid += 1

# State and temp on same time axis — bucketed and joined
correlation_sql = """\
WITH state_b AS (
  SELECT $__timeGroup(systime, '5s') AS ts,
         AVG(COALESCE(
           CAST(value_double  AS NUMERIC),
           CAST(value_integer AS NUMERIC),
           CAST(CAST(value_bool AS INTEGER) AS NUMERIC)
         )) AS val
  FROM telemetry
  WHERE $__timeFilter(systime)
    AND uuid = (${state_signal:raw})
    AND is_delta IN ('t', 'f')
  GROUP BY 1
),
temp_b AS (
  SELECT $__timeGroup(systime, '5s') AS ts,
         AVG(COALESCE(
           CAST(value_double  AS NUMERIC),
           CAST(value_integer AS NUMERIC),
           CAST(CAST(value_bool AS INTEGER) AS NUMERIC)
         )) AS val
  FROM telemetry
  WHERE $__timeFilter(systime)
    AND uuid = (${temp_signal:raw})
    AND is_delta IN ('t', 'f')
  GROUP BY 1
)
SELECT
  state_b.ts AS time,
  state_b.val AS "State",
  temp_b.val  AS "Temperature"
FROM state_b
LEFT JOIN temp_b ON temp_b.ts = state_b.ts
ORDER BY state_b.ts"""
panels.append(timeseries(pid, "[Analyst] Correlation — state + temperature",
                          0, 28, 24, 8, sql=correlation_sql, unit="short")); pid += 1

# ---------------------------------------------------------------------------
# Build & save
# ---------------------------------------------------------------------------
dashboard = build_dashboard(
    title="Signal Investigation — Analyst View",
    panels=panels,
    variables=variables,
    refresh="30s",
    hide_timepicker=False,
)

OUT = "/home/claude/references/examples/timeseries_analyst.json"
with open(OUT, "w") as f:
    json.dump(dashboard, f, indent=2)
print("wrote", OUT)
