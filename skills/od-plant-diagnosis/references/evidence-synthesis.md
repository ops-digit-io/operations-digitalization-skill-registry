---
type: Skill Reference
title: Evidence synthesis
description: How to turn interviews, workshops and gap-analysis notes into a plant diagnosis without over-claiming - grounding tags, coverage, the splitting variable, hard vs soft anchors and ranked open questions; open it before writing a diagnosis from interview notes.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Evidence synthesis from interviews

Method taken from the interview-based business-case update; applied here to plant diagnosis. No figures.

## Rules

1. **Find the splitting variable first.** Sort the plants by the one variable that drives the economics (example in the
   source: who owns the machine programs in-house) before averaging. A fleet average mixes two populations and hides the
   value. State the baseline per segment.
2. **Grounding tag on every claim or figure**: `[input]` stated by a source, `[assumption]` our estimate, `[market]`
   standard value when none was given, `[unknown]` crucial missing input we refuse to fake. An untagged figure does not leave
   the department.
3. **Carry unverified claims as unverified.** A claim "not found in the transcript" is neither dropped nor repeated as fact.
4. **Report evidence coverage per cluster**: full, partial, thin or none. Flag conclusions that lean on thin coverage.
   Uneven interview coverage means "not mentioned" is not "absent".
5. **Hard anchors vs soft.** Observed per-case costs and observed support spend are hard anchors, kept as single-plant anchors
   until a second plant confirms them. Interviews validate mechanism and baselines, not a bottom-up total.
6. **Do not mistake suppressed demand for stability** (a locked site makes few changes because it cannot).
7. **Redirect, do not add.** If the interviews show a problem is already solved (for example backup is standard) and the real
   gap is governance, point the action at governance.
8. **Re-scope to the addressable slice.** Credit an action only for the part of the problem it can reach.
9. **Enabler cases** are scored as enablers with the entry-condition relation written down.

## Output per plant or cluster

Baseline (before); sharpened statement (after); interview anchors, one line per source *role*; still open. Closing table:
before, now, direction (sharper, re-scoped, reframed, redirected, partial).

## Ranked open questions

Rank by influence on the conclusion. Lead each with a worked example so the answerer corrects a value rather than invents one.
Each has an owner role (for example controlling, purchasing, quality, plant key user).

## Interview and workshop practice

- The local key user is the entry point; typical contacts (heads of lines or departments) know the top-priority issues,
  the technical depth sits with setters, process engineers and specialists: interview both levels.
- Iterate dashboards or findings step by step; stakeholders often bring ideas but cannot state clear requirements at once.
- Plant visit blocks that are not discovery (trainings, hands-on use-case creation, machine-integration day) should not be
  counted as diagnosis evidence.
- Quote roles, never names; strip plant identity if the record leaves the department.

## Pitfalls

- Targets inherited from a blueprint without checking the baseline.
- Counting a relief (avoided external support) at fleet scale from one plant's figure.
- Reading a good-practice signature from one enthusiastic contact; confirm with a second role.
