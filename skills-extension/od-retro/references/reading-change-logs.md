---
type: Skill Reference
title: Reading change logs
description: What the generated use-case change logs record, what a line means, which kinds of change are signal and which are noise (bulk sweeps, tidy-ups, field-only edits), and how to turn a log into a retro learning item with evidence.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, retro, registers]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Reading change logs

Derived from the vault's register hub and the yearly use-case change logs. Method only: no counts of changes, use cases or plants,
and no dated events from the logs are carried. Own synthesis is marked `PROPOSAL`; unknowns are `<...>`.

## What a change log is

A generated register, one note per calendar year, built from the **version history** of the use-case list. It lists every dated
change of a use-case item: when, which use case, at which plant and under which capability template, what changed from what to
what. It exists so a retro (or any "what happened to this use case" question) can be answered from evidence instead of memory.

**It is AI-generated and not reviewed by a human.** The generator builds it; the text of any revision is not in the log but in the
use-case note's full-text block, under its earlier values. Change the generator, not the log.

## Anatomy

| Part | What it tells you |
|---|---|
| Header sentence | For the year: how many changes on how many use cases, split into *first recorded*, *with a status change*, *with a text revision (no status change)*, *with changes of other tracked fields only* |
| Quarter sections | The same entries grouped by calendar quarter, in date order |
| Line | `date · use case (plant, capability template): what changed` |
| Line kinds | **first recorded** (with its initial status) · **status** old to new · **text revised** (for example the target text) · **other tracked field** (priority, potential, development, implementation, handover, iteration, risk, implementation date) old to new |
| Sources | The list's version history and the generator script |

The header split is a **quality hint**: a year in which most changes are other-field edits and few are status changes describes
maintenance activity, not progress. Read the split before the lines.

## How to read it

1. **Pick the question.** (a) What moved in a status? (b) Which records were created? (c) Which texts were revised (rationale
   written or tidied)? (d) Which planning fields were touched?
2. **Filter to that line kind.** Status and first-recorded lines answer progress questions; other-field lines answer planning
   hygiene questions.
3. **Look for same-day clusters.** Many lines of the same kind on the same date for the same plant are **a bulk edit by one person**
   (for example a sweep that sets an old priority to closed), not many independent events. Count the sweep once and name it.
4. **Read direction, not volume.** A status moving back, a handover marked done while development is still open, or a priority
   moving to closed without a matching status change are the lines worth a question.
5. **Check the text.** A text revision is not shown in the log. Open the use-case note's earlier values: rationale, blockers and
   comments were often written during active work and later tidied away (see `dept-os`, honesty rule on version history).
6. **Cross-read.** Pair a status change with the saving basis and the blocker texts for the same use case before drawing a
   conclusion (`od-portfolio-and-savings-analysis`).

## Signal and noise

| Pattern | Reads as | Action |
|---|---|---|
| Bulk priority or status change on one day for one plant | Administrative sweep or a close-out decision | Ask the plant owner what the rule was; record it once |
| Many first-recorded lines with the same initial status | A wave or workshop output creating records | Link to the wave; it is a demand event, not a delivery |
| Status moves forward with handover and implementation fields updated together | A real delivery event | Candidate for a "what worked" item |
| Field-only edits with no status movement for a long time | Planning noise or a stalled use case | Candidate for the kill-or-hold review (`references/process-chain-practice.md`) |
| Text revised with no status change | Rationale written or removed | Open the earlier value before judging |
| A year with very few lines | Low maintenance, or a tracking gap | Do not infer inactivity; check the list owner's practice |

`PROPOSAL`: classify each log line used as retro evidence into **progress, planning hygiene, record creation, or text change**, and
quote the class with the line; it keeps a retro from counting maintenance as progress.

## From log to retro item

A usable item from a log has: the question, the line kinds used, the date range, the use cases (or the wave) it covers, the
sweeps identified and set aside, the cause class and the proposed one adjustment. If the evidence is a single sweep or a
keyword-inferred theme, say so; themes in the sibling blocker register are **inferred by keyword** and are leads, not findings.

## Limits to state in any retro that uses a log

- Net change **per version** of the list: edits inside a single version are invisible.
- The log covers the list items that have a note; items without a note are not rendered.
- Timestamps are those of the list's versions, not of the underlying event on the floor.
- It is generated at a point in time; re-generate before quoting it as current.

## AI agent operating notes

- **May do:** filter a log to a use case, a plant, a template or a quarter; separate sweeps from independent events; classify lines;
  draft a retro item with the evidence cited; list use cases whose status and field edits disagree.
- **Inputs:** the log year(s), the use-case notes with earlier values, the blocker register, the saving basis.
- **Evidence to cite:** the log year and line (date, use case, change), generation date, and the earlier-value block if a text was
  checked.
- **Human gate:** the retro owner decides which single adjustment is taken; naming a person's edit pattern (who swept what) stays
  out of the record, roles only.
- **Hands over to:** `od-retro` decision table, `od-risk-watch` (recurring blockers), `od-context-freshness` (a log older than the
  last list change).
