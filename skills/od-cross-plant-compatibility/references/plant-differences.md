---
type: Skill Reference
title: Plant differences
description: What differs between the 33 plants that a cross-plant standard must survive - region, controllers, field networks, ingress variants, tool rollouts, data-gap plants, capability-instance spread and recorded blockers - as counts with source and date.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Plant differences

Aggregates only. **Source:** the 33 plant notes in the work vault (`Graph/Plants`, plant-profile blocks, built from the
SharePoint machine, use case and tool lists; enriched 2026-09-25, full text 2026-11-05) and the Capability Epics notes,
aggregated 2026-11-05 by a one-off count. The figures are a snapshot, they will drift, and the plant notes say themselves
that figures are "as entered in the SharePoint list, not audited". Refresh from the Machine List and Tool Overview before
relying on a number for a verdict. A plant "has" a vendor, network or method when at least one of its machines is recorded
with it.

## 1. Region and integration state

| Region | Plants | Machines recorded | Integrated | Share |
|---|--:|--:|--:|--:|
| Europe | 20 | 1,017 | 489 | 48% |
| Americas | 9 | 482 | 231 | 48% |
| Asia | 4 | 216 | 101 | 47% |
| **All** | **33** | **1,715** | **821** | **48%** |

(Machine List total 1,715 and 821 integrated agree with `20-Done/Machine connectivity rollout.md`.)

Shape of the spread across plants (from the same notes):

| Group | Plants |
|---|---|
| 100% integrated | HannMuenden, Rennes, Somersworth, SunPrairie |
| 0 integrated, machines recorded | Korbach, Montemorelos, Ostrava, SanLuisPotosi, Tanger, Tlalnepantla |
| No machines recorded at all (cannot be graded) | Andrezieux, Dannenberg, Jeonju, Kranj, Oedelsheim |
| Largest recorded estates | Subotica 181, Mako 128, Vac 103, Changshu 99 |

Consequence: a standard "proven" on a mostly integrated plant says little about the six plants with nothing integrated,
and nothing about the five with no records.

## 2. Controllers (plants where the vendor appears)

| Vendor | Plants | Notes |
|---|--:|---|
| Siemens | 24 | Dominant everywhere except where listed below |
| Rockwell Automation - Allen Bradley | 6 | Auburn (all 60 machines), Monterrey (75 controllers), Montemorelos, Delicias, SunPrairie, Qingdao |
| Mitsubishi Electric | 4 | Changchun, Changshu, Montemorelos, PontaGrossa |
| Beckhoff | 4 | Somersworth, Subotica, Waltershausen, SanLuisPotosi |
| Bachmann (Electronic / OPC) | 3 | Changshu, DolneVestenice, Northeim (listed as "Bachmann OPC" there) |
| B&R | 2 | DolneVestenice, Waltershausen |
| Omron | 2 | Monterrey, Timisoara |
| Engel | 2 | Northeim, Somersworth |
| Schneider Electric | 1 | Rennes (all 32 machines, Modbus/TCP) |

Plants whose largest vendor is not Siemens: Auburn, Montemorelos, Monterrey, SunPrairie (Rockwell); Rennes (Schneider);
Northeim (Engel / Bachmann); DolneVestenice (B&R / Bachmann).

## 3. Field networks (plants where recorded)

PROFINET 19 · Ethernet/IP 11 · TCP/IP 10 · PROFIBUS 8 (plus variants) · EtherCAT 7 · Modbus/TCP 4 · MPI 4 · PPI 1.
Dominant network of a few plants: Rennes Modbus/TCP, Auburn TCP/IP, SunPrairie TCP/IP, DolneVestenice Ethernet/IP, Caluire Modbus/TCP.

## 4. Ingress variant (the path to the platform)

| Integration method recorded | Plants |
|---|--:|
| IIoT Edge Computing Platform | 21 |
| Central OPC UA aggregation server | 14 |
| Evaluation ongoing (no path chosen) | 6 |

Several plants use two or three. Examples: Mako 58 on IIoT Edge and 44 on the central OPC UA server; Waltershausen 37 / 34 /
9 evaluation; PontaGrossa all 75 on central OPC UA; Subotica 172 on IIoT Edge. Montemorelos 45 of 51 and Changshu 36 of 99
are "evaluation ongoing".

Why it matters: the platform receives data by different routes, so where a name or a timestamp is set (edge flow, aggregation
server, platform) differs by route. Test the standard on **each** route in use, not on one.

## 5. Tool rollouts recorded per plant (plants listing the tool as available)

| Tool | Plants available | Plants "ongoing" |
|---|--:|--:|
| Energy Management 2.0 | 25 | 0 (1 recorded "not available") |
| RuleEngine 2.0 | 19 | 0 |
| Concept 3, IIoT Edge Computing Platform | 14 | 0 |
| MDA/PDA 2.0 | 14 | 0 |
| MSB 2.0 | 13 | 0 |
| Concept 1, Central OPC-UA Server | 11 | 0 |
| MSB 4.0 | 6 | 3 |
| MDA/PDA 1.0 | 6 | 0 |
| Energy Management 1.0 | 4 | 0 |
| MDA-PDA 3.0 | 3 | 0 |
| MSB 1.0 | 3 | 0 |
| MES 1.0 | 1 | 0 |
| Concept 2, container-based integration | 1 | 0 |
| QFPR | 1 | 1 |
| MIL 1.0 / Data Science Factory | 0 | 1 each |

Reading it: versions of the same tool (MSB 1.0, 2.0, 4.0; MDA/PDA 1.0, 2.0, 3.0) coexist, so a standard that depends on a
tool feature is not automatically available everywhere. `od-system-fit-check` holds the tool boundaries.

## 6. Capability-instance spread (the eleven templates)

Each template has one instance per plant (Andon Board, Process Values and Recipe Values 33; the other eight 32). Among the
numbered plant instances, the number that have **at least one member use case** (derived from the epic notes, 2026-11-05;
the one unnumbered instance per template is not included):

| Capability | Instances with members | of |
|---|--:|--:|
| Process Values | 18 | 32 |
| Andon Board | 17 | 32 |
| Manual Quality Data | 12 | 31 |
| Process Quality Data | 12 | 31 |
| Other Use Cases | 11 | 31 |
| Analytics | 9 | 31 |
| Downtime Reporting | 9 | 31 |
| Machine Alerts | 8 | 31 |
| Cycle Time | 6 | 31 |
| OEE Calculation | 6 | 31 |
| Recipe Values | 4 | 32 |

So a template that exists at 32 plants is *used* at far fewer. A standard for OEE or Cycle Time has in-use evidence at about
six plants; the other plants are the ones for which the check is a prediction, not a measurement.

The case groups say the same from the use-case side. Example, `CG-01 Process Values - Rubber`: 62 plant use cases;
delivered at 7 plants, planned at 1, idea at 2, white space at 1 (Case Groups, 2026-11-04, AI-grouped, not human-reviewed).

## 7. Known blockers that are cross-plant differences

From the Blocker Register (export of 2026-08-21; keyword-inferred themes, verbatim texts; 83 blocker texts on 68 use
cases at 18 plants):

| Theme | Texts | Plants | Reading for this skill |
|---|--:|--:|---|
| Connectivity concept and connector reuse | 15 | 10 | A connector built for one plant is not automatically reusable |
| Master data, planning data and data model | 8 | 7 | The data model is itself a recorded blocker |
| PLC access and PLC program | 24 | 8 | Context for a signal needs the PLC program; not available everywhere |
| Data availability and quality | 4 | 4 | Signals missing at some plants |
| Network and IT infrastructure | 6 | 3 | Infrastructure differs |

Related: "data model standardization" is the most-recorded machine-integration blocker, **23 machines** (`od-signal-standardization`).
`CT Base` is the recorded name of that blocker; it is a live identifier, leave it as written.

## 8. Plants the flow corpus cannot speak for

`od-data-availability-check/references/plant-instance-map.md` lists 16 plants for which Node-RED flows were not available
as evidence. For those, "what lands on the platform" is *unproven*; the compatibility verdict for them is *unknown* until
the edge platform is checked directly.

## Not recorded (do not guess)

- Tag language per plant. - Unit and scaling per signal ("Nothing else is carried" by the edge platform's data-point list).
- Which consumers (dashboards, reports) read which signal. - Plant-level owner roles beyond Plant ME and Plant IT.
