---
type: Skill Guide
title: OD integration
description: "How the portable Grafana dashboard skill is used at OESL: which lane calls it, what a plant Grafana instance is for, and what stays out of it."
resource: SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [grafana, dashboards, portable]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Using this skill inside Operations Digitalization

`build-grafana-ops-dashboard` is **portable** — it is domain-generic and its body and
references are vendored unmodified. This file is the only OD-specific addition: it says
what changes when the dashboard being built is an OD deliverable.

Nothing here overrides the skill's own hard rules (Grafana time macros; PostgreSQL /
DuckDB portability). Those still win.

## Load `od-context` first

An OD dashboard inherits the department's honesty rules, and two of them constrain what a
panel may show:

- **Tracked is not proven.** A savings panel that sums the `UseCase SavingCalculation` rows
  shows the *tracked* total. Only the rows that have passed the SPRINT review are *proven*.
  A single "Savings" stat tile that shows the tracked number as if it were proven is wrong by the
  department's own standard. Read both totals live from the saving rows; quote neither here. Split the tile, or label it. See `od-benefit-calculation`.
- **Absence is not a zero.** Many saving rows carry no reliability and many use cases carry
  `UNKNOWN` priority (count the share on the live list). `COALESCE(x, 0)` on those columns turns an honest gap into
  a false floor. Filter to rows that carry a value and show the coverage denominator
  alongside, or bucket `UNKNOWN` as its own visible category.

## Grafana is local, per plant

**A Grafana instance belongs to one location.** It builds that plant's manufacturing
dashboards from that plant's data — it is a shop-floor tool, not a company-wide reporting
layer.

Two things follow, and both are easy to get wrong:

- **Do not point a plant's Grafana at the global data platform.** Global analytics live
  elsewhere; a local dashboard that queries a central lake inherits its latency, its cost
  model and its access story for no benefit, and stops working the moment the site link
  does. Keep the query local to the plant.
- **Do not build a cross-plant view here.** If a panel needs several sites at once, it is
  not a local manufacturing dashboard and this is the wrong instance to build it on. Raise it
  as a portfolio or reporting question instead.

⟨**To confirm:** the local datasource each plant's Grafana reads — engine, and whether it is
uniform across sites. That decides how literally the skill's PostgreSQL/DuckDB portability
rule applies here; until it is confirmed, keep the rule as written, since its whole purpose
is that the same dashboard JSON survives being moved between instances — which is exactly
what a per-plant Grafana estate needs.⟩

## Grafana's place in the OD landscape

Grafana is where **most of what the function builds is actually seen** — the dashboard is by far the
most common output asset recorded on use cases. Two consequences:

1. **Grafana is the shop-floor layer; Power BI is the steering layer.** The Digitalization
   Scorecard and the two OD reports (`OD-Report-Use_Case_Integration`,
   `OD-Report-Equipment_Integration`) live in Power BI and stay there. Do not rebuild a
   Scorecard panel in Grafana — it will drift from the authoritative figure.
2. **Grafana has no export worth relying on.** Capturing dashboard state for a review or a
   report goes through the dashboard-screenshot automation (`_apps/` in the knowledge
   graph), not a Grafana export. If the dashboard's numbers have to appear in an ODEC pack,
   plan that route in.

## Before building: two OD gates

- **`od-data-availability-check`** — walk machine → connector → integration concept →
  local datasource before promising a panel. A Grafana panel over a signal that is not
  standardized is a per-plant transformation buried in a query, and that is how cross-plant
  comparability is lost — the fact that the dashboard is local is not a licence to skip the
  standard.
- **`od-analytics-asset-build`** — name the **ritual** the dashboard is read inside (daily
  Gemba, shift check, Andon escalation) before choosing panels. A dashboard that is not read
  inside a ritual is a dashboard nobody reads: use cases whose utilization rate is recorded as
  `NEVER` are the symptom (count them on the live list).

That check also decides whether a dashboard is the right asset at all. Dashboards
dominate the recorded output assets over reports, apps and analytics workflows — the
dashboard is the default, and the default is worth questioning.

## Timeseries archetype ↔ the OESL signal model

The skill's **timeseries archetype** (UUID-keyed long-format telemetry) is the shape the
shop-floor data already arrives in. The `PLCPacket` record carried over MQTT is
UUID-keyed, with a `sys_time` epoch and a `oneof` measured value —
see `od-node-red-flow-builder` for the full schema and the UUID→label lookup. When you
pick the timeseries patterns, that is the model you are matching, and the label dimension
comes from the IIoT edge platform's data-point config, not from the payload.

## Lane 1a self-service

When a plant key user applies a catalogued dashboard template (Lane 1a), this skill is the engine and
`od-analytics-asset-build` (self-service mode) with `catalog-usecase`'s guardrails is the frame: start from the
catalog template, pass the go-live check, let the plant confirm adoption. The department names this
generic engine `build-grafana-ops-dashboard` under its naming convention.

## After building

Run `od-handover-and-adoption`. A Grafana dashboard is handed over when the plant can
answer, without the builder: what decision it supports, where its data comes from and what
breaks it, and who owns it now. Record the output asset, the business process, the
utilization expectation and the named plant owner on the use-case record.

Publishing to a shared Grafana instance is human-approved.
