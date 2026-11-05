---
type: Skill Reference
title: Process chain practice
description: How equipment integration is run as a chain step (1b3, 3b4, 3b5) - the wave and its weekly capital-request micro-process with Cyber Security as a parallel go-live gate, the per-plant planning workflow, data classes with default hub and leading system, energy-monitoring and MES lessons, handoffs and agent notes.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, technical, process-chain, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - integration wave, planning workflow and lessons

Derived from the Operations Digitalization slide decks (integration, energy-monitoring, MES, edge-platform and community-call
decks), abstracted into process guidance. No figures. `PROPOSAL` = synthesis not stated in a deck; `<...>` = unknown or to
confirm. Connector, route and gate detail stays in the neighbouring references; this file adds how the work is run.

## Where it sits in the chain

1b3 order and connect (standardized system), 3b4 connector and pipeline, 3b5 procure and connect. Upstream: 33 / 1b2 capital
decision and the Cyber Security gate. Downstream: `od-signal-standardization`, `od-acceptance-test`.

## 1 Method in practice

### The wave and its weekly micro-process

Machine integration is delivered in **waves**, planned by quarter per plant. A wave bundles the systems the plant needs (service
bus, edge platform, central aggregation server, machine connectivity) and the machine list. The capital request (eCR) is
milestone one of each wave. Per plant the same three steps repeat, shifted by one calendar week from plant to plant:

1. call with the local OT expert,
2. prepare the capital request with the local expert,
3. upload with the local team, then close-loop communication until approval.

Status per plant is a traffic light with a call-for-action cell: red = phase delayed, yellow = close-loop update required,
green = on track. Use one traffic-light scale per round; "input collected", "delayed" or "at risk" may appear only as reason text in the comment.

**Cyber Security runs decoupled and in parallel; it gates go-live only.** Patches on controllers and open approvals delayed the second
wave and the savings behind it, so start the sign-off package early. Put the controller patch status and the sign-off scope (wave-level
where one exists, see `od-cybersec-gate`) on the wave plan and keep the track running alongside planning and build. The gate blocks
only the live connection and live operation; planning, build and the wave's preparation go on, and nothing goes live without sign-off.

### Wave decision rules

- **Budget class** follows the systems needed (small, medium, large). Eligibility follows request order;
  central capacity goes first to first-mover plants that are staffed (key user, capacity, coverage). State the rule used on the plan.
  First-mover status is not eligibility, only capacity.
- **Staffing check in the wave decision.** A connectivity budget is approved but the plant lacks resources or skill: include
  the plant's resource rating before the wave is committed.
- **Connect whole processes or areas at once** and reuse existing infrastructure as far as possible.
- **Scale known machine types.** An approach of connecting the ten hardest machines first and leaving the easy ones to plants
  burned reputation and killed the local project. Rule: at most one unknown machine type per new deployment, document the
  procedure per controller type, write the integration standard.
- **Layout stability.** Machines that are relocated repeatedly delay integration; check the area layout before committing.
- **Low-cost pattern.** Where data frequency is low, reuse an existing edge device and translate addresses on a switch so PLC and
  HMI addresses and programs stay unchanged: one switch configuration instead of per-device changes. Trial one device on one
  machine before ordering more. Not for high-frequency signals.
- More integrated machines do not equal more savings. A plant with many connected machines and no pull from Production produced
  none. Ask for the use-case demand and the plant owner before sizing (this sharpens Route A step 2).

### Per-plant planning workflow (tool-shop model)

Sequence for each rollout plant:

- machine list from the template,
- machine CV (PLC program, version history, vendor),
- machine integration guide run per core process,
- integration plan (hardware and software changes per machine),
- rough time and cost planning that feeds the capital request,
- kick-off with the plant,
- initial tag list,
- hardware integration,
- software integration (for example a data block in the PLC),
- flow design to the standard base model on an OPC-UA server.

Roles: the plant provides inputs; the machine-building tool shop is mandatory for own machines and support for third-party
machines; the central integration team leads the flow design; execution in the plant or external is decided in planning. A frame
contract with tool shops is considered only after experience with the first rollouts; the first period executes on fixed-price
positions. Meeting cadence per phase is known (few meetings for guide and plan, many for tag lists and hardware): plan plant
capacity per phase, not per project. Side effects worth recording: it exposes suppliers with poor control over PLC programs
(an insourcing trigger) and builds PLC naming and versioning habit.

### Tag-list decision per machine

Decide four things: transactional signals, streaming signals, what the connected systems need, and what is wanted for analytics
or data-quality loops. Tag selection follows the documented flow per controller family; the plant keeps its latest PLC
programs and tag lists in the central list. Do not structure tags to the PLC layout (guardrail above).

### Data classes: default hub and leading system

| Class | Contains | Default hub | Leading system |
|---|---|---|---|
| Transactional | Events, cycle time, counters, set values, limits, alarms | Service bus with OPC-UA (changes are hard to propagate) | Per object `<...>` |
| Time series | Curves, process values | MQTT stream (changes are easy to propagate) | Not applicable |
| Master data | Recipes, meter structures, asset structure | Received via API by non-leading systems | ERP as single source of truth |

Route per machine: native OPC-UA machine, aggregation server, or edge device; standardized and non-standardized transactional and
time-series data each have their own interface choice. Consumers get **one interface**; vendor-specific naming is normalised in a
mapping layer. The ERP is the master for material, order and product master data; local systems (MES and similar, including recipe and
meter-structure masters held locally) are derived from it and report back. Mark the leading system per object on the plan.

### Edge or not, camera, legacy

- Edge device needed (rather than plain OPC-UA): vision or robot; full traceability expected; high-resolution series from
  process-critical sensors; inline measurement; advanced analytics planned (`od-system-fit-check` practice file).
- Cameras: prefer the edge connector per camera system (cheap, quick) over vendor turnkey adjustments to third-party software;
  route all cameras of a line through one edge device (fewer endpoints, one security surface); extract features on the edge and
  forward features or images only.
- Legacy system with only a non-standard interface (for example SOAP) and no security: build a managed connector in the
  connector framework instead of point-to-point; many plants run the same legacy system, so a connector scales.
- Manual data points where no machine signal exists: a soft HMI into the service bus is an accepted route.
- Hybrid capture: record what the PLC can give, add a standardized manual reason list for what it cannot see.

### Workshop-style integration (preparation checklist)

Integration done during a workshop needs on the IT side: access to jump hosts and servers (internal and external support), firewall
rules in place, platform apps running, physical access to all edge devices including unmounted ones, and a priority list with
the best starting and stopping point. Open topics usually concern operating-system, admin-rights and support gaps on GPU or
vision PCs. Output: updated machine list and baseline, use cases per area, IT preconditions, next steps toward the capital
request, a short block to prepare the handover to use-case support.

## 2 Decision rules at a glance

| Situation | Rule |
|---|---|
| Machine not connected, use case waiting | Integration wave first; use cases only after |
| Old device signals incompatible with the bus or logger | Compatibility check before the cost line, not after |
| Controller patch or sign-off open | Parallel track; hold go-live (the live connection) until signed off |
| Barrier with no route | `od-barrier-triage`; log, never omit silently |
| Lab or quality dashboard not tied to a machine | Not in the integration sequence; local quality team owns |

## 3 Handoff contract

| Direction | Skill | Content |
|---|---|---|
| Receive | `od-capital-request` / `od-investment-input` (1b2, 33) | Approved scope, budget class, machine list, named plant owner |
| Receive | `od-cybersec-gate` | Sign-off scope and conditions, or the wait state |
| Hand on | `od-signal-standardization` | Machine CV with mandatory and optional tags, tag list, base-model flow design |
| Hand on | `od-acceptance-test` | Data path, signal list, witness, expected values |
| Hand on | use-case support (`od-use-case-support-service`) | Machine list with connected status, remaining machines with blocker, integration-to-use-case handover note |
| Hand on | `od-barrier-triage` | Machines with no route, class and dependent use cases |
| Hand on | `od-scorecard-reporting` | Wave status, traffic light, call-for-action |

## 4 Pitfalls and lessons

**Bus-based and energy metering.** Check meter compatibility with the bus, one converter per pulse output, unique bus
addresses, limits per segment or logger. A wireless link between logger and plant network proved unreliable; logger-to-server
communication was fragile. Naming of measure points must be settled up front and master-data entry is laborious (ask for
guided set-up and a pre-configured logger structure). The cost of connecting existing meters is easily underestimated. Cloud
energy tools need office and shop-floor network separation and certificate-based encrypted traffic first.

**Energy rollout method (reusable for any sensor-to-system rollout).** Start team (local IT, engineering, energy supply, central
expert) -> device list with technical data and interfaces plus a location drawing -> hardware check including server ->
hardware, bus and cost planning -> tender documents and capital request -> purchasing after approval -> hardware commissioning,
then software commissioning (server, import connector, watchdog) -> training split admin and user -> database in the backup
routine -> final documentation (lists, cabinet drawings, bus cabling). High consumers first. Standards that made it scale:
mandatory object structure (organisation, location, main counters, cost centre), naming convention for measure points, meters,
series and virtual series, a white list of tested devices, an add-on with standard settings, a shared knowledge site, a user forum.
Run old and new in parallel for a limited time and match the reading date to the billing period; add plausibility checks and
manual correction.

**MES rollouts.** Old HMIs are hard to connect and need an emergency strategy when the system is down; a service contract without
out-of-hours coverage creates supply-security risk; ERP-to-MES interface faults and slow vendor reaction recurred; no "shop-floor IT"
or ERP key user was assigned for the use phase.

**Platform migration across plants.** Check the runtime licence model before moving a virtual server (an OPC-UA server licence can
be bound to one machine; keep the key); confirm DNS, certificates and access carry-over; reserve an outage window per location for
reconfiguring edge devices; one checklist file per location with a traffic light.

**Vulnerability notices.** Response speed is bounded by machine-list completeness; keep the list current.

## 5 Questions to ask and definition of done

- Which machines does an accepted use case need, and who is the named plant owner? Is the layout stable?
- Is the controller patched, is the sign-off package started and in scope of a wave-level approval, is the IT precondition list ready?
- Which data classes does each machine deliver and which system leads each master object?
- Does the plant have the people and skill to run its part of the wave?

Done = hardware and software commissioned, master data set, import and monitoring running, key users trained, backup integrated,
documentation complete, old process switched off, plus the Route A or B definition of done.

## 6 AI agent operating notes

- **Can do**: draft the machine list, the machine CV and a tag-list proposal from a PLC export; check protocol compatibility against
  the connector catalogue; classify data signals into the three classes; build the plant status table with traffic light; list
  machines whose controller patch status is unknown; draft the preparation checklist.
- **Inputs required**: Machine List export (dated), PLC program or tag export, plant tool overview, sign-off scope.
- **Evidence to cite**: the guide step or rule used (`rules.json` is authoritative), the connector catalogue row, the list read date.
- **Human gates**: connecting a machine, approving an external connection, the capital request submission, the wave commitment,
  and the Cyber Security sign-off (all human, no expedited path).
- **Handover**: the protocol of the chosen route, with unknowns as `<...>` and the open-item owner role.
