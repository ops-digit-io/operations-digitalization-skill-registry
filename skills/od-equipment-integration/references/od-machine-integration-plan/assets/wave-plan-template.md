---
type: Skill Asset
title: Wave plan template
description: Template for one integration wave - machine list and CV fields, machine type and route, cost line, plant status row, readiness check and barrier log; fill with placeholders, never with remembered numbers.
resource: ../procedure.md
status: draft
tags: [information-integration-service, practice, template]
---
# Wave plan - `<plant or area>` · `<wave id>`

| | |
|---|---|
| **Prepared by / date** | `<role>` · `<date>` |
| **Draft status** | Draft for OD lead and Plant ME; nothing here connects or approves anything |
| **Budget class** | `<small / medium / large>` (limits `<look up>`) |
| **Kick-off date / team staffed** | `<date>` · `<yes / no, roles>` |

## 1 Machine list and CV (one row per machine)

| Machine id | Type (vendor, PLC family, protocol) | Known type? | PLC program available, under own control | Program version history | Network drop | Cyber-security update status | Layout stable? | Use case waiting |
|---|---|---|---|---|---|---|---|---|
| `<id>` | `<type>` | `<known / unknown>` | `<yes / no / partial>` | `<>` | `<>` | `<>` | `<yes / no>` | `<>` |

Check: unknown types in this wave `<n>` (must be at most one).

## 2 Route and cost per machine type

| Machine type | Data classes | Route | Edge needed? | Time and cost lines (hardware, software, IT/OT) | Compatibility checked? |
|---|---|---|---|---|---|
| `<type>` | `<transactional / time series>` | `<native / aggregation server / edge / low-cost / custom connector>` | `<y / n and why>` | `<lines, with source>` | `<y / n>` |

## 3 Plant status row (weekly micro-process)

| Plant | Week of OT call | Week of request preparation | Week of upload | Status | Call for action (week, owner) |
|---|---|---|---|---|---|
| `<plant>` | `<cw>` | `<cw>` | `<cw>` | `<green / yellow / red>` | `<>` |

## 4 Readiness

| Criterion | Result | Owner if open |
|---|---|---|
| Machine list complete enough | `<>` | `<>` |
| Layout stable | `<>` | `<>` |
| Controllers: no blocking patch or approval | `<>` | `<>` |
| IT platform ready | `<>` | `<>` |
| Team staffed, IT and OT assessments scheduled | `<>` | `<>` |
| Compatibility checked | `<>` | `<>` |
| Operations concept named | `<>` | `<>` |
| Cyber Security package started | `<>` | `<>` |

## 5 Barrier log

| Barrier (class) | Machines affected | Use cases waiting | Decision needed, forum | Owner, due week | Cost of non-decision (portfolio source, read date) | Status |
|---|---|---|---|---|---|---|
| `<>` | `<>` | `<>` | `<>` | `<>` | `<value or "unquantified">` | `<>` |

## 6 Hand-over

Next: `od-capital-request` (list, route, cost lines, open items) · `od-equipment-integration` Route B per
machine · `od-equipment-integration` for rows in section 5 · next-wave recommendation `<>` · training for
self-service `<>`.
