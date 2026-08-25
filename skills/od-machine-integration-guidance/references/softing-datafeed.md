# Pattern — Central Aggregation Server (Softing dataFEED OPC Suite)

The aggregation pattern: a Softing dataFEED OPC Suite server holds the driver connections to
the PLCs and exposes them as one OPC UA address space, which the **IIoT Edge Platform** then
reads through the **`DTQ-OPCUA-Connector`**. No edge device in the machine cabinet, no 24 V
supply, no mounting — the cost sits in the server, its licences and its operation instead.

> **This is a concentrator, not a destination.** It is **variant ③** of three ingress shapes
> — the department's *Concept 1 — Central OPC-UA Server*, recorded at 11 plants. Machines
> behind the Softing server are integrated into the IIoT Edge Platform via OPC UA and reach
> the MDL through it like every other machine. ③ therefore needs **both** pieces — the
> guide's own Siemens S7 recommendation says you cannot connect the PLCs *"when you have
> chosen the OPC-UA server as the connectivity framework **and you don't have the IIoT Edge
> Computing Platform available**"*. See [`iiot-edge-platform.md`](iiot-edge-platform.md)
> § *The bridge* and § *The three integration concepts*.

**Valid for BROWNFIELD.** (The OPC-UA-server data source is the exception — brownfield and
greenfield.)

**Sources.** Product behaviour is from the **Softing dataFEED OPC Suite V5.70 operating
manual** (German, 1,540 pp., dated 2026-02-16), in the knowledge bundle at
`_knowledge/machine-integration-guidance-app/dataFEEDOPCSuite_de.pdf`. Page references
below are to that manual. OESL process is from the Equipment integration guide
(`rules.json` / `rules-next.json`). Where the two disagree, **§ Where the OESL guidance
does not match the product** says so — read that section before following any procedure.

---

## ⚠ Where the OESL guidance does not match the product

Two things in the OESL recommendations cannot be done as written in V5.70. Both are in the
happy path of a route somebody will try this month.

### 1. There is no Beckhoff data source

The OESL recommendation *Central Aggregation Server — Beckhoff Integration* says:

> *"Navigate to Data Sources and select **Beckhoff** … Choose the appropriate Beckhoff
> protocol (such as **ADS**) … Configure advanced settings specific to Beckhoff
> Communication Protocol, focusing on **ADS port, target and source IDs**…"*

**dataFEED OPC Suite V5.70 has no Beckhoff data source and no ADS driver.** The complete
data-source list is below; Beckhoff is not on it. In the entire 1,540-page manual the word
"Beckhoff" appears **once** — as an example of a vendor whose controllers speak *Modbus*
(p. 222).

So a Beckhoff PLC reaches the aggregation server only by one of:

| Route | Requires |
|---|---|
| **Modbus data source** | The Beckhoff PLC exposes Modbus TCP — the manual's own example vendor list for Modbus is "Schneider Electric, Wago, **Beckhoff**" |
| **OPC UA Server data source** | A TwinCAT OPC UA Server in front of the PLC |
| **OPC Server (Classic) data source** | A TwinCAT OPC DA server |

The native ADS path is the **edge** route and its `DTQ-Beckhoff-Connector` — which is the
branch `rules.json` still marks `TODO`. Net effect: **Beckhoff has no fully-written route
on either platform.** Say that plainly and take it to the IIAE rather than following a
procedure for a driver that is not there.

### 2. NetLink is discontinued

The OESL recommendations list the Siemens protocol options as *"Siemens S7, Siemens S7-2,
Siemens S5, **Netlink**, etc."*. The manual (p. 161):

> *"The NetLink protocol was discontinued with version 5.38. In existing configurations
> based on older versions that still use NetLink, the protocol remains available. We
> strongly recommend migrating these configurations to Siemens S7."*

Do not select NetLink on a new connection — it is not offered. A **Helmholz NetLink
gateway** is still the right OT hardware for a PLC with no Ethernet of its own; you simply
address it with the **Siemens S7** protocol now. The hardware and the protocol name are two
different things, and the OESL text conflates them.

Existing configurations still running NetLink are migration candidates. ⟨Whether any OESL
plant has one — to check.⟩

---

## What dataFEED can actually connect (V5.70)

**Data sources** (p. 153 ff.) — where datapoints are defined:

| Data source | Manual p. | In the OESL tree? |
|---|--:|---|
| Siemens devices (S7 · S7-2 · S5 · Send/Receive) | 155 | ✅ |
| Siemens SINUMERIK CNC devices | 183 | ✅ *(next tree)* |
| Modbus devices | 222 | ✅ |
| Rockwell devices | 242 | ✅ |
| B&R devices | 257 | ⚠️ `TODO` |
| Mitsubishi devices | 272 | ✅ (task list only) |
| **FANUC CNC devices** | 287 | ❌ no route |
| OPC UA Server | 315 | ✅ *(next tree)* |
| OPC Server (Classic) | 368 | ❌ no route |
| OPC Classic Tunnel Server | 404 | ❌ no route |
| **Database read** (ODBC) | 439 | ❌ no route |
| **MQTT Broker** | 484 | ❌ no route |
| **MQTT Publisher** | 548 | ❌ no route |
| **File read** | 580 | ❌ no route |
| Local datapoints | 616 | — |

**Data targets** (p. 844 ff.) — who consumes them: OPC UA Client · OPC Client · OPC Classic
Tunnel Client · MQTT Broker · Database · REST Server · MPDV MIP Server · NoSQL database ·
File · Web Service.

> "Data source" and "data target" **do not describe flow direction** (p. 25). They say who
> *defines* the datapoints and who *uses* them; the actual flow is usually bidirectional.

**Also available, and relevant to OESL:**

- **Store and Forward** — buffers locally when the connection drops and resumes when it
  returns. OPC Classic S&F is in Base and Extended; **OPC UA Store and Forward (server
  side) is Extended only** (p. 46). This is the answer to "what happens to data during a
  network outage", and it is a licensing question before it is a configuration one.
- **Preprocessing Engine** (p. 764) — mathematical and logical calculations across
  datapoints, written into other datapoints. Deriving a value here rather than downstream
  is a **data-model decision**, not a local convenience → `od-signal-standardization`.
- **Exchange** (p. 25) — server-to-server or server-to-PLC data exchange.

Five of these — FANUC, database read, MQTT as a *source*, file read, OPC Classic — are
product capabilities the OESL tree has no route for. **A capability is not an approved
route.** Put the case to the IIAE; if adopted it becomes a change to `rules.json`.

---

## Licences, before anything else

Licensing is per driver family, and a missing one is the fastest way to lose an afternoon
(p. 45–54):

| Licence | Unlocks |
|---|---|
| **dataFEED OPC Suite Extended** | Everything: OPC Classic + UA client/server, both tunnels, **OPC Classic and OPC UA Store and Forward**, Exchange, Local Items, SQL (ODBC) and NoSQL, file read/write, and connections to the **SINUMERIK, Rockwell and Mitsubishi** families |
| dataFEED OPC Suite Base | The classic/UA interfaces and OPC Classic Store and Forward, without the extended set |
| dataFEED **OPC Server Siemens / CNC / Rockwell / Mitsubishi / Modbus / B&R** | One PLC family each |
| dataFEED OPC Server **Extension 50** | Concurrent access to up to **50** OPC UA / OPC / tunnel servers |
| OPC Organizer Classic / UA | Gateway between OPC standards — but **limited to 1 server connection** without the Extension licence |

Three rules that bite:

1. **The licence major version must match the product major.** A 5.00 key unlocks 5.xx; a
   4.00 key does not. Higher-version licences do unlock lower product versions.
2. **Only *started* configurations consume licence items.** Stopped configurations are free.
3. **Changing licences while the local application is running stops it**, and the
   configuration shows the expired-demonstration icon.

**Capacity:** up to **100 configurations**, of which **50 can run concurrently** (p. 25).
Split configurations so that connections you want to start, stop or test together live
together — that is the manual's own advice, and it is what lets one plant's machines be
restarted without touching another's.

---

## The shape of every data-source pattern

Whatever the driver, the moves are the same. Learn the shape once; the per-driver sections
only differ in the italicised parts.

```
Configurator → Data Sources → *driver family*
 1. Add a connection                                    (button, context menu, or CTRL+A)
 2. Name it — unique in the configuration
 3. Enable it                                           (disabled = greyed out, ignored at runtime)
 4. Select the *application protocol*
 5. Target address — IPv4, IPv6 or DNS host name
 6. *Protocol-specific advanced communication settings*
 7. Global settings (all connections of that family) vs Advanced settings (this connection)
 8. Connection Test  ← before defining a single tag
 9. Define the address space — three import methods
```

**The connection name becomes the root of that device's namespace** (p. 156), so it is what
every OPC-UA node id downstream is prefixed with. Three consequences:

- **Name it after the machine**, matching the Machine List. A connection called `PLC1` is
  unjoinable six months later.
- It must be **unique** in the configuration.
- It must contain **no address-space delimiters, no multi-byte characters and no spaces**.
  This is a hard constraint, not a style preference.

**Copy Connection** (context menu only) duplicates a connection, proposing `<name>_Copy` and
defaulting the address to `localhost` (p. 159). For a line of near-identical machines this
is the right tool — and remember to change *both* the name and the address.

**A connection cannot be deleted** while any datapoint from its address space is still used
by a processing function or a data target (p. 158). If a delete is refused, that is why.

**Simulation mode** puts a connection into simulation (it shows red in the list) — useful
to build and test a configuration before the machine exists. **Not available for S7-2
connections.**

---

## Tag definition — three methods

Every PLC driver offers the same three. This is the highest-leverage choice in the pattern.
Syntax detail for every family is in [`softing-tag-syntax.md`](softing-tag-syntax.md).

| Method | What it is | Use when | Failure mode |
|---|---|---|---|
| **Symbol file import** | Import an **SDFI** file exported from the PLC program (p. 637) | Default — you already had to have the PLC program to pass the breakpoint | Mismatch against the *deployed* program version |
| **Import Items Wizard** | Import a `.txt` in Softing's format (p. 646) | You have a tag list but not an importable project | Format errors surface as missing items, not as an error |
| **Manual definition** | Type each tag: name + syntax identifier (p. 688) | A handful of tags, or a family with no symbol export | Silent address typos; unmaintainable past ~20 tags |

When adding a datapoint manually, **access rights and data type are read-only** — access
rights come from the connection, and the data type is derived automatically from the syntax
you type (p. 688). A tag whose type is not what you expected is a syntax problem, not a
type problem.

**Structure tags to the data model, not to the PLC's layout.** The OESL guidance says "in a
structured way (e.g. **CT Base**)". This is the moment cross-plant comparability is decided:
a tag named for its data-block address is a tag nobody at another plant can match.
*Data model standardization (CT Base)* is already the most-recorded integration blocker in
the estate — 23 machines — which is what deferring this step looks like.

**Split mandatory from optional tags in the Machine CV.** Every OESL route asks for it. A
mandatory tag missing at acceptance is a rework; an optional one missing is a note.

---

## Driver — Siemens (S7-300 / 400 / 1200 / 1500, S5)

*Data Sources → Siemens.* Manual p. 155–182, advanced comms p. 163.

**Application protocols (p. 161):** `Siemens S7` · `Siemens S7-2` **(SIMATIC S7-1200 and
S7-1500 only)** · `Siemens S5` · `Send/Receive`. NetLink is discontinued — see the warning
at the top.

### Advanced communication settings — S7

| Setting | What it does | Guidance |
|---|---|---|
| **No header** | For partners speaking raw TCP/IP only; the application must monitor both ends | — |
| **RFC1006** | Packs H1 telegrams into TCP/IP | The normal choice for S7 |
| **Life Data Acks** | Empty user-data telegrams to hold an idle connection open | **Softing recommends OFF for S7 PLCs** |
| **Acks** (keep-alive) | Enables socket-library connection monitoring | **Softing recommends ON.** With it off, the connection is considered closed after KeepAliveTime *without telling the partner* |
| **Write allowed** | Permits writing to the PLC and opens a write connection | **Leave off unless a use case writes.** Note: every write is preceded by a read |
| **Use High Performance Protocol** | Converts accesses to variables in *different* operand areas (`DB5.W3 + MW1 + T2`) into a single field access | Fewer packets, better packing, lower network load, faster server. Turn it on |
| **Read / write ports** | 16-bit, 1–65535 | Must be **identical on both sides**. Read, write and event ports must **differ from each other**. Avoid 1–1023 (well-known ports) |

### RFC1006 settings — the classic failure

| Field | Values |
|---|---|
| **Service** | `01` PG or PC · `02` OS (operator/monitoring device) · `03` Others (e.g. OPC server, SIMATIC S7 PLC) |
| **Rack** | The rack holding the CPU: **0 to 7** |
| **Slot** | The slot holding the CPU: **0 to 31**. **For an S7-300 the slot is always 2** |
| **Local / remote TSAP** | Required for RFC1006. **They must cross-match**: the local TSAP of one system must equal the remote TSAP of the other, or the connection will not come up |

Rack and slot are the most common Siemens misconfiguration, and they fail *well* — the
connection refuses rather than returning bad data. **Run the Connection Test before defining
a single tag.**

### S7-2 advanced settings (S7-1200 / 1500 only)

`Advanced settings` is available **only for S7-2 connections** (p. 157). All values are
per-connection, and the configurator validates the constraints between them (p. 683–686):

| Parameter | Default | Range |
|---|---|---|
| Service timeout | 30 s | 1–600 s |
| Service queue size | 1000 | 100–5000 — calls beyond the queue are rejected |
| Connection timeout | 10 s | 1–600 s — also the watchdog: no traffic for this long and the connection is dropped |
| Connection check period | 5 s | 1–600 s — the keep-alive interval |
| Request timeout | 5 s | tune to network latency and PLC performance |
| **Security connection timeout** | **55 minutes** | see below |

> **Security connection timeout is a real operational trap.** Siemens devices require a
> periodic security-token exchange, and current firmware requires it **hourly**; the
> connection is dropped automatically if the exchange fails. The manual warns: **if this
> value is larger than the controller's own connection-monitoring interval, data can be
> lost** between the disconnect and dataFEED re-establishing the connection. Leave it at 55
> minutes unless you know the controller's interval, and if you change it, change it *down*.

---

## Driver — Rockwell / Allen Bradley

*Data Sources → Rockwell.* Manual p. 242–256. Covers ControlLogix / CompactLogix and the
PLC-5 / SLC families (separate tag syntax — see [`softing-tag-syntax.md`](softing-tag-syntax.md)).

One ControlLogix-specific global setting is worth knowing before anyone reports a bug
(p. 657):

> **"Wait for ControlLogix browsing to finish before registering datapoints."** After a
> program start the tags of a CLX connection are compared against the online PLC, and this
> can take a while. Registering datapoints during that window makes the server report
> *datapoint not available*. With this option on, registration blocks the OPC client until
> browsing completes.

A CLX connection that reports missing datapoints immediately after a restart and is fine
later is this, not a wiring fault.

Rockwell is the second-largest vendor family in the OESL estate and carries the largest
share of `EVALUATION ONGOING` machines — the route decision is genuinely open more often
here than for Siemens.

## Driver — Modbus

*Data Sources → Modbus.* Manual p. 222–241. Protocol variants **TCP** and **RTU**; the
manual's example device vendors are *Schneider Electric, Wago, Beckhoff*.

Two Modbus-specific behaviours, both silent:

- **Modbus has no type system.** A holding register is sixteen bits and nothing says it is a
  temperature in tenths of a degree. Conversion to engineering units is where meaning is
  applied; skip it and the data flows and is wrong, with no error anywhere.
- **Discrete inputs and outputs are read-modify-written 8 bits at a time.** They occupy one
  bit on the PLC, but a write reads 8 bits, flips the one, and writes 8 back. The manual's
  own warning: *if another bit of that byte changes in the meantime, it is overwritten with
  the old value.* One more reason to leave write access off.

Global setting: **Discard read responses of invalid byte count** — discards TCP
retransmissions of Modbus read responses (p. 657).

**RTU is serial.** It is not a checkbox variant of TCP; it brings its own physical layer.

## Driver — B&R, Mitsubishi, SINUMERIK, FANUC

All four exist as data sources (p. 257, 272, 183, 287) with their own connection wizards.
Each needs its **own licence** — `dataFEED OPC Server B&R`, `… Mitsubishi`, `… CNC` — or
Suite Extended.

**FANUC CNC has no OESL route at all**, and the manual carries a FOCAS2 address-space and
error-code section (p. 310–314) for it. If OESL has FANUC CNCs that need integrating, that
is an IIAE conversation, not a configuration task.

## Driver — OPC UA Server as a data source

*Data Sources → OPC UA Server.* Manual p. 315–367. **Valid for brownfield and greenfield.**

This is the route when a machine already fronts itself with an OPC UA server — the cheapest
path in the whole guide, because there is no PLC program, no tag export and no cabinet work.

**Security configuration** (p. 354):

| Setting | Options |
|---|---|
| **Message security mode** | `None` (readable on the wire; fastest and least secure) · `Sign` (integrity, body not encrypted) · `Sign & Encrypt` (private and integrity-assured) |
| **Security policy** | `None` · `Basic128RSA15` · `Basic256Sha256` |
| **Server application certificate** | Accept **all** server certificates automatically · Accept **only trusted** certificates (trust one via certificate management) |
| **Authentication** | `Anonymous` · `User name` + password · `Certificate` |

**"Accept all server certificates automatically" defeats the point of the certificate.** It
is a commissioning convenience. Endpoints must be connected per OT cyber-security rules
(Connext Wiki), and that means named trust, not blanket acceptance. Note also that with
`Basic256Sha256` enabled, regenerating certificates with a smaller key size disables the
Basic256Sha256 endpoint (p. 340).

**Advanced connection settings** (p. 325–327): session name (auto-generated as
`Softing dataFEED Suite <ConfigurationName>`), **session timeout** default 60 s (1–3600),
network timeout default 60 s.

**Reverse connections need an openable port.** The connection test starts a Reverse
Listener and waits for the server to connect; if the port on the client endpoint URL is
already held by another application, another dataFEED configuration, or the running runtime
of *this* configuration, **the test fails** (p. 325). A reverse-connection test that fails
while everything looks correct is usually this.

The connection-test dialog **cannot be cancelled** and can run for the full network timeout.

---

## Commissioning hygiene

**Turn tag browsing off once commissioning is done** (p. 657). Where a server has a large
symbol table, browsing transfers it to the client on request — memory and CPU. Switching it
off after commissioning shortens server start-up after a restart. On an aggregation server
carrying many machines this is not a micro-optimisation.

**Cyclic read intervals are where a shared server is won or lost.** The OESL guidance's own
examples are **1000 ms** for Siemens, Rockwell and Modbus. A 100 ms read on a machine that
reports a counter is load spent for nothing. Start at the guidance value and justify
anything faster against a use case that needs it.

**Enable read optimization**, and on Siemens enable **High Performance Protocol** — both
reduce packet count rather than data volume, which is what saturates a server carrying
dozens of connections.

---

## Fallbacks specific to this pattern

| Situation | Do this |
|---|---|
| **No Softing server** at the plant | The aggregation path is **closed**. Reach the PLC with a native edge connector instead, or go to rollout preparation. There is no partial version |
| Softing server present but **no IIoT Edge Platform** | ③ still does not deliver. The server concentrates; the edge is what publishes to MQTT and reaches the MDL. Both are required |
| Server present, **driver licence missing** | Procurement, not configuration. Check whether Suite Extended already covers it |
| **Beckhoff PLC** | No Beckhoff driver exists. Modbus TCP, or a TwinCAT OPC UA / OPC DA server in front. Native ADS is the edge route — and that branch is `TODO` |
| Somebody asks for **NetLink** | Discontinued since 5.38. Use the **Siemens S7** protocol; the Helmholz NetLink *hardware* is still fine |
| **PLC program unavailable** | The breakpoint applies here too — see [`fallbacks.md`](fallbacks.md) §1 |
| PLC has **no Ethernet interface** | Helmholz NetLink or equivalent gateway, addressed as Siemens S7 |
| **Connection Test fails** | Siemens → rack/slot, RFC1006 header, TSAP cross-match. Rockwell → timeouts and port. OPC UA → certificate trust, and for reverse connections a free listener port. **Do not start defining tags** |
| Connection up, **tags empty or wrong** | Symbol file mismatch — re-export from the **deployed** program version, not an archived project |
| CLX reports **"datapoint not available"** after a restart | Enable *wait for ControlLogix browsing to finish* |
| **Delete refused** on a data source | A datapoint from its address space is still used by a processing function or data target |
| Data lost during **network outages** | Store and Forward. OPC UA S&F needs **Suite Extended** |
| Server **degrading** as machines are added | Cyclic-read intervals up to the guidance values, read optimization on, High Performance Protocol on, tag browsing off. Only then a second server — or split into more configurations (100 max, 50 concurrent) |
| S7-1200/1500 dropping **roughly hourly** | Security connection timeout vs the controller's monitoring interval. Lower it |
| Machine is a **camera** | Not connectable to any aggregation server. Edge only |
