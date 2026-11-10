---
type: Skill Reference
title: Streaming
description: "The mechanics under every flow: how a PLC value reaches a derived signal, and what is synchronous, buffered or lost along the way."
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [node-red, streaming, mqtt]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# How the real-time streaming works

The mechanics underneath every flow: how a machine value gets from a PLC into a derived
signal, what guarantees hold at each hop, and where throughput is actually spent. Settings
quoted below are properties of the technology or the method; count your own usage live.

## The path, hop by hop

```text
PLC ──① ingress variant ──► IIoT Edge Platform ──② MQTT (protobuf) ──► Node-RED
                                                                          │
                                                              ③ transform │
                                                                          ▼
                                                    IIoT Edge Platform ──④ offload──►
                                                          Databricks → Azure Storage
                                                                        (Parquet)
```

| Hop | Carries | Timing |
|---|---|---|
| ① PLC → edge | Cyclic read or change event, per connector | Cyclic interval, set per connector (read it from the connector configuration) |
| ② edge → Node-RED | `PLCPacketList` over MQTT, protobuf-encoded | Event-driven, as published |
| ③ Node-RED | The transformation; usually publishes a new packet back onto ② | Sub-millisecond per message |
| ④ edge → data platform | Batched offload | Per offload, **not** real time |

**Only ① to ③ is real time.** The data platform is a batch destination — a dashboard that
needs a current value at the line reads the local layer, not the lake. This is why Grafana
is a local instance per plant.

## The message

Each MQTT message is one protobuf `PLCPacketList` containing a repeated `plc_packets`
array. See [`plc-packet.md`](plc-packet.md) for the schema.

**Set `mqtt in` datatype to `buffer`** for protobuf topics — the decode node needs the raw
bytes. Both `auto` and `buffer` appear in the estate; `auto` works because the payload is
binary either way, but `buffer` states the intent.

**QoS is 0 on most subscriptions.** That is at-most-once: a
message lost in transit is gone, and nothing retries. It is the right default for a cyclic
signal — the next sample is 500 ms away — and the **wrong** default for an event that is
only published once.

> **If your signal is an event rather than a sample, QoS 0 will silently lose some.**
> Subscriptions at QoS 1 or 2 are where the
> event-shaped flows live. Choose deliberately; the default is not a decision.

**Retain.** Not used on the publish side in the corpus. A retained message would give a new
subscriber the last known value immediately — useful for slow-changing state, and a
deliberate change, not a default.

## The four streaming primitives

Everything in the estate is built from these.

### 1 · split — one packet at a time

```text
decode → function "filter uuids" → split (arraySplt 1) → per-packet processing
```

Almost all split nodes use `arraySplt: 1`. It turns one `PLCPacketList` into N single
packets so the rest of the flow reasons about one value.

**Filter before you split.** `filter uuids` runs over `msg.payload.plcPackets` while it is
still an array — one pass instead of one per packet. Splitting first works and costs more.

Split sets `msg.parts`, which is why `prepare for protob encoding` deletes it before the
encode.

### 2 · rbe — change detection

This is how a cyclic stream becomes an event stream.

| Mode | Behaviour |
|---|---|
| `rbe` | Block unless the value changed |
| `rbei` | Same, but also ignore the **initial** value after deploy |

**Always point it at the value field, never the whole payload.** The estate does so:
`payload.isHigh`, `payload.valueString`, `payload.valueInteger`, `payload.valueDouble` (mostly `rbei`),
`payload.valueBool`. A few nodes compare `payload` whole — and a payload contains a changing
`sysTime`, so those never block anything.

`rbei` matters after a redeploy: without it every flow re-emits its current value on
restart, which downstream looks like a real event.

### 3 · delay — rate limiting

Used in *rate limit* mode with a short queue timeout to pace a burst so a downstream consumer or an
HTTP endpoint is not flooded. Read the configured rate and timeout on the node; do not assume them.

**Rate limiting drops or queues — know which.** A rate limiter in front of a counter turns
a burst of parts into one part.

### 4 · join — batching

The dominant configuration is `mode: custom, build: array, joiner: \n` with a fixed line count, and that
is the **CSV read** pattern: a file is split into lines, the lines are joined back into an array, and the
`csv` node parses it. It is not a
streaming construct; it is how a lookup table is loaded at startup.

## Ordering, and what it guarantees

Node-RED processes messages **one at a time per flow, in arrival order**, single-threaded
per message chain. Within one flow, order is preserved.

Three things break that assumption:

- **`split` fans out**, and each part traverses the flow to completion in order — but an
  async node (`http request`, `delay`, `file in`) inside the chain lets a later part
  overtake an earlier one.
- **`link out` → `link in`** hands off between groups without ordering guarantees across
  different sources.
- **Two flows on one tab** share flow context and interleave freely.

> **Never accumulate across parts without a `join`.** A counter incremented inside a split
> chain that contains an async node will count correctly but may attribute values to the
> wrong timestamp.

## State: flow context

`flow.get` / `flow.set` are used throughout the estate. Two rules that cause
most "it worked yesterday" reports:

1. **Scope is the tab.** Two flows on one tab share context. Moving a flow to another tab
   silently changes its state namespace.
2. **Deploy clears it** unless persistent context storage is configured. Every accumulator
   must tolerate `undefined` — the house pattern is `flow.get("ShiftPartProduced") || 0`.

`global` context and node-scoped `context` are rare, and
`global` couples flows that should not know about each other. Prefer `flow`.

## Back-pressure — there isn't any

MQTT at QoS 0 with no acknowledgement means **nothing upstream slows down when Node-RED is
busy**. If a flow cannot keep up, messages queue in memory and then are lost. Practical
consequences:

- Keep per-message work small. Heavy work belongs in the offload, not the flow.
- A synchronous `http request` inside the per-packet chain is the classic stall — the safe
  pattern is to fetch config **once at startup**
  into flow context (the `get variable config from iiot edge platform` group),
  not per message.
- `delay` in rate-limit mode protects the *downstream*, not this flow.

## Errors do not stop the stream

A `catch` node receives the error and the message is dropped from its original chain.
Nothing retries, nothing is dead-lettered. So an error is a **lost message**, not a paused
stream, which is why the standard four-node error path exists and why flows without
one lose messages invisibly.

## Throughput checklist

| Do | Why |
|---|---|
| Filter by UUID before the split | One filter pass instead of N |
| Subscribe with a wildcard and filter in the flow | Topic stays stable when a data block is renumbered |
| Use `rbe` on the value field | Turns a cyclic stream into events; cuts downstream volume |
| Fetch config once at startup | Avoids a synchronous HTTP call per message |
| Keep debug nodes off in prod | They are a development aid |
| Choose QoS deliberately | 0 for cyclic samples, 1–2 for events that happen once |
