---
type: Skill Asset
title: Missing signal and binding table
description: The two tables of AI signal selection - signals needed but not collecting, reported first, and the binding of each matched tag to a requirement and a dashboard panel.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, ai, template]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Missing signal and binding table - <machine or equipment type> · <plant>

Illustrative template. Report table A before anything else. Fill with `<...>`.

| | |
|---|---|
| Inputs | datapoint export `<date>` · requirements `<version>` · reference dashboard `<yes/no>` · HMI screenshot `<yes/no>` |
| Prepared by / date | `<agent or role>` · `<date>` |
| Expert validation | `<role>` on the running dashboard · `<date>` · `<accepted/changed>` |

## A Missing signals (reported first, never approximated)

| Signal id | Label | Why needed (requirement) | Hand over to |
|---|---|---|---|
| `<id>` | `<label>` | `<requirement ref>` | `od-signal-standardization` / information-integration lane |

## B Binding of matched tags

| Requirement | Tag id | Tag label | Match rule | Query pattern | Panel | Unit and scaling |
|---|---|---|---|---|---|---|
| `<ref>` | `<id>` | `<label>` | `<label suffix scoped to device · other>` | `<trend · latest · event-anchored · scaled>` | `<panel>` | `<unit, factor>` |

## C Dropped and open

| Item | Reason |
|---|---|
| `<archived point · ambiguous label · unit unknown>` | `<>` |
