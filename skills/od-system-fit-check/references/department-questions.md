---
type: Skill Reference
title: Department questions
description: "Ready-made questions to put to the requesting department per verdict and per open criterion."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [invest-screen, gate, department-package]
derived_from:
  - "Department knowledge base, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `investment-checking.zip/reference/department-questions.md` (the master).

# Department questions — what OD raises per involved item

The questions OD brings to the invest review / ODEC / COP. Grouped by concern; ask only the ones an item leaves open. Phrase them as help ("so we can connect this cleanly"), not as gatekeeping.

## Involvement & ownership
- Does this produce or consume production data, or need any network/PLC connection? (If yes, OD is involved.)
- Which department owns the row, and who owns the **digital / software part** after go-live?
- Is anyone from OD already aware, or is this the first we see it?

## Business case & fit
- What is the measurable value (saving / lead-time / risk / customer-mandatory) and the rough payback?
- Which roadmap (plant or central) does it sit on?
- What is the kill criterion — when would we stop?
- Does it reinforce a bet (data platform / MSB+CyberSec / MES-pilot) or hit a non-bet (MES rollout, EMS, energy/facility ownership, tool proliferation)?

## Compounding & standardisation
- Is this reusable across plants, or a one-off? Could it be a standard use case / signal model?
- What interface does the data use — standardised (OPC UA / MQTT / MSB / data platform) or proprietary?
- Does it expose endpoints (FTP, own DB, web UI) that **duplicate or compete with** our internal connectors?

## Complexity & proof
- What must be **proven first**? Can we do a small PoC before committing org-wide?
- What new tool / vendor / operational burden does it add, and who operates it?
- Is there a simpler, lower-footprint way to get 80% of the value?

## Software / IT footprint & cyber (the blind spot)
- Does it include or require a **PC / server / embedded controller**? Who patches it?
- What **software / framework / license** runs on it — version, vendor, EOL, on an approved list?
- Does it need a **Cyber Security** review or sign-off before any external connection?
- What does it connect to (shopfloor VLAN / corporate LAN / internet), and does it need firewall/segmentation?

## Cross-region interlock
- Is a similar Energy / ME / IT project running elsewhere that this should align with?
- Will it need the data platform / IIoT Edge / MSB / edge devices later — should OD co-own from the start rather than retrofit?
- Does it risk standing up a **parallel data path or silo** that we'll have to reconcile?
