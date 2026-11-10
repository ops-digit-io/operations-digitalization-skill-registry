---
type: Skill Reference
title: Software footprint gate
description: "The mandatory software / IT-footprint hard gate: the 8-point checklist every invest row passes before scoring."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [invest-screen, gate, department-package]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/30-skills/investment-checking.zip/reference/software-footprint-gate.md, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `investment-checking.zip/reference/software-footprint-gate.md` (the master).

# Software / IT-footprint gate (mandatory, blocking)

The gate OD most often misses. Many purchases are booked as **equipment** (ME/PPI/Quality/FM) or as **indirect** spend, but they quietly ship software, a PC, a framework, a license, or network endpoints that OD ends up having to integrate, secure or operate — without ever being asked.

**Reference case:** a Lessmüller laser-control device is bought as a machine part. In reality it needs a PC running a framework OD has never seen from a Cyber Security standpoint, and it exposes endpoints (e.g. an FTP server) that compete with OD's internal connectors. None of that is on the invest row.

This gate is **hard**: while it is tripped and unresolved, the item cannot be "Go", regardless of business case.

## Applies to

- **Direct** software/IT purchases (a license, a server, a SCADA/MES module, a database).
- **Indirect** software riding on hardware/equipment: any machine, retrofit, test bench, camera/vision, laser/marking, controller, measuring system, or "device" that includes a computer or software.
- Anything that touches the **shopfloor / OT network** or corporate network.

Trigger the gate for every OD-touching and cross-region item, and for any equipment row hitting a software/endpoint/connectivity/cyber signal from the lexicon.

## The checklist (each must be answered — ⟨open⟩ counts as tripped)

1. **Embedded compute?** Does it include or require a PC / IPC / server / workstation / embedded controller? Who patches and owns it?
2. **Software & framework?** What software, runtime or framework runs on it? Version, vendor, support/EOL. Is it on any approved list?
3. **Licenses?** Named user / floating / per-device licenses, subscription, renewal, and who carries the recurring cost?
4. **Endpoints exposed?** Does it stand up services — FTP/SFTP, OPC, REST, shares, its own DB, a web UI? Do any **compete with or duplicate an internal connector** (IIoT Edge / MSB / data-platform path)?
5. **Network / OT touch?** What does it connect to (shopfloor VLAN, corporate LAN, internet)? Inbound/outbound flows? Does it need a firewall rule or segmentation?
6. **Cyber Security clearance?** Is the framework/device known to Cyber Security? MSB / security-bundle applicable? Any sign-off needed before an external connection (per decision-rights "Cyber Security sign-off for external connection")?
7. **Interface fit vs standard?** Does the data path use a standardised interface, or a proprietary one that will need custom glue and add long-term maintenance?
8. **Ownership after go-live?** Who operates, monitors, updates and secures the software footprint once the machine is running — the plant, ME, IT, OD? Named or ⟨open⟩?

## Gate outcome

- **Clear** — all eight answered, no unmanaged software/endpoint, owner named, Cyber Security ok (or not applicable). Gate passes; proceed to score.
- **Tripped** — any unmanaged compute/software/endpoint, unknown framework, competing endpoint, missing Cyber Security clearance, or unnamed owner. Verdict is **Blocked**; the deliverable is the specific open question + who must answer it (usually the item owner + Cyber Security + OD connectivity lane).

Write the tripping reason explicitly, e.g. *"Ships a vendor PC + unknown control framework; exposes FTP — competes with IIoT Edge connector; Cyber Security clearance ⟨open⟩ → Blocked."*
