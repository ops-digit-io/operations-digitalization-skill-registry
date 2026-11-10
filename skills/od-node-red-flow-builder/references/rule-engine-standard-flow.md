---
type: Skill Reference
title: Rule engine standard flow
description: "The standard rule-engine flow layout: config flow, input, calculation, output to DATATRON, the node groups and the variables each needs."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [node-red, rule-engine, department-package]
derived_from:
  - "Department knowledge base, OD Department Knowledge/OD-instance/30-skills/ops-rule-engine.skill/references/standard-flow.md, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `ops-rule-engine.skill/references/standard-flow.md` (the master).

# Standard rule-engine flow: anatomy and conventions

Distilled from the production flows in `rule-engine-examples/` (AC402, M1072 Rosenberger, BLM AST30,
Pink leak test, Line 15 Final Gauge, Grazioli, Erlas 2). Every rule-engine flow reads raw
datapoints (DPs) from a DATATRON MQTT stream, derives a value, and writes it back as a new
**virtual datapoint** (its own UUID, pre-created in DATATRON) on the same MQTT/protobuf format.

## Contents
1. Data model (PLCPacket)
2. The six groups of a standard flow
3. Naming conventions
4. MQTT topics
5. Timestamps (sysTime)
6. Writing the output packet
7. Deviations seen in the examples (and which to follow)

---

## 1. Data model

MQTT payload = protobuf `PLCPacketList { repeated PLCPacket plcPackets }`,
schema file `/data/plcschema.proto` (protobuf-file config node, `keepCase: false`).

| field | type | notes |
|---|---|---|
| `uuid` | string | datapoint id |
| `sysTime` | uint64 | high 32 bit = unix seconds, low 32 bit = nanoseconds |
| `plcTime` | uint64 | PLC timestamp; decoded as string, many flows `$number()` it or delete it |
| `isDelta` | bool | `true` = real change; `false` = snapshot/re-send (e.g. after reconnect) |
| `valueInteger` | int64 | **arrives as a string** after decode (`"1"`, `"-9"`) - always `Number()` it |
| `valueDouble` | double | |
| `valueBool` | bool | |
| `valueString` | string | |

A batch can contain many packets, several of them for the same UUID. DATATRON typically
publishes **on change**, so the DPs you need rarely arrive together in one batch.

The encoder silently **drops unknown fields**. If the result is not in one of the four
`value*` fields, the published packet contains only uuid + timestamp.

## 2. The six groups

```
[config flow]
  inject "Trigger once" (once) -> change "Set flow config" (all UUIDs as flow vars)
  -> function "set datapointConfigFilter" (array of input UUIDs)
  -> function "Debug flow config" -> debug
  (+ optional: template "mapping table" -> csv -> change "move to flow variable")

[mqtt connection and message decoding]
  mqtt in (topic from user) -> decode PLCPacketList -> function "filter uuids"
  -> split "flatten PLCPacket Array" -> function "Convert sysTime (UTC timestamp)" -> link out

[set message filters / remember latest values]
  link in -> switch on payload.uuid (one output per input DP, compared to flow var)
  -> change "value for <Name>" (flow.value<Name> = payload.<field>) -> link out

[calculate <Output>]           (the only part that differs between use cases)
  link in -> function "calculate <Output>" (reads flow.value*, returns value)
  -> [rbe "filter on change"] -> link out

[prepare, encode and publish]
  link in -> change "format msg.payload" (payload.uuid = flow.datapoint<Output>, isDelta=true)
  -> change "prepare for protob encoding" (delete parts/protobufType/_msgid, move payload -> payload.plcPackets[0])
  -> [trigger "intervaltime" = resend every N min]
  -> function "Convert sysTime back (UTC timestamp)" -> encode -> mqtt out

[error logging]
  catch -> change (NR_FLOW_ID / NR_FLOW_NAME) -> template "[error] ..." -> debug
```

Store-then-calculate must be **serial** (switch -> change -> calc). Wiring the calc function in
parallel with the store nodes (as in example 16) races: the calc may run before the value is stored.

## 3. Naming conventions

- Flow variables: `datapoint<Name>` = UUID, `value<Name>` = latest raw value,
  `time<Name>` = its sysTime (ms), `datapointConfigFilter` = input UUID array,
  `machineName` / `datatronName` = machine id.
- `<Name>` is PascalCase meaning, e.g. `datapointMachineModeAutomatic`, `datapointCycleTimeNormalized`.
- Output DP naming used in plants: `...Normalized`, `...Mapped`, `...Trigger`, `...Counter`,
  `ShiftPartProduced`, `totalParts...`, `downtime`.
- Tab label: `<Machine / Line> (<EQ number>) - <What it produces>`, e.g.
  `Rosenberger Double Head - M1072 (EQ40015929) - Cycle Time Normalization`.
  `(OK)` prefix is used by the team to mark flows verified in production.

## 4. MQTT topics

The **user supplies the input topic**. Seen formats:

- `datatroniq/data/protob/plc/<datatron>/<driver>/<n>` (driver: `cifx`, `tia`, `opcua`)
- with wildcard: `datatroniq/data/protob/plc/datatron-eq40015929/cifx/#`

Output topic conventions seen:
- same topic as input without wildcard (Erlas, Pink, Grazioli, AC402, Helium) - the filter
  drops the output UUID, so no loop;
- `datatron-eqXXXX/cifx/#` in -> `eqXXXX/cifx` out (M1072, BLM);
- different channel number (Line 15: `tia/#` in -> `tia/10` out).

If the user did not state the output topic, ask. If they don't know, default to the input
topic without the trailing `/#` and say so. Broker: `emqx.mqtt.svc:1883`, config node id
`a5b9953ab68b73bb` (older flows: `877128a3121fd6c2`, same broker).

## 5. Timestamps

Decode side: `ms = (sysTime >> 32) * 1000 + round((sysTime & 0xFFFFFFFF) / 1e6)` - use
this ms value for durations (downtime = end - start).

Encode side: the output packet is stamped with **now** in the same 32/32 format.
Use `Math.floor(ms/1000)` for the seconds part - the legacy flows use `Math.round`, which puts
the timestamp up to 1 s in the future for the second half of each second.

## 6. Writing the output packet

Build a **fresh** payload containing only the value field, then `format msg.payload` adds
`uuid` and `isDelta: true`. Reusing the incoming packet (legacy style) requires deleting the
other `value*` fields and `plcTime`, which is easy to forget.

Output field by result type: counts/ints -> `valueInteger`; measured/derived numbers
(cycle time, leak rate, durations in s) -> `valueDouble`; triggers/flags -> `valueBool`;
states/text/part numbers -> `valueString`.

## 7. Deviations in the examples

| seen | follow instead |
|---|---|
| calc needs both DPs in one batch (13 broken) | store latest values in flow context |
| calc wired in parallel to store nodes (16) | serial chain |
| `filter uuids` with a single string (21, `uuids.includes` works by substring accident) | always an array |
| `Math.round` in sysTime back | `Math.floor` |
| encode not wired to mqtt out (12, 13) | always wire it |
| `debugInfo`, `machine`, etc. left in payload | fresh payload with one value field |
| counters in plain flow context | fine, but they reset on Node-RED restart unless a persistent context store is configured - tell the user |
