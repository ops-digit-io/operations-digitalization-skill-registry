---
type: Skill Asset
title: Existing system worksheet
description: Short worksheet for the fit check when the plant may already run a legacy application or a rolled-out tool that covers the need - what it is, how reachable and supported it is, and which of reuse, redesign or escalate follows.
resource: ../SKILL.md
status: draft
tags: [all, practice]
---

# Existing system worksheet

Fill alongside [`system-fit-check.md`](system-fit-check.md) when the need is outside every
lightweight tool, or when a use case names a tool the plant row does not show as available
([`plant-tool-availability.md`](../references/plant-tool-availability.md)). Five minutes. Fields
come from the Legacy Application List columns, so the answers can be compared with the
record; where the record is blank, write "not recorded" and name who can answer.

## 1. The need, restated

| | |
|---|---|
| Plant | |
| The need in one sentence, independent of the requester's wording | |
| Tool boundary crossed (name the "is not" line) | |

## 2. The candidate existing system

| Item | Record (Legacy Application List) | Plant answer |
|---|---|---|
| Application name and version | | |
| Category (e.g. custom MES, custom SCADA, laboratory software, camera system configuration) | | |
| Functional mapping | | |
| What it does today (one line) | | |
| Production criticality / customer impact | | |
| Network status (standalone, IT, OT/IT, OT) | | |
| Cyber-security status | | |
| Support concept (internal, external contract, maintenance and run concept) | | |
| Licence (unknown / none / local / OESL) | | |
| Supplier software status | | |
| Interfaced machines | | |
| Number of deployments; scaling potential | | |

## 3. Reading

| If | Then |
|---|---|
| The application covers the need and is supported | Verdict "fits the lean footprint", with the existing application named as the covering system; replacing or changing it goes to `od-decision-routing` (tool or system rollout row) |
| It covers part of the need | Redesign the request onto the lighter tool for the rest; name what stays on the legacy application |
| It is critical, standalone and has cyber-security "not started" | Touching it triggers the Cyber Security / OT gate (`od-cybersec-gate`); do not plan a connection yet |
| Support concept blank and criticality critical | Ask Plant ME / Plant IT who supports it before anything is promised |
| No candidate, and the need crosses a boundary | Escalate as an exception, as in the main check |

## 4. Result

| | |
|---|---|
| Verdict (the three in the main check): fits / redesign onto lighter tool / escalate | |
| Named next step and owner (role) | |
| Records consulted and their export dates | |
