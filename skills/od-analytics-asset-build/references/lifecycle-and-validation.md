---
type: Skill Reference
title: Lifecycle and validation
description: The build lifecycle mapped onto this registry's own upstream and downstream skills, and the checklist that separates an asset that renders from one that is correct.
resource: ../SKILL.md
status: stable
tags: [analytical-support-service, use-case-support-service, lifecycle]
---
# Lifecycle and validation

## The lifecycle, and which skill owns which track

The Kimball Lifecycle (Kimball & Ross, *The Data Warehouse Toolkit*) runs requirements
gathering, then a **data track** and a **BI track** in parallel, then brings them back
together for deployment and maintenance. This registry already has a skill for every track —
this one's job is specifically the BI track, and naming that boundary is what stops the
asset-build step from quietly re-doing another skill's work:

| Kimball track | This registry's skill |
|---|---|
| Requirements | `od-use-case-definition` / `od-use-case-solution-evaluation` |
| Data track (source → target, fit for use) | `od-data-availability-check`, `od-signal-standardization` |
| **BI track — design the asset, then build it** | **this skill**, then `build-grafana-ops-dashboard` for the Grafana build itself |
| Deployment (communication, training, support) | `od-handover-and-adoption` |
| Maintenance and growth (usage monitoring, rework) | the monthly utilization review already named in `SKILL.md`'s procedure |

Deployment in the Kimball Lifecycle is explicitly a planned phase with its own pre-deployment
testing, documentation and training — not an afterthought once the build looks finished. That
is exactly why step 6 (validate) and step 7 (deliver and explain) are separate steps in this
skill's procedure, not one step: a validated asset that is handed over without explanation
fails at the Kimball-Lifecycle deployment gate, not at the build gate, and it shows up here
as a `NEVER` utilization row.

## Validate before calling it built

**Rendering and being correct are different claims.** An asset can produce a chart with no
errors and still be wrong — the query ran, the number traces to no real source, or it reads
a 2 instead of the 3 it should. Stephen Few's *Information Dashboard Design* names the
recurring failure modes of a BI-track output that technically works but still fails its
purpose; the checklist below is built from his list, translated into something to tick
before delivery:

- [ ] **Every figure traces to a nameable source** — the exact table, signal UUID or report
  row, not "the data platform" in general. An unnamed source is the single most common way
  a correct-looking number turns out to be wrong later.
- [ ] **Data fitness was confirmed, not assumed** — `od-data-availability-check`'s verdict
  for every signal the asset reads, checked again here if the asset was built weeks after
  that check ran.
- [ ] **The asset fits inside the moment it serves, not around it.** Few's own definition:
  consolidated on a single screen, monitored at a glance. A dashboard that requires
  scrolling or a second screen during the Daily Gemba walk has already failed the ritual
  test in `SKILL.md`'s "Design for the ritual" section, whatever its queries return.
- [ ] **Non-data pixels are reduced, data pixels are not drowned.** Few's two core moves:
  cut decoration that carries no information, then make the few numbers that matter stand
  out — a KPI tile next to six identically-styled ones that do not matter is the opposite
  of this.
- [ ] **The display medium fits the question.** Few's own list of common mistakes includes
  choosing a deficient measure or an inappropriate chart type for what is actually being
  asked — a trend question answered with a single stat tile, or a comparison question
  answered with a line chart, is a mismatch even when every number in it is right.
- [ ] **Context is supplied, not just the number.** A bare "42" with no target, trend or
  comparison is the same mistake Few flags as "inadequate context" — without it, nobody
  can tell whether 42 is good.
- [ ] **The asset was explained to the requester before being left alone with it.** Not a
  validation of the asset itself, but the step most responsible for a `NEVER` utilization
  row when skipped — see `SKILL.md`'s procedure.

An asset that passes every technical check above and is still never opened has not failed
validation — it has failed the ritual test earlier in `SKILL.md`. Re-check that first before
assuming the build itself needs rework.
