---
type: Skill Reference
title: Status labels
description: Which OD AI items the department decks label pilot, PoC, PoC proven or rollout, where the two decks disagree, and the rule for quoting a label.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Status labels

Source: the two AI decks in the knowledge bundle, read 2026-11-05 (slide text only). Neither slide carries a
date or an owner name in its text, so quote the file name, not a date of the item.

## "Where do we apply AI already" (`AI_Where_We_Apply_Today.pptx`, one slide, MPEE / OD rows)

| Item | Label on the slide |
|---|---|
| Department OS - auto-generated context and decks | building |
| AI manufacturing dashboards - live at two plants named on the slide (Mako, Subotica) | **rollout** |
| AI requirements-to-mockup (Gemba App) | **pilot** |
| AI machine signal selection | **PoC** |
| Manufacturing app store - GitOps deployment | **pilot** |
| Agentic dashboard and integration-flow creation | **PoC** |
| Claude Desktop for analysis and documents | **pilot** |
| Deployment efficiency - SQL troubleshooting and technical docs | initiative |
| Cycle time analyzer (plants / manufacturing) | live on the shopfloor, **rollout** |
| Predictive maintenance (plants / manufacturing) | initiative |

## "Where we apply AI today" (`AI_Board_TwoPager.pptx`, slide 1 of 2)

| Item | Label on the slide |
|---|---|
| AI-assisted analysis and document work (Claude Desktop / Cowork), MPEE / OD | pilot |
| Predictive quality - defect prediction | **PoC proven** |
| Cycle-time optimization analyzer | **PoC proven** |
| Agentic dashboard creation, MPEE / OD | **PoC proven** |
| Agentic integration-flow creation, MPEE / OD | **PoC proven** |
| HS-code classification for trade compliance | PoC |
| Domain chatbots (FMEA, R&D project knowledge) | PoC / example |

Slide 2 of the same deck ("Where we want to apply AI - next 3 to 6 months") lists "AI requirements-engineering
pipeline - MPEE / OD / IT" as a target, not an applied item.

## What the two decks show

1. **The labels disagree on the same item.** "Agentic dashboard and integration-flow creation" is **PoC** in the
   first deck and **PoC proven** in the second. "Cycle Time Analyzer" is **rollout** in the first and the "cycle-time
   optimization analyzer" is **PoC proven** in the second (the names differ slightly; assumed to be the same item, to confirm). The slide text does not say what "proven" was measured against, by whom or
   when. ⟨Definition of "PoC proven" and the evidence behind it⟩: OD lead.
2. **"Rollout" means live use at named plants**, not proven savings. For the AI dashboards the slide names two plants;
   it gives no euro figure. A saving still has to be a row in `od-benefit-calculation` and, to be proven, pass SPRINT.
3. **The requirements-to-mockup item is labelled "pilot"**, the middle rung. It is neither a PoC proven nor a rollout.

## Rules for using a label

- Quote the label with its source file: "pilot (AI_Where_We_Apply_Today.pptx)".
- Do not upgrade a label because a deck for a higher audience uses a stronger word.
- Do not write "proven" for any pilot or PoC. In this department proven value means finance confirmed it through
  SPRINT (`od-benefit-calculation`: 19 of 553 recorded rows, a figure dated 2026-10-22; check it is still current).
- A pilot at one plant is not a rollout. State the number of plants and the period.
- If the slide gives no scope, period or measure, write ⟨scope / period / measure not stated⟩.
