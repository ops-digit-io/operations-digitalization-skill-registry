---
name: process-derivation
description: >-
  Derive a lived business process from a validated use case: gate on request, demand and passed prototype; redesign, BPMN to-be model, adoption plan, landscape entry, monitoring. Not for building the prototype.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: process-derivation
  tier: practice
  lane: lane-2
  new_state_lane: "Lane 2 (23a)"
  new_state_step: "Derive the process: from the validated prototype to a to-be process that can be run and kept"
  department_names: ["process-derivation", "process-change"]
  owner_role: human:jakob.gabriel
  tags: [use-case-support-service, practice, new-state, draft, process, bpmn]
  authority_level: draft the derivation package, the to-be model and its check; the process owner accepts it, and every change approval and go-live stays human
  status: draft
  sources_read: 2026-11-16
  requires: [dept-context]
  derived_from:
    - "Public sources opened on 2026-11-16 and listed in references/public-methods.md (BPM lifecycle, redesign heuristics, BPMN/ISO 19510, CMMN, DMN, APQC PCF, VDI/VDE 3682 catalogue page, standardized work, ADKAR, Kotter, 29 CFR 1910.119(l), Process Mining Manifesto). No public source was found for this exact trigger; the composition is this skill's own inference."
  composes: [funnel-use-case, funnel-requirements, funnel-prototype, bc-build, bc-capital-request, dept-decision-rights, deploy-handover, catalog-usecase, metrics-scorecard]
  okf:
    type: Agent Skill
    title: Process derivation
    tags: [use-case-support-service, practice, new-state, draft, process, bpmn]
---

# Process derivation

Read `dept-context` first.

## Purpose

A prototype that passed proves a user can work with an idea. It does not make a process. This skill takes a use case that has a **request**, a **demand** and a **validated prototype** and derives the business process around it: what changes in the work, who does what, how it is modelled in BPMN, how it is standardised, how people are brought along, where it sits in the process landscape and how it will be checked once it runs. The aim is a process the organisation keeps running after the project team has left.

**Status: draft.** No public source opened for this work prescribes a method for exactly this trigger. The skill composes public methods for the parts ([`references/public-methods.md`](references/public-methods.md) says what each one states and what could not be verified); the composition is this skill's inference and nobody has validated it. Text marked **Inference** is reasoning, not a source's statement.

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## The gate: when this skill may run

All three must exist as records. If one is missing, stop, write the refusal note and send it back.

| Gate item | Evidence (a record, not a statement) | If missing |
|---|---|---|
| Use-case request | A defined use case with a named requester role and plant (`funnel-use-case`) | Back to `funnel-use-case` |
| Use-case demand | A requirement with acceptance criteria and growth boundaries, recorded as demand (`funnel-requirements`) | Back to `funnel-requirements` |
| Validated prototype | A validation record whose result is **passed**, with its status label and a named plant validator (`funnel-prototype`) | Back to `funnel-prototype`; a failed or inconclusive result stops here |

A prototype is not a proven value. The package never writes "proven"; it writes what the record says.

## Inputs and output

- **In:** the three records of the gate; the data verdict (`mi-data-availability`) where the process depends on machine data; the process landscape the organisation uses, if any (ask the owner).
- **Out:** the process derivation package [`assets/process-derivation-package.md`](assets/process-derivation-package.md), the to-be model as a BPMN 2.0 file checked by `scripts/check_derivation.py`, the adoption and embedding plan, and the landscape entry. A refusal note if the gate is not met. A human reviews; the process owner accepts.

## Procedure

Phases follow the BPM lifecycle: identify, discover, analyse, redesign, implement, monitor [PD1]. Keys [PDn] are in [`references/public-methods.md`](references/public-methods.md).

1. **Check the gate.** Open the three records, copy their references into section 0 of the package, and read the prototype result. If anything is missing or the result is not "passed", write the refusal note and stop. Control point: three references and one result in the package.
2. **Identify the process.** Name it as verb and object, name the **owner role** (never a person) and the plants or lines in scope; ask which process landscape applies. Control point: an owner role exists. No owner role means no process.
3. **Read the prototype as the as-is evidence** (discovery). What users did, which roles took part, what the pass criterion and result said, what was not tested. Ask the plant validator only for what the record does not answer. Method: [`references/derivation-method.md`](references/derivation-method.md).
4. **Write the change in one sentence, then redesign.** "Today <role> does <work> with <system>; after the change <role> does <work> with <use case output>." Run the redesign checklist [PD2]; judge every change on cost, flexibility, time and quality with evidence, or list it as an open item. Control point: no design change without evidence.
5. **Model the to-be process in BPMN** [PD3] [PD4]: one pool, a lane per role, named events and gateways, labelled flows, the exception path, external waits as events. Use a decision table (DMN [PD6]) or a case model (CMMN [PD5]) only where a flow is the wrong tool. Run `python scripts/check_derivation.py package.md process.bpmn` and fix every finding. Control point: the check reports READY.
6. **Standardise the repetitive work** [PD9]: sequence, role, trigger, what the use case shows, who may change the standard and when it is reviewed. Skip it, with the reason, for work that has no fixed sequence. Method: [`references/adoption-and-embedding.md`](references/adoption-and-embedding.md).
7. **Plan the change.** One ADKAR row per role group with evidence for the earliest unmet element [PD10]; a programme-level check against Kotter's steps [PD11] if the change spans more than one team; the five change-control points [PD12] if the process alters how a line or machine is operated. Control point: every role group has a row with evidence.
8. **Hook the process into the landscape**: level, parent, stable id, interfaces with the object that crosses, owner role, model location, version, review date [PD7]. Method: [`references/landscape-and-monitoring.md`](references/landscape-and-monitoring.md). Control point: every interface names its object.
9. **Design the monitoring now** [PD13]: which events the use case system records with timestamp and case id, which three questions the owner will ask, the event-to-model mapping, who looks and how often, and what triggers a new model version. Control point: if no event data exists, say so as an open item.
10. **Close the package.** List the open items and the decisions that belong to humans. Hand it to `bc-build` (step 24) as evidence for the benefit rows; the model, the plan and the landscape entry wait for the approval route and are executed in step 26 with `deploy-handover`. Stop there.

## Human gate and AI-agent notes

- **An agent may:** check the gate, read the records, draft the package, draft and check the BPMN model, fill the checklists, propose the landscape entry, write the refusal note.
- **Stays with roles:** the process owner accepts the process and the landscape entry; the plant representative confirms the as-is and the standard work; the OD lead and the Plant ME decide scope and priority (`dept-decision-rights`); the approvers decide investment (`bc-capital-request`); the plant's safety role names any legal change-control requirement; a human changes the landscape. The agent never publishes a process into the landscape, signs off a change or starts a go-live.

## Pitfalls

- Starting without the gate: a process derived from a click-dummy that nobody validated is a guess with a diagram.
- Writing a benefit: the package gives evidence for the benefit rows; `bc-build` calculates them. Do not write a saving, a time or a cost that no record gives.
- A model without the exception path, or with a gateway that has no question.
- A process without an owner role, or with the project team as the owner.
- "Everyone is informed" as the adoption plan: it names no role group and no barrier.
- Treating the regulation in [PD12] as proof that a plant process is covered by it. It is a checklist pattern here.
- Treating the numbering of a landscape as a sequence; the order lives in the model [PD7].
- Promising process mining. The skill prepares the event data and the questions [PD13]; running it is separate work.

## Definition of done

The package is complete or its gaps are named with the role that closes them; the gate record names three records and a passed result; the BPMN file passes `scripts/check_derivation.py`; every role group has an adoption row with evidence; the landscape entry is filled with an owner role; the monitoring section names the events and the review; nothing in it says "proven" or states a figure that no record gives; a human has been handed the package. Nothing has been accepted, published or started by the agent.

## Example

Fictional example (invented, not a company figure):

```text
Gate    : request = record A (role: shift lead, line X); demand = record B (acceptance: reason recorded within the shift);
          prototype = record C, result passed, status label click-dummy, validator = plant representative
Change  : "Today the shift lead writes the downtime reason on paper at shift end; after the change the line operator
          selects it on the use case screen when the stop happens."
Model   : pool "Plant", lanes line operator and shift lead; start "Stop detected"; gateway "Reason known?"
          (yes / no, no -> shift lead assigns); end "Reason recorded"; the check reports READY
ADKAR   : line operator -> earliest unmet element Knowledge (evidence: prototype session, two of three unsure of the list)
Landscape: process id proposed, Level 3, parent "Run production", owner role = production manager
Monitoring: event "reason recorded" with timestamp and stop id; question 1 = share of stops with a reason within the shift
```

If it fails: when the prototype record says "inconclusive", the refusal note names `funnel-prototype` as the place to continue and no model is drawn.

## Available Scripts

| Script | Purpose | Arguments |
|---|---|---|
| [`scripts/check_derivation.py`](scripts/check_derivation.py) | Check the gate record of a package and the structure of a BPMN file (start and end events, connected flow, named gateways with labelled flows, every task in a lane, named tasks) | `package.md [process.bpmn]`; exit 0 = READY, 1 = findings printed |
| [`scripts/test_check_derivation.py`](scripts/test_check_derivation.py) | Tests of the check | `python -m unittest scripts/test_check_derivation.py` |

An agent runs a script with its code or shell tool (`run_script` in tools that expose it) and reads the exit code and output.

## References

| File | Use it for |
|---|---|
| [`references/public-methods.md`](references/public-methods.md) | The public sources: what each says (quoted), what it is used for, its tier, what could not be verified, and the finding that no single method covers this trigger |
| [`references/derivation-method.md`](references/derivation-method.md) | Steps 3 to 5: the prototype as as-is evidence, the redesign checklist, BPMN modelling rules, decision table or case model, stop conditions |
| [`references/adoption-and-embedding.md`](references/adoption-and-embedding.md) | Steps 6 and 7: standard work, the ADKAR table per role group, the Kotter check, the change-control checklist, what makes it last |
| [`references/landscape-and-monitoring.md`](references/landscape-and-monitoring.md) | Steps 8 and 9: the landscape entry, placement level, reference numbers, interfaces, the monitoring questions from the Process Mining Manifesto |
| [`references/outputs.md`](references/outputs.md) | What the skill delivers, to whom, and when each output is complete |
| [`assets/process-derivation-package.md`](assets/process-derivation-package.md) | The package this skill produces, with the gate record |
| [`assets/to-be-process.example.bpmn`](assets/to-be-process.example.bpmn) | A fictional BPMN 2.0 model that passes the check; copy it as the starting point |
