---
name: od-node-red-flows
description: >-
  Build, review, document, troubleshoot and port Node-RED flows the way the OESL shop-floor
  estate does it - the seven-group canonical layout, the protobuf PLCPacket schema over MQTT,
  the datatroniq and CT topic conventions, the standard function nodes (sysTime unpack and
  re-pack, UUID filtering, flow-config debug), catch-based error handling and the naming the
  auto-documentation depends on; and diagnose a flow that is broken, silent or producing wrong
  values, starting from its exported JSON with a static analyser (sysTime, protobuf oneof,
  hardcoded secrets or thresholds, severed pipeline, UUIDs in function bodies, missing catch,
  unset flow context) plus a symptom-to-cause table. Use when writing or changing a flow for a
  machine or use case (step 3b4), reviewing a flow before a prod instance, porting a flow
  between plants, or when a flow publishes nothing, a wrong value or a nonsense timestamp, stops
  after a redeploy, or a dashboard has gone flat (step 3b5, also 3b6 when acceptance fails).
license: MIT
allowed-tools: Read Grep Glob Write Edit Bash(python3 scripts/analyze_flow.py:*)
metadata:
  id: od-node-red-flows
  tier: technical
  lane: information-integration-service
  scope: od
  origin: derived
  owner_role: IIoT Interface & Automation Engineer (IIAE)
  authority_level: author flows and fixes on a test instance; read and diagnose only elsewhere; prod deploys are human-approved
  status: stable
  sources_read: 2026-11-05
  corpus: the exported ct-oesl Node-RED flows (count live, do not quote a remembered figure)
  requires: [od-context]
  composes: [od-equipment-integration, od-signal-standardization, od-acceptance-test, od-analytics-asset-build, od-data-availability-check]
  derived_from:
    - ops-knowledge-graph/_knowledge/node-red-auto-docs/docs/** (exported flow JSON and generated docs)
    - ops-knowledge-graph/_knowledge/node-red-auto-docs/generate_docs.py
    - ops-knowledge-graph/_knowledge/10-Department/Machine integration.md
    - Node-RED auto-docs flow JSON re-read 2026-11-05 (ops-knowledge-graph/_knowledge/node-red-auto-docs/docs) for disabled flows, drivers, MQTT settings, timers and flow-config keys
    - Work vault (Work-OpsDigit-Knowledge), Graph/Connectors profile blocks for the TIA, S7, Beckhoff, Allen-Bradley and Omron connectors, read 2026-11-05
    - Analyser re-run unchanged over all exported flow files on 2026-11-05 and the same files re-checked for disabled tabs, drivers and context keys
    - Work vault (Work-OpsDigit-Knowledge), Graph/Connectors, DTQ-Beckhoff-Connector profile block, read 2026-11-05
  okf:
    type: Agent Skill
    title: od-node-red-flows
    tags: [information-integration-service, od, technical]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-06T00:00:00Z }
---

# Node-RED flows (build, troubleshoot, connect)

Read `od-context` first. The house pattern from the `ct-oesl-*-nodered-*` flows plus the way to repair one - not a Node-RED tutorial. Where the corpus is consistent, that is the standard.

| Step | Part | Go to |
|---|---|---|
| **3b4** connector and pipeline to the data platform (flow design to the standard base model); also 22 and 26 | **Build** | below, then `references/build-guide.md` |
| **3b5** procure and connect the machine (a connected machine's flow does not deliver); **3b6** when acceptance fails; faults from 23 or 26 ("dashboard is flat") | **Troubleshoot** | below, then `references/symptoms.md` |
| every step | **Shared rules** | below |

Chain handoffs, library classes, placement of logic and agent operating notes:
[`references/process-chain-practice.md`](references/process-chain-practice.md).

## Where a flow sits

A Node-RED flow is the **transformation stage** between a connected machine and a use case.

```text
PLC ──(ingress variant)──► IIoT Edge Platform ──MQTT──► Node-RED ──► IIoT Edge Platform
                                                                          │ offload
                                                                          ▼
                                                    Databricks ──► Azure Storage Account
                                                                        (Parquet)
```

Flows publish back onto the MQTT spine; the platform offloads via **Databricks** to an **Azure Storage Account** (**Parquet**) that dashboards read, so the output UUID and `isDelta` semantics matter beyond the flow. The machine is connected per `od-equipment-integration` (guidance route); the signal
standard is set per `od-signal-standardization`; the flow turns raw `PLCPacket` messages into the
derived signal a use case consumes (cycle time, part count, quality event, alert).

Instances are named **`ct-oesl-<plant-code>-nodered-<prod|test>[N]`**
([`references/instances.md`](references/instances.md)).

> **Build and fix on a `test` instance. Deploying to a `prod` instance is human-approved.**

## Shared rules (build and troubleshoot)

- **Config from `flow`, never a literal.** Everything bound to a machine (datatron name, UUIDs,
  limits) lives in the `Set flow config` change node and is read with `flow.get(...)`. Porting is
  editing one node. A UUID or threshold inside a `function` body is a defect.
- **`sysTime` is a packed uint64** (seconds `<<32` | nanos), never an epoch. Unpack inbound with
  `Convert sysTime`, re-pack outbound with `Convert sysTime back` - **both, always**. Reading it as
  milliseconds gives the year 2262. Copy the standard functions, do not rewrite them
  ([`standard-functions.js`](references/standard-functions.js)).
- **`measured_value` is a protobuf `oneof`**: exactly one `value*` field reaches the encode;
  `prepare for protob encoding` deletes the rest. Also delete `msg.parts`, `msg.protobufType`,
  `msg._msgid` and `payload.label` (not a PLCPacket field) before the encode.
- **`uuid` is the data point and the join key**; the human label lives in the edge platform's
  data-point config. Never hardcode a label as identity; never invent a UUID (fetch the config; the
  output data point must already be registered there or consumers ignore the packet).
- **Set the output UUID from config and `isDelta` explicitly** on a derived packet; do not inherit.
- **Flow context is per tab and cleared on deploy.** Tolerate `undefined`
  (`flow.get("ShiftPartProduced") || 0`). Two flows on one tab share keys. Prefer `flow` over `global`.
- **Guard, then warn, then drop.** A bare `return null` makes a dropped message untraceable; add
  `node.warn(...)`. Wire the `else`. Keep a `catch` (scope all) with the four-node error pattern.
- **Never hardcode a secret** (token, password, webhook URL); use `$env(...)` / `env.get()` or
  Node-RED credentials. The flow repositories are cloned by the doc generator and git history keeps
  what you delete: **rotate** any secret found, do not only remove it.
- **Never change the signal standard or a topic from inside a flow.** A topic is an interface; a
  per-plant fix-up in a function hides the problem from every other plant. Raise a data-model
  change with `od-signal-standardization` (Consultation with Plant ME / Plant IT).
- **Never widen or remove `filter uuids` to make data appear**; if it drops everything the UUID is
  wrong or the machine is silent. Never delete a `catch` to quieten a debug pane. Never leave
  `debug` nodes enabled at volume in prod.
- **Structure to the data model, not the PLC layout** (the most-recorded blocker in the estate).

## Build (step 3b4)

1. **Gather inputs**: signal analysis report and derived outputs to register
   (`od-signal-standardization`), integration plan and tag list (`od-equipment-integration`),
   tags not collecting closed (`od-data-availability-check`), and the filled config contract
   [`assets/flow-config-contract.md`](assets/flow-config-contract.md) from the plant key user.
2. **Look for an artefact first**: [`references/artefacts.md`](references/artefacts.md) lists what
   the flows already build, with a sanitized example per artefact and the naming convention. Place
   the logic (PLC, flow or service bus) and choose streaming or scheduled per
   [`references/process-chain-practice.md`](references/process-chain-practice.md).
3. **Pick the transformation.** Thirteen patterns cover almost every flow
   ([`transformation-patterns.md`](references/transformation-patterns.md)): P1 delta gate, P2
   accumulator, P3 two-event time range, P4 threshold crossing, P5 value mapping, P6 lookup table,
   P7 UUID to label, P8 build from nothing, P9 clear the oneof, P10 composite string, P11 OEE chain,
   P12 windowed extremum, P13 liveness watchdog. Single input is the minority: multi-input shapes
   (filter array, latch into flow context, evaluate on the trigger, cold-start guard) and the
   four-question method for "no pattern fits" (inputs, history, what drives output, output) are in
   [`composing-transformations.md`](references/composing-transformations.md). Do not force the
   nearest pattern. Real-time path guarantees (split/rbe/delay/join, QoS, ordering, back-pressure):
   [`streaming.md`](references/streaming.md).
4. **Use the canonical seven-group layout** (config flow, mqtt connection and message decoding,
   set message filters, a use-case group, prepare and convert payload, message encoding and
   connection, ungrouped error handling). If your flow does not look like that, have a reason.
   Walkthrough: [`architecture.md`](references/architecture.md); layout diagram in the build guide.
5. **Make it deployable**: read [`deployable-flow.md`](references/deployable-flow.md) before
   generating a file. The corpus exports hold no config nodes; `decode`/`encode` need the
   `node-red-contrib-protobuf` module and MQTT and protobuf config nodes must be added. On a new
   instance import [`assets/protobuf-schema-bootstrap.flow.json`](assets/protobuf-schema-bootstrap.flow.json)
   once, before any decode/encode flow.
6. **Document as you build** (the generator reads only tab label and info, node name and info,
   group name): write the **tab description** (what it produces, for which machine, for which use
   case; almost no flow has one); **name every node**; use the standard group names; put the
   config contract in the `config flow` comment node.
7. **Prove it**: run the analyser (below) on the export, reach zero blockers, deploy to `test`,
   and hand to `od-acceptance-test` (machine to connector to edge to flow to data platform to the
   asset the plant opens). A flow is not done until that passes. Prod import is a request to the
   human approver with the analyser result and test evidence. File the flow-library entry (new,
   standard or plant-specific).

Review of someone else's flow: eight questions and standards table in
[`references/build-guide.md`](references/build-guide.md#reviewing-someone-elses-flow). Wire and topic detail (`datatroniq/data/protob/plc/<edge-device>/<driver>/<id>`, ISA-95 `CT/<BA>/...`):
[`plc-packet.md`](references/plc-packet.md), [`topic-conventions.md`](references/topic-conventions.md); corpus census (read live): [`corpus-census.md`](references/corpus-census.md).

## Troubleshoot (step 3b5)

**Start from the flow JSON** (`node-red-auto-docs/docs/<instance>/<Flow_Name>.json` or an editor
export); no access to the running instance is needed for most findings. First ask what changed and
when it last worked, and check the tab is enabled
([`symptoms-extended.md`](references/symptoms-extended.md)).

### Step A - run the analyser

```bash
python3 scripts/analyze_flow.py path/to/Flow.json
python3 scripts/analyze_flow.py docs/ct-oesl-som-nodered-prod/*.json --quiet   # whole instance
python3 scripts/analyze_flow.py Flow.json --json                              # machine-readable
```

Standard library only. Exit **2** on any blocker, **1** on any warning, **0** otherwise (fits CI or a pre-deploy check). `BLOCKER` corrupts or loses data, `WARN` degrades it or makes the flow unmaintainable, `INFO` is hygiene. Count findings on the day.

| Check | Severity | Meaning |
|---|---|---|
| `hardcoded-secret` | BLOCKER | Literal token or password in the flow |
| `systime-not-unpacked` | BLOCKER | Inbound `sysTime` used without unpacking |
| `systime-not-repacked` | BLOCKER | Unpacked but not re-packed before the encode |
| `oneof-violation` | BLOCKER | More than one `measured_value` field reaches the encode |
| `systime-unpaired` | BLOCKER | Only one half of the unpack / re-pack pair present |
| `no-flow-description` | WARN | Tab has no description |
| `no-catch` | WARN | No error handling; exceptions are silent |
| `output-uuid-not-set` | WARN | Output UUID equals input UUID |
| `no-flow-config` | WARN | UUIDs not held in a `Set flow config` node |
| `hardcoded-threshold` | WARN | A limit is a literal in a function body (P4/P12 is the fix) |
| `spine-severed` | WARN | A pipeline node has no inbound wire |
| `unset-context-read` | WARN | A context key is read but never written on the tab |
| `mostly-unnamed-nodes` | WARN | Most nodes have no name |

### Step B - read findings in this order

1. `hardcoded-secret` - stop and rotate (shared rules).
2. `systime-*` - timestamps are wrong and nothing errors.
3. `oneof-violation`.
4. `spine-severed` - a decode, split, encode or mqtt out node with no inbound wire: the flow moves
   no data, usually why "it publishes nothing".
5. `hardcoded-threshold` - not data loss, but the flow cannot be tuned or ported without editing a function.
6. Everything else, in printed order.

### Step C - what the analyser cannot see

It reads a static export: not the broker, edge platform, PLC or runtime state. Work
[`references/symptoms.md`](references/symptoms.md) (symptom, cause, layer to check) and
[`symptoms-extended.md`](references/symptoms-extended.md) (disabled-tab check, where findings
concentrate, more rows, worked findings). **Walk the path outward from the machine** (machine,
connector, ingress variant, edge, flow, offload, asset), not inward from the dashboard: most
"dashboard is broken" reports are a machine that stopped publishing. After a platform or server
migration the flow is rarely the cause (DNS, certificates, access, connector licence).

### Silent corruptions and fast triage

The tables of silent corruptions (timestamps in the 23rd century, unpaired sysTime, oneof violation, Modbus 16-bit register) and the symptom-to-first-look table (publishes nothing, value constant, works on test but not prod, stopped after redeploy, counter jumps, dashboard flat, error with no node name) are in [`references/symptoms.md`](references/symptoms.md) § *Silent corruptions and fast triage*.

Fill [`assets/triage-record.md`](assets/triage-record.md) while diagnosing (cheapest checks first,
analyser result, what the analyser cannot see, decision). Route outcomes: a signal or topic
problem to `od-signal-standardization` as a data-model change, a connection or machine problem to
`od-equipment-integration` / `od-barrier-triage`, an ownership gap to `od-decision-routing`.

## Done when

A flow passes when the analyser reports **zero blockers**, the tab carries a description, `Set flow
config` holds every UUID, the sysTime pair is present, a `catch` reports with the flow name, and the
output UUID differs from the input. The same bar serves a new flow (build) and a repaired one
(troubleshoot: cause named as flow, configuration, machine, connector, platform change or ownership;
fix tested on `test`; triage record filled; plant key user confirmed correct values).

## Files

| Path | Use |
|---|---|
| `references/build-guide.md` | Layout, message, standard functions, config, topics, standards, error handling, documentation, review checklist |
| `references/artefacts.md`, `transformation-patterns.md`, `composing-transformations.md`, `streaming.md`, `architecture.md` | Build depth |
| `references/plc-packet.md`, `topic-conventions.md`, `standard-functions.js`, `deployable-flow.md`, `instances.md`, `corpus-census.md` | Wire, topics, functions, deployable file, instances, live census |
| `references/symptoms.md`, `symptoms-extended.md` | Troubleshoot depth |
| `references/process-chain-practice.md` | Chain role, handoffs, agent notes (sections: Build, Troubleshoot) |
| `assets/flow-config-contract.md`, `protobuf-schema-bootstrap.flow.json`, `triage-record.md` | Config form, importable schema flow, triage record |
| `scripts/analyze_flow.py` | Static analyser |
