# The artefact catalogue

What the 825 flows across 53 instances actually build. Crawled from the flow labels and
node contents, not from a wish list — if it is in this table, somebody has built it and
you can copy it.

**Before building anything, look here first.** Almost every new request is an instance of a
family that already exists at another plant.

## Naming convention

**74 % of flows (608 of 825)** follow:

```
[(status)] <asset> [(EQ id)] - <artefact>
```

- `(OK)` — 60 flows · `(TODO)` — 20 flows. A status prefix in the *name* is the estate's
  informal review marker.
- `(EQ40018861)`-style equipment ids appear on 38 flows — the strongest form, because it
  joins straight to the Machine List.
- The **artefact half after the last ` - `** is what the flow produces, and it is the
  column that makes the table below possible.

> **Name a new flow this way.** The tab label is the page title in the generated docs and
> the only index anyone browses. `Flow 1` — which exists — is unfindable.

## Artefact families, by flow count

| Artefact family | Flows | What it produces |
|---|--:|---|
| Part / piece counter | 193 | A part-produced trigger, a total, a shift total |
| Autoclave / vessel process | 120 | Temperature, pressure and heating-mode signals per vessel |
| Cycle time | 104 | A derived duration between two trigger events |
| Config / setup | 93 | Protobuf schema injection, base models, test harnesses |
| Alerting / notification | 51 | An error-number → message lookup, published or pushed |
| Pressure | 51 | Filtered pressure, thresholds, quality events |
| Tool / mould | 50 | Tool-id to part-number mapping |
| Shift | 42 | Shift-scoped counters and resets |
| Temperature | 31 | Tolerances, limits, quality events |
| Machine state / mode | 29 | A normalized machine status from raw mode integers |
| Braider | 27 | Status duration, standard speed, operation time |
| Extrusion | 21 | Setup monitors, product-failure mapping |
| Scrap / NOK | 21 | Failure mapping and transformation |
| Downtime / stoppage | 20 | Downtime events and durations |
| Quality event | 14 | Threshold-breach events per process value |
| Speed | 11 | Standard speed, operation time |
| OEE | 11 | Availability × performance × quality |
| Dashboard / UI | 10 | Local HMI and alert screens |
| Traceability / recipe | 2 | Recipe data, serial injection |

## The specific artefacts, by name

The exact artefact string after the ` - `, top of the distribution:

| Artefact | Flows | Pattern used |
|---|--:|---|
| Part Counter Trigger | 56 | Delta gate → publish trigger |
| Cycle Time | 55 | Two-event time range |
| Shift Part Counter | 34 | Delta gate → accumulator → reset |
| Alerting | 32 | CSV lookup table → code-to-message |
| Tool ID Mapping | 28 | CSV lookup table → id-to-part-number |
| Tolerance Values for Temperature | 19 | Static limits into context |
| Loading Time Estimation on Pressure | 18 | Threshold-crossing time range |
| Downtime | 16 | State duration |
| Cycle Time Estimation on Pressure | 14 | Threshold-crossing time range |
| Machine Mode Normalization | 14 | Integer → normalized state mapping |
| OK / NOK Part Counter Trigger | 21 | Delta gate, split by quality outcome |
| Load Counter Threshold | 11 | Accumulator with a threshold event |
| Cycle Counter Trigger | 8 | Delta gate on a cycle signal |
| Cycle Time Calculation / Normalization | 15 | Two-event time range |
| String Split | 8 | Parse a composite `valueString` |
| Standard Speed / Operation Time | 5 + | Static reference values into context |
| Machine Status | 5 | State mapping, published |
| Shot Weight Estimation | 5 | Derived value from process signals |
| Error Handling | 6 | Dedicated error-routing flow |

Six flows exist whose whole artefact is **Error Handling** — a dedicated tab that collects
and routes errors rather than the per-flow catch. Worth knowing before building a seventh.

## Generalized example per artefact

One sanitized shape per family — **no real UUIDs, machine names, endpoints or credentials**.
Every identifier is a config key you set in `Set flow config`; every value is a placeholder.
Copy the shape, then fill the config from the machine's own data points.

**Convention used below.** `cfg.<name>` means a flow variable set in the config group and
read with `flow.get('<name>')`. `⟨…⟩` is a value you must supply. Nothing here is
copy-pasteable as a literal, deliberately.

### Part / piece counter — trigger and total

```
config:  cfg.datapointPartTrigger   ⟨input  uuid⟩
         cfg.datapointPartTotal     ⟨output uuid⟩

filter uuids [cfg.datapointPartTrigger] → split → convert sysTime
  → switch  payload.isDelta is true                       ← P1 delta gate
  → function: total = (flow.get('partTotal') || 0) + 1; flow.set('partTotal', total)
  → change  set payload.isDelta      = true
            set payload.valueInteger = flow.partTotal
            set payload.uuid         = cfg.datapointPartTotal
  → prepare for protob encoding → convert sysTime back → encode → mqtt out
```

Shift variant: identical, plus a reset. `inject` on the shift boundary →
`flow.set('partTotal', 0)`. **State the timezone** the boundary is evaluated in.

### Cycle time — between two trigger events

```
config:  cfg.datapointCycleStart ⟨uuid⟩  cfg.datapointCycleEnd ⟨uuid⟩
         cfg.datapointCycleTime  ⟨output uuid⟩

filter uuids [start, end] → split → convert sysTime (prefer plcTime if present)
  → switch payload.uuid
      ├─ start → change: set flow.sysTimeStart = payload.sysTime      (latch)
      └─ end   → function: compute and emit
```

```javascript
const start = flow.get('sysTimeStart');
if (start === undefined) { node.warn('cycle end without a start — cold start?'); return null; }

const seconds = (msg.payload.sysTime - start) / 1000;
if (!Number.isFinite(seconds)) { node.warn('cycle_time not finite'); return null; }
if (seconds < 0)               { node.warn('negative cycle_time — events out of order'); return null; }

flow.set('sysTimeStart', undefined);        // arm for the next cycle
msg.payload.valueDouble = seconds;
return msg;
```

### Threshold crossing — estimation on a process value

```
config:  cfg.datapointProcessValue ⟨uuid⟩   cfg.threshold ⟨number⟩
         cfg.datapointDuration     ⟨output uuid⟩

filter → split → convert
  → function: msg.payload.isHigh = msg.payload.valueDouble > flow.get('threshold')
  → rbe  (property: payload.isHigh)                       ← edges only
  → switch payload.isHigh
      ├─ true  → latch the rising-edge timestamp
      └─ false → compute duration from the latch (as cycle time above)
```

Add hysteresis if the signal noise band straddles the threshold — two limits, enter above
the upper, leave below the lower. Raising the rate limit does not fix edge chatter.

### Machine state / mode normalization

```
config:  cfg.datapointModeRaw ⟨uuid⟩   cfg.datapointModeName ⟨output uuid⟩

filter → split → convert → switch payload.isDelta is true
  → switch payload.valueInteger
      ├─ eq ⟨code⟩ → change: set payload.valueString = "⟨StateName⟩"
      ├─ eq ⟨code⟩ → change: set payload.valueString = "⟨StateName⟩"
      └─ else      → debug / node.warn   ← WIRE THIS
  → change: set payload.uuid = cfg.datapointModeName, delete payload.valueInteger
```

**Publish the name, not the code.** A downstream consumer that has to know that 15 means
Setup is a consumer coupled to one PLC program.

### Alerting — code to message, CSV-backed

```
startup:  inject (once) → file in ⟨path⟩ → split → join (array, ⟨n⟩, \n)
          → csv (sep ';', columns: error_code,error_message)
          → change: set flow.alertTable = payload

runtime:  filter [cfg.datapointAlertCode] → split → convert
          → function: look the code up in flow.alertTable
          → change: set payload.uuid = cfg.datapointAlertText
```

```javascript
const table = flow.get('alertTable');
if (!Array.isArray(table)) { node.warn('alert table not loaded'); return null; }

const hit = table.find(e => String(e.error_code) === String(msg.payload.valueInteger));
if (!hit) { node.warn(`no alert text for code ${msg.payload.valueInteger}`); return null; }

msg.payload.valueString = hit.error_message;
return msg;
```

**Never put a webhook URL or token in the flow.** If an alert is pushed to a chat channel,
the endpoint comes from `$env(...)` or Node-RED credentials. 42 flows in the estate get this
wrong and the values are in git history.

### Tool / mould id → part number

Identical to alerting, different table: `csv` columns `tool_id,internal_partnumber`, output
written to `payload.valueString`. Same two guards — table loaded, and a miss branch.

### Tolerance / quality event — multi-input

```
config:  cfg.datapointCurrentValue  cfg.datapointUpperLimit
         cfg.datapointLowerLimit    cfg.datapointMachineMode
         cfg.datapointVerdict ⟨output⟩

function "Define filter array" → filter uuids (array) → split → convert
  → switch payload.uuid
      ├─ limits, mode → change: set flow.value<Name> = payload.value*   (latch only)
      └─ current value → function "evaluate"                            (triggers)
```

The evaluation, the cold-start guard and the trigger-selection trap are in
[`composing-transformations.md`](composing-transformations.md) — this is the shape **461 of
665** configured flows actually use, and the one most worth getting right.

### Rate / output per period — windowed

```
config:  cfg.datapointCumulative ⟨uuid⟩   cfg.datapointRate ⟨output uuid⟩
         cfg.windowSeconds ⟨number⟩

filter → split → convert → function "record over the window" → function "difference"
  → change: set payload.uuid = cfg.datapointRate, set payload.valueDouble = ⟨rate⟩
```

Buffer shape and the **counter wrap-around** trap: see `composing-transformations.md` §Q2.
`last - first` is wrong whenever the PLC counter resets inside the window.

### Composite KPI — availability × performance × quality

```
config:  one uuid per component input, plus cfg.datapointKpi ⟨output⟩
         plus static references: cfg.standardSpeed, cfg.plannedTime ⟨numbers⟩

multi-input latch (as tolerance above)
  → function: compute each component, then the product
  → guard every divisor, clamp each component to [0,1], emit valueDouble
```

```javascript
const a = plannedTime > 0 ? runTime / plannedTime : null;
const p = idealRate  > 0 ? actualRate / idealRate : null;
const q = totalCount > 0 ? goodCount / totalCount : null;
if ([a, p, q].some(x => x === null)) { node.warn('KPI skipped — divisor zero or input missing'); return null; }

const clamp = x => Math.min(Math.max(x, 0), 1);
msg.payload.valueDouble = clamp(a) * clamp(p) * clamp(q);
return msg;
```

**A KPI that silently returns 0 because a divisor was 0 is worse than one that does not
publish.** Guard first, warn, then drop.

### Composite string split

```
config:  cfg.datapointComposite ⟨uuid⟩ + one output uuid per extracted field

filter → split → convert → function: split, validate field count and types, emit N packets
```

```javascript
const parts = String(msg.payload.valueString).split('⟨separator⟩');
if (parts.length !== ⟨expected⟩) {
    node.warn(`composite string has ${parts.length} fields, expected ⟨expected⟩ — PLC program changed?`);
    return null;
}
```

**Validate the field count every time.** A PLC program change silently reorders the fields
and every derived value is then wrong with no error anywhere.

### Timer-driven emit

```
inject (repeat ⟨interval⟩ / crontab ⟨schedule⟩)
  → function "create object": build a packet from config and pack sysTime yourself
  → encode → mqtt out
```

Use when the output must exist even if nothing changed — a target value, a plan figure, a
heartbeat. There is no inbound packet to re-pack from, so pack the timestamp explicitly
(P8 in [`transformation-patterns.md`](transformation-patterns.md)).

---

## The building blocks these are made of

The reusable pieces, with how many flows carry each. Copy them; do not rewrite them.

### Standard function nodes

| Node name | Flows | Purpose |
|---|--:|---|
| `Debug flow config` | 675 | Echo the config so a misconfiguration shows at deploy |
| `Convert sysTime (UTC timestamp)` | 625 | Unpack the packed `sys_time` |
| `Convert sysTime back (UTC timestamp)` | 617 | Re-pack before the encode |
| `filter uuids` | 599 | Keep only the configured data points |
| `set datapointConfigFilter` | 205 | Build the data-point config query filter |
| `create json payload` | 157 | Assemble the outbound packet |
| `calculate timerange between cycle_start and cycle_end event` | 148 | The cycle-time primitive |
| `create object` | 65 | Build a packet from flow config rather than an input |
| `lookup and filter messages raw mqtt messages` | 41 | Attach a label from the data-point config |
| `set device endpoint` / `set data_points endpoint` | 41 each | Edge-platform API calls |
| `set null to multiple keys` | 34 | Clear unused `oneof` members |
| `lookup toolId to partnumber` | 29 | CSV-backed id mapping |

Verbatim source: [`standard-functions.js`](standard-functions.js).

### Standard groups

| Group | Flows |
|---|--:|
| `config flow` | 656 |
| `prepare and convert payload` | 620 |
| `mqtt connection and message decoding` | 606 |
| `message encoding and connection` | 580 |
| `functional flow` | 552 |
| `set inputs for config flow` | 458 |
| `set message filters` | 309 |
| `lookup uuid to label, including postprocessing` | 195 |
| `filter messages` | 180 |
| `calculate cycle time based on triggers` | 152 |
| `parse csv input for alert messages` | 83 |
| `get variable config from iiot edge platform` | 24 |

The first seven are the canonical layout. The rest are the named transformation groups —
adding one of those to a flow is a signal to the reader that a known pattern is in use.

### Standard comment headings

Comments carry the prose in the generated documentation. The recurring headings —
`config flow` (661), `connect to MQTT and decode messages` (600), `functional flow` (594),
`prepare and convert payload` (585), `encode and publish to MQTT` (553), `set filters`
(509), `set necessary input` (458) — mirror the groups. The valuable ones are the
configuration contracts written in the `config flow` comment: which flow variables must be
set, what each means, where to get it. **32 % of comment nodes carry a body; those are what
the good ones look like.**

### Node types in use

106 distinct types across the corpus. The ones that matter:

| Type | Nodes | Role |
|---|--:|---|
| `comment` | 5,749 | Documentation |
| `group` | 5,313 | Structure |
| `change` | 4,711 | Mapping and config |
| `function` | 4,670 | Transformation |
| `switch` | 2,068 | Filtering and routing |
| `debug` | 1,976 | Development aid |
| `link in` / `link out` | 1,668 / 1,631 | Inter-group routing |
| `inject` | 1,154 | Config trigger, timers |
| `mqtt in` / `mqtt out` | 742 / 661 | The spine |
| `split` | 648 | One packet at a time |
| `decode` / `encode` | 600 / 588 | Protobuf |
| `template` | 541 | Error and CSV text |
| `catch` | 448 | Error handling |
| `rbe` | 192 | Change detection |
| `http request` | 142 | Edge-platform config, webhooks |
| `delay` | 95 | Rate limiting |
| `csv` | 83 | Lookup tables |
| `join` | 82 | Batching |
| `OPCUA-IIoT-*` | 209 | Direct OPC UA read/browse/write |
| `influxdb out` | 39 | Local timeseries write |
| `ui-*` / `ui_*` | ~250 | Local dashboards |

Five subflows are in use, the largest at 22 flows (`subflow:e38c467b545b6fe2`, 66 nodes).
⟨Subflow contents are not in the per-flow exports — read them on the instance.⟩

## Coverage, honestly

| | |
|---|---|
| Groups named | 92 % |
| Nodes named | 63 % |
| Comment nodes with a body | 32 % |
| **Flows carrying a description** | **1 %** (12 of 825) |

The catalogue above was reconstructable only because the *naming* convention held. It
would have been reconstructable far better if the 1 % were 100 %.
