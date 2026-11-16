---
name: funnel-first-aid
description: >-
  Capture an ad-hoc plant process issue (ramp-up problem, trouble-shooting case, unexplained process behaviour, "the diameter keeps oscillating") in a structured first-aid request and route it: make the problem S.M.A.R.T., record process, machine and existing data, pick data scenario A or B, name who benefits, then send it to a one-off analysis, to use case intake (recurring need) or back as a data gap. Use when a plant raises a process issue with no use case yet, asks for the Process First-Aid Kit, or when a one-off analytical request must be scoped before analysis starts. Drafts only; commits no cost and connects nothing. Not for a recurring need (funnel-use-case), a permanent machine connection (mi-equipment) or a dashboard change request (dept-intake).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: funnel-first-aid
  aliases: [od-first-aid-kit]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Extension, deepens Intake (i1), Lane 2 (21)"
  new_state_step: "Classify the demand into exactly one lane; Capture the idea, process diagnostics"
  owner_role: human:jakob.gabriel
  authority_level: draft
  status: draft
  requires: [dept-context]
  composes: [dept-intake, funnel-use-case, mi-data-availability, funnel-requirements, deploy-cybersec, mi-equipment, dept-decision-rights, invest-screen]
  okf:
    type: Agent Skill
    title: Process First-Aid Kit
    tags: [use-case-support-service, practice, first-aid, ad-hoc]
---
# Process First-Aid Kit

- Read `dept-context` first.
- This skill is a working version of the first-aid template and routing rule; it is a draft for the DBVE to adopt or replace.
- Outputs: [`outputs.yaml`](outputs.yaml) lists what this skill delivers, to whom, and when each output is complete.

## Purpose

- Turn a vague plant complaint into one filled request form and one routing decision with a written reason.
- First aid means process or product ramp-up support and trouble shooting: prepare data acquisition, make the problem S.M.A.R.T., generate an insight.
- It stops at the request and the route. It does not install, connect or price anything.

## Inputs and output

| | Content |
|---|---|
| Needs | The symptom in the requester's words, plant, machine or process, requester role, and a plant owner (role) who can confirm facts |
| Produces | The filled [`assets/first-aid-request.md`](assets/first-aid-request.md), a route with reason, a closing message to the requester |
| Tools | Read, Grep, Glob only (no connections to machines or data platforms) |

## When it applies, and when it does not

| Situation | Use this skill? | Instead |
|---|---|---|
| A process issue now, no use case, plant wants insight | Yes | |
| The need keeps coming back every shift or week | Capture it, then route to intake | `dept-intake`, then `funnel-use-case` |
| A request to change the look of an existing dashboard | No | `dept-intake` (refusal playbook) |
| Plant wants a machine connected for good | No, that is integration | Information Integration lane, `mi-equipment` |
| Request without an owner who can confirm facts at the plant | Not yet | Ask the Plant ME to name one |

## Procedure

- Copy this checklist and tick it off:

```text
[ ] 1 Log the request (date, plant, requester role)
[ ] 2 Fill sections 1-3 of the form with the requester
[ ] 3 Restate the problem S.M.A.R.T. (object and event)
[ ] 4 Check data, record scenario A or B
[ ] 5 Choose the route, write the reason
[ ] 6 Answer the cost question without a quote
[ ] 7 Hand over the form, tell the requester
```

1. **Receive and log the request** through the channel "ad-hoc analytics / Process First-Aid Kit requests". Note date, plant, requester role.
   - The central queue or mailbox is not confirmed yet (open question in `references/background.md`); write the channel you actually used.
2. **Fill the first-aid request** with the requester, in this order:
   - symptom in plain words; where and since when; process and machine; what is already measured;
   - what has been tried; what decision the answer informs; who at the plant owns the answer.
   - If the requester cannot state a question, run the S.M.A.R.T. step first, because the later sections depend on it.
3. **Make it S.M.A.R.T.** Restate the problem with a measurable symptom, a defined scope, a question the data can answer, a reason it matters and a time frame.
   - Test: specific purpose, clear objective, a real problem, a timeframe, a named stakeholder who needs it.
   - A precise date and a quantified target **without a baseline** still fail, because the target is invented. Capture the baseline first.
   - Reduce the plant sentence to an object and an event on a time axis; then judge whether it is unique.
4. **Check the data** with `mi-data-availability`: is the signal readable, at what resolution, for what period?
   - Scenario A: edge platform and compliant network available. Scenario B: no way to connect the machine to an available edge installation.
   - Scenario B means a device on the machine and manual data transfer. A live connection needs the `deploy-cybersec` sign-off before go-live; start that package early, it runs in parallel.
5. **Decide the route** with the routing table below and write the reason on the form.
6. **State the cost question honestly.** First aid may carry extra investment (device, reconfiguration, analytical template) that depends on preconditions.
   - A price indication in a tool deck is not a quote. Cost goes to the OD lead (`dept-decision-rights`).
7. **Hand over with the form** so the next skill does not re-ask. Tell the requester what was routed where and why.

## Example

```text
Raw request (fictional): "Line 3 diameter oscillates, can you look at the data?"

Not S.M.A.R.T.: no baseline, no owner, no question a dataset can answer.

Restated (fictional): "Since the new mandrel in week 12, the diameter at the
oven exit on line 3 swings more than before; the shift lead (role) wants to know
which controller input or product change precedes the swings, using the last
four weeks of PLC data, answer needed before the next ramp-up."
Object: product. Event: swing of the dimension beyond tolerance.
Data: signals readable on the platform -> scenario A.
Route: one-off analysis, because the need appeared once.
```

## Routing decision

| Finding | Route | Why |
|---|---|---|
| One-off question, data readable, insight is the answer | One-off analysis: Lane 1 self-service, or the absorbed ad-hoc procedure (below) | The goal is an insight, not an industrialized solution; refusing to industrialize is valid |
| One-off question, data not readable on the data platform | Information Integration lane, mark a **data gap**; do not approximate missing data | Interpolated data produces a confident wrong answer |
| Same need raised by several shifts, lines or plants, or recurring | `dept-intake` then `funnel-use-case` | A need that surfaces once is first aid; recurring is a use case |
| Insight delivered and used repeatedly, with recurring value | Promotion to a standard use case via `catalog-standardization` | Recurring value justifies industrializing |
| Needs a system outside the lean standardized footprint | Refuse and say why | Intake rule |
| Needs new connectivity or a Cyber Security decision | `deploy-cybersec`, Information Integration lane | Wait state in the lane playbook |
| Plant cannot name a question or an owner | Back to requester with the missing items | Nobody can confirm facts |

## Absorbed mode: ad-hoc analytics delivery

- Scope with this skill first. Open the absorbed procedure only when the route is "one-off analysis" and the analysis itself has to be run.
- Run [`references/od-analytical-support-service/procedure.md`](references/od-analytical-support-service/procedure.md) for composed artefacts and the task chain; recurring needs still go to intake, catalogued ones to Lane 1 self-service.
- It keeps its own references and assets and the authority it had (read-only on data sources).

## Human gate and AI-agent notes

- The requester accepts the rewritten S.M.A.R.T. statement; the plant owner confirms facts.
- Cost and any connection or installation are human decisions (OD lead, Cyber Security); this skill only proposes and routes.
- An agent may rewrite the statement, propose object and event, and draft the form; it marks every unknown as not recorded rather than guessing.

## Pitfalls

- Do not turn a one-off issue into a use case just because it is interesting; the funnel is for recurring need.
- Do not quote any price indication as an offer; prices change and the sources do not say who pays.
- Do not connect, install or reconfigure anything; propose it, route it, and respect the Cyber Security gate.
- Do not invent missing data or fill gaps by interpolation; mark a data gap.
- Do not accept a target without a baseline; the number would be invented and the analysis cannot show improvement.
- Do not name people in the form; use roles. No hostnames, addresses or credentials.
- A sensor value is not an event: derive the event deliberately before promising an answer.

## Definition of done

- The request form is complete or lists exactly what is missing; the problem is restated S.M.A.R.T.
- Data availability and scenario are recorded; the route is chosen with a written reason; the requester has been told.
- No cost or connection has been promised.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/first-aid-offering.md`](references/first-aid-offering.md) | You must explain scenario A versus B, the cost structure, or the shape of a typical ad-hoc analysis |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | The S.M.A.R.T. step is hard: good versus bad pair, object and event reduction, diagnosis patterns, handoff contract |
| [`references/background.md`](references/background.md) | You need provenance, the open questions (template, queue, closing rule, who pays) or the output table; never an instruction |
| [`references/od-analytical-support-service/references/composed-artefacts.md`](references/od-analytical-support-service/references/composed-artefacts.md) | The route is one-off analysis and you need the built asset behind each analysis step |
| [`references/od-analytical-support-service/references/process-chain-practice.md`](references/od-analytical-support-service/references/process-chain-practice.md) | You run ad-hoc analysis: descriptive first, plausibility before explainability, local versus global |
| [`references/od-analytical-support-service/references/task-chain-and-tool-use.md`](references/od-analytical-support-service/references/task-chain-and-tool-use.md) | You need the recurring tasks as a trigger chain and why each tool has its access |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
| [`references/outputs.md`](references/outputs.md) | The output contract in full (generated from outputs.yaml) |
