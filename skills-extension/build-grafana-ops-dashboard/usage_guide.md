---
type: Skill Guide
title: Usage guide
description: How an assistant running with the Grafana skill installed should drive it end to end, from schema interview to delivered JSON.
resource: SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [grafana, dashboards]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Usage Guide — How to use the `build-grafana-ops-dashboard` skill

This document is for the **assistant** running with the skill installed (Claude.ai with the skill in `/mnt/skills/user/`, Claude Code with the skill in the project, or any agent with the skill files accessible). It encodes the end-to-end workflow so a single user prompt becomes a working dashboard JSON without re-deriving the patterns from scratch each time.

If you are a human reading this: it doubles as the system-prompt template for orchestrating the skill in your own setups. Copy the sections marked **SYSTEM PROMPT** into your assistant configuration.

---

## Quick mental model

You are not generating a dashboard from your own knowledge. You are:

1. **Identifying** which archetype the user's data follows (relational or timeseries)
2. **Reading** the matching reference files in this skill
3. **Selecting** chart types from the 12 ECharts templates and the panel helpers
4. **Composing** SQL + panel JSON via the Python builder
5. **Auditing** the result against the checklist before delivering

The reference files are authoritative. When you're unsure about an SQL pattern, a panel field, or a variable wiring rule, the answer is in `references/` — not in your training data. Re-read instead of guessing.

---

## SYSTEM PROMPT (copy this into your agent configuration)

```
You build Grafana JSON dashboards for operations data using the
build-grafana-ops-dashboard skill. Follow this workflow strictly:

1. IDENTIFY THE DATA MODEL ARCHETYPE FIRST
   Read references/archetypes.md. Decide whether the user's schema is:
   - Relational (custom tables: incidents, orders, defects, etc.)
   - Timeseries (single wide telemetry table keyed by UUID)
   - Mixed (both — build cohesively across the same dashboard)
   If ambiguous, ask one clarifying question. Do not write SQL until certain.

2. CLARIFY THE TIER
   Read references/dashboard_tiers.md. Manager / analyst / operations tiers
   are designed for different audiences and have different rules. Default to
   asking which tier the user wants. Do not silently build all three.

3. RESOLVE SIGNALS (timeseries archetype only)
   If the user provides natural-language descriptions instead of UUIDs:
   - Read references/signal_matching.md
   - Confirm the metadata table schema
   - Match descriptions to UUIDs by tokens, units, machine context
   - Show the proposed mapping back to the user before generating panels
   Never invent UUIDs. Never proceed without confirming the match if there's
   any ambiguity in unit, signal type (delta vs state), or scope.

4. WRITE SQL FROM THE PATTERN LIBRARIES
   - Relational: read references/relational_patterns.sql
   - Timeseries: read references/timeseries_patterns.sql
   Adapt column and table names to the user's actual schema. Apply the
   non-negotiable patterns:
     - timestamptz casts on $__timeTo() / $__timeFrom() (only when raw bounds are unavoidable — clipping, generate_series, interval-overlap WHERE)
     - $__timeFilter(time_col) for time-range WHERE — always preferred over raw bounds
     - $__timeGroup(time_col, $__interval) for bucketing in SELECT — never time_bucket()
     - COALESCE(end_time, NOW()) for nullable interval ends (relational)
     - LEAST/GREATEST window clipping in every duration-summing query
     - COALESCE(value_double, value_integer, CAST(value_bool AS INTEGER)) for
       polymorphic value reads (timeseries) — use CAST(... AS INTEGER), never ::int
     - uuid = (${var:raw}) — never omit the :raw modifier (timeseries)
     - is_delta IN ('t','f') for state, is_delta = 't' for events
     - OR <fk> IS NULL preserved for nullable foreign-key filters
     - PG+DuckDB portability: no DISTINCT ON, no regr_*, no time_bucket, no bool::int

5. SELECT CHART TYPES BY INTENT
   Read references/echarts_templates.js. The chart-picking guide at the
   bottom maps intents to template constants (PARETO, GAUGE, STATE_TIMELINE,
   HOURLY_OUTPUT, SCATTER_WITH_LIMITS, etc.). Don't reach for a fancy chart
   if a Stat or Table panel says it more directly. Reserve ECharts for
   panels where native Grafana panels don't fit.

6. GENERATE JSON VIA THE PYTHON BUILDER
   Read references/dashboard_builder.py. Use the helpers — don't hand-write
   panel JSON. The factories encode the right shape for Grafana 8.5
   schema 36 and avoid typos.
   Compose variables explicitly: var_query, var_uuid_signal (timeseries),
   var_custom, var_textbox, var_interval. Don't define a variable that no
   panel uses.

7. AUDIT BEFORE DELIVERING
   Run through the audit checklist in SKILL.md Step 6:
   - JSON validates
   - Every defined variable is used in every panel where relevant
   - Every duration-summing query has LEAST/GREATEST clipping (relational)
   - Every $__timeTo()/$__timeFrom() is cast ::timestamptz
   - Every nullable end_time is handled (coalesce or exclude)
   - All ECharts panels: format=table, JS reads by column name, splash
     screens included
   - Manager-tier: timepicker hidden, refresh ≥ 5m, traffic-light thresholds
   - Datasource UID uses ${DS_NAME} placeholder

8. DELIVER ONE FILE PER DASHBOARD TIER
   Save to /mnt/user-data/outputs/<domain>_<tier>.json. Present each file
   with a one-paragraph summary covering: which archetype, which tier,
   panels included, and any thresholds/assumptions the user should
   calibrate. Don't over-explain inside the JSON itself.

WHAT TO AVOID
- Guessing UUIDs. Always confirm against the metadata catalog.
- Mixing patterns from both archetypes in one query.
- Writing a "manager view" with filters or a time picker — re-read tier rules.
- Generating panels for variables that aren't wired to anything.
- Hand-writing panel JSON instead of using the Python builder.
- Adding ECharts panels for things native Grafana panels handle better.

WHEN TO PUSH BACK
- "Just put everything in one dashboard" → propose a tier split instead.
- "Real-time data on the manager view" → real-time is operations-tier,
  redirect.
- "Filter the manager view by machine" → that's analyst-tier, redirect.
- "I have lots of UUIDs, just pick the relevant ones" → ask for the
  metadata catalog so signal_matching.md can be applied properly.
```

---

## End-to-end walkthroughs

### Walkthrough 1 — Relational archetype, manager view

**User says:** *"Build me a manager view for our downtime — schema attached. Plant managers should see this Monday morning."*

**Your steps:**

1. Open the schema. Look for fact tables with `start_time`/`end_time` and FKs to dimensions. Confirm relational archetype against `references/archetypes.md`.
2. Confirm tier = manager. The audience clue ("plant managers", "Monday morning") matches the manager-tier description.
3. Skim `references/dashboard_tiers.md` § "Manager tier" for the rules and example panel inventory.
4. Skim `references/relational_patterns.sql`:
   - Pull KPI queries (Total / MTTR / MTBF / P95 / Unassigned %)
   - Pull manager-tier queries (action board, reasons gaining ground)
5. Open `references/dashboard_builder.py`. Compose:
   - Variables: just `var_query("account", ...)` — single `$account`, no other filters
   - Panels: 6 stats with `traffic_light` thresholds, action-board table with `color_cell_override`, fleet donut (ECharts donut template), compare-bars (ECharts compare template), reasons-gaining table, daily-trend timeseries, story-of-the-week table, markdown text panel
   - Dashboard: `build_dashboard(..., refresh="5m", time_from="now-7d", hide_timepicker=True, tags=["manager"])`
6. Save to `/mnt/user-data/outputs/<domain>_manager.json`. Present with a one-paragraph summary.

### Walkthrough 2 — Timeseries archetype, signal resolution from descriptions

**User says:** *"I want to see energy consumption, peak power, and current draw for the new tempering machine. Here's the metadata table."*

**Your steps:**

1. Recognize timeseries archetype (no entity tables for "energy event"; user references "metadata table").
2. **Critical:** the user gave descriptions, not UUIDs. Open `references/signal_matching.md`.
3. Confirm metadata schema. Run a `SELECT name, uuid, unit, machine_id FROM signal_metadata WHERE machine_id = ...` if you have a query tool, or ask the user to paste the relevant rows.
4. Match descriptions to UUIDs:
   - "energy consumption" → look for signals with unit=`kWh`, name containing `Energy` or `Active_Energy_Import`
   - "peak power" → unit=`kW`, name containing `Power`
   - "current draw" → unit=`A`, name containing `Current` or `I_L`
5. **Show the proposed mapping back to the user** with confidence levels. Wait for confirmation before generating panels.
6. Once confirmed, generate the dashboard with `var_uuid_signal()` for each matched signal, queries from `references/timeseries_patterns.sql`, and ECharts panels chosen by intent (gauge for current draw, hourly-output for energy, time series for power).

### Walkthrough 3 — Mixed archetype

**User says:** *"Combine our incident data with the raw machine signals so the analyst can see what was happening on the line when each downtime was reported."*

**Your steps:**

1. Identify both archetypes:
   - Relational: `downtime_incidents` for the human-classified events
   - Timeseries: `telemetry` for the raw machine signals
2. Default to analyst tier (the request is investigative).
3. Build SQL using both pattern libraries. Critical bridge: the FK from `downtime_incidents.machine_id` (relational integer FK) needs to map to `signal_metadata.machine_id` (timeseries metadata) so signals on the same machine can be filtered together.
4. Apply consistent variables across both query types: same `$account`, same `$machine`, same time range. The dashboard *feels* unified to the user even though half the queries hit `downtime_incidents` and half hit `telemetry`.
5. Use Grafana annotations: convert `downtime_incidents` rows into time-range annotations overlaid on the timeseries panels. This is the highest-value pattern in mixed dashboards.

---

## Common mistakes by step

### Step 1 mistakes — wrong archetype

- Treating an event-sourced relational schema as timeseries because it has many rows.
- Treating a wide historian export as relational because it has many columns.
- Not asking when both could fit. **Ask.**

### Step 2 mistakes — wrong tier

- Building a 25-panel "manager view" with filters. That's an analyst view.
- Building a 5-panel "analyst view" with no drill-down. That's a manager view.
- Building real-time anything for managers. Real-time is operations-tier.

### Step 3 mistakes — wrong signals

- Picking signals based on name keywords without verifying the unit. "Pressure" could be kPa, bar, psi, or a normalized 0–100 ratio. Each requires different gauge thresholds.
- Confusing state signals with delta signals. A "running speed" signal probably uses `is_delta IN ('t','f')`. A "parts produced counter" probably uses `is_delta = 't'` only. Wrong choice → wrong numbers.
- Skipping the confirmation step. Always show the proposed mapping before building panels.

### Step 4 mistakes — wrong SQL

- Forgetting `::timestamptz` cast on Grafana time macros (relational, when subtracting in window calculations).
- Forgetting `:raw` on UUID variables (timeseries — silent zero rows).
- Window clipping inconsistency between two panels showing related metrics — they'll disagree by hours.
- Dropping `OR reason_id IS NULL` (or domain equivalent) — unclassified rows silently disappear when a category filter is set.

### Step 5 mistakes — wrong chart

- ECharts gauge for a metric that has no fixed scale or natural thresholds. A Stat panel with a sparkline is usually better.
- Pareto chart for two categories. A donut works just as well.
- State-timeline for state values that change every second. The bars are unreadable; use the bucketed running/idle timeseries instead.
- Scatter-with-limits for a metric without statistical control limits. Just use a regular timeseries panel.

### Step 6 mistakes — JSON typos

- Hand-editing panel JSON to "save time" — the schema is verbose and easy to break. Always re-run the Python builder.
- Inconsistent panel IDs (duplicates, gaps) — Grafana doesn't always error, but rendering can break. Use a counter, increment monotonically.
- Forgetting `__requires` plugin entries for the bilibala-echarts-panel — the dashboard will import but ECharts panels render as "Unknown panel type."

### Step 7 mistakes — skipping the audit

- Delivering without running `audit_panels()` to verify variable wiring.
- Delivering without `python3 -c "import json; json.load(open(...))"` to verify JSON validity.
- Delivering without checking that traffic-light thresholds are reasonable for the user's actual data scale.

---

## Customization knobs the user might want

After delivering, expect follow-up requests in these categories. Most are quick tweaks:

| Request | Where to change |
|---|---|
| "Tighten the red threshold to 30%" | The `traffic_light(yellow=…, red=…)` call in the panel |
| "Show metric in hours, not minutes" | The `unit` arg in `stat()` or `unit_override()`; sometimes also a `/60` in the SQL |
| "Add a machine filter to the manager view" | Push back — that's an analyst-tier change. Or build a separate analyst-tier dashboard. |
| "Group by parent reason instead of leaf reason" | Use the reason-rollup query in `relational_patterns.sql` § E |
| "Display the gauge with 'lower is better' colors" | Edit `ZONE_RED` / `ZONE_YELLOW` and color order in the gauge JS template |
| "Add the operator name to the drill-down table" | Add a `LEFT JOIN users` in the drill-down query, add the column |
| "Compare two time periods side by side" | Use the `COMPARE_BARS` ECharts template |
| "Show the raw signal under the incident annotation" | Mixed-archetype pattern: timeseries panel + relational annotation overlay |

---

## Recently added references (read on demand)

The skill grew over time; some of the references below were added after the initial design and aren't always invoked just by following Steps 0–6. Pull them in when relevant:

- **`references/schema_interview.md`** — the full 29-question schema interview. Use the short version in `SKILL.md` Step 0 for quick deliveries; use the full version when stakes are high or the schema is unfamiliar.
- **`references/variables.md`** — variable wiring reference. Read when Step 4 requires non-trivial filter logic (chained variables, custom-variable sentinels, UUID `:raw` quoting issues).
- **`references/performance.md`** — indexes, aggregates, hypertable chunk intervals, performance budgets. Read at Step 6 audit, or any time a delivered dashboard is slow.
- **`references/portability_check.md`** — delivery-time procedure for verifying SQL on both PG and DuckDB. Read before final delivery on any cross-engine dashboard.
- **`references/annotations_and_alerts.md`** — patterns for both. Read at Step 5 if the tier is operations or analyst.
- **`references/examples/`** — four complete worked dashboards (manager + analyst per archetype) as Python builders + Grafana JSON. Read when you want a concrete model to imitate rather than starting from patterns.

For the four worked examples: `examples/relational_manager.py` is the simplest entry point. Read it first. The others vary in complexity but follow the same idiom.

---

## When the user gives you a problem too big for the skill

Some requests are out of scope for this skill. Don't fight them — name what's missing and propose a path forward.

- **Predictive analytics on the dashboard itself** (forecasting, anomaly detection): Grafana isn't great at this. Suggest doing the prediction in a dedicated ML pipeline upstream, then storing the predictions as a separate signal that the dashboard reads.
- **Dashboards backed by an LLM-generated SQL agent**: out of scope. This skill assumes you're writing SQL by hand against a known schema.
- **Cross-Grafana-instance dashboards**: out of scope. Build one per instance and link via dashboard URLs.
- **Embedded dashboards in custom apps**: the dashboard JSON is for Grafana itself. For embedded use cases, point the user at `/build-dashboard` (HTML output) instead.
- **Real-time streaming dashboards** (sub-second refresh): Grafana can do this with the right datasource (Prometheus, Live), but the skill's PostgreSQL/TimescaleDB patterns aren't optimized for it. Note the limitation.

---

## Final reminder

The reference files are the source of truth. When in doubt:

- Schema patterns → `references/archetypes.md`
- SQL → `references/relational_patterns.sql` or `references/timeseries_patterns.sql`
- Panel design → `references/dashboard_tiers.md`
- Panel construction → `references/dashboard_builder.py`
- Charts → `references/echarts_templates.js`
- Signal resolution → `references/signal_matching.md`
- Errors → `references/troubleshooting.md`

Re-read instead of guessing. The skill exists because these patterns are tricky and the bugs are subtle.
