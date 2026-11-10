---
name: od-requirements-breakdown
description: >-
  Turn an accepted demand into a requirement another lane can act on, for any of the three
  new-state lanes (Lane 2 and the Lane 3 front-end, and the hand-offs between them). Elicits the problem behind the stated request, sets it against the
  capability's standard baseline, names the signals it needs and whether they exist, writes
  testable acceptance criteria, assesses the legacy MF IT systems it touches, and produces
  both the handover packet that crosses a lane boundary and a standardized epic with its
  user stories and a background description of what it is used for. Use after intake accepts a
  demand and before anything is built — when scoping a use case for integration, specifying a machine or
  its signals, baselining a project, or scoping an analytical request.
license: MIT
allowed-tools: Read Grep Glob Bash(python3 scripts/check_requirement.py:*)
metadata:
  id: od-requirements-breakdown
  tier: practice
  lane: [lane-2, lane-3]
  new_state_lane: "Lane 2 (22), Lane 3 front-end (31)"
  new_state_step: "Requirements, features and data check; Requirements engineering"
  department_names: ["funnel-requirements", "requirements-funnel"]
  formerly: od-requirements-breakdown
  scope: od
  origin: derived
  owner_role: Digital-Business-Value-Engineer (DBVE) or IIoT Interface & Automation Engineer (IIAE), per lane
  authority_level: draft the requirement; accept or refuse per intake; approvals are human
  status: stable
  sources_read: 2026-11-10
  requires: [od-context]
  composes: [funnel-features, od-use-case-intake-triage, od-system-fit-check, od-use-case-definition, od-data-availability-check, od-signal-standardization, od-use-case-standardization, od-benefit-calculation, od-equipment-integration, od-acceptance-test, od-handover-and-adoption, it-demand-package]
  derived_from:
    - "Work vault, OD Department Knowledge/OD-instance/30-skills/product-funnel-skills.zip (skills/requirements-funnel/SKILL.md, references/handoff-schema.md), read 2026-11-10"
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md (UC-03, P-04)
    - ops-knowledge-graph/.../20-lanes/*/playbook.md (step 3 in each lane)
    - ops-knowledge-graph/_knowledge/90-Sources/generated/kg_nodes.csv (use case field population, target_text and blockers grammar; legacy applications)
    - ops-knowledge-graph/_knowledge/90-Sources/org-analysis/usecase-standardization-knowledgebase.md
    - ops-knowledge-graph/.../00-core/{05-intake,15-resources}.md
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/Transcripts/2026-09-11_OD-IT-alignment_meeting-notes.txt, read 2026-11-10"
  okf:
    type: Agent Skill
    title: Requirements breakdown
    tags: [all, od, practice]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Requirements breakdown

## Purpose and where it sits

Turns an accepted demand into a requirement another lane can act on, plus one epic with its user stories. It serves
Lane 2 step **22** (features and data check) and the Lane 3 front-end step **31** (requirements). The lane variant is
the artefact that crosses a lane boundary; it makes tacit judgement explicit. Key user: DBVE (use case, analytics) or
IIAE (integration, project). An AI agent drafts; the receiving lane accepts or says what is missing. Read `od-context`
first. The template is not new: its headings already appear in the estate's `target_text` and `blockers` fields
(`references/requirement-template.md`).

## Inputs and output

- **Inputs:** the accepted demand from `od-use-case-intake-triage` (or the defined use case from `od-use-case-definition`); the library check; signal verdicts from `od-data-availability-check`.
- **Output:** the requirement with its lane variant ([`assets/requirement-template.md`](assets/requirement-template.md)) and one epic with stories (`funnel-features`).

## Procedure

0. **Pick the entry and frame it** - the department's requirements funnel ([`requirements-funnel.md`](references/requirements-funnel.md)): idea mode or as-is mode; in as-is mode map the current process, find where the time actually goes, propose the to-be and derive requirements from the delta. Frame the need and name the **riskiest assumption** first.
1. **Elicit the problem, not the solution.** Five rounds in [`elicitation.md`](references/elicitation.md), then decompose and converge (funnel stages 2-4). A stated problem that names a technology is a solution: ask again.
2. **Check the library.** If another plant built it, the requirement is an adoption, not a build: `od-use-case-standardization`.
3. **Set the standard baseline.** Take the cluster's KPI set and checklist; record only this plant's deltas; check for a public data model (`od-signal-standardization`).
4. **Name and verify the signals.** Canonical name, direction in/out, existence verdict per signal from `od-data-availability-check` (verified, not assumed). An `out` signal is registered on the edge platform before anything publishes. A sensor value is not an event: state how each event is derived and whether production metadata (order, part, batch) is needed; a missing relation is a data gap, not approximated. Missing signals go into a `signal id | label | why needed` table for the information-integration lane.
5. **Write testable acceptance criteria**, including one that requires use in a real shift by a named plant role.
5a. **Fix the boundaries** (§6a, from the OD x IT alignment of 2026-09-11): objective, in and out of scope, approved interfaces, a **growth boundary** (the plants, machines, users or data volume it must not grow past) and the change rule. Anything beyond the line is a new requirement through intake, not an edit; this is the guard against mission creep, which AI-assisted building makes easy.
6. **Assess legacy systems and footprint** ([`legacy-system-assessment.md`](references/legacy-system-assessment.md)). If the spec implies more than the lightweight tools cover (cross-process scheduling, full order genealogy, heavier image/recipe/energy reads), run `od-system-fit-check` before specifying further.
7. **Classify the blockers.** *Method undefined* and *parameter selection open* are the requirement's own work, not an escalation.
8. **Value it honestly.** Label every figure `CALCULATION`, `ESTIMATION` or *not yet assessed* (`od-benefit-calculation`).
9. **Cut one epic with at least two stories** (`funnel-features`); by moment and role or by existing signals, never by technical layer.
10. **Check both**, then hand over:

```bash
python3 scripts/check_requirement.py MyRequirement.md --lane use-case
python3 ../../skills-extension/funnel-features/scripts/check_epic.py MyEpic.md
```

Exit **2** blockers, **1** warnings, **0** ready. Together they catch: a problem naming a technology, prose acceptance, a figure without a reliability label, an unverified signal list, a missing lane section, a missing growth boundary, a placeholder role, a generic "so that", an epic with one story, a story without a use-in-a-real-shift criterion.

## The epic

The epic and its user stories are the department's next funnel stage, **`funnel-features`**: hand the accepted requirement there. This skill stops at the requirement and its lane variant.

## Decision rules

- **Lane variants:** same core, one added section each; **nothing crosses a lane boundary without its variant** (an integration request without signal list and acceptance is a conversation, not a work item).

| Variant (`--lane`) | Adds | Flow step |
|---|---|---|
| `use-case`: Lane 2 use case that needs a new system or connection | Handover packet to Lane 3 (3a system demand or 3b connector): machines, signals, data path, outputs to register, integration acceptance; handed over with a business case | 22, requirements and data check; assess legacy IT |
| `integration`: Lane 3b new connector, Lane 1b order and connect | Equipment requirement: PLC identity, protocol, ingress variant, connector, PLC program available?, tag export, companion specification, Cyber Security sign-off | 3b4, connector design; feeds the PRS where a machine is bought or modified |
| `project`: Lane 3 front-end (new system) | Project scope baseline: stage/gate, investment and eCR route, milestones with acceptance points, resources, dependencies, training, flow owner | 31, requirements; kick-off and scope |
| `analytical`: ad-hoc request (Lane 1, Lane 2 or external, via `od-first-aid-kit`) | Request scope: question, decision supported, data verdict, turnaround, one-off or recurring | i1, request scoped |

- **One use case or three?** Different people or moments mean different use cases.
- **Real problem?** Ask what they would do differently with the answer.
- **Standard or specific?** Standard is declared at intake; adopt before specifying.
- **Signal or decision missing?** A missing parameter selection is the requirement's job, not engineering's.
- **Worth doing?** Fail it here, cheaply, not at the business case.
- **Refuse with a named route and a written reason** when: no roadmap link or nameable business case, needs a system outside the lean footprint, owned by a sibling function, one-off without recurring value, already exists elsewhere. A refusal beats a thin requirement that takes an integration slot and stalls.
- One story that will not split is a story, not an epic.

## Handoff

Write the funnel's **handoff file** ([`handoff-schema.md`](references/handoff-schema.md): `frame`, `riskiest_assumption`, `problems`, `candidates`, with the rules the next stage relies on) so `funnel-features` and `od-prototype-poc` resume without re-asking. The lane variant goes to the receiving lane (integration, `od-system-fit-check` at step 32, project, analytics); the epic goes into the backlog. Done when sections 1-6, 6a and 10 are complete, the variant is present, every signal has a verdict, acceptance is testable with an adoption criterion, blockers are classified with owners, legacy assessment and value label are done, both checks report zero blockers, and the receiver accepts.

## Human gate and AI-agent notes

- **Agent may:** elicit, draft the requirement and epic, run both checks, list what is missing. **Humans decide:** accept or refuse per intake, whether the problem is the real one, who is the shift-use role, all approvals.
- **Evidence to cite:** the verdict per signal, the library check result, the reliability label per figure, the check output.
- Chain detail (category to method to data job, object/event/metadata checks, AI-assisted signal selection, rubrics): [`process-chain-practice.md`](references/process-chain-practice.md).

## Pitfalls and open points

- Writing the solution (which nodes to wire) instead of what must be true.
- No growth boundary, or one that is a wish ("scalable"): the requirement quietly grows from one machine to every plant.
- Assuming a signal exists; blockers found late are usually assumptions.
- Inventing a figure to make the case look decided; *not yet assessed* is honest.
- Skipping the library check, the failure standardization exists to prevent.
- Handing over without the lane variant, the only part the receiver acts on.
- "So that the process gains transparency": generated on every story, tells nobody anything.
- Cutting by technical layer (connect the PLC, build the flow, build the dashboard): tasks, none usable alone.
- **Open points:** none recorded.

## References

| File | Open when |
|---|---|
| [`references/requirement-template.md`](references/requirement-template.md) | Writing the ten core sections or a lane variant, and how each fails |
| [`references/elicitation.md`](references/elicitation.md) | Running the question rounds; the five judgement calls; refusal |
| [`references/legacy-system-assessment.md`](references/legacy-system-assessment.md) | Checking legacy applications and the lean-footprint fit |
| [`references/requirements-funnel.md`](references/requirements-funnel.md) | The department package's requirements funnel (master): entry, as-is mapping, frame / elicit / decompose / converge, red flags, chaining |
| [`references/handoff-schema.md`](references/handoff-schema.md) | The handoff file between funnel stages, with a minimal valid example |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Steps 22 and 31 chain practice, signal handoff, agent notes |
| [`assets/requirement-template.md`](assets/requirement-template.md) | The blank requirement |
| [`scripts/check_requirement.py`](scripts/check_requirement.py) | Completeness check before handover (the epic check is in `funnel-features`) |
