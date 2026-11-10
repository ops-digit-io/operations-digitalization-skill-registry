---
name: od-analytics-asset-build
description: >-
  Build the thing the plant actually opens — a dashboard, report, analytics workflow, app
  or agent — so that it is consumed inside a real moment in the day, diagnosable by the
  plant, and countable in the portfolio. Covers choosing the asset type, designing for the
  ritual that consumes it, the Grafana and Power BI reality, recording the asset and its
  utilization expectation, and knowing when not to build. Use whenever a delivery asset is
  being designed or built, when an existing one is being reworked, or when choosing
  between a dashboard, a report and an app.
license: MIT
metadata:
  id: od-analytics-asset-build
  tier: practice
  lane: [lane-1, lane-2]
  new_state_lane: "Lane 1a (1a2), Lane 1b (1b4), Lane 2 (23, 26)"
  new_state_step: "Apply the standard template (self-service); Standardized deployment, go live, confirm adoption; Prototype / click-dummy, validated with the recipient; Implement, evaluate impact, ensure adoption, catalogue"
  department_names: ["ops-dashboard-datatron (self-service mode, external engine)"]
  owner_role: Digital-Business-Value-Engineer (DBVE)
  authority_level: draft/author the asset; publishing externally is human-approved
  status: stable
  sources_read: 2026-11-10
  requires: [od-context]
  composes: [build-grafana-ops-dashboard, od-data-availability-check, od-handover-and-adoption, od-use-case-standardization, catalog-usecase]
  derived_from:
    - "Work vault, OD Department Knowledge/OD-instance/30-skills/ops-grafana-dashboards.zip (SKILL.md), read 2026-11-10"
    - ops-knowledge-graph/_knowledge/10-Department/Operating model.md
    - ops-knowledge-graph/_knowledge/10-Department/Rituals.md
    - ops-knowledge-graph/_knowledge/20-Done/Grafana dashboard screenshot automation.md
    - ops-knowledge-graph/.../20-lanes/analytical-support-service/{playbook,skills}.md
    - Kimball, R. and Ross, M. (2013). The Data Warehouse Toolkit / the Kimball Lifecycle (3rd ed.), Wiley — the requirements-track/data-track/BI-track structure and the deployment-readiness gate, adapted below to this registry's own upstream/downstream skills.
    - "Few, S. (2006). Information Dashboard Design: The Effective Visual Communication of Data, O'Reilly — single-screen/at-a-glance design, reducing non-data pixels, the common design mistakes this skill's validation checklist is built from."
    - Work vault (Work-OpsDigit-Knowledge), Dashboard Exports specs SPEC-00 to SPEC-04 with their data files, the Dashboard Notes, the change reports, a sample of the JSON exports, Graph/Use Case Views (template views, template-standards, Dashboard Use Cases - Overview), the dashboard family notes in Graph/Use Cases, Case Groups - Overview, Vault Gap Analysis - SharePoint and Grafana Full Text and Slide Index for the dashboard tool evaluation, read 2026-11-05
    - "`build-grafana-ops-dashboard` (this registry, vendored) — the tool-specific build mechanics this skill routes into once \"Dashboard\" is chosen; not re-derived here."
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT (README, lane 1-3), read 2026-11-10"
    - "Work vault, OD Department Knowledge/OD-instance/skills-inventory-and-roadmap.md and OD_Skill_Naming_Convention.md, read 2026-11-10"
  okf:
    type: Agent Skill
    title: Analytics asset build
    tags: [analytical-support-service, practice, use-case-support-service]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Analytics asset build

Read `od-context` first. Run `od-data-availability-check` before building anything.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/ops-grafana-dashboards.md`](references/ops-grafana-dashboards.md) | **Building a DATATRON dashboard**: the department package (master) - families, drill-down, schema, queries, variables, panel recipes, ECharts, andon, datapoint enablement, equipment context |
| [`references/lifecycle-and-validation.md`](references/lifecycle-and-validation.md) | The build lifecycle mapped onto this registry's own upstream/downstream skills, and the validation checklist that separates "it renders" from "it is correct" |
| [`references/asset-type-and-tier.md`](references/asset-type-and-tier.md) | The asset-type decision worked through, and exactly where this skill's job ends and `build-grafana-ops-dashboard`'s begins once "Dashboard" is chosen |
| [`references/dashboard-estate-baseline.md`](references/dashboard-estate-baseline.md) | **How to read and measure the plant Grafana estate** (no figures). What to look up per plant, which data-source and query patterns to expect, lifecycle and churn - and the answer to the data-source question left open in the vendored skill's OD note |
| [`references/dashboard-families-catalogue.md`](references/dashboard-families-catalogue.md) | **Look here before building.** The family groups, the sharing classes (central / template / same name different content / plant-specific), and 14 family cards with the signals each needs and the traps seen |
| [`references/dashboard-worked-examples.md`](references/dashboard-worked-examples.md) | 14 illustrative dashboard patterns, each with the lesson it teaches, and how to pick real ones |
| [`references/dashboard-json-sample.md`](references/dashboard-json-sample.md) | How to sample dashboard JSON, and the nine query patterns found |
| [`references/capability-templates-and-placement.md`](references/capability-templates-and-placement.md) | The 11 templates, the 13 placement rules and their precedence, how case groups work, how to place a new asset |
| [`references/dashboard-spec-and-change-report-patterns.md`](references/dashboard-spec-and-change-report-patterns.md) | **Structure of a dashboard spec set** (hub, baseline, data contract, authoring standard, families), requirement id families, the requirements and summary pair with its markers, reverse-engineering routine, how to read the change and creation reports |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | **How the step runs in the chain**: the dashboard-without-action-owner smell, the generative-AI dashboard process, reconciling with paper records, sprint practice, handoff contract, AI agent operating notes |
| [`assets/dashboard-requirements-template.md`](assets/dashboard-requirements-template.md) | **Template.** Requirements specification and summary for one system's dashboards, with the observed / issue / open markers and the common requirements |
| [`assets/dashboard-review-checklist.md`](assets/dashboard-review-checklist.md) | **Checklist.** Ritual, family, signal binding, authoring rules with how to check each on the current export, placement, delivery |

**This skill does not re-derive Grafana build mechanics.** `build-grafana-ops-dashboard` already
owns the SQL patterns, the manager/analyst/operations tiers, the variable wiring and the
ECharts templates in depth — this skill is the layer above it: which asset type, for which
ritual, validated against what, handed off to whom. Once the asset type is "Dashboard," go
straight to that skill's Step 0.

## What this function actually produces

Across the use cases that record an output asset, the **dashboard** is by far the most common
output; reports, apps, analytics workflows and agents are rare (re-count on the use-case list
before quoting a split). The dashboard is the default output, and the default is worth
questioning rather than inherited.

| Asset | Fits when |
|---|---|
| **Dashboard** | A number has to be current at the line, inside a recurring moment |
| **Report** | A question is asked on a cadence and the answer is read away from the line |
| **Analytics workflow** | The insight is derived, repeatable, and consumed by another system or analysis |
| **App** | The user has to *enter* or *decide* something, not only read |
| **Agent** | The work is judgement over data on a cadence, with a named responsible human |

## Design for the ritual, not the data

**A dashboard that is not read inside a ritual is a dashboard nobody reads.** Before
building, name the moment:

- **Daily Gemba** — the shop-floor walk, the single largest consumer of what OD builds.
  It needs current numbers at the line, not a report assembled afterwards. Most use cases
  that record a utilization rate are used daily (re-count on the list).
- **Shift checks** — recorded in plants' own standard procedures: *"our shift supervisors
  check the OEE four times per shift and talk to the operators if we are not meeting the
  goal"*, *"our shift supervisors check the line speeds twice per shift"*. The asset
  either supports or replaces a defined standard procedure — find out which.
- **Escalation** — Andon signalling is two-step by design: the first signal requests help
  without stopping the line, the second stops it if unresolved, with defined tiers and a
  time-boxed response per tier. **Every event is logged rather than only displayed** — the
  log is what makes the improvement analysis possible at all. An Andon asset that only
  displays is half an asset.

## Where it will live

**Grafana** is where most of what the function builds is actually seen. Once this skill has
named the ritual, the decision and chosen "Dashboard," the actual JSON build is
`build-grafana-ops-dashboard`'s job — its schema interview, archetype choice and tier
picking take over from here. Grafana has no export worth relying on: if dashboard state must appear in a report or review, use the screenshot
automation in `_apps/`.

**Power BI / OESL Dashboards** carry the Scorecard and the two OD reports — that is the
steering layer, not the shop-floor layer. Do not build a line-side asset there.

**Layer:** Grafana is a local instance per plant; Databricks and the Azure Storage Account are the global platform
(`od-context`). A line-side dashboard belongs on the local instance, a cross-plant question does not.

## What the plants already have

Before designing, read the baseline and the catalogue. **Most dashboards exist in one plant only,
and titles that recur across plants are shared in name but, for Andon, Alert and Operations, not in
content.** The local Grafana mostly reads a PostgreSQL-type `telemetry` source, a few plants read
InfluxDB, and signals are mostly bound by literal UUID. Those are patterns, not counts; measure
them on the current export (`references/dashboard-estate-baseline.md`); the specs they come from
are drafts, unreviewed. Bind new panels through a variable, not a literal UUID, and put shift windows and targets in
configuration.

## Lane 1a self-service mode

In the new state a plant runs a **catalogued** use case itself (Lane 1a): the key user applies the
standard template or dashboard; OD supplies the catalog entry, the template and the guardrails
(`catalog-usecase`). In that mode this skill is used by the key user, not by OD:

1. Start from the catalog entry's template (`catalog-usecase`, `od-template-resolution`), never from a blank
   dashboard or an ad-hoc copy.
2. Apply it to this plant's signals; anything the template does not cover is a deviation, not a local
   extension: stop and route it (a recurring need is Lane 2).
3. Pass the guardrails (`catalog-usecase`, `references/technical-guardrails.md`) and its go-live check;
   passing the checklist is the approval gate.
4. The plant confirms adoption (`od-handover-and-adoption`).

The department's DATATRON dashboard package `ops-grafana-dashboards` (master) is transcribed in
[`references/ops-grafana-dashboards.md`](references/ops-grafana-dashboards.md): the four dashboard families and the
L1 to L3 drill-down, the telemetry and ConfigRepo schema, value extraction and `is_delta`, the two time-filter
dialects, the cascading variable chain, reusable panel recipes (machine state, state durations per shift, downtime with
flicker protection, cycle count from a sawtooth counter, SPC, andon board), ECharts conventions, layout and naming,
**datapoint enablement** (the "UUIDs to enable" list) and the equipment context (KKA, press centres, utilities). Use it
for any DATATRON dashboard in Lane 1a, 1b4 and Lane 2; the extension skills `ops-dashboard-datatron` and
`build-grafana-ops-dashboard` hold the deeper builder. A value the machine does not deliver directly is derived first
as a calculated datapoint (`od-node-red-flow-builder`, rule engine).

## Procedure

1. Confirm data availability and fitness → `od-data-availability-check`.
2. Check the reference library first — take a proven entry rather than building
   → `od-use-case-standardization`.
3. Name the **ritual**, the **decision** and the **action owner** the asset supports. Missing any of them, it is a
   "dashboard without an action owner": do not build it (five smell checks in
   [`process-chain-practice.md`](references/process-chain-practice.md)).
4. Choose the asset type from the table above; justify it if it is a dashboard by default
   → `references/asset-type-and-tier.md`.
5. Build to the standard layout. Every figure traces to a nameable source. If the asset is
   a dashboard, hand the ritual, the tier and the data model to `build-grafana-ops-dashboard`
   rather than hand-building panels here.
6. **Validate before calling it built** — `references/lifecycle-and-validation.md`'s
   checklist. Rendering is not the same claim as correct. **Reconcile with the paper record** for the same period (production
   and engineering deep dives, differences explained) and name who stops the paper process.
7. **Deliver it and explain it to the requester.** Delivery without explanation is the
   most common route to a `NEVER` utilization row.
8. Record on the use case: output asset, business process, **utilization expectation**,
   named plant owner, data path → `od-handover-and-adoption`. Fill
   [`assets/asset-build-protocol.md`](assets/asset-build-protocol.md) as the work happens —
   it is what `od-acceptance-test` and `od-handover-and-adoption` both read next.
9. Review utilization monthly; low utilization means rework or retire.

## When not to build

- The insight is a one-off with no recurring value → deliver the answer, close it as
  ad-hoc, **do not industrialize**.
- An asset for this capability already exists at another plant → adopt it.
- The data gap is real → route it, do not build on a proxy.
- The smell checks in step 3 fail → a dashboard without an action owner.

## Do not

- Do not present unvalidated insight as fact.
- Do not state a figure without a nameable source (`od-context` rule 4).
- Do not publish an asset externally without the responsible human; an agent never marks an asset accepted before the paper reconciliation is signed.
- Do not add a tool to build it. The strategy is a deliberately small operational footprint.

**Open points:** none recorded; chain detail (handoff contract, generative-AI process, paper reconciliation, sprint practice, agent notes) is in `references/process-chain-practice.md`.
