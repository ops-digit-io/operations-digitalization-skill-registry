---
name: od-use-case-definition
description: >-
  Run step 21 (define and diagnose) and the Lane 2 funnel around it (the former Use Case Support Service).
  Define a plant use case so it can be built, standardized, handed over and measured: scope it,
  break down the requirement, assess the (legacy) MF IT systems, place it on its capability
  template and process group, record the fields that make it evaluable. Also prepares and runs
  Use Case Definition and Integration workshops, and answers what happens to a use case between
  demand and daily use (roles, control points, error paths, autonomy, metrics, Process First-Aid
  Kit, prioritizing a use case or business case). Use when an accepted plant demand needs a
  definition, a use-case record is too thin to act on, or a workshop is being prepared.
license: MIT
metadata:
  id: od-use-case-definition
  tier: technical
  lane: lane-2
  new_state_lane: "Lane 2 (21)"
  new_state_step: "Capture the idea, process diagnostics"
  owner_role: Digital-Business-Value-Engineer (DBVE)
  authority_level: draft
  capacity: per the current DBVE roster
  escalation: OD lead (decision route per the current approval policy; look up)
  status: stable
  sources_read: 2026-10-23
  requires: [od-context]
  composes: [od-use-case-standardization, od-use-case-solution-evaluation, od-benefit-calculation, od-data-availability-check, od-use-case-intake-triage, od-system-fit-check, od-requirements-breakdown, od-handover-and-adoption, od-scorecard-reporting]
  derived_from:
    - ops-knowledge-graph/.../20-lanes/use-case-support-service/{playbook,skills,tasks,metrics,agent-brief}.md
    - ops-knowledge-graph/_knowledge/10-Department/Use case lifecycle.md
    - ops-knowledge-graph/_knowledge/10-Department/Use case standardization.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/12-portfolio.md
    - personal vault, Graph/Use Cases/*.md (650 pages) and Graph/Library Use Cases/*.md (100 pages), read 2026-09-17
  okf:
    type: Agent Skill
    title: Use-case definition
    tags: [technical, lane, use-case-support-service]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-09-17T00:00:00Z }
---

# Use-case definition

Read `od-context` first. Provenance: merged from the lane's playbook and the use-case vault pages.

## Start here: understand your own use case idea

You do not need to be a DBVE. If you have an idea for a use case, fill in the [`assets/idea-check.md`](assets/idea-check.md) sheet first: ten plain questions, the first being **"has someone already done this?"**, because a catalogued use case needs no definition at all (Lane 1). It ends in a one-page summary and a next step: ask for the catalogued use case (Lane 1), hand a new recurring need to OD (Lane 2), or learn that it needs new software or a connection first (Lane 3). "Don't know" is a valid answer, and a number without a source stays "unknown". Terms are explained in the vocabulary of `od-context`. A complete worked example, in words and clearly fictional, is in [`references/worked-examples.md`](references/worked-examples.md) section 4.

The rest of this skill is the DBVE's full method for the same idea once it goes ahead.

## Purpose and where it sits

Serves **step 21, define and diagnose**, and holds the service flow of the lane around it
(Lane 2, steps 21 to 26, plus the use-case half of Lane 1). Key user: the
Digital-Business-Value-Engineer (DBVE), with Plant ME as customer; an AI agent drafts, humans decide.
Every use case is **one plant's instance of one need**, never a programme or plant-wide ambition.
Lane detail (error paths, wait states, tasks, access, autonomy, metrics): `references/lane-service-flow.md`.

## Inputs and output

- **In:** an accepted plant demand (`od-use-case-intake-triage`), a SMART statement, the plant owner.
- **Out:** a defined use case: the filled [`assets/use-case-definition-protocol.md`](assets/use-case-definition-protocol.md)
  (one per use case, four sections = four phases), produced by asking
  [`assets/use-case-definition-questionnaire.md`](assets/use-case-definition-questionnaire.md)
  (Is/Is-Not and 5 Whys for Analyse, Benefits Dependency Network walk-through for Control).

## Lane flow: from demand to adoption

**Trigger:** a genuinely new recurring need on connected equipment (Lane 2), accepted by
`od-use-case-intake-triage`, or a workshop request. A known, catalogued case is Lane 1 and does not
come here (`catalog-usecase`). **Done (lane):** use case defined, requirements and data checked,
prototype validated, business case agreed, capital request approved where investment is needed,
implemented, adopted and, when proven and repeatable, catalogued. Step 21 = rows 1 and 2.

| # | Flow step | Step | Who | Control point | Skill |
|---|---|---|---|---|---|
| 1 | intake | Collect plant use-case demand | DBVE + Plant ME | Demand logged against the plant roadmap; no nameable business case: refuse per intake | `od-use-case-intake-triage` |
| 2 | 21 | Plant- and process-specific definition; process diagnostics | both | Use case scoped with a clear objective | this skill |
| 3 | 22 | Requirements, features and data check; assess (legacy) MF IT systems | DBVE | Requirement and data verdict agreed | `od-requirements-breakdown`, `od-data-availability-check`, `od-system-fit-check` |
| 4 | 23 | Prototype / validate with the recipient | DBVE + Plant | Prototype validated | `od-prototype-poc`, `od-analytics-asset-build` |
| 5 | 24 | Benefit calculation, business case, rank | both | Business case and priority agreed with Plant ME | `od-benefit-calculation`, `bc-assessment` |
| 6 | 25 | Capital request, if investment is needed | DBVE; humans approve | Approved by MPEE / BA Operations | `od-decision-routing`, `od-capital-request` |
| 7 | 26 | Implement; evaluate impact; ensure adoption; catalogue | both | Use case running; recipient confirms adoption | `od-handover-and-adoption`, `od-use-case-standardization`, `catalog-usecase` |

**Chaining out of Lane 2** (do not build it here): the use case needs new software or an app: hand
the system demand to Lane 3, branch 3a (`od-system-fit-check` routes 3a.1 to 3a.4). It needs a new
machine connection: hand it to Lane 3, branch 3b (`od-equipment-integration`). Record the move on the same
demand. A proven, repeatable result is catalogued (`catalog-usecase`) and future runs are Lane 1.

Before row 7 run `od-use-case-standardization`: a match to a library entry takes it rather than
being re-specified. Per-step template routing: `references/lane-templates.md`.

## The coordinate every use case carries

1. **Plant** (plant master data). 2. **Material family / process group**: Rubber, Plastic, Metal or Assembly, and a process group within.
3. **Capability**: a cross-plant template (Andon Board, OEE Calculation, Downtime Reporting, Process Quality Data, Machine Alerts,
Cycle Time, Recipe Values, Process Values, Manual Quality Data, Analytics, Other Use Cases).

Without all three the use case is not findable from another plant. Instantiated is not delivered:
confirm a usable precedent in `references/library-catalog.md` before assuming the template answers the need.

## States it is tracked in (set expectations at definition time)

- **Delivery status:** `IDEA` -> `PLANNED` -> `IMPLEMENTED` -> `PRODUCTIVE` (or `STOPPED`).
- **Workflow states** (development, implementation, handover) and **rollout phase** (`PHASE 1`..`5`) are tracked independently; detail in `references/lane-service-flow.md`.
- **Category:** standard cross-process · standard per-process · non-standard unique to one plant · AI use case.
  **The hinge:** declaring "standard" commits the use case to `od-use-case-standardization`.

## Procedure: four phases, each with a control point

Collect -> Analyse -> Assess -> Control. Maps to the portfolio stages Captured / Evaluated / Assessed / Planned;
a use case stuck at a stage stalled in the matching phase (`references/lane-service-flow.md`).

### 1 · Collect
1. **Confirm the need is one need.** Two decisions by two people at two moments = two use cases.
2. **Start from a SMART statement** (purpose, objective, real problem, timeframe, named stakeholder; a target without a baseline fails); if intake did not pass it, run the test and object / event / time reduction first.
3. **Log the demand** against the plant roadmap (workshop output or direct request).
4. **Name the moment in the day** from `references/vocabulary.md` (Daily Gemba, Troubleshooting, Activity Tracking, Utilization Improvement, Process Improvement, Quality Improvement, Traceability, Energy Reporting; more than one allowed). One that fits none is a use case nobody opens.

**Control point: demand logged against the plant roadmap.**

### 2 · Analyse
1. **Run process diagnostics** from the stated problem to the actual one.
2. **State the diagnosis, not the ask:** what is wrong and why it matters (`references/worked-examples.md` §1).
3. **Scope the objective**, not the solution; no dashboard design in place of a problem.
4. **State the business benefit, not the technical enabler**; classify tangible/intangible × cashable/non-cashable (`references/benefit-theory.md`). It is the input `od-benefit-calculation` needs.
5. **Name what else was considered** (doing nothing, closest library entry, smaller scope; one sentence each). A bespoke build with no rejected alternative is a default, not a decision.
6. **Match depth to category** (`references/patterns.md`): `standard` inherits its objective from the template, a one-line target is enough; `non-standard, unique to one plant` needs the full diagnosis.

**Control point: use case scoped with a clear objective.**

### 3 · Assess
1. **Break down the customer / process requirement.**
2. **Assess the (legacy) MF IT systems** (`references/vocabulary.md`). Check whether the need is already served by one on the Legacy Application List being retired; ask the plant, it is not a lookup (`references/patterns.md`).
3. **Name the machine(s)**, or confirm there are none.
4. **Split data points by source** (machine / checklist or manual / system) per process step; the data check consumes this.
5. **Check the data exists** -> `od-data-availability-check`. Unreadable data = integration request first; record the dependency now.
6. **Check the library before specifying** (`references/library-catalog.md`); take the closest entry, not a blank page. If it composes into a standard declaration, `od-use-case-standardization` is the library of record.

**Control point: system assessment complete.**

### 4 · Control (decide)
1. **Name the business or process change:** who does something differently and who confirms it happens (who *acts*, not who receives). No named change = a technical enabler that reaches `IMPLEMENTED` and stalls before `PRODUCTIVE`.
2. **Record the fields that make it evaluable:** output asset (Dashboard default; Report, App, Analytics Workflow, Agent alternatives; an App or Agent warrants asking if a Dashboard serves cheaper), business process, utilization expectation, plant owner, every known dependency. A title is not a definition.
3. **Evaluate whether the solution fits** -> `od-use-case-solution-evaluation` before the business case; a missing capability belongs in its scope and cost, not as an integration surprise.
4. **Calculate the business case and prioritize** -> `od-benefit-calculation`.
5. **Decide.** This commits capacity; everything before is preparation.

**Control point: business case and priority agreed with Plant ME.**

## Decision rules

- Not one need -> split. No nameable business case -> refuse per intake, return to demand owner.
- Library entry matches -> take it (`od-use-case-standardization`). Machine not connected -> no use case yet; integration request.
- Required system not deployed / operations concept missing -> tool-rollout decision to strategy; mark blocked in the portfolio.
- Savings with no registered plant project or no baseline -> a claim, not a result; fix before the next sprint review.
- Priority, potential and savings are filled on the benefit-calculation cadence, independent of Phase 2; a filled priority is not evidence of scoping (`references/patterns.md`).
- `UNKNOWN` priority or potential is not "low". Integration fails acceptance or no adoption -> rework back to the Lane 3 hand-off (see "Chaining out of Lane 2").

## Workshops

| Workshop | When | Template |
|---|---|---|
| Use Case Definition Workshop | Plant onboarding or a new demand wave | Standard Agenda - Use Case Workshop (SharePoint); run the questionnaire inside it |
| Use Case Integration Workshop | Use case ready for integration | Use Case Integration Workshop agenda |

Past workshop locations: the workshop folder of the vault.

## Definition of done

All four control points met. The use case carries plant, capability, process group, category, output asset,
utilization expectation, named plant owner and dependencies, plus (`references/benefit-theory.md`) the benefit
stated and classified, rejected options named, and the business/process change with who confirms it.

## Handoff

To `od-equipment-integration` **with** business case and requirement breakdown (via `od-use-case-standardization` first);
to `od-handover-and-adoption` at row 7 (flow step 26). Receiver needs the completed protocol, so a plant engineer who was not in the room can read what
was decided, why, what is open. Block-to-block handoff table: `references/process-chain-practice.md`.

## Human gate and AI-agent notes

- **Agent may:** read the data platform, Scorecard and library; draft definitions, benefit calculations, prioritization proposals, impact reports, workshop material.
- **Only a human decides:** investment, equipment integration, external machine connection (Cyber Security sign-off), data-model or rollout changes, external publishing; escalation OD lead.
- **Evidence:** never invent savings or impact (mark to-be-collected); cite the protocol answers, library entry and source for each figure.
- Systems and access, metrics: `references/lane-service-flow.md`.

## Pitfalls

- Declaring `standard` to look scalable: the CSP gate disagrees and rollout economics rest on it.
- A definition only its author can read: the handover test applies from the first draft (what is this, where does data come from, who owns it).
- Expecting the legacy-system check to be pre-answered: it is asked fresh every time.
- Recording the output asset as the benefit: the decision someone makes differently is the benefit.
- A blank benefit field because it resists a number: "intangible, non-cashable" is valid; silence is not.

## Open points

- ⟨Lane lead time to confirm⟩.
- ⟨Process First-Aid Kit request template: none found anywhere in the registry (real gap, `references/lane-templates.md`)⟩.
- ⟨MSB access scope (read / write) to confirm⟩.
- ⟨A dedicated OD use-case one-pager / business-case template beyond the SharePoint agenda: checked, not found; the questionnaire and protocol fill that gap⟩.

## References

| File | Open when |
|---|---|
| [`references/benefit-theory.md`](references/benefit-theory.md) | Benefits Dependency Network, benefit classification, options considered, the Implemented-to-Productive gap |
| [`references/patterns.md`](references/patterns.md) | Match effort to category, a decision isn't a scope, legacy check is tacit |
| [`references/vocabulary.md`](references/vocabulary.md) | Controlled vocabulary: business process, output asset, legacy systems and tools |
| [`references/worked-examples.md`](references/worked-examples.md) | Three illustrative use cases through the four phases |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Part A: step 21 in the AI chain (canvas, diagnosis patterns, can/cannot, handoff to 22). Part B: lane blocks, sprint deliverables, registration gate, handoffs |
| [`references/lane-service-flow.md`](references/lane-service-flow.md) | Error paths, wait states, recurring tasks, systems and access, autonomy, metrics |
| [`references/lane-templates.md`](references/lane-templates.md) | Which skill's asset answers each lane step's template |
| [`references/task-chain-and-tool-use.md`](references/task-chain-and-tool-use.md) | Recurring tasks as a trigger chain, tool access reasons, partner seams |
| [`references/library-catalog.md`](references/library-catalog.md) | Searching the use-case library by capability |
