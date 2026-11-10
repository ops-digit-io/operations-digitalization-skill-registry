---
type: Skill Reference
title: Classes and routes
description: The seven root-cause classes of a machine that will not connect, the question that tells them apart, and for each the exit (roadmap, strategy, substitution), owner, forum and wait state.
resource: ../procedure.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Classes and routes

The class list groups what `mi-connector` already records: the eight blocking places in
[`fallbacks`](../../fallbacks.md), the named-blocker root causes in
[`barrier-classes`](../../barrier-classes.md) and the lane's three
error paths. The grouping is this skill's proposal; the OD lead has not confirmed it. Each machine gets
**one** class (the one that is binding now); name a second only as "behind it".

## The three exits

| Exit | Meaning | Where it goes |
|---|---|---|
| **Roadmap** | The barrier is known and can clear; the machine keeps a sequence position behind it | Assessment protocol section 5 "barriers logged" (`mi-connector`); lane playbook error path "log barrier in landscape module; escalate to roadmap" |
| **Strategy** | A decision above the machine is needed | OD lead: the playbook error path "operations concept for target system missing: escalate to strategy (tool rollout decision)". `od-decision-routing`: the OD lead and the deciding role named in the current approval policy (look up) for strategy, priority, rollout and blocked projects; COP for technical matters such as connection barriers and missing operations concepts |
| **Substitution** | Reach the data another way, or replace what cannot connect | Fallback ladder, `mi-connector` Route B; paid options through `bc-cost` |

## The seven classes

| # | Class | The question that identifies it | Typical evidence | Exit | Owner (role) | Wait state |
|---|---|---|---|---|---|---|
| C1 | **Information missing** | Do we hold the entire PLC program, the tag export, the documentation? | "PLC program missing"; "no source code provided"; wiring or configuration lost; the PLC is a black box only the OEM touches | Roadmap, after the ladder; substitution if a rung hits | IIAE with Plant ME | Awaiting the program from the machine supplier. Start the request the same day: lead time is weeks, sometimes a commercial negotiation (`fallbacks` item 1) |
| C2 | **Owner, window or will missing** | Is there someone with the toolchain, a maintenance window and a commitment to change the PLC or patch it? | Program exists but nobody can change it; no owner or scheduled OT window for a patch; Plant IT/OT unwilling or unable to commit | Roadmap; if the root cause is capacity, escalate as a capability gap | Plant ME / Plant IT; OD lead for capability gaps | Awaiting a planned line stop. Do not record as C1 (`fallbacks` item 2) |
| C3 | **Security gate** | Has Cyber Security / OT signed off the connection? | Sign-off missing; firmware patch required; vulnerability to patch before integration | Roadmap (hold) | Plant IT/OT with Cyber Security; `od-cybersec-gate` | Awaiting Cyber Security / OT sign-off. "There is no expedited path"; the sign-off runs in parallel and blocks only go-live, not planning or build: start the package early and bundle it with the wave instead of per machine (`fallbacks` item 4). Never connect first (go-live) |
| C4 | **Platform missing** | Is the target platform installed here (IIoT Edge Platform, Softing server) and is there an operations concept for the system that receives the data (MSB, data platform)? | No edge platform; edge platform but no edge device on site; no Softing server for variant 3; operations concept missing | Strategy | OD lead (tool rollout decision, counterpart `⟨to confirm⟩`) | Awaiting the rollout decision. The machine "can be connected and still have nowhere to send data" (`mi-connector`, error paths) |
| C5 | **No route** | Is the machine's protocol in the connector set and the decision tree, and is its branch written? | Protocol outside the connector set; branch is `TODO` in the guide (Beckhoff and Modbus on the edge, B&R INA2000 on aggregation, Omron NJ on edge); the OESL text names a menu item the product lacks (Beckhoff, NetLink) | Substitution (take the written route on the other platform; re-run the ladder); Strategy if only a connector development fixes it for use cases that wait | IIAE; OD lead if connector development | Awaiting connector development, with "high lead times for OT and IT cyber-security approvals". Name the dependent use cases: they decide whether a connector gets built |
| C6 | **Legacy hardware limit** | Can the hardware ever speak a supported protocol or be patched? | Serial-only PLC without Ethernet; no native security; cannot be patched without a generation upgrade; vendor gone or platform unsupported (the recorded answer in that case: buy a new machine) | Substitution: gateway (a Helmholz NetLink gateway addressed with the Siemens S7 protocol is the recorded example), sensor or camera instead of the PLC, retrofit, or replacement; a capital decision | Plant ME with IIAE; OD lead for the capital step | Awaiting the investment decision (`bc-cost`) |
| C7 | **Data model, not connection** | Does the connection carry data that no use case can compare across plants? | "Data model standardization (CT Base)"; tags structured to the PLC layout, not a data model | Not a connection barrier: hand to `od-signal-standardization` | IIAE (Consultation with a counterpart `⟨to confirm⟩`) | Awaiting a decision on signal or data-model standards |

Decision rule when two classes apply: the one that is cheapest to clear does not decide; the one that
**blocks first** does, in the order of the preparation gates in `decision-paths` (budget, infrastructure,
PLC program, tags, cyber security). Note it as "behind it" for the next triage.

## Substitution options, by what they cost the plant

| Option | Source | Cost signal |
|---|---|---|
| Machine already on an OPC-UA server; vendor connector; file drop (FTP, SMB); HTTP or SOAP interface; serial interface | `fallbacks` item 1, rungs 1 to 5 | No PLC program needed; connector availability per `connectors` (some listed connectors cannot be used; check the connector notes) |
| Signal from a neighbouring PLC (recorded for robot signals) | rung 6; recorded for robot signals ("robot signals might be available within the related machine / PLC") | No new hardware |
| Remote sensor or camera | rung 7 | Cost depends on PLC vendor, sensor type and edge needs; an internal proposal exists (`Sensor-Upgrade Decision Frame` business case): look up its current cost frame there |
| Protocol gateway in front of a PLC without Ethernet | `fallbacks` item 7 | OT hardware; cost `⟨look up with Plant ME / vendor quote⟩` |
| Replace the PLC or machine | `barrier-classes`; `PLC Evergreening` business case (a proposal; read its current cost and approval state in the business-case note) | A capital decision; goes to `bc-cost` |

## Routing checks before the exit is final

- A substitution that adds a tool to the footprint is a system-fit question (`invest-screen`):
  "no broad tool proliferation" is a strategy non-bet.
- A substitution that opens an external connection needs Cyber Security / OT sign-off before scheduling.
- A strategy exit is a decision request (`od-decision-routing`), not an e-mail; record the gate as a
  dependency on the use case or saving row.
- A roadmap exit needs a named owner and a date to look again; "waiting" without both is how a machine
  disappears from a wave.
