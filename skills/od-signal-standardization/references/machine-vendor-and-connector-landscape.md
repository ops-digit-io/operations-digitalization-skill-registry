---
type: Skill Reference
title: Machine vendor and connector landscape
description: Counts of the 1,715 machine records by controller vendor, integration method and status, and what each connector family reaches, so a key user can see what a new machine's signals will look like and which path they arrive by.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, technical, signals]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Machine vendor and connector landscape

The machine notes carry **no signal names** - the data-point list lives on the edge platform and
in the flows (see [`field-signal-vocabulary.md`](field-signal-vocabulary.md)). What they do carry
is the controller, the field network and the integration route, which decide what a tag export
will look like and which skill route applies. Counts: `Work-OpsDigit-Knowledge/Graph/Machines`
(1,715 notes) front matter, read 2026-11-05. "Not recorded" means the field is absent on the
note; it is a count, not a finding that the machine has none.

## 1. Controller vendor

| Vendor (as recorded) | Machines | Integrated | Not integrated | Method recorded |
|---|--:|--:|--:|---|
| Siemens | 1,032 | 402 | 232 | edge platform 451, central OPC UA server 251, evaluation ongoing 51, not recorded 279 |
| Rockwell Automation - Allen Bradley | 220 | 113 | 58 | edge 78, central server 30, evaluation ongoing 52, not recorded 60 |
| vendor not recorded | 133 | 91 | 23 | edge 54, central 32 |
| Beckhoff | 42 | 17 | 22 | edge 35, not recorded 7 |
| Bachmann Electronic GmbH | 39 | 20 | 10 | central server 16, not recorded 23 |
| Engel | 38 | 32 | 6 | central 6, edge 1, not recorded 31 |
| B&R Industrial Automation | 32 | 29 | 1 | central 30 |
| Schneider Electric | 32 | 32 | 0 | not recorded 32 |
| Bachmann OPC | 24 | 24 | 0 | not recorded 24 |
| Mitsubishi Electric | 17 | 3 | 8 | central 4, evaluation 7 |
| Delta Electronic 14, keyence 12, Omron 12, Philips 9 | | | | |

Whole estate: integration method - edge platform 672, central OPC UA server 384, evaluation
ongoing 117, not recorded 542; integration status - integrated 821, not integrated 395,
integration ongoing 48, not recorded 451. Priority: PRIORITY 1 456, 2 386, 3 252, 4 82, 5 65, not
recorded 474.

**Siemens models** (1,032): S7-300 321, S7-1200 250, S7-1500 166, SINUMERIK 840D sl 19, S7-200
19, model not recorded 189. **Allen-Bradley** (220): CompactLogix 5370 88, 5069-L306ER 44,
CompactLogix 15, SLC 5/05 12, MicroLogix 1500 7.

**Field network** (where recorded, 1,164 of 1,715): PROFINET 445, TCP/IP 220, EtherNet/IP 186,
Modbus TCP 80, PROFIBUS 56 (plus 38 PROFIBUS/MPI and 14 `Profibus`: spelled three ways), EtherCAT
49, MPI 43, PPI 8. Machines on MPI, PPI and PROFIBUS-only networks are the old S7-300/200 population;
whether those can be reached at all is a `od-equipment-integration` question, not a naming one.

Reading for the signal work: **the integration route and the status are better recorded than
anything about the signals.** A machine with no recorded method (542) or status (451) is a
machine whose signal list nobody has been asked for yet. The analyser's input - the
`/data_points` list - exists only for machines on the edge platform path.

## 2. Connector families and what they reach

From the profile blocks of `Graph/Connectors` (26 notes). Only connectors with a recorded
machine count are shown.

| Connector | Controllers recorded | Machines | Plants | Status | Integrated / not / ongoing |
|---|---|--:|--:|---|---|
| DTQ-TIA-Connector | S7-1200, S7-1500 | 416 | 20 | productive | 196 / 103 / 5 |
| DTQ-S7-Connector (`SFT-SIMATIC S7-Connector` shows identical counts) | S7-300, S7-400 | 330 | 20 | productive | 112 / 86 / 26 |
| DTQ-ALLENBRADLEY-ROCKWELL-Connector | (not recorded) | 220 | 6 | productive | 113 / 58 / 2 |
| DTQ-Beckhoff-Connector | Beckhoff | 42 | 5 | productive | 17 / 22 / - |
| DTQ-Bachmann-Connector | | 63 | 3 | idea | 44 / 10 / - |
| DTQ-Engel EMI-Connector | | 38 | 3 | idea | 32 / 6 / - |
| DTQ-B&R-Connector | | 32 | 2 | idea | 29 / 1 / - |
| SINUMERIK connector | SINUMERIK | 27 | 4 | productive | 12 / 11 / - |
| SFT-OPC-Suite | | 24 | 1 | productive | 24 / - / - |
| DTQ-OMRON FINS / KEYENCECAM / RS232 | Omron FINS PLCs; Keyence camera; Keyence TM-3000 | 12 each | 2 / 1 / 1 | productive | 12 / - / - |
| DTQ-PIOVAN-Connector | Piovan drying systems | 2 | 2 | productive | 1 integrated |

The remaining connectors (EtherCAT IO, FTP2MIL for Cognex cameras, Optris IR camera, Modbus,
Multicon CMC131, OPC UA, S7-NET, SIMOTION D, SINUVARS, SMB, SmartKlaus, Zwick) have no machine
count on their notes. **Status words disagree with the machine counts**: three connectors marked
`idea` (Bachmann, Engel, B&R) are linked to 133 machines, 105 of them recorded as integrated -
those machines reach the platform by another route (the central OPC UA server, 30 of 32 B&R
machines). ⟨Reconcile connector status with the machine list - owner of the Connector list.⟩

Documentation: the connector notes list `documentation_available` as NO for the TIA connector
and most others, "what it does: not recorded". The connector facts above are therefore routing
facts only; for what a connector publishes, read the edge platform's data-point list.

### Topic driver segment to connector

The flows' topic `.../<edge-device>/<driver>/<id>` names the driver (`corpus-census-2026-11.md`
in `od-node-red-flow-builder`). The Connector notes give container image names that match five of
them: `tia`, `ads` (Beckhoff), `abrock` (Allen-Bradley), `cifx` (S7), `omron`. This is a naming
match, not a stated mapping - ⟨confirm with the IIAE⟩ before it is used to tell a key user which
connector a topic belongs to.

## 3. What this means for a new machine

1. Look the controller up in section 1 and the route in `od-equipment-integration`
   (`decision-paths.md`); do not start naming signals before the route is decided.
2. If the machine goes by the edge platform, get the `/data_points` list and run the analyser.
   If it goes through the central OPC UA server, the tag names come from the server's tag
   configuration; the analyser still works on that list.
3. A vendor with a high share of "not recorded" integration method (Engel 31 of 38, Bachmann OPC
   24 of 24, Schneider 32 of 32) is a vendor whose routing has to be asked, not read.
4. A vendor whose machines are mostly `NOT INTEGRATED` (Beckhoff 22 of 42, Siemens 232 of 1,032,
   Mitsubishi 8 of 17) is where "no data on the topic" is the first hypothesis.

## Sources

`Work-OpsDigit-Knowledge/Graph/Machines/` (1,715 notes, front matter), `Graph/Connectors/`
(26 notes, profile blocks), read 2026-11-05. Connector counts are the notes' own.
