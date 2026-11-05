---
type: Skill Reference
title: Architecture
description: An illustrative canonical flow walked end to end, with placeholder values, so the shape of a real flow is concrete before you build one.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [node-red, architecture]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# A canonical flow, node by node

Walkthrough of an illustrative flow, `<asset> - Part Counter Trigger` on `ct-oesl-<site>-nodered-<prod|test>`,
representative of the house pattern. Values are placeholders, not real identifiers. Read alongside
[`standard-functions.js`](standard-functions.js) and [`plc-packet.md`](plc-packet.md).

## What it does

Watches a total-part-counter data point on one machine, and every time the counter moves
(`isDelta` true) publishes a *part produced* trigger packet back onto the spine under a
different UUID. That is the whole use case: turn a counter into an event other flows and
use cases can consume.

## Group 1 — `config flow` (+ `set inputs for config flow`)

```text
inject "Trigger once"
  → change "Set flow config"          ← the ONLY place machine identity appears
  → function "Debug flow config"
  → debug
```

`Set flow config` writes three flow-scoped variables:

| Variable | Value | Is |
|---|---|---|
| `datatronName` | `<edge-device>` | the edge device |
| `datapointTotalPartCounter` | `<input-uuid>` | **input** UUID |
| `datapointPartProducedTrigger` | `<output-uuid>` | **output** UUID |

Two UUIDs, in and out, is the shape of every derive-a-signal flow. Nothing downstream
contains either literal.

The group's `comment` node carries the flow's configuration contract in prose — which
variables must be set, what each means, and where to get it (query the edge platform by
`datatronName` / `plcName`). That comment is the best documentation habit in the corpus:
only a minority of comment nodes carry a body, and this is what the good ones look like.

## Group 2 — `mqtt connection and message decoding`

```text
mqtt in  (topic: datatroniq/data/protob/plc/…, qos 1)
  → decode "DecodeProto"           protoType: PLCPacketList
  → function "filter uuids"        keeps only the configured input UUID
  → split "flatten PLCPacket Array"   arraySplt: 1
  → function "Convert sysTime (UTC timestamp)"
  → link out
```

Order matters and is counter-intuitive: **filter before split.** `filter uuids` runs over
`msg.payload.plcPackets` while it is still an array, so one filter pass replaces one per
packet. Splitting first would work and cost more.

`link out` ends the group. Groups are wired to each other through link nodes rather than
long cross-canvas wires — `link in` / `link out` pairs are used throughout the corpus.
This is what keeps the generated flow diagram readable.

## Group 3 — `set message filters`

```text
link in → switch "is delta true >> 1" → (output 1) → …
                                        (output 2) → nothing
```

The gate that makes this an event flow rather than a sampling flow: only packets reporting
a change pass. The unused second output is deliberate and visible — a dropped branch you
can see beats an implicit one.

## Group 4 — `lookup uuid to label, including postprocessing`

Here it is minimal: a `change` node setting `payload.valueBool = true`, then `link out`.
The counter's *value* is irrelevant; the fact that it moved is the signal.

In flows where the label matters, this group holds the data-point-config lookup — many
flows carry it, and some of those fetch the config live from the edge platform
(`GET {url}/{datatronId}/data_points`) rather than embedding it.

## Group 5 — `prepare and convert payload`

```text
link in
  → change "format msg.payload"
        set    payload.isDelta = true                    (bool)
        set    payload.uuid    = flow.datapointPartProducedTrigger   ← OUTPUT identity
        delete payload.valueInteger
  → change "prepare for protob encoding"
        delete parts, protobufType, _msgid               (Node-RED bookkeeping)
        delete payload.valueDouble                       (oneof: send exactly one)
        move   payload → payload.plcPackets[0]           ← rebuild the List wrapper
  → function "Convert sysTime back (UTC timestamp)"
```

Three things happen here that are each a common bug when missing:

1. **The UUID is replaced.** A derived packet that carries the input UUID is a duplicate of
   the source, not a new signal.
2. **The `oneof` is cleaned.** `valueInteger` and `valueDouble` are deleted so only
   `valueBool` remains. Two value fields is a malformed `oneof`.
3. **The payload is re-wrapped** into `plcPackets[0]`. `PLCPacketList` expects an array;
   without the move the encode succeeds and decodes to nothing useful.

## Group 6 — `message encoding and connection`

```text
encode "EncodeProto"   protoType: PLCPacketList, same protofile as the decode
  → mqtt out  (topic: datatroniq/data/protob/plc/<edge-device>/ads/<id>, same broker)
```

Same broker as the input, same family, different data block. `ads` is the driver segment —
a Beckhoff ADS connector.

## Error handling — ungrouped, by convention

```text
catch (all nodes)
  → change "get env variables of flow"
        msg.flow_id   = $env('NR_FLOW_ID')      (jsonata)
        msg.flow_name = $env('NR_FLOW_NAME')    (jsonata)
  → template "create error message"
        [error] flow_id: {{flow_id}}, flow_name: {{flow_name}},
                node_id: {{error.source.id}}, node_name: {{error.source.name}}, {{error.message}}
  → debug
```

Most well-built flows carry this. It is why node naming is not cosmetic: `{{error.source.name}}` is
the failing node's `name` field, so an unnamed node produces an error message that
identifies nothing.

## The shape in one line

```text
config → [mqtt in → decode → filter → split → convert] → filter → transform
       → [format → rewrap → convert back → encode → mqtt out]
                                                            ⟂ catch → env → template → debug
```

Everything specific to one machine lives in the first box. Everything else is the
template. That is why porting this flow to another machine is editing one change node — and
why a UUID anywhere else is a defect.
