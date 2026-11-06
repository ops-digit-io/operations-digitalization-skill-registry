---
name: od-barrier-triage
description: >-
  Classify why a machine will not connect (legacy hardware, protocol with no route, missing PLC program,
  platform not installed, Cyber Security wait, data model) and route it to one of three exits - the
  integration roadmap, strategy, or a substitution path - with an owner and a logged barrier, instead of
  leaving the machine silently out of the wave. Builds on the fallback ladder and barrier classes of
  od-equipment-integration. Use when a machine cannot be connected or an assessment finds no route, when
  a blocker text such as "firmware patching required" or "PLC program missing" is recorded, or when
  someone asks whether a stuck machine is a roadmap, strategy or substitution matter.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-barrier-triage
  tier: practice
  lane: information-integration-service
  new_state_lane: Lane 3b (step 4b), Lane 1b
  new_state_step: "Connector design: barrier triage"
  owner_role: human:jakob.gabriel
  authority_level: draft
  status: draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-equipment-integration, od-decision-routing, od-signal-standardization, od-investment-input, od-cybersec-gate, od-information-integration-service, od-data-availability-check, od-system-fit-check]
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/information-integration-service/playbook.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/information-integration-service/agent-brief.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/10-modules/smart-factory-use-case/landscape.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/02-strategy.md
    - Skill od-equipment-integration, its references barrier-classes, fallbacks, decision-paths and connectors, and its assessment protocol, read 2026-11-05
    - Skill od-decision-routing, escalation forums and the risk triggers, read 2026-11-05
    - Work vault bundle file kg_nodes.csv, the Machine records read as an aggregate (status, vendor, protocol, blocker text) and the Connector records, 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Graph/Business Cases notes PLC Evergreening and Sensor-Upgrade Decision Frame, read 2026-11-05
    - New-state flow (docs/new-state-flow.md, VSM skill map), Lane 3b step 4b connector design, read 2026-11-05
  okf:
    type: Agent Skill
    title: Barrier triage
    tags: [information-integration-service, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Barrier triage

Read `od-context` first.

**Plan row II-08** (`OD_Skill_Map.md`): trigger "machine will not connect (legacy / protocol)"; output
"classified barrier + routing (roadmap / strategy / substitution)"; runs at the plant; authority `draft`;
wave 2. Sources named by the plan: the lane's playbook error paths and the `landscape` module.

## Purpose and definition of done

The lane playbook gives one rule for a machine that cannot connect: "log barrier in landscape module;
escalate to roadmap." Two related error paths send other cases elsewhere (Cyber Security sign-off missing:
hold at the wait state; operations concept for the target system missing: escalate to strategy as a tool
rollout decision). This skill turns those three sentences into a decision a plant key user can take in
one sitting.

Done when: the machine's use-case demand is stated; the fallback ladder was run; the barrier has **one
root-cause class** and a **difficulty tier**; it is routed to **roadmap, strategy or substitution** with a
named owner and forum; the barrier is logged (not silently omitted from the wave); and the record is
filed.

## Where it sits

Lane 3b of the new-state flow: *4b connector design* (VSM skill map: `od-equipment-integration`,
`od-signal-standardization`, `od-node-red-flows`); the barrier sits ahead of *5b procure and
connect*. It also serves Lane 1b, where a standardized-system match fails (the plant picked a kit and the
machine will not take it). Assessment (Route A) and guidance (Route B) of `od-equipment-integration` find
the barrier; this skill classifies and routes it.

## References and assets

| File | Use it for |
|---|---|
| [`references/classes-and-routes.md`](references/classes-and-routes.md) | The seven root-cause classes, the questions that tell them apart, and for each the exit, the owner, the forum and the wait state |
| [`references/estate-patterns.md`](references/estate-patterns.md) | How to read the Machine List for barrier patterns: where `NOT INTEGRATED` clusters by vendor, protocol and plant, how to group recorded blocker texts by class, and the data gaps that make triage impossible - guidance and live-count recipes, no figures |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Recurring blocker patterns mapped onto the classes, ownership tells of a stuck case, the blocker one-pager, barrier reporting with cost of non-decision, handoffs, agent notes |
| [`assets/barrier-triage-record.md`](assets/barrier-triage-record.md) | The record: facts, class, tier, exit, owner, log line |

Already in `od-equipment-integration`, not repeated here: the difficulty ranking
([`barrier-classes`](../../skills/od-equipment-integration/references/barrier-classes.md)), the seven-rung ladder for
an unavailable PLC program and the eight blocking places
([`fallbacks`](../../skills/od-equipment-integration/references/fallbacks.md)), the routing gates
([`decision-paths`](../../skills/od-equipment-integration/references/decision-paths.md)) and the connector set
([`connectors`](../../skills/od-equipment-integration/references/connectors.md)).

## Procedure

1. **Facts first.** Fill the Machine List fields (vendor, PLC model, part number, protocol, status) and
   the pre-assessment tells from `barrier-classes` (cabinet and cabling, a usable network drop, Plant IT /
   ME responsiveness, topology, whether the PLC program is available and under own control). Missing
   fields stay `⟨unknown⟩`; many machine records carry no protocol or PLC model, so expect gaps.
2. **Is there a use case waiting?** `NOT INTEGRATED` records a state, not a failure
   (`od-equipment-integration`). No accepted or planned use case needs the data: close the triage as
   "parked, no demand" and stop. Otherwise name the use case.
3. **Run the ladder.** Work through the seven rungs of `fallbacks` item 1 (machine already on an OPC-UA
   server, vendor connector, file drop, HTTP or SOAP, serial, neighbouring PLC, added sensor). A hit is a
   **substitution** exit: go to step 6. Check also that the "barrier" is not an unwritten branch of the
   guide (`fallbacks` item 6) or the product mismatch for Beckhoff and NetLink (item 7).
4. **Classify the root cause**, one class, with [`classes-and-routes.md`](references/classes-and-routes.md).
   Cyber-security firmware patching is a symptom, not a class: separate no owner or window, unwilling
   Plant IT/OT, hardware that cannot be patched, missing program or costly vendor support, and a vendor
   that no longer exists (`barrier-classes`).
5. **Place the tier.** Position of the machine's protocol and vendor in the easy-to-hard ranking
   (`barrier-classes`). Say where the ranking disagrees with the raw integration rate of the estate.
   A tool or system with no named operations owner and support level is class C4 whatever the
   blocker text says (`references/process-chain-practice.md`), and a case with no named owner is
   not a Roadmap exit.
6. **Choose the exit.**
   - **Roadmap**: the barrier is known, owned and can clear (patch window, program from the supplier,
     Cyber Security sign-off, edge device on order). Log it, give it a sequence position and an owner,
     and let the wave move on.
   - **Strategy**: it needs a decision above the machine (operations concept for the target system
     missing, tool or platform not rolled out at the plant, connector to be developed for several
     machines). Escalate to the OD lead (rollout and strategy to the deciding role named in the current approval policy, technical matters through
     COP, per `od-decision-routing`).
   - **Substitution**: reach the data another way, or replace the thing that cannot connect. When it
     costs money, hand the options to `od-investment-input`.
7. **Log it.** Write the barrier against the machine with its class, owner and date; add the use cases
   that depend on it (the guide asks for them: they decide whether a connector gets built). Update the
   readiness picture through the lane's reporting, not by hand-marking a dimension.
8. **Handover.** Roadmap items go back to the assessment protocol (section 5, barriers logged); strategy
   items to `od-decision-routing` as a decision request; substitutions to `od-equipment-integration`
   Route B or to `od-investment-input`. A data-model blocker (connected, tags not standardized) goes to
   `od-signal-standardization`.

## Output

[`assets/barrier-triage-record.md`](assets/barrier-triage-record.md), one per machine or per group of
identical machines.

## Still open

- `⟨Whether "roadmap" means the plant roadmap or the lane's integration roadmap⟩`: the playbook says
  "escalate to roadmap" without naming the owner. Supplier: IIAE.
- `⟨The barrier log's form and location⟩`: the playbook says "landscape module"; the module read
  (`landscape.md`) has a facility table with a "known barriers" column, not a per-machine log.
- `⟨Lead times⟩` for connector development and for OT and IT cyber-security approvals: called "high",
  no number in the sources.
- `⟨Counterpart for tool rollout decisions⟩` (open in `08-decision-rights.md`).
- `⟨Whether a vendor-less machine row⟩` is a data gap or an unknown machine: Plant ME.
- The class list is this skill's grouping of the recorded fallbacks and blocker texts; the OD lead has
  not confirmed it.

## Do not

- Do not connect, patch, write to a PLC or approve an external connection. This skill classifies and
  routes (`draft`).
- Do not record a barrier as "PLC program unavailable" when the program exists but nobody can change it
  (two blockers, two owners).
- Do not compose a procedure for an unwritten (`TODO`) branch, and do not configure a product capability
  that has no approved route.
- Do not leave a machine out of the wave without a logged barrier and an owner.
- Do not change a signal or data-model standard to make one machine easier.
- Do not read the integration rate of a vendor as the difficulty of its next machine.
