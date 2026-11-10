"""
Worked example — relational archetype, analyst tier.

Domain: machine downtime investigation.
Audience: CI engineer / planner, drilling into "why did the spike happen".
Question: what caused it, on which machines, in which window?

Run this script to regenerate `relational_analyst.json`.

Compared to the manager view, this dashboard:
- Uses $__timeFilter() / $__timeGroup() (full time picker is enabled)
- Has the full filter set (machine, reason, severity, min duration, source)
- Includes data quality KPIs and drill-down detail tables
- Follows the [Analyst] panel naming convention
"""

import json, sys
sys.path.insert(0, "/home/claude/references")
from dashboard_builder import (
    stat, table_panel, echarts, timeseries, row, text,
    traffic_light, reverse_traffic_light,
    color_cell_override, width_override,
    var_query, var_custom, var_textbox, build_dashboard,
)

# ---------------------------------------------------------------------------
# Variables — full filter set
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
ORDER BY m.name""", multi=True, include_all=True),
    var_query("reason", "Reason", """
SELECT dr.name AS __text, dr.id AS __value
FROM downtime_reasons dr
WHERE dr.is_archived = false
  AND dr.is_active   = true
  AND dr.account_id IN ($account)
ORDER BY dr.name""", multi=True, include_all=True),
    var_custom("severity", "Severity",
               ["all", "critical", "major", "minor"],
               default="all"),
    var_custom("auto_detected", "Source",
               [("All", -1), ("Auto", 1), ("Manual", 0)],
               default="All"),
    var_textbox("min_duration_min", "Min duration (min)", default="0"),
]

# ---------------------------------------------------------------------------
# Canonical WHERE — used in every analyst panel
# ---------------------------------------------------------------------------
WHERE = """\
WHERE di.is_archived = false
  AND $__timeFilter(di.start_time)
  AND di.machine_id IN ($machine)
  AND di.account_id IN ($account)
  AND ((di.reason_id IN ($reason)) OR di.reason_id IS NULL)
  AND ('$severity' = 'all' OR CAST(dr.severity AS TEXT) = '$severity')
  AND ($auto_detected = -1
       OR CAST(di.is_auto_detected AS INTEGER) = $auto_detected)
  AND EXTRACT(EPOCH FROM (COALESCE(di.end_time, NOW()) - di.start_time)) / 60.0
        >= $min_duration_min"""

# Window-clipped duration in minutes (for duration-summing queries)
CLIP = """\
LEAST(COALESCE(di.end_time, NOW()), $__timeTo()::timestamptz)
- GREATEST(di.start_time,             $__timeFrom()::timestamptz)"""

# Interval-overlap WHERE — needed for clipped queries instead of $__timeFilter
OVERLAP_WHERE = """\
WHERE di.is_archived = false
  -- interval-overlap: dropping rows fully outside the visible window
  AND di.start_time   <  $__timeTo()::timestamptz
  AND COALESCE(di.end_time, NOW()) >= $__timeFrom()::timestamptz
  AND di.machine_id IN ($machine)
  AND di.account_id IN ($account)
  AND ((di.reason_id IN ($reason)) OR di.reason_id IS NULL)
  AND ('$severity' = 'all' OR CAST(dr.severity AS TEXT) = '$severity')
  AND ($auto_detected = -1
       OR CAST(di.is_auto_detected AS INTEGER) = $auto_detected)"""

# ---------------------------------------------------------------------------
# Panels
# ---------------------------------------------------------------------------
panels = []
pid = 200

# --- Row: KPIs ------------------------------------------------------------
panels.append(row(pid, "🎯 KPIs — selected window", 0)); pid += 1

panels.append(stat(pid, "[Analyst] Downtime — Total clipped",
                   0, 1, 4, 4,
                   sql=f"""SELECT
  ROUND(CAST(SUM(EXTRACT(EPOCH FROM ({CLIP}))) / 60.0 AS NUMERIC), 1) AS minutes
FROM downtime_incidents di
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
{OVERLAP_WHERE}""",
                   unit="m",
                   thresholds=traffic_light(yellow=120, red=480))); pid += 1

panels.append(stat(pid, "[Analyst] Downtime — Incidents",
                   4, 1, 4, 4,
                   sql=f"""SELECT COUNT(*) AS n
FROM downtime_incidents di
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
{WHERE}""", unit="short")); pid += 1

panels.append(stat(pid, "[Analyst] Downtime — MTTR (closed)",
                   8, 1, 4, 4,
                   sql=f"""SELECT
  ROUND(CAST(AVG(EXTRACT(EPOCH FROM (di.end_time - di.start_time))) / 60.0
       AS NUMERIC), 1) AS mttr_min
FROM downtime_incidents di
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
WHERE di.end_time IS NOT NULL
  AND $__timeFilter(di.start_time)
  AND di.machine_id IN ($machine)
  AND di.account_id IN ($account)
  AND ((di.reason_id IN ($reason)) OR di.reason_id IS NULL)""",
                   unit="m",
                   thresholds=traffic_light(yellow=45, red=90))); pid += 1

panels.append(stat(pid, "[Analyst] Downtime — P95 duration",
                   12, 1, 4, 4,
                   sql=f"""SELECT
  ROUND(CAST(PERCENTILE_CONT(0.95) WITHIN GROUP (
    ORDER BY EXTRACT(EPOCH FROM (di.end_time - di.start_time)) / 60.0
  ) AS NUMERIC), 1) AS p95_min
FROM downtime_incidents di
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
WHERE di.end_time IS NOT NULL
  AND $__timeFilter(di.start_time)
  AND di.machine_id IN ($machine)
  AND di.account_id IN ($account)""", unit="m")); pid += 1

panels.append(stat(pid, "[Analyst] Downtime — % unclassified",
                   16, 1, 4, 4,
                   sql=f"""WITH t AS (
  SELECT di.reason_id
  FROM downtime_incidents di
  LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
  {WHERE}
)
SELECT CASE WHEN COUNT(*) = 0 THEN 0
            ELSE ROUND(100.0 *
                       SUM(CASE WHEN reason_id IS NULL THEN 1 ELSE 0 END)
                       / COUNT(*), 1)
       END AS unassigned_pct
FROM t""", unit="percent",
                   thresholds=traffic_light(yellow=10, red=25))); pid += 1

panels.append(stat(pid, "[Analyst] Downtime — % auto-detected",
                   20, 1, 4, 4,
                   sql=f"""WITH t AS (
  SELECT di.is_auto_detected
  FROM downtime_incidents di
  LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
  {WHERE}
)
SELECT CASE WHEN COUNT(*) = 0 THEN 0
            ELSE ROUND(100.0 *
                       SUM(CASE WHEN is_auto_detected THEN 1 ELSE 0 END)
                       / COUNT(*), 1)
       END AS auto_pct
FROM t""", unit="percent")); pid += 1

# --- Row: trends ----------------------------------------------------------
panels.append(row(pid, "📈 Trends — bucketed views", 5)); pid += 1

# Stacked downtime by reason
panels.append(timeseries(pid, "[Analyst] Downtime — by reason (stacked)",
                          0, 6, 12, 8,
                          sql=f"""SELECT
  $__timeGroup(di.start_time, $__interval) AS time,
  COALESCE(dr.name, 'Unassigned')          AS metric,
  ROUND(CAST(SUM(EXTRACT(EPOCH FROM ({CLIP}))) / 60.0 AS NUMERIC), 1) AS value
FROM downtime_incidents di
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
{OVERLAP_WHERE}
GROUP BY 1, 2
ORDER BY 1""", unit="m")); pid += 1

# Rolling 7-day MTTR
panels.append(timeseries(pid, "[Analyst] Downtime — MTTR rolling 7-day",
                          12, 6, 12, 8,
                          sql=f"""WITH daily AS (
  SELECT
    date_trunc('day', di.start_time) AS day,
    AVG(EXTRACT(EPOCH FROM (di.end_time - di.start_time))) / 60.0 AS mttr_min
  FROM downtime_incidents di
  LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
  WHERE di.end_time IS NOT NULL
    AND $__timeFilter(di.start_time)
    AND di.machine_id IN ($machine)
    AND di.account_id IN ($account)
  GROUP BY 1
)
SELECT
  day AS time,
  AVG(mttr_min) OVER (ORDER BY day ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)
    AS "MTTR 7d rolling [min]"
FROM daily
ORDER BY day""", unit="m")); pid += 1

# --- Row: rankings -------------------------------------------------------
panels.append(row(pid, "🏆 Rankings", 14)); pid += 1

# Pareto by machine × reason
pareto_sql = f"""SELECT
  m.name || ' :: ' || COALESCE(dr.name, 'Unassigned') AS metric,
  ROUND(CAST(SUM(EXTRACT(EPOCH FROM ({CLIP}))) / 60.0 AS NUMERIC), 1) AS value
FROM downtime_incidents di
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
LEFT JOIN machines m          ON m.id  = di.machine_id
{OVERLAP_WHERE}
GROUP BY 1
ORDER BY value DESC
LIMIT 20"""

# Use a simple ECharts Pareto template (defensive splash screens included)
PARETO_JS = """\
let data = data.series[0]?.fields;
if (!data || data.length < 2) {
  return { title: { text: 'No data', left: 'center', top: 'middle',
                    textStyle: { color: '#888' } } };
}
const labels = data[0].values;
const values = data[1].values;
let cum = 0; const total = values.reduce((a,b)=>a+b, 0);
const cumPct = values.map(v => { cum += v; return total ? (cum/total*100) : 0; });
return {
  tooltip: { trigger: 'axis' },
  grid: { left: 60, right: 60, top: 30, bottom: 80 },
  xAxis: { type: 'category', data: labels, axisLabel: { rotate: 35 } },
  yAxis: [
    { type: 'value', name: 'Minutes' },
    { type: 'value', name: '%', max: 100, axisLabel: { formatter: '{value}%' } }
  ],
  series: [
    { type: 'bar',  data: values, name: 'Minutes', itemStyle: { color: '#888' } },
    { type: 'line', data: cumPct, name: 'Cumulative %', yAxisIndex: 1,
      lineStyle: { color: '#222' }, symbol: 'circle' }
  ]
};
"""
panels.append(echarts(pid, "[Analyst] Downtime — Pareto by machine × reason",
                       0, 15, 12, 9,
                       sql=pareto_sql, get_option_js=PARETO_JS)); pid += 1

# Machine ranking table
panels.append(table_panel(pid, "[Analyst] Downtime — by machine",
                           12, 15, 12, 9,
                           sql=f"""SELECT
  m.name AS "Machine",
  COUNT(*) AS "Incidents",
  ROUND(CAST(SUM(EXTRACT(EPOCH FROM (COALESCE(di.end_time, NOW()) - di.start_time)))
        / 60.0 AS NUMERIC), 1) AS "Total min",
  ROUND(CAST(AVG(EXTRACT(EPOCH FROM (COALESCE(di.end_time, NOW()) - di.start_time)))
        / 60.0 AS NUMERIC), 1) AS "Avg min",
  ROUND(CAST(MAX(EXTRACT(EPOCH FROM (COALESCE(di.end_time, NOW()) - di.start_time)))
        / 60.0 AS NUMERIC), 1) AS "Worst min"
FROM downtime_incidents di
JOIN machines m ON m.id = di.machine_id
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
{WHERE}
GROUP BY m.name
ORDER BY "Total min" DESC
LIMIT 50""",
    overrides=[
        color_cell_override("Total min", traffic_light(yellow=60, red=180), unit="m"),
        width_override("Machine", 220),
    ])); pid += 1

# --- Row: drill-down -----------------------------------------------------
panels.append(row(pid, "🔎 Drill-down — incident detail", 24)); pid += 1

panels.append(table_panel(pid, "[Analyst] Downtime — Incident detail (top 500)",
                           0, 25, 24, 11,
                           sql=f"""SELECT
  di.start_time AS "Start",
  di.end_time   AS "End",
  m.name        AS "Machine",
  COALESCE(dr.name, 'Unassigned')              AS "Reason",
  COALESCE(CAST(dr.severity AS TEXT), 'unset') AS "Severity",
  ROUND(CAST(EXTRACT(EPOCH FROM (COALESCE(di.end_time, NOW()) - di.start_time))
        / 60.0 AS NUMERIC), 1) AS "Duration (min)",
  CASE WHEN di.is_auto_detected THEN 'auto' ELSE 'manual' END AS "Source",
  COALESCE(u.first_name || ' ' || u.last_name, '—') AS "Reported by",
  di.affected_item AS "Affected",
  di.notes         AS "Notes"
FROM downtime_incidents di
LEFT JOIN machines m          ON m.id  = di.machine_id
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
LEFT JOIN users u             ON u.id  = di.reported_by_id
{WHERE}
ORDER BY "Duration (min)" DESC
LIMIT 500""",
    overrides=[
        width_override("Machine", 180),
        width_override("Reason",  220),
        width_override("Notes",   320),
        color_cell_override("Duration (min)", traffic_light(yellow=15, red=60), unit="m"),
    ])); pid += 1

# ---------------------------------------------------------------------------
# Build & save
# ---------------------------------------------------------------------------
dashboard = build_dashboard(
    title="Downtime — Analyst View (Historical)",
    panels=panels,
    variables=variables,
    refresh="30s",
    hide_timepicker=False,
)

OUT = "/home/claude/references/examples/relational_analyst.json"
with open(OUT, "w") as f:
    json.dump(dashboard, f, indent=2)
print("wrote", OUT)
