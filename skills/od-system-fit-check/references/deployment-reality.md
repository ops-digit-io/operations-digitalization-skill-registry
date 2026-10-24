---
type: Skill Reference
title: Deployment reality
description: Real per-plant tool-availability snapshots showing the same tool catalogue in three different states, so a system-fit check is run against what a specific plant actually has, not against the estate average.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [practice, system-fit]
generated: { by: claude-code/1, at: 2026-10-23T00:00:00Z }
---
# Deployment reality — the same tools, three different plants

Every Use Case Definition Workshop records a **Smart Factory Tools Availability** table —
status and recommendation, per tool, for that one plant. Three real snapshots, to make the
point concrete: the non-bets list is estate-wide policy, but whether MDA/PDA or QFPR is
*available right now* is a per-plant fact that changes between these three alone.

| Tool | San Luis Potosí (Dec 2023) | Subotica/Carei (May 2024) | Timisoara (Jul 2024) |
|---|---|---|---|
| IIoT Edge Computing Platform | Ongoing — planned 2023 | Done | Done |
| Manufacturing Service Bus | Ongoing — planned 2023 | Done | Done |
| MDA/PDA (Iconics Genesis64) | Ongoing — planned 2023 | *(not listed)* | *(not listed)* |
| Manufacturing Execution System | Not available — **not necessary** | Not available — **not recommended as of now** | Not available — **not recommended as of now** |
| Recipe Management (Camline) | Not available — not necessary | Not available — not necessary | Not available — not necessary |
| Manufacturing Image Library | Not available — not necessary | Not available — not necessary | Not available — not necessary |
| Quality Feedback App (QFPR) | Not available — not necessary | **Ongoing — needed for multiple use cases** | Not available — not necessary |
| Data Science Factory | Not available | Not available — planned 2024 | Ongoing — planned 2025 |

**What this is actually useful for:** QFPR goes from "not necessary" to "needed for
multiple use cases" between two plants with no other column changing — availability
tracks demand, not a rollout schedule applied uniformly. **Check this plant's own current
table before assuming a tool is or is not there** — the MES row is the one constant across
every plant checked; everything else moves.

## The one-weeks'-difference case for MIL specifically

Two separate 2024 workshop summaries (Subotica, Timisoara) record the *identical* line for
the Manufacturing Image Library: a demo/test system is already **deployed**, and in the
same breath — *"No Use Cases yet. Not yet planned for [that plant]."* A tool being
technically present is not the same fact as a use case being in scope there. Check which
one a request is actually claiming before accepting it.

## Sources

Internal evidence, read 2026-10-22: `Work-OpsDigit-Knowledge/Split Slides/10-Workshops--
2023_06_29_Summary_SanLuisPotosi_SmartFactory_UseCase_Definition_Workshop*.pptx`,
`--2024_04_04_Summary_Subotica_SmartFactory_UseCase_Definition_Workshop*.pptx`,
`--2024_07_04_Summary_Timisoara_SmartFactory_UseCase_Definition_Workshop*.pptx`. Full
citations in `SKILL.md`'s `metadata.derived_from`.
