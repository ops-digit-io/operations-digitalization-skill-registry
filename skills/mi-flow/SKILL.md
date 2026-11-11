---
name: mi-flow
description: >-
  Build, review, document, troubleshoot and port Node-RED flows to the OESL estate standard (MQTT, protobuf, topics, error handling). Not for choosing signal names (mi-signals).
license: MIT
allowed-tools: Read Grep Glob Write Edit Bash(python3 scripts/analyze_flow.py:*)
metadata:
  id: mi-flow
  aliases: [od-node-red-flow-builder]   # former name (naming convention, 2026-11-11)
  tier: technical
  lane: lane-3
  new_state_lane: "Lane 3b (3b4, 3b5)"
  new_state_step: "Connector design and data pipeline (edge to data platform); Procure and connect; Cyber Security sign-off in parallel; execution supplier-dependent"
  department_names: ["ops-pipeline", "data-pipeline-builder"]
  scope: od
  origin: derived
  owner_role: IIoT Interface & Automation Engineer (IIAE)
  tags: [information-integration-service, od, technical]
  authority_level: author flows and fixes on a test instance; read and diagnose only elsewhere; prod deploys are human-approved
  status: stable
  corpus: the exported ct-oesl Node-RED flows (count live, do not quote a remembered figure)
  requires: [dept-context]
  composes: [mi-equipment, mi-signals, deploy-acceptance, ops-analytics-asset, mi-data-availability]
  okf:
    type: Agent Skill
    title: mi-flow
    tags: [information-integration-service, od, technical]
---

# Node-RED flows (build, troubleshoot, connect)

Read `dept-context` first. The house pattern from the `ct-oesl-*-nodered-*` flows plus the way to repair one - not a Node-RED tutorial. Where the corpus is consistent, that is the standard.

| Step | Part | Go to |
|---|---|---|
| **3b4** connector and pipeline to the data platform (flow design to the standard base model); also 22 and 26 | **Build** | below, then `references/build-guide.md` |
| **3b5** procure and connect the machine (a connected machine's flow does not deliver); **3b6** when acceptance fails; faults from 23 or 26 ("dashboard is flat") | **Troubleshoot** | below, then `references/symptoms.md` |
| every step | **Shared rules** | below |

Chain handoffs, library classes, placement of logic and agent operating notes:
[`references/process-chain-practice.md`](references/process-chain-practice.md).

## Purpose

Builds, reviews and ports Node-RED flows to the OESL house pattern, builds calculated datapoints with the rule engine, and diagnoses a flow that is broken, silent or producing wrong values. Use it for steps 3b4 and 3b5 (3b6 when acceptance fails).
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Inputs and output

- **Build in:** signal analysis report, integration plan and tag list, the filled config contract. **Build out:** an importable flow, its tab description, the analyser result and test evidence.
- **Troubleshoot in:** the flow JSON export and the symptom. **Troubleshoot out:** the findings, the named cause and the filled triage record.

## Procedure

1. Read the Shared rules.
2. Build: follow "Build (step 3b4)" in order; for derived values use "Calculated datapoints - the rule engine".
3. Troubleshoot: follow "Troubleshoot (step 3b5)": Step A analyser, Step B order of findings, Step C what it cannot see.
4. Test on a `test` instance and hand to `deploy-acceptance`; a prod import goes to the human approver.
5. Close against "Done when".

## Where a flow sits

A Node-RED flow is the **transformation stage** between a connected machine and a use case.

```text
PLC ──(ingress variant)──► IIoT Edge Platform ──MQTT──► Node-RED ──► IIoT Edge Platform
                                                                          │ offload
                                                                          ▼
                                                    Databricks ──► Azure Storage Account
                                                                        (Parquet)
```

Flows publish back onto the MQTT spine; the platform offloads via **Databricks** to an **Azure Storage Account** (**Parquet**) that dashboards read, so the output UUID and `isDelta` semantics matter beyond the flow. The machine is connected per `mi-equipment` (guidance route); the signal
standard is set per `mi-signals`; the flow turns raw `PLCPacket` messages into the
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
  change with `mi-signals` (Consultation with Plant ME / Plant IT).
- **Never widen or remove `filter uuids` to make data appear**; if it drops everything the UUID is
  wrong or the machine is silent. Never delete a `catch` to quieten a debug pane. Never leave
  `debug` nodes enabled at volume in prod.
- **Structure to the data model, not the PLC layout** (the most-recorded blocker in the estate).

## Build (step 3b4)

1. **Gather inputs**: signal analysis report and derived outputs to register
   (`mi-signals`), integration plan and tag list (`mi-equipment`),
   tags not collecting closed (`mi-data-availability`), and the filled config contract
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
   and hand to `deploy-acceptance` (machine to connector to edge to flow to data platform to the
   asset the plant opens). A flow is not done until that passes. Prod import is a request to the
   human approver with the analyser result and test evidence. File the flow-library entry (new,
   standard or plant-specific).

Review of someone else's flow: eight questions and standards table in
[`references/build-guide.md`](references/build-guide.md#reviewing-someone-elses-flow). Wire and topic detail (`datatroniq/data/protob/plc/<edge-device>/<driver>/<id>`, ISA-95 `CT/<BA>/...`):
[`plc-packet.md`](references/plc-packet.md), [`topic-conventions.md`](references/topic-conventions.md); corpus census (read live): [`corpus-census.md`](references/corpus-census.md).

## Calculated datapoints - the rule engine (steps 1a2, 1b4, 3b4)

A new value derived from existing DATATRON datapoints is built as a **rule-engine flow** with `scripts/build_flow.py`, never by hand-writing the flow JSON. The five-step workflow (collect the requirement, pick the pattern, write the spec and generate, test before delivering, deliver) is in [`references/rule-engine.md`](references/rule-engine.md), section "Workflow for calculated datapoints".

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

It reads a static export, not the broker, edge platform, PLC or runtime state. Walk the path outward from the machine, not inward from the dashboard; the symptom tables and the full method are in [`references/symptoms-extended.md`](references/symptoms-extended.md), section "What the analyser cannot see".

### Silent corruptions and fast triage

The tables of silent corruptions (timestamps in the 23rd century, unpaired sysTime, oneof violation, Modbus 16-bit register) and the symptom-to-first-look table (publishes nothing, value constant, works on test but not prod, stopped after redeploy, counter jumps, dashboard flat, error with no node name) are in [`references/symptoms.md`](references/symptoms.md) § *Silent corruptions and fast triage*.

Fill [`assets/triage-record.md`](assets/triage-record.md) while diagnosing (cheapest checks first,
analyser result, what the analyser cannot see, decision). Route outcomes: a signal or topic
problem to `mi-signals` as a data-model change, a connection or machine problem to
`mi-equipment` / `mi-equipment`, an ownership gap to `dept-decision-rights`.

## Human gate and AI-agent notes

- **Agent may:** write and change flows on a test instance, run the analyser and the simulator, read exports, draft the triage record.
- **Roles decide:** the human approver (with the IIAE) approves any import to a `prod` instance; the plant key user confirms the values are correct; the owner of `mi-signals` decides on a signal or topic change. The agent only reads and diagnoses on other instances.

## Available Scripts

| Script | Purpose | Arguments |
|---|---|---|
| [`scripts/analyze_flow.py`](scripts/analyze_flow.py) | Static analysis of a flow export. Exit 2 blocker, 1 warning, 0 clean | `FLOW.json [FLOW.json ...] [--json] [--quiet]` |
| `scripts/build_flow.py` | Generate a rule-engine flow from a spec | `spec.json output_flow.json` |
| `scripts/simulate.js` | Dry-run a generated flow without Node-RED (Node.js) | `flow.json batches.json` |
| `scripts/e2e_test.sh` | Run a generated flow in a throw-away Node-RED with a local broker | `<flow.json> <batches.json> <output-uuid>` |
| [`scripts/e2e_runner.js`](scripts/e2e_runner.js) | Helper called by `e2e_test.sh` | `<batchFile> <inTopic> <outTopic> <outUuid>` |
| [`scripts/test_plcschema.proto`](scripts/test_plcschema.proto) | Stand-in PLCPacket schema for the end-to-end test; the production schema is authoritative | not run |

An agent runs a script with its code or shell tool (`run_script` in tools that expose it) and reads the exit code and output.

## Example

Fictional example; the flow name is made up for illustration.

```text
$ python3 scripts/analyze_flow.py ExampleFlow.json
=== Example Flow
  BLOCKER systime-not-repacked
  WARN    no-catch
    1 blocker . 1 warn . 0 info          -> exit 2
```

If the analyser reports a blocker, the flow fails the bar in "Done when": fix it on `test`, run the analyser again, then continue.

## Pitfalls

- Fixing a symptom in a function body (a UUID, a threshold, a topic) instead of in the config node or the data model.
- Reading the dashboard inward instead of walking outward from the machine.
- Treating a clean static analysis as proof: it cannot see the broker, the PLC or runtime state.
- Hand-writing rule-engine flow JSON instead of generating it.

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
| `references/plc-packet.md`, `topic-conventions.md`, `standard-functions.js`, `deployable-flow.md`, `instances.md`, `corpus-census.md` | Wire, topics, functions, deployable file, instances, live census |
| `assets/flow-config-contract.md`, `protobuf-schema-bootstrap.flow.json`, `triage-record.md` | Config form, importable schema flow, triage record |
| [`references/rule-engine.md`](references/rule-engine.md), [`rule-engine-patterns.md`](references/rule-engine-patterns.md), [`rule-engine-standard-flow.md`](references/rule-engine-standard-flow.md), the examples below | Calculated datapoints: the department's rule-engine workflow, patterns, standard flow, production examples |

### Rule-engine examples

| File | Kind |
|---|---|
| [`references/rule-engine-examples/12_ac402_machine_status_mapping.json`](references/rule-engine-examples/12_ac402_machine_status_mapping.json) | Rule-engine production example |
| [`references/rule-engine-examples/13_helium09_leakrate_BROKEN.json`](references/rule-engine-examples/13_helium09_leakrate_BROKEN.json) | Rule-engine production example |
| [`references/rule-engine-examples/13b_helium09_leakrate_FIXED.json`](references/rule-engine-examples/13b_helium09_leakrate_FIXED.json) | Rule-engine production example |
| [`references/rule-engine-examples/14_m1072_shift_part_counter.json`](references/rule-engine-examples/14_m1072_shift_part_counter.json) | Rule-engine production example |
| [`references/rule-engine-examples/15_m1072_part_counter_trigger.json`](references/rule-engine-examples/15_m1072_part_counter_trigger.json) | Rule-engine production example |
| [`references/rule-engine-examples/16_m1072_machine_mode_normalization.json`](references/rule-engine-examples/16_m1072_machine_mode_normalization.json) | Rule-engine production example |
| [`references/rule-engine-examples/17_m1072_alert_counter_trigger.json`](references/rule-engine-examples/17_m1072_alert_counter_trigger.json) | Rule-engine production example |
| [`references/rule-engine-examples/18_m1072_cycle_time_normalization.json`](references/rule-engine-examples/18_m1072_cycle_time_normalization.json) | Rule-engine production example |
| [`references/rule-engine-examples/19_blm_ast30_status_code_lookup.json`](references/rule-engine-examples/19_blm_ast30_status_code_lookup.json) | Rule-engine production example |
| [`references/rule-engine-examples/20_pink_total_parts_ok_plus_nok.json`](references/rule-engine-examples/20_pink_total_parts_ok_plus_nok.json) | Rule-engine production example |
| [`references/rule-engine-examples/21_line15_toolid_to_partnumber_lookup.json`](references/rule-engine-examples/21_line15_toolid_to_partnumber_lookup.json) | Rule-engine production example |
| [`references/rule-engine-examples/22_grazioli_downtime_duration.json`](references/rule-engine-examples/22_grazioli_downtime_duration.json) | Rule-engine production example |
| [`references/rule-engine-examples/23_erlas2_nok_part_trigger.json`](references/rule-engine-examples/23_erlas2_nok_part_trigger.json) | Rule-engine production example |
| [`references/rule-engine-examples/24_erlas2_ok_part_trigger.json`](references/rule-engine-examples/24_erlas2_ok_part_trigger.json) | Rule-engine production example |
