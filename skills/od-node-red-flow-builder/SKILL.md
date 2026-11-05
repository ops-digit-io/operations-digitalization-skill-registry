---
name: od-node-red-flow-builder
description: >-
  Build, review and document Node-RED flows the way the OESL shop-floor estate already
  does it — the seven-group canonical layout, the protobuf PLCPacket schema over MQTT, the
  datatroniq and CT topic conventions, the standard function nodes (sysTime conversion both
  ways, UUID filtering, flow-config debug), link-node wiring, catch-based error handling,
  and the naming discipline the auto-documentation depends on. Use when writing or
  modifying a Node-RED flow for a machine or use case, reviewing someone else's flow,
  porting a flow between plant instances, debugging why a flow produces nothing, or asking
  how the flows across the ct-oesl Node-RED instances are structured.
license: MIT
allowed-tools: Read Grep Glob Write Edit
metadata:
  id: od-node-red-flow-builder
  tier: technical
  lane: information-integration-service
  scope: od
  origin: derived
  owner_role: IIoT Interface & Automation Engineer (IIAE)
  authority_level: author flows on a test instance; deploying to a prod instance is human-approved
  status: stable
  sources_read: 2026-11-05
  corpus: the exported ct-oesl Node-RED flows (count live, do not quote a remembered figure)
  requires: [od-context]
  composes: [od-equipment-integration, od-signal-standardization, od-acceptance-test, od-analytics-asset-build, od-node-red-flow-troubleshooting]
  derived_from:
    - ops-knowledge-graph/_knowledge/node-red-auto-docs/docs/** (exported flow JSON and generated docs)
    - ops-knowledge-graph/_knowledge/node-red-auto-docs/generate_docs.py
    - ops-knowledge-graph/_knowledge/10-Department/Machine integration.md
    - Node-RED auto-docs flow JSON re-read 2026-11-05 (ops-knowledge-graph/_knowledge/node-red-auto-docs/docs) for disabled flows, drivers, MQTT settings, timers and flow-config keys
    - Work vault (Work-OpsDigit-Knowledge), Graph/Connectors profile blocks for the TIA, S7, Beckhoff, Allen-Bradley and Omron connectors, read 2026-11-05
  okf:
    type: Agent Skill
    title: Node-RED flow builder
    tags: [information-integration-service, od, technical]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Node-RED flow builder

Read `od-context` first. This skill is the house pattern extracted from the flows across the
`ct-oesl-*-nodered-*` instances — not a Node-RED tutorial. Where the corpus is
consistent, that consistency is the standard; where it is not, this file says so.

## Where a flow sits

A Node-RED flow is the **transformation stage** between a connected machine and a use case.

```text
PLC ──(ingress variant)──► IIoT Edge Platform ──MQTT──► Node-RED ──► IIoT Edge Platform
                                                                          │ offload
                                                                          ▼
                                                    Databricks ──► Azure Storage Account
                                                                        (Parquet)
```

Flows publish back onto the MQTT spine; the platform offloads from there through
**Databricks** to an **Azure Storage Account** in **Parquet**, which is what analytics and
dashboards read. A flow that derives a signal is therefore writing something that lands in
the lake — which is why the output UUID and the `isDelta` semantics matter beyond the flow.
The machine is connected per `od-equipment-integration` (guidance route); the signal standard is set
per `od-signal-standardization`; the flow is what turns raw `PLCPacket` messages into the
derived signal a use case consumes — a cycle time, a part count, a quality event, an alert.

Instances are named **`ct-oesl-<plant-code>-nodered-<prod|test>[N]`**. Full inventory:
[`references/instances.md`](references/instances.md).

> **Build on a `test` instance. Deploying to a `prod` instance is human-approved.**

## The references

| File | Use it for |
|---|---|
| [`references/artefacts.md`](references/artefacts.md) | **Look here first.** What the flows actually build - artefact families, a sanitized generalized example per artefact, the reusable building blocks, and the naming convention |
| [`references/transformation-patterns.md`](references/transformation-patterns.md) | The thirteen patterns the estate is built from, with implementations and what breaks each |
| [`references/composing-transformations.md`](references/composing-transformations.md) | **When no pattern fits.** The four questions that classify any transformation, the multi-input latch-and-evaluate shape, windowing, timer-driven emit, composition rules, and the two timestamp conventions |
| [`references/streaming.md`](references/streaming.md) | How the real-time path works - the hops and their guarantees, split/rbe/delay/join, QoS, ordering, flow context, back-pressure |
| [`references/architecture.md`](references/architecture.md) | An annotated walkthrough of one canonical flow, node by node |
| [`references/plc-packet.md`](references/plc-packet.md) | The PLCPacket protobuf schema and the packed `sysTime` |
| [`references/topic-conventions.md`](references/topic-conventions.md) | Both MQTT topic grammars and their vocabularies |
| [`references/standard-functions.js`](references/standard-functions.js) | The standard function bodies, verbatim |
| [`references/deployable-flow.md`](references/deployable-flow.md) | **Read before generating a flow file.** The palette module, the config nodes the corpus exports do not contain, the structural envelope, and how to verify a flow actually starts |
| [`assets/protobuf-schema-bootstrap.flow.json`](assets/protobuf-schema-bootstrap.flow.json) | **Importable flow.** Writes the PLCPacketList schema to the instance's file store — run once on any new instance before any decode/encode flow |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | **How the step runs in the chain**: where logic belongs, streaming against scheduled work, flow library classes, legacy-middleware migration, handoff contract, AI agent operating notes |
| [`references/instances.md`](references/instances.md) | Instance naming, site codes, how to count flows live, and the documentation pipeline |
| [`references/corpus-census.md`](references/corpus-census.md) | **How to census the corpus live** (no figures): disabled flows, driver segments, MQTT QoS and retain settings, cron and delay patterns, the flow-config key vocabulary, global-context use, HTTP and UI use, and how to read each |
| [`assets/flow-config-contract.md`](assets/flow-config-contract.md) | **Form.** The config contract a key user fills in before building - identity, input and output UUIDs, limits, shift and timezone, topics - using the key names the flows already use |

**A broken flow rather than a new one?** Use `od-node-red-flow-troubleshooting`, which runs
a static analyser over the flow JSON.

> **The corpus these references come from is incomplete in one specific way.** The per-flow
> exports contain a tab and its nodes and **nothing else** — there are **no
> config nodes** in them. So the patterns here describe a correct transformation but not a
> *deployable file*: `decode`/`encode` need the `node-red-contrib-protobuf` palette module,
> and both the MQTT and protobuf nodes reference config nodes that must be added by hand.
> [`deployable-flow.md`](references/deployable-flow.md) covers that layer, verified against
> Node-RED v5.0.4, and
> [`assets/protobuf-schema-bootstrap.flow.json`](assets/protobuf-schema-bootstrap.flow.json)
> is an importable flow that puts the schema on the instance.

## The canonical seven-group layout

Most flows carry a group called *prepare and convert payload* and one called *mqtt
connection and message decoding*. This is not a coincidence — it is the template.

```text
┌ config flow ────────────────────────────────────────────
│   inject "Trigger once"  →  change "Set flow config"  →  function "Debug flow config"  →  debug
│   └ set inputs for config flow ─────────────────────────
│
├ functional flow ────────────────────────────────────────
│   ├ mqtt connection and message decoding ───────────────
│   │     mqtt in → decode(PLCPacketList) → function "filter uuids"
│   │            → split "flatten PLCPacket Array" → function "Convert sysTime" → link out
│   │
│   ├ set message filters ───────────────────────────────
│   │     link in → switch(es)  →  link out
│   │
│   ├ <use-case-specific group> ───────────────────────── e.g. "calculate cycle time based
│   │     the actual logic: lookup, join, calculate         on triggers",
│   │                                                       "lookup uuid to label"
│   │
│   ├ prepare and convert payload ───────────────────────
│   │     link in → change "format msg.payload"
│   │            → change "prepare for protob encoding"
│   │            → function "Convert sysTime back"
│   │
│   └ message encoding and connection ───────────────────
│         encode(PLCPacketList) → mqtt out
│
└ error handling (ungrouped, by convention)
      catch → change "get env variables of flow" → template "create error message" → debug
```

The commonest wiring pairs in the corpus are `change → function`, `switch → change`,
`function → debug`, `change → change` and `inject → change`. The MQTT spine is
`mqtt in → decode → function → split → function → function → encode → mqtt out`. If your flow
does not look like that, have a reason.

Full annotated walkthrough of an illustrative flow:
[`references/architecture.md`](references/architecture.md).

## The message: PLCPacket over protobuf

Every `datatroniq/*` message is a protobuf `PLCPacketList`. Full schema and field
semantics: [`references/plc-packet.md`](references/plc-packet.md).

```protobuf
message PLCPacket {
  string uuid = 1;             // the data point — this is the join key, not the name
  int32  sequence_number = 2;
  uint64 sys_time = 3;         // packed: seconds<<32 | nanos — never a plain epoch
  uint64 plc_time = 4;
  oneof measured_value {
    sint64 value_integer = 5;  string value_string  = 6;
    double value_double  = 7;  bool   value_bool    = 8;  bytes value_bytes = 9;
  }
  bool is_delta = 10;
}
message PLCPacketList { repeated PLCPacket plc_packets = 1; }
```

Two things bite everybody:

1. **`sysTime` is a packed 64-bit value, not a timestamp.** Upper four bytes are seconds
   since epoch, lower four are nanoseconds. Decode it on the way in and re-pack it on the
   way out — that is exactly what the two standard functions do. Reading it as
   milliseconds gives a date in the year 2262.
2. **`uuid` identifies the data point; the human label lives elsewhere** — in the IIoT
   edge platform's data-point config, fetched per datatron. That is why many flows carry a
   *lookup uuid to label* group. Never hardcode a label as if it were the identity.

## The standard function nodes

Copy these; do not rewrite them. Verbatim source:
[`references/standard-functions.js`](references/standard-functions.js).

| Node name | Does |
|---|---|
| `Debug flow config` | Echoes the flow variables set by *Set flow config* so a misconfiguration is visible at deploy, not at 3 a.m. |
| `Convert sysTime (UTC timestamp)` | Unpacks `sysTime` → epoch milliseconds |
| `Convert sysTime back (UTC timestamp)` | Re-packs epoch milliseconds → `sysTime` before encoding |
| `filter uuids` | Keeps only the `plcPackets` whose `uuid` is in the flow config |
| `set datapointConfigFilter` | Builds the filter for the data-point config query |
| `calculate timerange between cycle_start and cycle_end event` | The cycle-time primitive |
| `create json payload` | Assembles the outbound payload |

## Configuration: flow variables, never literals in logic

The config group is the single place a flow is bound to a machine. `Set flow config` is a
`change` node writing **flow-scoped** variables:

```json
{"t":"set","p":"datatronName",              "pt":"flow","to":"ski4-bm01","tot":"str"}
{"t":"set","p":"datapointTotalPartCounter", "pt":"flow","to":"85f29811-…","tot":"str"}
{"t":"set","p":"datapointPartProducedTrigger","pt":"flow","to":"59fa510e-…","tot":"str"}
```

Everything downstream reads `flow.get(...)`. **This is what makes a flow portable between
plants** — porting is editing one change node, not hunting UUIDs through function bodies.
A UUID appearing inside a `function` node body is a defect.

Data-point config is fetched from the IIoT edge platform rather than typed in:
`GET {url}/{datatronId}/data_points` with the Bearer header from `flow.get("headers")` —
the flows that fetch it do so under a *get variable config from iiot edge platform* group.

## Topics

Two families. Full grammar and segment vocabulary:
[`references/topic-conventions.md`](references/topic-conventions.md).

**`datatroniq/data/protob/plc/<edge-device>/<driver>/<id>`** — the dominant family, protobuf
`PLCPacketList`. The `<driver>` segment names the connector family: `dqcdc`, `cifx`, `tia`,
`ads`, `abrock`. A flow usually **subscribes and publishes on the same broker**, reading
raw packets and writing derived ones back with a new `uuid`.

**`CT/<BA>/<region>/<country>/<plant>/<area>/<sub-area>/<machine>/<signal>`** — the
ISA-95-shaped hierarchical topic, e.g.
`CT/OESL/AS/CHN/<plant>/<area>/<sub-area>/<machine>/<signal>` (illustrative). Vocabulary:
BA `OESL` | `MFS`; region `AS` | `NA`; country `CHN` | `USA`; plant `QDA` | `SPR` | `CSHZ`.

**Publishing a derived signal keeps `is_delta` semantics honest.** The standard pattern
sets `payload.isDelta` explicitly and assigns the *output* UUID from flow config before
encoding — it does not reuse the input packet's identity.

## The transformation itself

Thirteen patterns cover almost every flow in the estate. Full implementations and failure
modes: [`references/transformation-patterns.md`](references/transformation-patterns.md).

| # | Pattern | Shape |
|---|---|---|
| P1 | **Delta gate** | `switch` on `payload.isDelta` — turns a cyclic sample stream into events |
| P2 | **Accumulator** | `flow.get(k) \|\| 0` → increment → `flow.set` → publish, with a separate reset |
| P3 | **Two-event time range** | Capture start, capture end, subtract; guard `NaN` and negative |
| P4 | **Threshold crossing** | A function flags `isHigh` on every sample; `rbe` turns it into two clean edges |
| P5 | **Value mapping** | A chain of `eq` switches (single flag) or nested `if` (several flags), code → named state |
| P6 | **Lookup table** | CSV loaded once into flow context; `filter` per message |
| P7 | **UUID → label** | Enrich from the edge platform's data-point config |
| P8 | **Build from nothing** | Construct a packet from config; pack `sysTime` yourself |
| P9 | **Clear the oneof** | Delete the value fields that do not apply |
| P10 | **Composite string** | Split a packed `valueString`; validate every field |
| P11 | **OEE chain** | Availability × performance × quality, each published, then multiplied |
| P12 | **Windowed extremum** | Latch the running max/min while a threshold-bounded window is open |
| P13 | **Liveness watchdog** | Detect a heartbeat toggle; publish "not alive" on a timeout, node-scoped `context` |

**P1 to P11 are mostly single-input shapes, and single input is the minority.** Most
flows that carry data-point config read **two or more** data points — every tolerance check,
quality event and composite KPI is multi-input. That shape (build a filter array, latch each
input into flow context, evaluate on the triggering one) is in
[`composing-transformations.md`](references/composing-transformations.md), along with
windowing, timer-driven emit and the cold-start guard the latch needs.

### When none of them fits

Do not force the nearest pattern. Classify the transformation with four questions — **how
many inputs · does it need history · what drives the output · what is the output** — then
compose it from the primitives. That method, the composition order, and the pre-flight
checklist are in
[`composing-transformations.md`](references/composing-transformations.md).

Two prerequisites people discover late, both of which stop a flow dead:

- **The output data point must already exist** on the edge platform's data-point config. A
  derived UUID is registered, not invented; until it is, everything downstream ignores your
  packet.
- **Check which envelope and clock you are on.** Most of the estate is packed `sysTime` on
  protobuf topics, but some flows also carry `plcTime` — the PLC's own clock, and the more
  truthful source for anything measuring machine behaviour — and a few read a JSON
  envelope whose `sys_time` is a formatted local-time string, not a packed integer.

### Standards for any transformation

| Rule | Why |
|---|---|
| **Config from `flow`, never a literal** | Porting is one change node. A UUID in a function body is a defect |
| **Unpack `sysTime` in, re-pack out — both, always** | Flows exist that ship one without the other; every downstream timestamp is then wrong |
| **Set the output UUID from config** | A derived packet under the input UUID is invisible to its consumer — many flows never set one |
| **Exactly one `value*` field reaches the encode** | `measured_value` is a protobuf `oneof`; flows exist that violate it |
| **Set `isDelta` explicitly on the output** | State what the derived signal is; do not inherit |
| **Guard, then warn, then drop** | A bare `return null` makes a dropped message untraceable. `node.error`/`node.status` are barely used anywhere in the corpus — that is the gap |
| **Wire the `else`** | Most `else` branches go nowhere. An unmapped code is a finding |
| **Tolerate `undefined` context** | Deploy clears flow context |
| **Structure to the data model, not the PLC layout** | The most-recorded blocker in the estate |

## The data structure you are working on

Three layers travel together, and confusing them causes most transformation bugs.

**1 · The protobuf packet** — what the wire carries. `plcPackets[]`, each with `uuid`,
`sysTime` (packed), `sequenceNumber`, `plcTime`, `isDelta`, and exactly one of
`valueInteger` / `valueString` / `valueDouble` / `valueBool` / `valueBytes`. Full schema:
[`plc-packet.md`](references/plc-packet.md).

**2 · The Node-RED message envelope** — what the flow manipulates:

| Property | Set by | Note |
|---|---|---|
| `msg.payload` | decode, then every node | After the split, one packet |
| `msg.parts` | `split` | **Must be deleted before the encode** |
| `msg.protobufType` | `decode` | Bookkeeping; delete before the encode |
| `msg._msgid` | Node-RED | Delete before the encode |
| `msg.topic` | `mqtt in` | The source topic; useful for routing |
| `msg.payload.label` | P7 enrichment | **Not a PLCPacket field** — remove before the encode |

**3 · Flow context** — the state. Per-tab, cleared on deploy. Configuration keys (`datatronName`, `datapoint*`)
and accumulators (`ShiftPartProduced`) live here. `global` is used rarely and couples
flows that should not know about each other — prefer `flow`.

## Error handling

Most well-built flows carry a `catch`. The house pattern is four nodes and is worth copying exactly:

```text
catch (all nodes)
  → change  "get env variables of flow"   $env('NR_FLOW_ID'), $env('NR_FLOW_NAME')
  → template "create error message"
       [error] flow_id: {{flow_id}}, flow_name: {{flow_name}},
               node_id: {{error.source.id}}, node_name: {{error.source.name}}, {{error.message}}
  → debug
```

Because the message carries the flow *name* and the failing *node* name, an error is
traceable without opening the editor — which is the whole reason node naming matters below.

**What an error actually does to the stream.** The catch receives it and the message is
**dropped from its chain**. Nothing retries, nothing is dead-lettered, the stream does not
pause. So an error is a *lost message*, and the flows with no `catch` lose them
invisibly.

**Two error paths, and both are needed:**

| Path | Catches | Add it |
|---|---|---|
| `catch` (scope: all nodes) | Thrown exceptions — a lookup on `undefined`, a bad JSON parse | Always; use scope *all*, not selected |
| An explicit guard in the function | Business-invalid values — `NaN` cycle time, negative duration, unmapped code | Wherever the pattern has a "silent drop" branch |

The guard is the one people skip. The house pattern returns `null`, which drops the message
with no trace:

```javascript
if (isNaN(msg.payload.cycle_time)) { return null; }        // invisible
```

Make it diagnosable for one extra line:

```javascript
if (isNaN(msg.payload.cycle_time)) {
    node.warn(`cycle_time NaN for ${msg.payload.uuid} — start event missing`);
    return null;
}
```

Across the whole corpus `node.error` and `node.status` are barely used. That is
the single biggest observability gap in the estate: flows drop messages correctly and say
nothing about it.

**Some flows exist whose entire artefact is `Error Handling`** — a dedicated tab collecting
and routing errors rather than a per-flow catch. Check whether the instance has one before
building another.

## Build so the documentation writes itself

`generate_docs.py` clones every `ct-oesl-*-nodered-*` repo and generates a page per flow
from **four fields and nothing else**: the tab `label`, the tab `info`, each node's `name`
and `info`, and each group's `name`. There is no other input. What you name is what gets
documented.

The corpus's honest state, as a pattern (measure it live; see `references/artefacts.md`):

| | |
|---|---|
| Groups named | mostly |
| Nodes named | the majority |
| Comment nodes with a body | a minority |
| **Flows carrying a tab description** | **almost none** |

Groups are disciplined. Flow-level descriptions are essentially absent — most flows document
their internals and never say what the flow is *for*. That is the single highest-leverage
fix available in this corpus, and it costs one field.

**So, when you build:**

1. **Write the tab description.** One paragraph: what this flow produces, for which machine,
   consumed by which use case. This is the `info` on the tab and it becomes the page's
   opening.
2. **Name every node.** An unnamed node renders as its bare type in the docs table and in
   the error message.
3. **Use the standard group names.** They are what makes the generated pages comparable.
4. **Put the configuration contract in the `config flow` comment node.** The best flows in
   the corpus document, in that comment, exactly which flow variables must be set and where
   to get each one. Copy that habit.

## Guardrails

- **Never hardcode a secret.** The corpus has contained **literal Teams webhook URLs and
  literal Bearer tokens** in committed flow JSON. Those repositories are the documentation
  source and are cloned by the doc generator. Use `$env(...)` / `env.get(...)` — many flows
  already do — or Node-RED credentials, never a literal. Do not copy an existing flow's
  literal forward; when you touch a flow that has one, replace it.
- **Never deploy to a `prod` instance without approval.** Build and prove on `test`.
- **Never invent a UUID.** Fetch the data-point config from the edge platform.
- **Never change the signal standard from inside a flow.** A per-plant fix-up buried in a
  `function` node is how cross-plant comparability is lost — that is a
  `od-signal-standardization` decision, Consultation with Plant ME / Plant IT.
- **Never leave `debug` nodes enabled at volume in prod.** Debug nodes
  are a development aid.
- **A flow is not done until its acceptance test passes** end to end — machine → connector →
  edge → flow → data platform → the asset the plant opens. See `od-acceptance-test`.

## Reviewing someone else's flow

1. Does the tab carry a description? (Few do — ask for one.)
2. Is every UUID in `Set flow config` rather than in a function body?
3. Are the two `sysTime` conversions present and paired? An outbound packet without the
   re-pack is the most common silent corruption.
4. Does `filter uuids` read from flow config?
5. Is there a `catch` with the four-node error pattern?
6. Any literal token, password or webhook URL?
7. Do the group names match the canonical seven?
8. Does the output topic and the output UUID differ from the input, deliberately?
