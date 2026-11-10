---
name: od-cross-plant-compatibility
description: >-
  Check that a signal standard, data model or capability solution stays consumable by every
  plant's instance of the same capability - build the plant grid (controller vendor, field
  network, ingress variant, tool versions, language, state of the instance), test the standard
  against each difference, and write a verdict per plant that is consumable, consumable with a
  mapping, not consumable or unknown. Use when a signal standard or data-model change is about
  to be recommended, when a use case from one plant is proposed for another, when a flow or
  dashboard hard-codes something plant-specific, or when someone asks whether a standard will
  hold at the other plants.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-cross-plant-compatibility
  tier: practice
  lane: lane-3
  new_state_lane: "Extension, deepens Lane 3b (3b4)"
  new_state_step: "Connector design and data pipeline (edge to data platform)"
  owner_role: human:jakob.gabriel
  authority_level: recommend
  status: draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-signal-standardization, od-use-case-standardization, od-equipment-integration, od-data-availability-check, od-system-fit-check, od-decision-routing, catalog-usecase]
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/08-decision-rights.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/06-operating-rhythm.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/10-modules/smart-factory-use-case/landscape.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/information-integration-service/playbook.md
    - Work vault (Work-OpsDigit-Knowledge), Graph/Plants (plant notes, plant-profile blocks), read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Graph/Capability Epics (the template notes and their numbered plant instances), read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Graph/Registers/Blocker Register and Case Groups, read 2026-11-05
    - Skills od-signal-standardization, od-use-case-standardization and od-data-availability-check (plant-instance-map), read 2026-11-05
  okf:
    type: Agent Skill
    title: Cross-plant compatibility check
    tags: [information-integration-service, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Cross-plant compatibility check

Read `od-context` first.

Plan item P-08 of the department's skill map. The decision-rights table gives the rule in one line: data-model and
signal standardization (IIAE, consultation, no approval, reversible) carries the threshold **"must stay
consumable by every plant's instance of the capability"**, authority level `recommend`. This skill is how that threshold
is tested instead of assumed.

It composes, it does not repeat: `od-signal-standardization` defines the standard signal set for one machine;
`od-use-case-standardization` places a use case on a capability template and runs the CSP gate. This skill
asks the question neither asks: *does the thing still work at the plants that are not the first plant?*

## Why a check is needed

- A capability is not a one-off. Each of the eleven cross-plant capability templates has an instance at
  (nearly) every plant (read the Capability Epics notes). The standard has to serve all of them.
- The plants are not uniform underneath. The grid in [`references/plant-differences.md`](references/plant-differences.md)
  shows that most plants have Siemens controllers but several also run Rockwell, Mitsubishi, Beckhoff and others, and that
  there are three different integration paths to the platform (IIoT Edge, central OPC UA aggregation server, "evaluation
  ongoing"). A name or mapping that holds for the first plant's path may not hold for another.
- The foundation data model does not fit every machine: it was found suitable for greenfield, discrete,
  time-series-centric machines, while brownfield and continuous processes need other models
  (`references/process-chain-practice.md`). The base model applies to discrete manufacturing; a standard for continuous processes must be checked for fit first.
- Naming already drifts without a check: many distinct signal names for a much smaller set of concepts, several names for
  machine state alone (`od-signal-standardization`). Plant languages are a further source of variance.

## The references

| File | Use it for |
|---|---|
| [`references/plant-differences.md`](references/plant-differences.md) | The dimensions on which plants differ and how to read each live: region, vendors, field networks, ingress variants, tool rollouts, data-gap plants, capability-instance spread, known blockers. No figures |
| [`references/compatibility-tests.md`](references/compatibility-tests.md) | The tests to run per difference dimension, what a pass and a fail look like, and which composed skill supplies the evidence |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Where the base data model does and does not fit, process-specific models, data classes, plant differences that break a standard, one unknown machine type at a time, handoff contract, agent notes |
| [`assets/compatibility-check.md`](assets/compatibility-check.md) | The output: the plant grid with verdicts, the findings and the recommendation |

## Procedure

1. **Fix the subject.** Name the capability (one of the eleven), the standard under test (signal set, data model,
   flow, dashboard, library entry) and the first plant it was built at. Take the standard itself from the
   `od-signal-standardization` report or the `od-use-case-standardization` review; do not restate it.
2. **List the plants in scope.** Default: every plant that instantiates the capability, from the Capability Epics
   notes. If the standard is proposed for a subset, say which and why; the rule is written for every plant.
3. **Build the plant grid** using [`plant-differences.md`](references/plant-differences.md): for each plant in scope fill
   controller vendor, field network, ingress variant, tool versions available, plant language of tags, and the state
   of its instance. Refresh any figure from the live lists (Machine List, Tool Overview) if you rely on it for a
   verdict; the reference holds no figures.
4. **Run the tests** in [`compatibility-tests.md`](references/compatibility-tests.md) for each dimension in which at
   least one plant differs from the first plant. Use `od-data-availability-check` to learn what the platform really
   receives per plant instance.
5. **Give a verdict per plant** from four values:
   - *Consumable*: works unchanged.
   - *Consumable with mapping*: works if the plant's local name, unit or state model is mapped to the standard;
     the mapping is written down, owned and the standard itself is untouched (the local name stays an alias; see
     `od-signal-standardization`, multilingual tags).
   - *Not consumable*: the standard would need a plant-specific branch. This is a finding against the standard.
   - *Unknown*: no evidence either way. This is never rounded to "consumable".
6. **Decide what the standard does about a "not consumable".** Options, in order of preference: change the standard
   so it holds (a COP matter, see below); add a mapping rule to the standard; narrow the stated scope of the standard
   and say which plants it does not cover. Never add a plant-specific branch inside the standard.
7. **Write the recommendation** in [`assets/compatibility-check.md`](assets/compatibility-check.md) and route it with
   `od-decision-routing`. The decision is IIAE's by consultation; for a tool or system rollout the
   IIAE decides in tandem with the IT-responsible role of the business side (`08-decision-rights.md`). A change to a data model or connector
   is taken to the COP (monthly, technical), which is where the operating rhythm puts datamodel and connector updates.
8. **If the standard feeds the catalog**, hand the verdict grid to `catalog-usecase` so a plant picking the entry sees
   which plants it was checked at and which not.

## Decision table: what to do with the result

| Result | Action |
|---|---|
| All plants consumable | Recommend the standard; attach the grid |
| Some consumable with mapping | Recommend the standard plus the mapping rules; owner for each mapping is the plant's IT role, `⟨named owners to confirm⟩` |
| Any not consumable | Do not recommend as "standard for all plants"; return to step 6 |
| More than a few unknown | Recommend only for the checked plants; list the unknown plants and the evidence that would resolve each |
| First-plant-only evidence | Say so: a standard proven at one plant is a proposal, not a standard (compare the CSP gate in `od-use-case-standardization`) |

## What is still open

- **Per-plant tag language** is recorded nowhere as a field; infer from the signal list with `od-signal-standardization`.
- **Plants with no machine records** (zero machines in the plant notes) cannot be graded; their verdict is *unknown*.
- **Tool rollout records** in the plant notes list only tools that are recorded per plant; a missing line is not proof of
  "not available". Confirm with the IIAE role.
- **Whether a mapping is accepted by consumers** (dashboards, reports on the data platform) is not recorded anywhere;
  the test needs a named consumer per capability. `⟨consumer inventory per capability, to collect from DBVE and IIAE⟩`.
- **Lead time of the COP route** is not stated (escalation window `⟨to confirm⟩` in the operating rhythm).

## Do not

- Do not hard-code a plant, line or machine name into a standard, flow or dashboard that is meant for all.
- Do not treat "the data lands on the platform" as "the standard holds": two plants can land different names for the same concept.
- Do not edit the standard to fit one plant; map the plant to the standard.
- Do not call a standard cross-plant on the evidence of the plant that built it.
- Do not decide the data-model change yourself: you recommend; the decision route is in `od-decision-routing`.
