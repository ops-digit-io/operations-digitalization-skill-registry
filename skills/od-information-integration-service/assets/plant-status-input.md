---
type: Skill Asset
title: Plant status input
description: One-page input a plant fills for the equipment-integration line of an ODEC status slot - the plant's numbers with sources and dates, the open blockers, the eCR state and the asks - built from the fields the ODEC KPI slides actually track.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, lane]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Plant status input

The ODEC (Operations Digitalization Exchange Call) slides track, per region, **equipment
integration "today (plan)"** and **use case development "today (plan)"**,
the **eCR status** of the connectivity roadmap, and a regional **equipment integration
roadmap status** with "done in site", "done remote" and "pending" per plant. These are the fields a plant is asked for. This form collects them in one place
before the call. Source of the slide fields: `ODEC Facts` staging notes (AI-extracted, not
verified; open the slide before relying on it).

Fill from the live Machine List and Tool Overview, not from memory. The monthly figures
belong to the Equipment Integration report (`OD-Report-Equipment_Integration`, owned by the
lane); this form feeds it, it does not replace it.

| Field | Value | Source and date |
|---|---|---|
| Plant, region | | |
| Prepared by (role), date | | |
| Machines integrated: today / plan for the year | | Machine List; plan from the roadmap |
| Of those, integrated since the last call | | integration dates in the Machine List |
| Machines `INTEGRATION ONGOING` | | Machine List |
| Machines with no status recorded (not "not integrated") | | Machine List |
| Use cases in development: today / plan | | use case list |
| eCR state for the current wave: not started / in preparation / uploaded / approved / in implementation | | eCR system |
| Wave or project reference | | Machine List `project_reference` |
| Integration mode for the last machines: in site / remote | | slide wording "done in site" / "done remote" |
| Open blockers (kind, count; see the blocker table in `od-equipment-integration`) | | |
| Cyber Security / OT sign-off pending for which machines | | |
| Budget status | | |
| Asks to the lane or to the department | | |

Rules that keep the line honest:

1. Quote counts with their export date; a count without a date is not a status.
2. "Blank status" is reported as such, not as "not integrated".
3. A machine is `INTEGRATED` only after its acceptance test passed
   (`od-acceptance-test`); do not count a machine that has only been connected.
4. The department's target figures belong to the lane's metrics table in
   [`SKILL.md`](../SKILL.md); copy the target from there and leave the actual to the plant.
