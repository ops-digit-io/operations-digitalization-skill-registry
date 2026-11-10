---
type: Skill Reference
title: Barrier classes
description: Which vendors/protocols are actually cheap vs. expensive to connect, the resolved Modbus/aggregation-route question, pre-assessment tells not in the Machine List, and blocker root causes behind the recorded free text.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [information-integration-service, connectability, elicited]
derived_from:
  - kg_nodes.csv and the Connector Overview export — integration-rate read by vendor and protocol
  - interview with human:jakob.gabriel, 2026-09-17 — difficulty ranking, pre-assessment tells, blocker root causes
  - general industry research, 2026-09-17 — brownfield-integration hurdles section, sourced inline
generated: { by: claude-code/1, at: 2026-09-17T00:00:00Z }
---

# Barrier classes

Integration rate by vendor/protocol, mined from the Machine List and Connector Overview,
describes what got connected historically. It is not the same question as what's cheap to
connect next — a vendor can show a high rate because of how the existing machines happened
to route, not because a new machine of that type is easy. This reference resolves the two
readings against each other.

## Difficulty ranking — easy to hard

Elicited 2026-09-17, supersedes a raw read of the integration-rate figures:

1. OPC-UA-capable PLCs
2. Siemens TIA Profinet / Ethernet
3. Siemens S7 PROFINET
4. Allen-Bradley (Rockwell)
5. Modbus
6. B&R
7. Mitsubishi
8. Beckhoff
9. Bachmann
10. Siemens S7 PROFIBUS
11. Delta
12. Philips
13. anything else — treat as PROFIBUS-tier or worse until proven otherwise

Where this disagrees with the raw integration-rate read, and why the rate alone misleads:

- Modbus ranks harder here than B&R and Bachmann despite showing a very high integration
  rate. That rate reflects the historical aggregation-server route, not the
  difficulty of a fresh connection.
- Beckhoff and Bachmann both rank harder than their integration rate alone would suggest.
  Beckhoff's placement matches its known gap — no ADS driver on the Central Aggregation
  Server. Bachmann's placement is new: the rate alone reads it as unremarkable.
- Siemens splits by protocol, not vendor: TIA Profinet/Ethernet sits near the top of this
  list, S7 PROFIBUS sits near the bottom. A vendor-level integration rate collapses that
  split — read a Siemens machine by protocol, not by vendor badge.

## The Modbus contradiction

`DTQ-MODBUS-Connector` remains `Idea` status. That doesn't block Modbus integration: Modbus
is solved at the Central OPC-UA Aggregation Server, not the edge connector. The missing edge
connector only matters for a plant running the edge-platform concept instead of the
aggregation route.

## Pre-assessment tells

Not in the Machine List or Connector Overview — check on site before opening the Equipment
integration guide app:

- Panel/cabinet condition
- Network cabinet and cabling — whether a usable drop exists near the machine at all
- Plant IT/ME contact responsiveness
- PLC type, interfacing, and machine network topology — what's actually wired to the PLC and how
- Whether the PLC program is available and under own control, versus a black box only the OEM
  can touch

## Named blockers: symptom vs. root cause

Cyber-security firmware patching is a frequently cited blocker in the Machine List free text.
Citing it rarely points at one cause. In practice it covers:

- No owner or scheduled OT maintenance window for the patch itself
- Plant IT/OT unwilling or unable to commit to the change
- Legacy hardware that cannot be patched at all without a generation upgrade
- Missing PLC program, or vendor support that exists but is costly
- Vendor no longer exists or no longer supports the platform — a common brownfield outcome:
  no update available, buy a new machine

Distinguish which of these it is before sizing the fix. The first two are a scheduling and
organizational problem; the last two are a capital decision integration can't resolve on its
own.

## Brownfield hurdles beyond this estate

General industry pattern, not from this estate's own data — worth checking against a specific
machine when a barrier doesn't map cleanly onto a named blocker above.

- No native connectivity. Older PLCs are serial-only with proprietary protocols and no
  Ethernet port; getting one online at all is a protocol-bridging problem before it's a data
  problem.
- Missing documentation. Wiring diagrams, PLC source and configuration frequently don't
  exist or are lost, and the original vendor may no longer exist to ask.
- No native security, not just an unapplied patch. Legacy PLCs and HMIs were built without
  authentication or encryption capability. Often there's no patch that adds it, because the
  hardware can't support the mechanism at all.
- Flat network, shared credentials. OT networks built before segmentation was a concern
  tend to run on shared accounts with no real access control. Adding identity governance
  later means retrofitting a concept the architecture wasn't built for, not applying a
  setting.
- Approval friction competes with production. Any change to a live line needs a maintenance
  window; getting one can take longer than the technical fix, and the production schedule
  wins by default.
- Skill and capital intensity. Bridging legacy and modern environments needs OT-specific
  integration skill most IT teams don't carry, and the usual fix — edge gateways, protocol
  converters — is a capital line item, not a configuration change.

Sources: [IIoT World — harnessing IoT data from legacy industrial systems](https://www.iiot-world.com/industrial-iot/connected-industry/a-new-way-to-harness-iot-data-from-legacy-industrial-systems/),
[Alumio — IIoT retrofitting for legacy factories](https://www.alumio.com/blog/iiot-retrofitting-legacy-factory-equipment),
[Integration Objects — legacy OT cyber security best practices](https://integrationobjects.com/blog/legacy-ot-cyber-security-best-practices-for-connecting-legacy-operational-technology-systems/),
[nhimg.org — why legacy OT systems increase cyber risk](https://nhimg.org/faq/why-do-legacy-ot-systems-increase-cyber-risk-in-industry-40-programmes/)
