---
type: Skill Asset
title: Use case definition questionnaire
description: The actual questions to ask, in order, across the four phases - Is/Is-Not and 5 Whys for Analyse, a Benefits Dependency Network walk-through for Control - so a workshop produces a defined use case instead of a title and a savings guess.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [use-case-support-service, questionnaire, workshop]
generated: { by: claude-code/1, at: 2026-09-17T00:00:00Z }
---

# Use case definition questionnaire

> **Sourcing.** Is/Is-Not is Kepner-Tregoe's problem-specification technique; 5 Whys is
> Toyota's. Both are standard Lean/CI tools, adapted here to this department's four phases
> — not reproduced in general form. The rest is built from the real fields this registry's
> own use-case pages actually carry (`references/worked-examples.md`,
> `references/vocabulary.md`).

Run this in order. Do not let the requester skip to Phase 4 because they arrived with a
solution already in mind — that's useful information (note it), not a shortcut. Answers go
into `assets/use-case-definition-protocol.md` as you get them.

## Before you start

Listen for these while you work through every phase, not just where they're listed:

- **Opens with the solution, not the problem** ("we need a dashboard that shows...").
  Normal — note it, then ask Phase 2's questions anyway. A solution offered early is a
  hypothesis to test, not a scope to accept.
- **"Everyone wants this."** No named owner behind a stated need is a need that stalls at
  Control. Ask who, specifically, changes what they do.
- **The "why" chain ends at a person or "that's just how it is."** Both mean you stopped
  one level too early — go back and ask the branch again from the process, not the person.

## 1 · Collect

1. Who are you, and what's your role here?
2. Walk me through the moment this comes up. Is it during the daily Gemba walk, a shift
   handover, troubleshooting something that's already broken, or something else? (Real
   vocabulary: `references/vocabulary.md` — Daily Gemba, Troubleshooting, Activity
   Tracking, Utilization Improvement, Process Improvement, Quality Improvement,
   Traceability, Energy Reporting.)
3. How often does this come up — every shift, weekly, or only when something's already
   gone wrong? (A need that only surfaces once is a first-aid request, not a use case —
   route it accordingly rather than defining it here.)
4. If I asked five people on your shop floor about this, would they describe the same
   problem? (If the honest answer is "no, everyone means something different," stop —
   that's several use cases wearing one name.)
5. Is this already logged anywhere — a use case list, a prior workshop note, an email
   thread? (Don't define a duplicate; find and update the existing record instead.)

**Before moving on:** can you state the need in one sentence with no "and" in it? If not,
split it now, before Analyse makes the split harder to see.

## 2 · Analyse

**Current vs. desired, in the requester's own words:**

6. What's happening today — not the fix, the symptom? Numbers if you have them.
7. What should be happening instead?

**Is / Is-Not — scope the problem before diagnosing it:**

| | **Is** (where/when it happens) | **Is Not** (where/when it doesn't, though you might expect it to) |
|---|---|---|
| Where | ⟨line, station, plant⟩ | ⟨a comparable line/station that's fine⟩ |
| When | ⟨shift, condition, cycle phase⟩ | ⟨a comparable time that's fine⟩ |
| Who | ⟨affected role⟩ | ⟨a comparable role that isn't affected⟩ |

The **Is Not** column is where the actual cause usually hides — what's different between
the two columns is the lead.

**5 Whys — stop at something actionable, not a person or a shrug:**

8. Why does that happen? → *(ask the answer back as a why, twice more)* → Why does *that*
   happen? → Why does *that* happen?

**Before moving on:**

9. What have you already tried, and why didn't it stick?
10. If nothing changes for another year, what does that actually cost — scrap, downtime,
    rework, a near-miss, or just nobody trusting the number on the board anymore?

State the objective in one sentence. It should name the gap from step 7, not a dashboard.

## 3 · Assess

11. Which machine or line does the data come from, and is it connected today? (If not,
    this is an integration request first — `od-equipment-integration`.)
12. Which system already touches this — even a spreadsheet? RuleEngine 2.0, MSB, MDA-PDA,
    QFPR, MIL, Data Science Factory, Energy Management, or something not on that list?
    (`references/vocabulary.md`)
13. Is there a legacy application on the retirement list that's supposed to already cover
    this?
14. *(Open `references/library-catalog.md` together, in the room.)* Has another plant
    already built something close to this? What's different about your case?
15. What data would this need that you don't have today, and whose job is it to get it?

## 4 · Control

**Walk the Benefits Dependency Network, in this order — `references/benefit-theory.md`:**

16. Picture the day after this ships. Who does something differently than they do today?
    Walk me through their day, before and after — specifically, not "they'll have better
    visibility."
17. Who confirms, a few months from now, that they're actually doing that differently?
18. Is the benefit a number that shrinks a budget line, or does it free up capacity
    without removing a cost? (cashable vs. non-cashable, `references/benefit-theory.md`)
19. Can you put a rough number on it? If not — is that because it's genuinely hard to
    count, or because nobody's tried yet? Either answer is fine; a guess dressed up as a
    number is not.

**Options considered — say it out loud, one sentence each:**

20. What happens if we do nothing for six months?
21. Did the library entry from question 14 actually not fit, or would it with a small
    change?
22. Would a smaller scope — one line, one shift, one plant instead of the wave — get most
    of the value for a fraction of the build?

**Close it out:**

23. What does this depend on that's outside your control — an eCR, a machine integration,
    plant IT, another team's roadmap?
24. Output asset: Dashboard, Report, App, Analytics Workflow, or Agent? (Dashboard is the
    default — if you're naming something else, say why a Dashboard wouldn't do.)
25. Who's the named plant owner — not a department, a person?

## Before you leave the room

Check against `SKILL.md`'s four control points. If any of these isn't a real answer yet,
the use case isn't defined yet, whatever else got written down:

- [ ] Demand logged against the plant roadmap
- [ ] Objective stated as a gap, not a solution
- [ ] Business benefit stated and classified (tangible/intangible × cashable/non-cashable)
- [ ] Options considered, with what was rejected and why
- [ ] Systems and machines assessed, library checked
- [ ] Business/process change named, with who confirms it
- [ ] Output asset, business process, utilization expectation and a named owner recorded
