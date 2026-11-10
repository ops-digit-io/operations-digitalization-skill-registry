---
type: Map of Content
title: Worked Grafana examples
description: "Four complete dashboards demonstrating the skill's rules end to end, each in build-script and finished-JSON form."
resource: ../../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [grafana, examples]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Worked examples

Four complete dashboards demonstrating the skill's rules end-to-end. Each example exists in two forms:

- `*.py` — Python builder script that generates the dashboard. Easier to read, easier to modify, idiomatic. Run it to regenerate the JSON.
- `*.json` — the resulting Grafana dashboard JSON, importable into Grafana 8.5+.

## The four examples

| File | Archetype | Tier | What it demonstrates |
|---|---|---|---|
| `relational_manager.py` / `.json` | Relational | Manager | Fixed-window WoW deltas, traffic-light KPIs, action-board ranking with portable top-N (ROW_NUMBER instead of DISTINCT ON), zero-filled daily trend |
| `relational_analyst.py` / `.json` | Relational | Analyst | Full filter set wired through every panel, $__timeFilter / $__timeGroup default usage, ECharts Pareto, drill-down detail table, data-quality KPIs |
| `timeseries_manager.py` / `.json` | Timeseries | Manager | Aggregating UUID-keyed long-format down to per-machine KPIs, state-duration with window clipping, data-staleness check, daily zero-filled trend |
| `timeseries_analyst.py` / `.json` | Timeseries | Analyst | UUID variables with `:raw` modifier, polymorphic value reads with `CAST(value_bool AS INTEGER)`, state-duration breakdown, counter reset detection, two-signal correlation via bucketed inner join |

## How to use these

**Reading order if you're new to the skill:** start with `relational_manager.py` — it's the simplest and demonstrates the manager-tier conventions (fixed window, no filters, traffic lights). Then read `relational_analyst.py` to see the full filter set wired in. The two timeseries examples follow the same pattern but with the polymorphic value pattern and UUID variables instead.

**Reading the SQL:** every panel's SQL appears as a Python string in the script. Search the Python file for the panel title to find its query. The SQL strings are intentionally long and verbose — none of the SQL is hidden inside helpers, so you can copy any panel's SQL directly to inspect or adapt.

**Modifying for your schema:** change the table names and column names in the SQL strings. The structure (CTE shape, window functions, JOIN order) is portable; the names aren't. Search-and-replace works for renames; the `WHERE` and `JOIN` blocks are the parts that need attention if your schema differs structurally.

**Importing the JSON:** Grafana → Dashboards → New → Import → upload the `.json` file. You'll be prompted to pick a datasource (this is the `${DS_NAME}` placeholder doing its job).

## What these examples are NOT

- **Not finished products.** Names of tables, columns, and signal patterns reflect the schemas documented in `relational_patterns.sql` and `timeseries_patterns.sql`. They will not match your schema exactly.
- **Not exhaustive.** Each example covers the most common panels in its tier. Operations-tier examples are not included because their content is highly site-specific (live machine state on the floor display).
- **Not a substitute for the rules in SKILL.md.** Reading these examples helps with pattern matching but doesn't replace understanding why each rule exists.

## Verifying the examples follow the rules

```bash
# Regenerate all four:
for f in /home/claude/references/examples/*.py; do
  python3 "$f"
done

# Validate JSON:
for f in /home/claude/references/examples/*.json; do
  python3 -c "import json; json.load(open('$f'))"
done

# Grep for forbidden constructs:
grep -E 'time_bucket|DISTINCT ON|::int[^e]|regr_(slope|intercept|r2)' \
  /home/claude/references/examples/*.json && echo "FOUND VIOLATIONS" || echo "OK"
```

Should print `OK`. If any of the three checks fail, an example needs fixing.

## Adapting these into your dashboard

Three steps:

1. **Pick the closest example** to what you want — the right archetype, the right tier.
2. **Copy the `.py` file** to a new name and edit the table/column names to match your schema.
3. **Run it.** The output `.json` is your starting point.

This is the workflow the skill is optimized for: examples as editable templates, not finished products.
