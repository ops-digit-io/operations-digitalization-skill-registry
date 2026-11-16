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

The foundation every other OD skill assumes: one vocabulary, the three new-state lanes, who decides what, where the
truth lives, and the honesty rules. Serves every process step as the precondition (it is not a step of its own);
users are all roles and every AI agent, which loads it before any OD work.
**Inputs:** none (read-only). **Output:** a resolved term, route or source, never a figure (numbers are read live from
the lists below).

## Outputs and hand-off: the text before outputs.yaml

`dept-context` is the read-only foundation, not a step of its own. It delivers a resolved term, route or source to the skill that asked, never a figure of its own.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Resolved term, lane or gate | Chat reply, taken from the vocabulary table or its reference | The calling skill and its user | Each term has one meaning; where two sources disagree, the SharePoint list wins |
| Source for a figure | Chat reply naming the list and export date | The calling skill | The figure is read live from the named list; no figure is stated without a nameable source |
| Gate route | Chat reply pointing to `dept-decision-rights` | `dept-decision-rights` | The gate is routed through "Who decides"; the decision stays with the named role |
| Unresolved marker | "to confirm" marker in the calling skill's output | The calling skill and the OD lead | A figure with no source or a term that does not resolve is marked and work stops there; the gap is not filled |

## Handoff

- **Receives from:** none; it is read first by every OD skill.
- **Next in the flow:** it has no step id. The spine serves every step; gates go to `dept-decision-rights`, and blocked work goes to the OD lead.
- **Stops here when:** a term does not resolve or a figure has no source. Mark it to confirm and stop. It never writes to the knowledge graph or acts on an external machine connection.
