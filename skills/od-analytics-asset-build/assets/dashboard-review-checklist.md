---
type: Skill Asset
title: Dashboard review checklist
description: A checklist a plant key user ticks before a Grafana dashboard is called built - ritual, family, signal binding, authoring rules with the estate's violation counts, template placement and handover - using the proposals of the dashboard specs as the yardstick.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [analytical-support-service, practice, dashboard]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Dashboard review checklist

Use it twice: at design (sections A to C) and before delivery (all sections). It adds the
estate-specific checks to the general validation list in
[`../references/lifecycle-and-validation.md`](../references/lifecycle-and-validation.md); it does not
replace it. The yardstick is the authoring standard **proposed** in `Dashboard Exports/specs`
(SPEC-02, SPEC-03, SPEC-04; drafts of 2026-11-03, not reviewed by a human). A rule here is a
proposal until the owner accepts it; the "estate today" column is a count from the exports
(2026-11-03) and tells you how normal a violation is, not that it is allowed.

Dashboard: ⟨name⟩  Plant: ⟨⟩  Folder: ⟨⟩  Grafana version: ⟨⟩  Reviewer (role): ⟨⟩  Date: ⟨⟩

## A. Purpose and ritual

| # | Check | Estate today | Done |
|---|---|---|---|
| A1 | The ritual that reads it is named (daily Gemba, shift check, escalation, weekly review) and the decision it supports is written in the description | description on 128 of 1,010 dashboards | [ ] |
| A2 | The asset type is right (a dashboard that nobody walks away from to act is a report) | - | [ ] |
| A3 | It fits one screen for its ritual; above 40 panels it is split into linked levels | 98 dashboards above 40 panels; median 10 | [ ] |
| A4 | A named plant owner (role) is in the description | not measured | [ ] |

## B. Family and reuse

| # | Check | Done |
|---|---|---|
| B1 | The family was looked up in `references/dashboard-families-catalogue.md`; an existing one at another plant was considered for adoption | [ ] |
| B2 | If the title is one of the 17 cross-plant titles, the class is known (A central, B template, C same name different content) and the central master was used where one exists | [ ] |
| B3 | Where the dashboard repeats per machine or oven, a variable-driven version was built, not N copies (the Carei ovens: 19 copies against 1 dynamic dashboard) | [ ] |
| B4 | Nothing was copied from `dev`, `ZZ - ...`, `Trashbin`, `Testcenter` or a title with `(old)`, `DEV`, `Copy of` | [ ] |

## C. Signals and data (SPEC-02)

| # | Check | Estate today | Done |
|---|---|---|---|
| C1 | Every signal has a row in the signal binding sheet (`od-signal-standardization`, `assets/signal-binding-sheet.md`): canonical name, value type, unit, scale, collection method | no record exists in the registry for unit/scale | [ ] |
| C2 | No signal is bound by a literal UUID typed into SQL; binding is by variable or lookup on the registry (D-02) | 16,452 literal predicates in 498 dashboards | [ ] |
| C3 | No empty binding `uuid = ''` (D-03) | 450 in 49 dashboards | [ ] |
| C4 | Value type is not guessed with a `COALESCE` chain; the signal's actual type is stated (D-04) | 8,463 queries | [ ] |
| C5 | The `is_delta` filter is used as the written definition says, in one spelling, exposed as the `$delta` variable (D-05) | eight spellings, 13,819 queries | [ ] |
| C6 | Queries follow the time picker (`$__timeFilter`, `$__timeFrom`, `$__timeTo`, `$__interval`); a fixed `time_bucket` or a `now()` literal carries a note (D-06) | 670 queries in 67 dashboards ignore the picker | [ ] |
| C7 | Shift windows, hourly targets and labels per UUID are not typed in SQL (patterns Q4, Q8 in `dashboard-json-sample-2026-11.md`) | seen in Karben, Vac | [ ] |
| C8 | The data source name is the role name agreed for the plant, and the dashboard imports without re-binding (D-07) | `TelemetryPLC` 398 inputs, `Telemetry` 110, `Quackito`, 129 dashboards name none | [ ] |
| C9 | If the plant is on InfluxDB (Changshu, Sun Prairie, Caluire, Changchun), the `CT/...` topic is confirmed with the flow owner and not renamed | 136 inputs | [ ] |
| C10 | The signals were confirmed on live data on the date: ⟨date⟩ by ⟨role⟩ (`od-data-availability-check`) | - | [ ] |

## D. Authoring rules (SPEC-03, numbered so a lint can report them)

| # | Rule | Estate today | Done |
|---|---|---|---|
| D1 (S-01) | Title `<Area or line> - <What it shows>`; no Draft, Copy of, Test, New dashboard in a production title | 32 titles | [ ] |
| D2 (S-02/E-04) | Status is a tag (`production`, `test`, `wip`, `deprecated`), not a folder such as `ZZ - WIP` | 162 dashboards in lifecycle folders | [ ] |
| D3 (S-03) | Tags: status, template (one of 11), plant | no tag set identifies a template | [ ] |
| D4 (S-06) | Every panel has a title (a stat panel without one sits in a titled row) | 4,494 untitled panels | [ ] |
| D5 (S-07) | No panel without a query or content | 2,231 targets in 181 dashboards | [ ] |
| D6 (S-08) | No legacy panel types (`graph`, `table-old`) | 61 panels | [ ] |
| D7 (S-09) | Core panel types by default; a plugin panel (ECharts) has a reason and is on the approved list | 1,241 ECharts panels in 273 dashboards | [ ] |
| D8 (S-10) | Every numeric panel has a Grafana unit, never free text (`[m]`, `suffix:s`); one unit per quantity | 10,920 panels without unit | [ ] |
| D9 (S-12) | Limits are threshold steps with a documented colour meaning; "no fault" is green | 2,989 of 9,573 stat panels with thresholds | [ ] |
| D10 (S-13) | Coded states use value mappings with readable text | 2,378 panels use mappings | [ ] |
| D11 (S-14) | Live status board: 5 min range and 5-30 s refresh; trend board: 6-24 h and refresh no faster than 1 min; shift reports use shift-aligned ranges; 5 s refresh has a note on query cost | 101 dashboards at 5 s refresh | [ ] |
| D12 (S-16) | Variable names lower case: `datasource`, `datatron`, `device`, `machine`, `delta` | `machine` and `Machine` both used | [ ] |
| D13 (S-18) | Description: purpose (the "issue solved"), audience, data sources, link to the family or spec note | 128 of 1,010 | [ ] |
| D14 (S-19) | Calculated KPIs and thresholds carry a panel description with the definition | 1,736 of 17,961 panels | [ ] |
| D15 | The default time range is relative, not an absolute date saved by accident | seen on three of 20 sampled dashboards (Changchun, Testcenter, Vac); Qingdao "Availability per Machine" opens on 2023 | [ ] |

## E. Placement and records

| # | Check | Done |
|---|---|---|
| E1 | The template is placed with the rules R1 to R13 (`references/capability-templates-and-placement.md`) and written on the use case | [ ] |
| E2 | The use case records output asset, business process, utilization expectation and named plant owner | [ ] |
| E3 | If the dashboard belongs to a case group, the group is known; delivered without a saving is noted | [ ] |

## F. Delivery

| # | Check | Done |
|---|---|---|
| F1 | A screenshot was taken through the screenshot automation (not a Grafana export) if the state must appear in a report | [ ] |
| F2 | Explained to the requester in person; training date ⟨⟩ | [ ] |
| F3 | Published to a shared Grafana only with human approval: ⟨role, date⟩ | [ ] |
| F4 | A review date for utilization is in the calendar (monthly) | [ ] |

## Result

Items the reviewer treats as blocking (suggestion: C2 to C6 and C10 for a production dashboard, D4 and D5 for any status; the reviewer confirms): ⟨⟩
Accepted deviations (with the reason and the approver): ⟨⟩
