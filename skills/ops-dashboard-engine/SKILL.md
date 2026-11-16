---
name: ops-dashboard-engine
license: MIT
description: >-
  Build importable Grafana JSON dashboards over SQL for operations data (downtime, production, quality, energy, machine telemetry): schema interview, relational or UUID-telemetry archetype, manager, analyst or operations tier, portable PostgreSQL and DuckDB queries with Grafana time macros, variables, ECharts panels, audit checklist. Use when someone asks for a Grafana dashboard JSON to import, a downtime or telemetry dashboard, panel SQL that fails on DuckDB, or a dashboard rebuilt after a wrong schema assumption. Not for HTML or Chart.js dashboards (build-dashboard) or choosing the asset type and ritual (ops-analytics-asset).
allowed-tools: Read Grep Glob Write Edit
metadata:
  argument_hint: "[domain] [schema or signal list]"
  id: ops-dashboard-engine
  aliases: [build-grafana-ops-dashboard]   # former name (naming convention, 2026-11-11)
  tier: technical
  lane: lane-1
  new_state_lane: "Lane 1a (1a2), Lane 1b (1b4)"
  new_state_step: "Apply template (1a2); Apply template & go live (1b4)"
  department_names: ["ops-dashboard-engine"]
  scope: portable            # domain-generic; not derived from the OD knowledge graph
  origin: vendored           # the author's skill; OD sections and file links added 2026-11-11, rules and references unchanged
  owner_role: human:jakob.gabriel
  authority_level: author the dashboard; publishing to a shared Grafana is human-approved
  status: stable
  related: [ops-analytics-asset, mi-data-availability, deploy-handover]
  od_integration: skills/ops-dashboard-engine/OD-INTEGRATION.md
  okf:
    type: Agent Skill
    title: Grafana ops dashboard builder
    tags: [analytical-support-service, portable, technical, use-case-support-service]
---

# ops-dashboard-engine — Grafana JSON for Operations Data

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## When to use this skill vs `/build-dashboard`

| Output is… | Use |
|---|---|
| Self-contained `.html` file with embedded data, Chart.js | `/build-dashboard` |
| Importable Grafana `.json` with live SQL, ECharts panels, variables | **this skill** |

- If unspecified, ask once. The two are not interchangeable: Grafana queries a live database, HTML embeds a static snapshot.

## Inputs and output

- **In:** the domain and the question the dashboard answers; the schema (tables and columns) or the signal list (UUIDs and labels); the audience tier (manager, analyst, operations).
- For an OD dashboard also the ritual it is read in and the walked data path (see [`OD-INTEGRATION.md`](OD-INTEGRATION.md)).
- **Out:** one importable Grafana `.json` file with portable SQL, plus the Step 6 audit ([`references/outputs.md`](references/outputs.md)).

## Procedure

1. In OD, pass the two gates of [`OD-INTEGRATION.md`](OD-INTEGRATION.md) first; the end-to-end walk-through is [`usage_guide.md`](usage_guide.md).
2. Confirm the schema (Step 0), identify the archetype (Step 1), pick the tier (Step 2).
3. Apply the time-window patterns (Step 3) and wire the variables (Step 4).
4. Generate the JSON with the builder (Step 5); never hand-write panel JSON.
5. Run the audit checklist (Step 6) and fix every failed line; re-run until clean.
6. The two hard rules apply to every query; hand over with `deploy-handover`.

## Hard rules — apply to every SQL query in this skill

- These two rules are **non-negotiable** and override any pattern in the references; if a snippet contradicts them, the rule wins.

### Rule 1 — Always use Grafana query macros for time

- Hand-rolled `WHERE ts BETWEEN $__timeFrom() AND $__timeTo()` is a bug: it bypasses macro expansion, breaks across datasources and fails Rule 2.

| Need | Use this | Not this |
|---|---|---|
| Time-range WHERE | `$__timeFilter(ts_column)` | `ts BETWEEN $__timeFrom() AND $__timeTo()` |
| Time bucketing in SELECT | `$__timeGroup(ts_column, $__interval)` | `time_bucket('1h', ts)` or `date_trunc('hour', ts)` |
| Bucketing with `time` alias | `$__timeGroupAlias(ts_column, $__interval)` | manual `... AS time` |
| Bucket size | `$__interval` (auto from panel width) | hardcoded `'1 hour'` |
| Unix epoch bounds | `$__unixEpochFrom()` / `$__unixEpochTo()` | manual `EXTRACT(EPOCH FROM ...)` |

- Raw `$__timeFrom()` / `$__timeTo()` are legitimate only where a macro cannot express the operation:
   - window clipping with `LEAST` / `GREATEST` (Step 3, Pattern U3);
   - `generate_series` bounds for zero-fill scaffolds (Pattern U5);
   - interval-overlap WHERE such as `start_time < $__timeTo() AND end_time >= $__timeFrom()`.
- In every such case cast to `timestamptz` (`$__timeTo()::timestamptz`) and say in a SQL comment why the macro was not enough.

### Rule 2 — Every query must be PostgreSQL and DuckDB compatible

- The same SQL string goes to both engines through different Grafana datasources, so it must parse and run on both.

| Don't use | Use instead | Why |
|---|---|---|
| `time_bucket('1h', ts)` | `$__timeGroup(ts, $__interval)` | TimescaleDB-only; not in vanilla Postgres or DuckDB |
| `time_bucket_gapfill(...)` | `generate_series` + `LEFT JOIN` (Pattern U5) | TimescaleDB-only |
| `bool_col::int` | `CAST(bool_col AS INTEGER)` | DuckDB rejects the implicit cast via `::` in some contexts |
| `DISTINCT ON (col)` | `ROW_NUMBER() OVER (PARTITION BY col ORDER BY ...) = 1` | Postgres-only syntax |
| `array_agg(... ORDER BY ...)` with complex sort | `array_agg(...)` over a pre-sorted CTE | Ordering inside aggregates differs |
| `interval '1 day'` | `INTERVAL '1 day'` | DuckDB prefers uppercase keyword |
| `regexp_matches(...)` returning setof | `regexp_extract(...)` or split via CTE | Set-returning regex differs |
| Implicit `text` ↔ `uuid` comparison | `uuid_col::text = '...'` on both sides | DuckDB is stricter about UUID types |
| `EXTRACT(epoch FROM …)` | `EXTRACT(EPOCH FROM …)` | DuckDB requires the uppercase field name |

- Safe-in-both list and the cross-engine smell test (any TimescaleDB function fails on DuckDB): `references/portability_check.md`.
- If portability cannot be achieved (for example continuous aggregates), call it out in a SQL comment and mark the panel "Postgres-only" in its JSON description.
- Audit: before delivery run each query against both dialects in your head, then on the CLIs (Step 6); flag anything Timescale-specific.

## Step 0 — Confirm the schema before writing SQL

- Most dashboard rebuilds happen because the first version assumed a schema that was wrong; ask once, in one message, and do not guess column names.
- If the first message gives the schema in detail, skip to Step 1.
- Minimum to extract: domain and reader (tier), fact table and archetype, canonical timestamp column and type, interval or point shape and the meaning of NULL `end_time`.
- Also: tenant column, soft-delete flags (`is_archived`, `is_active`, `is_ignored`), the 3 to 5 KPIs with exact formulas, and the expected order of magnitude of each KPI.
- Full eight questions: `references/schema_interview.md` ("The minimum eight questions"); long engagements use its 29-question interview.
- Answers the user cannot give are where the dashboard fails later: flag them explicitly, do not paper over them with assumptions.

## Step 1 — Identify the data model archetype FIRST

- The two archetypes need different SQL patterns; decide before writing SQL (`references/archetypes.md`).

| | A — Relational (custom schema) | B — Timeseries (UUID-keyed long format) |
|---|---|---|
| Looks like | Entity tables (`downtime_incidents`, `production_orders`), typed columns `start_time`, `end_time`, `machine_id`, foreign keys, often ORM-generated | One table (`telemetry`, `signals`, `points`) with `systime`, `uuid`, `value_double` / `value_integer` / `value_bool` / `value_string`, `is_delta` |
| Patterns | `references/relational_patterns.sql` | `references/timeseries_patterns.sql` |
| Producers | Application databases | ts-shape, UMH, Benthos, OPC-UA bridges, MQTT historians |

- `is_delta` separates event values (delta, `t`) from state values (continuous, `f`).
- Mixed environments: build separate queries per archetype but share variables, time range and visual conventions.

## Step 2 — Pick the dashboard tier(s)

| Tier | Audience | Question | Filters | Panels |
|---|---|---|---|---|
| **Manager** | Plant managers, OPEX, executives | "Where do I send my attention this week?" | None except `$account` | 8–13, fixed window, traffic lights |
| **Analyst** | CI engineers, planners, analysts | "Why did this happen?" | Full filter set, time picker | 20–30+, drill-down, data quality |
| **Operations** | Shift leads, operators | "What's happening right now?" | None | Few, large fonts, live state |

- Always ask which tier(s) before building; do not default to all three, because each tier needs its own layout.
- Design rules and panel inventories: `references/dashboard_tiers.md`.

## Step 3 — Apply the universal time-window patterns

- They apply to both archetypes and honour the hard rules. Full SQL, with the reasons, is in `references/relational_patterns.sql` (section "Universal time-window patterns").

| Pattern | Use | Rule |
|---|---|---|
| U1 | Default time WHERE | `WHERE $__timeFilter(ts_column)` |
| U2 | Bucketed trend in SELECT | `$__timeGroupAlias(ts_column, $__interval) AS time`; pin a bucket only for shift-based aggregation |
| U3 | Duration of interval events | Clip with `LEAST` / `GREATEST` against the window; WHERE is a two-column overlap, not `$__timeFilter(start_time)` |
| U4 | Nullable `end_time` | `COALESCE(end_time, NOW())` for live panels; `WHERE end_time IS NOT NULL` for historical averages and MTTR |
| U5 | Zero-fill of empty periods | `generate_series` + `LEFT JOIN`, `$__timeFilter` on the join |

- Why U3 matters: without clipping, an 8-hour stoppage in a 1-hour view contributes the full 8 hours, the most overlooked bug in homegrown ops dashboards.
- Use U3 in every duration-summing query (relational archetype only; timeseries rows have no `end_time`).

```sql
SELECT SUM(EXTRACT(EPOCH FROM (
         LEAST(COALESCE(end_time, NOW()), $__timeTo()::timestamptz)
       - GREATEST(start_time, $__timeFrom()::timestamptz)))) / 60.0 AS clipped_minutes
FROM downtime_incidents
WHERE start_time < $__timeTo()::timestamptz
  AND COALESCE(end_time, NOW()) >= $__timeFrom()::timestamptz;   -- raw bounds: window clipping (Rule 1 exception)
```

## Step 4 — Wire variables consistently

- Every defined variable must be used in every relevant panel; defining one and not wiring it is a bug.
- Variable types, refresh order, the three filter patterns and the audit checklist: `references/variables.md`; the default sets per archetype are in the same file.
- Timeseries: one variable per signal, UUID from a metadata table, used as `uuid = (${signal_name:raw})` because without `:raw` the quotes double up and the panel silently returns zero rows.
- Three reusable filter patterns:
   - Optional sentinel: `'$severity' = 'all' OR CAST(severity AS TEXT) = '$severity'`.
   - Integer escape: `$auto_detected = -1 OR CAST(is_auto_detected AS INTEGER) = $auto_detected`.
   - NULL preservation: `(reason_id IN ($reason)) OR reason_id IS NULL`, so unclassified rows stay visible.
- Audit before delivery: search every panel's SQL for each defined variable.

## Step 5 — Generate JSON via the Python builder

- Do not hand-write Grafana panel JSON. Read `references/dashboard_builder.py` first: helpers for `stat`, `table_panel`, `echarts`, `timeseries`, `row`, `text`, threshold builders, variable factories and `build_dashboard`.
- Requires Python 3 and the standard library only; `python references/dashboard_builder.py validate out.json` checks a generated file (exit 0 clean, 1 findings).

```python
from dashboard_builder import (stat, row, traffic_light, var_query, build_dashboard)

panels = []; pid = 100
panels.append(row(pid, "KPIs", 0)); pid += 1
panels.append(stat(pid, "Total downtime", 0, 1, 4, 4, sql=sql_total, unit="m",
                   thresholds=traffic_light(yellow=20, red=50))); pid += 1
dashboard = build_dashboard(title="Downtime — Manager View (fictional)", panels=panels,
                            variables=[var_query("account", "ACCOUNT", account_sql, multi=False)],
                            refresh="5m", hide_timepicker=True)
```

- ECharts panels need `format: table` SQL with named columns and a `getOption` that reads columns by name.
- `references/echarts_templates.js` has 12 templates (Pareto, donut, heatmap, bars, histogram, gauge, state-timeline, hourly output, scatter, KPI grid, correlation, stacked area); pick by intent with its guide.
- Always include the two defensive splash screens (No data, Unexpected data shape).
- Timeseries with natural-language signal descriptions plus a UUID catalog: `references/signal_matching.md`.

## Step 6 — Audit checklist before delivering

- [ ] **JSON validates:** `python3 -c "import json; json.load(open('out.json'))"` and the builder's `validate`
- [ ] **Archetype is consistent** (no `COALESCE(end_time, NOW())` in timeseries queries)
- [ ] **Every defined variable is used in every relevant panel**
- [ ] **Every duration-summing query uses `LEAST/GREATEST` clipping** (relational only)
- [ ] **Time WHERE clauses use `$__timeFilter()`**; raw bounds only in justified exceptions, each with a comment
- [ ] **Bucketing uses `$__timeGroup()` / `$__timeGroupAlias()` and `$__interval`**; no `time_bucket()`, no hardcoded `date_trunc` bucketing
- [ ] **Every raw `$__timeTo()` / `$__timeFrom()` is cast `::timestamptz`**
- [ ] **No TimescaleDB-only functions** (`time_bucket*`, `first()`, `last()`, `locf()`)
- [ ] **No Postgres-only syntax** (`DISTINCT ON`, `bool_col::int`, lowercase `epoch`); booleans use `CAST(x AS INTEGER)`
- [ ] **UUID/text comparisons cast both sides** (`uuid_col::text = '...'`)
- [ ] **Every nullable-end-time case is explicit** (coalesce or exclude)
- [ ] **`OR <fk> IS NULL`** preserved wherever filtering on a nullable foreign key
- [ ] **Soft-delete flags** on every fact-table query
- [ ] **ECharts panels:** `format` is `table`, JS reads columns by name, splash screens included
- [ ] **Time series panels:** `format` is `time_series`, columns `time` / `metric` / `value`
- [ ] **Manager tier:** `timepicker.hidden = true`, refresh at least 5m, traffic-light thresholds set
- [ ] **`__requires`** declares schema, plugin and Grafana versions; datasource UID is the `${DS_NAME}` placeholder
- [ ] **Timeseries:** `${var:raw}` used for UUID variables
- [ ] **Indexes match WHERE shapes** and the **performance budget is met** (manager under 2s, analyst under 5s, operations under 1s): `references/performance.md`
- [ ] **Portability check passed** on at least 5 representative panels on both PG and DuckDB: `references/portability_check.md`
- [ ] **Panel titles follow** `[Tier] <Domain> — <Question>` for analyst dashboards (`references/dashboard_tiers.md`)
- [ ] **Annotations and alerts** considered for operations and analyst tiers; each added one has a named owner and a calibrated threshold (`references/annotations_and_alerts.md`)

## Human gate and AI-agent notes

- **Agent may:** confirm the schema, write the SQL and the dashboard JSON, run the audit and the portability check, and list what is not confirmed.
- **Humans decide:** publishing the dashboard to a shared Grafana instance (human-approved); the plant owner confirms adoption.

## Example

```text
Request (fictional): "Downtime dashboard for the plant manager, table downtime_incidents, one tenant column account_id."
Step 0 : archetype A (relational); end_time NULL = ongoing; KPI "total downtime" = clipped minutes in the window
Step 2 : manager tier only; 8-13 panels, fixed window, traffic lights
Step 3 : U3 clipping for the KPI; U5 zero-fill for the daily trend
Step 6 : portability check on 5 panels; delivered as one .json with ${DS_NAME}; publish = human approval
```

## Pitfalls

- A query that uses `time_bucket()`, hardcoded time bounds or `::int` on a boolean breaks the two hard rules, even when a reference snippet shows it; treat such a snippet as outdated.
- Building on a guessed schema: skipped Step 0 is the commonest cause of a rebuild.
- Defining a variable and not wiring it into the panels.
- Summing durations without clipping, so partially overlapping events inflate totals.
- Hardcoding a UUID in panel SQL; use a variable from a metadata table.
- In OD: a savings tile showing the tracked total as proven; `COALESCE(x, 0)` turning a missing value into a zero; a plant's Grafana pointed at the global platform.
- In OD: a cross-plant view built on a local instance (see [`OD-INTEGRATION.md`](OD-INTEGRATION.md)).

## Definition of done

- The JSON validates, every item of the Step 6 checklist is ticked or its exception stated, the portability check passed on at least five representative panels, and the dashboard is handed over with `deploy-handover`.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/background.md`](references/background.md) | You need context and rationale; never an instruction |
| [`OD-INTEGRATION.md`](OD-INTEGRATION.md) | Every OD dashboard: gates, local Grafana, handover |
| [`usage_guide.md`](usage_guide.md) | Invoking the skill end to end from a system prompt or Claude Code session |
| [`references/schema_interview.md`](references/schema_interview.md) | Step 0: minimum eight questions and the full interview |
| [`references/archetypes.md`](references/archetypes.md) | Step 1: recognising relational against timeseries, edge cases |
| [`references/relational_patterns.sql`](references/relational_patterns.sql) | Archetype relational, and Step 3 universal patterns |
| [`references/timeseries_patterns.sql`](references/timeseries_patterns.sql) | Archetype timeseries: counters, state durations, shift clipping |
| [`references/dashboard_tiers.md`](references/dashboard_tiers.md) | Step 2: tier design rules and naming |
| [`references/variables.md`](references/variables.md) | Step 4: variable types, refresh order, filter patterns, default sets |
| [`references/dashboard_builder.py`](references/dashboard_builder.py) | Step 5: panel helpers and the `validate` command |
| [`references/echarts_templates.js`](references/echarts_templates.js) | Step 5: an ECharts panel is needed |
| [`references/annotations_and_alerts.md`](references/annotations_and_alerts.md) | Step 5: operations or analyst tier with annotations or alerts |
| [`references/signal_matching.md`](references/signal_matching.md) | Timeseries, and the user describes signals in words instead of UUIDs |
| [`references/performance.md`](references/performance.md) | Step 6 audit, or the dashboard is slow |
| [`references/portability_check.md`](references/portability_check.md) | Step 6, before delivery: check queries on PG and DuckDB; safe-in-both list |
| [`references/troubleshooting.md`](references/troubleshooting.md) | Debugging an error, including first-time DuckDB setup |
| [`references/examples/`](references/examples/) | You want a complete model to imitate: [`README.md`](references/examples/README.md) lists four manager and analyst dashboards (`.py` and `.json`) |
| [`references/outputs.md`](references/outputs.md) | Before handing over: what must be delivered, to whom |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
| [`references/examples/relational_analyst.json`](references/examples/relational_analyst.json) | A worked input or output to copy the shape from |
| [`references/examples/relational_analyst.py`](references/examples/relational_analyst.py) | A worked input or output to copy the shape from |
| [`references/examples/relational_manager.json`](references/examples/relational_manager.json) | A worked input or output to copy the shape from |
| [`references/examples/relational_manager.py`](references/examples/relational_manager.py) | A worked input or output to copy the shape from |
| [`references/examples/timeseries_analyst.json`](references/examples/timeseries_analyst.json) | A worked input or output to copy the shape from |
| [`references/examples/timeseries_analyst.py`](references/examples/timeseries_analyst.py) | A worked input or output to copy the shape from |
| [`references/examples/timeseries_manager.json`](references/examples/timeseries_manager.json) | A worked input or output to copy the shape from |
| [`references/examples/timeseries_manager.py`](references/examples/timeseries_manager.py) | A worked input or output to copy the shape from |
