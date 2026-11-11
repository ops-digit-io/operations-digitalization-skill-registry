---
type: Skill Reference
title: Outputs
description: The outputs funnel-requirements must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`funnel-requirements` delivers the requirement another lane can act on, with its lane variant, and the handoff file the
next funnel stage resumes from. Nothing crosses a lane boundary without its variant.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Requirement with lane variant | `assets/requirement-template.md`, filled, with the variant section for the lane (`use-case`, `integration`, `project` or `analytical`) | `invest-screen` (step 32), `mi-equipment`, `deploy-it-demand`; receiving lane | Sections 1-6, 6a and 10 complete; variant present; every signal has a verdict from `mi-data-availability`; acceptance is testable with a real-shift adoption criterion; blockers classified with owners; legacy assessment and value label done; growth boundary stated |
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
