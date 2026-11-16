---
name: mi-equipment
description: >-
  Assess and connect machines to the platform: plan a wave, route a machine to IIoT Edge or dataFEED, clear gates, triage a machine that will not connect. Not for acceptance (deploy-acceptance).
license: MIT
metadata:
  id: mi-equipment
  aliases: [od-equipment-integration]   # former name (naming convention, 2026-11-11)
  tier: technical
  lane: [lane-1, lane-3]
  new_state_lane: "Lane 1b (1b3), Lane 3b (3b4, 3b5)"
  new_state_step: "Order and connect; Cyber Security sign-off in parallel; Connector design and data pipeline (edge to data platform); Procure and connect; Cyber Security sign-off in parallel; execution supplier-dependent"
  department_names: ["mi-connector", "mi-roadmap", "mi-readiness", "connector-design"]
  owner_role: IIoT Interface & Automation Engineer (IIAE)
  tags: [information-integration-service, technical]
  authority_level: draft on assessments and roadmaps; recommend a route and a configuration; never connect, never approve an external connection
  status: stable
  requires: [dept-context]
  composes: [mi-signals, deploy-acceptance, dept-decision-rights, mi-flow]
  okf:
    type: Agent Skill
    title: Equipment integration — assessment and guidance
    tags: [information-integration-service, technical]
---

# Equipment integration

- Read `dept-context` first.
- Two entry routes to one protocol: **Route A - Assessment** (a plant or wave) and **Route B - Guidance** (one machine).
- Serves process steps **1b3** (order and connect), **3b4** (connector and pipeline), **3b5** (procure and connect).
- Key user: IIoT Interface & Automation Engineer (IIAE), in tandem with Plant ME / Plant IT.
- AI agent: drafts and recommends only.
- Where the guide's `rules.json` and this skill disagree, `rules.json` wins (the maintained artefact).
- Detail behind every rule below: [`routing-detail.md`](references/routing-detail.md).

## Purpose

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.
- Use this skill to decide how machines get connected: per plant or wave (Route A) and per machine (Route B).
- It returns a route, a connector, a sequence position and a record of barriers, never a connection made by an agent.

## Inputs and output

| Route | Needs | From | Output (fill as the work happens) |
|---|---|---|---|
| Plant level, before either | Plant row from the records, flags, plant-only questions | Machine List, Tool Overview | [`plant-readiness-brief.md`](assets/plant-readiness-brief.md) |
| **A** | Machine List export for the plant, accepted or planned use cases, roadmap, readiness matrix | `dept-context`, `mi-data-availability` | [`assessment-protocol.md`](assets/assessment-protocol.md): one per plant/wave, machine table, sign-off |
| **B** | A Route A inventory row for the machine | Route A | [`guidance-protocol.md`](assets/guidance-protocol.md): one per machine, gates in order, handoff to `deploy-acceptance` |

- Choose: no assessment yet for this plant or wave -> A.
- Assessment done, one machine needs route, connector, configuration -> B.
- B without an A inventory: start at A, do not guess scope.

## Procedure - Route A (assessment)

1. **Inventory** the plant's machines against the Machine List (vendor, PLC model, part number, protocol, criticality, status). Count live; `NOT INTEGRATED` is not a backlog of failures, a blank status is a data gap.
2. **Filter by demand**: only machines an accepted or planned use case needs. No use case, no integration.
3. **Classify the barrier tier** per machine - [`barrier-classes.md`](references/barrier-classes.md) (practitioner ranking differs from raw integration rates).
4. **Route each machine** through the Route B gates for concept and connector; log a barrier where no route exists.
5. **Sequence the wave** against roadmap and readiness matrix: strategic plants first, then red capabilities; wave allocation by request order with first-mover capacity.
6. **Size the investment** and take it through integration investment planning (`execute-with-approval`, Tandem with Plant ME / Plant IT).
7. **Start Cyber Security decoupled and in parallel**; track controller patch status and sign-off scope on the wave plan. It blocks only go-live, not planning or build; open patches delayed a wave in practice ([`process-chain-practice.md`](references/process-chain-practice.md)).
8. Hand to execution, then `mi-signals`, then `deploy-acceptance`.

- Targets: look up the current integration target and actual in the department KPI and roadmap status (owner: OD lead), state the date, never plan from remembered numbers.

## Procedure - Route B (guidance, one machine)

1. **Gate 0 - what is installed at this plant?** Decides which patterns exist ([`decision-paths.md`](references/decision-paths.md)).
2. **Cheap question first: is the machine already on an OPC-UA server?** Yes -> variant 3, bridge `DTQ-OPCUA-Connector`, no PLC program or cabinet work. Largest cost difference in the guide.
3. **Gate 1 - variant** for this PLC family: 1 edge device, 2 connector without device, 3 via aggregation server. A per-machine decision, not vendor or plant policy (comparison table in `routing-detail.md`).
4. **Gate 2 - connector** (edge) or **data source driver** (aggregation). Check it exists and is usable first (see Pitfalls).
5. **Walk the pattern**: [`softing-datafeed.md`](references/softing-datafeed.md) or [`iiot-edge-platform.md`](references/iiot-edge-platform.md).
6. **Gate 3 - clear preparation blocks in order**: budget, infrastructure, **PLC program**, tags, cyber security.
7. **Blocked?** Work [`fallbacks.md`](references/fallbacks.md) before recording it as blocked.
8. **Gate 4 - record**: Machine List, Machine CV (mandatory vs optional tags), Edge Device List, inform MPEE OD. `INTEGRATED` only after `deploy-acceptance` passes.

- Short example of a Route B record (fictional example; the machine and plant are invented):

```text
Machine: M-017 (fictional), PLC family from the Machine List row (dated)
Gate 0: edge platform installed   Gate 1: variant 3 (already on an OPC-UA server)
Gate 2: DTQ-OPCUA-Connector, available   Gate 3: PLC program present, cyber security open -> waits for go-live
Handoff: deploy-acceptance; INTEGRATED only after it passes
```

- If a gate would fail or a guide branch is `TODO`, do not compose a route: use the fallbacks or escalate as stated in the rules below.

## Decision rules

- **No PLC program -> "we CAN NOT connect the PLC!"** Raise at the first conversation; work the seven non-PLC rungs in `fallbacks.md` section 1 before declaring blocked.
- **Variant 3 needs the IIoT Edge Platform behind the Softing server**; without it nothing reaches the data platform.
- **Variant 2 has no written route** -> IIAE conversation, never a standard option.
- **Both 1 and 3 available at a plant** -> choose per machine; driver gaps decide (Beckhoff: edge connector, no Softing driver; Modbus: Softing driver, unwritten edge branch). Cameras: variant 1 only.
- **No route exists** -> log the barrier in the landscape module and escalate into the roadmap; never a silent omission from the wave.
- **Guide branch is `TODO`** -> say which branch is unwritten; take the other platform's route if written, else escalate to the IIAE. Never compose a procedure.
- **Cyber Security sign-off missing** -> machine waits to go-live; no expedited path. External connection: confirm the gate before scheduling.
- **No operations concept for the target system** (MSB / data platform) -> escalate to strategy as a tool-rollout decision.
- **Approved edge device sizes**: re-confirm with the IIAE before sizing a wave (small/medium may not exist).
- Overlapping ladders: apply the stricter route.

## Lane 3b order and the absorbed modes

- The department's Lane 3b runs: connector design → data-pipeline design (edge to the data platform) → Cyber Security sign-off → procurement and hardware → integration execution → acceptance test, live on the data platform.
- Cyber Security runs **in parallel** with planning and build and blocks go-live, not the start (owner decision, 2026-11-06; `references/process-chain-practice.md`).
- **Integration execution is supplier-dependent and not covered by any OD skill**: the department records it as a gap waiting on a supplier decision (the App-Store-Ops feature request).
- Record the wait, do not plan around it.

| Mode | Absorbed procedure | Use when |
|---|---|---|
| Wave plan | [`references/od-machine-integration-plan/procedure.md`](references/od-machine-integration-plan/procedure.md) | A wave goes from the machine list to flow design: known types first, route per machine type, readiness, barrier log, workshop preparation |
| Barrier triage | [`references/od-barrier-triage/procedure.md`](references/od-barrier-triage/procedure.md) | A machine will not connect: classify the barrier and route it to the roadmap, strategy or a substitution path |
| Former lane | [`references/od-information-integration-service/procedure.md`](references/od-information-integration-service/procedure.md) | You need the old Information Integration lane's tool fact sheets, roles and support model, finding decks or lane handoffs |

## Handoff

- Route A -> Route B per machine in the wave.
- Route B -> `mi-signals` (tag list, PLC program version, Machine CV), then `deploy-acceptance`; `mi-flow` for the pipeline; `dept-decision-rights` for investment approval.
- Receiver needs: concept, connector, sequence position, logged barriers, Cyber Security status.

## Human gate and AI-agent notes

- **Agent may**: inventory, filter, classify barriers, draft the protocol, recommend route and configuration; cite the Machine List row (dated), the `rules.json` branch, reference file and manual page.
- **Only a human** connects a machine or approves an external connection (`execute-with-approval`, Tandem with Plant ME / Plant IT, Cyber Security / OT sign-off first). Only a human changes a signal or data-model standard (Consultation).
- Never enable **Write Permission** on an aggregation-server data source unless a use case writes to the PLC; read-only is the default.
- Never structure tags to the PLC layout; use the agreed data model (recorded as *CT Base*).
- Never mark `INTEGRATED` before acceptance passes, never claim a readiness dimension "Available" without evidence, never record a machine integrated without a barrier-tier judgement.

## Definition of done

- **A**: inventory and roadmap agreed with Plant ME / Plant IT; each machine in scope carries concept, connector and sequence position; barriers logged; investment planned; Cyber Security gate identified.
- **B**: Machine List, Machine CV and Edge Device List updated; MPEE OD informed; `INTEGRATED` only after `deploy-acceptance`.

## Pitfalls

- **An unavailable native connector is not an unreachable PLC.** `DTQ-B&R-Connector` and `DTQ-Bachmann-Connector` do not exist (`Idea`); those machines go over OPC UA via the aggregation server.
   - `SFT-SIMATIC S7-Connector` is `DO NOT USE` (no Cyber Security compliant communication); use `DTQ-S7-Connector`.
   - `DTQ-OPCUA-Connector` is the standing fallback; on the bridge path the Machine List row names both connectors.
- **OESL guidance errors**: dataFEED V5.70 has no Beckhoff data source or ADS (use Modbus TCP or TwinCAT OPC UA; no fully written Beckhoff route on either platform); NetLink is discontinued (address a Helmholz gateway with the Siemens S7 protocol).
   - Source of truth is `rules.json`; the fix is there.
- Softing drivers with no OESL route (FANUC, ODBC, MQTT, file read, OPC Classic, S5): put to the IIAE. Each PLC family needs its own licence unless Suite Extended; check licensed concurrent configurations.
- Empty Machine List fields (`production_criticality`, `cyber_security_status`, `machine_blockers`, `input_protocol`) are not values.
- The common recorded blockers (data-model standardization, firmware patching, TIA V16->V17, cyber-security vulnerability) are mostly not connectivity problems.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`routing-detail.md`](references/routing-detail.md) | Terminology, the three variants and comparison table, estate status vocabulary, connector traps, OESL errors, live constraints |
| [`decision-paths.md`](references/decision-paths.md) | The four gates, PLC family -> routes, where a path dead-ends |
| [`barrier-classes.md`](references/barrier-classes.md) | Barrier tier ranking, Modbus/aggregation question, pre-assessment tells, blocker root causes |
| [`connectors.md`](references/connectors.md) | What each connector reaches and whether it is available |
| [`connector-fact-sheets.md`](references/connector-fact-sheets.md) | Signal limits, sampling rates, file and camera endpoints, build estimates |
| [`vendor-protocol-routes.md`](references/vendor-protocol-routes.md) | Route per vendor, PLC model and protocol; combinations with no route |
| [`softing-datafeed.md`](references/softing-datafeed.md) | Aggregation Server pattern, driver list, licensing, per-driver settings |
| [`softing-tag-syntax.md`](references/softing-tag-syntax.md) | Tag identifier syntax per family |
| [`softing-data-targets.md`](references/softing-data-targets.md) | How data leaves dataFEED: OPC UA path, Store and Forward, MQTT |
| [`iiot-edge-platform.md`](references/iiot-edge-platform.md) | Edge pattern: six phases, hardware sequence, sizing, non-PLC endpoints |
| [`fallbacks.md`](references/fallbacks.md) | Before recording a machine as blocked |
| [`plant-integration-status.md`](references/plant-integration-status.md) | Building a plant-by-plant status view from the Machine List and Tool Overview |
| [`process-chain-practice.md`](references/process-chain-practice.md) | Weekly capital-request micro-process, Cyber Security as parallel gate, planning workflow, data classes, lessons |
| [`blockers-and-waves.md`](references/blockers-and-waves.md) | Kinds of recorded blocker, projects and waves, eCR step, roadmap figures (staging, unverified) |
| [`references/background.md`](references/background.md) | Context, rationale, examples and notes moved out of this file; never an instruction |
| [`references/od-barrier-triage/assets/barrier-triage-record.md`](references/od-barrier-triage/assets/barrier-triage-record.md) | The record of one blocked machine - facts, demand, ladder result, root-cause class, difficulty tier, exit, owner, wait state and the log line. |
| [`references/od-barrier-triage/references/classes-and-routes.md`](references/od-barrier-triage/references/classes-and-routes.md) | The seven root-cause classes of a machine that will not connect, the question that tells them apart, and for each the exit (roadmap, strategy, substitution), owner, forum and wait state. |
| [`references/od-barrier-triage/references/estate-patterns.md`](references/od-barrier-triage/references/estate-patterns.md) | How to read the Machine List for barrier patterns - where NOT INTEGRATED clusters by vendor, protocol and plant, how to group recorded blocker texts by class, and the data… |
| [`references/od-barrier-triage/references/process-chain-practice.md`](references/od-barrier-triage/references/process-chain-practice.md) | Recurring blocker patterns from the decks mapped onto the seven barrier classes, the ownership signals that show a stuck case early, the blocker one-pager, barrier reporting with cost of non-decision,… |
| [`references/od-information-integration-service/assets/plant-status-input.md`](references/od-information-integration-service/assets/plant-status-input.md) | One-page input a plant fills for the equipment-integration line of a status request - the plant's numbers with sources and dates, the open blockers, the capital request (eCR) state and… |
| [`references/od-information-integration-service/references/finding-decks.md`](references/od-information-integration-service/references/finding-decks.md) | How to find which archive deck holds what for the integration lane - the Slide Index and how to search it, and a topic-to-deck map for machine integration workshops, initiatives,… |
| [`references/od-information-integration-service/references/lane-handoffs.md`](references/od-information-integration-service/references/lane-handoffs.md) | Each happy-path step matched to the real, current asset the composed skill now produces, confirmed against each skill's actual state rather than assumed from its name. |
| [`references/od-information-integration-service/references/process-chain-practice.md`](references/od-information-integration-service/references/process-chain-practice.md) | How the Information Integration lane runs its rhythm in the AI-driven chain - wave cadence and status, the community call pack, plant tiering, integration workshop, hand-over to use-case support, recurring… |
| [`references/od-information-integration-service/references/roles-and-support-model.md`](references/od-information-integration-service/references/roles-and-support-model.md) | Who does what around the IIoT edge and manufacturing suite at a plant according to the operations concept deck - local key user, business-area key user, governance board, central key… |
| [`references/od-information-integration-service/references/task-chain-and-tool-use.md`](references/od-information-integration-service/references/task-chain-and-tool-use.md) | The integration lane's recurring tasks as a trigger chain with tool access rationale, the signal-standardization rule, the readiness matrix and source-catalogue traps, and metric hooks. |
| [`references/od-information-integration-service/references/tool-fact-sheets.md`](references/od-information-integration-service/references/tool-fact-sheets.md) | Guidance for answering "what is it, where is it, what does it need" for each shop-floor tool in the Tool Overview - what each tool is for, which records to… |
| [`references/od-machine-integration-plan/assets/wave-plan-template.md`](references/od-machine-integration-plan/assets/wave-plan-template.md) | Template for one integration wave - machine list and CV fields, machine type and route, cost line, plant status row, readiness check and barrier log; fill with placeholders, never with… |
| [`references/od-machine-integration-plan/assets/workshop-prep-checklist.md`](references/od-machine-integration-plan/assets/workshop-prep-checklist.md) | Preparation checklist for an equipment-integration workshop at a plant - inputs, IT and physical access, attendees, agenda order and outputs; to be completed before the visit. |
| [`references/od-machine-integration-plan/references/barrier-log-and-cost-of-non-decision.md`](references/od-machine-integration-plan/references/barrier-log-and-cost-of-non-decision.md) | The wave's barrier log - fields, how it relates to barrier triage, how to state the cost of non-decision, the rapid decision board and the error-log review - process guidance,… |
| [`references/od-machine-integration-plan/references/route-choice-per-machine-type.md`](references/od-machine-integration-plan/references/route-choice-per-machine-type.md) | How to choose the connector and route for each machine type in a wave - data classes, when an edge device is needed, the low-cost address-translation pattern, legacy and camera… |
| [`references/od-machine-integration-plan/references/wave-planning-and-readiness.md`](references/od-machine-integration-plan/references/wave-planning-and-readiness.md) | The scale-known-types rule, wave allocation, the weekly capital-request micro-process, status taxonomy, phase sequence from machine list to flow design, and readiness criteria - process guidance, no figures. |
