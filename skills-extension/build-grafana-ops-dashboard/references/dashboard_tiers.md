---
type: Skill Reference
title: Dashboard tiers
description: Manager, analyst and operations dashboards are three different products; the design rules and panel inventory for each.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [grafana, design]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Dashboard tiers — design rules and panel inventories

The single biggest design decision when building an ops dashboard is **who is it for**. Three audiences, three different dashboards. Stuffing all three audiences into one dashboard produces a tool nobody uses well.

The examples below are for downtime, but the structure works identically for energy, throughput, quality, OEE, or any operations domain.

---

## Manager tier — fleet view

### Audience

Plant managers, OPEX leads, executives. Anyone who walks into a Monday standup needing answers in 30 seconds.

### Question being answered

"Where do I send my attention this week?"

### Design rules

- **Few panels** — 8 to 13 maximum. Each one earns its place by answering one decision.
- **No filters** beyond multi-tenant `$account`. Managers should not have to pick filter values to read their dashboard.
- **Fixed time window** baked into queries. Typical: last 7 days vs prior 7 days. Hide the time picker via `"timepicker": {"hidden": true}`.
- **Traffic-light thresholds** on stats and table cell backgrounds. Calibrate to actual fleet baseline.
- **Action-oriented framing.** Every panel answers one of:
  - "What got worse?" (week-over-week deltas)
  - "Who do I talk to?" (top-3 entities, top-3 categories)
  - "What's the ROI of fixing it?" (impact ranked)
  - "Is the data trustworthy?" (data-quality KPIs)
- **Refresh ≥ 5 minutes.** Manager dashboards aren't real-time.
- **Story panel** — single worst event or single biggest outlier. Managers respond to narratives.

### Example panel inventory (downtime domain)

| Row | Panel | Type | Width |
|---|---|---|---|
| 🎯 This Week at a Glance | Total downtime (h) | Stat with traffic-light | 4 |
|   | vs last week (Δ min) | Stat with traffic-light | 4 |
|   | Incidents | Stat | 4 |
|   | Incidents WoW (%) | Stat with traffic-light | 4 |
|   | MTTR (min) | Stat | 4 |
|   | Unassigned % | Stat with traffic-light | 4 |
| 🚨 Action Board | Entities ranked w/ deltas + top category | Table with cell coloring | 16 |
|   | Fleet share donut | ECharts donut | 8 |
| 📈 What Changed | Entity comparison: this vs last week | ECharts compare bars | 16 |
|   | Categories gaining ground (top 5) | Table with cell coloring | 8 |
| 💡 Where to invest | Daily trend (14d) | Time series | 12 |
|   | Top 5 category groups | Table with gradient gauge | 12 |
| 📰 Story of the week | Worst single event | Table | 24 |
| ℹ How to read this | Markdown text panel | Text | 24 |

### Hard rules

- No drill-downs. If a manager wants to investigate, link to the analyst dashboard.
- No event-level detail. Managers don't read individual rows.
- No live state. That's the operations tier.
- No exploration tools (filter-heavy panels). That's the analyst tier.

---

## Analyst tier — deep-dive view

### Audience

Continuous-improvement engineers, production planners, data analysts. Anyone investigating root causes or building improvement projects.

### Question being answered

"Why did this happen and what should we change?"

### Design rules

- **Many panels** (20–30+) organized into **collapsible rows**.
- **Full filter set:** time picker, multi-select dimensions, numeric thresholds.
- **Every variable defined must be used in every relevant panel.** Defining a variable and not wiring it is a bug.
- **Drill-down detail table** as the last panel — top-N by impact with all metadata.
- **Data quality panels** as a dedicated row — most analyst dashboards skip this and lose weeks chasing dirty data.
- **Annotations** for events overlaid on time series panels for correlation.
- **Refresh: 30s–1m**.

### Example panel inventory (downtime domain, full)

| Row | Panels |
|---|---|
| 🟦 Headline KPIs | Total / Count / MTTR / MTBF / P95 / Unassigned % / Auto-detected % |
| 📈 Trends over time | Stacked by category · Stacked by entity · Rolling 7d MTTR |
| 🎯 Pareto & ranking | ECharts Pareto · Entity ranking · Category hierarchy rollup |
| 🔍 Patterns | DOW × hour heatmap · Duration histogram · Severity mix |
| 🧹 Data quality | Unassigned · Auto-closed · Auto-vs-manual donut · Reporter leaderboard |
| 📋 Planned vs unplanned | Comparison stat · Schedule deviation per entity |
| 🔬 Drill-down | Top 500 by impact with all metadata |

### Variables (relational archetype)

```
$account            (query, single, no 'all')
$<entity>           (query, multi, includeAll)     — e.g. $machine, $line, $department
$<category>         (query, multi, includeAll)     — e.g. $reason, $defect_type
$severity           (custom, single, with 'all' option)
$min_duration_min   (textbox, default 0)
$auto_detected      (custom, single: all=-1, manual=0, auto=1)
```

### Variables (timeseries archetype)

```
$account            (query, single)
$signal_a           (query, single, returns UUID via :raw)
$signal_b           (query, single, returns UUID via :raw)
... one per signal the dashboard tracks ...
$bucket             (interval: 1m, 5m, 15m, 1h)
```

---

## Operations tier — live shop-floor view

### Audience

Shift leads, operators, maintenance technicians on call. Often viewed on a wall-mounted screen in the production area.

### Question being answered

"What's happening right now?"

### Design rules

- **Few panels, large fonts, high contrast.** Optimized for being read across a room.
- **Short refresh** (15s–60s).
- **Single-shift or single-day window.** Not historical.
- **Live state focus:** open events, currently-active machines, alarms, cycle time vs target.
- **Color = status, not analytical encoding.** Red = down. Green = running. No gradients.
- **Sound/visual alerts** for new critical events (Grafana alert rules + dashboard alert annotations).

### Example panel inventory

| Row | Panel | Type |
|---|---|---|
| Top strip | Currently active count · Open critical · Last-shift KPI | Stats, large |
| Status grid | One stat per entity: green/yellow/red + current state | Stat repeat / state-timeline |
| Live events | Open events with elapsed time | Table with auto-sort by elapsed |
| Last hour activity | Events per entity in last 60 min | Bar chart |
| Recent events | Last 10 events (open or closed) | Table |

### Hard rules

- No filters. The dashboard shows the whole shop floor, not a slice.
- No deep history. If they need it, they switch to analyst dashboard.
- No data quality panels. Operators don't fix data quality.
- Every panel works at a glance. If it needs explanation, it's wrong for this tier.

---

## Cross-tier recommendations

### Link between tiers

Add dashboard links in each dashboard's settings:

- Manager → Analyst (filtered to one entity when clicking a row)
- Analyst → Operations (filtered to currently-relevant entities)
- Operations → Analyst (for post-shift review)

This is configured via the panel's "data links" feature, generating URLs like:

```
/d/<analyst-uid>?var-machine=${__data.fields.machine_id}
```

### Naming convention

- `<Domain> — Manager View (Fleet)`
- `<Domain> — Analyst View (Historical)`
- `<Domain> — Live (Shop Floor)`

The audience tag in the title prevents confusion.

### Panel naming convention

For analyst dashboards with 20+ panels, panel titles need to be browsable. Apply this pattern to every panel:

```
[<Tier>]  <Domain>  —  <Question>
```

Examples:
- `[Analyst]  Downtime  —  Top reasons by machine`
- `[Analyst]  Downtime  —  MTTR rolling 7-day`
- `[Manager]  Downtime  —  Week vs prior week`
- `[Ops]  Line 3  —  Current state`

Reasoning:
- The tier prefix prevents a panel from a manager view ending up next to one from an analyst view in search results without context.
- The domain anchor lets engineers searching across folders find every panel related to one topic.
- The question phrasing (rather than metric phrasing) reads more naturally and forces clarity. "Top reasons by machine" makes its purpose obvious; "Pareto chart" doesn't.

The tier prefix can be dropped on operations dashboards if every panel is operations-tier — the redundant prefix wastes space on screens designed to be glanced at, not read.

### Folder organization

Group all three under a single Grafana folder named after the domain (e.g., `Downtime`, `Energy`, `Quality`). Subfolders by tier are unnecessary and add navigation overhead.

### Permissions

Manager dashboards typically have wider read access (executives, customers, partners) — but should be edit-restricted. Analyst dashboards need write access for the analyst team. Operations dashboards should be locked to view-only on the shop-floor screen account.

---

## Anti-patterns to refuse

- **One mega-dashboard.** "Just put it all in one dashboard" produces a 60-panel monstrosity that no audience uses well. Push back on this.
- **Filter-heavy manager view.** If the user wants filters on a manager view, they actually want an analyst view — clarify.
- **Live data on a manager view.** "Real-time" is an operations concern. Managers need yesterday's truth, not this minute's noise.
- **Metric-only operations view.** Operators need to see entity names (machine names, line names), not just KPI numbers. State + identity beats abstract numbers.
- **No data-quality panels on the analyst view.** Without these, dirty data silently corrupts every other panel and analysts spend weeks chasing phantom trends.
