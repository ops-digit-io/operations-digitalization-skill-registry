---
type: Skill Reference
title: Screening method
description: "Whole-list screen of the MPEE Invest and Cost Planning list: involvement lexicon, classification OD-owned / touching / interlock / not, the de-noise rule."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [invest-screen, gate, department-package]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/30-skills/investment-checking.zip/reference/screening-method.md, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `investment-checking.zip/reference/screening-method.md` (the master).

# Screening method — pull the list, classify every row

## Where the list lives (source of truth)

- **MPEE Invest & Cost Planning** SharePoint list, MPEE site `team_10066743`
  `.../Lists/MPEEInvest_Cost_Planning/AllItems.aspx` — list GUID `8205d325-ec43-426e-af37-bec921c5ba11`.
  Intake runs through Power Automate pre-approval + central-approval flows.
- The list is the **single source of truth**. Link to it; do **not** copy its rows into any OD repo register or module markdown (that creates a stale duplicate). A dated analysis/screening report is fine; a parallel register is not.

## Getting the data

1. Preferred: read the current list live (SharePoint). 
2. Fallback: the periodic CSV export `MPEE-Invest_Cost_Planning.csv` (in the process owner's OneDrive `Documents/Dokumente/`). Note: saved list-view exports prepend a large `ListSchema=…` block — the real CSV starts at the header row `"ID","Title","Description",…`. Parse from there.
3. **Always record the snapshot date** of whatever you used, and state it in the output. An export more than ~2 weeks old should be called out as possibly stale.

## Columns you rely on

`ID · Title · Description · Project Responsible · Status · Source · Year · Budget Quarter · Cluster · Location · Department · Category · Priority · Status Description · Estimated GPA/RPE/Savings · Invest Cost–Timing · Approval flow fields · eCR Number`

Statuses seen: `IDEA · ONGOING · INVESTMENT APPROVED (TO LAUNCH ECR) · FINISHED (ECR APPROVED) · DECISION REQUEST · POSTPONED · CANCELLED · REJECTED`. Treat `CANCELLED`/`REJECTED` as dead (record but don't gate); everything else is live.

## Classify EVERY row

Assign one class per row and show the trigger:

1. **OD-owned** — `Department = OPERATION DIGITALIZATION`.
2. **OD-touching** — any department, but the text hits the **involvement lexicon** below.
3. **Cross-region interlock** — Energy/`FACILITY & GREEN OPERATIONS`, `MANUFACTURING ENGINEERING`, or `IT` items in a region that will need, or will parallel, an OD platform (the data platform / IIoT Edge / MSB / edge devices / traceability / a shopfloor data path). These get flagged for **co-ownership**, not just a comment.
4. **Not involved** — no signal. Count them, then drop from the working set.

### Involvement lexicon (signal words → OD is likely involved)

- **Data / analytics:** data, database, SQL, dashboard, analytic, reporting, traceability, KPI, historian, cloud, data platform, data layer (source rows may still say MDL: match it as a keyword, read it as the data platform).
- **Connectivity / OT:** PLC, PLC upgrade, IIoT, edge, MSB, OPC, MQTT, gateway, DataFeed/Softing, network integration, switch, access point, optical backbone, ethernet, FTP, interface, integration.
- **Software / endpoints:** software, license/licence, framework, PC, workstation, server, Windows, firmware, app, SCADA, MES, control system, controller, image/vision, camera, scanner, laser control, marking system, Keyence/Cognex/Precitec/KBA, TIA Portal.
- **Cyber / IT infrastructure:** firewall, VPN, DNS, active directory, backup server, UPS (server room), video surveillance server, HR/time-attendance system (Interflex), label software.
- **Automation with a digital tail:** poka-yoke with vision/PLC, retrofit of a controller/camera, test bench with automated data capture, "local AI solution".

A row hitting **any** connectivity, software/endpoint, or cyber signal is OD-touching **even if the owning department is ME/PPI/FM/Quality/R&D** — that is the blind spot this screen closes. Category `DATA PROCESSING` and Department `IT` are automatic candidates; scan them fully.

### De-noise rule — IT commodity lifecycle is NOT OD involvement

Validated against the live list (Aug 2026): a naive lexicon sweep pulls in ~34 `IT` rows, but most are **commodity IT lifecycle** with no OD footprint. Downgrade to *not-involved (IT-owned commodity)* when the item is a like-for-like refresh of: laptops / desktops / CAD workstations, UPS, multifunction printers, DNS / backup / file / AD servers, generic switch/AP end-of-life swaps, firewalls, wireless controllers. These are Central IT lifecycle — note the count, don't gate them.

**Keep them OD-relevant** only when they touch the shopfloor/OT data path or an OD platform, e.g.: a **PLC core switch** or **OT network** segment, an **optical backbone** feeding production, **MSB expansion**, **edge devices**, a **video-surveillance / QIP / historian server** that will hold or route production data, or a **time-attendance/HR system (Interflex)** only insofar as it exposes an integration OD would be asked to build. When unsure, keep it in and mark the involvement ⟨to confirm⟩ — under-flagging is the expensive error.

Likewise, downgrade pure mechanical equipment rows whose only "signal" is an incidental word (e.g. a laser *welding* machine with no data/PC/endpoint, a mold-cleaning unit, a voltage regulator, a server-leasing swap) to *not-involved*, **unless** they carry a controller/PC, vision/measurement data, marking/traceability output, or a network connection — those stay in.

**Match plurals and label-only bumps.** When applying the commodity filter, make the terms plural-tolerant: `laptop(s)`, `switch(es)`, `desktop(s)`, `server(s)` etc. must all be caught (a naive `\blaptop\b` misses "Laptops" / "Core Switches" and lets commodity rows leak into the shortlist — this was a real miss on the Aug-2026 data). Also treat a "label software version upgrade" and a like-for-like "server equipment replacement / leasing" as commodity unless they touch an OD platform or OT data path.

## Group the output by region (Cluster)

OD runs a **separate controlling cycle per region**, so the default deliverable is grouped by the `Cluster` field, not by class or status. The five values are `EMEA WEST`, `EMEA EAST`, `AMERICAS`, `APAC`, and `OESL` (global/cross-region — screen with whichever region owns delivery). Location→Cluster is already set on each row; use it directly. Put cross-region themes (a capability being bought plant-by-plant in several regions) *above* the regional sections so the central-standard argument is visible before the per-region tables. See `review-template.md` for the skeleton.

### Pointers, not populated copies

When the screen references list items in OD's repo, link to the list and keep only the analysis (class, verdict, open question) — never paste the raw rows in as a canonical table.
