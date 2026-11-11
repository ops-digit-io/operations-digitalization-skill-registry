---
type: Skill Reference
title: Rule engine
description: "The department's OPS rule engine on DATATRON / Node-RED: workflow for a new calculated datapoint (requirement, pattern, spec, generate, test, deliver) and for fixing an existing flow."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [node-red, rule-engine, datatron, department-package]
derived_from:
  - "Department knowledge base, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `ops-rule-engine.skill/SKILL.md` (the master).

# OPS Rule Engine (DATATRON / Node-RED)

A rule-engine flow subscribes to a machine's DATATRON MQTT topic, decodes the protobuf
`PLCPacketList`, keeps the latest value of each input datapoint (DP), runs a calculation, and
publishes the result as a **new virtual DP** (its own UUID, created beforehand in DATATRON) in the
same format. Every flow follows one house standard so colleagues can read any of them. This
skill produces that standard by generating the flow from a small spec, then testing it.

Files in this skill:
- `../scripts/build_flow.py` — spec → importable flows.json (always use it; don't hand-write flow JSON)
- `../scripts/simulate.js` — fast offline dry-run of the calculation with sample batches
- `../scripts/e2e_test.sh` — optional full run in a real Node-RED + local MQTT broker
- `rule-engine-standard-flow.md` — anatomy, PLCPacket fields, topics, timestamps, naming. Read when reviewing/fixing a flow or when something in the spec is unusual.
- `rule-engine-patterns.md` — use-case catalog with verified `calc` snippets. Read before writing any `calc`.
- `rule-engine-examples/*.json` — the production flows the standard comes from (counters, triggers, status mapping, mode normalization, cycle time, downtime, lookups, leak rate). Open the one matching the use case when the user's case is close to it or they reference that machine.

## Workflow: new calculated datapoint

### 1. Collect the requirement

You need, per input DP: a short PascalCase name, the UUID, and its value field
(`valueInteger` / `valueDouble` / `valueBool` / `valueString`). For the output: name, UUID,
value field. Plus: the logic, the **MQTT input topic (the user provides it)**, the output topic,
and the machine name / EQ number for the tab label.

Extract everything the user already gave. Ask only for what's missing, in one message. Typical gaps:
- **Value field of the inputs** — infer from meaning if obvious (counter → valueInteger, flags/bits → valueBool, cycle timer → valueDouble) and state the assumption instead of asking.
- **Output topic** — ask. If the user doesn't know, default to the input topic without the trailing `/#` and say so (see rule-engine-standard-flow.md §4 for plant conventions).
- **Ambiguous logic** — e.g. overlapping status bits: ask for the priority order; counters: ask whether it resets per shift and at which times.
- **Output UUID** — required; it must already exist as a DP in DATATRON. Never invent one.

### 2. Pick the pattern

Read `rule-engine-patterns.md`, match the intent, and take its settings + `calc` snippet as the
starting point. Quick map:

| user wants | pattern | evaluate |
|---|---|---|
| formula of current values (sum, ratio, %) | 1 Arithmetic | perBatch |
| several bits → one state text | 2 Status mapping | perBatch |
| code → text / part number | 3 Lookup table | perPacket |
| pulse per part / alarm | 4 Event trigger | perPacket |
| parts per shift | 5 Counter + cron reset | perPacket |
| downtime / time between signals | 6 Duration | perPacket |
| peak of a running timer | 7 Sawtooth peak | perPacket |
| mantissa+exponent, raw/100, units | 8 Scaled value | perBatch |

The core rule behind every pattern: **store each input's latest value in flow context and
calculate from the stored values.** DATATRON publishes on change, so waiting for all inputs in
one MQTT message (the classic bug, see `rule-engine-examples/13_helium09_leakrate_BROKEN.json`) means the
flow almost never fires.

### 3. Write the spec and generate

```json
{
  "tabLabel": "Rosenberger - M1072 (EQ40015929) - Total Parts",
  "machineName": "eq40015929",
  "description": "Total parts = OK + NOK (shown in the tab info)",
  "inputTopic": "datatroniq/data/protob/plc/datatron-eq40015929/cifx/#",
  "outputTopic": "datatroniq/data/protob/plc/eq40015929/cifx",
  "inputs": [
    {"name": "OkParts",  "uuid": "…", "field": "valueInteger"},
    {"name": "NokParts", "uuid": "…", "field": "valueInteger"}
  ],
  "output": {"name": "TotalParts", "uuid": "…", "field": "valueInteger"},
  "calc": "if (v.OkParts === undefined || v.NokParts === undefined) return null;\nreturn v.OkParts + v.NokParts;",
  "options": {
    "evaluate": "perBatch",
    "publishOnChangeOnly": true,
    "heartbeatMinutes": 0,
    "resetCrons": [],
    "lookupTable": null
  }
}
```

`calc` is a JS function body. Available: `v.<Name>` (typed latest value; int64 already converted
to Number), `t.<Name>` (its sysTime in ms), `trigger` / `triggerName` (the packet that caused this
run), `state` (persistent object, cleared by `resetCrons`), `lookup` (table rows). Return the value,
or `null` to publish nothing. Options are optional; defaults as shown. `brokerId` / `protoFileId`
can override the standard config-node ids.

```bash
python3 scripts/build_flow.py spec.json /mnt/user-data/outputs/<tab-name>.json
```

The script validates UUIDs, names, fields and rejects an output UUID that is also an input.

### 4. Test before delivering

Always dry-run with realistic batches, including the edge cases of the pattern (first value
only, two DPs changing in one batch, isDelta=false snapshot, unchanged value, unrelated UUID):

```bash
node scripts/simulate.js flow.json batches.json
# batches.json: [[{"uuid":"…","valueInteger":"345","isDelta":true}], [ … ]]
```

For new patterns or when the user asks for proof, run the real thing (installs Node-RED into /tmp
on first use, ~1 min):

```bash
bash scripts/e2e_test.sh flow.json batches.json <output-uuid>
```

### 5. Deliver

Present the flow file, then keep the message short: what the flow calculates (formula in one
line), the pattern/evaluate mode, the topics used, and the test result (e.g. "990/−9 → 9.9e‑9;
decade jump 105/−8 in one batch → 1.05e‑8, no false value"). Close with a deploy checklist of
only the items that apply:
- output UUID exists in DATATRON as a virtual DP with a matching data type;
- output topic confirmed (if it was derived);
- counters/state live in flow context and restart at 0 after a Node-RED restart unless a persistent context store is configured;
- cron resets use the container clock (usually UTC).

On import Node-RED reuses the existing broker (`a5b9953ab68b73bb`) and proto file
(`7a49aef9.46452`) config nodes because the ids match.

## Workflow: fix or review an existing flow

1. Map the flow first (node list with wiring, function code, change rules, topics) using a
   short Python dump of the JSON — don't eyeball raw JSON.
2. Check against the list below; these are the failures actually found in plant flows:
   - calculation requires all inputs in the same batch → no output
   - result written to fields not in PLCPacket (`leakage_rate`, `machine`, …) → encoder drops them
   - encode not wired to `mqtt out`, or `filter uuids` / sysTime nodes disconnected
   - calc wired in parallel with the store nodes → race
   - `filter uuids` given a string instead of an array; filter list not containing the inputs
   - two related DPs changing in one batch evaluated per packet → transient wrong value (use perBatch)
   - leftover `value*` fields from the input packet published with the output
   - `Math.round` in sysTime back (timestamp up to 1 s in the future)
   - output published to the input topic without the output UUID excluded from the filter → loop
3. Explain the causes briefly (numbered, one or two sentences each), then rebuild the flow with
   `build_flow.py` using the original UUIDs, topics and logic, test it, and deliver as above.
   Keep the colleague's calculation intent; only change what's broken.

When the user asks for a message to the colleague, write it plain and blame-free: what didn't
work and why, what changed, what to double-check.

## Workflow for calculated datapoints

A new value derived from existing DATATRON datapoints (parts per shift, machine mode, cycle time, status text,
downtime, OK + NOK totals, tool-to-part lookup) is built as a **rule-engine flow**, the department's
`ops-rule-engine` package (master; transcribed in `references/rule-engine.md` (`rule-engine.md`)):

1. **Collect the requirement** per input datapoint (PascalCase name, UUID, value field), the output datapoint (it must
   already exist in DATATRON; never invent a UUID), the logic, the MQTT input topic (the user gives it) and output topic.
2. **Pick the pattern** (`rule-engine-patterns.md`): arithmetic, status mapping,
   lookup, event trigger, counter with cron reset, duration, sawtooth peak, scaled value. Core rule: store each
   input's latest value in flow context and calculate from the stored values - DATATRON publishes on change.
3. **Write the spec and generate** with [`scripts/build_flow.py`](../scripts/build_flow.py); never hand-write the flow JSON.
   Anatomy, PLCPacket fields, topics, timestamps and naming: `rule-engine-standard-flow.md`.
4. **Test before delivering**: offline dry-run with [`scripts/simulate.js`](../scripts/simulate.js), optionally the full run
   in Node-RED with a local broker ([`scripts/e2e_test.sh`](../scripts/e2e_test.sh)).
5. **Deliver** the importable flow plus the spec; then the shared rules and the analyser below apply as to any flow.

Thirteen production flows are the reference cases ([`references/rule-engine-examples/`](rule-engine-examples/));
`13_helium09_leakrate_BROKEN.json` and `13b_..._FIXED.json` show the classic wait-for-all-inputs bug and its fix.
Signal naming and normalization rules for the output stay with `od-signal-standardization`.
