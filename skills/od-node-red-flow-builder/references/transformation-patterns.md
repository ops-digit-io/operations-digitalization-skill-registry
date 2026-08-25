# The transformation patterns

Ten patterns cover almost every flow in the estate. Each is given with its trigger, its
shape, the real implementation, and what breaks it. Copy these; do not reinvent them.

All of them sit inside the **`functional flow`** group of the canonical layout, between the
decode side and the encode side — see [`architecture.md`](architecture.md).

---

## P1 · Delta gate — "did this change?"

**The most common thing in the estate.** 193 counter flows and every event-shaped flow
start here.

```
link in → switch "is delta true >> 1"  (property: payload.isDelta, rule: is true)
        → …
```

A cyclic signal arrives at the connector's read interval. `isDelta` marks the packets that
represent a *change*. Gating on it turns a sample stream into an event stream, at zero
cost, before any logic runs.

**Where it goes wrong:** the source data point is not published as a delta, so the gate
never opens and the flow is silent. Confirm `isDelta` actually varies before building on
it — `rbe` on the value field is the fallback when it does not.

## P2 · Accumulator — counters with a reset

34 `Shift Part Counter` flows plus every total counter.

```javascript
var trigger      = msg.payload.isDelta
var ShiftCounter = flow.get("ShiftPartProduced") || 0      // ← tolerate undefined

if (trigger === true) { ShiftCounter++ }

flow.set("ShiftPartProduced", ShiftCounter)
return msg;
```

Then publish it:

```
change "format msg.payload":
  set payload.isDelta       = true                       (bool)
  set payload.valueInteger  = ShiftPartProduced          (flow)
  set payload.uuid          = datapointShiftPartProduced (flow)   ← OUTPUT identity
```

**The `|| 0` is not optional.** Flow context is cleared on deploy; without it the counter
becomes `NaN` on the first increment after every redeploy.

**Reset** is a separate trigger — an inject on a schedule, or a shift-boundary signal. 42
flows carry `static shift reset of counter`. A counter with no reset path is a counter that
only ever grows.

## P3 · Two-event time range — cycle time

104 cycle-time flows. Capture a start event, capture an end event, subtract.

```javascript
var cycle_start_time = msg.payload.sysTimeStart;
var cycle_end_time   = msg.payload.sysTimeEnd;

msg.payload.cycle_time = ((cycle_end_time - cycle_start_time) / 1000)

if (isNaN(msg.payload.cycle_time)) { return null; }   // no start captured yet
if (msg.payload.cycle_time < 0)    { return null; }   // clock or ordering problem

return msg;
```

**Both guards matter and both are silent.** `NaN` means the start event never arrived —
usual on the first cycle after deploy. Negative means the events arrived out of order, or
one timestamp was never unpacked. Returning `null` drops the message; prefer
`node.warn(...)` before the return so it is diagnosable.

Timestamps must already be **unpacked** here. Subtracting two packed `sysTime` values gives
a meaningless number that is not obviously wrong.

## P4 · Threshold crossing — estimation on a process value

32 flows (`Loading Time Estimation on Pressure`, `Cycle Time Estimation on Pressure`).
Where no explicit start/end trigger exists, derive one from a process value crossing a
limit.

```
rbe (payload.isHigh) → switch "is higher than 1.5 bar" → capture timestamp into flow context
                                                       → on the falling edge, run P3
```

45 flows carry the comment `is higher the 1.5 mbar`. The `isHigh` boolean is computed
upstream in a change/function pair; `rbe` on it turns a noisy analogue signal into two
clean edges.

**Where it goes wrong:** a signal that hovers at the threshold produces edge chatter. That
is what the `rbe` is for — but if the limit sits inside the signal's noise band, add
hysteresis rather than raising the rate limit.

## P5 · Value mapping — raw integer to named state

29 `Machine Mode Normalization` / `Machine Status` flows.

```
switch "isDelta is true"
  → switch "valueInteger is 1"   → change → set valueString "Running"
  → switch "valueInteger is 15"  → change → set valueString "Setup"
  → else                         → …
```

A chain of `eq` switches, one per state. `eq` is the second-most-common switch operator in
the estate (1,016 uses) and this is why.

**Where it goes wrong:** an unmapped code falls through the `else` and is dropped. 1,726
`else` branches exist and most go nowhere. **Wire the `else` to a debug or a warn** — an
unmapped machine mode is exactly the thing you want to know about.

For more than about six states, use P6 instead.

## P6 · Lookup table — CSV-backed mapping

83 flows (`parse csv input for alert messages`, `Tool ID Mapping`).

**Load once, at startup:**

```
inject (once) → file in → split → join (custom, array, count 1001, joiner \n)
              → csv (sep ';', no header, columns: error_number,error_message)
              → change: set flow.alertmessageConfig = payload
```

**Look up per message:**

```javascript
const lookup = flow.get("partnumberConfig")
const match  = msg.payload.valueInteger

const check = lookup.filter(e => e.tool_id == match)
if (check.length > 0) {
    msg.payload.valueString = check[0].internal_partnumber
    return msg
}
// no match → message is dropped
```

**Two failure modes, both silent.** The table is never loaded (inject not set to fire on
start) so `lookup` is `undefined` and the node throws — caught, message lost. Or there is no
match and the function falls off the end returning nothing.

**Add the miss branch.** `node.warn(\`no mapping for ${match}\`)` costs one line and turns an
invisible drop into a finding.

The `count: 1001` join is a fixed batch size, not a file length — a table longer than 1000
rows is silently truncated. 72 flows use exactly this number.

## P7 · UUID → label enrichment

195 flows carry `lookup uuid to label, including postprocessing`; 41 fetch the table live.

```javascript
const lookup = flow.get("datapointConfig")
const match  = msg.payload.uuid

const check = lookup.filter(e => e.uuid == match)
if (check.length > 0) {
    msg.payload.label = check[0].label
    return msg
}
```

The `datapointConfig` comes from the IIoT edge platform:

```
http request GET {url}/datatrons → set device endpoint
  → http request GET {url}/{datatronId}/data_points → change: set flow.datapointConfig
```

**Fetch it once at startup, never per message.** A synchronous HTTP call inside the
per-packet chain is the classic stall — see [`streaming.md`](streaming.md).

`label` is not a `PLCPacket` field. It exists only inside the flow, and must be removed
before the encode.

## P8 · Building a packet from nothing

65 `create object` flows. Where the output is not derived from an input packet — a target
value, a computed plan figure, a heartbeat.

```javascript
var payload = {
    uuid: flow.get('UUI_targetHr'),
    valueInteger: flow.get('TargerHour') * (flow.get('multiplicador') || 1),
    plcTime: 30,
    sysTime: 0
};

const dt_new = new Date()
const in_left = Math.round(dt_new.getTime() / 1000)
payload.sysTime = Number(BigInt(in_left) << 32n | BigInt(dt_new.getMilliseconds() * 1e6))

return { payload: payload, debugInfo: "Protobuf created" };
```

Note it packs `sysTime` itself, because there is no inbound packet to re-pack from.

## P9 · Clearing the oneof

34 `set null to multiple keys` functions, plus the change-node form in every standard
`prepare for protob encoding`.

```javascript
var keysToDrop = ["valueBool", "valueInt", "valueString"];
keysToDrop.forEach(function (key) {
  if (msg.payload.hasOwnProperty(key)) { msg.payload[key] = null; }
});
return msg;
```

**Prefer the change node's `delete`** over setting `null` — `measured_value` is a protobuf
`oneof`, and a present-but-null field is still a present field. The standard change node
does it correctly:

```
delete payload.valueDouble
delete parts
delete protobufType
delete _msgid
move   payload → payload.plcPackets[0]
```

18 flows in the estate send more than one value field. That is the `oneof-violation` the
troubleshooting analyser reports.

## P10 · Composite string parsing

8 `String Split` flows. A PLC packs several fields into one `valueString`; split it into
named values.

```
switch (payload.uuid eq the composite point) → function: split, validate, emit N packets
```

**Validate every field before emitting.** A composite string is the most brittle interface
in the estate — a PLC program change silently reorders the fields, and every derived value
is then wrong without a single error. Check the field count and the expected types, and
`node.warn` on a mismatch.

---

## Standards for any transformation

These hold whichever pattern you are in.

| Rule | Why |
|---|---|
| **Read config from `flow`, never a literal** | Porting to another machine is one change node. A UUID in a function body is a defect |
| **Unpack `sysTime` in, re-pack out — always both** | The pair is what keeps every downstream timestamp true. 19 flows ship one without the other |
| **Set the output UUID from config** | A derived packet under the input UUID is invisible to its consumer. 203 flows never set one |
| **Exactly one `value*` field survives to the encode** | `measured_value` is a `oneof` |
| **Set `isDelta` explicitly on the output** | State what the derived signal is; do not inherit it |
| **Guard, then warn, then drop** | `return null` alone makes a dropped message untraceable |
| **Wire the `else`** | An unmapped code is a finding, not noise |
| **Tolerate `undefined` context** | Deploy clears it — `flow.get(k) \|\| 0` |
| **Name every node** | `{{error.source.name}}` is the only identity an error message carries |
| **Structure to the data model, not the PLC layout** | The most-recorded blocker in the estate is data-model standardization |
