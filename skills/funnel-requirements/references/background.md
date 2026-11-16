---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Purpose and where it sits

Turns an accepted demand into a requirement another lane can act on, plus one epic with its user stories. It serves
Lane 2 step **22** (features and data check) and the Lane 3 front-end step **31** (requirements). The lane variant is
the artefact that crosses a lane boundary; it makes tacit judgement explicit. Key user: DBVE (use case, analytics) or
IIAE (integration, project). An AI agent drafts; the receiving lane accepts or says what is missing. Read `dept-context`
first. The template is not new: its headings already appear in the estate's `target_text` and `blockers` fields
(`references/requirement-template.md`).

## Example

Fictional example (requirement and output invented for illustration):

If the check reports a blocker, validate the named section against `requirement-template.md` (`references/requirement-template.md`) and re-run; do not hand over with a failed check.

## Outputs and hand-off: the text before outputs.yaml

`funnel-requirements` delivers the requirement another lane can act on, with its lane variant, and the handoff file the
next funnel stage resumes from. Nothing crosses a lane boundary without its variant.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Requirement with lane variant | `assets/requirement-template.md`, filled, with the variant section for the lane (`use-case`, `integration`, `project` or `analytical`) | `invest-screen` (step 32), `mi-equipment`, OpenSpec IT demand (external); receiving lane | Sections 1-6, 6a and 10 complete; variant present; every signal has a verdict from `mi-data-availability`; acceptance is testable with a real-shift adoption criterion; blockers classified with owners; legacy assessment and value label done; growth boundary stated |
| Epic with stories | Epic with at least two stories, cut by moment and role | `funnel-features` | Epic check reports zero blockers; no story cut by technical layer; each story has a use-in-a-real-shift criterion |
| Funnel handoff file | File per `references/handoff-schema.md`: `frame`, `riskiest_assumption`, `problems`, `candidates` | `funnel-features`, `funnel-prototype` | The next stage can resume without re-asking |
| Missing-signal table | Table `signal id / label / why needed` in the requirement | Information integration lane via `mi-equipment` | Every needed signal not yet collecting is listed with its reason |

## Handoff

- **Also receives from:** `ops-event-model`: Event definition canvas.
- **Also receives from:** `catalog-usecase`: Fall-through statement.
- **Receives from:** `dept-intake` (the accepted demand) or `funnel-use-case` (the defined use case);
  `mi-data-availability` (signal verdicts); `mi-signals` (public data model check).
- **Next in the flow:** `funnel-features` (the epic), `funnel-prototype` (step 23), `invest-screen` (step 32 in Lane 3),
  then `bc-build` (steps 24 and 33). The variant goes to the receiving lane.
- **Stops here when:** either check reports blockers (do not hand over with a failed check), there is no roadmap link or
  nameable business case, the need needs a system outside the lean footprint, it is owned by a sibling function, it is a
  one-off, or it already exists elsewhere. Refuse with a named route and a written reason.
