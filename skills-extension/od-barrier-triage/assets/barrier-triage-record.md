---
type: Skill Asset
title: Barrier triage record
description: The record of one blocked machine - facts, demand, ladder result, root-cause class, difficulty tier, exit, owner, wait state and the log line.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice, template]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Barrier triage - ⟨machine or group⟩ · ⟨plant⟩

| | |
|---|---|
| **Triage by / date** | ⟨role⟩ · ⟨date⟩ |
| **Triggered by** | ⟨assessment finding · Route B dead end · recorded blocker text · Lane 1b mismatch⟩ |
| **Draft status** | Draft for the IIAE and Plant ME; nothing here connects or approves anything |

## 1 Facts

| Field | Value |
|---|---|
| Machine / equipment id | ⟨⟩ |
| PLC vendor · model · part number | ⟨or ⟨unknown⟩⟩ |
| Network protocol | ⟨or ⟨unknown⟩⟩ |
| Integration status recorded | ⟨INTEGRATED · NOT INTEGRATED · ONGOING · none⟩ |
| Planned method recorded | ⟨edge · aggregation server · evaluation ongoing · none⟩ |
| Cabinet and cabling, usable network drop | ⟨⟩ |
| Plant IT / ME responsiveness | ⟨⟩ |
| PLC program available and under own control | ⟨yes · no · partial⟩ |
| Recorded blocker text (verbatim) | ⟨⟩ |

## 2 Demand

Use case(s) waiting for this machine's data: ⟨ids and status⟩. None waiting: close here as "parked, no
demand".

## 3 Ladder result

| Rung | Checked | Result |
|---|---|---|
| 1 Already on an OPC-UA server | ⟨⟩ | ⟨⟩ |
| 2 Vendor-specific connector (Engel, Piovan, Keyence, Zwick, Optris, Multicon) | ⟨⟩ | ⟨⟩ |
| 3 File drop (FTP, SMB, CSV) | ⟨⟩ | ⟨⟩ |
| 4 HTTP / SOAP | ⟨⟩ | ⟨⟩ |
| 5 Serial | ⟨⟩ | ⟨⟩ |
| 6 Signal on a neighbouring PLC | ⟨⟩ | ⟨⟩ |
| 7 Added sensor or camera | ⟨⟩ | ⟨⟩ |
| Unwritten branch or product mismatch (`fallbacks` items 6, 7) | ⟨⟩ | ⟨⟩ |

## 4 Classification

| | |
|---|---|
| **Root-cause class** | ⟨C1 information · C2 owner/window/will · C3 security gate · C4 platform · C5 no route · C6 legacy hardware · C7 data model⟩ |
| **Behind it (next class)** | ⟨⟩ |
| **Difficulty tier** | ⟨position in the ranking of `barrier-classes`; say if the raw integration rate would suggest otherwise⟩ |
| **Evidence for the class** | ⟨the answer to the identifying question⟩ |

## 5 Exit

| | |
|---|---|
| **Exit** | ⟨roadmap · strategy · substitution⟩ |
| **Owner (role)** | ⟨⟩ |
| **Forum** | ⟨ODEC for strategy and rollout · COP for technical⟩ |
| **Wait state** | ⟨awaiting program · line stop · Cyber Security sign-off · rollout decision · connector development · investment decision⟩ |
| **Look again on** | ⟨date⟩ |
| **Gate to record as dependency** | ⟨eCR · Cyber Security · IT demand · tool rollout⟩ |
| **Cost to size** | ⟨hand to `od-investment-input`: yes/no, options⟩ |

## 6 Log line (copy into the machine record and the assessment protocol, section 5)

`⟨machine⟩ | ⟨class⟩ | ⟨exit⟩ | ⟨owner role⟩ | ⟨dependent use cases⟩ | ⟨date⟩`

## 7 Still open

⟨What is unknown, who can supply it⟩
