---
type: Skill Reference
title: Softing data targets
description: How data leaves a dataFEED configuration - the data source and data target model, and which targets are in use.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [integration, softing]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Softing dataFEED — how the data leaves

A dataFEED configuration is a container of **data sources** and **data targets**. The
[driver patterns](softing-datafeed.md) cover the sources; this covers who consumes them,
what OESL actually uses, and four product capabilities that have no OESL route but change
what is possible if one were opened.

**Source:** Softing dataFEED OPC Suite V5.70 manual, ch. 9.3 (p. 844 ff.), at
`_knowledge/machine-integration-guidance-app/dataFEEDOPCSuite_de.pdf`.

> **"Data source" and "data target" do not describe flow direction** (p. 25). They say who
> *defines* the datapoints and who *uses* them. The actual flow is usually bidirectional —
> an OPC UA server is a typical data source, and its client normally both reads and writes.
> Keep this straight when reading the manual: a "target" is not necessarily downstream.

---

## The full target list

| Data target | Manual p. | Used by OESL today |
|---|--:|---|
| **OPC UA Client** | 845 | ✅ — indirectly: the IIoT Edge Platform is the UA client |
| OPC Client (Classic) | 928 | ❌ |
| OPC Classic Tunnel Client | 931 | ❌ |
| **MQTT Broker** | 937 | ❌ **no OESL route** — see below, this is the interesting one |
| Database (SQL / ODBC) | 1000 | ❌ |
| REST Server | 1085 | ❌ |
| MPDV MIP Server | 1157 | ❌ |
| NoSQL database | 1216 | ❌ |
| File | 1302 | ❌ |
| Web Service | 1360 | ❌ |

Plus three functions that act on the local address space rather than moving data out of it:

- **Exchange** — server-to-server or server-to-PLC data exchange.
- **Store and Forward** — buffers locally when a connection drops, resumes when it returns.
- **Preprocessing Engine** (p. 764) — mathematical and logical calculations across
  datapoints, written into other datapoints.

All three require the participating datapoints to exist in the local address space first
(p. 25). You cannot preprocess a value you have not defined as a tag.

---

## The OESL path today: dataFEED as an OPC UA server, edge as the client

This is the only approved route. The OESL recommendation text describes it from the *edge*
side and the manual describes it from the *server* side, so people talk past each other.

```text
PLC ──driver──► dataFEED data source ──► local address space ──► OPC UA server interface
                                                                          │
                                                      OPC UA  ────────────┤
                                                                          ▼
                                             IIoT Edge Platform  ── DTQ-OPCUA-Connector
                                                                          │
                                                                    MQTT / protobuf
                                                                          ▼
                                             Node-RED → Databricks → Azure Storage (Parquet)
```

**The edge is the UA client, and `DTQ-OPCUA-Connector` is how it connects.** That makes the
aggregation server a concentrator in front of the edge rather than a parallel route: this is
variant ③ of three ingress shapes, and every machine behind it still reaches the data
platform through the IIoT Edge Platform. Both pieces are required — a Softing server with no edge
platform behind it delivers nothing.

The OESL tasks for this route — *"connection details available (IP addresses, credentials,
certificates)"*, *"the structure on the OPC-UA Server is clear and known"*, *"endpoints
connected according to OT Cyber Security Rules"* — map onto the manual's endpoint and
security settings. Three of them decide whether it works:

**The address-space structure is the interface.** Every connection name becomes the root of
that device's namespace (p. 156), so the node ids the edge subscribes to are literally
`<connection name>.<tag name>`. Renaming a connection after the edge is configured breaks
every subscription. **Name connections from the Machine List on day one and do not rename
them.**

**Security is a matched pair.** The server's endpoint has to offer what the client asks
for. On the source side dataFEED offers message security mode `None` / `Sign` /
`Sign & Encrypt` and policies `None` / `Basic128RSA15` / `Basic256Sha256`, with certificate
handling of *accept all automatically* or *only trusted*, and authentication of
`Anonymous` / user name / certificate (p. 354). The same vocabulary applies at the server
endpoint the edge connects to. *Accept all automatically* is a commissioning convenience,
not a configuration — OT cyber-security rules mean named trust.

**Certificate regeneration can silently disable an endpoint.** With `Basic256Sha256`
enabled, regenerating certificates at a smaller key size disables the Basic256Sha256
endpoint (p. 340). A client that suddenly cannot negotiate security after a certificate
refresh is usually this, not a network change.

---

## The capability with no route: dataFEED publishing straight to MQTT

OESL's spine is MQTT — `datatroniq/data/protob/plc/…` carrying protobuf `PLCPacketList`,
consumed by Node-RED (see `od-node-red-flow-builder`). dataFEED can publish to an MQTT
broker directly, as a data target, without an edge device in between.

**There is no OESL route for this, and this section is not permission to build one.** It is
here so that when the question comes up — and on a plant with an aggregation server and no
edge devices it will — the answer is informed rather than improvised. Opening it would be a
change to `rules.json` and a data-model decision, because the payload would not be
`PLCPacketList`.

What the product does (p. 937–999):

**Protocol and identity.** MQTT versions `3 Auto Mode` (default), `3.1`, `3.1.1`, `5`.
Broker URI carries the transport: `tcp://` (typically 1883), `ssl://` (8883), `ws://`
(8000), `wss://` (443).

> **Client ID collisions fail silently in the worst way.** The client ID must be unique on
> the broker; if two clients use the same one the broker disconnects — and *the client
> cannot tell that the ID was already in use* (p. 945). A dataFEED publisher that keeps
> dropping for no visible reason, on a plant where somebody cloned a configuration, is this.
> Brokers can be configured to accept only known client IDs, which is the defence.

**Payload.** The publisher writes values as UTF-8 strings, and the format is set **per
topic**. The available format includes *JSON text with datapoint ID, value, timestamp and
quality* (p. 962) — structurally the same four fields as a `PLCPacket` (`uuid`,
`measured_value`, `sys_time`, and quality), but JSON rather than protobuf and with a
different time encoding. That difference is exactly why this would be a data-model decision
and not a wiring change: `od-node-red-flow-builder`'s decode stage expects
`PLCPacketList`, and its `sysTime` is a packed 64-bit value, not a formatted string.

**Topic names are constrained.** Printable ASCII only, and the characters `.`, `/`, `+` and
`#` may not appear in a name segment (p. 961) — the last two because they are MQTT
wildcards. The topic tree is built in the configurator, and topics can be exported and
imported, with four merge modes for what happens to properties of topics that already
exist (p. 964–966).

**Date and time formatting is a per-connection setting** (p. 970) — date formats
`mm/dd/YYYY` (default), `dd-mm-YYYY`, `dd.mm.YYYY`, `dd/mm/YYYY`, `YYYY-mm-dd`,
`mm-dd-YYYY`; time formats `HH:MM:SS pp` (default), `HH:MM:SS.FFF pp`, `HH:MM:SS.FFF`,
`HH:MM:SS`. **The default is US-formatted with a 12-hour clock**, which is not what any
downstream consumer at OESL would expect. If this route were ever opened, `YYYY-mm-dd` and
`HH:MM:SS.FFF` would be the settings to standardise on. Note also that a `DATETIME`
datapoint rendered with a milliseconds format shows milliseconds as zero.

**Last Will and Testament** (p. 966) is how a broker announces that a publisher has gone
away without saying goodbye. The manual's own pattern is worth copying anywhere it is used:
publish `Disconnected` as the last will on `<client id>/state`, publish `Connected` to the
same topic after connecting, and publish `Disconnected` yourself on a clean shutdown. A
consumer can then tell "no new data because nothing changed" from "no new data because the
publisher is gone" — a distinction the OESL spine currently has no equivalent of.

**Backup broker** (p. 951) — a second broker with its own certificates and validation, for
failover.

**Clean session / clean start** (p. 970) — whether the broker reuses the session associated
with the client ID. On MQTT 5 this pairs with a clean-session timeout bounding how long a
session survives a network fault.

**Store and Forward is available per MQTT connection** (p. 972).

---

## Store and Forward, properly

The answer to "what happens to our data during a network outage", and it is a **licensing**
question before it is a configuration one.

| Variant | Licence |
|---|---|
| OPC Classic Store and Forward | Suite **Base** and Extended |
| **OPC UA Store and Forward (server side)** | Suite **Extended** only |
| Per-connection S&F on an MQTT target | with the MQTT target |

The system stores data locally while the connection is down and resumes transmission when
it returns (p. 25). Two things to settle before relying on it: how much buffer the local
disk allows, and what the consumer does with a burst of backdated values on reconnect — a
dashboard that plots by arrival time rather than by source timestamp will draw a spike that
never happened.

---

## Preprocessing Engine — a data-model decision

The Preprocessing Engine (p. 764–843) runs **mathematical** (p. 777) and **logical**
(p. 784) expressions over datapoints and writes the result into other datapoints, which are
then available to clients like any other tag.

It is useful — a derived rate, a unit conversion, a simple state machine — and it is also
the easiest place in the estate to accidentally create a value that exists at one plant and
nowhere else.

**Deriving a value here is a data-model decision, not a local convenience.** The same
finding sits at the top of the estate's blocker list: *Data model standardization (CT Base)*,
a very common blocker. If a derived value is worth having at one plant it is worth defining once for
all of them → `od-signal-standardization`, Consultation with Plant ME / Plant IT. If it is
genuinely local — a machine-specific scaling nobody else has the machine for — say so in
the tag name and in the Machine CV.

The same argument applies one layer up, to Node-RED: a transformation buried in a function
node is a per-plant transformation too. The rule does not change with the tool.

---

## What to do with the unrouted targets

Database, REST, NoSQL, file and web-service targets exist and have no OESL route. Before
anyone proposes one, the department's own position applies: the strategy is a deliberately
**small operational footprint**, and broad tool proliferation is an explicit non-bet. A
dataFEED target that writes directly into some other system is a second integration path
around the data platform, and the data platform is the seam the whole department is built on.

The case that would justify opening one is a use case that cannot be served through the
data platform, named, with its benefit estimated (or calculated with a documented basis) — the same bar as any other intake. Put
it to the IIAE and the OD lead, not into a configuration.
