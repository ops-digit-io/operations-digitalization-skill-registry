---
type: Skill Asset
title: Dashboard review checklist
description: A checklist a plant key user ticks before a Grafana dashboard is called built - ritual, family, signal binding, authoring rules with the estate's violation counts, template placement and handover - using the proposals of the dashboard specs as the yardstick. No estate counts; measure them on the current export.
resource: ../SKILL.md
status: draft
tags: [analytical-support-service, practice, dashboard]
---
# Dashboard review checklist

Use it twice: at design (sections A to C) and before delivery (all sections). It adds the
estate-specific checks to the general validation list in
[`../references/lifecycle-and-validation.md`](../references/lifecycle-and-validation.md); it does not
replace it. The yardstick is the authoring standard **proposed** in `Dashboard Exports/specs`
(SPEC-02, SPEC-03, SPEC-04; drafts of 2026-11-03, not reviewed by a human). A rule here is a
proposal until the owner accepts it; the "How to check" column says where to measure how common a
violation is on the current export - normal does not mean allowed.

Dashboard: ⟨name⟩  Plant: ⟨⟩  Folder: ⟨⟩  Grafana version: ⟨⟩  Reviewer (role): ⟨⟩  Date: ⟨⟩

## A. Purpose and ritual

| # | Check | How to check | Done |
|---|---|---|---|
| A1 | The ritual that reads it is named (daily Gemba, shift check, escalation, weekly review) and the decision it supports is written in the description | dashboard `description` field in the JSON | [ ] |
| A2 | The asset type is right (a dashboard that nobody walks away from to act is a report) | - | [ ] |
| A3 | It fits one screen for its ritual; above 40 panels it is split into linked levels | panel count in the inventory vs the 40-panel line | [ ] |
| A4 | A named plant owner (role) is in the description | owner role named in the description | [ ] |

## B. Family and reuse

| # | Check | Done |
|---|---|---|
| B1 | The family was looked up in `references/dashboard-families-catalogue.md`; an existing one at another plant was considered for adoption | [ ] |
| B2 | If the title is one of the cross-plant titles, the class is known (A central, B template, C same name different content) and the central master was used where one exists | [ ] |
| B3 | Where the dashboard repeats per machine or oven, a variable-driven version was built, not N copies (a per-oven copy family against one dynamic dashboard) | [ ] |
| B4 | Nothing was copied from `dev`, `ZZ - ...`, `Trashbin`, `Testcenter` or a title with `(old)`, `DEV`, `Copy of` | [ ] |

## C. Signals and data (SPEC-02)

| # | Check | How to check | Done |
|---|---|---|---|
| C1 | Every signal has a row in the signal binding sheet (`mi-signals`, `assets/signal-binding-sheet.md`): canonical name, value type, unit, scale, collection method | signal binding sheet filled; the registry holds no unit/scale | [ ] |
| C2 | No signal is bound by a literal UUID typed into SQL; binding is by variable or lookup on the registry (D-02) | grep `uuid = '` literals in the dashboard JSON | [ ] |
| C3 | No empty binding `uuid = ''` (D-03) | grep `uuid = ''` | [ ] |
| C4 | Value type is not guessed with a `COALESCE` chain; the signal's actual type is stated (D-04) | grep `COALESCE(value_double` | [ ] |
| C5 | The `is_delta` filter is used as the written definition says, in one spelling, exposed as the `$delta` variable (D-05) | grep `is_delta` spellings | [ ] |
| C6 | Queries follow the time picker (`$__timeFilter`, `$__timeFrom`, `$__timeTo`, `$__interval`); a fixed `time_bucket` or a `now()` literal carries a note (D-06) | grep `now()` / `CURRENT_DATE` / fixed `time_bucket` | [ ] |
| C7 | Shift windows, hourly targets and labels per UUID are not typed in SQL (patterns Q4, Q8 in `dashboard-json-sample.md`) | patterns Q4, Q8 | [ ] |
| C8 | The data source name is the role name agreed for the plant, and the dashboard imports without re-binding (D-07) | data source names in the inventory; dashboards naming none | [ ] |
| C9 | If the plant is on InfluxDB (see the baseline for which locations), the `CT/...` topic is confirmed with the flow owner and not renamed | InfluxDB inputs in the inventory | [ ] |
| C10 | The signals were confirmed on live data on the date: ⟨date⟩ by ⟨role⟩ (`mi-data-availability`) | - | [ ] |

## D. Authoring rules (SPEC-03, numbered so a lint can report them)

| # | Rule | How to check | Done |
|---|---|---|---|
| D1 (S-01) | Title `<Area or line> - <What it shows>`; no Draft, Copy of, Test, New dashboard in a production title | titles with draft/copy/test words | [ ] |
| D2 (S-02/E-04) | Status is a tag (`production`, `test`, `wip`, `deprecated`), not a folder such as `ZZ - WIP` | folder paths | [ ] |
| D3 (S-03) | Tags: status, template (one of 11), plant | tags in the JSON | [ ] |
| D4 (S-06) | Every panel has a title (a stat panel without one sits in a titled row) | panels without `title` | [ ] |
| D5 (S-07) | No panel without a query or content | targets with empty query text | [ ] |
| D6 (S-08) | No legacy panel types (`graph`, `table-old`) | panel type `graph` / `table-old` | [ ] |
| D7 (S-09) | Core panel types by default; a plugin panel (ECharts) has a reason and is on the approved list | panel type ECharts | [ ] |
| D8 (S-10) | Every numeric panel has a Grafana unit, never free text (`[m]`, `suffix:s`); one unit per quantity | panels without `fieldConfig.defaults.unit` | [ ] |
| D9 (S-12) | Limits are threshold steps with a documented colour meaning; "no fault" is green | threshold steps on stat panels | [ ] |
| D10 (S-13) | Coded states use value mappings with readable text | value mappings present | [ ] |
| D11 (S-14) | Live status board: 5 min range and 5-30 s refresh; trend board: 6-24 h and refresh no faster than 1 min; shift reports use shift-aligned ranges; 5 s refresh has a note on query cost | dashboards with refresh <= 5 s | [ ] |
| D12 (S-16) | Variable names lower case: `datasource`, `datatron`, `device`, `machine`, `delta` | variable name spellings | [ ] |
| D13 (S-18) | Description: purpose (the "issue solved"), audience, data sources, link to the family or spec note | dashboard `description` present | [ ] |
| D14 (S-19) | Calculated KPIs and thresholds carry a panel description with the definition | panel `description` present | [ ] |
| D15 | The default time range is relative, not an absolute date saved by accident | time range `from`/`to` that are absolute dates | [ ] |

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
