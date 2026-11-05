---
type: Skill Reference
title: Symptoms
description: "What the static analyser cannot see: work down from the symptom to the cause and the file to open."
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [node-red, troubleshooting]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Symptom → cause → where to look

What the static analyser cannot see. Work down from the symptom; each row names the
**layer** to check, because the commonest diagnostic mistake is starting at the dashboard
and working inward.

## The rule: walk outward from the machine

```text
machine → connector → ingress variant → IIoT Edge → MQTT → Node-RED → offload → asset
   1          2              3               4         5        6         7        8
```

Most "the dashboard is broken" reports resolve at **1–4**. Check the flow (6) only after
you have seen the input topic carrying messages.

**The cheapest test in the estate:** subscribe to the flow's input topic with a wildcard
and watch. If nothing arrives, the flow is not the problem and no amount of reading it
will help.

---

## Nothing is published

| Check | How | If it fails |
|---|---|---|
| Is the flow deployed and enabled? | Tab not greyed out; nodes not `d: true` | Deploy it; the analyser reports `disabled-nodes` |
| Is the pipeline wired? | `spine-severed` finding | Re-wire mqtt in → decode → filter → split → … → encode → mqtt out |
| Is the broker connected? | Node status under the mqtt nodes in the editor | Broker host, credentials, TLS, client ID |
| Is anything arriving on the input topic? | Subscribe to `…/<edge-device>/#` | Machine, connector or edge device — not the flow |
| Does the input UUID exist on that topic? | Temporarily debug the decoded `plcPackets` before `filter uuids` | Wrong UUID in `Set flow config`, or the data point was never configured on the edge platform |
| Does `filter uuids` match? | Compare the flow-config UUID to what arrives | Fix the config; **do not widen the filter** |
| Does a switch gate it? | `isDelta`-true gates are the usual one | The signal is not changing, or is not published as a delta |

**A client-ID collision disconnects silently.** If two Node-RED instances or a cloned
configuration use the same MQTT client ID, the broker drops one and neither can tell. A
flow that connects, works briefly, then goes quiet — on a plant where somebody cloned an
instance — is this.

## Published, but the value is wrong

| Symptom | Cause | Where |
|---|---|---|
| Always the same value | `rbe` on the wrong property, or comparing the whole payload (a changing timestamp defeats it) | The `rbe` node's *property* |
| Value never updates after the first message | `rbe` where `rbei` was meant, or vice versa | `rbe` = block unless changed; `rbei` = also ignore the initial value |
| Off by a factor of 10, 100, 1000 | Missing unit conversion — Modbus carries no type | The transformation function |
| Correct today, but can't be tuned per machine, or stays wrong after the limit changes elsewhere | A threshold or limit is a literal in the function body instead of read from flow config | `hardcoded-threshold` finding; move it into `Set flow config` |
| Boolean arrives as a number | The wrong `value*` field was read | Check which `oneof` member the source data point actually uses |
| String truncated or with junk leading characters | S7 vs S5 string interpretation — S7 strings carry a two-byte length prefix | Upstream, at the aggregation server or connector |
| Value correct on one plant, wrong on another | Tags structured to the PLC layout instead of the data model | `od-signal-standardization` — this is a standard problem, not a flow problem |

## Timestamps are wrong

The sysTime pair. See the main skill. In short: packed `uint64`, seconds `<< 32` plus
nanos. Unpack in, re-pack out, always both.

| Reads as | Means |
|---|---|
| Year ~2262 | Treated as epoch milliseconds |
| Far future | Treated as epoch seconds |
| Plausible but shifted | Re-packed from `new Date()` rather than from the source packet — the house pattern deliberately stamps *now*, so a derived signal is timestamped when derived. If the source time was wanted, that is a change, and it needs saying in the node's info |

## It worked yesterday / stopped after a redeploy

**Flow context is cleared on deploy** unless persistent context storage is configured.

| Symptom | Cause |
|---|---|
| Counter restarted at 1, or produced `NaN` | Accumulator not seeded — use `flow.get(key) \|\| 0` |
| Shift counter never resets | The reset trigger is a separate inject or timer; check it exists and fires in the right timezone |
| Two counters interfere | Both flows on the same tab writing the same context key — **flow context is per-tab** |
| Config lost | `Set flow config` runs from an `inject` with *once after start*; if that box is unticked, config is only set when somebody presses the button |

## Works on test, not on prod

| Check | Note |
|---|---|
| Different UUIDs in `Set flow config` | The same machine has different data-point UUIDs per edge device |
| Different broker or topic prefix | `<edge-device>` segment differs per instance |
| Flow disabled on prod | Common after a copy |
| Prod instance not in the DATATRONiQ cluster | The device reports nothing and looks healthy in the cabinet |
| Test instance carries more flows than prod | Normal here — `som` runs 97 on test against 54 on prod. Do not assume prod is the superset |

## The downstream asset is empty

| Layer | Check |
|---|---|
| Flow publishes | Debug node on the output before the encode |
| Encode shape | `payload.plcPackets[0]` wrapper present; exactly one `value*` field |
| Output UUID | Differs from the input UUID, and is the one the consumer subscribes to |
| Offload | The edge platform's offload to the data platform — outside the flow |
| Asset | The dashboard's own query and time range |

**A derived packet published under the input UUID is invisible to its consumer** and looks
like a duplicate of the source. 203 flows in the corpus never set an output UUID.

## Errors you can see, and the ones you cannot

The house error pattern is four nodes:

```text
catch (all) → change "get env variables of flow" → template "create error message" → debug
```

The template resolves `{{flow_name}}`, `{{error.source.name}}` and `{{error.message}}`, so
an error identifies itself without opening the editor — **provided the failing node has a
name.** An unnamed node yields an error message that names nothing.

380 flows have no `catch` at all. In those, a runtime exception is silent: the message is
dropped and nothing is reported.

**`node.error` and `node.status` are barely used** across the corpus — 6 and 8 occurrences
respectively. So a function that fails a validation check typically `return null`s and the
message vanishes without trace. When adding a guard, prefer:

```javascript
if (!Number.isFinite(v)) { node.warn(`dropping non-numeric value for ${uuid}`); return null; }
```

over a bare `return null`.

## When to stop reading the flow

If the input topic carries no messages for the configured UUID, the flow is correct and the
problem is upstream: machine, connector, ingress variant, or the data-point configuration
on the edge platform. Hand it to `od-equipment-integration` (guidance route) — and record the finding
against the machine, not the flow.
