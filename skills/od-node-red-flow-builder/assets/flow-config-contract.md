---
type: Skill Asset
title: Flow config contract
description: A one-page form a key user fills in before a flow is built - every UUID, limit, topic and shift setting the flow needs, using the key names the existing flows already use.
resource: ../SKILL.md
status: draft
tags: [information-integration-service, technical, node-red]
---
# Flow config contract

Fill this in **before** opening the editor; paste the finished table into the `config flow`
comment of the tab. It is the contract between the machine, the edge platform and the flow:
everything the flow needs to know about the outside world is a row here, and nothing from this
table appears as a literal inside a function.

Key names follow what the existing flows use (see
[`../references/corpus-census.md`](../references/corpus-census.md) for how to list the keys
live). Reuse an existing key name where one fits; a new name is a new interface.

## 1. Identity

| Item | Key (corpus name) | Value | Source | Filled by |
|---|---|---|---|---|
| Edge device the flow listens to | `datatronName` | ⟨edge device name⟩ | edge platform `GET .../datatrons` | IIAE |
| Machine | `machineName` | ⟨machine label; EQ id if one exists⟩ | Machine List | Plant ME |
| PLC / device name | `plcName` | ⟨⟩ | edge platform devices | IIAE |
| Flow name | tab label `<asset> - <artefact>` | ⟨⟩ | naming rule in `artefacts.md` | builder |

## 2. Input data points (one row per signal read)

| Concept (canonical name from `od-signal-standardization`) | Key | UUID | Value type (`valueBool/Integer/Double/String`) | Unit and scale | Confirmed on live data? |
|---|---|---|---|---|---|
| e.g. part counter | `datapointTotalPartCounter` | ⟨UUID⟩ | ⟨⟩ | ⟨⟩ | ⟨yes/no, date⟩ |
| e.g. part trigger | `datapointPartProducedTrigger` | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| e.g. machine status | `datapointMachineStatus` | ⟨⟩ | ⟨⟩ | ⟨state code table⟩ | ⟨⟩ |
| e.g. tool id | `datapointToolId` | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |

A mode or state that is compared with a constant carries a second row for the constant, named
`datapoint<Concept>Value` as the corpus does (for example `MachineModeManualValue`): the code table
is configuration, not logic. Rule: the filter node receives **all** input UUIDs from a single
key (`datapointConfigFilter`) so that adding a signal is a config change.

## 3. Output data points (one row per derived signal)

| Derived concept | Key | Output UUID | Registered on the edge platform? | Differs from every input UUID? |
|---|---|---|---|---|
| e.g. cycle time | `cycleTimeUUID` | ⟨⟩ | ⟨yes/no, date⟩ | ⟨yes⟩ |

Rule: an output UUID that equals an input UUID is invisible to its consumer; the analyser flags a missing one as
`output-uuid-not-set`.

## 4. Limits, tolerances, constants

| Quantity | Key | Value | Unit | Where it comes from |
|---|---|---|---|---|
| e.g. upper running tolerance | `valueUpperRunningTolerance` | ⟨⟩ | ⟨⟩ | ⟨spec / handbook / setter⟩ |
| e.g. micro-stop threshold | ⟨new key, name it for the concept⟩ | ⟨⟩ | s | ⟨agreed with Plant ME⟩ |

Rule: if the value is a number you typed into a function body, it belongs here (analyser check
`hardcoded-threshold`).

## 5. Time and shift

| Item | Value | Note |
|---|---|---|
| Shift boundaries (local time) | ⟨e.g. three eight-hour shifts⟩ | a three-shift reset is typically three cron injects spaced by the shift length; read the boundaries from the plant shift plan |
| Timezone of the Node-RED instance clock | ⟨⟩ | not recorded in any flow; check on the instance |
| State scope | flow context (per tab) or global | global is used at few instances (for example `Turno*` keys); prefer flow |
| Persistent context storage on? | ⟨yes/no⟩ | decides whether a deploy resets the accumulator |

## 6. Topics and broker

| Item | Value |
|---|---|
| Subscribe topic (wildcard at device or block level, filter by UUID) | ⟨`datatroniq/data/protob/plc/<edge-device>/<driver>/#`⟩ |
| Driver segment | ⟨one of the driver segments listed in `corpus-census.md`⟩ |
| Publish topic and family (spine, `CT/...`, or both) | ⟨⟩ |
| QoS in / out | ⟨default 0 in, node default out; QoS 2 only with a stated reason⟩ |
| Retain | ⟨off; retain is rare, turn it on only with a stated reason⟩ |
| Broker client ID unique across instances? | ⟨yes/no⟩ |

## 7. Sign-off

| Check | Who | Date |
|---|---|---|
| Every UUID verified against live data on the topic | IIAE | ⟨⟩ |
| Output UUIDs registered | IIAE | ⟨⟩ |
| Limits agreed | Plant ME | ⟨⟩ |
| Analyser reports zero blockers | builder | ⟨⟩ |
