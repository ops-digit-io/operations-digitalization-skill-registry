---
type: Skill Reference
title: Validated routes
description: Guidance, no figures - how to classify an integration route as written-and-proven, proven-but-unwritten, fallback or none, from the guide and the Machine List, and how to count the evidence live. Open it before you say "there is a standard system for this machine".
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Validated routes

This file holds **no counts**. It teaches how to decide whether a route is a standard-system candidate and how to gather the
evidence live. Re-count on the live list before quoting a figure, and name the list and date.

A route is a **standard-system candidate** when it is (a) written down in full in the equipment-integration guide and
(b) proven by machines recorded as `INTEGRATED` through it, in at least two plants. The third part of a standard system, a
purchasable kit with price and lead time, is **not recorded anywhere** the skill could read, so no route is a finished
standard system. Rank routes by evidence.

## Where to read the evidence

- **Machine List** (SharePoint list, mirrored in vault `Graph/Machines`; fields `plc_vendor`, `plc_model`,
  `network_protocol`, `integration_status`, `integration_method`). Export it with `od-sharepoint-list-export`, group by
  controller vendor and model, method and status, and count machines and distinct plants per group.
- **Route status**: skill `od-equipment-integration`, `references/decision-paths.md` (the live tree and the "next" tree).
- **Connector status**: vault `Graph/Connectors` and `references/connectors.md` of the same skill (status such as
  Productive, Idea, Development; utilization such as USE, NOT AVAILABLE, DO NOT USE).
- **Method names in the list**: `IIoT Edge Computing Platform` = Concept 3 (edge route, topologies 1 and 2 of the guide);
  `Central OPCUA Aggregation Server` = Concept 1 (topology 3); `EVALUATION ONGOING` = not yet decided.

## Data-quality traps when counting

- A blank integration status is not "not integrated"; a blank method is not "no method used". Report blanks as their own
  group, never fold them into another.
- A blank or misspelled vendor ("Bachmann OPC" for "Bachmann") splits one family into several groups; normalise before
  counting.
- A route can be ahead of the guide: machines may be recorded as integrated through a route the guide still marks as a task
  stub. That is an update for the integration owner, not a reason to call the route written.
- The per-machine choice of route differs within one plant: some plants have machines on both the edge and the aggregation
  server. Evidence is per machine, not per plant.
- Sum of plants per route does not match the tool notes' rollout records (integration happened before the rollout was
  recorded, or the records were not updated). Treat as a question for the IIAE, not an error to fix silently.

## The four classes

### Class A - written route, proven in at least two plants (standard-system candidates)

Recognise: the guide has the full procedure, the connector is productive, several plants have machines integrated through it.
Typical members: Siemens S7 / TIA on the edge (`DTQ-S7` / `DTQ-TIA` / `DTQ-S7-NET`) and on the central aggregation server
(Softing dataFEED plus bridge `DTQ-OPCUA-Connector`); Rockwell / Allen Bradley on the edge (`DTQ-ALLENBRADLEY-ROCKWELL`) and
on the aggregation server. Rules that hold for the technology and the policy:

- Only the large edge device is approved; there is no approved small device (decision-paths). Low-frequency `S7-NET` is
  the answer where a device is not wanted.
- The aggregation-server route needs the edge platform behind the server. `SFT-SIMATIC S7-Connector` is DO NOT USE (no
  cyber-security-compliant PLC communication).

### Class B - proven in the field, but the guide's procedure is unwritten (`TODO` or stub)

Recognise: machines are recorded as integrated through the route, but the guide's body for it is `TODO` or a task stub, or
the connector documentation is not available. Typical members: Beckhoff on the edge (`DTQ-Beckhoff`, ADS; Softing has **no
Beckhoff driver**), Omron NJ / CJ on the edge (`DTQ-OMRON FINS`), Modbus TCP on the aggregation server, Keyence camera /
sensor on the edge (`DTQ-KEYENCECAM`, FTP; a non-PLC connector).

What is missing is the written procedure and its documentation, not a first deployment. A route marked `TODO` is not a
standard system until the IIAE writes the procedure. Say plainly: "this has been done, but the procedure is not written".

### Class C - proven only through a fallback or at a single plant

Recognise: one plant only, or only via a fallback, or the connector status is `Idea` / not available. Typical members: B&R
(aggregation server; dataFEED has a B&R driver), Bachmann over OPC UA, Mitsubishi Melsec-Q (aggregation only), Siemens
S7-200 (not in the guide's tree), Sinumerik NCU (`DTQ-SINUMERIK`, UDP/IP), Engel injection moulding (no vendor connector;
current Engel controllers serve OPC UA), Schneider (no method recorded). Also expect the field to be ahead of the guide here.
Not a candidate.

### Class D - no route, or blocked

- Controllers with no route in the guide (for example Delta Electronic, Philips, Mitsubishi beyond the aggregation route):
  anything not in the tree is "Integration of Other PLCs": connector development, long lead times (decision-paths). This is
  Lane 3b, not 1b.
- Camera systems cannot go through the aggregation server; edge only (rules-next).
- A machine **without the PLC program** cannot be connected; see `od-equipment-integration`, `references/fallbacks.md`.
- **Vendor not recorded** on a machine: do not place it in a class until its controller is known.

## How to read a machine against this classification

1. Controller vendor and model from the Machine List (a blank is unknown, not a "No").
2. Find the family. Class A: continue on branch 1b with that route; cost, lead time and kit are still ⟨to be supplied⟩ (see
   [standard-system-entry.md](../assets/standard-system-entry.md)).
3. Class B or C: say plainly "this has been done at other plants but the procedure is not written"; hand to the IIAE and
   `od-barrier-triage` / Lane 3b. Do not offer it as a standard system.
4. Class D or no row: no standard system; hand to `od-system-fit-check` and Lane 3b.

Re-derive the class of each family on the live list and live guide before relying on the typical members above: routes move
between classes when procedures are written or more plants prove them.

## Open

- ⟨The list of purchasable kits per route, prices and lead times⟩ - OD lead, IIAE, procurement; not in the vault notes read.
- ⟨Why some integrated machines carry no method⟩ and ⟨whether machines under `EVALUATION ONGOING` will land on edge or
  aggregation⟩ - IIAE.
- ⟨Whether the guide's `TODO` for Beckhoff and Omron on the edge is still current⟩ given that machines are recorded as
  integrated that way - IIAE.
