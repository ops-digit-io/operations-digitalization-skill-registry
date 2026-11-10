---
type: Skill Reference
title: Message and claims
description: How to word the single message and the proof points of a use-case story - evidence classes, result versus claim, scope statements, style rules and a worked before-and-after with placeholders only. Open it when a claim is unclear or a draft reads stronger than its evidence.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [lane-4, practice]
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Message and claims

The rules here are the knowledge base's own (`CLAUDE.md` sections 1.5 and 3: no invented figures, roles not individuals, English) and the registry's savings rule. They are proposed for Lane 4; the OD lead has not confirmed them.

## Evidence classes

| Class | Meaning | May be worded as |
|---|---|---|
| `CALCULATION` | Derived from named inputs by a stated method; the method is in the source | A result, if a plant savings project and a baseline are registered; otherwise a claim |
| `ESTIMATION` | A judgement with a stated basis and a range | A claim, with the range |
| `not yet assessed` | No basis yet | Not stated as a figure |

A saving is a **result** only when a plant savings project and a baseline are registered (`od-use-case-definition`, lane service flow). Until then say "expected" or "targeted" and name the class. Never round a figure up, never drop its scope.

## Scope statements

State the scope exactly: the plant, the line or machine group, the period. "One line at one plant for one quarter" is a scope; "plants" is not, unless several plants are meant.

## The message

One sentence, present tense, concrete: *what changed, where, for whom.* It must be repeatable by someone who read only that sentence, and it must be supported by at least one proof point of class `CALCULATION` or by an adoption fact (utilization, used in a real shift).

## Proof points

Two to four. Each: the claim, the class, the source (a file, register entry or dashboard, cited by name and date), and whether it is worded as a result or a claim. Adoption facts are strong proof and need no savings figure: "The shift lead uses the screen in the daily meeting" beats an unregistered number.

## Style

- Plain words. No superlatives ("revolution", "game-changing", "first ever", "best").
- Roles, never individuals. The plant, not the person who built it.
- No host names, addresses, links to internal systems, or credentials.
- Every draft repeats the proof points and adds no claim the brief does not carry.
- Placeholders (⟨ ⟩) stay visible until filled; a draft with a placeholder is not ready.

## Before and after (placeholders only)

| Before (fails the check) | After |
|---|---|
| "Our new dashboard will save ⟨amount⟩ and transforms the plant." | "At ⟨plant⟩ the shift lead reviews ⟨topic⟩ at the daily meeting on ⟨line⟩. Expected effect: ⟨figure⟩ (ESTIMATION, ⟨source⟩), to be confirmed once the savings project is registered." |
| "Built by ⟨name⟩." | "Built with the plant's ⟨role⟩." |
| "Available to all plants." | "Catalogued; a plant can request it through ⟨route⟩." |
