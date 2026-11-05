---
type: Skill Reference
title: Legacy application position
description: Aggregate of the 268 legacy applications by licence, support concept, criticality, cyber-security status and network status - what a standard system will meet on the shop floor and what is unknown about it. Open it when a kit has to coexist with, or replace, an installed application.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Legacy application position

Source: the 268 notes in vault `Graph/Legacy Applications` (SharePoint list `LegacyApplication-List`, export of 2026-08-24), fields and "Support and licensing" lines counted by script on 2026-11-05. Use as an aggregate, not note by note. The list holds the applications plants run beside the standard tools (mostly programming, laboratory, configuration and camera software), not a catalog of recommended systems.

Basic counts (application category, licence and support concept) also appear in `od-requirements-breakdown`, `references/legacy-system-assessment.md`, and agree with these. What follows is what that file does not carry.

## Criticality and cyber-security

| Production criticality | Applications |
|---|---:|
| Critical | 109 |
| Moderate | 34 |
| Minimal | 23 |
| NA | 61 |
| not recorded | 41 |

| Cyber-security status | Applications |
|---|---:|
| Not started | 172 |
| NA - Standalone | 15 |
| Approved | 7 |
| In Progress | 3 |
| not recorded | 71 |

- Of the **109 critical** applications: cyber-security `Not started` 70, `In Progress` 2, `Approved` 1, not recorded 36. Licence `unknown` 38, `Local License Available` 35, no licence required 30, `OESL license required` 6. Support concept: Internal Support 47, Maintenance & Run Concept 14, External Support Contract 11, **not recorded 37**.
- Network status: Standalone 94, IT 65, OT/IT 25, OT 21, not recorded 63. Standalone cases dominate "Not started" (74), but 49 on the IT network and 23 on OT/IT are also "Not started".
- Largest categories: PLC programming / configuration 73 (38 critical), laboratory software 52 (23 critical), equipment configuration 33, camera system configuration 25 (14 critical), custom SCADA 15, printer 12, quality software 10, internal Mendix apps 9, custom MES 8. Category not recorded on 15.
- Licence `unknown` is highest in custom SCADA (12 of 15), laboratory software (30 of 52), PLC programming (34 of 73).
- Suppliers with the most entries: Keyence 31, Siemens 18, internal 13, ContiTech 12, Mitsubishi 11, Hexagon 8; supplier not recorded on 67.
- The list holds 136 notes with no documentation gap; 114 lack a support concept, 71 lack a cyber-security status.

## What this means for a standard system

1. A kit that lands on a machine usually meets **PLC programming software** (73 entries) or **equipment configuration** (33). The kit cannot assume the plant holds a licence: for 34 of the 73 PLC programming entries the licence position is `unknown`. Ask before ordering (`od-equipment-integration`: no PLC program, no connection).
2. A kit that replaces a plant application touches **critical** software in about four of ten cases (109 of 268); never propose replacement without the support concept and cyber-security status of that application. Where the field is empty, the answer is "unknown", and an unknown stays in the entry as ⟨missing⟩.
3. **Cyber-security status is "Not started" for 172 of 268**; a connection that routes through one of them meets the external-connection sign-off, which is human-only (`catalog-guardrails` G7, `od-cybersec-gate`).
4. Custom MES (8) and custom SCADA (15) overlap with what the footprint rule excludes (MES rollout on hold). Treat them as `od-system-fit-check` cases, never as ordinary kits.

## Open

- ⟨Which plant runs which application⟩ is in the individual notes (a plant field), not in this aggregate - read the note when a specific plant is concerned.
- ⟨Whether "licence unknown" means not asked, or not held⟩ - plant IT, OD lead.
