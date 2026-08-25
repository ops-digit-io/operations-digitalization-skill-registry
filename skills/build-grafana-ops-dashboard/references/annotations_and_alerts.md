# annotations_and_alerts.md — Annotations and panel alerts

Two Grafana features that show up at the operations and analyst tiers but are absent from this skill's main patterns. Both have specific design constraints in the ops context.

---

## Annotations — overlaying events on time series

An annotation is a vertical line (or band) drawn on time-series panels at a specified timestamp, with a hover label. Common uses in ops:

- Shift change boundaries
- Deployment / configuration changes
- Known incidents (planned downtime, retooling, audits)
- External events (power outages, supplier delivery delays)
- Alarm transitions

### When to use them

- **Always** at the operations tier — operators benefit from seeing recent events as context for what they're looking at.
- **Often** at the analyst tier — annotations provide "why did the spike happen?" answers without leaving the dashboard.
- **Rarely** at the manager tier — clutter outweighs value when the question is week-over-week.

### Two ways to source them

**1. Static annotations** — manually entered, stored in Grafana's database. Useful for "team knows this happened" markers (releases, audits). Created via the Annotations sidebar in the dashboard editor.

**2. Query annotations** — sourced from the same database the dashboard queries. The most common pattern in ops is "draw a line for every shift change" or "highlight every active downtime incident as a band."

### Query annotation pattern — point events

For point-in-time events (deployments, alarms, shift starts):

```sql
SELECT
  s.start_time AS time,
  s.label      AS title,
  s.notes      AS text,
  ARRAY[s.shift_name, m.name] AS tags
FROM shift_starts s
JOIN machines m ON m.id = s.machine_id
WHERE $__timeFilter(s.start_time)
  AND m.id IN ($machine);
```

Required column aliases: `time` (always), `title` (always). Optional: `text`, `tags`, `timeEnd` (turns it into a band).

### Query annotation pattern — bands (relational archetype)

For interval events (incidents, scheduled maintenance windows):

```sql
SELECT
  di.start_time                       AS time,
  COALESCE(di.end_time, NOW())        AS timeEnd,
  COALESCE(dr.name, 'Unassigned')     AS title,
  di.notes                            AS text,
  ARRAY[m.name, COALESCE(dr.severity::text, 'unset')] AS tags
FROM downtime_incidents di
JOIN machines m              ON m.id  = di.machine_id
LEFT JOIN downtime_reasons dr ON dr.id = di.reason_id
WHERE $__timeFilter(di.start_time)
  AND m.id IN ($machine)
  AND di.is_archived = false
ORDER BY di.start_time;
```

The presence of `timeEnd` turns the annotation from a vertical line into a translucent band spanning the interval. Useful for visualizing "the machine was down during this whole window."

### Query annotation pattern — bands (timeseries archetype)

Derive intervals from successive state samples using LEAD:

```sql
WITH state_changes AS (
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
  systime                    AS time,
  COALESCE(next_systime, NOW()) AS timeEnd,
  CASE state
    WHEN 1 THEN 'Running'
    WHEN 0 THEN 'Stopped'
    ELSE  'Unknown'
  END AS title
FROM state_changes
WHERE state = 0;   -- only annotate "Stopped" intervals
```

This produces a band over every period the machine was stopped, overlaid on whatever time-series panels are showing concurrent signals (output, temperature, etc.).

### Performance notes for annotations

- Annotations run on **every panel** in the dashboard. A slow annotation query slows everything.
- Cap result count: `LIMIT 200` is usually enough. More than that and the panel is too cluttered to read anyway.
- Use the same `$__timeFilter()` macro the panels use — annotations share the dashboard's time range.
- If the annotation query hits a high-cardinality table, narrow it with the existing variables (`$machine`, `$account`).

---

## Panel alerts — notifying when a metric breaches threshold

Grafana panel alerts evaluate a query on a schedule and fire when the result crosses a defined threshold. In ops dashboards, common alert use cases:

- "Downtime in the last 30 minutes exceeds X" (operations)
- "Uncategorized incident percentage exceeds Y" (analyst — data quality)
- "MTTR week-over-week increased by more than Z%" (manager — degradation signal)
- "Signal X has not produced a sample in the last 5 minutes" (operations — connectivity check)

### Design constraints

Alerts should target one specific decision and one specific recipient. Generic "something is wrong" alerts get muted within a week. Specific "OEE on Line 3 dropped below 70% during shift A" alerts get acted on.

### Where alerts live

In the modern Grafana model (post-8.0), alerts are defined in a separate "Alerting" section, not on the panel itself. The dashboard panel is the *visualization* of the metric; the alert rule queries the same data and lives separately. This decoupling means:

- Alerts can be reused across dashboards
- Alerts survive panel deletion
- Alert state isn't visible on the dashboard unless you add an Alert List panel

For dashboards delivered under this skill, default to defining alerts as separate alert rules — not as panel-attached legacy alerts. Note the matching panel in the alert rule's annotations field so the on-call engineer can find the visualization quickly.

### Alert rule pattern — relational archetype

```sql
-- Alert: "Active downtime exceeds 30 minutes in the last hour"
SELECT
  m.name AS metric,
  ROUND(SUM(EXTRACT(EPOCH FROM (
    LEAST(COALESCE(di.end_time, NOW()), NOW())
    - GREATEST(di.start_time, NOW() - INTERVAL '1 hour')
  ))) / 60.0, 1) AS value
FROM downtime_incidents di
JOIN machines m ON m.id = di.machine_id
WHERE di.is_archived = false
  AND di.start_time   <  NOW()
  AND COALESCE(di.end_time, NOW()) >= NOW() - INTERVAL '1 hour'
  AND m.is_ignored = false
GROUP BY m.name
HAVING SUM(EXTRACT(EPOCH FROM (
    LEAST(COALESCE(di.end_time, NOW()), NOW())
    - GREATEST(di.start_time, NOW() - INTERVAL '1 hour')
  ))) / 60.0 > 30;
```

Each row returned represents a machine that's breached the threshold. Grafana fires one alert instance per row (per `metric` label), so the on-call gets per-machine notification.

### Alert rule pattern — timeseries connectivity check

A specific alert that catches "the data pipeline broke" — equally important as any business alert:

```sql
-- Alert: "Signal hasn't produced a sample in 5 minutes"
SELECT
  s.name AS metric,
  EXTRACT(EPOCH FROM (NOW() - MAX(t.systime))) / 60.0 AS value
FROM signal_metadata s
LEFT JOIN telemetry t ON t.uuid = s.uuid
WHERE s.is_active = true
GROUP BY s.name
HAVING MAX(t.systime) IS NULL
    OR MAX(t.systime) < NOW() - INTERVAL '5 minutes';
```

`value` is "minutes since last sample." Alert fires when this exceeds the defined threshold (e.g. 5).

### Avoiding alert fatigue

The single biggest failure mode for ops alerting is too many alerts firing too often. Three rules:

1. **Each alert rule has a clear owner.** No owner → delete the rule. Unowned alerts get muted within weeks.
2. **Threshold calibrated to the noise floor.** If the metric crosses the threshold three times a day under normal operation, the threshold is wrong, not the operation.
3. **`for` duration prevents flapping.** Set `for: 5m` so the metric must breach for 5 minutes before firing. Catches sustained problems; ignores transient blips.

### Audit checklist for alerts

- [ ] Each alert rule has a named owner
- [ ] Each alert references the matching dashboard panel in its annotations
- [ ] Threshold is set above the empirical noise floor for that metric
- [ ] `for` duration is set (typically 5–15 minutes for ops metrics)
- [ ] Alert grouping prevents one root cause from producing 50 notifications
- [ ] Recipients are aware they're on the receiving end before the alert is enabled

---

## When to skip both

Some dashboards genuinely shouldn't have annotations or alerts:

- One-shot analytical dashboards built for a single review meeting
- Manager dashboards where the goal is reading numbers, not getting paged
- Dashboards in development environments where alert noise would teach the wrong reflex

Default to including annotations at operations and analyst tiers, alerts only when there's a clear owner and clear action. When in doubt, leave them out — they're easier to add later than to remove without making someone unhappy.
