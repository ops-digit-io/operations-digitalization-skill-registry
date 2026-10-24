---
type: Skill Asset
title: Scorecard update protocol
description: The defined output of a periodic scorecard update - inputs from handover-and-adoption and portfolio-and-savings-analysis, the metrics refreshed with read dates, and the round-ready output, so the result is a reusable record rather than a one-off report.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [all, template, protocol]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---

# Scorecard update — ⟨month/quarter⟩

Copy once per reporting cycle. Fill as the work happens, not afterward.

| | |
|---|---|
| **Cycle** | ⟨month/quarter⟩ · ⟨year⟩ |
| **Prepared by** | ⟨name⟩ · ⟨date⟩ |
| **Round this feeds** | ⟨ODEC · COP · both⟩ on ⟨date⟩ |

## 1 · Inputs received

| From | What | Reference |
|---|---|---|
| `od-handover-and-adoption` | Use cases moved `IMPLEMENTED` → `PRODUCTIVE` this cycle; any new `NEVER`-utilization findings | ⟨handover record(s)⟩ |
| `od-portfolio-and-savings-analysis` | Refreshed savings roll-up (tracked vs. proven), by region/capability | ⟨roll-up reference⟩ |
| `od-acceptance-test` | Readiness-dimension changes this cycle, each with its acceptance-test record | ⟨record(s)⟩ |

A cycle with no input from one of these three still produces a scorecard update — record
"no change recorded this cycle" rather than omitting the row.

## 2 · Metrics refreshed

Refetch each from its authoritative source (`SKILL.md`'s sources table); do not carry
forward a figure from the previous cycle unread.

| Metric | Value | Read date | vs. target-to-date | Status |
|---|---|---|---|---|
| Integrated Use Cases (year) | | | | |
| Integrated Use Cases per month | | | | |
| Integrated Equipment (year) | | | | |
| Integrated Equipment per month | | | | |
| System / capability readiness | | | | |
| Use-case utilization rate | | | | |
| Use-case asset mix | | | | |
| Value delivery cycle | | | | |

## 3 · Readiness matrix, this cycle's changes only

Per `references/readiness-evidence.md` — every change here traces to an acceptance-test
record, never a status update.

| Dimension × location | Previous | Now | Evidence (acceptance-test record) |
|---|---|---|---|
| ⟨…⟩ | | | |

## 4 · Regional breakout (per `references/rounds-and-escalation.md`)

| Region | Equipment Integration: today (plan) | Use Case Development: today (plan) |
|---|---|---|
| EMEA East | | |
| EMEA West | | |
| Americas | | |
| APAC | | |

## 5 · The honest headline

⟨One or two sentences: which leading/lagging metrics agree, which diverge, and what that
implies per `references/scorecard-structure.md`'s cause-and-effect ordering — never lead
with the more favourable number alone.⟩

## 6 · Round output and the one retro change

| | |
|---|---|
| **Round output recorded** | ⟨roadmap decision / rollout guidance / priority change, with owner⟩ |
| **This cycle's one retro change** | ⟨the single decided adjustment — not a list⟩ |

## 7 · Open gaps carried forward

⟨Any `⟨to confirm⟩` field from `SKILL.md`'s metrics table still open this cycle — list them
so they are visibly still open, not silently dropped.⟩
