---
type: Skill Reference
title: Decision rights framework
description: Why Tandem, Consultation and Information are not ad hoc labels — each is one role pairing from a named decision-rights framework, cited so the vocabulary can be checked and extended.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [all, practice, decision-rights]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# Decision rights framework

`SKILL.md`'s table already works. This reference exists so its three modes are a cited
framework, not a house convention nobody can check against a source.

## Why RAPID, not RACI

RACI (Responsible, Accountable, Consulted, Informed) answers "who does the work and who
owns the deliverable" — a task-execution matrix. This skill answers a different question:
**who decides, and in what mode** — before any work starts. That is exactly what Bain &
Company's RAPID framework was built for (Rogers, P. and Blenko, M. (2006). *Who Has the D?
How Clear Decision Roles Enhance Organizational Performance*. Harvard Business Review,
84(1), 52-61).

RAPID names five roles: **R**ecommend (proposes, marshals the facts), **A**gree (formal veto
on named grounds), **I**nput (gives facts and perspective, no veto), **P**erform (executes
once decided), **D**ecide (the single decision-maker). Three of this skill's rows map onto
RAPID directly:

| This skill's mode | RAPID role pairing | What it means in practice |
|---|---|---|
| **Tandem** | OD holds Recommend, the named counterpart holds Agree | Both parties have a veto — the counterpart can block the recommendation on the grounds the table states (budget, cyber security, cross-plant consumability), and OD cannot proceed without it |
| **Consultation** | OD holds Decide, the counterpart holds Input only | The counterpart's view is sought and weighed, but carries no veto — OD decides alone and is accountable for having heard it |
| **Information** | OD holds Decide and Perform, the counterpart is informed after | Tell, do not ask — the counterpart has no role in the decision at all, only notice of it |

**One decision, one `D` or one `A`+`R` pair.** RAPID's own central warning is the same one
this skill's table already enforces structurally: a decision with two people both able to
say yes and no different things is not Tandem, it is undefined — if a decision in this
registry ever needs a third party's agreement, add a row, do not stretch an existing
Tandem into a three-way one.

## Applying it to a new decision not yet in the table

1. Name who recommends (almost always a DBVE or IIAE role in this registry — OD never
   holds Decide alone on anything that commits spend, a standard or an external connection).
2. Name who holds Agree or Decide — read it off `od-context`'s service-line ownership, or
   escalate to the OD lead if no owner is named yet.
3. Pick the mode from the pairing table above — do not invent a fourth mode. If none of the
   three fits, the decision does not belong in OD's own table; it is one of
   `od-decision-routing`'s five outside gates instead.
4. Record the threshold and reversibility exactly as the existing rows do — a mode without a
   threshold is not yet decidable, only discussable.
