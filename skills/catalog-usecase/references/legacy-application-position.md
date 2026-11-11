---
type: Skill Reference
title: Legacy application position
description: Guidance, no figures - how to read the legacy application list by licence, support concept, criticality, cyber-security status and network status, and what a standard system will typically meet on the shop floor. Open it when a kit has to coexist with, or replace, an installed application.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Legacy application position

This file holds **no counts**. Source to read live: knowledge base `Graph/Legacy Applications` (notes from the SharePoint list
`LegacyApplication-List`; fields and "Support and licensing" lines). Export it with `od-sharepoint-list-export` and
aggregate; use it as an aggregate, not note by note. The list holds the applications plants run beside the standard tools
(mostly programming, laboratory, configuration and camera software), not a catalog of recommended systems. Basic
aggregation by category, licence and support concept is also described in `od-requirements-breakdown`,
`references/legacy-system-assessment.md`.

## Fields to read

| Field | Values to expect | Reading rule |
|---|---|---|
| Production criticality | Critical, Moderate, Minimal, NA, not recorded | "not recorded" is its own group, never "Minimal" |
| Cyber-security status | Not started, In Progress, Approved, NA - Standalone, not recorded | "Not started" can dominate; a blank is unknown |
| Licence | unknown, Local License Available, no licence required, OESL license required | `unknown` can mean not asked, not "not held" |
| Support concept | Internal Support, Maintenance & Run Concept, External Support Contract, not recorded | A critical application with no support concept is a finding |
| Network status | Standalone, IT, OT/IT, OT, not recorded | Standalone does not imply cyber-security clearance |
| Category / supplier | PLC programming / configuration, laboratory software, equipment configuration, camera system configuration, custom SCADA, custom MES, printer, quality software, internal Mendix apps | Category or supplier can be blank; count blanks |

Useful live cuts: critical applications by cyber-security status, licence and support concept; licence `unknown` by category;
cyber-security `Not started` by network status (IT and OT/IT entries that are `Not started` matter most).

## What this means for a standard system

1. A kit that lands on a machine usually meets **PLC programming software** or **equipment configuration**. The kit cannot
   assume the plant holds a licence: in the PLC programming category the licence position is often `unknown`. Ask before
   ordering (`od-equipment-integration`: no PLC program, no connection).
2. A kit that replaces a plant application can touch **critical** software; never propose replacement without the support
   concept and cyber-security status of that application. Where the field is empty, the answer is "unknown", and an unknown
   stays in the entry as ⟨missing⟩.
3. Cyber-security status is often "Not started"; a connection that routes through such an application meets the
   external-connection sign-off, which is human-only (`catalog-usecase` G7, `od-cybersec-gate`).
4. Custom MES and custom SCADA applications overlap with what the footprint rule excludes (MES rollout on hold). Treat them as
   `od-system-fit-check` cases, never as ordinary kits.

## Open

- ⟨Which plant runs which application⟩ is in the individual notes (a plant field), not in the aggregate - read the note when
  a specific plant is concerned.
- ⟨Whether "licence unknown" means not asked, or not held⟩ - plant IT, OD lead.
