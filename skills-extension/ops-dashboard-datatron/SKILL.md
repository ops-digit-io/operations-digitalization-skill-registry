---
name: ops-dashboard-datatron
description: >-
  Build or apply a Grafana dashboard on the DATATRON telemetry schema (PostgreSQL / TimescaleDB) for
  cooling (KKA), press centres and utilities - the department's ops-dashboard-datatron, the engine of
  Lane 1a self-service. Selects the signals from the tag list, uses the proven query and variable
  patterns, handles scaled PLC values, outputs the list of datapoint UUIDs that must be enabled before
  the build, and passes the QA checklist as the go-live gate. Use when a plant applies a catalogued
  dashboard itself, when a DATATRON dashboard is built or reviewed, or when signals turn out to be
  disabled.
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
  requires: [od-context]
  composes: [build-grafana-ops-dashboard, catalog-usecase, catalog-guardrails]
  okf:
    type: Agent Skill
    title: DATATRON dashboards
    tags: [department-core, lane-1, technical]
---
# DATATRON dashboards

Read `od-context` first. The department's `ops-dashboard-datatron` (split from its `ops-grafana-dashboards` package;
the stakeholder-deck part went to `deck-stakeholder`). The package holds the query and variable patterns and the QA
checklist and is the master; this skill carries the procedure and the gates. `build-grafana-ops-dashboard` is the generic
engine for the Grafana JSON itself.

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Self-service mode (Lane 1a)

The plant key user applies a **catalogued** dashboard (`catalog-usecase`) to its own machines. Anything the template
does not cover is a deviation, routed to Lane 2, not a local extension. Passing the QA checklist is the go-live gate
(`catalog-guardrails`).

## Procedure

1. **Start from the catalog entry** and its template; never from a blank dashboard or an ad-hoc copy.
2. **Select the signals** from the DATATRON tag list for the equipment family (KKA cooling, press centre, utilities).
3. **List the datapoint UUIDs to enable.** Disabled signals are made explicit before the build starts; the plant
   switches them on (datapoint-enablement intake).
4. **Build with the proven patterns** (queries, variables, scaled-PLC handling) through `build-grafana-ops-dashboard`.
5. **Run the QA checklist**; it is the objective approval gate.
6. **Publish** an approved dashboard to the use-case library as a reusable example; publishing to a shared Grafana is
   human-approved.

## Open - in the department package, not yet here

- ⟨Query and variable patterns, scaled-PLC handling, the QA checklist⟩ - transcribe from `ops-grafana-dashboards.zip`.
- ⟨Value model coupled to the dashboard's own measured queries⟩ - shared with `od-benefit-calculation` (`bc-value-model`).
- Coverage beyond KKA, press centres and utilities (conveyors) is a department roadmap item.

## Do not

- Do not build on a signal that is disabled; list its UUID and stop.
- Do not extend a catalogued template locally; route the new need to Lane 2.
- Do not publish without the QA checklist passed.
