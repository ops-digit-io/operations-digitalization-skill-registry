---
type: Skill Asset
title: Dashboard requirements template
description: Template for a dashboard-level requirements document and its summary, written from an existing or planned dashboard, using the observed, issue and open markers and the common requirements checklist. Fields in angle brackets; illustrative only.
resource: ../SKILL.md
status: draft
tags: [analytical-support-service, practice, dashboard, template]
---
# Dashboard requirements template

Method and rules: `../references/dashboard-spec-and-change-report-patterns.md`. Do not paste user ids, host names or addresses.
Markers: **[observed]** visible in the screenshot, **[issue]** deviation to fix, **[open]** needs a decision by the process owner.

## Requirements specification: <system or area>

| | |
|---|---|
| Location (instance) | <plant / Grafana instance> |
| Dashboards | <title (uid)>, <title (uid)>, ... |
| Created | <dates> |
| Sources | Screenshot run <id>, time range <range>, first screen only: <yes/no>; JSON run <id> (all panels, signals, thresholds, queries) |
| Status | <Derived from the existing implementation (reverse-engineered) / Planned> |
| Owner role | <role> |

### 1 Purpose and scope

| Level | Reader (role) | Question it answers |
|---|---|---|
| <1 Overview> | <shift, operators> | <is it running, are values fine, any fault> |
| <2 Process detail> | <process engineering> | <which subsystem causes the deviation> |
| <3 Maintenance and diagnostics> | <maintenance> | <condition, wear, operating hours> |

Out of scope: <write-back to the machine / alarm notification / ...>

### 2 Common requirements

| ID | Requirement | Status marker |
|---|---|---|
| G-01 | Data from <table>; each signal addressed by <identifier>; data source input <role name> | |
| G-02 | Identifiers in hidden variables or one central place, not literals in queries | |
| G-03 | Stat tiles show the latest value in the range; trends aggregate with a bucket variable | |
| G-04 | Scaling applied in the query and written in the panel description: <signal, factor, unit> | |
| G-05 | Every physical value has a unit from the unit list | |
| G-06 | Default time range <relative range>; refresh <interval>, query cost noted if short | |
| G-07 | Status tiles use value mappings with text and colour; a good state is never red | |
| G-08 | Links between levels and drill-down links: <list> | |
| G-09 | One label language per dashboard: <language> | |
| G-10 | No-data text instead of 0 or an empty chart | |
| G-11 | Age of the newest data point visible; stale data (> <threshold>) marked | |

### 3 <Dashboard title>

- **What it shows [observed]:** <rows, tiles with unit and colour, charts and what they plot>
- **Requirements:** <ID: requirement> ...
- **Signals:** <signal name | address | scaling | unit | delivers data yes/no>
- **Issues [issue]:** <...>
- **Decisions [open]:** <...>

(repeat per dashboard)

## Summary: <system or area>

### <Dashboard title>

**Issue solved:** <situation without it, in operational terms: who has to go where, what is noticed too late>

**Requirements:** <one paragraph: what the screen must give, limits, links, refresh>

**Signals:**
- <signal> (<address>, <scaling>, <unit>)
