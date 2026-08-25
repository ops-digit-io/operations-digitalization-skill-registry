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
  shows **€2,384,217 tracked**. Only 19 rows, **€653,820**, have passed the SPRINT review.
  A single "Savings" stat tile that shows the first number is wrong by the department's own
  standard. Split the tile, or label it. See `od-benefit-calculation`.
- **Absence is not a zero.** 474 of 553 saving rows carry no reliability and 362 of 650 use
  cases carry `UNKNOWN` priority. `COALESCE(x, 0)` on those columns turns an honest gap into
  a false floor. Filter to rows that carry a value and show the coverage denominator
  alongside, or bucket `UNKNOWN` as its own visible category.

## Grafana's place in the OD landscape

Grafana is where **most of what the function builds is actually seen** — 173 of the 202 use
cases that record an output asset are dashboards. Two consequences:

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
  pipeline → MDL before promising a panel. A Grafana panel over a signal that is not
  standardized is a per-plant transformation buried in a query, and that is how cross-plant
  comparability is lost.
- **`od-analytics-asset-build`** — name the **ritual** the dashboard is read inside (daily
  Gemba, shift check, Andon escalation) before choosing panels. A dashboard that is not read
  inside a ritual is a dashboard nobody reads: 8 of the use cases that record a utilization
  rate are recorded as `NEVER`.

That check also decides whether a dashboard is the right asset at all. Of the recorded
output assets, 173 are dashboards against 12 reports, 11 apps and 5 analytics workflows —
the dashboard is the default, and the default is worth questioning.

## Timeseries archetype ↔ the OESL signal model

The skill's **timeseries archetype** (UUID-keyed long-format telemetry) is the shape OESL
shop-floor data already arrives in. The `PLCPacket` record carried over MQTT is
UUID-keyed, with a `sys_time` epoch and a `oneof` measured value —
see `od-node-red-flow-builder` for the full schema and the UUID→label lookup. When you
pick the timeseries patterns, that is the model you are matching, and the label dimension
comes from the IIoT edge platform's data-point config, not from the payload.

## After building

Run `od-handover-and-adoption`. A Grafana dashboard is handed over when the plant can
answer, without the builder: what decision it supports, where its data comes from and what
breaks it, and who owns it now. Record the output asset, the business process, the
utilization expectation and the named plant owner on the use-case record.

Publishing to a shared Grafana instance is human-approved.
