---
type: Skill Asset
title: Epic and stories example
description: A filled epic for OEE at Mako that passes every check in check_epic.py; read it before the blank.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [requirements, epic, example]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# EPIC-C07-MAK · Mako · OEE Calculation

## Background — what this is used for

**Today.** The shift leader at Mako walks the vulcanization area at 06:00 and again at 14:00,
reads the piece counter and the running-hours meter off each of the six presses, and writes
them on a clipboard. The numbers are typed into a spreadsheet the following morning, so the
Monday OEE figure is available on Wednesday. Downtime reasons are reconstructed from memory
in the same pass.

**The moment of use.** The 07:00 shift handover, where the outgoing and incoming shift leader
agree what ran badly and what the incoming shift should watch.

**The decision it changes.** With yesterday's availability split by press at 07:00 instead of
two days later, the incoming shift leader assigns the maintenance technician to the press
that actually lost time, rather than to the one that was loudest. Maintenance estimates two
misdirected interventions per week at roughly 40 minutes each.

**Why now.** Two presses were relocated from Vac in March and the manual counter round now
takes longer than the handover slot allows, so it is being skipped on late shifts.

**What this is not for.** Not quality or scrap reporting — that sits in the Manual Quality
Data epic. Not a plant-level OEE roll-up for management review.

## Epic statement

**As** the vulcanization shift leadership at Mako, **we want** availability, performance and
downtime reasons per press available at the 07:00 handover, **so that** the incoming shift
leader assigns maintenance to the press that lost the most time yesterday instead of
reconstructing it from memory.

## Epic frame

| | |
|---|---|
| Capability epic | OESL-OEE_Calculation |
| Process epic | OESL-Rubber-Vulcanization |
| Cluster | C07 |
| Plant / machines | Mako · presses VP-01…VP-06 (EQ 41221–41226) |
| Lane | use-case |
| Requirement | REQ-MAK-2026-014 |
| Owner | A. Nagy, Digital Business Value Engineer |
| Value (epic total) | EUR 34,000 2026 · ESTIMATION |
| Standard or specific | standard with deltas — adopt Timisoara's OEE build; delta is the six-press area view |

## Scope

**In.** Availability, performance and downtime reason per press, for the vulcanization area.
**Out.** Quality rate, scrap, plant roll-up, any press outside vulcanization.

## User stories

### US-01 · Counter and running hours without the clipboard round

**As** the vulcanization shift leader at Mako, **I want** the piece count and running hours
per press for the finished shift, **so that** the 06:00 walk stops being the only way the
number exists and the late shift stops skipping it.

**Background.** The counters are already on the PLC and two of the six presses are on the edge
platform from the Vac relocation. This story delivers on those two first and is the reason the
epic is not blocked end to end.

**Signals**

| Signal | Direction | Exists? | Unit | Collection |
|---|---|---|---|---|
| TotalPartCounter | in | yes 8f2a-… | pcs | transition |
| MachineRunningTime | in | yes 3c91-… | s | sample @ 10s |
| MachineState | in | no — VP-03…06 await integration | enum | transition |

**Acceptance criteria**

1. **Given** a shift has ended, **When** the shift leader opens the area view at 07:00,
   **Then** the piece count per press matches the PLC counter exactly and is at most
   5 minutes old.
2. **Given** a press was stopped for the whole shift, **When** the view is opened,
   **Then** it shows 0 pieces and 0 running hours rather than a blank.
3. The shift leader completes the 07:00 handover without the clipboard round for
   10 consecutive shifts.

**Blockers.** signal missing — VP-03…06 not integrated · owner IIAE · needed by 2026-10-01
**Value.** carried at epic level
**Depends on.** nothing
**Definition of done.** Development NOT STARTED · Implementation NOT STARTED · Handover NOT STARTED

### US-02 · Downtime reason captured at the press, not from memory

**As** the press operator at Mako, **I want** to pick a downtime reason on the HMI when a stop
runs past two minutes, **so that** the shift leader sees why a press stopped instead of
reconstructing it at handover the next morning.

**Background.** There is no reason code capture today; the reason list exists only in the
maintenance team's heads and differs between the two shifts.

**Signals**

| Signal | Direction | Exists? | Unit | Collection |
|---|---|---|---|---|
| MachineState | in | no — VP-03…06 await integration | enum | transition |
| DowntimeReasonCode | out | no — to register | enum | per event |

**Acceptance criteria**

1. **Given** a press has been stopped for more than 120 seconds, **When** the operator
   acknowledges on the HMI, **Then** the selected reason is stored against that stop.
2. **Given** a stop was not acknowledged, **When** the shift ends, **Then** it appears as
   "unclassified" and is counted, not dropped.
3. Operators classify at least 80% of stops longer than 2 minutes across 10 consecutive shifts.

**Blockers.** method undefined — the reason code list is not agreed · owner DBVE · needed by 2026-09-15
**Value.** carried at epic level
**Depends on.** US-01 for the state signal
**Definition of done.** Development NOT STARTED · Implementation NOT STARTED · Handover NOT STARTED

## Epic acceptance

All stories accepted, plus: the OEE build is registered against the C07 cluster template with
Mako's deltas recorded, and the clipboard round is stopped rather than run in parallel.

## Open questions

| Question | Who answers | Needed by |
|---|---|---|
| Is the Timisoara downtime reason list adoptable as-is? | Timisoara DBVE | 2026-09-15 |
