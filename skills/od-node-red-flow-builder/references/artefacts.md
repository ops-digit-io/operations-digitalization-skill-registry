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
