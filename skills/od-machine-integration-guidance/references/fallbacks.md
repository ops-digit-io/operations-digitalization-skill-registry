# Fallbacks — when the path is blocked

A blocked integration is usually blocked at one of eight places. For each: what it actually
means, what to try before declaring it blocked, and when to stop trying.

The rule underneath all of them: **a recorded blocker is steering information, not a
failure to hide.** Blocking points say why value is not flowing. Record it against the
machine, name its owner, and move on to the next machine — do not quietly leave it out of
the wave.

---

## 1. The PLC program is unavailable ★

The breakpoint. It closes both platform routes for a PLC data source, and it is the most
common reason a machine stays unconnected.

> *"In case you do not have the PLC program or you did not request the PLC program / you
> did not receive the PLC program, we CAN NOT connect the PLC!"*

**Before declaring it blocked, work down this list.** Each rung avoids the PLC entirely:

| # | Try | Why it works |
|---|---|---|
| 1 | **Is the machine already on an OPC-UA server?** | No program, no tag export, no cabinet work. The cheapest path in the guide |
| 2 | **Is there a vendor-specific connector?** Engel, Piovan, Keyence, Zwick, Optris, Multicon | Reaches the vendor's own interface, not the PLC |
| 3 | **Does the machine write a file?** FTP or SMB drop, CSV/log export | `DTQ-FTP2MIL-Connector`, `DTQ-SMB-Connector` — no program |
| 4 | **Does it expose HTTP / SOAP / a web service?** | `DTQ-Multicon CMC131-Connector` (HTTP(S)), `DTQ-PIOVAN-Connector` (SOAP) |
| 5 | **Is there a serial interface?** | `DTQ-RS232-Connector` |
| 6 | **Is the needed signal available on a *neighbouring* PLC?** | The estate records exactly this for robot signals — 5 machines. The line PLC may already read what the machine will not give up |
| 7 | **Can a sensor be added instead of reading the machine?** | A remote sensor or camera is a supported endpoint class and needs no program at all |

**Then, and only then:** request the program from the machine supplier and record the
machine as blocked pending it. Start the request the same day — the lead time is weeks and
sometimes a commercial negotiation, and it is the single most valuable thing to have
started early.

**What not to do:** do not read the PLC by guessing addresses, and do not treat a partial
program as sufficient. The requirement is the **entire** program, including the `.S7P` for
Siemens, because the tag export is derived from it.

**Prevention:** the *order a new machine* branch exists for exactly this. The
*Electrical Standard — Equipment Integration Extension* in Compliance Quest is what stops
the next machine arriving in the same state. Specifying connectivity at purchase is the
cheapest integration there is.

---

## 2. The PLC program exists but nobody can change it

Step 5 of the edge preparation block: *the capability to adjust the PLC program* —
implement the function block, adjust the hardware configuration.

This is a **resourcing and scheduling** block, not an engineering one. It needs a person
with the toolchain and a maintenance window on a production line.

- **Try:** schedule against a planned line stop rather than requesting one.
- **Try:** the aggregation route — a read-only Softing data source may need no program
  change, only the symbol file.
- **Escalate as:** a capability gap, per the department's own record of it (signal
  standardization and edge integration are named skill gaps against IIAE capacity).

Do not record this as "PLC program unavailable". They are different blockers with different
owners and conflating them hides the real one.

---

## 3. The target platform is not installed at the plant

**No Softing server** → the aggregation route is closed outright. There is no partial
version and no workaround at machine level.

**No IIoT Edge Platform and no edge device** → the edge-device hardware branch comes first;
it is a prerequisite, not a step of the integration.

**Neither** → this is not an integration question at all. Take the *nothing standard
installed* branch:

1. Check the **Plant Capabilities & System Availability & Rollout** list.
2. If the plant is not on it, contact MPEE Operations Digitalization.
3. Come to that conversation with: the **urgent need and the use case**, a **Machine List**,
   a **Use Case List**, and **calculated benefits and savings**.

That last item is the one people arrive without, and it is the one that decides the
outcome. A rollout request without a business case is refused at intake — see
`od-use-case-intake-triage`.

**Related, and more common than it looks:** *not sure* what is installed. Same list, then a
≤30 min call, plus the training offer if the systems themselves are unfamiliar. Guessing
here wastes a whole planning cycle.

---

## 4. Cyber security has not signed off

The machine waits. **There is no expedited path** and no authority level in the department
that shortens it.

- External connections need **Cyber Security / OT sign-off** before scheduling, not after.
- Endpoints must be connected per the **OT cyber-security rules** in the Connext Wiki.
- The estate records this as a real blocker in two shapes: *firmware patching required for
  cyber security* (13 machines) and *vulnerability, patch before integration* (5).

**Try:** bundle the sign-off with the wave rather than requesting it per machine — that is
the department's own strategy bet (Cyber Security bundled with the MSB rollout at strategic
plants). A wave-level approval is one conversation; twenty machine-level ones are twenty.

**Never:** connect anyway and record it afterwards.

---

## 5. No route exists for this PLC

The machine's protocol is not in the connector set and not in the decision tree.

Take the *Integration of Other PLCs* path:

1. Machine details in the **Machine List**.
2. **PLC details** — name, type, vendor with contact details, interfaces.
3. **Inform MPEE Operations Digitalization.**

Then set expectations honestly, because this path is long:

- It may require **connector development and deployment**.
- It carries **high lead times for OT and IT cyber-security approvals**.
- The guide asks you to name **which use cases depend** on this PLC — that is what decides
  whether a connector gets built. A custom connector for a machine with no waiting use case
  will not be prioritised, and should not be.

**Before taking it:** re-run the seven rungs in §1. A great many "no route" machines are
file-drop or vendor-interface machines that nobody checked for.

---

## 6. The guide's own branch is unwritten

Three recommendation bodies in the live tree are literally `TODO`:

| Branch | Status |
|---|---|
| Beckhoff on the **edge** | `TODO` — but the **aggregation** route is fully written. Use it |
| Modbus on the **edge** | `TODO` — but the **aggregation** route is fully written. Use it |
| OPC-UA server on the **aggregation server** | `TODO` in `rules.json`; **fully written in `rules-next.json`** |

Plus B&R INA2000 on aggregation (`TODO!`), and Omron NJ on edge (a task stub with no
procedure).

**Do not compose a procedure for an unwritten branch.** Say which branch is unwritten, and
either take the written route on the other platform — which is available for Beckhoff and
Modbus, and is the real answer for both — or put it to the IIAE.

Where `rules-next.json` has the procedure and `rules.json` does not, that is worth saying
out loud: the guidance exists, it is just not live yet.

---

## 7. Softing has a driver but OESL has no route

Softing's published capabilities cover more than the OESL tree routes — **Siemens S5**,
**FANUC CNC**, **Mitsubishi beyond Melsec-Q**, and file/database sources (XML, TXT, CSV,
ODBC, MongoDB, CouchDB, InfluxDB).

**A product capability is not an approved route.** The constraint is the OESL standard, not
the product. If one of these would solve a machine:

1. Put it to the IIAE with the machine and the dependent use case.
2. If adopted, it becomes a change to `rules.json` — the tree is data, that is the point.
3. Do **not** configure it on the server because the product allows it. An undocumented
   data source on a shared aggregation server is a support burden nobody agreed to.

`rules-next.json` already adds an `siemens_s5` question, so that gap at least is known.

---

## 8. Connected, but nothing arrives

The integration "worked" and there is no data. In order of likelihood:

| Symptom | Check |
|---|---|
| Edge device healthy in the cabinet, nothing in the platform | **Dashboard registration** and **DATATRONiQ cluster membership** — steps 6 and 9 of the hardware sequence |
| Softing connection green, tags empty or wrong | **Symbol file mismatch** — re-export from the *deployed* program version, not an archived project |
| Siemens connection refuses | **Rack / slot** and the **RFC1006 header** |
| Beckhoff connection refuses despite correct IP | **AMS route** missing on the PLC side |
| Modbus values present but nonsense | **No conversion** — raw counts were never scaled to engineering units. Modbus has no type system and will not complain |
| Values arrive but no use case can compare them across plants | **Tags were structured to the PLC layout, not to a data model.** `Data model standardization (CT Base)` is the estate's most-recorded blocker at 23 machines |
| Aggregation server degrading as machines are added | **Cyclic read intervals** below the guidance values; **read optimization** off |

**A connection that comes up and carries nothing is worse than one that refuses**, because
it looks finished. That is why the Connection Test comes before tag definition, and why the
acceptance test walks the full path — machine → connector → concept → pipeline → MDL → the
asset the plant opens — rather than stopping at the server. See `od-acceptance-test`.

---

## What is never a fallback

- Connecting without Cyber Security / OT sign-off.
- Marking a machine `INTEGRATED` before its acceptance test passes.
- Marking a readiness dimension "Available" without evidence.
- Changing a signal or data-model standard to make one machine easier — that is a
  Consultation decision with ContiTech central, and interface compatibility is a standing
  constraint.
- Inventing a procedure for a `TODO` branch.
- Adding a tool to the footprint. Broad tool proliferation is an explicit non-bet.
