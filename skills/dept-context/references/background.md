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

## Old service lines to new state (moved from SKILL.md)

| Old service line (owner) | New state |
|---|---|
| Smart Factory Use Case Support Service, incl. Process First-Aid Kit (DBVE) | Known use cases to Lane 1; genuinely new to Lane 2 |
| Analytical Support Service, incl. Ad-Hoc Analytics (DBVE) | Retired as a standing lane; ad-hoc analytics routes to Lane 1 self-service, Lane 2, or external support (`funnel-first-aid`) |
| Information Integration Service (IIAE) | Lane 3 branch 3b; integration-project management folds in (`mi-equipment`) |
| Project Support & Application Consultancy (IIAE) | The shared Lane 3 front-end: requirements, decision gate, clear demand, handover |

## Dates moved out of SKILL.md

- Lane 4 was added on 2026-11-10 at the owner's request.
- ODEC was held monthly until 2025-12 and is no longer held; it is a source of past decisions only.
- Databricks, the Azure Storage Account and Parquet were separate vocabulary rows; they are merged into the Data platform row.
