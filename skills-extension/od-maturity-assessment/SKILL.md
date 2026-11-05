---
name: od-maturity-assessment
description: >-
  Assess how mature and how complex one machine, system or application is along the 16 IT/OT focus areas
  (identity, communication, protocols, data collection, storage, processing, analytics, control, information
  model, point of use), derive the complexity drivers behind the profile and the prerequisite chain between
  the areas, and turn the result into a route signal for the tool decision, the standard-system pick, the
  data check and the connector design. Rates qualitatively with an evidence grade, never from the top of the
  scale. Use when a machine, system or app must be judged before a route is chosen, when "can this be
  connected / is this app fit to integrate" is unclear, or when a use case or tool request needs an as-is
  profile of the thing it depends on.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-maturity-assessment
  tier: practice
  lane: all
  new_state_lane: Lane 2 (step 22), Lane 3 front-end (step 32), Lane 3b (step 3b4), Lane 1b (step 1b1)
  new_state_step: "Features and data check; tool decision; connector design; pick the standard system (proposed)"
  owner_role: Digital-Business-Value-Engineer (DBVE) / IIoT Interface & Automation Engineer (IIAE), whichever lane the object came through
  authority_level: draft
  status: draft
  origin: plan-draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-use-case-solution-evaluation, od-system-fit-check, od-application-consulting, od-data-availability-check, od-equipment-integration, od-barrier-triage, od-machine-integration-plan, od-signal-standardization, od-requirements-breakdown, od-decision-routing]
  derived_from:
    - Work vault (Work-OpsDigit-Knowledge), External Research, IT-IoT-Maturity-Model (overview, the focus-area notes F01 to F16, dependencies, complexity drivers, assessment template, references), generalized from three peer-reviewed publications by Schott and co-authors (2017, 2017b, 2020), read 2026-11-05; the papers' case study and literature case base are not carried over.
  okf:
    type: Agent Skill
    title: Maturity assessment
    tags: [practice, all, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Maturity assessment

Read `od-context` first.

`od-use-case-solution-evaluation` asks "does this **use case's solution** need more capability than anyone
has named?" and ends in a case ranking, a score and a verdict. This skill asks the question one level
below and earlier: **what is the thing itself - this machine, this system, this application - and what
does that mean for the route?** It produces an **as-is profile of an object**, the complexity drivers
behind it, the prerequisite chain between its gaps, and a **route signal** for the neighbouring skills.
It never sets a target on its own and never approves anything (`draft`).

## Where it sits in the chain (proposed step ids, `docs/new-state/process.yaml`)

| Step | What the profile feeds |
|---|---|
| **1b1** pick the use case and the standard system (lane 1b, machine not connected) | Does the machine reach the connection prerequisites at all (networked, protocol, identity)? Matches or stalls the kit pick; a stall goes to `od-barrier-triage` |
| **22** features and data check (lane 2) | The as-is levels of the data source (collection, storage, identity, information model) for `od-data-availability-check`, and the as-is input to `od-use-case-solution-evaluation` |
| **32** tool decision and IT gate (lane 3 front-end) | Object profile of the requested or existing system or app for `od-system-fit-check` and `od-application-consulting` (integrate, keep, replace; edge or plain connection) |
| **3b4** connector and pipeline (lane 3b) | Protocol, communication style and information-model level of the machine for `od-equipment-integration`, `od-signal-standardization`, `od-machine-integration-plan` |

It is not a step of its own; it runs inside these steps, once per object, and the record travels with the
object so nobody re-asks.

## References and assets

| File | Use it for |
|---|---|
| [`references/rating-rubric.md`](references/rating-rubric.md) | The 16 focus areas as a rating rubric for a machine, system or app: level cues, the question to ask, the evidence that counts, the route signal of a low level; the evidence grade; the data and interface inventory |
| [`references/drivers-and-dependencies.md`](references/drivers-and-dependencies.md) | From observed fact to complexity driver to candidate area; the prerequisite chain (backbone) and plausibility checks between areas; how to sequence gaps without trusting the source table mechanically |
| [`references/routing-and-handoff.md`](references/routing-and-handoff.md) | The profile as a route signal per step (1b1, 22, 32, 3b4), decision rules, handoff contract, pitfalls, questions and definition of done |
| [`references/model-caveats.md`](references/model-caveats.md) | What the model is and is not: provenance, the undefined levels, architecture-choice areas, why it is not a benchmark |
| [`assets/maturity-assessment-record.md`](assets/maturity-assessment-record.md) | The record: one object, 16 rows with as-is level, evidence grade, source, owner |
| [`assets/driver-and-gap-sheet.md`](assets/driver-and-gap-sheet.md) | Driver rating, candidate areas, gap chain and route signal on one page |

The full level tables, the driver list with area mapping, the dependency table and the evaluation script
live in `od-use-case-solution-evaluation` (`references/focus-areas`, `complexity-drivers`, `dependencies`);
they are linked, not copied. The rubric here is the object-level reading of the same model.

## Procedure

1. **Name the object and the question.** One object per record: a machine (with its controller), a
   system (historian, MES-like, platform) or an application (tool, dashboard, plant-local legacy app). State
   the question the profile serves: pick a standard system (1b1), check data (22), decide tool (32), design
   a connector (3b4). Without a question the assessment becomes maturity for its own sake.
2. **Gather facts from the records before asking anyone.** Machine List row, Connector Overview, tool and
   legacy-application lists, flow corpus, prior records of the same object type. Mark what is missing as
   `⟨unknown⟩`, not as level 1.
3. **Rate the 16 areas** with [`rating-rubric.md`](references/rating-rubric.md): the level actually in use
   today, an evidence grade (seen, stated, assumed) and the source. Areas that do not apply to this object
   type get `n/a` with a reason. Two people rate the contested areas independently, then reconcile.
4. **Check plausibility.** A level that contradicts its published prerequisites (for example data pushed
   by the asset but no network) is a rating error or a hidden gateway; find out which
   ([`drivers-and-dependencies.md`](references/drivers-and-dependencies.md)).
5. **Derive the complexity drivers.** Let the plant-side owner and the IT/OT side rate the drivers
   independently (no, little, medium, high, dominant); collect the areas that high and dominant drivers
   point at. Only these are candidates for a level above as-is; the rest stay "good enough".
6. **Chain the gaps.** For each candidate area with a stated need, list the prerequisites and order the
   steps. A gap without a use case, an owner and a business case is not planned.
7. **Read the route signal** with [`routing-and-handoff.md`](references/routing-and-handoff.md) for the step
   you are in, quote the rule it rests on, and hand on. The route itself is decided by the neighbouring
   skill and the human gate.
8. **File the record** with the object, with the date and the evidence, so the next step reads it instead
   of repeating the interview.

## Output

[`assets/maturity-assessment-record.md`](assets/maturity-assessment-record.md) (profile) and
[`assets/driver-and-gap-sheet.md`](assets/driver-and-gap-sheet.md) (drivers, gaps, route signal), one pair per
object or per group of identical objects.

## AI agent operating notes

- **Can do**: pre-fill the record from the Machine List, tool overview and legacy list; extract protocol,
  interface and storage hints from manuals, flow definitions and tickets; draft the interview questions
  from the rubric; flag implausible level combinations; propose candidate drivers and areas; draft the
  gap chain and the route signal with the rule quoted.
- **Inputs required**: the object and its question, the plant, the record sources above, and a named
  person who can confirm each area.
- **Evidence to cite**: per area the source and its read date; per route signal the rule in
  `routing-and-handoff.md` it rests on. A level with no source is graded "assumed".
- **Human gate**: the DBVE or IIAE accepts the profile; the plant owner and the IT/OT side confirm the
  driver ratings; every target above as-is, and the route itself, is a human decision through
  `od-decision-routing` where a forum is involved. The agent never rates a level it did not find evidence
  for, never sets a target "because the platform allows it", and never connects, configures or approves.
- **Handover**: the record and the sheet to the next skill of the step, open unknowns as a list with an
  owner role each, and the gap chain to `od-use-case-solution-evaluation` or `od-machine-integration-plan`.

## Still open

- `⟨Whether the profile is kept per machine type or per machine⟩`: per type is cheaper and matches the
  one-unknown-type-per-deployment practice of `od-machine-integration-plan`; per machine is needed where
  firmware or retrofit state differs. PROPOSAL: per type, with exceptions listed.
- `⟨Where the records are stored⟩`: no register is named in the sources; PROPOSAL: next to the Machine
  List row or the tool record.
- `⟨The meaning of the undefined fourth levels⟩` of protocols and of control structure
  ([`model-caveats.md`](references/model-caveats.md)).
- `⟨An internally validated dependency set⟩`: the source table is a starting point, not validated for this
  architecture.

## Do not

- Do not rate a level from capability on paper ("the PLC could speak OPC UA"); rate what is in use.
- Do not treat unknown as level 1, and do not fill an unknown with the estate's typical level.
- Do not set a target from the top of the scale, and do not climb the architecture-choice areas as a ladder.
- Do not present the literature's level distributions as a benchmark for any plant.
- Do not use the profile to rank plants or machines against each other; it describes one object for one
  decision.
- Do not sequence a roadmap mechanically from the source dependency table.
