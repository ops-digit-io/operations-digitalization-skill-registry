---
type: Skill Reference
title: Ops grafana dashboards
description: "The department's ops-grafana-dashboards: DATATRON / Grafana dashboards end to end - tag selection, Grafana 8.5 JSON (schemaVersion 36), ECharts panels, and the stakeholder pitch deck with an auditable savings model."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [dashboard, grafana, datatron, department-package]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/30-skills/ops-grafana-dashboards.zip/SKILL.md, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `ops-grafana-dashboards.zip/SKILL.md` (the master).

# Ops Grafana Dashboards (DATATRON)

Design importable Grafana JSON dashboards over the DATATRON telemetry schema. Target platform: **Grafana 8.5.22, schemaVersion 36**, dark style, PostgreSQL/TimescaleDB datasources, plus the `bilibala-echarts-panel` plugin for anything the core panels can't draw.

## The flow

```
 unselected tags ──▶ [1] tag selection ──┐
                                          ├──▶ [2] dashboard JSON ──▶ [3] confirm ──▶ [4] stakeholder pitch deck
 already-selected tags ───────────────────┘
```

- **[1] Tag selection** — a tag export/audit arrives; curate the datapoints worth collecting and list the disabled ones that need enabling (see *Datapoint enablement*).
- **[2] Dashboard** — build the Grafana JSON per the family, query and panel conventions below.
- **[3] Confirm** — the user says the dashboard is the one they want.
- **[4] Pitch** — build the stakeholder deck (see *Stage 4*). It also runs standalone: the user hands over a dashboard JSON (plus optional screenshots) and asks for the pitch directly, with no tag or build stage.

Stage 4 never runs unasked in the middle of stage 2. Offer it in one line once the dashboard is done, or run it when the user asks.

## The four dashboard families

| Family | Purpose | Signature panels | Typical time range / refresh |
|---|---|---|---|
| **Andon Board** (L1) | Shop-floor TV wall, one row or card per machine, glanceable | text headers + `stat` (colorMode background) + ECharts cards | `now-24h`, refresh `30s` |
| **Production Overview** (L2) | Per-machine shift/production KPIs | stat header strip, state-timeline, hourly output, cycle time, state durations | `now-24h`, manual refresh |
| **Process Values** (L3) | Deep PLC process parameters for engineers | collapsed rows of `timeseries`, raw dataset table | `now-24h` |
| **Alert Dashboard** | Machine errors across many machines | barchart + donut + two tables, `-- Mixed --` datasource | `now-3h`, interval variable |
| **Performance / Cycle-Time Analysis** | Per-piece or per-cycle quality & throughput | SPC charts, histograms, heatmaps, Pareto, per-piece drill-down table | `now-12h`/`now-24h` |

### L1 → L2 → L3 drill-down
- **L1 Card View / Andon**: one panel per machine, hard-coded UUIDs (no templating), a status-colored card, and a click target that opens L2.
- **L2 Production Overview**: templated (`area`→`datatron`→`plc`), one machine at a time.
- **L3 Process Values**: same variable chain, one collapsed row per subsystem.

The L1 → L2 jump is done inside the ECharts card by opening a fully-parameterized L2 URL: every hidden UUID variable is passed as a URL-encoded `var-<name>=%27<uuid>%27` (the `%27` are the single quotes the resolver variables normally produce). Build that URL once per machine card:

```
https://<host>/grafana/d/<l2-uid>/<slug>?orgId=1&var-datasource=TelemetryPLC
  &var-area=4&var-datatron=1&var-plc=79,84
  &var-machine_state=%27adece74e-...%27&var-cycle_time=%274ba4bac7-...%27&...
```

## Schema

### `telemetry` (DS_TELEMETRYPLC / DS_QUACKITO)
```
systime        TIMESTAMPTZ   event timestamp
uuid           UUID          datapoint UUID (joins to ConfigRepo.data_points)
is_delta       BOOLEAN       't' = value changed at this sample, 'f' = periodic resample
value_double   DOUBLE
value_integer  BIGINT
value_bool     BOOLEAN
value_string   TEXT          strings AND JSON payloads
```

### ConfigRepo (DS_CONFIGREPO)
```
locations    (id, name, parent_id)      -- recursive plant hierarchy
datatrons    (id, name, location_id)    -- edge devices
devices      (id, name, datatron_id)    -- PLCs / endpoints
data_points  (uuid, label, device_id, is_archived)
```

### Datasource inputs — declare what the dashboard actually uses
```json
"__inputs": [
  { "name": "DS_TELEMETRYPLC", "label": "TelemetryPLC", "type": "datasource", "pluginId": "postgres" },
  { "name": "DS_CONFIGREPO",   "label": "ConfigRepo",   "type": "datasource", "pluginId": "postgres" },
  { "name": "DS_DATADASH",     "label": "Datadash",     "type": "datasource", "pluginId": "postgres" },
  { "name": "DS_QUACKITO",     "label": "Quackito",     "type": "datasource", "pluginId": "postgres" }
]
```
`DS_DATADASH` serves the `locations` hierarchy (AREA variable). `DS_QUACKITO` is the alternate telemetry store — expose it through a datasource variable so users can switch:

```json
{ "type": "datasource", "name": "datasource", "label": "DATASOURCE",
  "query": "postgres", "regex": "/TelemetryPLC|Quackito/" }
```

Andon boards that are hard-wired to one machine declare only `DS_TELEMETRYPLC`.

## Value extraction — always the same two lines

```sql
COALESCE(value_double, value_integer, value_bool::integer) AS "Metric"   -- numeric/boolean
value_string AS "Partnumber"                                             -- strings
```
For arithmetic that needs numeric typing: `COALESCE(value_double, value_integer::numeric)`; for a bigint anchor: `COALESCE(value_integer, value_double::bigint)`.

### `is_delta` decides the semantics — get this right
| Filter | Meaning | Use for |
|---|---|---|
| `is_delta IN ('t','f')` | every stored sample | states, temperatures, pressures, anything you want a continuous line for |
| `is_delta IN ('t')` / `= 't'` | change events only | counters, part-produced triggers, per-piece anchors, cycle-completion events |

Counting a `is_delta='t'` boolean trigger is how "parts produced" is derived. Filtering `AND value_double > 0` next to it removes the machine's spurious zeros — add that comment inline so the next reader knows why.

## Two time-filter dialects (both are in production — be consistent within a dashboard)

**Dialect A — machine dashboards (L1/L2/L3):**
```sql
SELECT
  time_bucket('30s', systime) AS "time",
  COALESCE(value_double, value_integer, value_bool::integer) AS "MachineState"
FROM telemetry
WHERE
  $__timeFilter(systime) AND
  uuid = (${machine_state:raw}) AND
  is_delta IN ('t','f')
GROUP BY 1,2
ORDER BY 1
```
`uuid = (${var:raw})` for a single-valued resolver, `uuid IN (${var:raw})` when the resolver may return several.

**Dialect B — analysis/alert dashboards:**
```sql
WHERE uuid IN (${u_var:raw})
  AND systime >= $__timeFrom()::timestamptz
  AND systime <  $__timeTo()::timestamptz
```
or, inside `LATERAL` subqueries where macros can't be nested, the literal form:
```sql
WHERE systime >= '${__from:date:iso}' AND systime <= '${__to:date:iso}'
```

`$__interval` is used on BMW-style dashboards where the bucket should follow the panel width; a fixed `time_bucket('30s', …)` is used where cycle resolution matters. A `bucket` interval variable (`1m,5m,15m,1h,6h,1d`) is preferred on analysis dashboards.

## The cascading variable chain

Order matters: `datasource → area → datatron → plc → hidden UUID resolvers`.

**AREA** (DS_DATADASH) — leaf nodes of the recursive location hierarchy:
```sql
WITH RECURSIVE hierarchy AS (
    SELECT id, name::text AS full_name FROM locations WHERE parent_id IS NULL
  UNION ALL
    SELECT l.id, h.full_name || ' | ' || l.name
    FROM locations l JOIN hierarchy h ON l.parent_id = h.id
)
SELECT id AS __value, full_name AS __text
FROM hierarchy
WHERE id NOT IN (SELECT parent_id FROM locations WHERE parent_id IS NOT NULL)
  AND full_name ILIKE '%Crippa Bending%';
```
Scope with `ILIKE '%<area>%'`, then narrow further with the variable's `regex` (e.g. `/(?!.*Bending)/` to exclude a sub-area).

**DATATRON** (DS_CONFIGREPO) — pretty-print the edge-device name:
```sql
SELECT upper(split_part(datatrons.name, '-', 2)) AS __text, datatrons.id AS __value
FROM datatrons WHERE location_id IN ($area)
```
Name formats differ per plant: `split_part(name,'-',2)`, `split_part(name,' // ',1)`, or `ILIKE '%EQ40015942%'` when the dashboard is pinned to one machine.

**DEVICES / PLC** — strip the virtual-device suffix and aggregate ids:
```sql
SELECT REGEXP_REPLACE(devices.name, ' - Virtual Device$', '') AS __text,
       STRING_AGG(devices.id::text, ',') AS __value
FROM devices WHERE devices.datatron_id IN ($datatron)
GROUP BY __text ORDER BY __text;
```
Use `refresh: 2` (on time range change) for this one so it re-resolves; `refresh: 1` elsewhere.

**Hidden UUID resolvers** — one per signal, `hide: 2`, name == label of the datapoint:
```sql
SELECT CONCAT('''', uuids, '''')
FROM (SELECT 'group_by_helper',
             array_to_string(array_agg(DISTINCT dp.uuid), ''',''') AS uuids
      FROM data_points dp
      INNER JOIN devices dev ON dp.device_id = dev.id
      WHERE dev.id IN ($plc)
        AND dp.is_archived = 'f'
        AND dp.label = 'CYCLETIME_NR'          -- or LIKE '%<node path tail>'
      GROUP BY 1) u;
```
The `CONCAT`/`array_to_string` dance produces `'uuid1','uuid2'` — already quoted, which is why the SQL says `uuid IN (${var:raw})` with no quotes of its own. Match on the standardized label (`CYCLETIME_NR`, `PARTPRODUCEDTRIGGER_NR`, `ALERTMESSAGE_NR`) when one exists, otherwise `LIKE '%'` + the PLC node-path tail (`'%Trägerinfo_Station_Letzter.r_Pressvorgang_Rohr_MaxKraft'`).

Andon boards and single-machine card views skip variables entirely and inline `uuid IN ('dd6b2ac7-…')`.

## Reusable panel recipes

### Machine state — one mapping, four panels
State codes and colors are fixed across the estate. Reuse verbatim:
```json
"mappings": [{ "type": "value", "options": {
  "0": { "text": "Stop",      "color": "red",    "index": 3 },
  "1": { "text": "Manual",    "color": "yellow", "index": 1 },
  "2": { "text": "Automatic", "color": "green",  "index": 0 },
  "5": { "text": "Setup",     "color": "purple", "index": 2 }}}]
```
Binary machines use `0 = Stopped (red) / 1 = Running (green)`. Feed the same query into a `stat` (colorMode `background`, `lastNotNull`), a full-width `state-timeline` (`fillOpacity: 70`, `lineWidth: 0`, `mergeValues: true`, `rowHeight: 0.9`), and the duration analyses below. On the piechart the labels come back as text, so map with `"type": "regex"` patterns (`Manual.*`, `Setup.*`, …) to keep the same colors.

### Header strip — identity stats from ConfigRepo, not telemetry
Workplace/machine identity is derived from the device name, so the stat panel queries **ConfigRepo** and reduces on `/^__text$/`:
```sql
SELECT (regexp_replace(split_part(regexp_replace(devices.name,' - Virtual Device$',''),' ',2),'_.*$','')
        || ' ' || split_part(devices.name,' ',1)) AS __text,
       STRING_AGG(devices.id::text, ',') AS __value
FROM devices WHERE devices.datatron_id IN ($datatron) AND devices.id IN ($plc)
GROUP BY __text ORDER BY __text;
```
Options: `colorMode: background`, threshold color `transparent`, `text.valueSize: 30`, `textMode: value` (or `value_and_name` when the label helps). Order/mould/material stats use `textMode: "value_and_name"` with `reduceOptions.fields: "/^Mould$/"`.

### State durations per shift (table)
Production day starts at **06:00** and runs 24h; shifts are **06-14 / 14-22 / 22-06**. Compute durations with `LEAD`, then clip each state segment against each shift window:
```sql
WITH time_window AS (
  SELECT date_trunc('day', $__timeFrom()::timestamptz) + INTERVAL '6 hours'  AS prod_start,
         date_trunc('day', $__timeFrom()::timestamptz) + INTERVAL '30 hours' AS prod_end
),
raw_states AS (
  SELECT t.systime, COALESCE(t.value_double::int, t.value_integer, t.value_bool::int) AS state
  FROM telemetry t CROSS JOIN time_window tw
  WHERE t.uuid = (${machine_state:raw})
    AND t.systime >= tw.prod_start AND t.systime < tw.prod_end
    AND t.is_delta IN ('t','f')
),
state_with_next AS (
  SELECT systime AS time, state, LEAD(systime) OVER (ORDER BY systime) AS next_time FROM raw_states
),
durations AS (
  SELECT time AS start_time,
         COALESCE(next_time, (SELECT prod_end FROM time_window)) AS end_time, state
  FROM state_with_next
)
-- then: JOIN a 3-row shift_series and sum
--   EXTRACT(EPOCH FROM LEAST(end_time, s.prod_end) - GREATEST(start_time, s.prod_start))
--   where the segment overlaps the shift; percentage = 100 * duration / shift total
```

### State durations over the panel range (piechart)
Same `LEAD` skeleton, but bounded by `$__timeFrom()/$__timeTo()` and with `COALESCE(next_time - time, INTERVAL '1 second')` for the open last segment. Format HH:MM:SS **portably** — no `TO_CHAR` on a computed interval:
```sql
LPAD(CAST(CAST(sec AS BIGINT)/3600 AS TEXT),2,'0') || ':' ||
LPAD(CAST((CAST(sec AS BIGINT)%3600)/60 AS TEXT),2,'0') || ':' ||
LPAD(CAST(CAST(sec AS BIGINT)%60 AS TEXT),2,'0')
```
Emit `state_label, total_duration_seconds, total_duration_minutes, formatted_duration, percentage` and let the panel pick fields.

### Downtime with flicker protection
Raw PLC status bits chatter. Bucket, group consecutive equal states with a `SUM(is_new_state) OVER (ORDER BY time)` island, then **drop islands shorter than 2 buckets** before summing:
```sql
base            -- time_bucket('45s', systime), MAX(value) AS state
ordered         -- LAG(state) OVER (ORDER BY time) AS prev_state
state_changes   -- CASE WHEN state IS DISTINCT FROM prev_state THEN 1 ELSE 0 END AS is_new_state
state_groups    -- SUM(is_new_state) OVER (ORDER BY time) AS state_group
group_durations -- GROUP BY state_group, state; COUNT(*) AS bucket_count
stable_states   -- WHERE bucket_count >= 2; bucket_count * 45 AS duration_seconds
```
Then `SUM(duration_seconds) WHERE state = 0` for downtime and a percentage against the stable total.

### Cycle count from a sawtooth counter
A counter that resets marks a completed cycle — count the drops:
```sql
WITH bucketed AS (
  SELECT date_trunc('second', systime) AS time,
         MAX(COALESCE(value_double::numeric, value_integer::numeric, value_bool::int::numeric)) AS cycle_time
  FROM telemetry
  WHERE $__timeFilter(systime) AND uuid = (${cycle_time:raw}) AND is_delta IN ('t','f')
  GROUP BY 1
),
with_next AS (SELECT cycle_time, LEAD(cycle_time) OVER (ORDER BY time) AS next_val FROM bucketed)
SELECT COUNT(*) AS cycle_count FROM with_next WHERE next_val < cycle_time;
```

### Multi-signal cycle panel (timeseries / histogram)
One target per phase time (`refId` A…I), all named `LastCycle$InjectionUnit1$Injection time`-style, then transform:
`merge` → `filterByValue` (exclude rows where `Counter` or `CycleTime` is null) → `groupBy` (Time = groupby, everything else = `last`) → `organize` (hide the helper columns). The counter target exists only to gate the rows; it is always excluded at the end.

### Raw dataset per cycle (JSON in `value_string`)
Some machines publish the whole cycle as JSON. Explode it in SQL and let the table do the rest:
```sql
SELECT time_bucket('1s', systime) AS "time",
       (value_string::json ->> 'CycleTime')::int   AS CycleTime,
       (value_string::json ->> 'InjectionUnit1InjectionWork')::float AS InjectionUnit1InjectionWork,
       ...
FROM telemetry WHERE uuid = (${cycle_dataset_nr:raw})
```
Add an `organize` transformation that excludes `value_string` itself.

### Alert dashboard
Alerts arrive as `value_string` on the `ALERTMESSAGE_NR` datapoints (populated by a Node-RED flow — say so in the panel `description`). Panel datasource is `-- Mixed --`: query A counts from telemetry, query B fetches the human device name from ConfigRepo, and a `merge` + `organize` transformation joins them on `uuid` and hides `uuid`/`datatron`.
```sql
SELECT uuid, value_string, count(value_string) AS alert_count
FROM telemetry
WHERE uuid IN (${alert_uuids:raw})
  AND systime >= $__timeFrom()::timestamptz AND systime < $__timeTo()::timestamptz
GROUP BY uuid, value_string
ORDER BY alert_count DESC
```
Ship four views of the same query: vertical `barchart` (`xTickLabelRotation: -90`), donut `piechart` (legend as table, values), a sorted `table`, and a time-bucketed table using an `interval` variable `time_interval` (`15m,30m,1h,6h,12h,1d,7d,14d`) inside `time_bucket('$time_interval', systime)`. Set `unit: dateTimeAsUS` on the bucketed `systime` column.

### Per-piece event-anchored analysis (press centers)
Anchor on the serial number's change events, then `LEFT JOIN LATERAL` the last value of each signal at or just before the anchor:
```sql
WITH anchor AS (
    SELECT systime, COALESCE(value_integer, value_double::bigint) AS serial
    FROM telemetry
    WHERE systime >= '${__from:date:iso}' AND systime <= '${__to:date:iso}'
      AND uuid IN (${u_serial:raw}) AND is_delta = 't'
),
pieces AS (
    SELECT a.systime AS event_time, v_force.v AS force, v_done.v AS done
    FROM anchor a
    LEFT JOIN LATERAL (
        SELECT COALESCE(value_double, value_integer::numeric) AS v FROM telemetry
        WHERE systime >= '${__from:date:iso}' AND systime <= '${__to:date:iso}'
          AND uuid IN (${u_force:raw})
          AND systime >= a.systime - INTERVAL '1 hour'
          AND systime <= a.systime + INTERVAL '2 seconds'
        ORDER BY systime DESC LIMIT 1
    ) v_force ON TRUE
    LEFT JOIN LATERAL ( ... value_bool AS v ... uuid IN (${u_done:raw}) ... ) v_done ON TRUE
)
```
The `-1 hour / +2 seconds` window is the convention: look back far enough to catch a slow signal, forward only enough to catch same-instant writes.

KPI reductions off `pieces`:
```sql
-- OK rate
100.0 * COUNT(*) FILTER (WHERE iO)  / NULLIF(COUNT(*) FILTER (WHERE done), 0)
-- Force CV %
CASE WHEN AVG(force) > 0 THEN (100.0*STDDEV_SAMP(force)/AVG(force))::numeric(5,2) END
-- P95
PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY force)
```

### SPC chart (mean ±3σ)
Return the control limits as extra columns on every row; the ECharts script reads the last value of each:
```sql
, stats AS (SELECT AVG(force) AS mu, STDDEV_SAMP(force) AS sd FROM pieces WHERE done AND force IS NOT NULL)
SELECT p.event_time AS time, p.force AS value,
       s.mu AS target, s.mu + 3*s.sd AS ucl, s.mu - 3*s.sd AS lcl
FROM pieces p, stats s
WHERE p.done AND p.force IS NOT NULL
ORDER BY p.event_time;
```

## ECharts (`bilibala-echarts-panel`) conventions

Set `options.followTheme: true`, `backgroundColor: 'transparent'`, and return the option object from `options.getOption`.

**Field extraction — Grafana 8 exposes three different shapes; always use the guard:**
```js
function extractFieldValues(f) {
  if (!f) return [];
  if (typeof f.values?.toArray === 'function') return f.values.toArray();
  if (Array.isArray(f.values)) return f.values;
  if (Array.isArray(f.values?.buffer)) return f.values.buffer;
  return [];
}
const frame = data.series.find(s => s.refId === 'A');
```
Always return a `{ title: { text: 'No Data' }, … }` option when the frame or fields are missing — a thrown script blanks the panel with no message.

**Panel time range** (needed to pad empty buckets rather than trimming to the data):
```js
const from = new Date(data?.request?.range?.from).getTime();
const to   = new Date(data?.request?.range?.to).getTime();
```
Fall back to min/max of the data, then to `now-6h`.

**Hourly bucket + trim**: build every hour between `from` and `to`, zero-fill, then walk in from both ends dropping empty hours so the chart doesn't start with a wall of zeros. Thin the labels rather than the buckets:
```js
let labelEvery = 1;
if (n > 48) labelEvery = 3; if (n > 96) labelEvery = 6;
if (n > 168) labelEvery = 12; if (n > 336) labelEvery = 24;
axisLabel: { rotate: n > 48 ? 35 : 0, hideOverlap: true,
             formatter: (v, i) => (i % labelEvery === 0 ? v : '') }
```

**Timezone**: telemetry is UTC and buckets stay UTC — apply the offset only to display labels. Derive it dynamically so DST is handled:
```js
function getUtcOffsetHours(tz) {
  const now = new Date();
  const utc = new Date(now.toLocaleString('en-US', { timeZone: 'UTC' }));
  const loc = new Date(now.toLocaleString('en-US', { timeZone: tz }));
  return Math.round((loc - utc) / 3600000);
}
```
Plant timezones in use: `Europe/Belgrade` (Subotica), `Europe/Budapest`. Shift boundaries are hours `[6, 14, 22]` local.

**Hourly output (stacked OK/NOK by part number + total line)**: aggregate OK (`refId A`) and NOK (`refId B`) into `{hourKey: {part: {OK_Count, NOK_Count, Total}}}`, keyed by an hour map built from a part-number query (`refId D`). One `bar` series per part per verdict, `stack: part`, `#4CAF50` for OK / `#F44336` for NOK, plus a white `line` series on `yAxisIndex: 1` with `label.show: true` for the hourly total. Set both y-axes to the same `max` so the line sits over the bars.

**Cycle-time heatmap**: y-axis = non-uniform cycle-time bins (`[0,20],[20,40],[40,60],[60,120],[120,240],[240,600],[600,9999]`), x-axis = hours, viridis ramp `['#440154','#482878','#3E4989','#31688E','#26828E','#1F9E89','#35B779','#6CCE59','#B4DE2C','#FDE725']`, `#1a1a1a` for zero, color scaled against the matrix max.

**SPC scatter**: `xAxis.type: 'time'`, scatter with per-point `itemStyle` red (`#d62728`) when outside UCL/LCL else blue (`#3a6ea5`), and `markLine` (`silent: true`, `symbol: 'none'`) for UCL/LCL dashed red and Target solid green.

**KPI tile (shift sum)**: for a per-shift counter, sum the samples between the computed shift start/end and return only a `title` with `fontSize: 35` and empty `series` — a text-only ECharts panel. Three copies (`morning`/`afternoon`/`night`) differing by one `const selectedShift` line give a shift comparison row.

**Machine card (L1)**: draw the whole card with `graphic` — a rounded `rect` whose `stroke` is the status color, a colored header rect (`r: [15,15,0,0]`), machine name + workplace ID text, then label/value rows via a `makeRow(idx, label, value)` helper, and a footer "↗ Open Level 2" group whose `rect` and `text` both carry `onclick: () => window.open(CUSTOM_LINK, '_blank')`. Keep the machine-specific bits in a `CONFIG` block at the top (`MACHINE_NAME`, `WORKPLACE_ID`, `CUSTOM_LINK`, `TIMEZONE`, `SHIFT_HOURS`) so cloning a card for the next machine is a three-line edit.

## Andon board construction

- No templating at all; UUIDs inlined per machine. `refresh: "30s"`, `time: now-24h`.
- Row 0 is a strip of 1-height `text` panels acting as **column headers** (`content: "  "`, the title carries the label): Workplace | Machine | Feeder Status | Bender Status | Shift 1 | Shift 2 | Shift 3 | Last Part Produced | Downtime.
- Each machine is one 2-height band of panels on the same x grid: `text` (workplace no. and equipment ID as `<h2 style="text-align:center"><strong>…</strong></h2>`), two status `stat`s, three ECharts shift tiles, a last-part `stat`, a downtime `stat`.
- Status stats: `colorMode: background`, `orientation: horizontal`, `textMode: value`, threshold color `transparent`, `noValue: "-"`, and the state mapping supplying the color. For a noisy analog-ish status use `AVG(...)` over a 90s bucket with **range** mappings (`0–0.001 → Stopped`, `0.001–10 → Running`) instead of value mappings.
- Repeat the band by copying and swapping the UUIDs; keep panel ids unique.

## Layout, units, and naming

- 24-column grid. Header stats `h:2–3`; state-timeline `h:4–5, w:24`; process timeseries `h:6, w:24`; analysis charts `h:7–16`.
- Group L3 process values into **collapsed rows** (`"collapsed": true`) per subsystem: Injection Unit 1/2, Moveable Plate, Fixed Plate, Hydraulic Pumps, Metal Monitoring, Oil Level & Filter, Raw Datasets.
- Panel titles are always human-readable and carry the unit: `Injection Unit 1 - Injection Pressure [bar]`. Never leave a raw signal name (`inject_unit_1_plast_speed_act`) as a title, and when cloning a row for a second unit, retitle every copy — `Injection Unit 2 - …`, not a leftover `Injection Unit 1`.
- Units: `s`, `ms`, `celsius`, `pressurebar`, `forceNm`, `lengthmm`, `percent`, `short`, `string`, `none`, `dateTimeAsUS`.
- Tags follow `<plant letter>`, `<material/process group>`, `<Process>-<DashboardType>`:
  `["K","Rubber","2K_Injection_Molding-Production_Overview"]`, `["K","Metal","Forming","Metal_Forming-Andon_Board"]`, `["Processes","Processes_All-Alert_Dashboard"]`, `["Assembly","Component Assembly"]`.
- Dashboard title format: `Building 2 | Crippa Bending - Andon Board`, `Desma 2K Injection Molding - Level 2 - Production Overview`.
- `timezone: "browser"`, `style: "dark"`, `pluginVersion: "8.5.22"`, `id: null` and a stable `uid` on export.
- Ship an absolute default time range (`now-24h`) — an exported dashboard pinned to fixed ISO timestamps is a bug from a debugging session.

## Datapoint enablement

Some UUIDs need collection turned on before the dashboard has data. Always output the disabled ones:
```
UUID                                    | Label                                  | Why needed
----------------------------------------|----------------------------------------|------------------
9270c46c-d53f-4de3-bed7-4e77a646dd3c    | DB 35.D_56 TEMP.VORLAUF PRIM.-KREISL. | Vorlauf stat + trend
```

## Equipment context

### KKA (Kreislauf-Kühlanlage)
`DB 35.D_56` Vorlauf Primärkreis (x0.1°C) · `DB 35.D_59` Rücklauf CC (x0.1°C) · `DB 35.D_47` Druck Primärkreislauf (x0.1 bar) · `DB 35.D_42` Wassermenge CC (x0.1 m³/h) · `DB 35.D_154` Kühlleistung · `ED 30` korrigierter Volumenstrom l/h · `Waermetauscherregler.Input/Setpoint/Output` PID · `DB 1.Pumpe_N.Strom/Drehzahl/Leistung` · `DB 62.Pumpe_N_Betriebsstunden` · `FB 80…CC/Bypass.AnalogSollwert` (0–100%) · `DB 71.Eingang.*` power meter.
Thresholds: temps blue <18, green 18–28, yellow 28–35, red >35 °C; primary pressure green <4.5, yellow 4.5–6, red >6 bar.
**Scaling:** many PLC integers are `x0.1` — divide by `10.0` and check `config_comment` before trusting a raw value.

### Automatic Press Centers (501–504)
`Trägerinfo_Station_Letzter.ui_Seriennummer` (per-piece anchor) · `r_Pressvorgang_Rohr/Stutzen_MaxKraft` / `MaxWeg` · `Pressvorgang_*_iO / niO / durchgeführt / nicht_durchgeführt` · `NOK_Reason` / `NOK_Reason_Text` · checkpoints Halteblech, Stutzen presence, Kupferring, Kameraauswertung · `Werkstück_Ausschleusen`.
Dashboard: one row per press with 8 stats (pieces, OK rate, NOK count, skipped %, mean/P95 force, force CV %, mean position), then shared quality rows (verdict donut, NOK Pareto stacked by press, verdict trend), SPC rows per press, a "last 500 pieces" table, and a checkpoint row.

### 2K Injection Molding (Desma)
Signals: `machine_state`, `order_number`, `partnumber`, `material_number`, `mould_number`, `cycle_time`, `part_counter`, `injection_counter`, `production_quantity`, `real_cure_time`, per-unit `plast_work/speed/time_act` and `inject_position/work/speed/pressure/time_act`, heating platens (moveable/fixed 1–3), `hydraulic_pump_N_pressure_act`, `custom_metal_monitor_count_act`, `maint_oil_level`, `maint_oil_filter`, `cycle_dataset_nr` (JSON).
L1 card view covers Desma 351–361, one ECharts card each.

### Bending / forming cells (Crippa)
Standardized labels: `CYCLETIME_NR`, `PARTPRODUCEDTRIGGER_NR`, plus German PLC paths `PLC_1.Blocks.Meldebaustein-FB_DB.Lampe grün` (machine status), `PLC_1.Blocks.Aktions-FB_DB.Schutztür` (door). Cycle-time analysis = min/mean/max stats, scatter, histogram (`bucketSize: 5`, `value_double < 300` to drop outliers), heatmap, hourly output.

### Assembly cells (BMW KL33)
Flat single-machine dashboard, hard-coded UUIDs, `$__interval` buckets, `Power On`/`Start Automatik` booleans, shift OK/NOK counters, per-station text headers (ST100/ST150/ST200/ST300/ST400) over station stats.

## Stage 4 — Stakeholder pitch deck

A dashboard nobody uses has no value. The pitch deck is what turns a finished dashboard into adoption: it tells production, maintenance, quality and management what the thing is *for them*, and what decision it lets them make that they make blind today.

**Inputs**: the dashboard JSON (that is enough — panel titles, units, tags and queries say what it measures), the machine/area name, optionally screenshots, optionally the presenter's name, optionally the plant's cost rates (see *The value model*).

**Output**: `.pptx` on the neuwerk corporate template. **Ask the user to attach `neuwerk_presentation_template with samples.pptx`** — it cannot be bundled with this skill. If it is not available, either ask for it, or fall back to a clean HTML one-pager (below) rather than faking the branding.

### Deck structure — 6 slides, 4 of them content

| # | Purpose | Layout (index / name) | Fill |
|---|---|---|---|
| 1 | Title + value proposition | `0` starter slide 01 | title idx0 = dashboard name; idx13 = the one-sentence value proposition |
| 2 | Why it exists | `8` headline with 3 text box | idx0 title, idx11 lead; boxes (head→body) `15→12`, `16→13`, `17→14` = **What it shows / What it answers / What it replaces** |
| 3 | Who gets value | `13` hl text and 4 boxes | idx0 title, idx11 lead; boxes `15→12`, `17→16`, `19→18`, `21→20` = **Production / Maintenance / Quality / Engineering-Management** |
| 4 | The dashboard | `19` hl pic (1 image) · `21` (2) · `22` (3) | picture placeholder idx16 (and 17, 18); image fitted, or a dashed drop-in frame when no screenshot exists yet |
| 5 | What it is worth | `2` headline with text | idx0 title, idx11 lead, then a 4-column value table (see below) |
| 6 | Close | `31` closing slide 01 | idx0 = a short closing headline, idx13 = the rollout line |

Use layout `8` (3 boxes) instead of `13` when only three roles are genuinely served — do not pad a fourth. Drop slide 5 only if the user explicitly does not want a business case.

**Footer slots** (fill on every slide; the tuple is *deck title, presenter, brand, year*):

```python
FOOTER = {0:(10,11,14,12), 2:(10,12,14,13), 8:(10,18,20,19), 13:(10,22,14,13),
          19:(13,14,17,15), 21:(13,14,18,15), 22:(13,14,19,15), 31:(10,11,14,12)}
BRAND = "The neuwerk way"
```

Other useful layouts: `4` section cover or key message, `24` hl text and single pic 02 (lead + wide chart box), `29` agenda, `30` timeline.

## The value model — how to put a number on a dashboard

A dashboard does not save money. It shortens the distance between a loss happening and someone acting on it. That distance is measurable, so the savings are calculable — as **a model with visible inputs**, never as an asserted figure.

Every number on the value slide belongs to exactly one of three classes, and the slide must make clear which:

1. **Measured** — comes out of the dashboard's own queries over a stated period. Cite the panel and the window ( "mean 41.2 s over 14 days, Cycle Time panel" ).
2. **Rate** — supplied by the plant: machine hour rate, contribution margin, scrap cost. Never guess one. If the user does not have it, print the placeholder `<EUR/h>` and hand them a form, not a fiction.
3. **Assumption** — the scenario: how much of the gap gets closed. Always shown, always a range, never buried.

### The four levers

**1. Cycle-time recovery (throughput)**
```
gap        = CT_mean - CT_ref            # CT_ref = design takt, or p10 of observed = best sustained
recovered  = N_parts_year x gap x f / 3600      # f = capture fraction, 0.30 base (0.15 / 0.50 range)
value      = recovered_h x machine_hour_rate                    # cost avoidance
           OR (recovered_s / CT_ref) x contribution_margin      # if the line is capacity-constrained
```
**Ask which one applies.** "Is this line sold out?" changes the answer by 5–10x, and getting it wrong is the difference between a credible case and a laughed-at one. Sold out → recovered time becomes sellable parts. Not sold out → it is only avoided machine cost, and possibly nothing at all.

**2. Downtime reaction (Andon / alerts)**
```
minutes_saved = stops_per_year x R      # R = minutes cut from DETECTION + REACTION, not repair
value         = minutes_saved / 60 x rate
```
`stops_per_year` and mean stop duration come straight from the flicker-protected downtime query. Be explicit that an Andon board does not repair anything: it only removes the interval where a machine sat stopped and nobody knew. Claim that slice and nothing more.

**Pareto sharpening** is the strongest version, because the share is real: the alert dashboard already reports that reason #1 is *p* % of all alerts. Then the only assumption is the elimination fraction:
```
value = total_downtime_h x p x e x rate      # e = fraction of that one cause eliminated
```

**3. Quality containment (SPC / per-piece)**
The honest claim is the **containment window** — how many parts get made between drift starting and someone noticing:
```
pieces_caught_earlier = L_today - L_spc        # L_today: found at the gauge or end of shift
value                 = events_per_year x pieces_caught_earlier x scrap_cost_per_part
```
Plus the steady-state term when a target NOK rate is agreed:
```
value = N_parts_year x (q_now - q_target) x scrap_cost_per_part
```
`q_now`, force CV % and out-of-control counts are measured; `q_target` and `events_per_year` are assumptions.

**4. Engineering and setup time (L3 process values)**
```
value = incidents_year x hours_saved_each x engineer_rate
      + setups_year x minutes_saved x machine_hour_rate / 60
```
Setup duration is measured — it is the `Setup` state in the state-duration query. Hours saved per troubleshooting incident is an assumption (1–2 h of "walk to the machine, connect a laptop, try to reproduce it" is the usual shape).

### Payback

```
payback_weeks = (build_hours x internal_rate + edge/licence cost) / (annual_value / 52)
```
Build effort is knowable: tag enablement + dashboard configuration. This is the number management actually asks for, and it is usually the most flattering one — which is exactly why it must sit next to its inputs.

### Rates to request from the plant

- Machine (or cell) hour rate, EUR/h
- Contribution margin per part, EUR — only if the line is capacity-constrained
- Scrap cost per part at this station, EUR (material + value added so far)
- Annual volume and annual production hours
- Engineer / technician rate, EUR/h
- **Is the line sold out?** (the single answer that most changes the result)

Ask for these once, up front. If they are unavailable, build the slide with placeholders — a filled-in form is a deliverable; an invented rate is a liability.

### Honesty rules for the value slide

- Title it **"What it is worth"** or **"Value scenario"** — never "Savings" or "ROI", which read as promises.
- Carry the disclaimer verbatim: *"Scenario arithmetic from <period> data and the assumptions shown — not a forecast."*
- Show a **range** (low / base / high on the capture fraction), never a single point.
- Show the formula next to the result so any engineer in the room can challenge an input instead of the conclusion.
- Never sum the four levers into one headline number without saying they overlap — recovered cycle time and reduced downtime partly count the same hours.
- Never claim savings the dashboard cannot cause. It makes a loss visible; the improvement still needs someone to act.

### Value table mechanics

A 4-column `add_table` on layout `2`, columns *Lever | Measured by the dashboard | Scenario assumption | Annual value*, widths `1.9 / 4.1 / 3.1 / 3.0` inches at left `0.55`, top `2.35`. Header row filled navy `#1B1E51` with white 11 pt bold; body cells white, 10 pt, first column bold navy, `vertical_anchor = MSO_ANCHOR.MIDDLE`, `word_wrap = True`, row height `0.95`. **Render any run containing `<` in periwinkle `#8793CA`** so unfilled placeholders read as a form, not as data. Add a 9 pt periwinkle textbox underneath listing the rates still needed plus the payback formula and the disclaimer.

### Content rules

The deck is a pitch, not a manual. Every claim traces to a panel that exists in the JSON.

- **Value proposition** ≤ 95 characters, concrete, no marketing. "Every bending cycle, measured. See where the seconds go — by hour, by shift, by part — and get them back." Not "leveraging Industry 4.0 to unlock synergies."
- **Slide titles** ≤ 28 characters on layouts 8/13/19 (the title box is one line), ≤ 60 on layouts 0/31.
- **Box headers** 1–3 words. **Box bodies** 45–60 words on layout 8, 30–40 on layout 13 (four narrower boxes); set 10 pt on layout 13 bodies.
- **Per-role boxes follow one shape**: what that role looks at → what they decide → what changes. "A slowly rising mean cycle time is a machine telling you something is wearing. Catches it as a trend and plans the intervention instead of reacting to a breakdown."
- **Outside the value slide, no numbers at all** unless measured or user-supplied. The business case lives in one place, with its assumptions attached.
- Name the roles as the plant names them, and use the plant's own words for the equipment (Rohr/Stutzen, Schutztür, takt).

Derive the content from the JSON: panel titles and units → *what it shows*; the state mappings, SPC limits, Pareto and histogram panels → *what it answers*; alert/andon families → maintenance and shift-lead value plus lever 2; SPC and cycle-time families → quality and engineering value plus levers 1 and 3.

### Build mechanics (python-pptx) — the parts that bite

```python
prs = Presentation(TEMPLATE)          # keeps all 33 layouts, master, logo, brand graphics
wipe_slides(prs)                      # template ships 7 sample slides - delete them first
```

- **Delete the sample slides** via `prs.slides._sldIdLst`, dropping each `rId` with `prs.part.drop_rel(rId)` first.
- **Fit every title.** The 50 pt content titles wrap onto a second line past ~28 characters and spill over the lead paragraph. Step the size down until it fits: chars-per-line ≈ `0.95 * box_width_in / (0.008 * pt)`, line height `1.22 * pt / 72`.
- **Never `insert_picture` a dashboard screenshot into a picture placeholder** — it center-crops to the placeholder's aspect and beheads a 16:9 capture. Compute the fit yourself, remove the placeholder, and `add_picture` centered:
  ```python
  scale = min(box_w / iw, box_h / ih); w, h = int(iw*scale), int(ih*scale)
  left = box_l + (box_w - w)//2; top = box_t + (box_h - h)//2
  pic_ph._element.getparent().remove(pic_ph._element)
  slide.shapes.add_picture(path, left, top, width=w, height=h)
  ```
- **No screenshot yet** → drop a rounded dashed frame (`MSO_SHAPE.ROUNDED_RECTANGLE`, no fill, `#8793CA` 1.25 pt dashed, centered 14 pt label "Insert dashboard screenshot here") in the placeholder's box, so the user pastes the capture in later without touching the layout.
- **Moving a placeholder: set all four of `left, top, width, height`.** A partial `xfrm` renders as nothing — the shape silently disappears.
- **Remove placeholders you left empty** (`drop_empty`, keeping the footer set) so PowerPoint shows no "Click to add text" ghosts.
- **Verify visually before delivering**: `soffice --headless --convert-to pdf`, then `pdftoppm -png -r 70`, and actually look at every slide. Overflowing titles, vanished shapes and tables running off the page are invisible in the XML.

### HTML fallback

No template available, or the user wants a shareable link instead of a file: build the same six sections as one self-contained HTML page — navy `#1B1E51` ground, periwinkle `#8793CA` accents, teal `#1EB68A` for the positive callout, white cards for the role boxes, a real `<table>` for the value model, `<img>` or a dashed drop-in frame for the screenshot. Same content rules, same three-class discipline on every number. Persist it as an artifact so the user gets a link they can send.

## Checklist

- [ ] `__inputs` declares exactly the datasources referenced (TelemetryPLC, ConfigRepo, and Datadash if AREA is used)
- [ ] Variable chain resolves: area → datatron → plc → hidden (`hide: 2`) UUID resolvers; `plc` uses `refresh: 2`
- [ ] SQL uses `${var:raw}` (never bare UUIDs) on templated dashboards; inline UUIDs only on Andon/card views
- [ ] `is_delta` filter matches intent (`'t'` for counters/triggers/anchors, `'t','f'` for states and analog trends)
- [ ] `COALESCE(value_double, value_integer, value_bool::integer)` everywhere numeric
- [ ] One time-filter dialect per dashboard; `LATERAL` subqueries use `'${__from:date:iso}'`
- [ ] Machine-state mapping and colors match the estate standard (0/1/2/5)
- [ ] Shift logic uses 06/14/22 boundaries and a 06:00 production-day start
- [ ] Duration queries use `LEAD` + `COALESCE` for the open last segment; downtime applies flicker protection
- [ ] ECharts scripts guard field extraction, handle a missing frame, and read the range from `data.request.range`
- [ ] Timezone offset derived dynamically (DST-safe), applied to labels only
- [ ] Scaled values divided correctly (`x0.1` → `/10.0`)
- [ ] Every panel titled with a human name and unit — no raw signal names, no stale titles on cloned rows; descriptions note the datapoint/DB block and any Node-RED dependency
- [ ] Units, thresholds, and `noValue` set; stat panels use `colorMode: background` where status color carries meaning
- [ ] Tags, title, `uid`, `timezone: browser`, and a relative default time range
- [ ] L1 cards link to the correct L2 URL with every `var-*` parameter URL-encoded
- [ ] Disabled-but-needed UUIDs listed for enablement

### Pitch deck

- [ ] Sample slides wiped; every slide sits on the mapped neuwerk layout
- [ ] Titles fitted (no wrap into the lead paragraph); footer slots filled on all slides
- [ ] Screenshots fitted without cropping, or a dashed drop-in frame left in their place
- [ ] Role boxes follow *looks at → decides → changes*, in the plant's own vocabulary
- [ ] Every number is labelled measured / rate / assumption; measured ones cite panel and period
- [ ] Capacity-constrained question asked before any throughput value is claimed
- [ ] Value shown as a range with the formula visible; disclaimer line present
- [ ] No rate invented — unfilled inputs shown as periwinkle `<placeholders>`
- [ ] Rendered to PNG and visually checked slide by slide before sending