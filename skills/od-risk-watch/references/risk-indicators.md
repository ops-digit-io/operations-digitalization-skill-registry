---
type: Skill Reference
title: Risk indicators
description: The six registered risks with the source of each early indicator, the snapshot reading available from the vault with its date, the trigger test and the gaps that make an indicator unreadable today.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Risk indicators

Register: `00-core/09-risks.md` (owner role: OD lead; review cadence monthly; last verified 2026-08-10). Wording of
indicators and triggers is the register's. "Snapshot" readings come from the work vault and are dated; they are not live
values. Status wording per [`../SKILL.md`](../SKILL.md).

## R1. Missing operations concept for core systems (data platform, MSB, MDA/PDA)

| Item | Entry |
|---|---|
| Early indicator | Rollouts stalled; support tickets rising |
| Owner | OD lead |
| Trigger | Rollout blocked at a strategic plant |
| Where to read | Tool Overview list (one row per tool per plant); the portfolio's blocking points with owner and class (`12-portfolio.md`); the strategic plants named in the landscape module (Carei, Mako, Subotica, Timisoara, Karben, Northeim and others) |
| Snapshot reading | Plant notes (aggregated 2026-11-05) record tool rollouts as "ongoing" at: MSB 4.0, 3 plants; QFPR, MIL 1.0 and Data Science Factory, 1 plant each. Which plants, and whether any is a strategic plant with the rollout blocked, must be read from the Tool Overview list. Blocker Register theme "Software, platform and licence": 5 texts on 5 use cases at 4 plants (export 2026-08-21) |
| Unreadable part | Support tickets (no source system named). "Blocked" versus "in progress" is not a field in the plant notes |
| Status test | Triggered only if a strategic plant's rollout is recorded as blocked with a blocker owner |

## R2. Key-person / staffing gaps (open positions Asia, Americas)

| Item | Entry |
|---|---|
| Early indicator | Open roles unfilled; delivery slippage |
| Owner | OD lead |
| Trigger | Open role > `⟨n⟩` months |
| Where to read | The staffing plan the register points to ("Global staffing plan"); delivery slippage from the Scorecard targets-to-date |
| Context | Capability bottlenecks: IIAE capacity is three roles; DBVE capacity is two roles; open positions are planned in Asia and Americas, Europe partly staffed (`capabilities.md`) |
| Snapshot reading | None available: no staffing source in the material read |
| Status test | *Unreadable* until n is set and a source for open roles is named. Slippage can be read from `od-scorecard-reporting` (use cases behind target-to-date at the 2026-08-10 read) but slippage alone is not the trigger |

## R3. Limited internal IT knowledge (data platform, MDA/PDA)

| Item | Entry |
|---|---|
| Early indicator | Dependence on few individuals |
| Owner | OD lead |
| Trigger | Single point of failure identified |
| Where to read | A judgement by the OD lead role and the IIAE role, recorded at the COP (knowledge sharing via COP is the countermeasure); training records; the plant-instance map in `od-data-availability-check` shows where flow evidence is thin |
| Snapshot reading | The flow corpus cannot speak for 16 of 33 plants (`od-data-availability-check/references/plant-instance-map.md`); a thin evidence base is not by itself a single point of failure |
| Status test | *Unreadable* as a value. Treat a named single point of failure, once recorded, as Triggered |
| Note | A training-session count of 40 sessions and 80 participants for 2023 exists on a COP slide (ODEC Facts, staging, 2024#1 COP deck); no current figure |

## R4. External tooling dependence (MES/ERP, licensing)

| Item | Entry |
|---|---|
| Early indicator | Blocked rollout awaiting an external decision |
| Owner | `⟨owner - to confirm⟩` (register) |
| Trigger | Decision delayed past plan |
| Where to read | Portfolio blocking points of class "external decision"; Blocker Register themes "IT security and approvals" (3 texts, 3 use cases, 3 plants) and "Software, platform and licence" (5 texts); the landscape module: MES in two pilot plants on hold, ERP / S4HANA dependent, MIL not deployed |
| Snapshot reading | MES 1.0 recorded as available at 1 plant in the plant notes (2026-11-05); the landscape module (2026-08-10) records MES as "on hold until value delivery cycle proven" |
| Unreadable part | "Plan" date for each external decision is not recorded in the material read |
| Status test | Triggered if a blocked rollout has an external decision with a planned date that is past. No planned dates are recorded, so *Unreadable* |

## R5. Cyber Security / OT exposure on machine connection

| Item | Entry |
|---|---|
| Early indicator | Non-compliant connection detected |
| Owner | OD lead with Cyber Security |
| Trigger | Security gap on connected asset |
| Where to read | Cyber Security findings via the COP (technical Cyber Security aspects are a COP output); the sign-off standard is `to collect`; the Legacy Application List field *cyber-security status* |
| Snapshot reading | Legacy Applications (268 notes, 2026-11-05): cyber-security status Not started 172, Not applicable - standalone 15, Approved 7, In progress 3, no value 71. Production criticality: Critical 109, Moderate 34, Minimal 23, not applicable 61, no value 41 |
| Reading note | The legacy-application status is about applications, not about connected machines. It is a related exposure signal, not the register's indicator. Do not equate "Not started" with "non-compliant" |
| Status test | Triggered when a security gap on a connected asset is reported. Absent such a report: *Unreadable* for connections (no detection source), and note the legacy-application figure as context. Rule: no external machine connection without sign-off |

## R6. Value not materializing from investment

| Item | Entry |
|---|---|
| Early indicator | Use-case impact below plan |
| Owner | DBVE |
| Trigger | Impact < target for the quarter |
| Where to read | Scorecard (utilization rate, integrated use cases), the savings roll-up in `od-portfolio-and-savings-analysis`, `od-benefit-calculation` for the basis of a saving |
| Snapshot reading | `od-context` records EUR 2.38 M tracked and EUR 653 k proven (SPRINT review: 19 of 553 saving rows) and says the two are never added. ODEC strategy recap (slide dated 2025-03-27, ODEC facts staging): 2024 target savings EUR 1.5 M over 59 use cases; actual savings EUR 805 k; target integrated machines 200, actual 145 |
| Unreadable part | The quarter's impact target is not defined: utilization has "no fixed target - trend only", and the value delivery cycle is not captured in any system |
| Status test | *Unreadable* on target; the savings gap (tracked vs proven) is context, not the trigger. Do not turn tracked savings into a reading of impact |

## Overall picture today (honest)

Of six indicators, none is fully readable from a live source in the material read. The best-supported are R1 (tool
rollouts), R5 (legacy-application context) and R6 (savings context). R2 and R3 have no source; R4 has no planned dates.
That is the first finding the OD lead should receive, and its fix is a source or a rewrite of the register row, not a
guess.
