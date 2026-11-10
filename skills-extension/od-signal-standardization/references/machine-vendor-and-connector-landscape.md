---
type: Skill Reference
title: Machine vendor and connector landscape
description: How to read the Machine List and the connector notes to see what a new machine's signals will look like and which path they arrive by - controller vendor families, field networks, integration routes, connector families and the traps in the records. Guidance only; counts are measured live.
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
will look like and which skill route applies. Source: `Work-OpsDigit-Knowledge/Graph/Machines`
front matter and `Graph/Connectors` profile blocks. "Not recorded" means the field is absent on
the note; it is a gap in the record, not a finding that the machine has none.

**How to get the numbers.** Group the machines by controller vendor, by integration method and
by status, and count each cell on the current Machine List export; name the export date. This
file deliberately holds no counts.

## 1. Controller vendor

Fields to tabulate per vendor (as recorded): machines, integrated, not integrated, status not
recorded, and the integration method used (edge platform, central OPC UA server, evaluation
ongoing, not recorded).

What to expect, qualitatively:

- **One or two vendor families dominate** the estate (Siemens, Rockwell Automation / Allen
  Bradley); a long tail follows (Beckhoff, Bachmann, Engel, B&R, Schneider Electric, Mitsubishi
  Electric, Delta, Keyence, Omron, Philips and others).
- **"Vendor not recorded"** is a sizeable group of its own. Treat it as a data-quality item.
- **Model families within a vendor** matter more than the vendor: Siemens S7-300, S7-1200,
  S7-1500, SINUMERIK, S7-200; Allen-Bradley CompactLogix, SLC, MicroLogix. Tabulate the model
  field per vendor.
- **Vendor spelling variants** occur (for example a company name and a product name for the same
  maker); match on all spellings.

**Field network** (where recorded): PROFINET, TCP/IP, EtherNet/IP, Modbus TCP, PROFIBUS (spelled
in several ways), EtherCAT, MPI, PPI. Machines on MPI, PPI and PROFIBUS-only networks are the
old S7-300/200 population; whether those can be reached at all is a `mi-connector`
question, not a naming one.

**Reading for the signal work.** The integration route and the status are better recorded than
anything about the signals. A machine with no recorded method or status is a machine whose
signal list nobody has been asked for yet. The analyser's input - the `/data_points` list -
exists only for machines on the edge platform path.

## 2. Connector families and what they reach

From the profile blocks of `Graph/Connectors`. Tabulate, for each connector with a recorded
machine count: the controllers it serves, machines, plants, connector status, and machines
integrated / not integrated / ongoing.

Families to expect (names as in the connector notes):

| Connector family | Reaches |
|---|---|
| DTQ-TIA-Connector | S7-1200, S7-1500 |
| DTQ-S7-Connector (and the `SFT-SIMATIC S7-Connector` entry) | S7-300, S7-400 |
| DTQ-ALLENBRADLEY-ROCKWELL-Connector | Allen-Bradley / Rockwell PLCs |
| DTQ-Beckhoff-Connector | Beckhoff |
| DTQ-Bachmann-Connector, DTQ-Engel EMI-Connector, DTQ-B&R-Connector | status may be `idea`: see the trap below |
| SINUMERIK connector | SINUMERIK controllers |
| SFT-OPC-Suite | OPC-based access |
| DTQ-OMRON FINS / KEYENCECAM / RS232 | Omron FINS PLCs; Keyence camera; Keyence TM-3000 |
| DTQ-PIOVAN-Connector | Piovan drying systems |

Other connectors (EtherCAT IO, FTP2MIL for Cognex cameras, Optris IR camera, Modbus, Multicon
CMC131, OPC UA, S7-NET, SIMOTION D, SINUVARS, SMB, SmartKlaus, Zwick) often have no machine
count on their notes.

**Trap: status words disagree with the machine counts.** Connectors marked `idea` can be
linked to machines that are recorded as integrated - those machines reach the platform by
another route (typically the central OPC UA server). Compare each connector's status with the
integration method of its machines before saying a path exists or does not.
⟨Reconcile connector status with the machine list - owner of the Connector list.⟩

**Trap: documentation.** The connector notes list `documentation_available` as NO for most
connectors and "what it does: not recorded". The connector facts are therefore routing facts
only; for what a connector publishes, read the edge platform's data-point list.

### Topic driver segment to connector

The flows' topic `.../<edge-device>/<driver>/<id>` names the driver (`corpus-census.md`
in `ops-pipeline`). The Connector notes give container image names that match
several of them: `tia`, `ads` (Beckhoff), `abrock` (Allen-Bradley), `cifx` (S7), `omron`. This
is a naming match, not a stated mapping - ⟨confirm with the IIAE⟩ before it is used to tell a
key user which connector a topic belongs to.

## 3. What this means for a new machine

1. Look the controller up in section 1 and the route in `mi-connector`
   (`decision-paths.md`); do not start naming signals before the route is decided.
2. If the machine goes by the edge platform, get the `/data_points` list and run the analyser.
   If it goes through the central OPC UA server, the tag names come from the server's tag
   configuration; the analyser still works on that list.
3. A vendor whose integration method is mostly "not recorded" is a vendor whose routing has to
   be asked, not read.
4. A vendor whose machines are mostly `NOT INTEGRATED` is where "no data on the topic" is the
   first hypothesis.

## Sources

`Work-OpsDigit-Knowledge/Graph/Machines/` front matter and `Graph/Connectors/` profile blocks.
Connector counts, where quoted, are the notes' own.
