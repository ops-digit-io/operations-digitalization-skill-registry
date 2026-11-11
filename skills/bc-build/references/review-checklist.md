---
type: Skill Reference
title: Review checklist
description: Why a saving row's methodology is usually missing, the smell test that follows from it, and the department's own three failed fixes before the current one — Phase-1 tacit-knowledge item #3, resolved from the department's own retrospective record.
resource: ../SKILL.md
status: stable
tags: [use-case-support-service, practice]
---
# Review checklist

`SKILL.md` explains how to read the honest state of the ledger - many rows carry no
reliability label at all. This file is *why*, taken from the department's own
retrospective rather than from memory, and the smell test it implies.

## Why the methodology field is usually the one missing

The department tried handing savings evaluation to the plants directly, on the
reasoning that they know their own process best. The real result, in its own words:
*"Plants lack confidence in Use Case evaluation and provided 'social proof' by
collectively avoiding doing it."* A plant that is not confident in its own estimate does
not produce a wrong number — it produces no number, or a number with nothing behind it.
**This is the root cause the many empty reliability fields are a symptom of**, not a data-entry
gap to chase down row by row.

## Three things tried before the current approach, in order, each one failing differently

1. **Use Case Library with savings attached.** Reasoning: show plants a proven number
   from elsewhere and let them reference it. Result: *"Looks nice, nobody is looking into
   it really."* A passive reference does not get consulted under deadline pressure.
2. **Add the topic to the workshop format.** Reasoning: force the conversation to happen
   live, with support in the room. Result: *"We are messing up the workshop by having too
   many domains on the table & stall in a non-productive meeting."* Savings calculation
   needs focused time, not a slot inside a broader agenda.
3. **Current approach: provide a Use Case Calculator proactively, iterate on pushback.**
   OD computes the first number itself, using its own formula, and the plant reacts to
   that number rather than being asked to originate one. This is the same shape as
   `SKILL.md`'s own rule — a `CALCULATION` row needs its methodology written down — applied
   one step earlier: write the methodology *before* asking for the number, not after.

## The smell test this gives you

**A saving row that did not go through the calculator is the one to distrust first** —
not because the plant is wrong, but because the department's own experience is that a
plant asked to self-originate a number either avoids the task or produces one with no
stated formula behind it. Before trusting a `CALCULATION` label:

- Can you see the calculator output, or a methodology line that reads like one (a stated
  formula with real inputs), behind this specific row?
- If the row looks plant-authored with no calculator trace, treat it as an `ESTIMATION`
  candidate regardless of its recorded label, and ask for the formula before repeating the
  number anywhere.

## What is still open

The specific reasons a *particular* row gets challenged or bounced at the SPRINT review
itself — as opposed to why the ledger is thin in the first place — are not in this
record. If there is a recurring SPRINT objection (a category SPRINT routinely does not
accept, a methodology SPRINT routinely asks to redo), add it here directly; the above
explains the upstream cause, not the review gate's own criteria.

## Sources

Internal evidence from the department's own workshop material (the MPEE strategy workshop
chapter on use case saving calculation, and a plant definition workshop summary that
listed savings estimation as an open task). Full citations in `SKILL.md`'s
`metadata.derived_from`.
