---
type: Skill Reference
title: Freshness
description: The cadence of each source, and the rule that an analysis cannot be fresher than the slowest pipeline feeding it.
resource: ../SKILL.md
status: stable
tags: [data-availability, freshness, cadence]
---

# Freshness

**Check the cadence before the query, not after.** An analysis whose conclusion depends on
data being fresher than its pipeline delivers is not supportable, and finding that out at
delivery costs the whole analysis.

| Source | Cadence | What it can and cannot support |
|---|---|---|
| Machine signals at the edge | near real-time | A shift-level decision, an alert, a live line view |
| Databricks / Azure Storage offload | per offload | Yesterday and before. Not "what is happening now" |
| MSB exchange | event-driven | Arrives when something happens, so silence is ambiguous |
| Digitalization Scorecard | monthly | A trend across months. Never a question about this week |
| Machine List | edited by hand | As current as the last person to touch it — `integration_date` is only partly populated (measure it live) |

## The rule

An analysis is as fresh as its **slowest** input. Joining a near-real-time signal to a monthly
scorecard produces a monthly answer wearing a real-time timestamp, which is worse than a
monthly answer, because the timestamp invites a decision the data cannot carry.

Ask it as a question about the moment of use, the same way `funnel-requirements` does:
**when will somebody look at this, and what will they do next?** A shift leader deciding at
07:00 what the incoming shift should watch needs last night's data by 07:00. A monthly
steering review does not. Most requests that arrive asking for "real time" mean "before my
next meeting", and the two have entirely different costs.

## Depth, which is the other half

Freshness is about the newest row; **history is about the oldest**, and it is the one nobody
asks about until the model will not train. `integration_date` says when a machine started
producing, and a machine integrated in March has no data for February — no pipeline can
recover it. Before promising a year-on-year comparison or anything that learns from history,
check the integration date of every machine in scope, not just one.

A signal renamed midway is the same problem in disguise: the history exists but sits under two
names, and a query for the current one silently returns a short series. That is
`mi-signals`'s many names for a much smaller set of concepts, arriving
as an analytical defect.
