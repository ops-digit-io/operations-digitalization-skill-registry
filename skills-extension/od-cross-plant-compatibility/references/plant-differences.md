---
type: Skill Reference
title: Plant differences
description: Guidance, no figures - the dimensions along which plants differ that a cross-plant standard must survive (region and integration state, controllers, field networks, ingress variants, tool rollouts, capability-instance spread, recorded blockers, data-gap plants), where to read each live and how to interpret it.
resource: ../SKILL.md
status: draft
tags: [information-integration-service, practice]
---

# Plant differences

This file holds **no counts, shares or plant lists**. It names each dimension, where to read it live, what patterns to expect
and what to do about them. **Sources:** the plant notes in the department knowledge base (`Graph/Plants`, plant-profile blocks, built from
the SharePoint machine, use case and tool lists), the Capability Epics notes and the Blocker Register. The plant notes say
themselves that figures are "as entered in the SharePoint list, not audited". Always read the live lists (Machine List, Tool
Overview) before relying on a number for a verdict, and state the date. A plant "has" a vendor, network or method when at
least one of its machines is recorded with it.

## 1. Region and integration state

Read per plant: region, machines recorded, machines integrated, share. Group by region (Europe, Americas, Asia) to see
whether a pattern is regional; usually the spread inside a region is larger than between regions.

Shape of the spread to look for:

| Group | How to find it | Consequence |
|---|---|---|
| Fully integrated plants | integrated = recorded | A standard "proven" here says little about plants with nothing integrated |
| Machines recorded, none integrated | integrated = 0, recorded > 0 | Test the route to the platform first; the ingress variant may not be chosen |
| No machines recorded at all | recorded = 0 | Cannot be graded; verdict is *unknown* |
| Largest recorded estates | rank by machines recorded | Where a mapping error costs the most |

## 2. Controllers

Per plant, list the controller vendors with at least one recorded machine (field `plc_vendor` of the Machine List). Typical
vendors: Siemens (dominant in most plants), Rockwell / Allen Bradley, Mitsubishi Electric, Beckhoff, Bachmann (also spelled
"Bachmann OPC"), B&R, Omron, Engel, Schneider Electric. Normalise spelling variants before counting.

Find the plants whose largest vendor is not Siemens: those are where a standard written with Siemens naming and data types in
mind is most likely to break. A single-vendor plant on a different protocol (for example Modbus/TCP) differs in state and
timestamp semantics, not only in the connector.

## 3. Field networks

Read per plant the recorded `network_protocol` values (typical: PROFINET, Ethernet/IP, TCP/IP, PROFIBUS and variants,
EtherCAT, Modbus/TCP, MPI, PPI). Note the dominant network of plants that differ from the first plant. Field network decides
the available connector and the reachable timestamp resolution.

## 4. Ingress variant (the path to the platform)

Read per plant the recorded integration methods: IIoT Edge Computing Platform, Central OPC UA aggregation server, Evaluation
ongoing (no path chosen). Several plants use two or three, so the choice is per machine, not per plant. Plants with most
machines on "evaluation ongoing" have no settled route yet.

Why it matters: the platform receives data by different routes, so where a name or a timestamp is set (edge flow,
aggregation server, platform) differs by route. Test the standard on **each** route in use, not on one.

## 5. Tool rollouts recorded per plant

Read from `Graph/Tools` (rollout records per plant: Available, Ongoing, Not Available). Versions of the same tool coexist
(MSB 1.0 / 2.0 / 4.0; MDA/PDA 1.0 / 2.0 / 3.0; Energy Management 1.0 / 2.0), so a standard that depends on a tool feature is
not automatically available everywhere. A plant with no row for a tool is unknown, not "not available". `od-system-fit-check`
holds the tool boundaries.

## 6. Capability-instance spread (the eleven templates)

Each template has one instance per plant in the Capability Epics notes (numbered plant instances plus one unnumbered). Count
live, per template, the instances that have **at least one member use case**.

Reading: a template that exists at nearly every plant is *used* at far fewer. A standard for a template with little in-use
evidence has few plants where the check is a measurement; at the others it is a prediction. Case Groups (AI-grouped, not
human-reviewed) show the same from the use-case side: per group, plants with delivered, planned and idea use cases.

## 7. Known blockers that are cross-plant differences

Read the Blocker Register (keyword-inferred themes, verbatim texts). Recurring themes:

| Theme | Reading for this skill |
|---|---|
| Connectivity concept and connector reuse | A connector built for one plant is not automatically reusable |
| Master data, planning data and data model | The data model is itself a recorded blocker |
| PLC access and PLC program | Context for a signal needs the PLC program; not available everywhere |
| Data availability and quality | Signals missing at some plants |
| Network and IT infrastructure | Infrastructure differs |

Related: "data model standardization" is a recorded machine-integration blocker (`od-signal-standardization`); `CT Base` is
the recorded name of that blocker; it is a live identifier, leave it as written. Count the themes live (texts, use cases,
plants) when quoting them.

## 8. Plants the flow corpus cannot speak for

`od-data-availability-check/references/plant-instance-map.md` lists which plants have no Node-RED flows available as
evidence. For those, "what lands on the platform" is *unproven*; the compatibility verdict for them is *unknown* until the
edge platform is checked directly.

## Not recorded (do not guess)

- Tag language per plant. - Unit and scaling per signal ("Nothing else is carried" by the edge platform's data-point list).
- Which consumers (dashboards, reports) read which signal. - Plant-level owner roles beyond Plant ME and Plant IT.
