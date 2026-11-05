---
type: Skill Reference
title: Artefacts
description: Guidance, no figures - the artefact families Node-RED flows actually build, the naming convention, a generalized key-free example per artefact, and the reusable building blocks; count usage live.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [node-red, artefacts]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# The artefact catalogue

What the flows across the instances actually build. Crawled from the flow labels and
node contents, not from a wish list - if it is in this catalogue, somebody has built it and
you can copy it. This page holds **no counts**; count families and artefacts live from the
exported flow labels (see `corpus-census.md`) and quote the figure with its date.

**Before building anything, look here first.** Almost every new request is an instance of a
family that already exists at another plant.

## Naming convention

Most flows follow:

```text
[(status)] <asset> [(EQ id)] - <artefact>
```

- `(OK)` / `(TODO)`: a status prefix in the *name* is the estate's informal review marker.
- An `(EQ<id>)`-style equipment id is the strongest form, because it joins straight to the Machine List.
- The **artefact half after the last ` - `** is what the flow produces, and it is the
  column that makes the catalogue possible.

> **Name a new flow this way.** The tab label is the page title in the generated docs and
> the only index anyone browses. A default title such as `Flow 1` is unfindable.

To measure how well the convention holds today: split every tab label on the last ` - `, and count the
labels that have both halves.

## Artefact families

| Artefact family | What it produces |
|---|---|
| Part / piece counter | A part-produced trigger, a total, a shift total |
| Autoclave / vessel process | Temperature, pressure and heating-mode signals per vessel |
| Cycle time | A derived duration between two trigger events |
| Config / setup | Protobuf schema injection, base models, test harnesses |
| Alerting / notification | An error-number to message lookup, published or pushed |
| Pressure | Filtered pressure, thresholds, quality events |
| Tool / mould | Tool-id to part-number mapping |
| Shift | Shift-scoped counters and resets |
| Temperature | Tolerances, limits, quality events |
| Machine state / mode | A normalized machine status from raw mode integers |
| Braider | Status duration, standard speed, operation time |
| Extrusion | Setup monitors, product-failure mapping |
| Scrap / NOK | Failure mapping and transformation |
| Downtime / stoppage | Downtime events and durations |
| Quality event | Threshold-breach events per process value |
| Speed | Standard speed, operation time |
| OEE | Availability x performance x quality |
| Dashboard / UI | Local HMI and alert screens |
| Traceability / recipe | Recipe data, serial injection |

The families are listed by kind, not ranked. Part counters, cycle times and the config/setup tabs are the
common ones; traceability is rare. Re-rank on the live label tally if volume matters.

## The specific artefacts, by name

The exact artefact string after the ` - ` maps to a pattern:

| Artefact | Pattern used |
|---|---|
| Part Counter Trigger | Delta gate -> publish trigger |
| Cycle Time | Two-event time range |
| Shift Part Counter | Delta gate -> accumulator -> reset |
| Alerting | CSV lookup table -> code-to-message |
| Tool ID Mapping | CSV lookup table -> id-to-part-number |
| Tolerance Values for Temperature | Static limits into context |
| Loading Time Estimation on Pressure | Threshold-crossing time range |
| Downtime | State duration |
| Cycle Time Estimation on Pressure | Threshold-crossing time range |
| Machine Mode Normalization | Integer -> normalized state mapping |
| OK / NOK Part Counter Trigger | Delta gate, split by quality outcome |
| Load Counter Threshold | Accumulator with a threshold event |
| Cycle Counter Trigger | Delta gate on a cycle signal |
| Cycle Time Calculation / Normalization | Two-event time range |
| String Split | Parse a composite `valueString` |
| Standard Speed / Operation Time | Static reference values into context |
| Machine Status | State mapping, published |
| Shot Weight Estimation | Derived value from process signals |
| Error Handling | Dedicated error-routing flow |

Some flows have **Error Handling** as their whole artefact - a dedicated tab that collects
and routes errors rather than the per-flow catch. Check whether the instance already has one before
building another.

## Generalized example per artefact

One sanitized shape per family — **no real UUIDs, machine names, endpoints or credentials**.
Every identifier is a config key you set in `Set flow config`; every value is a placeholder.
Copy the shape, then fill the config from the machine's own data points.

**Convention used below.** `cfg.<name>` means a flow variable set in the config group and
read with `flow.get('<name>')`. `⟨…⟩` is a value you must supply. Nothing here is
copy-pasteable as a literal, deliberately.

### Part / piece counter — trigger and total

```text
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

```text
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

```text
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

```text
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

```text
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
the endpoint comes from `$env(...)` or Node-RED credentials. Flows in the estate have got this
wrong, and the values are in git history.

### Tool / mould id → part number

Identical to alerting, different table: `csv` columns `tool_id,internal_partnumber`, output
written to `payload.valueString`. Same two guards — table loaded, and a miss branch.

### Tolerance / quality event — multi-input

```text
config:  cfg.datapointCurrentValue  cfg.datapointUpperLimit
         cfg.datapointLowerLimit    cfg.datapointMachineMode
         cfg.datapointVerdict ⟨output⟩

function "Define filter array" → filter uuids (array) → split → convert
  → switch payload.uuid
      ├─ limits, mode → change: set flow.value<Name> = payload.value*   (latch only)
      └─ current value → function "evaluate"                            (triggers)
```

The evaluation, the cold-start guard and the trigger-selection trap are in
[`composing-transformations.md`](composing-transformations.md) — this is the shape most configured flows use, and the one most worth getting right.

### Rate / output per period — windowed

```text
config:  cfg.datapointCumulative ⟨uuid⟩   cfg.datapointRate ⟨output uuid⟩
         cfg.windowSeconds ⟨number⟩

filter → split → convert → function "record over the window" → function "difference"
  → change: set payload.uuid = cfg.datapointRate, set payload.valueDouble = ⟨rate⟩
```

Buffer shape and the **counter wrap-around** trap: see `composing-transformations.md` §Q2.
`last - first` is wrong whenever the PLC counter resets inside the window.

### Composite KPI — availability × performance × quality

```text
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

```text
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

```text
inject (repeat ⟨interval⟩ / crontab ⟨schedule⟩)
  → function "create object": build a packet from config and pack sysTime yourself
  → encode → mqtt out
```

Use when the output must exist even if nothing changed — a target value, a plan figure, a
heartbeat. There is no inbound packet to re-pack from, so pack the timestamp explicitly
(P8 in [`transformation-patterns.md`](transformation-patterns.md)).

---

## The building blocks these are made of

The reusable pieces. Copy them; do not rewrite them. To see how widely each is used, count the node
names or group names across the flow exports.

### Standard function nodes

| Node name | Purpose |
|---|---|
| `Debug flow config` | Echo the config so a misconfiguration shows at deploy |
| `Convert sysTime (UTC timestamp)` | Unpack the packed `sys_time` |
| `Convert sysTime back (UTC timestamp)` | Re-pack before the encode |
| `filter uuids` | Keep only the configured data points |
| `set datapointConfigFilter` | Build the data-point config query filter |
| `create json payload` | Assemble the outbound packet |
| `calculate timerange between cycle_start and cycle_end event` | The cycle-time primitive |
| `create object` | Build a packet from flow config rather than an input |
| `lookup and filter messages raw mqtt messages` | Attach a label from the data-point config |
| `set device endpoint` / `set data_points endpoint` | Edge-platform API calls |
| `set null to multiple keys` | Clear unused `oneof` members |
| `lookup toolId to partnumber` | CSV-backed id mapping |

Verbatim source: [`standard-functions.js`](standard-functions.js).

### Standard groups

| Group | Role |
|---|---|
| `config flow` | Where the flow is bound to a machine |
| `prepare and convert payload` | Format the outbound packet and re-pack `sysTime` |
| `mqtt connection and message decoding` | Subscribe, decode, filter, split, unpack |
| `message encoding and connection` | Encode and publish |
| `functional flow` | The logic as a whole |
| `set inputs for config flow` | Inputs that feed the config |
| `set message filters` | Switches on the stream |
| `lookup uuid to label, including postprocessing` | P7 enrichment |
| `filter messages` | Additional filtering |
| `calculate cycle time based on triggers` | The cycle-time pattern |
| `parse csv input for alert messages` | CSV-backed lookup |
| `get variable config from iiot edge platform` | Fetch data-point config |

The first seven are the canonical layout. The rest are the named transformation groups -
adding one of those to a flow is a signal to the reader that a known pattern is in use.

### Standard comment headings

Comments carry the prose in the generated documentation. The recurring headings -
`config flow`, `connect to MQTT and decode messages`, `functional flow`,
`prepare and convert payload`, `encode and publish to MQTT`, `set filters`,
`set necessary input` - mirror the groups. The valuable ones are the
configuration contracts written in the `config flow` comment: which flow variables must be
set, what each means, where to get it. Only a minority of comment nodes carry a body; those are what
the good ones look like.

### Node types in use

Many distinct node types appear in the corpus. The ones that matter:

| Type | Role |
|---|---|
| `comment` | Documentation |
| `group` | Structure |
| `change` | Mapping and config |
| `function` | Transformation |
| `switch` | Filtering and routing |
| `debug` | Development aid |
| `link in` / `link out` | Inter-group routing |
| `inject` | Config trigger, timers |
| `mqtt in` / `mqtt out` | The spine |
| `split` | One packet at a time |
| `decode` / `encode` | Protobuf |
| `template` | Error and CSV text |
| `catch` | Error handling |
| `rbe` | Change detection |
| `http request` | Edge-platform config, webhooks |
| `delay` | Rate limiting |
| `csv` | Lookup tables |
| `join` | Batching |
| `OPCUA-IIoT-*` | Direct OPC UA read/browse/write |
| `influxdb out` | Local timeseries write |
| `ui-*` / `ui_*` | Local dashboards |

Subflows are in use at some sites. ⟨Subflow contents are not in the per-flow exports - read them on the instance.⟩

## Documentation coverage: how to measure it

The generated pages are built from four fields only (see `SKILL.md`, "Build so the documentation writes
itself"). To measure coverage on the day, over the flow exports:

- share of groups with a `name`;
- share of non-comment nodes with a `name`;
- share of `comment` nodes with a body;
- share of tabs with a non-empty `info` (the flow description).

Pattern to expect: groups are disciplined, node names are mostly present, comment bodies are a minority,
and flow-level descriptions are close to absent. The catalogue above was reconstructable only because the
*naming* convention held; it would be far better if every tab carried a description.
