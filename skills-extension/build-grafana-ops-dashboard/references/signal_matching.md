---
type: Skill Reference
title: Signal matching
description: "The timeseries archetype's core problem: the user knows what they want to see but not which UUIDs hold it."
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [grafana, signals]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Signal matching — picking the right UUIDs from a description

A core challenge of the timeseries archetype: **the user knows what they want to see, but not which UUIDs hold the data**. They tell you "I want to see energy consumption and power draw for machine X" — your job is to translate that into the specific UUIDs and queries.

This guide covers the workflow. Use it whenever the user provides:

- A **machine UUID** (or machine name) as context
- A **natural-language description** of what they want visualized

…instead of (or in addition to) explicit UUIDs.

---

## The metadata table

Timeseries archetypes typically have a metadata / catalog table that maps UUIDs to human-readable signal info. The exact schema varies, but a typical shape:

```sql
signal_metadata (
  uuid          uuid primary key,
  name          text,         -- e.g. "PLC_Tempering_2.Blocks.109.Total_Active_Energy_Import_kWh"
  description   text,         -- optional human description
  unit          text,         -- e.g. "kWh", "°C", "rpm"
  machine_id    uuid,         -- which machine this signal belongs to
  data_type     text,         -- 'double' | 'integer' | 'bool' | 'string'
  is_delta      bool,         -- whether the signal is event/delta or state
  tags          text[]        -- optional categorization tags
)
```

Common variations: this table may be called `tags`, `signals`, `points`, `parameters`. The columns above may have different names — `signal_id` instead of `uuid`, `display_name` instead of `name`, etc. **Always confirm the actual schema before writing the query.**

If no metadata table exists, ask the user. Without it, signal matching is impossible — you can only work with explicit UUIDs.

---

## The workflow

### Step 1 — Confirm the metadata schema

```sql
-- Inspect the metadata table to understand its columns
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'signal_metadata'
ORDER BY ordinal_position;
```

Or simpler — ask the user for one example row.

### Step 2 — Query candidates filtered by machine

Pull all signals for the given machine, with enough info to score them by relevance:

```sql
SELECT
  uuid,
  name,
  description,
  unit
FROM signal_metadata
WHERE machine_id = '${machine_uuid}'
ORDER BY name;
```

Don't filter by description text in SQL — you don't know yet what the user wants. Pull everything for the machine, then narrow down.

For a machine with hundreds of signals (common with PLCs), pre-filter by signal type or naming pattern:

```sql
-- Energy-related only
SELECT uuid, name, description, unit
FROM signal_metadata
WHERE machine_id = '${machine_uuid}'
  AND (name ILIKE '%energy%'
       OR name ILIKE '%power%'
       OR name ILIKE '%kwh%'
       OR name ILIKE '%active%'
       OR unit IN ('kWh', 'kW', 'W', 'A', 'V'))
ORDER BY name;
```

### Step 3 — Match the user's description to candidates

This is the core matching step. Score each candidate by how well it matches the user's request, then either:

- **Auto-pick** the top candidates if the match is unambiguous, OR
- **Present a short list** to the user for confirmation if ambiguous

#### Matching heuristics (in order of importance)

1. **Unit match.** If the user says "current draw," signals with unit `A` (amperes) score high. "Power" → `kW`. "Temperature" → `°C` / `°F`. "Speed" → `m/min`, `rpm`, `m/s`.

2. **Keyword match in `name` and `description`.** Tokenize both the request and each candidate's name + description. Score by overlap. Don't just look for exact matches — manufacturing names often have hierarchical paths (`PLC_Tempering_2.Blocks.109_Energy_DB.Total_Active_Energy_Import_kWh`) where the meaningful tokens are deep in the path.

3. **Synonym expansion.** Common manufacturing synonyms:
   - "energy" ≈ kWh, Wh, "energy_import", "active_energy"
   - "power" ≈ kW, W, "active_power", "instantaneous_power"
   - "current" ≈ A, "phase current", "L1/L2/L3 current"
   - "speed" ≈ rpm, m/min, "feed", "motor speed"
   - "temperature" ≈ temp, °C, "actual_temp", "process_temp"
   - "pressure" ≈ bar, Pa, "system pressure"
   - "running" ≈ state, run/idle, machine_state, is_running
   - "OK parts" ≈ good_count, ok_count, gut_teile (German)
   - "NOK parts" ≈ scrap_count, defect_count, schlecht_teile, ausschuss

4. **`is_delta` filter.** If the user wants a counter (cumulative parts, total energy), prefer `is_delta = false` (state) for cumulative reading or `is_delta = true` for per-event increments. Cumulative-vs-target queries (template 11) typically use state-shaped signals.

5. **Reject ambiguity.** If multiple signals tie on score, don't guess — ask the user.

### Step 4 — Present candidates and confirm

For each visualization the user requested, present 1–3 candidates with:

- The signal name (full path)
- The unit
- A one-line description
- Why you picked it

Then either pick the top one (if confident) or ask for confirmation. Example:

> For "energy consumption per hour", I found these signals on machine X:
>
> 1. `PLC_T2.Blocks.109_Energy_DB.Total_Active_Energy_Import_kWh` (unit: kWh) — best match, cumulative meter
> 2. `PLC_T2.Tags.Total_Active_Energy_import_Wh` (unit: Wh) — alternate, in Watt-hours (would need ÷1000)
>
> Going with #1. The dashboard query will use this UUID. Tell me if you'd prefer #2.

This lets the user catch mismatches before the dashboard is generated, and creates a paper trail of *why* each signal was chosen — useful when revisiting the dashboard months later.

### Step 5 — Generate the SQL

Once signals are confirmed, plug the UUIDs into the query patterns from `timeseries_patterns.sql`. Use Grafana variables defined via `var_uuid_signal()` so the user can override choices in the dashboard UI later.

---

## SQL patterns for metadata querying

### List all signals on a machine with type info

```sql
SELECT
  sm.uuid,
  sm.name,
  sm.description,
  sm.unit,
  sm.is_delta,
  -- Detect data type from sample data
  CASE
    WHEN EXISTS (SELECT 1 FROM telemetry t WHERE t.uuid = sm.uuid AND t.value_double IS NOT NULL LIMIT 1)
      THEN 'double'
    WHEN EXISTS (SELECT 1 FROM telemetry t WHERE t.uuid = sm.uuid AND t.value_integer IS NOT NULL LIMIT 1)
      THEN 'integer'
    WHEN EXISTS (SELECT 1 FROM telemetry t WHERE t.uuid = sm.uuid AND t.value_bool IS NOT NULL LIMIT 1)
      THEN 'bool'
    WHEN EXISTS (SELECT 1 FROM telemetry t WHERE t.uuid = sm.uuid AND t.value_string IS NOT NULL LIMIT 1)
      THEN 'string'
    ELSE 'unknown'
  END AS detected_type,
  -- Last sample time as freshness indicator
  (SELECT MAX(systime) FROM telemetry t WHERE t.uuid = sm.uuid) AS last_seen
FROM signal_metadata sm
WHERE sm.machine_id = '${machine_uuid}'
ORDER BY sm.name;
```

### Search by free-text description

```sql
SELECT uuid, name, description, unit
FROM signal_metadata
WHERE machine_id = '${machine_uuid}'
  AND (
    name        ILIKE '%' || $search_term || '%'
    OR description ILIKE '%' || $search_term || '%'
  )
ORDER BY
  -- Prioritize name matches over description matches
  CASE WHEN name ILIKE '%' || $search_term || '%' THEN 0 ELSE 1 END,
  name;
```

### Get signals with sample values (sanity check before committing)

```sql
SELECT
  sm.uuid,
  sm.name,
  sm.unit,
  -- Show last value as a sanity check
  (
    SELECT COALESCE(value_double::text, value_integer::text, value_bool::text, value_string)
    FROM telemetry t
    WHERE t.uuid = sm.uuid
    ORDER BY systime DESC LIMIT 1
  ) AS last_value,
  (
    SELECT systime
    FROM telemetry t
    WHERE t.uuid = sm.uuid
    ORDER BY systime DESC LIMIT 1
  ) AS last_seen
FROM signal_metadata sm
WHERE sm.machine_id = '${machine_uuid}'
  AND sm.uuid = ANY('{<uuid1>, <uuid2>, ...}')
ORDER BY sm.name;
```

This is useful right before generating the final dashboard — verify the picked UUIDs actually have recent data.

---

## Building the variable for Grafana

Once a UUID has been picked, define a variable that lets the user re-pick later:

```sql
-- Variable definition, contextualized by the active machine variable
SELECT name AS __text, uuid AS __value
FROM signal_metadata
WHERE machine_id IN ($machine)
  -- Optional further narrowing:
  AND (name ILIKE '%energy%' OR unit IN ('kWh', 'Wh'))
ORDER BY name;
```

Use `var_uuid_signal()` from `dashboard_builder.py`:

```python
var_uuid_signal(
    name="energy_signal",
    label="ENERGY SIGNAL",
    signal_table="signal_metadata",
    name_col="name",
    uuid_col="uuid",
    where_clause="AND machine_id IN ($machine) AND (name ILIKE '%energy%' OR unit IN ('kWh','Wh'))",
)
```

Then in panel SQL: `WHERE uuid = (${energy_signal:raw})`.

---

## When matching fails

Cases where automated matching can't pick:

- **Multiple equally-good candidates** (e.g. `Phase_L1_Current`, `Phase_L2_Current`, `Phase_L3_Current` all match "current draw"). Ask the user which phase or whether to show all three.
- **Description is too vague** ("show me the data"). Ask for narrower intent.
- **No metadata table exists.** Tell the user; offer to work with explicit UUIDs they provide manually.
- **Metadata table exists but has no useful descriptions** (just opaque PLC tag paths). Walk the user through identifying signals by tag prefix or unit.

In all these cases: **ask before guessing**. A wrong UUID produces a working dashboard that shows the wrong data — far worse than asking one extra question.

---

## End-to-end example

User says:
> "Build me a dashboard for machine `9cd63e77-36b4-47f6-bb27-ec27eaaf711d` showing energy consumption per hour and the current power draw."

Workflow:

1. **Query candidates for the machine:**
   ```sql
   SELECT uuid, name, description, unit
   FROM signal_metadata
   WHERE machine_id = '9cd63e77-36b4-47f6-bb27-ec27eaaf711d'
     AND (name ILIKE '%energy%' OR name ILIKE '%power%'
          OR unit IN ('kWh','Wh','kW','W'))
   ORDER BY name;
   ```

2. **Score and pick:**
   - For "energy consumption per hour": pick the cumulative kWh signal (use template 7 line+area, computing hourly delta with MAX − MIN per hour bucket)
   - For "current power draw": pick the kW signal (use template 6 gauge, with `MIN=0`, `MAX=<machine rated power>`, zones tuned to circuit limits)

3. **Confirm with user:**
   > For energy: I found `PLC.Total_Active_Energy_Import_kWh` (unit: kWh, cumulative meter). For current power: `PLC.Active_Power_kW`. Going with these unless you'd prefer alternates.

4. **Generate dashboard JSON** using `timeseries_patterns.sql` queries plus the `ECHARTS_LINE_AREA_JS` and `ECHARTS_GAUGE_JS` templates.

5. **Define variables** so the user can swap signals via the dashboard UI:
   ```python
   var_uuid_signal("energy_signal", "ENERGY",
                   where_clause="AND machine_id IN ($machine) AND unit = 'kWh'"),
   var_uuid_signal("power_signal", "POWER",
                   where_clause="AND machine_id IN ($machine) AND unit IN ('kW','W')"),
   ```
