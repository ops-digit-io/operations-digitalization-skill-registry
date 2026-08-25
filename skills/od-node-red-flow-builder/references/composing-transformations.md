# When no pattern fits — composing a transformation

The catalogue tells you what exists. This tells you what to do when the thing you need is
not in it, which is the normal case for any genuinely new use case.

**A transformation is not chosen from a list. It is classified, then composed** from a small
set of primitives. Four questions place any transformation; the answers determine its shape.

---

## The four questions

| # | Question | Answers | Decides |
|---|---|---|---|
| 1 | **How many inputs?** | one · several · one plus a static table | Whether you need a filter array and latching |
| 2 | **Does it need history?** | no · last value · a window · since a boundary | Whether you need flow context, and what resets it |
| 3 | **What drives the output?** | an input event · a clock · a threshold · a completed window | Where the emit sits |
| 4 | **What is the output?** | a value · an event · a state · nothing (side effect) | The packet shape and whether `isDelta` is true |

Write the four answers down before opening the editor. Most flows that go wrong went wrong
at question 2 or 3 — usually by assuming one input and an event-driven emit because that is
what the nearest example did.

---

## Q1 · Inputs — and the majority case the catalogue under-sells

**461 of the 665 flows that carry data-point config read two or more data points.** Single
input is the minority (204 flows). Anything evaluating a rule — a tolerance, a quality
event, a machine-state-aware calculation — is multi-input by nature.

### Single input

```
mqtt in → decode → filter uuids (one UUID from config) → split → convert → …
```

### Multi-input — the latch-and-evaluate shape

You cannot evaluate two data points in one message, because **each arrives in its own
packet**. The house solution is to latch each into flow context as it arrives, and evaluate
on whichever arrives last.

```
config: one flow variable per input data point, plus the output one
   ↓
function "Define filter array"   ← builds the UUID array from config
   ↓
filter uuids (array)  →  split  →  convert sysTime
   ↓
switch on payload.uuid  ──► one branch per input
   │                          each branch: change → set flow.value<Name> = payload.value*
   ↓
(the branch carrying the *triggering* value) → function "evaluate"
   ↓
read every latched value from context, apply the rule, emit
```

```javascript
// "Define filter array" — build the subscription set from config, never a literal
const uuids = [
    flow.get('datapointMachineMode'),
    flow.get('datapointCurrentValue'),
    flow.get('datapointHardUpperLimit'),
    flow.get('datapointHardLowerLimit'),
].filter(Boolean);          // drop unconfigured optionals
flow.set('uuids', uuids);
return msg;
```

```javascript
// the evaluation — every input read from context, not from the message
const mode  = flow.get('valueMachineMode');
const value = msg.payload.valueInteger;        // the trigger carries its own value
const hi    = flow.get('valueHardUpperLimit');
const lo    = flow.get('valueHardLowerLimit');

if (mode === undefined || hi === undefined || lo === undefined) {
    node.warn('evaluation skipped — not all inputs latched yet');
    return null;                                // cold start, not an error
}
if (mode !== 'standby' && value > hi) { msg.payload.valueString = 'out of upper limit'; return msg; }
if (mode !== 'standby' && value < lo) { msg.payload.valueString = 'out of lower limit'; return msg; }
msg.payload.valueString = 'in tolerance';
return msg;
```

**Three things this shape gets wrong if you are not careful:**

1. **Cold start.** Until every input has arrived once, the latched values are `undefined`.
   Guard and `node.warn` — do not evaluate against `undefined`, which compares false and
   silently reports "in tolerance".
2. **Which input triggers.** Evaluating on *every* input re-emits the same verdict up to N
   times. Usually only the measured value should trigger; limits and mode only latch.
3. **Staleness.** A latched limit from three days ago is still used. If a limit can change,
   consider latching its timestamp too and refusing to evaluate on a stale one.

### One input plus a static table

The lookup shape — P6/P7 in [`transformation-patterns.md`](transformation-patterns.md).
The table is loaded once at startup into flow context, not per message.

---

## Q2 · History — and what clears it

| Need | Mechanism | Resets when |
|---|---|---|
| None | Stateless function | — |
| Last value | `flow.set` on each arrival | Deploy |
| Change detection | `rbe` node | Deploy (`rbei` suppresses the first emit after) |
| A window of values | Array in `context` / `flow` | Deploy, or when the window closes |
| Since a boundary | Accumulator + an explicit reset trigger | The reset fires |

**Flow context is per-tab and cleared on deploy.** Every accumulator needs
`flow.get(k) || 0`. 12 flows carry an explicit `reset flow` group; a counter with no reset
path only ever grows.

**`context` (node-scoped) vs `flow` (tab-scoped).** 72 flows use node-scoped `context` —
correct when the state belongs to one node and nothing else should see it, such as a
window buffer. Use `flow` for configuration and for anything a second node reads. `global`
(496 uses) couples flows that should not know about each other; avoid it.

### Windowed aggregation

36 flows buffer values over a window. The shape:

```javascript
let buf   = context.get('valueArray') || [];
let start = context.get('windowStart') || null;
const now = Date.now();

if (start === null) { start = now; context.set('windowStart', start); }

buf.push(msg.payload.valueDouble);
context.set('valueArray', buf);

if ((now - start) < 60_000) { return null; }      // window still open — emit nothing

// window closed: compute, emit, reset
const out = { first: buf[0], last: buf[buf.length - 1],
              min: Math.min(...buf), max: Math.max(...buf), n: buf.length };
context.set('valueArray', []);
context.set('windowStart', null);

msg.payload.window = out;
return msg;
```

**Windowing has three traps.** A window that never closes because no message arrives (add a
timer to close it). An unbounded buffer if the close condition is wrong (cap the length). And
**counter wrap-around** — where the value is a cumulative counter, `last - first` is wrong
whenever the PLC counter resets inside the window, which is why the corpus's per-minute
output function inspects `min`/`max` against `first`/`last` rather than subtracting blindly.

---

## Q3 · What drives the output

| Driver | Mechanism | Use when |
|---|---|---|
| An input event | The message itself | The default — a derived value per input value |
| A threshold | `switch` + `rbe` on the boolean edge | The event is "crossed a limit" |
| A clock | `inject` with `repeat` or `crontab` | The output must exist even when nothing changes |
| A closed window | The window function returns only when closed | Rates, per-period aggregates |
| A boundary | Shift change, day change | Resets and period totals |

**798 flows carry a scheduled or repeating inject** — mostly the once-at-start config
trigger, but timer-driven emit is normal here. A KPI that must appear on a dashboard every
minute regardless of machine activity is clock-driven, not event-driven.

**Timezone.** A shift or day boundary is a local-time concept and `new Date()` on the edge
device is not necessarily local. Any boundary logic needs the timezone stated explicitly —
⟨the estate's convention is not recorded; confirm with the IIAE⟩.

---

## Q4 · The output

| Output | `isDelta` | Value field | Note |
|---|---|---|---|
| A measured or derived value | `false` for a sample, `true` for a change | the matching `value*` | One field only |
| An event / trigger | `true` | often `valueBool: true` | The fact of it is the signal |
| A state | `true` on change | `valueString` | Publish the name, not the code |
| A rate or aggregate | `true` | `valueDouble` | Timestamp it at window close |

**The output data point must exist before you publish to it.** A derived UUID is not
something you invent — it is registered on the IIoT edge platform's data-point config, and
until it is, everything downstream ignores your packet. Get the output UUID first; it is a
prerequisite, not a finishing step.

---

## Composition rules

Patterns chain, and the order is not arbitrary.

```
filter → split → convert → [latch] → gate → transform → [window] → format → wrap → convert back → encode
```

| Rule | Why |
|---|---|
| **Filter before split** | One pass over the array instead of one per packet |
| **Convert sysTime immediately after split** | Everything downstream assumes epoch millis |
| **Latch before gating** | A value that arrives while gated is still needed later |
| **Gate before transforming** | Do not compute on samples you will discard |
| **Window last, before formatting** | The window emits at most one message per period |
| **Format, wrap, convert back, encode — in that order** | The wrap moves `payload` under `plcPackets[0]`; converting after the wrap means addressing `payload.plcPackets[0].sysTime` |

**Chaining across flows** is legitimate and common: one flow derives a signal and publishes
it, another consumes that derived UUID. Prefer this over a single flow with fifteen config
keys — 22 flows carry 8 or more data-point keys and they are the hardest in the estate to
read. **The seam between two flows is a published data point**, which is diagnosable; the
seam inside one flow is a wire nobody can inspect.

---

## Two timestamp conventions, not one

The references describe the packed `sysTime`. That is the `datatroniq/*` protobuf envelope
and it covers most of the estate — but not all of it.

| Envelope | Field | Format | Flows |
|---|---|---|--:|
| protobuf `PLCPacketList` | `sysTime` | packed `uint64`, seconds `<<32` \| nanos | most |
| protobuf `PLCPacketList` | `plcTime` | same packing — **the PLC's own clock** | 145 |
| JSON topics (e.g. `extrusion-cutting/…`) | `sys_time` | formatted string `MM/DD/YYYYThh:mm:ss AM/PM` | 75 |

**`sysTime` and `plcTime` are different clocks.** `sysTime` is when the edge saw it;
`plcTime` is when the PLC produced it. For anything measuring machine behaviour — cycle
time, downtime duration — `plcTime` is the more truthful source and does not drift with edge
scheduling. Flows that convert both convert them the same way and keep them separate.

**The JSON envelope carries a formatted local-time string with an AM/PM meridian**, which
must be parsed with a regex and reassembled. If you meet one of these, do not assume the
packed convention — check the topic family first.

---

## Before you build: the pre-flight

1. **The four questions**, written down.
2. **Does an artefact already exist for this?** → [`artefacts.md`](artefacts.md). At another
   plant, almost certainly.
3. **Do all input data points exist and publish?** Subscribe and watch before building —
   `od-data-availability-check`.
4. **Does the output data point exist** on the edge platform's config?
5. **Which envelope and which clock** — `sysTime`, `plcTime`, or the JSON string?
6. **What is the reset**, if there is state?
7. **What happens on cold start**, before context is populated?

## After you build

Run the analyser before deploying — `od-node-red-flow-troubleshooting`:

```bash
python3 scripts/analyze_flow.py MyNewFlow.json
```

Zero blockers is the bar. Then the acceptance test walks the whole path, machine to asset —
`od-acceptance-test`.
