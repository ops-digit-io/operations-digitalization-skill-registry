# Pattern — Central Aggregation Server (Softing dataFEED OPC Suite)

The aggregation pattern: a Softing dataFEED OPC Suite server holds the driver connections
to the PLCs and exposes them as one OPC-UA address space, which the IIoT Edge Platform (or
another consumer) reads. No edge device in the machine cabinet, no 24 V supply, no
mounting — the cost sits in the server and its licences instead.

**Valid for BROWNFIELD.** (The OPC-UA-server data-source pattern is the one exception —
valid for brownfield *and* greenfield.)

> **Sourcing note.** The procedures below are the OESL integration guidance captured in the
> Equipment integration guide's `rules-next.json`, which references the OESL guideline
> documents *"Machine Integration — Softing DataFeed — Siemens S7-300 / S7-400 / S7-1200 /
> S7-1500 Integration"* and *"Machine Integration — Softing dataFEED — Beckhoff PLC
> Integration"*. Softing's own product documentation was **not reachable from this
> environment** (`industrial.softing.com` is blocked by the network egress policy), so
> vendor capability statements here are marked as such and should be checked against the
> current Softing manual before being relied on. ⟨Vendor manual — to attach.⟩

---

## The shape of every dataFEED data-source pattern

Whatever the driver, the procedure is the same eleven moves. Learn the shape once; the
per-driver sections below only differ in the italicised parts.

```
Log in to the Softing OPC-UA Aggregation Server
 1. Data Sources → select the *driver family*
 2. Create a new connection
 3. Name it uniquely — use the PLC name or machine name, matching the Machine List
 4. Enable the connection
 5. Select the *specific protocol variant*
 6. Configure the PLC address — IPv4, IPv6 or hostname
 7. Configure *protocol-specific advanced settings*
 8. Configure Read Optimization — do not read whole blocks for single variables
 9. Set the Cyclic Read interval
10. Prioritize read requests ahead of writes in the queue
11. Set value conversion (e.g. DateTime → text)
    → Connection Test
    → Define tags (three methods, below)
```

**Name the connection after the machine, not the PLC's role.** The connection name is what
ties the OPC-UA node back to a Machine List row; a connection called `PLC1` is unjoinable
six months later.

**Read Optimization and Cyclic Read are where an aggregation server is won or lost.** One
server carries many machines. A 100 ms cyclic read on a machine that reports a counter is
load spent for nothing; the guidance's own examples are **1000 ms** for Siemens, Rockwell
and Modbus, **500 ms** for Beckhoff. Start at the guidance value and justify anything
faster against a use case that needs it.

---

## Tag definition — three methods, in order of preference

Every driver offers the same three. This is the highest-leverage choice in the pattern.

| Method | What it is | Use when | Cost of getting it wrong |
|---|---|---|---|
| **Symbol File Import** | Import an **SDFI** file exported from the PLC program (S7 project etc.) | Default. You have the PLC program — which the breakpoint already required | — |
| **Import Items Wizard** | Import a `.txt` in Softing's custom data format | You have a tag list but not an importable project | Format errors surface as missing items, not as an error |
| **Manual Definition** | Type each tag: name + syntax identifier | A handful of tags, or a protocol with no symbol export | Silent address typos; unmaintainable past ~20 tags |

Syntax identifiers differ per driver:

| Driver | Example identifier |
|---|---|
| Siemens S7 / TIA | `DB15,INT1032` |
| Beckhoff ADS | `GlobalVar.intSpeed` |
| Modbus | `Holding Register, HR300` |
| Rockwell | `DB15,INT1032` *(as written in the guidance)* |

**Structure the tags to a data model, not to the PLC's layout.** The guidance says to
define tags "in a structured way (e.g. **CT Base** or other data model integration)". This
is the moment cross-plant comparability is decided: a tag named for its data-block address
is a tag nobody at another plant can match. `Data model standardization (CT Base)` is
already the single most-recorded integration blocker in the estate — 23 machines — which is
what it looks like when this step is deferred.

**Split mandatory from optional tags in the Machine CV.** Every route asks for it. A
mandatory tag missing at acceptance is a rework; an optional one missing is a note.

---

## Driver pattern — Siemens S7 (S7-300 / 400 / 1200 / 1500)

*Data source:* **Siemens**

| Step | Setting |
|---|---|
| Protocol variant | Siemens S7 · **Siemens S7-2** · Siemens S5 · **Netlink** · … |
| Address | IPv4 / IPv6 / hostname |
| Advanced | **Header definition** (e.g. RFC1006 header) · **Write permission** (only if values must be sent *to* the PLC) · **RFC1006 settings**: Service, **Rack**, **Slot** |
| Read optimization | On — avoid reading complete blocks for single variables |
| Cyclic read | e.g. **1000 ms** |
| Request priority | Reads before writes |
| Conversion | DateTime → text |
| Verify | **Connection Test** |

**Rack and slot are the classic failure.** An S7-300 and an S7-1500 do not use the same
rack/slot pair, and a wrong one produces a connection that refuses rather than one that
returns bad data — which is the good failure mode. Use the Connection Test before defining
a single tag.

**Leave Write Permission off unless a use case writes to the PLC.** Read-only is the
default posture; enabling writes on an aggregation server that fronts many machines widens
the blast radius of a misconfigured item far beyond one machine.

**Netlink is the protocol variant for a Helmholz NetLink gateway** — the OT device the
budget block keeps naming. That is the route for a PLC with no Ethernet interface of its
own: the gateway bridges MPI/PROFIBUS to Ethernet and dataFEED speaks to the gateway.

## Driver pattern — Siemens TIA

Identical to S7, with one binding constraint:

> **Protocol variant `Siemens S7-2` is for SIMATIC S7-1200 and S7-1500 only.**

Selecting S7-2 for an S7-300/400 is a misconfiguration. Given that the S7-300 is the single
largest PLC model in the estate, this is a mistake with plenty of opportunity to occur.

## Driver pattern — Beckhoff

*Data source:* **Beckhoff**

| Step | Setting |
|---|---|
| Protocol variant | **ADS** |
| Address | PLC IP plus **port and route settings** |
| Advanced | **ADS port**, **target and source AMS Net IDs**, synchronization settings |
| Read optimization | On |
| Cyclic read | e.g. **500 ms** |
| Request priority | Reads and writes both managed |
| Verify | Connection Test |
| Tags | `GlobalVar.intSpeed` style symbolic names |

**ADS needs a route on both ends.** Unlike the Siemens pattern, the target PLC must know
the AMS Net ID of the requesting system. An ADS connection that fails despite a correct IP
is almost always a missing route entry on the PLC side, not a network problem.

Beckhoff's OT hardware line in the budget block is **EtherCAT terminals**, not a NetLink
gateway — the shopping list differs from the Siemens one.

## Driver pattern — Rockwell / Allen Bradley

*Data source:* **Rockwell**

| Step | Setting |
|---|---|
| Protocol variant | per Rockwell family (ControlLogix / CompactLogix / SLC-500 / PLC-5) |
| Address | IP plus **port settings and network configuration** |
| Advanced | **Network timeouts**, **data refresh rates**, **error handling** |
| Read optimization | On — explicitly to minimise network load |
| Cyclic read | e.g. **1000 ms** |
| Request priority | Reads and writes sequenced |
| Verify | Connection Test |

Rockwell is the second-largest vendor family in the estate and carries the largest share of
`EVALUATION ONGOING` machines — the route decision is genuinely open more often here than
for Siemens. Where the estate records a route, it splits edge / aggregation roughly 78 / 30.

## Driver pattern — Modbus

*Data source:* **Modbus**

| Step | Setting |
|---|---|
| Protocol variant | **TCP** or **RTU** |
| Address | IPv4 / IPv6 / hostname |
| Advanced | **Timeouts**, **polling intervals**, **retries** |
| Read optimization | On |
| Cyclic read | e.g. **1000 ms** |
| Conversion | **Raw counts → engineering units** |
| Tags | `Holding Register, HR300` |

Two things are Modbus-specific and both are silent failures:

- **Modbus has no type system.** A holding register is sixteen bits and nothing tells you
  it is a temperature in tenths of a degree. The conversion step is where that meaning is
  applied, and if it is skipped the data flows and is wrong — no error anywhere.
- **RTU is serial.** Choosing RTU means a serial link and its own physical constraints;
  it is not a variant of TCP with a different checkbox.

## Driver pattern — OPC-UA server as a data source

*Data source:* **OPC UA Server** · **valid for BROWNFIELD and GREENFIELD**

| Step | Setting |
|---|---|
| Create | New server instance |
| Identity | Unique server name; **URL and port** |
| Enable | Activate the instance |
| Security | **Encryption and authentication methods** |
| Endpoints | **Security profiles**; any **user roles** |
| Communication | **Session timeouts**, **data transfer limits** |
| Performance | Tune for expected traffic and data load |
| Verify | Test connectivity **and** security settings |
| Deploy | Go live |
| Operate | Monitor performance and stability with dataFEED's own tools; keep server and security settings updated |

This pattern's preparation block is different from the PLC ones: the breakpoint is
**server software and licences**, not a PLC program, and the record is a **Server List**
(name, URL, port, security settings) rather than the Machine List alone.

It is the only pattern in the guide that carries an explicit **operate** phase. Take that
seriously — an aggregation server is a shared dependency, and "monitor performance and
stability" is the difference between one machine failing and every machine behind that
server failing at once.

---

## What Softing can do that the OESL tree does not route

From Softing's published product capabilities (search-result summary; **vendor manual not
verified from this environment**):

- **Controllers:** Siemens S5, S7 and SINUMERIK · FANUC CNC · Rockwell SLC-500, PLC-5,
  ControlLogix, CompactLogix · Mitsubishi MELSEC-Q · B&R · Modbus TCP devices
- **Also as sources:** any controller with an integrated OPC UA server or MQTT publisher
- **Files and databases:** XML, TXT and CSV read/write; ODBC-compatible databases; MongoDB,
  CouchDB, InfluxDB
- **As sinks:** production data to file, SQL database, MongoDB or CouchDB

Three of these are routes the OESL tree has no entry for — **S5**, **FANUC CNC**, and the
file/database sources. A product capability is **not** an approved OESL route. If one of
them would solve a machine, that is a case to put to the IIAE and, if adopted, a change to
`rules.json` — not something to configure on the server because the product allows it.

`rules-next.json` adds an `siemens_s5` question, so the S5 gap at least is known.

---

## Fallbacks specific to this pattern

| Situation | Do this |
|---|---|
| Softing server **not available** at the plant | The aggregation route is **closed**. Go to the edge route, or to rollout preparation. There is no partial version |
| Server available but **no licence** for the driver | Procurement, not configuration. The OPC-UA pattern names this as its own breakpoint |
| **PLC program unavailable** | The breakpoint applies here too — see [`fallbacks.md`](fallbacks.md) |
| PLC has **no Ethernet interface** | Helmholz NetLink or equivalent gateway, then the **Netlink** protocol variant |
| Connection Test **fails** | Siemens → rack/slot and RFC1006 header. Beckhoff → AMS route on the PLC. Rockwell → timeouts and port. Do not start defining tags |
| Connection up, **tags empty or wrong** | Symbol file mismatch against the running PLC program version. Re-export from the deployed program, not from an archived project |
| Server **overloaded** as machines are added | Raise cyclic-read intervals to the guidance values first; read optimization on; only then discuss a second server |
| Machine is a **camera** | Not connectable to any aggregation server. Edge only |
