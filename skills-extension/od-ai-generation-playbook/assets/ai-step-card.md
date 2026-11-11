---
type: Skill Asset
title: AI step card
description: The card that admits an AI agent step (owner, data source, review point), records its inputs, evidence and open items, and names the human gate and the next skill.
resource: ../SKILL.md
status: draft
tags: [all, practice, ai, template]
---
# AI step card - <step id> <step title> · <plant or scope>

Illustrative template; fill with `<...>`, never invent values.

## 1 Admission (no name, no start)

| Field | Value |
|---|---|
| Process owner (role) | `<role>` |
| Data source | `<list, export, document>` and read date `<date>` |
| Review point (who, when) | `<role>` · `<moment>` |
| Context section used | `<section>` · owner `<role>` · review date `<date>` · fresh? `<yes/no>` |
| Template used | `<master>` via `od-template-resolution` |
| Agent task | `<draft · classify · extract · summarise · check · monitor · document>` |
| Read-only? | `<yes/no>`; if no, review point is mandatory |

## 2 Inputs (fixed structure)

| Input | Present | Note |
|---|---|---|
| `<tag list / requirements text / reference / equipment reference>` | `<yes/no>` | `<>` |

## 3 Output and evidence

| Output element | Source (row, entry, document) | Read date | Rule or check used |
|---|---|---|---|
| `<element>` | `<source>` | `<date>` | `<rule>` |

Label: `<draft · reviewed>`. Visual QA done: `<yes · no · not possible>`. Placeholder leak check: `<done/not done>`.

## Open items and missing inputs

| Item | Why it matters | Who closes it |
|---|---|---|
| `<to confirm>` | `<>` | `<role>` |

## 5 Human gate and handoff

| | |
|---|---|
| Decision still needed | `<accept requirement · expert verdict · ranking · scope · sign-off · deployment>` |
| Gate held by (role) | `<role>` |
| Gate outcome | `<pending · accepted · changed · rejected>` · `<date>` |
| Next skill / step | `<skill>` · `<step id>` |
| Not done on purpose | `<nothing connected, written, approved or submitted>` |
