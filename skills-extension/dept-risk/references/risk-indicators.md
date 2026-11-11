---
type: Skill Reference
title: Risk indicators
description: The six registered risks with the source of each early indicator, how to read each indicator live, the trigger test and the kinds of gap that make an indicator unreadable.
resource: ../SKILL.md
status: draft
tags: [all, practice]
---

# Risk indicators

Register: `00-core/09-risks.md` (owner role: OD lead; review cadence monthly; read its `last-verified` date every time). Wording of
indicators and triggers is the register's. This file carries no readings: every value is read live at the source named
below, with its read date. Status wording per [`../SKILL.md`](../SKILL.md).

## R1. Missing operations concept for core systems (data platform, MSB, MDA/PDA)

| Item | Entry |
|---|---|
| Early indicator | Rollouts stalled; support tickets rising |
| Owner | OD lead |
| Trigger | Rollout blocked at a strategic plant |
| Where to read | Tool Overview list (one row per tool per plant); the portfolio's blocking points with owner and class (`12-portfolio.md`); the list of strategic plants in the landscape module |
| How to read it live | On the Tool Overview list, filter rollout status "ongoing" per tool and plant; intersect with the strategic-plant list. Then read the Blocker Register theme "Software, platform and licence" (use cases, plants) for blockers with owner. "Blocked" versus "in progress" may not be a field in the plant notes: confirm with the plant before calling it blocked |
| Unreadable part | Support tickets (no source system named). "Blocked" versus "in progress" is not a field in the plant notes |
| Status test | Triggered only if a strategic plant's rollout is recorded as blocked with a blocker owner |

## R2. Key-person / staffing gaps (open positions Asia, Americas)

| Item | Entry |
|---|---|
| Early indicator | Open roles unfilled; delivery slippage |
| Owner | OD lead |
| Trigger | Open role > `⟨n⟩` months |
| Where to read | The staffing plan the register points to ("Global staffing plan"); delivery slippage from the Scorecard targets-to-date |
| Context | Capability bottlenecks: read role capacity and planned open positions per region from the staffing plan (`capabilities.md`) |
| How to read it live | Needs a named staffing source for open roles; none may exist. Ask the OD lead role |
| Status test | *Unreadable* until n is set and a source for open roles is named. Slippage can be read from `metrics-scorecard` (use cases behind target-to-date) but slippage alone is not the trigger |

## R3. Limited internal IT knowledge (data platform, MDA/PDA)

| Item | Entry |
|---|---|
| Early indicator | Dependence on few individuals |
| Owner | OD lead |
| Trigger | Single point of failure identified |
| Where to read | A judgement by the OD lead role and the IIAE role, recorded at the COP (knowledge sharing via COP is the countermeasure); training records; the plant-instance map in `mi-data-availability` shows where flow evidence is thin |
| How to read it live | Check the plant-instance map for plants where flow evidence is thin; a thin evidence base is not by itself a single point of failure |
| Status test | *Unreadable* as a value. Treat a named single point of failure, once recorded, as Triggered |
| Note | Training-session counts and participants appear on COP slides; read the latest COP deck rather than quoting an older figure |

## R4. External tooling dependence (MES/ERP, licensing)

| Item | Entry |
|---|---|
| Early indicator | Blocked rollout awaiting an external decision |
| Owner | `⟨owner - to confirm⟩` (register) |
| Trigger | Decision delayed past plan |
| Where to read | Portfolio blocking points of class "external decision"; Blocker Register themes "IT security and approvals" and "Software, platform and licence" (count texts, use cases and plants live); the landscape module for MES (pilot status, ERP / S4HANA dependence) and MIL deployment state |
| How to read it live | Tool Overview list for the tool's rollout state per plant; the landscape module for the stated MES position (for example "on hold until value delivery cycle proven") with its date |
| Unreadable part | "Plan" date for each external decision is not recorded in the material read |
| Status test | Triggered if a blocked rollout has an external decision with a planned date that is past. No planned dates are recorded, so *Unreadable* |

## R5. Cyber Security / OT exposure on machine connection

| Item | Entry |
|---|---|
| Early indicator | Non-compliant connection detected |
| Owner | OD lead with Cyber Security |
| Trigger | Security gap on connected asset |
| Where to read | Cyber Security findings via the COP (technical Cyber Security aspects are a COP output); the sign-off standard is `to collect`; the Legacy Application List field *cyber-security status* |
| How to read it live | On the Legacy Application List, group by cyber-security status (for example Not started / In progress / Approved / Not applicable / blank) and by production criticality, and count live. Blank is a data gap, not a status |
| Reading note | The legacy-application status is about applications, not about connected machines. It is a related exposure signal, not the register's indicator. Do not equate "Not started" with "non-compliant" |
| Status test | Triggered when a security gap on a connected asset is reported. Absent such a report: *Unreadable* for connections (no detection source), and note the legacy-application figure as context. Rule: no external machine connection without sign-off |

## R6. Value not materializing from investment

| Item | Entry |
|---|---|
| Early indicator | Use-case impact below plan |
| Owner | DBVE |
| Trigger | Impact < target for the quarter |
| Where to read | Scorecard (utilization rate, integrated use cases), the savings roll-up in `bc-portfolio`, `bc-build` for the basis of a saving |
| How to read it live | Read tracked and proven savings separately from the saving rows (proven = SPRINT-reviewed) and the integrated use cases and machines against target from the Scorecard; the two savings figures are never added. Compare any older strategy-recap figure only as a dated reference, never as the current reading |
| Unreadable part | The quarter's impact target is not defined: utilization has "no fixed target - trend only", and the value delivery cycle is not captured in any system |
| Status test | *Unreadable* on target; the savings gap (tracked vs proven) is context, not the trigger. Do not turn tracked savings into a reading of impact |

## Overall picture (pattern, not a status)

In past readings the best-supported indicators were the ones backed by a list (tool rollouts, legacy-application
context, savings context). Indicators without a named source (staffing, dependence on few individuals) or without
planned dates (external decisions) tend to be unreadable. If that is still the case when you read, it is the first
finding the OD lead should receive, and its fix is a source or a rewrite of the register row, not a guess.
