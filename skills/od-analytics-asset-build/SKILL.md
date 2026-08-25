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
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-analytics-asset-build
  tier: practice
  lane: [analytical-support-service, use-case-support-service]
  owner_role: Digital-Business-Value-Engineer (DBVE)
  authority_level: draft/author the asset; publishing externally is human-approved
  status: stable
  last_verified: 2026-08-10
  requires: [od-context]
  composes: [od-data-availability-check, od-handover-and-adoption, od-use-case-standardization]
  derived_from:
    - ops-knowledge-graph/_knowledge/10-Department/Operating model.md
    - ops-knowledge-graph/_knowledge/10-Department/Rituals.md
    - ops-knowledge-graph/_knowledge/20-Done/Grafana dashboard screenshot automation.md
    - ops-knowledge-graph/.../20-lanes/analytical-support-service/{playbook,skills}.md
---

# Analytics asset build

Read `od-context` first. Run `od-data-availability-check` before building anything.

## What this function actually produces

Of the 202 use cases that record an output asset: **173 dashboards**, 12 reports,
11 apps, 5 analytics workflows, 1 agent. The dashboard is the default output, and the
default is worth questioning rather than inherited.

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
  It needs current numbers at the line, not a report assembled afterwards. 125 of the 202
  use cases recording a utilization rate are used daily.
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

**Grafana** is where most of what the function builds is actually seen. It has no export
of its own worth relying on, which is why capturing dashboard state was automated
separately (the dashboard-screenshot automation in `_apps/`). Plan for that: if the state
of your dashboard needs to appear in a report or a review, it goes through the screenshot
route, not through a Grafana export.

**Power BI / OESL Dashboards** carry the Scorecard and the two OD reports — that is the
steering layer, not the shop-floor layer. Do not build a line-side asset there.

## Procedure

1. Confirm data availability and fitness → `od-data-availability-check`.
2. Check the reference library first — take a proven entry rather than building
   → `od-use-case-standardization`.
3. Name the **ritual** and the **decision** the asset supports.
4. Choose the asset type from the table above; justify it if it is a dashboard by default.
5. Build to the standard layout. Every figure traces to a nameable source.
6. **Deliver it and explain it to the requester.** Delivery without explanation is the
   most common route to a `NEVER` utilization row.
7. Record on the use case: output asset, business process, **utilization expectation**,
   named plant owner, data path → `od-handover-and-adoption`.
8. Review utilization monthly; low utilization means rework or retire.

## When not to build

- The insight is a one-off with no recurring value → deliver the answer, close it as
  ad-hoc, **do not industrialize**.
- An asset for this capability already exists at another plant → adopt it.
- The data gap is real → route it, do not build on a proxy.

## Do not

- Do not present unvalidated insight as fact.
- Do not state a figure without a nameable source.
- Do not publish an asset externally without the responsible human.
- Do not add a tool to build it. The strategy is a deliberately small operational
  footprint; broad tool proliferation is an explicit non-bet.
