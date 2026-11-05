---
type: Skill Asset
title: Prefilled test items
description: Test items to copy into sections 1 to 3 of the acceptance test protocol, prefilled per route (edge, aggregation, file or image endpoint) and per use case cluster, with the typical failure points from the records beside each item.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Prefilled test items

Copy the block that matches the artefact into [`acceptance-test-protocol.md`](acceptance-test-protocol.md)
§1 to §3, then delete what does not apply and add what is specific. Expected values and
tolerances are **yours to fill**: the records do not give them. Grades and sources of every
item: [`acceptance-by-route.md`](../references/acceptance-by-route.md) and
[`cluster-acceptance-criteria.md`](../references/cluster-acceptance-criteria.md). Items are
suggested checks unless marked *rule*.

## A. Machine integration, any route

| Item | Expected | Real or simulated | Result | Evidence |
|---|---|---|---|---|
| Machine List row names every connector in the chain, route filled (*rule*) | ⟨⟩ | | | |
| Vendor, PLC model, network protocol filled | ⟨⟩ | | | |
| Cyber Security / OT sign-off reference present (*rule*) | ⟨reference⟩ | | | |
| Write permission off on aggregation data sources (*rule*) | off | | | |
| Tags named to the agreed data model, not the PLC layout (*rule*) | ⟨⟩ | | | |
| Each named signal: value equals the machine's own display | ⟨tolerance⟩ | real | | |
| Value reaches the data platform within the expected delay | ⟨seconds⟩ | real | | |
| Timestamp and unit correct at the data platform | ⟨⟩ | real | | |
| Blocker text on the row closed or restated | ⟨⟩ | | | |
| Status set to `INTEGRATED` only after this protocol passed; integration date written (*rule*) | ⟨date⟩ | | | |

## B. Edge route, add

| Item | Expected | Result | Evidence |
|---|---|---|---|
| Connector matches the PLC family (S7-300/400 vs S7-1200/1500; Softing edge connector not used) (*rule*) | ⟨⟩ | | |
| Shared edge device: each machine behind it tested separately; failure domain written down | ⟨machines⟩ | | |
| Engineering software version compatible (TIA) | ⟨version⟩ | | |
| Firmware or vulnerability patch state confirmed | ⟨state⟩ | | |
| Sinumerik or Sinuvars: signal count and rate within the connector's limits; PLC function block and G-code present | ⟨count, ms⟩ | | |
| Camera on the same device: images arrive as well as signals | ⟨images per part⟩ | | |

Typical failures in the records: missing data-model alignment (23 rows), unpatched firmware
(13), TIA version (12), edge device allocation or camera hardware (20), wrong or missing PLC
program (6).

## C. Aggregation route, add

| Item | Expected | Result | Evidence |
|---|---|---|---|
| Driver and licence for the PLC family in place (*rule*) | ⟨licence⟩ | | |
| Edge platform present behind the server (*rule*) | ⟨⟩ | | |
| Hop 1: the machine's tags readable in the server's address space | ⟨tags⟩ | | |
| Hop 2: the edge reads the address space through `DTQ-OPCUA-Connector` | ⟨⟩ | | |
| No Beckhoff ADS data source claimed; Beckhoff reached by Modbus TCP or a TwinCAT OPC server, or by the edge connector (*rule*) | ⟨⟩ | | |

## D. File, image or serial endpoint, add

| Item | Expected | Result | Evidence |
|---|---|---|---|
| File or image arrives for each part in the test window | ⟨count⟩ | | |
| Metadata arrives with the image | ⟨fields⟩ | | |
| Naming convention as agreed | ⟨pattern⟩ | | |
| Source retention and backup known | ⟨days⟩ | | |
| Value read equals the instrument's display (serial, web service) | ⟨tolerance⟩ | | |

## E. Dashboard or analytics asset, by cluster

Pick the rows for the cluster; each is a UAT scenario for the plant owner, run in a real shift.

| Cluster | Scenario | Expected result | Result |
|---|---|---|---|
| C01 OEE | Open the line view: availability, performance, quality shown separately; ideal cycle time and micro-stop threshold stated | ⟨values⟩ | |
| C02 Andon | Raise a signal by hand and from the machine; second signal escalates; event in the log afterwards | ⟨tiers, minutes⟩ | |
| C03 SPC | Control and specification limits shown separately; a test out-of-control point triggers the reaction plan | ⟨limits, person⟩ | |
| C04 Manual data | An entry is read downstream in the routine; the old form has a switch-off date | ⟨who reads⟩ | |
| C05 Downtime and alerts | A test stop is classified with the agreed reason catalogue; a test alert reaches the named recipient and is acknowledged | ⟨recipient, minutes⟩ | |
| C07 Recipe and traceability | A recipe change is logged; a test unit is traced one up and one down | ⟨serial⟩ | |
| C08 Energy | Consumption is attributed to a named line, machine or product; baseline period stated | ⟨baseline⟩ | |
| Every cluster | **Baseline recorded** (scrap, downtime or reporting hours, before) so a saving can later be claimed | ⟨baseline, source⟩ | |
| Every cluster | The plant owner named, and has used it in a real shift | ⟨name, shift⟩ | |
