# The PLCPacket message

Every `datatroniq/*` MQTT message in the estate is a protobuf-encoded `PLCPacketList`.
The schema is written to `/data/plcschema.proto` on the instance by an inject-once flow
(`Generate Text for Protobuffer Schema`), and the `decode` / `encode` nodes reference it
by file id with `protoType: PLCPacketList`.

```protobuf
syntax = "proto3";

package datatron;

option go_package = "/internal/protobuf";

message PLCPacket {
  string uuid = 1;
  int32 sequence_number = 2;

  uint64 sys_time = 3;
  uint64 plc_time = 4;

  oneof measured_value {
    sint64 value_integer = 5;
    string value_string  = 6;
    double value_double  = 7;
    bool   value_bool    = 8;
    bytes  value_bytes   = 9;
  }

  bool is_delta = 10;
}

message PLCPacketList {
  repeated PLCPacket plc_packets = 1;
}
```

In Node-RED the fields arrive camel-cased: `plcPackets`, `sysTime`, `plcTime`,
`valueInteger`, `valueString`, `valueDouble`, `valueBool`, `valueBytes`, `isDelta`,
`sequenceNumber`.

## Field usage across the corpus

Occurrences in function-node source across all 825 flows — a fair proxy for what flows
actually touch:

| Field | Uses |
|---|--:|
| `sysTime` | 5,974 |
| `uuid` | 2,586 |
| `plcPackets` | 1,891 |
| `valueDouble` | 730 |
| `valueString` | 513 |
| `isDelta` | 461 |
| `valueInteger` | 228 |
| `label` *(not in the schema — added by lookup)* | 219 |
| `valueBool` | 115 |
| `quality` *(not in the schema)* | 7 |

## `sys_time` — packed, not an epoch

The single most important detail. `sys_time` is a `uint64` carrying two 32-bit halves:

```
┌──────────── 32 bits ────────────┬──────────── 32 bits ────────────┐
│  seconds since 1970-01-01 UTC   │          nanoseconds            │
└─────────────────────────────────┴─────────────────────────────────┘
```

Unpack inbound, re-pack outbound. Both directions are in
[`standard-functions.js`](standard-functions.js). Symptoms of getting it wrong:

- Treating it as epoch **milliseconds** → timestamps in the 23rd century.
- Treating it as epoch **seconds** → timestamps far past any plausible date.
- Unpacking inbound and forgetting to re-pack outbound → the encode succeeds and every
  consumer downstream sees a broken time. **Nothing errors.** This is the most common
  silent corruption in the corpus's failure modes, and it is why the two functions are a
  pair, not two independent conveniences.

## `oneof measured_value` — exactly one value field is present

Because it is a protobuf `oneof`, a decoded packet carries **one** of the five value
fields. Two consequences the house pattern handles explicitly:

- **Reading:** do not assume `valueDouble`. Switch on which field is present, or configure
  the flow with the type it expects for that UUID.
- **Writing:** the standard *prepare for protob encoding* change node **deletes** the value
  fields that must not be sent, e.g. `delete msg.payload.valueDouble` when publishing a
  boolean. Sending two value fields is a malformed `oneof`.

## `uuid` is the identity; `label` is not in the message

The packet identifies its data point by UUID only. Human labels come from the IIoT edge
platform's data-point config (`GET {url}/{datatronId}/data_points`), which is why 195 flows
carry a *lookup uuid to label, including postprocessing* group and 219 function-node
references to `label` exist for a field the schema does not define.

Consequence for the timeseries data model: this is UUID-keyed long-format telemetry, and
the label is a **dimension joined in**, not a column of the fact. That is the archetype
the Grafana skill calls *timeseries* — see `build-grafana-ops-dashboard`.

## `is_delta`

Whether the packet reports a change rather than a cyclic sample. 461 function-node
references. Two uses in the corpus:

- **Filtering inbound** — `is delta true >> 1` switch nodes gate on it so a flow reacts to
  transitions rather than to every sample.
- **Asserting outbound** — the standard *format msg.payload* change node sets
  `payload.isDelta` explicitly on a derived packet. Do not let it inherit; state what the
  derived signal is.

## The outbound transformation, in order

The *prepare and convert payload* group does exactly this, and the order matters:

1. **`format msg.payload`** — set `isDelta`; set `uuid` from flow config (the **output**
   data point, not the input one); delete the value fields that do not apply.
2. **`prepare for protob encoding`** — delete Node-RED bookkeeping (`parts`,
   `protobufType`, `_msgid`); move `payload` into `payload.plcPackets[0]`.
3. **`Convert sysTime back`** — re-pack the timestamp.
4. **`encode`** → **`mqtt out`**.

Skipping step 2's `move` produces a packet that encodes without error and decodes to
nothing useful downstream, because `PLCPacketList` expects a `plc_packets` array.
