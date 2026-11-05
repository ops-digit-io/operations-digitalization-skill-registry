---
type: Skill Asset
title: Signal binding sheet
description: One row per signal that a dashboard or flow will read - the record that the Grafana exports show is missing today (unit, scale, value type, delta flag, consumers) - to be filled by the key user before a signal is bound.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, technical, signals]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Signal binding sheet

**Why it exists.** In the 1,010 Grafana dashboards of the export a signal is bound by a
literal UUID typed into SQL (16,452 predicates in 498 dashboards, 6,590 distinct UUIDs), and
the unit, scale and value type are decided per panel (`COALESCE(value_double, value_integer,
value_bool::integer)` in 8,463 queries; a unit on only 7,041 of 17,961 panels). The registry knows
datatron, device and device type per UUID, but no plant, machine, unit or scale (SPEC-02, read
2026-11-05). This sheet is the missing record, per signal, written down once.

Fill one row per signal **before** a flow or dashboard binds it. Keep the sheet next to the
signal analysis report (`signal-analysis-report.md`); it is the form behind its mapping table.

## A. Header

| Item | Entry |
|---|---|
| Machine (EQ id or Machine List name) | ⟨⟩ |
| Plant / edge device / device name | ⟨⟩ |
| Capability template of the use case (11) | ⟨⟩ |
| Context situation (full context / tag export only / handbook only / proven instance) | ⟨⟩ |
| Filled by (role) and date | ⟨⟩ |

## B. The rows

| # | Canonical name | Local name (alias, original language) | UUID | Value type actually filled (`valueDouble/Integer/Bool/String`) | Unit | Scale (e.g. divide by 10) | Setpoint or actual | Collection (transition / sample, interval) | `is_delta` meaning | Used by (flow, dashboard, use case) | Verified on live data (date, by) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |

Column notes (rules, each from a count in the exports):

- **Value type actually filled.** A query that coalesces three types does not know which one
  a signal fills. Write the one that carries data; the flow's `oneof` rule keeps exactly one.
- **Unit and scale.** Raw PLC scaling lives in the panel today (a Hannover pulp-mixer
  requirement lists a signal as "DB 35.D_56, divided by 10, degrees Celsius"). Write it here;
  do not repeat it per panel.
- **`is_delta`.** The dashboards filter on it in 13,819 queries in eight spellings and no
  note explains it (SPEC-02 open question). ⟨Definition - data team / IIAE.⟩ Until it is
  written, record which value the consumers use.
- **Setpoint or actual.** Two signals, two rows; `_sv`, `SV`, `Setpoint`, `Soll` all occur.
- **Local name.** Keep the original language; the sheet is where the alias lives.
- **Used by.** This is what answers "which dashboards use machine X", which cannot be listed
  today without parsing SQL (SPEC-02 P3).

## C. Not signals - configuration the dashboards currently carry

| Item | Value | Where it lives instead |
|---|---|---|
| Shift boundaries (the OEE dashboards pass four shift start/end labels as signals) | ⟨⟩ | flow config or plant calendar, one place |
| Ideal cycle time / standard time (dashboards use a `CycleTimeSetting` variable in 24 OEE dashboards) | ⟨⟩ | stored with the machine or product, agreed with Plant ME |
| Micro-stop threshold | ⟨⟩ | same |
| Reason codes for downtime (operator-entered) | ⟨⟩ | a record schema, not a signal (`od-requirements-breakdown`) |

## D. Checks before the row is used

- [ ] The canonical name is in `signal-catalogue.md` or the deviation is written in the report.
- [ ] The UUID exists on the edge platform's data-point configuration (not an empty `uuid = ''`
  template leftover - 450 such predicates in 49 dashboards).
- [ ] Unit and scale are stated, not "see panel".
- [ ] A second plant's instance of the same capability could read this row without asking.
- [ ] The consumers listed here are the only ones; any other binding is reported back.

## E. How the sheet feeds the next steps

`od-node-red-flow-builder` takes the UUID, type and limit rows into its config contract
(`assets/flow-config-contract.md`); `od-analytics-asset-build` takes the same rows into the
dashboard review (`assets/dashboard-review-checklist.md`); `od-acceptance-test` checks the
"verified on live data" column.
