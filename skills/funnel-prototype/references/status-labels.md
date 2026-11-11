---
type: Skill Reference
title: Status labels
description: How the department's AI decks label items (pilot, PoC, PoC proven, rollout), the ways labels mislead, and the rule for quoting one - no list of which item carries which label today.
resource: ../SKILL.md
status: draft
tags: [use-case-support-service, practice]
---
# Status labels

Sources to read for the *current* labels: `AI_Where_We_Apply_Today.pptx` (MPEE / OD rows) and `AI_Board_TwoPager.pptx` in the
knowledge bundle (slide text only). Neither slide carries a date or an owner name in its text, so quote the file name, not a
date of the item. This file does not copy which item carries which label; open the decks.

## The label ladder the decks use

`initiative` (an idea with an owner) -> `building` -> `PoC` -> `PoC proven` -> `pilot` -> `rollout` / `live`. Note that the two
decks do not use one ladder: "PoC proven" appears only on the board deck, "pilot" and "rollout" mostly on the department deck.

## What the decks show (patterns to check each time)

1. **The labels can disagree on the same item.** An item can be "PoC" in one deck and "PoC proven" in another, and an item
   can be "rollout" in one deck while a differently named twin is "PoC proven" in the other (assume same item only after
   confirming). The slide text does not say what "proven" was measured against, by whom or when.
   ⟨Definition of "PoC proven" and the evidence behind it⟩: OD lead.
2. **"Rollout" means live use at named plants**, not proven savings. The slide may name plants; it gives no euro figure. A
   saving still has to be a row in `bc-build` and, to be proven, pass SPRINT.
3. **"Pilot" is the middle rung.** It is neither a PoC proven nor a rollout. Items such as the requirements-to-mockup item
   and the app-store GitOps deployment have carried it.
4. **Target slides are not applied items.** A "where we want to apply AI next" slide lists targets, not things in use.

## Rules for using a label

- Quote the label with its source file: "pilot (AI_Where_We_Apply_Today.pptx)".
- Do not upgrade a label because a deck for a higher audience uses a stronger word.
- Do not write "proven" for any pilot or PoC. In this department proven value means finance confirmed it through
  SPRINT (`bc-build`); count the proven rows live on the saving rows before quoting any share.
- A pilot at one plant is not a rollout. State the number of plants and the period (read from the source, then say so).
- If the slide gives no scope, period or measure, write ⟨scope / period / measure not stated⟩.
