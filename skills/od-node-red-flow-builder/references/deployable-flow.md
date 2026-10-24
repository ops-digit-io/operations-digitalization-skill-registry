---
type: Skill Reference
title: Deployable flow
description: "The half that is not the transformation: tabs, groups, wires, config nodes, and the traps that make a flow import but not run."
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [node-red, deployment]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Making the flow actually deployable

The transformation is the interesting half. This is the other half — the structure and the
configuration layer Node-RED needs before a flow will start.

**Why this file exists.** The corpus these references are derived from is the *per-flow*
export produced by `node-red-auto-docs`, which contains the tab and its nodes and **nothing
else**. Across all 825 exports there are **zero config nodes**: no `mqtt-broker`, no
`protobuf-file`. A flow built from the patterns alone therefore imports with dangling
references, connects to no broker, and decodes nothing.

Everything below was **verified by deploying a generated flow into Node-RED v5.0.4**, which
reported `Started flows` only once all three pieces were present.

---

## 1 · The palette module

`decode`, `encode` and `protobuf-file` are **not core Node-RED**. They come from:

```bash
npm install node-red-contrib-protobuf     # v1.1.2 verified
```

It registers exactly three types: `decode`, `encode`, `protobuf-file`.

Without it, Node-RED starts, loads the flow, and then sits at:

```
[info] Waiting for missing types to be registered:
 -  decode
 -  encode
 -  protobuf-file
```

The flow is **not running** in that state, and nothing else in the log says so. If a flow
looks deployed but moves no data on a fresh instance, check the log for this before anything
else.

**Other contrib modules in use across the corpus**, by node-type prefix — same check as
above: `[info] Waiting for missing types to be registered` names exactly which one is
missing.

| Prefix / type | Likely module | Where it shows up |
|---|---|---|
| `OPCUA-IIoT-*` (Read, Write, Browser, Inject, Response, Result-Filter, Listener) | an OPC-UA client nodeset (e.g. `node-red-contrib-iiot-opcua`) | 59+ nodes, mostly Caluire and the IIoT OPC-UA browser/test flows |
| `ui-*` **and** `ui_*` (gauge, button, text, form, dropdown, table, chart, …) | `node-red-dashboard` | OEE and alerting dashboards. **Both an underscored and a hyphenated family appear side by side** — e.g. `ui-gauge` and `ui_gauge`, `ui-button` and `ui_button` — consistent with two dashboard-module generations both being in use across the estate, not one typo. Confirm which generation a target instance actually has before reusing a UI node type from the other family |
| `influxdb in` / `influxdb out` | `node-red-contrib-influxdb` | Sun Prairie, Ponta Grossa |
| `postgres` | a PostgreSQL contrib node | Data-quality scoring (`ct-oesl-wth1`) |
| `sparkplug-payload` | a Sparkplug B decode/encode node | One MQTT Sparkplug test flow (`ct-oesl-wth2`) |
| `soap request` | a SOAP contrib node | One webserver-integration flow (`ct-oesl-spr`) |
| `data-generator`, `uuid`, `counter`, `e-mail` | small single-purpose contrib nodes | Scattered, one or two flows each |

**None of this is guaranteed to be on every instance.** It names what the exported flows use,
not what is installed everywhere — an instance that has never run an OPC-UA or dashboard
flow may carry none of these. Check the target instance's palette before reusing a node type
outside core, the same way you would for `node-red-contrib-protobuf` above.

## 2 · The config nodes

Config nodes have **no `z`** (they do not belong to a tab) and no position. They sit in the
same top-level array as everything else.

### `mqtt-broker`

```json
{
  "id": "<16 hex chars>",
  "type": "mqtt-broker",
  "name": "plant broker",
  "broker": "⟨host⟩",
  "port": "1883",
  "clientid": "⟨unique per instance⟩",
  "autoConnect": true,
  "usetls": false,
  "protocolVersion": "4",
  "keepalive": "60",
  "cleansession": true
}
```

Every `mqtt in` / `mqtt out` node references it by `"broker": "<that id>"`.

> **`clientid` must be unique on the broker.** If two instances or a cloned configuration
> share one, the broker disconnects one and **the client cannot tell** — see
> [`streaming.md`](streaming.md). Name it after the instance and the flow, not the machine.

**Credentials are not in the flow file.** Username and password live in
`flows_cred.json`, encrypted. Exporting a flow does not carry them, and importing one does
not create them — they are entered on the target instance. That is a feature: it is why a
flow JSON is safe to commit, and why the 42 flows carrying literal webhook URLs and tokens
are a defect rather than a convention.

### `protobuf-file`

```json
{
  "id": "<16 hex chars>",
  "type": "protobuf-file",
  "protopath": "/data/plcschema.proto",
  "watchFile": false,
  "keepCase": false
}
```

`decode` and `encode` reference it by `"protofile": "<that id>"`, plus
`"protoType": "PLCPacketList"`.

**`/data/plcschema.proto` has to exist on the instance.** The estate writes it from a flow —
35 flows carry a `Generate Text for Protobuffer Schema` function and an
`Inject protobuffer config once` tab that writes the schema to the Node-RED file store. On a
new instance, that flow runs first.

**Use the ready asset:**
[`assets/protobuf-schema-bootstrap.flow.json`](../assets/protobuf-schema-bootstrap.flow.json).
Import it, set `protoPath` in its `Set flow config` node, deploy. It fires once on deploy,
writes the schema, and is idempotent (`overwriteFile: true`), so redeploying is safe. It
carries the standard four-node error path and passes the troubleshooting analyser with zero
findings. Verified on Node-RED v5.0.4: the file lands and the schema round-trips through
protobufjs.

> **The `file` node's filename is a trap when you copy the corpus.** The estate's flows carry
> `"filename": "/data/plcschema.proto"` with **no** `filenameType` — the pre-V3 form, which
> Node-RED upgrades in place to a literal string. If you set `filenameType: "msg"` you must
> also set `filename` to the **name of the message property** — `"filename": "filename"` —
> not to a path and not to `""`. With `filenameType: "msg"` and an empty `filename`, the node
> evaluates an unnamed property, **writes nothing, and logs no error**. The flow starts, the
> debug node shows the payload, and the file is simply absent. This cost a test cycle to find
> and it is invisible from the flow JSON alone.

**`keepCase: false` is why the JavaScript sees camelCase.** The `.proto` declares
`sys_time`, `value_integer`, `plc_packets`; with `keepCase` false the decoder converts to
`sysTime`, `valueInteger`, `plcPackets` — which is what every function in the corpus expects.
Setting it true silently breaks every downstream field reference.

## 3 · The structural envelope

Per-flow exports show this, but it is easy to omit when generating a flow from scratch.

| Field | On | Notes |
|---|---|---|
| `id` | everything | 16 hex characters, unique within the file |
| `type` | everything | — |
| `z` | every node on a tab | The **tab's id**. Config nodes have none |
| `g` | every node inside a group | The **group's id** |
| `x`, `y` | every node on a tab | Coordinates. Node-RED tolerates missing ones but the editor stacks them |
| `wires` | every node with outputs | Array of arrays — one inner array per output |

### The tab

```json
{ "id": "<id>", "type": "tab", "label": "⟨Asset⟩ - ⟨Artefact⟩",
  "disabled": false, "info": "⟨the flow description — see the documentation section⟩" }
```

`info` is the field that becomes the generated page's description, and the one **1 % of the
corpus fills in**.

### Groups are double-linked

A group both lists its members **and** each member points back:

```json
{ "id": "<gid>", "type": "group", "z": "<tab id>", "name": "config flow",
  "style": { "label": true }, "nodes": ["<id>", "<id>"], "x": 20, "y": 20, "w": 600, "h": 160 }
```

…and every member carries `"g": "<gid>"`. **Both directions are required.** Setting only one
gives a group that renders wrong or loses its members on the next deploy. A group may
contain another group — the canonical layout nests `set inputs for config flow` inside
`config flow`.

### Link nodes are double-linked too

`link out` carries `"links": ["<link in id>"]` and the matching `link in` carries
`"links": ["<link out id>"]`. One-sided links are the `orphan-link-out` finding in the
troubleshooting analyser.

---

## The minimal deployable skeleton

Ordered as Node-RED writes it: tab, groups, nodes, config nodes last.

```
[
  { tab },
  { group: "config flow" }, { group: "set inputs for config flow" },
  { group: "mqtt connection and message decoding" },
  { group: "set message filters" },
  { group: "prepare and convert payload" },
  { group: "message encoding and connection" },

  … the nodes, each with z, g, x, y, wires …

  { "type": "mqtt-broker",   … },      ← no z
  { "type": "protobuf-file", … }       ← no z
]
```

## Verifying before you hand it over

```bash
# 1 · static analysis — zero blockers is the bar
python3 <registry>/skills/od-node-red-flow-troubleshooting/scripts/analyze_flow.py flow.json

# 2 · does Node-RED actually accept it?
npm install node-red node-red-contrib-protobuf
node-red -u ./nrdata -s ./nrdata/settings.js
```

Read the log. Three outcomes, and only one is success:

| Log says | Means |
|---|---|
| `Started flows` | The flow is structurally sound and every node type resolved |
| `Waiting for missing types to be registered` | A palette module is missing — **the flow is not running** |
| `Connection failed to broker` after `Started flows` | The flow is fine; the broker is unreachable. Expected off-site |

The analyser cannot catch a missing palette module or a dangling config-node reference,
because a flow JSON with those problems is still valid JSON with valid node objects. **A
local Node-RED start is the only check that catches them**, and it takes a minute.

## What still needs the real instance

Even a flow that starts locally is not proven. These need the target:

- **Credentials** — entered per instance, never in the file.
- **The `.proto` on disk** at the configured path.
- **The output data point registered** on the IIoT edge platform, or nothing downstream
  consumes what you publish.
- **The palette** — confirm the target instance carries every contrib module your flow uses.
- **Deploy to `test` first.** Promoting to a prod instance is human-approved.
