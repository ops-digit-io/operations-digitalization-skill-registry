---
type: Skill Asset
title: Retro record
description: One-page monthly retro record with the check of last month's adjustment, the evidence list, exactly one decided adjustment and the parking list.
resource: ../SKILL.md
status: draft
tags: [all, practice]
---

# Retro record

Procedure: [`../SKILL.md`](../SKILL.md). Roles only; no names; no agenda.

| Field | Entry |
|---|---|
| Month | ⟨YYYY-MM⟩ |
| Prepared by (role) | ⟨role⟩ |
| Roles present | ⟨roles⟩ |
| Inputs read, with read dates | metrics ⟨date⟩ · COP ⟨date⟩ · ODEC records, historical ⟨date or "not used"⟩ · incidents ⟨source, date⟩ · risk reading ⟨date or "not run"⟩ |

## 1. Check of last month's adjustment

| Last month's adjustment | Observable named then | What we saw (evidence, date) | Outcome |
|---|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨kept / changed / dropped⟩ |

## 2. What was learned

| # | What happened | Evidence (source, date) | Input | OD can change it? | First seen |
|---|---|---|---|---|---|
| 1 | ⟨⟩ | ⟨⟩ | ⟨metric / incident / COP / ODEC record⟩ | ⟨yes / no⟩ | ⟨YYYY-MM⟩ |

## 3. The one adjustment

| Field | Entry |
|---|---|
| Adjustment (an action) | "From ⟨date⟩, ⟨role⟩ does ⟨X⟩." |
| Why this one (one sentence, rule a / b / c) | ⟨⟩ |
| Owner role | ⟨role⟩ |
| Observable at the next retro | ⟨metric, record or round output⟩ |
| Reversible? | ⟨yes / no⟩ |
| Decided by (role) and date | ⟨decider role, to confirm⟩ · ⟨date⟩ |
| Gate outside OD touched? | ⟨no / yes: routed with `od-decision-routing`, reference⟩ |
| Passed to | ⟨next COP input or the deciding role per the current approval policy (look up) · `od-context-freshness`⟩ |

If there is no evidence-backed candidate, write: "No adjustment this month: no evidence-backed candidate", and list the inputs read.

## 4. Parking list

| Item | First seen | Months parked |
|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨⟩ |

## 5. Escalations (items OD cannot change by itself)

| Item | Forum (strategy and priority: deciding role per the current approval policy, look up; technical: COP) | Sent via |
|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨⟩ |
