---
type: Skill Reference
title: Retro inputs
description: Where each of the three retro inputs (incidents, metrics, ODEC and COP feedback) is read from, which usable signals the sources already carry, and the limits of each; open it when preparing a monthly retro.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Retro inputs

The operating rhythm names the three inputs: **incidents, metrics, ODEC/COP feedback**
(`00-core/06-operating-rhythm.md`). This page says where to read each one, what a usable item looks like, and what the
sources do not give.

## 1. Metrics

Read with `od-scorecard-reporting`; do not re-derive. The retro uses the table of metrics with their read date and the
intervention thresholds from `07-metrics.md`.

| Signal | Source | Retro use |
|---|---|---|
| Integrated use cases vs target-to-date | Digitalization Scorecard, Digital Use Cases | A month "below 12" (red bar) on the Use Case Integration report is a threshold item |
| Integrated equipment vs target-to-date | Digitalization Scorecard, Equipment Integration | A month "below 25" is a threshold item |
| Readiness matrix, "not available" at a strategic plant | Scorecard readiness matrix | Threshold item (quarterly metric: read it in the quarter-end retro) |
| Share of low-utilization use cases rising | Scorecard, Digital Use Case Utilization | Threshold item (adoption) |
| Value delivery cycle | not captured in any system today | Not a signal; do not report |

Values were captured 2026-08-10 and drift: refetch before use. Illustration of the shape (not a decision taken): the
Scorecard then showed integrated use cases at 101 against a target of 153 for the year while equipment integration was at
338 against 331 (`07-metrics.md`). A retro reading that would list "use-case integration is behind and equipment is ahead"
as two items, then choose the one OD can change.

## 2. ODEC and COP feedback

Read from the round's own output: ODEC produces "central strategy updates; roadmaps, rollouts and workshops; priorities
and deadlines", COP produces "datamodel / connector updates; rollout guidance; technical Cyber Security aspects". The
recurring content shape of the rounds (regional breakout, not a blended total) is in `od-scorecard-reporting`
(`references/rounds-and-escalation.md`). Items that were *carried forward* from one round to the next are the ones to read
first: the escalation window is one round, so a carried item is a repeated item.

The ODEC fact slides in the vault (`ODEC Facts`, AI-extracted staging, not human-reviewed) show what the rounds have
tracked over time (savings target vs actual, machines integrated, connectivity-roadmap eCR status, training sessions and
participants, use-case upvoting). They are raw material for finding a pattern in previous months; open the cited archive
slide before treating any line as evidence.

## 3. Incidents

The sources name no incident register. What exists, and its limit:

| Candidate source | What it gives | Limit |
|---|---|---|
| Blocker Register (work vault, `Graph/Registers`) | Every recorded blocker text from the use-case list, by keyword theme, plant and template. Export of 2026-08-21: 83 blocker texts on 68 use cases at 18 plants; largest themes: use case details and evaluation missing (29 texts), PLC access and PLC program (24), edge device and hardware (17), connectivity concept and connector reuse (15) | Themes are keyword-inferred; the export is a snapshot, not a stream |
| Use-case change logs (work vault, `Graph/Registers`) | Every dated status change and text revision, per year (2026: 390 changes at the time of the hub note) | Shows movement, not cause |
| `12-portfolio.md` blocking points (owner, class) | Why value is not flowing, per undertaking | Table is a template; filled from the Scorecard and use-case library |
| Support tickets | Named as an early indicator in `09-risks.md` | No source system named: `⟨to confirm⟩` |

Rule from `od-context`: version history carries text the current record does not, so an "incident" may be visible only in
the change log.

## 4. What a usable item looks like

| Field | Example of the shape |
|---|---|
| What happened | One sentence, observable |
| Evidence | Source and date: a metric with its read date, a register line, a round output |
| Input | metric / incident / ODEC-COP feedback |
| Changeable by OD? | yes / no (if no: escalation item) |
| First seen | month; used by the "recurred" rule |

## 5. Not available in the sources

Retro participants and agenda (excluded by design), the decider role, a record location, a named incident register,
and any lane-level lead times (all four `⟨to confirm⟩`, so "overdue" cannot be judged).
