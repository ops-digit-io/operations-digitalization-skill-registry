---
type: Skill Reference
title: Transformation patterns
description: Thirteen patterns covering almost every flow in the estate, each with its trigger, its state, its output and how it fails.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [node-red, transformation, patterns]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# The transformation patterns

Thirteen patterns cover almost every flow in the estate. Each is given with its trigger, its
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

45 flows carry the comment `is higher the 1.5 mbar`. The `isHigh` boolean itself is computed
upstream, in a function that runs on every sample:

```javascript
// "catch if higher then 1.5 bar"
var currentValue     = msg.payload.valueDouble;
var currentTimestamp = msg.payload.sysTime;

if (currentValue > 1.5) {
    if (flow.get("isHigh") === true) {
        flow.set("actual_timestamp", currentTimestamp);   // still high — keep the latest time
    }
    flow.set("isHigh", true);
    msg.payload.isHigh = true;
} else {
    flow.set("isHigh", false);
    msg.payload.isHigh = false;
}

return msg;
```

`rbe` downstream on `payload.isHigh` is what turns this into the two clean edges the switch
needs — the function alone only produces a flag on every sample, not an edge.

**The `1.5` is the estate's own counter-example to "read config from flow, never a
literal."** 68 flows in the corpus hardcode a limit in the function body instead of reading
it from flow config — not just this one (1.5 bar, 2000 rpm in the sibling max-speed version),
but process-time constants and other limits too. Porting any of them to a different limit
means editing a function, not a change node. Copy the shape; read the limit with
`flow.get('thresholdX')` instead. `od-node-red-flow-troubleshooting`'s `hardcoded-threshold`
check reports exactly this.

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

**When the state depends on more than one flag, the switch chain becomes a nested `if`.**
A braider's machine status is not one raw integer but three flow-context flags, classified
together, most-specific case first:

```javascript
var released = flow.get("valueMachineIsReleased");
var state    = flow.get("valueMachineState");
var mode     = flow.get("valueMachineMode");
var setup    = flow.get("valueMachineSetup");

if (released === false)                         { msg.payload.valueString = "Planned Downtime";  return msg; }
if (released === true && state === 2)            { msg.payload.valueString = "Breakdown";         return msg; }
if (released === true && state === 0 && setup)   { msg.payload.valueString = "Setup-ChangeYarn";  return msg; }
if (released === true && state === 1 && mode)    { msg.payload.valueString = "Normal Operating";  return msg; }
if (released === true && state === 1 && !mode)   { msg.payload.valueString = "Manual Operating";  return msg; }
// no final else — every real copy of this ends here, so an unrecognised combination is
// dropped silently instead of being wired to a debug node
```

This is the four-question classification from
[`composing-transformations.md`](composing-transformations.md) in its most common shape —
several inputs latched in flow context, evaluated together — written as `if`/`else` because
a `switch` node tests one property at a time. **Order the conditions most-specific first**:
`state === 2` (Breakdown) has to be checked before a looser combination would otherwise
claim it. Give this one the `else` the real copies skip, for the same reason as above.

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

## P11 · OEE chain — availability × performance × quality

7 `oee_Calculator_*` flows. Three independent branches, each publishing its own signal,
feed one final multiply.

```javascript
// "availability"
var td = Number(flow.get('TD_minutos'))   // planned time, minutes
var tm = Number(flow.get('TM_minutos'))   // downtime, minutes

msg.payload = (td - tm) / td
return msg;
```

```javascript
// "performance"
var target = Number(flow.get('TargetDay'))
msg.payload = Number(msg.payload.valueInteger) / target
return msg;
```

```javascript
// "oee calculate"
msg.payload = msg.payload * flow.get("performance") * Number(flow.get('quality'))
return msg;
```

Availability and performance are each computed and published as their own signal before the
final multiply — a dashboard reads them individually as well as the combined OEE. **Quality
is read from flow context, not computed here**; in the estate it arrives from a separate
reject/scrap count upstream, so this chain does not itself define what counts as a defect.

**None of the real copies guard the division.** A planned time or a target of `0` — the
normal value before a shift's first part — publishes `Infinity` or `NaN` straight to the
dashboard. Guard it the way P3 guards `NaN`: check before dividing, not after.

## P12 · Windowed extremum capture — the peak value while a threshold holds

A machine property (speed, position, pressure) crosses a threshold, opening a window;
latch the running maximum while the window stays open; publish it once the window closes.
Related to P4, but a single value and a single timestamp survive the whole window, not just
the two edges.

```javascript
const uuid       = flow.get('datapointMaxSpeed')
const isNewCycle = flow.get('isNewCycle');
const lastSpeed  = flow.get('lastSpeed');
const maxSpeed   = flow.get('maxSpeed');
const threshold  = flow.get('thresholdMaxSpeed')   // the real copy hardcodes 2000 — don't

flow.set('lastSpeed', msg.payload.valueInteger);

if (msg.payload.valueInteger > threshold && lastSpeed < threshold) {
    flow.set('isNewCycle', true);                       // rising edge opens the window
}
if (isNewCycle && maxSpeed < msg.payload.valueInteger) {
    flow.set('maxSpeed', msg.payload.valueInteger)
    flow.set('maxSpeedTime', msg.payload.sysTime)        // latch the value AND when it happened
}
if (isNewCycle && msg.payload.valueInteger < threshold && lastSpeed > threshold) {
    flow.set('isNewCycle', false);                       // falling edge closes the window
    msg.payload = {
        uuid: uuid, sysTime: Number(flow.get('maxSpeedTime')),
        valueInteger: maxSpeed, isDelta: true
    }
    flow.set('maxSpeed', 0); flow.set('maxSpeedTime', 0);
    return msg;
}
return null;   // window still closed, or still open — nothing to publish yet
```

**Why a function and not `rbe` + `switch`.** The edge test needs both the current sample and
the previous one (`lastSpeed`) in the same comparison — that is one function, not a node
graph, which is why this pattern is self-contained rather than composed from P4's pieces.
Same hardcoded-threshold caution as P4 — `hardcoded-threshold` in the troubleshooting
analyser catches the real copy's literal `2000` too.

## P13 · Liveness watchdog — did the heartbeat stop?

A PLC heartbeat toggles on every real control cycle. Detect the toggle; if none arrives
within a timeout, publish "not alive" without waiting for a downstream consumer to notice
the dashboard went flat.

```javascript
let timer         = context.get('timer') || null;
let lastMsg       = context.get('lastMsg') || null;
let lastSentValue = context.get('lastSentValue');

function sendBoolean(val) {
    if (val !== lastSentValue) {
        node.send({ payload: {
            uuid: flow.get("datapointHeartbeatNormalized"),
            sysTime: msg.payload.sysTime, isDelta: true, valueBool: val
        }});
        context.set('lastSentValue', val);
    }
}

if (!timer) {
    timer = setInterval(function () { sendBoolean(false); timer = null; context.set('timer', timer); }, 300000);
    context.set('timer', timer);
}
if (lastMsg && msg.payload.valueBool !== lastMsg.payload.valueBool
            && msg.payload.isDelta === true && lastMsg.payload.isDelta === true) {
    sendBoolean(true);
    clearInterval(timer);
    timer = setInterval(function () { sendBoolean(false); timer = null; context.set('timer', timer); }, 300000);
    context.set('timer', timer);
}
context.set('lastMsg', msg);
```

**Node-scoped `context`, not `flow`.** Every other pattern here uses `flow` because the
state is meant to be shared across the tab. This one deliberately uses `context` because the
timer belongs to this one node — a second heartbeat flow sharing a tab must not be able to
clear a timer it does not own.

**The timeout (300 s here) is a judgement call tied to the signal's real publish interval,
not a constant to copy verbatim.**

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
| **State the unit, and convert it in one place** | A register or counter carries no unit of its own. One real flow divides a Modbus `valueInteger` by 1000 to turn milliseconds into seconds — correct, but nothing except the signal's name says the conversion is needed, so the next flow can skip it unnoticed |
