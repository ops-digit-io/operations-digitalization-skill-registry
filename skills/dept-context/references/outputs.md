---
type: Skill Reference
title: Outputs
description: The outputs dept-context must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

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
