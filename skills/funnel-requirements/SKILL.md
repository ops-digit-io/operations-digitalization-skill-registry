---
name: funnel-requirements
description: >-
  Turn an accepted demand into a requirement another lane can act on: a verified signal list, testable acceptance criteria, a lane variant, a handover packet and one epic. Use when a demand or use case has been accepted and someone must write the requirement, spec or handover for integration, a project or an analysis, when a requirement needs checking before it crosses a lane boundary, or when a request is vague ("we need a dashboard", "connect this machine"). Drafts the requirement; accepting or refusing stays with intake, approvals are human. Not for choosing the tool (invest-screen), splitting into stories (funnel-features) or defining the use case (funnel-use-case).
license: MIT
allowed-tools: Read Grep Glob Bash(python3 scripts/check_requirement.py:*)
metadata:
  id: funnel-requirements
  aliases: [od-requirements-breakdown]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: [lane-2, lane-3]
  new_state_lane: "Lane 2 (22), Lane 3 front-end (31)"
  new_state_step: "Requirements, features and data check; Requirements engineering"
  department_names: ["funnel-requirements", "requirements-funnel"]
  scope: od
  origin: derived
  owner_role: Digital-Business-Value-Engineer (DBVE) or IIoT Interface & Automation Engineer (IIAE), per lane
  tags: [all, od, practice]
  authority_level: draft the requirement; accept or refuse per intake; approvals are human
  status: stable
  requires: [dept-context]
  composes: [funnel-features, dept-intake, invest-screen, funnel-use-case, mi-data-availability, mi-signals, catalog-standardization, bc-build, mi-equipment, deploy-acceptance, deploy-handover]
  okf:
    type: Agent Skill
    title: Requirements breakdown
    tags: [all, od, practice]
---

# Requirements breakdown

## Purpose and where it sits

- Turns an accepted demand into a requirement another lane can act on, plus one epic with its user stories.
- Terms: a **demand** is what intake accepts; the **requirement** is the document this skill writes about it; a **request** to another lane is the requirement plus its lane variant.
- Default: start in idea mode unless a current process exists to map; use the `use-case` variant unless the demand names a connector, a project or an ad-hoc question.

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Inputs and output

- **Inputs:** the accepted demand from `dept-intake` (or the defined use case from `funnel-use-case`); the library check; signal verdicts from `mi-data-availability`.
- **Output:** the requirement with its lane variant ([`assets/requirement-template.md`](assets/requirement-template.md)) and one epic with stories (`funnel-features`).

## Procedure

0. **Pick the entry and frame it** - the department's requirements funnel ([`requirements-funnel.md`](references/requirements-funnel.md)): idea mode or as-is mode; in as-is mode map the current process, find where the time actually goes, propose the to-be and derive requirements from the delta.
   - Frame the need and name the **riskiest assumption** first.
1. **Elicit the problem, not the solution.** Five rounds in [`elicitation.md`](references/elicitation.md), then decompose and converge (funnel stages 2-4). A stated problem that names a technology is a solution: ask again.
2. **Check the library.** If another plant built it, the requirement is an adoption, not a build: `catalog-standardization`.
3. **Set the standard baseline.** Take the cluster's KPI set and checklist; record only this plant's deltas; check for a public data model (`mi-signals`).
4. **Name and verify the signals.** Canonical name, direction in/out, existence verdict per signal from `mi-data-availability` (verified, not assumed).
   - An `out` signal is registered on the edge platform before anything publishes.
   - A sensor value is not an event: state how each event is derived and whether production metadata (order, part, batch) is needed; a missing relation is a data gap, not approximated.
   - Missing signals go into a `signal id | label | why needed` table for the information-integration lane.
5. **Write testable acceptance criteria**, including one that requires use in a real shift by a named plant role.
6. **Assess legacy systems and footprint** ([`legacy-system-assessment.md`](references/legacy-system-assessment.md)). If the spec implies more than the lightweight tools cover (cross-process scheduling, full order genealogy, heavier image/recipe/energy reads), run `invest-screen` before specifying further.
7. **Classify the blockers.** *Method undefined* and *parameter selection open* are the requirement's own work, not an escalation.
8. **Value it honestly.** Label every figure `CALCULATION`, `ESTIMATION` or *not yet assessed* (`bc-build`).
9. **Cut one epic with at least two stories** (`funnel-features`); by moment and role or by existing signals, never by technical layer.
10. **Fix the boundaries** (§6a, from the OD x IT alignment, see `references/background.md`): objective, in and out of scope, approved interfaces, a **growth boundary** (the plants, machines, users or data volume it must not grow past) and the change rule.
   - Anything beyond the line is a new requirement through intake, not an edit; this is the guard against mission creep, which AI-assisted building makes easy.
11. **Check both documents**, fix every blocker and re-run until exit code 0, then hand over:

```bash
python3 scripts/check_requirement.py MyRequirement.md --lane use-case
python3 ../../skills-extension/funnel-features/scripts/check_epic.py MyEpic.md
```

- Exit **2** blockers, **1** warnings, **0** ready.
- Together they catch a problem naming a technology, prose acceptance, a figure without a reliability label, an unverified signal list, a missing lane section and a missing growth boundary.
- They also catch a placeholder role, a generic "so that", an epic with one story and a story without a use-in-a-real-shift criterion.

## Available Scripts

| Script | Purpose | Arguments |
|---|---|---|
| [`scripts/check_requirement.py`](scripts/check_requirement.py) | Completeness check of a requirement document before it crosses a lane boundary | `REQUIREMENT.md` (file), `--lane use-case`, `integration`, `project` or `analytical`, `--json` |

- Needs Python 3 and the standard library only; no packages to install. Run `python3 scripts/check_requirement.py --help` for usage.
- An agent runs a script with its code or shell tool (`run_script` in tools that expose it) and reads the exit code and output: 2 blockers, 1 warnings, 0 ready.

## The epic

- The epic and its user stories are the department's next funnel stage, **`funnel-features`**: hand the accepted requirement there.
- This skill stops at the requirement and its lane variant.

## Decision rules

- **Lane variants:** same core, one added section each; **nothing crosses a lane boundary without its variant** (an integration request without signal list and acceptance is a conversation, not a work item).

| Variant (`--lane`) | Adds | Flow step |
|---|---|---|
| `use-case`: Lane 2 use case that needs a new system or connection | Handover packet to Lane 3 (3a system demand or 3b connector): machines, signals, data path, outputs to register, integration acceptance; handed over with a business case | 22, requirements and data check; assess legacy IT |
| `integration`: Lane 3b new connector, Lane 1b order and connect | Equipment requirement: PLC identity, protocol, ingress variant, connector, PLC program available?, tag export, companion specification, Cyber Security sign-off | 3b4, connector design; feeds the PRS where a machine is bought or modified |
| `project`: Lane 3 front-end (new system) | Project scope baseline: stage/gate, investment and eCR route, milestones with acceptance points, resources, dependencies, training, flow owner | 31, requirements; kick-off and scope |
| `analytical`: ad-hoc request (Lane 1, Lane 2 or external, via `funnel-first-aid`) | Request scope: question, decision supported, data verdict, turnaround, one-off or recurring | i1, request scoped |

- **One use case or three?** Different people or moments mean different use cases.
- **Real problem?** Ask what they would do differently with the answer.
- **Standard or specific?** Standard is declared at intake; adopt before specifying.
- **Signal or decision missing?** A missing parameter selection is the requirement's job, not engineering's.
- **Worth doing?** Fail it here, cheaply, not at the business case.
- **Refuse with a named route and a written reason** when: no roadmap link or nameable business case, needs a system outside the lean footprint, owned by a sibling function, one-off without recurring value, already exists elsewhere.
   - A refusal beats a thin requirement that takes an integration slot and stalls.
- One story that will not split is a story, not an epic.

## Handoff

- Write the funnel's **handoff file** ([`handoff-schema.md`](references/handoff-schema.md): `frame`, `riskiest_assumption`, `problems`, `candidates`, with the rules the next stage relies on) so `funnel-features` and `funnel-prototype` resume without re-asking.
- The lane variant goes to the receiving lane (integration, `invest-screen` at step 32, project, analytics); the epic goes into the backlog.
- Done when sections 1-6, 6a and 10 are complete, the variant is present, every signal has a verdict, acceptance is testable with an adoption criterion, blockers are classified with owners, legacy assessment and value label are done,
- both checks report zero blockers,
- and the receiver accepts.

## Human gate and AI-agent notes

- **Agent may:** elicit, draft the requirement and epic, run both checks, list what is missing. **Humans decide:** accept or refuse per intake, whether the problem is the real one, who is the shift-use role, all approvals.
- **Evidence to cite:** the verdict per signal, the library check result, the reliability label per figure, the check output.
- Chain detail (category to method to data job, object/event/metadata checks, AI-assisted signal selection, rubrics): [`process-chain-practice.md`](references/process-chain-practice.md).

## Example

```text
Bad (fictional):  AC-1  The dashboard shows downtime nicely.
                  Signal: "the machine status" (no name, no direction, no verdict)
Good (fictional): AC-1  Given line 3 is running, when a stop above 2 minutes occurs,
                        then the stop appears in the downtime view within 1 minute.
                  AC-2  The shift lead (role) uses the view in one real shift check.
                  Signal: machine.state | in | verified readable on the platform

$ python3 scripts/check_requirement.py MyRequirement.md --lane use-case
BLOCKER: signal list not verified (fictional output)
exit code 2 -> fix, then re-run
```

- The bad version fails because nobody can test "nicely" and an unnamed signal cannot be checked for existence.

## Pitfalls

- Do not widen a requirement after handover; open a new one through intake, because the receiver already planned to the old boundary.
- Writing the solution (which nodes to wire) instead of what must be true.
- No growth boundary, or one that is a wish ("scalable"): the requirement quietly grows from one machine to every plant.
- Assuming a signal exists; blockers found late are usually assumptions.
- Inventing a figure to make the case look decided; *not yet assessed* is honest.
- Skipping the library check, the failure standardization exists to prevent.
- Handing over without the lane variant, the only part the receiver acts on.
- "So that the process gains transparency": generated on every story, tells nobody anything.
- Cutting by technical layer (connect the PLC, build the flow, build the dashboard): tasks, none usable alone.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/requirement-template.md`](references/requirement-template.md) | Writing the ten core sections or a lane variant, and how each fails |
| [`references/elicitation.md`](references/elicitation.md) | Running the question rounds; the five judgement calls; refusal |
| [`references/legacy-system-assessment.md`](references/legacy-system-assessment.md) | Checking legacy applications and the lean-footprint fit |
| [`references/requirements-funnel.md`](references/requirements-funnel.md) | The department package's requirements funnel (master): entry, as-is mapping, frame / elicit / decompose / converge, red flags, chaining |
| [`references/handoff-schema.md`](references/handoff-schema.md) | Step 11 handover: the handoff file between funnel stages, with a minimal valid example |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Steps 22 and 31 chain practice, signal handoff, agent notes |
| [`assets/requirement-template.md`](assets/requirement-template.md) | The blank requirement |
| [`scripts/check_requirement.py`](scripts/check_requirement.py) | Completeness check before handover (the epic check is in `funnel-features`) |
| [`references/background.md`](references/background.md) | You need provenance (the OD x IT alignment behind step 10), rationale or the output table; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
