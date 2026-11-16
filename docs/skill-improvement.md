---
title: Skill improvement run: before and after
description: "The 51 skills were improved from the review against Anthropic's skill-authoring best practices, then reviewed again blind. This page compares the two runs, with a control for reviewer drift."
---

# Skill improvement run: before and after

Run date 2026-11-16. Before: the review in [skill-review-before.json](new-state/skill-review-before.json) (commit `3afec33`). After: [skill-review.md](skill-review.md) and [skill-review.json](new-state/skill-review.json). Criteria: [skill-review-rubric.md](skill-review-rubric.md).

## What this is and is not

- **Method:** eight improver agents changed the skills from the review and the registry's own files; eight new reviewers then rated every skill again without seeing the earlier review.
- **Reviewers are an AI reading the text.** Nobody ran the skills with and without the skill. The evals were written in this run and not yet executed.
- **Reviewer drift:** a control agent re-reviewed six unchanged skills from the before snapshot. It agreed on 83 of 96 ratings and rated the same unchanged skills +3.8 points higher (86.8 against 83.0). Part of the gain below is that drift.
- **Knowledge used:** the improvers did not use the Obsidian vault or the archive (searches timed out), except for one vault note used by `ops-dashboard-datatron`. Domain content was therefore not extended; gaps are written down as open questions in each `references/background.md`.

## Result by best-practice criterion

Score = (meets + 0.5 x partly) / rated skills, in percent. n/a is left out.

| Id | Criterion | Meets before | Meets after | Partly before | Partly after | Gap before | Gap after | Score before | Score after | Change |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| J1 | Description: what and when, user's key terms | 28 | 51 | 23 | 0 | 0 | 0 | 77 | 100 | +23 |
| J2 | Description: one point of view, user intent | 33 | 41 | 18 | 10 | 0 | 0 | 82 | 90 | +8 |
| J3 | Concise, adds only what the agent lacks | 11 | 21 | 40 | 30 | 0 | 0 | 61 | 71 | +10 |
| J4 | Specificity matches fragility | 50 | 51 | 0 | 0 | 1 | 0 | 98 | 100 | +2 |
| J5 | Procedures, not declarations | 44 | 49 | 7 | 2 | 0 | 0 | 93 | 98 | +5 |
| J6 | Defaults, not menus | 45 | 49 | 6 | 2 | 0 | 0 | 94 | 98 | +4 |
| J7 | Gotchas section | 43 | 49 | 8 | 2 | 0 | 0 | 92 | 98 | +6 |
| J8 | Output template where format matters | 49 | 51 | 1 | 0 | 1 | 0 | 97 | 100 | +3 |
| J9 | Concrete examples | 22 | 50 | 15 | 1 | 14 | 0 | 58 | 99 | +41 |
| J10 | Checklist / validation loop | 34 | 42 | 17 | 9 | 0 | 0 | 83 | 91 | +8 |
| J11 | Progressive disclosure, says when to read | 28 | 48 | 22 | 3 | 1 | 0 | 76 | 97 | +21 |
| J12 | Consistent terminology | 12 | 31 | 39 | 20 | 0 | 0 | 62 | 80 | +19 |
| J13 | Explains the why | 33 | 48 | 18 | 3 | 0 | 0 | 82 | 97 | +15 |
| J14 | Scripts solve, handle errors, state deps | 6 | 12 | 7 | 2 | 1 | 0 | 68 | 93 | +25 |
| J15 | One coherent unit | 31 | 33 | 20 | 18 | 0 | 0 | 80 | 82 | +2 |
| J16 | Grounded in expertise and sources | 29 | 32 | 21 | 19 | 1 | 0 | 77 | 81 | +4 |
| | **All criteria** | 498 | 658 | 262 | 121 | 19 | 0 | **80.7** | **92.2** | **+11.5** |

## Overall rating per skill

| Rating | Before | After |
|---|---:|---:|
| strong | 13 | 25 |
| adequate | 37 | 26 |
| needs-work | 1 | 0 |

Per skill: 14 moved up, 36 stayed, 1 moved down.

## Measured facts, before and after

| Fact | Before | After |
|---|---:|---:|
| Skills with evals | 0 of 51 | 51 of 51 |
| Skills with a long reference lacking a contents list | 33 | 0 |
| Skills with a script lacking `--help` or argument parsing | 2 | 0 |
| Skills with a script that reads interactive input | 0 | 0 |
| Skills with dates in the body | 14 | 17 |
| Mean description length (characters) | 433 | 684 |
| Mean body size (token estimate) | 2484 | 2704 |
| Largest body (token estimate) | 7280 | 5916 |
| Skills with body over 5000 tokens (estimate) | 1 | 1 |

## SkillEvaluator (NVIDIA, tier 1), a second opinion

| Measure | Before | After |
|---|---:|---:|
| Mean score, all 51 skills | 89.8 | 91.3 |
| Mean score, 26 core skills | 95.6 | 93.4 |

Per skill: 25 higher, 24 lower, 2 equal. The tool's scores fall for most core skills for two reasons that are conventions of the tool, not of Anthropic: it deducts for descriptions over 150 characters (the new descriptions carry what and when, about 600 characters, under the 1024 limit of the specification) and for 'vague words' in some descriptions. The tool does not read the evidence the reviewers cite. The two measures disagree here; read the criteria table for what the best practice asks.

## Went the wrong way

- **Dates in the body:** 14 skills before, 17 after. The sources say to avoid time-sensitive text; some new examples carry dates.
- **Size:** descriptions and bodies grew (see the facts). One skill, `know-skill-authoring`, scored slightly lower than before, the only one; its overall rating stayed strong.
- **SkillEvaluator:** core skills score lower (see above).

## Not changed in this run

- Splitting skills that bundle several jobs (J15): `dept-governance`, `invest-screen`, `funnel-evaluation`, `bc-portfolio`, `mi-equipment`, `metrics-scorecard`. It needs a registry decision.
- Sources and owner confirmations (J16): open questions stay open, for example the decision-rights source, the guardrails G8-G19, the project-order chapter rules.
- `metrics-scorecard` has `valid_until` 2026-11-10, already past; its owner has to renew it.
- Deck scripts of `bc-assess` and `bc-capital-request` still carry example slide text.

## Next steps

1. Run the evals with and without each skill: that is the test the sources ask for, and the only way to confirm that the text changes help.
2. Decide the skill splits above.
3. Redo this review after the evals, with a human reading a sample of skills.
