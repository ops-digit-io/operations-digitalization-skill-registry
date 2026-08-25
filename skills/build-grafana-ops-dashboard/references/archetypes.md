# Data model archetypes — how to choose

Operations dashboards backed by SQL come from one of two fundamentally different schemas. Picking the wrong patterns wastes time and produces broken queries. Identify the archetype before writing any SQL.

---

## Archetype A — Relational (custom schema)

### What it looks like

Multiple tables, each modeling a specific entity. Foreign keys link facts to dimensions.

```
downtime_incidents (id, start_time, end_time, machine_id, reason_id, ...)
machines           (id, name, type, ...)
downtime_reasons   (id, name, severity, parent_reason_id, ...)
```

Every domain has its own dedicated tables. Adding a new entity means a new table.

### Signs you're looking at this archetype

- Tables named for **entities**, not for **storage layers** (`incidents`, `orders`, `defects`, `users` — not `telemetry`, `metrics`, `events`)
- Each row has typed, named columns: `start_time`, `end_time`, `quantity`, `unit_price`
- **Foreign keys** to dimension tables: `machine_id`, `reason_id`, `account_id`
- Soft-delete and audit columns: `is_archived`, `is_active`, `created_at`, `updated_at`, `created_by_id`
- Often ORM-generated — Rails, Django, SQLAlchemy patterns visible
- Multi-tenancy via `account_id` or `tenant_id`
- Hierarchies via self-referencing FKs: `parent_reason_id`, `parent_id`

### Where it comes from

- SaaS products (Plex, Tulip, MachineMetrics, custom internal tools)
- ERP/MES systems (SAP, Infor, dedicated MES exports)
- Custom-built operations apps
- Anywhere a software team designed the schema for a specific business problem

### Strengths

- Schema enforces meaning — column names tell you what the data is
- Joins are natural and well-typed
- Easy to add domain-specific business logic to queries
- Constraints (NOT NULL, FOREIGN KEY, CHECK) catch bad data at insert time

### Weaknesses

- Inflexible — adding a new sensor or signal requires a schema migration
- Often opinionated about granularity (one row per incident, not per second)
- Heterogeneous — each table is its own little world

### Use these patterns

`references/relational_patterns.sql` — interval-shaped facts (start_time/end_time), Pareto by reason×machine, MTTR/MTBF, drill-down detail tables.

---

## Archetype B — Timeseries (UUID-keyed long-format)

### What it looks like

A single wide table — every measurement from every sensor is one row, identified by a UUID indicating *what* is being measured.

```sql
CREATE TABLE telemetry (
  systime         timestamptz NOT NULL,
  uuid            uuid        NOT NULL,
  value_double    double precision,
  value_integer   bigint,
  value_bool      boolean,
  value_string    text,
  is_delta        char(1)             -- 't' = event/delta, 'f' = state
);
```

Every signal — temperature, speed, part-counter, machine-state, partnumber-name — lives in this same table. The `uuid` column is the only thing that distinguishes one signal from another.

### Signs you're looking at this archetype

- **One fact table** named `telemetry`, `metrics`, `signals`, `points`, `tags`, `samples`, or similar
- A UUID / signal_id / tag_id column — this is the hottest filter
- **Multiple `value_*` columns** for different types (double, integer, bool, string)
- Read pattern always involves: `COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER))` (use `CAST(... AS INTEGER)` not `::integer` — portable across PG and DuckDB)
- An `is_delta` or `is_event` flag distinguishing state values from event/delta rows
- Often partitioned by time (TimescaleDB hypertable) or stored as Parquet (DuckDB / Spark / data lake)
- Sometimes a separate **metadata table** maps UUID → human-readable name + units + machine

### Where it comes from

- IIoT platforms: UMH (Unified Manufacturing Hub), Benthos-UMH bridges
- OPC-UA / MQTT / Sparkplug B telemetry pipelines
- Time-series databases (TimescaleDB, InfluxDB, QuestDB) used for industrial data
- The `ts-shape` Python library's expected schema
- PI / Ignition / Wonderware historians (sometimes flattened to this shape downstream)

### Strengths

- Schema-flexible — adding a new sensor means adding a UUID, not migrating tables
- Uniform query patterns work across every signal type
- Works at very high cardinality (thousands of UUIDs, billions of rows)
- Natural fit for streaming ingestion (one measurement → one row)

### Weaknesses

- UUIDs are opaque without a metadata lookup
- Joining two signals requires aligning timestamps (rarely identical)
- Many small queries (one per signal) instead of one big join
- Easy to forget the `is_delta` filter and double-count

### The canonical query patterns

> All snippets follow the two hard rules from `SKILL.md`: time access via Grafana macros (`$__timeFilter`, `$__timeGroup`), and PostgreSQL+DuckDB portability (no `time_bucket`, no `::int` on booleans).

**Read a single signal as a time series:**
```sql
SELECT
  systime AS "time",
  COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) AS "Signal Name"
FROM telemetry
WHERE
  $__timeFilter(systime)
  AND uuid = (${signal_var:raw})       -- :raw avoids quote escaping
  AND is_delta IN ('t', 'f')           -- 't','f' for state; 't' only for deltas
ORDER BY 1;
```

**Bucket and aggregate:**
```sql
SELECT
  $__timeGroupAlias(systime, $__interval) AS time,
  AVG(COALESCE(
    CAST(value_double  AS NUMERIC),
    CAST(value_integer AS NUMERIC),
    CAST(CAST(value_bool AS INTEGER) AS NUMERIC)
  )) AS "Avg Value"
FROM telemetry
WHERE $__timeFilter(systime)
  AND uuid = (${signal_var:raw})
  AND is_delta = 't'
GROUP BY 1
ORDER BY 1;
```

**Join two signals on time bucket:**
```sql
WITH a AS (
  SELECT $__timeGroup(systime, '1s') AS ts,
         COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) AS val
  FROM telemetry
  WHERE $__timeFilter(systime) AND uuid = (${signal_a:raw}) AND is_delta IN ('t','f')
),
b AS (
  SELECT $__timeGroup(systime, '1s') AS ts,
         COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) AS val
  FROM telemetry
  WHERE $__timeFilter(systime) AND uuid = (${signal_b:raw}) AND is_delta IN ('t','f')
)
SELECT a.ts AS time, a.val AS "Signal A", b.val AS "Signal B"
FROM a INNER JOIN b ON a.ts = b.ts
ORDER BY a.ts;
```

Use these patterns. `references/timeseries_patterns.sql` has more, including counter-reset handling, state-duration computation, and shift-clipping.

---

## Mixed environments

A user can have **both archetypes** simultaneously. Common pattern in manufacturing:

- `telemetry` (timeseries) — raw machine signals: PLC tags, sensor readings, counters
- `downtime_incidents` (relational) — human-classified events with reason codes
- `production_orders` (relational) — planned production with ERP integration

Build dashboards that use **both** when needed:

- A KPI panel might pull total downtime from `downtime_incidents` (clean classified data)
- A trend panel might pull machine speed from `telemetry` (raw signal)
- The two link via `machine_id` (relational FK ↔ a UUID metadata mapping)

When mixing, keep panels visually consistent — same time range, same variable names, same color palette — even if the underlying SQL is very different.

---

## How to ask if you can't tell

If the schema isn't clear from what the user provides, ask:

> "Quick check: is your data in **dedicated tables** like `incidents`, `orders`, `defects` — each with their own typed columns — or is it in **one wide telemetry table** where every measurement is a row keyed by a UUID or signal_id?"

Most users immediately know. If they say "both," ask which the dashboard should focus on.

---

## Edge cases

### Star schema / data warehouse

Looks relational on the surface but is denormalized for analytics. `fact_production` joined to `dim_machine`, `dim_time`, `dim_product`. Treat as relational archetype — same patterns work, dimensions are just narrower.

### Event-sourced / append-only

Tables like `machine_events` with rows like `(timestamp, machine_id, event_type, payload_jsonb)`. Closer to timeseries archetype than relational — you'll filter by `event_type` the way the timeseries archetype filters by UUID. The patterns in `timeseries_patterns.sql` adapt cleanly.

### Wide-format historian dump

Some PI / Wonderware exports come as wide CSVs: `(timestamp, sensor_1, sensor_2, sensor_3, ...)`. This is rarely seen in databases — usually flattened to the timeseries archetype during ingestion. If you do see it, treat each sensor column as its own time series.

### NoSQL / document store

If the user's data is in MongoDB, Elasticsearch, or similar — Grafana has separate datasource plugins for these and the SQL patterns in this skill don't apply. Politely note and pivot to the relevant Grafana datasource documentation.
