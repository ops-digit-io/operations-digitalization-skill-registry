---
name: od-use-case-definition
description: >-
  Define a plant use case so it can be built, standardized, handed over and measured —
  scope it against the plant's process, break down the requirement, assess the (legacy)
  MF IT systems it touches, place it on its capability template and process group, and
  record the fields that make it findable and evaluable later. Also covers preparing and
  running Use Case Definition and Use Case Integration workshops. Use when a plant demand
  has been accepted and needs turning into a defined use case, when an existing use-case
  record is too thin to act on, or when a definition or integration workshop is being
  prepared.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-use-case-definition
  tier: technical
  lane: use-case-support-service
  owner_role: Digital-Business-Value-Engineer (DBVE)
  authority_level: draft
  status: stable
  sources_read: 2026-09-17
  requires: [od-context]
  composes: [od-use-case-standardization, od-use-case-solution-evaluation, od-benefit-calculation, od-data-availability-check]
  derived_from:
    - ops-knowledge-graph/.../20-lanes/use-case-support-service/{playbook,tasks}.md
    - ops-knowledge-graph/_knowledge/10-Department/Use case lifecycle.md
    - ops-knowledge-graph/_knowledge/10-Department/Use case standardization.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/12-portfolio.md
    - personal vault, Graph/Use Cases/*.md (650 pages) and Graph/Library Use Cases/*.md (100 pages), read 2026-09-17
  okf:
    type: Agent Skill
    title: Use-case definition
    tags: [technical, use-case-support-service]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-09-17T00:00:00Z }
---

# Use-case definition

Read `od-context` first. Every use case is **one plant's instance of one need** — never a
programme, never a plant-wide ambition.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/benefit-theory.md`](references/benefit-theory.md) | The Benefits Dependency Network mapped to the four phases — why a technical enabler is not a benefit, the business/process change that closes the Implemented-to-Productive gap, the tangible/intangible × cashable/non-cashable benefit classification, and the options-considered discipline |
| [`references/patterns.md`](references/patterns.md) | The abstract rules this procedure runs on — match effort to category, a decision isn't a scope, the legacy-system check is tacit knowledge — each stated as a rule, illustrated once |
| [`references/vocabulary.md`](references/vocabulary.md) | The controlled vocabulary actually in use: business process, output asset, legacy systems and tools — for Phases 1, 3 and 4 |
| [`references/worked-examples.md`](references/worked-examples.md) | Three illustrative use cases (invented, placeholder values) carried through the four phases — a complete record, one correctly stopped before Control, and a minimal-but-correct standard case |
| [`references/library-catalog.md`](references/library-catalog.md) | How to search the use-case library (proven reference solutions) by capability, what a good entry looks like, and the method vocabulary — a guide to the live list, not a copy of it |

## The coordinate every use case carries

1. **Plant** — one of the manufacturing plants (plant master data).
2. **Material family / process group** — Rubber, Plastic, Metal or Assembly, and one of
   the process groups inside them.
3. **Capability** — one of the cross-plant templates, for example: Andon Board, OEE Calculation,
   Downtime Reporting, Process Quality Data, Machine Alerts, Cycle Time, Recipe Values,
   Process Values, Manual Quality Data, Analytics, Other Use Cases.

Without all three, the use case is not findable from another plant, which is the whole
reason the taxonomy exists. A capability is typically already instantiated at nearly every plant — the template is
rarely the thing that is missing. **Instantiated is not
delivered**, though: many capability-epic records at a plant group no use case at all (see
`references/patterns.md`; count them live). Confirm a usable precedent exists — in
`references/library-catalog.md`, not from the coordinate alone — before assuming the
template already answers this need.

## The states it will be tracked in

Set expectations at definition time, because these fail separately:

- **Delivery status** — `IDEA` → `PLANNED` → `IMPLEMENTED` → `PRODUCTIVE` (or `STOPPED`).
- **Three workflow states, tracked independently** — development, implementation,
  handover. Handover consistently trails the other two by about thirty use cases across
  the portfolio; that is the normal shape, not an anomaly to explain away.
- **Rollout phase** — `PHASE 1`…`PHASE 5`, named rollout batches usually tied to a plant
  project, not sequential queues.
- **Category** — standard cross-process · standard per-process · non-standard unique to
  one plant · AI use case. **This declaration is the hinge the whole function turns on**:
  declaring "standard" commits the use case to `od-use-case-standardization`.

## Procedure — four phases, each with a control point

The playbook's happy path (`20-lanes/use-case-support-service/playbook.md`) names a
**control point** at every step — the department's own term for the checkpoint that must be
true before the use case moves on. Read as four phases, in the playbook's own order —
**Collect → Analyse → Assess → Control** — not the order the words might suggest:

| Phase | Playbook step(s) | Control point |
|---|---|---|
| 1 · Collect | 1 | Demand logged against plant roadmap |
| 2 · Analyse | 2 | Use case scoped with clear objective |
| 3 · Assess | 3 | System assessment complete |
| 4 · Control (decide) | 4 | Business case & priority agreed with Plant ME |

This also lines up with the portfolio's own stage-gate model
(`00-core/12-portfolio.md`: `Captured → Evaluated → Assessed → Planned/Implementation →
Handed over → Effective`) — Collect produces *Captured*, Analyse produces *Evaluated*,
Assess produces the literal *Assessed* gate, and Control is the decision that moves a use
case into *Planned*. A use case stuck at one portfolio stage has stalled in the matching
phase below; that's where to look first.

Run [`assets/use-case-definition-questionnaire.md`](assets/use-case-definition-questionnaire.md)
to get there — the actual questions to ask, in order, including Is/Is-Not and 5 Whys for
Analyse and the Benefits Dependency Network walk-through for Control. Record each answer as
it happens, in `assets/use-case-definition-protocol.md` — the four phases are that
document's four sections.

### 1 · Collect

- **Confirm the need is one need.** If it decomposes into two decisions taken by two
  people at two moments, it is two use cases.
- **Log the demand** against the plant roadmap — workshop output or a direct request.
- **Name the moment in the day it belongs to**, from the controlled vocabulary in
  `references/vocabulary.md` (Daily Gemba, Troubleshooting, Activity Tracking, Utilization
  Improvement, Process Improvement, Quality Improvement, Traceability, Energy Reporting — a
  use case can carry more than one). A use case that fits none of these is a use case
  nobody will open.

**Control point: demand logged against the plant roadmap.**

### 2 · Analyse

- **Run process diagnostics** to get from the stated problem to the actual one.
- **State the diagnosis, not the ask.** A diagnosis names what's actually wrong and why it
  matters; a restated request does not. See `references/worked-examples.md` §1 for the
  shape of one.
- **Scope the objective.** This phase's control point is the objective, not the solution —
  do not let a specific dashboard or app design substitute for a stated problem.
- **State the business benefit, not the technical enabler.** What measurably improves, for
  whom — then classify it tangible/intangible × cashable/non-cashable, per
  `references/benefit-theory.md`. This is the input `od-benefit-calculation` needs; it
  does not derive the benefit from the output asset on its own.
- **Name what else was considered.** Doing nothing, the closest library entry, a smaller
  scope — one sentence each, per `references/benefit-theory.md` § *Options considered*. A
  bespoke build with no rejected alternative on record is a default, not a decision.
- **Match the depth to the category** — see `references/patterns.md`. A `standard` use
  case inherits its objective from the capability template; a one-line target is enough. A
  `non-standard, unique to one plant` use case has no template behind it — write the full
  diagnosis here, or nobody downstream can build it.

**Control point: use case scoped with a clear objective.**

### 3 · Assess

- **Break down the customer / process requirement.**
- **Assess the (legacy) MF IT systems** it touches — named systems and tools in
  `references/vocabulary.md`. The Legacy Application List tracks applications being replaced or
  retired; check whether the need is already served by one being retired. This is a
  question to ask the plant, not a lookup — see `references/patterns.md`.
- **Name the machine(s), if any**, and confirm rather than assume whether the use case
  genuinely has none.
- **Check the data exists** → `od-data-availability-check`. A use case whose data is not
  readable is an integration request first; record that dependency now.
- **Check the library before specifying** → [`references/library-catalog.md`](references/library-catalog.md),
  the proven entries by capability. Take the closest one rather than drafting from a
  blank page; if it composes into a standard declaration, `od-use-case-standardization` is
  the library of record.

**Control point: system assessment complete.**

### 4 · Control (decide)

- **Name the business or process change.** Who does something differently once this
  exists, and who confirms it's actually happening — not who receives the output, who
  *acts* on it. See `references/benefit-theory.md`. A use case with no named change is a
  technical enabler with nothing connecting it to its benefit; that is the shape of a use
  case that reaches `IMPLEMENTED` and stalls before `PRODUCTIVE`.
- **Record the fields that make it evaluable**: output asset (Dashboard is the default;
  Report, App, Analytics Workflow and Agent are the alternatives — see
  `references/vocabulary.md`), business process, utilization expectation, plant owner by
  name, and every known dependency. A title alone is not a definition. Naming an App or
  Agent is unusual enough to be worth a second look at whether a Dashboard would serve the
  same need cheaper.
- **Evaluate whether the envisioned solution actually fits** → `od-use-case-solution-evaluation`,
  before the business case — a solution that looks standard can still need a capability
  nobody has built yet, and that belongs in the business case's scope and cost, not as a
  surprise at integration.
- **Calculate the business case and prioritize** → `od-benefit-calculation`.
- **Decide.** This is the phase that actually commits capacity — everything before it is
  preparation for this decision, not the decision itself.
- **This phase's numbers are not Phase 2's objective.** Priority, potential and savings get
  filled on the benefit-calculation cadence, independent of whether Phase 2 ever produced a
  stated objective — see `references/patterns.md`. A filled priority is not evidence the
  use case was scoped.

**Control point: business case and priority agreed with Plant ME.**

## Input and output — the questionnaire and the protocol

Neither the four phases nor the workshops end in prose. Ask
[`assets/use-case-definition-questionnaire.md`](assets/use-case-definition-questionnaire.md);
fill [`assets/use-case-definition-protocol.md`](assets/use-case-definition-protocol.md) as
the work happens — one document per use case, its four sections matching the four phases
above, so a plant engineer who wasn't in the room can read what was decided, why, and
what's still open.

## Workshops

| Workshop | When | Template |
|---|---|---|
| Use Case Definition Workshop | Plant onboarding or a new demand wave | Standard Agenda — Use Case Workshop (SharePoint); run [`assets/use-case-definition-questionnaire.md`](assets/use-case-definition-questionnaire.md) inside it |
| Use Case Integration Workshop | Use case ready for integration | Use Case Integration Workshop agenda |

Past workshop locations are listed in the workshop folder of the vault. ⟨A dedicated OD use-case one-pager / business-case template
beyond the SharePoint agenda is not confirmed to exist in the source systems — checked, not
found; the questionnaire and protocol here are what fills that gap.⟩

## Definition of done

All four control points are met: demand logged against the plant roadmap, the use case
scoped with a clear objective, its requirement broken down and system assessment complete,
and a business case and priority agreed with Plant ME. It carries plant, capability, process
group, category, output asset, utilization expectation, a named plant owner and its
dependencies — plus, per `references/benefit-theory.md`: the business benefit stated and
classified, the rejected options named, and the business/process change named with who
confirms it happened.

## Do not

- Do not record `UNKNOWN` priority or potential as though it were low. Many use cases
  carry `UNKNOWN` priority or potential; absence is not an answer.
- Do not declare a use case `standard` to make it look scalable. The CSP gate will not
  agree, and the declaration is what the rollout economics rest on.
- Do not write a definition that only its author can read. The handover test applies from
  the first draft: what is this, where does its data come from, who owns it.
- Do not treat a filled priority or savings figure as proof the use case was scoped —
  see Phase 4.
- Do not expect the legacy-system check to be pre-answered anywhere. It is asked fresh,
  every time — see `references/patterns.md`.
- Do not record the output asset as the benefit. A dashboard is not a benefit; the decision
  someone makes differently because it exists is — see `references/benefit-theory.md`.
- Do not leave a benefit field blank because it resists a number. A blank field and "never
  assessed" already look identical, which is exactly why "intangible, non-cashable" is a
  valid, recordable answer and silence is not.
