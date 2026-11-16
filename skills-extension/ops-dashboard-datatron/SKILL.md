---
name: ops-dashboard-datatron
description: >-
  Apply a catalogued DATATRON Grafana dashboard (cooling KKA, press centres, utilities) to a plant's own machines in self-service: match the template's panels to the machine's tag list, list the data points that must be switched on first, build through the dashboard engine and pass the QA checklist before go-live. Use when a plant applies a catalogued dashboard itself, a DATATRON dashboard is reviewed, panels render flat or empty, or signals turn out to be disabled. Draft. Not for new dashboard types or the asset choice (ops-analytics-asset, ops-dashboard-engine) or a need the template does not cover (Lane 2).
license: MIT
metadata:
  id: ops-dashboard-datatron
  tier: technical
  lane: [lane-1, lane-2]
  new_state_lane: "Lane 1a (1a2), Lane 1b (1b4), Lane 2 (23)"
  new_state_step: "Apply the standard template (self-service); Standardized deployment, go live; Prototype"
  department_names: ["ops-dashboard-datatron", "datatron-dashboard-builder", "ops-grafana-dashboards"]
  owner_role: Digital-Business-Value-Engineer (DBVE); the plant key user in self-service mode
  authority_level: author the dashboard; publishing to a shared Grafana is human-approved
  status: draft
  requires: [dept-context]
  composes: [ops-dashboard-engine, catalog-usecase, catalog-guardrails]
  okf:
    type: Agent Skill
    title: DATATRON dashboards
    tags: [department-core, lane-1, technical]
---

# DATATRON dashboards

- Read `dept-context` first.
- Status: draft. The query and variable patterns live in the department package `ops-grafana-dashboards`, transcribed in the `ops-analytics-asset` reference `references/ops-grafana-dashboards.md`; this skill carries the procedure, the gates and the checklists.
- `ops-dashboard-engine` is the generic engine for the Grafana JSON itself.
- Terms: **data point** = one UUID entry on a DATATRON; **tag list** = the labelled data points of a machine; **signal** = what a panel shows; DATATRON names the system only.

## Purpose

- Let a plant key user apply a catalogued DATATRON dashboard (cooling KKA, press centres, utilities) to its own machines without building from a blank page, and prove it with a QA result.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Inputs and output

- **In:** the catalog entry and its template (`catalog-usecase`), the machine's tag list with labels, the plant's equipment family, the guardrails (`catalog-guardrails`).
- **Out:** the list of data points (UUIDs) to enable, the built dashboard JSON, the filled QA result, and after the pass a published example.

## Self-service mode (Lane 1a)

- The plant key user applies a **catalogued** dashboard (`catalog-usecase`) to its own machines.
- Anything the template does not cover is a deviation, routed to Lane 2, not a local extension.
- Passing the QA checklist is the go-live gate (`catalog-guardrails`).

## Procedure

1. **Start from the catalog entry** and its template; never from a blank dashboard or an ad-hoc copy.
2. **Select the signals** from the tag list for the equipment family (KKA cooling, press centre, utilities): match each panel of the template to one labelled data point; unmatched panels stay empty and are listed.
   - Check the label and the `config_comment` of each data point before trusting it; PLC integers are often scaled.
3. **List the data points to enable** with the template below. A disabled data point makes its panel render flat or empty, so list every one before the build and stop; the plant switches them on (datapoint-enablement intake).
4. **Build with the proven patterns** through `ops-dashboard-engine`: UUIDs through resolver variables (`uuid = (${var:raw})`), one time-filter dialect per dashboard, scaled values divided in the query.
5. **Run the QA checklist** below and record the result; it is the objective approval gate. Fix every failed line and re-run until clean.
6. **Publish** an approved dashboard to the use-case library as a reusable example; publishing to a shared Grafana is human-approved.

## Templates

```text
UUIDs to enable (one row per disabled data point; fictional example)
UUID                                  | Label                         | Why needed
--------------------------------------|-------------------------------|------------------
<uuid>                                | DB 35.D_56 flow temperature   | flow-temperature stat and trend
```

```text
QA result (one per dashboard)
Dashboard / plant / equipment family : <title> / <plant> / <family>
Catalog entry and template version   : <entry> / <version>
Checklist lines                      : <n passed> of <n>; failed lines and fix: <list or "none">
Data points still disabled           : <none | list, build stopped>
Deviation from the template          : <none | routed to Lane 2 as ...>
Result (pass / fail), checked by     : <pass|fail>, <role>   Date: <date>
```

## QA checklist (go-live gate)

- [ ] Declared datasource inputs are exactly the ones the dashboard uses
- [ ] The variable chain resolves (area, datatron, plc, hidden UUID resolvers) and SQL uses `${var:raw}` on templated dashboards
- [ ] The `is_delta` filter matches intent (`'t'` for counters, triggers and per-piece anchors; `'t','f'` for states and analog trends)
- [ ] Numeric values use the standard `COALESCE(value_double, value_integer, value_bool::integer)` extraction
- [ ] One time-filter dialect per dashboard; `LATERAL` subqueries use the literal form
- [ ] Machine-state mapping and colours match the estate standard
- [ ] Shift logic uses the 06/14/22 boundaries and a 06:00 production-day start
- [ ] Duration queries handle the open last segment; downtime has flicker protection
- [ ] Scaled values are divided correctly (for example `x0.1` becomes `/10.0`)
- [ ] Every panel has a human title with a unit; cloned rows are retitled
- [ ] Units, thresholds and `noValue` set; tags, title, `uid`, browser timezone, relative default time range
- [ ] Disabled but needed UUIDs are listed for enablement
- Source and the full wording: the checklist section of `references/ops-grafana-dashboards.md` in `ops-analytics-asset`.

## Example

```text
Request (fictional): plant applies the catalogued cooling (KKA) dashboard to its own plant.
Step 2: 11 of 12 template panels matched to labelled data points; "return temperature" has none -> listed as unmatched.
Step 3: 2 data points are disabled -> UUID list sent to the plant; build stops until they are enabled.
Step 4: flow temperature stored as a PLC integer, scaled x0.1 -> query divides by 10.0.
Step 5: QA result: 12 of 12 lines passed after one fix (one cloned row still titled "Unit 1"); result pass, checked by key user role.
```

## Human gate and AI-agent notes

- **Agent may:** match panels to data points, draft the UUID list, build through the engine, run the checklist and fill the QA result.
- **Humans decide:** the plant switches data points on; the plant key user signs the QA result; publishing to a shared Grafana is human-approved.

## Pitfalls

- **Scaled PLC integers**: many values are stored times ten; a raw value plotted as is looks plausible and is wrong. Check `config_comment`.
- **`is_delta` has no written definition and appears in eight spellings** in the estate; use the package's reading and flag any panel that mixes them.
- **Disabled data points**: the panel renders flat, which looks like a quiet machine. List the UUID and stop.
- **Two time-filter dialects** are in production; mixing them in one dashboard gives inconsistent ranges.
- Do not extend a catalogued template locally; route the new need to Lane 2, because local extensions break comparability.
- Do not publish without the QA checklist passed.

## Definition of done

- The UUID list was produced and no build rests on a disabled data point; the dashboard follows the template.
- The QA result is filled with a pass and a named role; the deviation field is empty or routed to Lane 2.

## Open - not yet in this skill

- The department master package (`ops-grafana-dashboards.zip`) is not in the registry; the transcription in `ops-analytics-asset` is the source and is itself draft. See `references/background.md` for open questions.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/background.md`](references/background.md) | You need the context, the open questions and the sources used; never an instruction |
| [`references/outputs.md`](references/outputs.md) | Before handing over: what must be delivered, to whom |
| `ops-analytics-asset`, `references/ops-grafana-dashboards.md` | Writing a query: schema, value extraction, time-filter dialects, variable chain, panel recipes, equipment context |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
