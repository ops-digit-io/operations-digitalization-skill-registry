---
type: Skill Asset
title: Maturity assessment record
description: The as-is profile of one machine, system or application on the 16 focus areas - level, evidence grade, source, owner - with plausibility notes; a draft for the DBVE or IIAE to accept.
resource: ../procedure.md
status: draft
tags: [practice, maturity, template, draft]
---
# Maturity assessment - ⟨object⟩ · ⟨plant⟩

| | |
|---|---|
| **Object** | ⟨machine and controller · system · application⟩, ⟨id or name⟩, ⟨type or group if several are identical⟩ |
| **Question this profile serves** | ⟨pick a standard system (1b1) · data check (22) · tool decision (32) · connector design (3b4)⟩ |
| **Use case or request behind it** | ⟨id and status⟩ |
| **Assessed by / date** | ⟨role⟩ · ⟨date⟩ |
| **Reviewed with** | ⟨plant owner role · IT/OT role⟩ |
| **Draft status** | Draft for the DBVE or IIAE; nothing here connects, configures or approves anything |

Level: the number and label of the level **in use today**, or `unknown` or `n/a` (with reason) or `mixed` (then split the row).
Evidence: **S** seen, **T** told, **A** assumed. Only S and T feed a route signal.

## 1 Profile

| Area | Level (as-is) | Evidence S/T/A | Source and read date | Owner role | Note (potential, contradiction, open) |
|---|---|---|---|---|---|
| F1 System familiarity | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨assets and products separately⟩ |
| F2 Communication capabilities | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| F3 Degree of intelligence | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| F4 Localization | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| F5 Mobility | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| F6 Degree of automation | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| F7 Information provision | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| F8 Human-machine interface | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| F9 Communication interfaces | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨network segment, usable drop⟩ |
| F10 Communication protocols | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨per interface; custom drivers and their owner⟩ |
| F11 Data collection | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨rate, delay, source time stamp⟩ |
| F12 Information storage | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨system of record; behaviour on network failure⟩ |
| F13 Information processing | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨edge owner⟩ |
| F14 Data analytics | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨tool, who builds and runs⟩ |
| F15 Control structure | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨who schedules, what is local⟩ |
| F16 Information-model continuity | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨naming standard, model owner⟩ |

## 2 Plausibility notes

⟨Combinations that contradict their prerequisites (`drivers-and-dependencies`, section 4), and what was found out: rating error, hidden gateway,
manual step.⟩

## 3 Unknowns

| Area | Question | Who can answer (role) | By |
|---|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |

## 4 Handoff

Profile goes to ⟨skill of the step⟩; driver and gap sheet: `driver-and-gap-sheet.md`.
Next refresh when: ⟨firmware, retrofit, rollout or tool status changes · date⟩.
