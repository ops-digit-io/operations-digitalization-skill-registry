---
type: Skill Reference
title: Vendor protocol routes
description: Guidance per controller vendor, PLC model and network protocol - how to read the Machine List for each family, which connector the Connector Overview names, and what the records do and do not say about how each family is reached. Guidance only, no company figures.
resource: ../SKILL.md
status: draft
tags: [information-integration-service, technical]
---

# Vendor and protocol routes

Use this when someone says "we have Rockwell machines at the plant, what happens to them?". It
tells you **how to read the written-down status** per family and what patterns to expect. It does
not rank difficulty (that is `barrier-classes.md`, an elicited judgement)
and it does not give the configuration (that is `decision-paths.md` and the
Softing and edge references).

**This file holds no counts.** The per-vendor, per-model and per-protocol tables that used to sit
here were a snapshot of one export. To get the numbers, group the live Machine List by controller
vendor, PLC model or network protocol, and by `integration_status` and `integration_method`
(`Edge` = IIoT Edge Computing Platform; `Aggr.` = Central OPCUA Aggregation Server; `Eval.` =
`EVALUATION ONGOING`; blank = field not filled). Re-count before quoting and give the export date.
Statements marked **Rule** cite where they come from.

## Reading rules

1. **Rule (existing `SKILL.md`):** a blank is not a no. Blank status, route or protocol means
   nobody filled the field.
2. **Rule (this analysis):** read a family by status, by route **and** by plant. A family whose
   integrated machines all sit in one plant shows that plant's decision, not that the family is
   easy.
3. **Rule (`connectors.md`):** where the Overview's native connector is `NOT
   AVAILABLE`, ask what the machine exposes; `DTQ-OPCUA-Connector` reaches any OPC UA server.
4. **Data-quality trap:** the vendor field carries variant spellings of the same vendor (for
   example `Keba` / `KEBA Industrial Automation`, `VIPA` / `Vipa`, `Bachmann Electronic GmbH` /
   `Bachmann OPC`) and a blank bucket. Count a family with all of its spellings, and report the
   blank bucket separately.

## By controller vendor - how to read each family

| Family | What to expect in the record | Connector in the Overview (state) |
|---|---|---|
| Siemens | Dominates the estate; mix of S7-300/400 legacy and S7-1200/1500; routed over both edge and aggregation; a large share without status | `DTQ-S7-Connector` (S7-300/400, Productive, USE), `DTQ-TIA-Connector` (S7-1200/1500, Productive, USE), `DTQ-SINUMERIK-Connector`, `DTQ-SINUVARS`, `DTQ-SIMOTIOND`, `DTQ-S7-NET`; `SFT-SIMATIC S7-Connector` is `DO NOT USE` |
| Rockwell / Allen-Bradley | Second large family; the most rows with the route still `EVALUATION ONGOING`; concentrated in a few plants, so the question is model- and plant-specific | `DTQ-ALLENBRADLEY-ROCKWELL-Connector` (Productive, USE) |
| Beckhoff | Routed to edge, not to aggregation; the Central Aggregation Server has no Beckhoff driver ([`SKILL.md`](../SKILL.md)) | `DTQ-Beckhoff-Connector` (ADS, Productive, USE); `DTQ-EthercatIO-Connector` for Beckhoff clamps |
| Bachmann (two spellings) | Often integrated with the route field blank or aggregation; the `Bachmann OPC` spelling is recorded as connected through the OPC Suite | `DTQ-Bachmann-Connector` is `Idea`, `NOT AVAILABLE`; `SFT-OPC-Suite` is recorded as connecting the `Bachmann OPC` machines |
| B&R | Integrated mostly through the aggregation route despite no native connector | `DTQ-B&R-Connector` is `Idea`, `NOT AVAILABLE` |
| Engel | Integrated with the route field mostly blank | `DTQ-Engel EMI-Connector` is `Idea`, `NOT AVAILABLE`; its comment: consider a custom connector for high-frequency time series |
| Schneider | Integrated with the route field blank, often concentrated in one plant | none named |
| Mitsubishi | Mostly not integrated, route under evaluation or aggregation | none named; the aggregation server needs its own Mitsubishi licence ([`SKILL.md`](../SKILL.md)) |
| Delta | Not integrated, routed to edge | none named |
| Omron | Integrated, edge | `DTQ-OMRON FINS-Connector` (Productive, USE) |
| Keyence | Integrated, edge, often concentrated in one plant | `DTQ-KEYENCECAM-Connector` and `DTQ-RS232-Connector` (both Productive, USE) |
| Philips | Not integrated, no route | none named |

Patterns, not counts:

- A family that looks integrated may be integrated at one plant only; check the plant spread.
- A native connector marked `NOT AVAILABLE` does not mean the family is unreachable: several such
  families are integrated over OPC UA.
- A family with the route field blank is "integrated and undocumented", not "no route needed".

## By PLC model - patterns

- **Siemens S7-300** is the largest single model family; it splits across integrated, not
  integrated, ongoing and blank status, and clusters in a few plants.
- **Rockwell `PLC 5069-L306ER`** has tended to carry no integrated machine and a route under
  evaluation, while **`Compact Logix 5370`** is the opposite (mostly integrated). The Rockwell
  question is model- and plant-specific, which is why the vendor line shows so many
  `EVALUATION ONGOING`.
- **`SIMATIC ET200SP`** is a distributed I/O family: check which PLC sits above it before reading
  the row as a PLC. A free-text blocker says the same kind of thing: "IM151-1 Standard: No PLC.
  Which PLC-Type is used?".
- **S7-200** is mostly integrated over the aggregation route; the protocol field says PPI.
- **Delta `DVP14SS2`** is the model behind the Delta rows not yet integrated.

## By network protocol - patterns

The protocol field is free text with many spellings (PROFIBUS appears as `PROFIBUS`, `Profibus`,
`PROFIBUS / MPI`, `Profibus / Profinet`, ...); a sizeable share of rows has none. Normalise the
spellings before grouping.

- **Modbus / TCP:** nearly all rows integrated, but the route field records the aggregation route
  only for part of them and is blank for the rest. The statement that the high Modbus integration
  rate reflects the aggregation-server route (`barrier-classes.md`) is
  visible in the route field for some rows and **not demonstrable from it for the others**. The
  bulk sits in one or two plants. ⟨How the Modbus machines of those plants reach the data
  platform. Who could supply it: the responsible IIAE.⟩ The edge `DTQ-MODBUS-Connector` is `Idea`
  with utilization `USE`, and no Modbus row records an edge route.
- **PROFIBUS, MPI and PPI (every spelling containing Profibus or MPI, including mixed entries):**
  mostly not integrated or without status. This fits the elicited ranking where S7 PROFIBUS is
  near the bottom. The `PPI` and `Profibus / Industrial ethernet` rows are aggregation-routed.
- **EtherCAT:** largely the Beckhoff family, routed to edge (clamps via
  `DTQ-EthercatIO-Connector`).
- **Ethernet/IP** is mainly the Rockwell protocol; many of these rows are under route evaluation.
- **PROFINET** is the largest named protocol and is mostly edge-routed.

## What the records do not give

⟨Cost per machine by family. A department roadmap slide shows a cost next to a list of plants, but
the slide's table structure did not survive extraction, so it cannot be turned into a unit cost.
Who could supply it: OD lead or regional IIAE, from the eCR calculation templates.⟩

⟨Whether a Machine List row is brownfield or greenfield: not a field in the list.⟩

## Sources

- Knowledge base `Graph/Machines` (notes quoting the `Machine-List` SharePoint export).
- Knowledge base `Graph/Connectors` (`ConnectorOverview-List`) for connector names and states.
- Knowledge base `ODEC Facts - Department KPIs and Roadmap Status` (staging, unverified) for the one cost
  slide.
- Registry references `barrier-classes.md` and
  `connectors.md` for the rules cited.
