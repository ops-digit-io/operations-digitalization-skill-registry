# variables.md — Grafana variable wiring reference

Every variable defined in a dashboard must be used in every panel where it's logically relevant. A defined-but-unused variable is the most common silent bug in ops dashboards: filters look like they work, but specific panels ignore them and quietly show stale numbers.

This file consolidates everything about variables — how to define, wire, refresh, and debug them — so the patterns and audit checks live in one place.

---

## The mental model

A Grafana variable is a placeholder Grafana substitutes into the SQL string before sending the query to the database. The substitution happens client-side; the database never sees `$account` — it sees `1`, or `1, 2, 3`, or `'all'`, depending on how Grafana expanded it.

Three things determine how that expansion behaves:

1. **The variable type** — `query`, `custom`, `textbox`, `interval`, `datasource`, `constant`.
2. **The selection mode** — single-value, multi-value, "All" included or not.
3. **The format modifier** in the SQL — `${var}`, `${var:raw}`, `${var:csv}`, `${var:singlequote}`, etc.

Most variable bugs are mismatches between these three. The patterns below cover the combinations that show up in real ops dashboards.

---

## Variable types and when to use them

| Type | When | Example |
|---|---|---|
| `query` | Dropdown sourced from the database. By far the most common. | `$machine`, `$reason`, `$account`, signal UUIDs |
| `custom` | Static list of options not in the DB | `$severity` (critical / major / minor / all), tri-state flags |
| `textbox` | Free-text numeric or string input | `$min_duration_min`, `$threshold_value` |
| `interval` | Time-bucket size selector | `$bucket` (1m, 5m, 15m, 1h) — separate from `$__interval` |
| `datasource` | Switch between configured datasources | Multi-environment dashboards (dev/stg/prod) |
| `constant` | Hidden, can't change at runtime | API keys baked into URLs (rare in ops) |

---

## Defining a query variable

The variable's SQL must return two specific column aliases — anything else and the dropdown stays empty.

```sql
SELECT
  m.name AS __text,    -- shown in the dropdown
  m.id   AS __value    -- substituted into panel SQL
FROM machines m
WHERE m.is_ignored = false
  AND m.account_id IN ($account)   -- chained on $account
ORDER BY m.name;
```

Common mistakes:

- Aliasing as `name` / `id` instead of `__text` / `__value` — Grafana ignores other names. Drop-down is empty, no error.
- Forgetting to filter out soft-deleted rows — archived machines appear in the picker.
- Forgetting to chain on `$account` — every tenant sees every other tenant's machines.

---

## Multi-select, "All", and `IN ($var)`

For multi-select variables, set `multi: true` and `includeAll: true`. The "All" option tells Grafana to expand to every value, not the literal string `'all'`.

In the SQL, always use `IN ($var)`:

```sql
WHERE machine_id IN ($machine)
```

When the user selects "All", Grafana expands `$machine` to `1, 2, 3, ...`. When they select two specific values, it expands to `1, 2`. Both shapes are valid SQL. The `IN ()` empty-list case (Grafana's bug when the variable hasn't loaded) is the failure mode — set `includeAll: true` so it never produces empty lists.

---

## The three filter patterns

These three patterns repeat across every analyst-tier dashboard. Memorize them.

### 1. Optional sentinel for custom variables

For categorical filters with discrete values plus an "All" choice — typical for `$severity`, `$status`, anything not from the DB:

```sql
AND ('$severity' = 'all' OR CAST(severity AS TEXT) = '$severity')
```

The variable's options must include `'all'` as a literal value. Note the **quotes around `$severity`** — these turn it into a string literal so the comparison works.

### 2. Tri-state integer escape

For boolean-like filters that need three states: only-true, only-false, both. Use a custom variable with values `-1`, `0`, `1`:

```sql
AND ($auto_detected = -1 OR CAST(is_auto_detected AS INTEGER) = $auto_detected)
```

`-1` is the "show all" sentinel because it can't match either `0` or `1`. The `CAST(... AS INTEGER)` is required for PG/DuckDB portability — `bool::int` is Postgres-only.

### 3. NULL preservation for nullable foreign keys

`IN (1, 2, 3)` does not match NULL. If a fact table has a nullable FK and you filter on it, every NULL row vanishes silently — including legitimately unclassified records that should be visible.

```sql
AND ((reason_id IN ($reason)) OR reason_id IS NULL)
```

Use this on every nullable foreign-key filter without exception. Common columns: `reason_id`, `defect_type_id`, `parent_reason_id`, `assigned_to_id`.

---

## UUID variables for the timeseries archetype

UUIDs need the `:raw` format modifier. Without it, Grafana wraps the value in single quotes that double up against the literal quotes already in the UUID string, and the comparison silently returns zero rows.

```sql
-- Variable definition:
SELECT name AS __text, uuid AS __value
FROM signal_metadata
WHERE machine_id IN ($machine)
ORDER BY name;
```

```sql
-- Usage in panel SQL:
WHERE uuid = (${signal_var:raw})
```

Always wrap in parentheses too — `(${var:raw})` — for visual clarity and to prevent ambiguity if the surrounding expression has its own operators.

Diagnostic when a signal panel returns zero rows: open Inspect → Query, look at the rendered UUID. If it shows `''<uuid>''` (doubled quotes), `:raw` is missing.

---

## Refresh order and chained variables

Variables can depend on each other (`$machine` filtered by `$account`, `$reason` filtered by both). Grafana resolves variables in the order they appear in the templating list — top to bottom. If a variable depends on one defined below it, the dependency hasn't loaded yet on first render and the dependent variable shows empty.

Rules:

- **Order parents before children** in the templating list. `$account` first, then `$machine`, then `$reason`.
- **Set `refresh` correctly:**
  - `refresh: 1` ("On Dashboard Load") — for variables that don't change with the time range.
  - `refresh: 2` ("On Time Range Change") — for variables whose values depend on what's in the visible window. Use sparingly; it makes the time picker reload slow.
- **Hide internal-use variables** (`hide: 2`) so they don't clutter the UI but can still drive filters in panel SQL.

---

## Variable-driven panel titles

Panel titles can interpolate variables: `Downtime — $machine`. Useful for drill-down dashboards where one panel shows the selected entity. Two caveats:

- Multi-value variables expand to a comma-separated list, which can produce ugly titles like `Downtime — Machine A,Machine B,Machine C`. Switch the variable to single-select for title use, or use the `${machine:text}` modifier which returns just the display labels.
- "All" expands to `All` literally, which is usually fine.

---

## Audit checklist

Before delivery, walk through every variable and answer these:

- [ ] Variable's defining SQL returns `__text` / `__value` columns
- [ ] Variable's defining SQL filters out soft-deleted rows
- [ ] Variable's defining SQL is chained on `$account` (or whatever the multi-tenant column is)
- [ ] Variable's `refresh` is set explicitly — not left at default `0` ("Never")
- [ ] Variable order in the templating list puts parents before children
- [ ] Multi-select variables have `multi: true` and `includeAll: true`
- [ ] Every panel SQL uses each variable that's logically relevant — grep panel JSON for the variable name to verify
- [ ] UUID variables use `(${var:raw})` everywhere they appear
- [ ] Nullable FK filters include `OR <fk> IS NULL`
- [ ] Tri-state custom variables use `CAST(x AS INTEGER)`, not `x::int`
- [ ] Custom-variable sentinels (`'all'`, `-1`) match the variable's options exactly

---

## Quick debug

When a panel renders blank or "off" and you suspect a variable:

1. **Inspect → Query.** Read the rendered SQL. Variables expanded literally? Empty list? Wrong format?
2. **Run the rendered SQL directly** against the database. If it errors there, the variable is producing bad SQL. If it returns rows there but Grafana shows nothing, the issue is panel-side (column names, format, splash screens).
3. **Toggle the variable values.** Pick "All" vs specific values vs single specific. The combination that fails reveals the missing pattern (sentinel, NULL preservation, escape).
