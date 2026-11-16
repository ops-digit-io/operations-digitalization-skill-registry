---
name: invest-screen
description: >-
  Check whether a plant request quietly needs a system outside the lean footprint (MES, EMS or similar) and, in Lane 3, run the tool-decision gate that routes a demand to reuse, self-develop, external build, integrate an app or a new connector. Gives a fit verdict (fits, redesign, escalate) or a gate verdict (Go, PoC-first, Reduce-complexity, Hold, Reject, Blocked) with a named next step. Use when a request sounds like live scheduling, full order genealogy or traceability across processes, when someone asks make or buy, integrate or connect, "do we need an MES for this", when an application design question needs a recommendation, or when an invest list needs screening. Recommends only; the OD lead decides. Not for writing the requirement (funnel-requirements) or intake lane triage (dept-intake).
license: MIT
metadata:
  id: invest-screen
  aliases: [od-system-fit-check]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Intake (i1), Lane 3 front-end (32)"
  new_state_step: "Classify the demand into exactly one lane; Tool-decision / IT-footprint gate (make, buy, integrate or connect)"
  department_names: ["invest-screen", "investment-screening", "investment-checking"]
  owner_role: Digital-Business-Value-Engineer (DBVE) / IIoT Interface & Automation Engineer (IIAE), whichever lane the request entered through
  tags: [practice, all]
  authority_level: recommend — flags the fit risk and proposes a redesign or an escalation; never approves a system change or a rollout exception itself
  status: stable
  origin: derived
  requires: [dept-context]
  composes: [dept-decision-rights, funnel-evaluation, deploy-appstore, mi-equipment, funnel-prototype]
  okf:
    type: Agent Skill
    title: System fit check
    tags: [practice, all]
---

# System fit check

- Read `dept-context` first.
- This is the cross-cutting check `dept-intake` and `funnel-requirements` both call before a request is scoped further: does this quietly need a system outside the lean footprint?
- A request rarely names a system. "Live cross-process scheduling with full order genealogy" is MES in different words, and redesigning after the use case is scoped is a much bigger conversation than catching it at intake.

## Purpose

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.
- Four modes, one skill; pick the mode first, because each has its own input and verdict.

| Mode | Use when | Input | Verdict words |
|---|---|---|---|
| Fit check (default) | A request is at intake or requirements; "do we need a system for this" | One request | Fits, Redesign, Escalate |
| Lane 3 gate (step 32) | A demand is in the Lane 3 front-end | One demand plus the tool in question | Go, PoC-first, Reduce-complexity, Hold, Reject, Blocked |
| Whole-list screen | The input is the MPEE Invest and Cost Planning list | A list of rows | The gate words per relevant row, grouped by region |
| Application consulting | An application question needs a full solution design recommendation | One application question | A design recommendation form |

- Terms: **fit check** is the three-step check below; **gate** is the Lane 3 tool-decision step; both are run through the same artefact, [`assets/system-fit-check.md`](assets/system-fit-check.md).

## Inputs and output

- **In:** the request or demand as the requester worded it, the plant, and for Lane 3 the purchase or tool in question.
- **Out:** the filled [`assets/system-fit-check.md`](assets/system-fit-check.md) with one verdict and a named next step.

```text
Request: "Live cross-process scheduling with full order genealogy" (plant X, fictional)
Need restated: schedule across processes and trace every order end to end
Boundaries crossed: no lightweight tool covers it (see references/tool-boundaries.md)
Plant availability: checked, dated
Verdict: Escalate as exception -> dept-decision-rights, "Tool/system rollout"
```

## Procedure: the fit check

- Copy this checklist and tick it off:

```text
[ ] 1 Need restated, independent of the request's wording
[ ] 2 Each tool boundary walked, reason written
[ ] 3 This plant's availability checked and dated
[ ] 4 Verdict and next step written in the fit-check form
```

### 1 · State the need, not the request

- Restate what the request asks the data or process layer to do, independent of the system or dashboard name the requester used.
- Do this first because the requester's own framing does the disguising, not lying; skipping it is why a request "sounds like a normal ask".

### 2 · Walk the tool boundaries in order

- Check the need against each lightweight tool's own **"is not"** line (`references/tool-boundaries.md`).
- QFPR is quality feedback, not KPI calculation or master data. MDA/PDA is machine and asset data, the "lightweight MES" for automation data.
- The Manufacturing Image Library is images and DL inspection, not process-parameter storage or model training. Recipe Management / Camline is recipe master data, not live value storage or alerting. The Energy Management System is energy data only.
- Test each tool's "integration recommended if" trigger as well: it says when the tool earns a rollout; its cost class (never a number) goes on the record.
- **If none covers it, the need is MES- or EMS-shaped.** Name the specific boundary line the need crosses, not a feeling.

### 3 · Check this plant's actual availability, not the estate average

- The same tool can be "not necessary" at one plant and "needed for multiple use cases" at another (`references/deployment-reality.md`).
- A tool being right in principle and a tool being deployed here are two facts; check both before concluding.
- Read the plant's own tool table with `references/plant-tool-availability.md`; check a legacy application with `references/legacy-applications-landscape.md`.

### 4 · Verdict and next step

| Verdict | When | Next |
|---|---|---|
| **Fits the lean footprint** | A covering tool exists and is available at this plant | Hand back to the calling skill; no further action |
| **Redesign onto a lighter tool** | The need is covered by a lighter tool than the request assumed | Re-scope the request onto that tool before defining it any further |
| **Escalate as exception** | The need is genuinely MES/EMS-shaped, or needs a tool not yet deployed here with no substitute | `dept-decision-rights` "Tool/system rollout" row; the OD lead decides with the IT-responsible role of the business side |

- Fill [`assets/system-fit-check.md`](assets/system-fit-check.md) as the check happens: five minutes, not a workshop.
- When the plant may already run a covering legacy application or tool, add [`assets/existing-system-worksheet.md`](assets/existing-system-worksheet.md).
- An "escalate" with a large capability gap in `funnel-evaluation` is the same finding from two angles; check whether that evaluation ran before escalating twice.
- If a step fails (no boundary line can be named, two sources disagree, plant status unknown), the check is not finished.

## Lane 3 tool-decision gate (step 32)

- In Lane 3 this is the mandatory **tool-decision / IT-footprint gate**; no demand leaves the front-end without it.
- Run the fit check first, then [`references/tool-decision-gate.md`](references/tool-decision-gate.md):

1. **Footprint hard gate**: the 8-point checklist in [`software-footprint-gate.md`](references/software-footprint-gate.md). Any open point blocks.
2. **Route** to 3a.1 reuse, 3a.2 self-develop, 3a.3 external build (guided buy), 3a.4 integrate a foreign app, or 3b new connector, by the OD x IT sourcing principles.
   - Solution-design stage first; build in-house only where the know-how is manufacturing's own; prefer cloud services, open source and the CMO deployment path; judge external builds on multi-year TCO.
3. **Score** the six criteria ([`decision-criteria.md`](references/decision-criteria.md)) with the sub-scores visible, then give the gate verdict with one decisive reason.
   - Gate verdict words: Go, PoC-first, Reduce-complexity, Hold, Reject, Blocked. "Engage" (OD should join an equipment invest) is an involvement class, not a verdict.

## Whole-list screen and application consulting

- **Whole-list screen.** For the MPEE Invest and Cost Planning list, run the `investment-checking` workflow ([`investment-checking-workflow.md`](references/investment-checking-workflow.md)).
   - Classify every row OD-owned, touching, interlock or not, with the involvement lexicon ([`screening-method.md`](references/screening-method.md)).
   - Run the footprint gate and the scored gate per relevant row, put open points to the department ([`department-questions.md`](references/department-questions.md)).
   - Write the review grouped by region, one controlling cycle per region ([`review-template.md`](references/review-template.md)). Read-only: recommend, never decide.
- **Application consulting.** For an application question needing a full solution design recommendation (which tool or app covers it, how data reaches it, who runs it afterwards), run [`references/od-application-consulting/procedure.md`](references/od-application-consulting/procedure.md).
   - The route goes to OpenSpec IT demand (external) for 3a.3 and 3a.4, `deploy-appstore` for 3a.1 and 3a.2, or `mi-equipment` for 3b.

## Human gate and AI-agent notes

- **Agent may:** restate the need, walk the boundaries, read the plant tool availability, draft the check and the Lane 3 screen, flag open footprint points.
- **Humans decide:** the OD lead and the IT-responsible role of the business side decide every rollout exception and every Lane 3 verdict; the plant's operations owner confirms what is deployed.
- **Evidence to cite:** the boundary line crossed, the dated plant availability, the footprint gate points.

## Pitfalls

- Never conclude "MES-shaped" from a feeling; name the specific boundary the need crosses, or the check is not finished.
- Never use the estate average for a plant; the same tool is in different states at different plants.
- Never return "fits" for a tool nobody runs; a tool with no named operations owner and support level is a service gap, so escalate (`references/process-chain-practice.md`).
- Never let the check approve a rollout exception; it recommends, and the "Tool/system rollout" gate in `dept-decision-rights` decides.
- Never silently resolve the EMS discrepancy below by picking the convenient version; ask.

## A live discrepancy to surface, not hide

- `references/non-bets.md` records the strategy position on EMS rollout; the tool catalogue in `references/tool-boundaries.md` can describe WiriTec (the EMS) as rolled out and in active use.
- When the written position and the catalogue disagree, confirm current status before citing either version. This is the policy-versus-practice drift the check exists to catch.

## Definition of done

- The actual need is stated independent of the request's framing.
- Each lightweight tool's boundary is checked against it with a stated reason, and this plant's availability is checked and dated.
- The verdict is one of the three fit verdicts with a named next step.
- In Lane 3, additionally: the footprint gate has no open point (or the verdict is Blocked), and the demand carries one route (3a.1 to 3a.4 or 3b) with its next skill.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/tool-boundaries.md`](references/tool-boundaries.md) | Step 2: what each lightweight tool (QFPR, MDA/PDA, MIL, Camline, WiriTec) is and is not for |
| [`references/deployment-reality.md`](references/deployment-reality.md) | Step 3: why the same tool is in different states at different plants |
| [`references/plant-tool-availability.md`](references/plant-tool-availability.md) | Step 3: reading the live Tool Overview for a plant (status codes, empty cells, disagreement with workshop tables) |
| [`references/legacy-applications-landscape.md`](references/legacy-applications-landscape.md) | The plant may already run a parallel MES, SCADA or dashboard system; how to read the Legacy Application List |
| [`references/maturity-profile-signals.md`](references/maturity-profile-signals.md) | You hold a maturity profile from `funnel-evaluation` and want fit-check signals from it |
| [`references/non-bets.md`](references/non-bets.md) | The request touches what OD deliberately does not pursue, or you need kill criteria |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Intake and step 32: boundary lines as classifiers, demand shapes, operations-concept precondition, handoff contract |
| [`references/tool-decision-gate.md`](references/tool-decision-gate.md) | Lane 3 gate: route to 3a.1-3a.4 or 3b, sourcing principles, verdict words |
| [`references/software-footprint-gate.md`](references/software-footprint-gate.md) | Lane 3 gate step 1: the 8-point footprint checklist |
| [`references/decision-criteria.md`](references/decision-criteria.md) | Lane 3 gate step 3: six scored criteria and verdict taxonomy |
| [`references/investment-checking-workflow.md`](references/investment-checking-workflow.md) | Whole-list screen: the workflow of the `investment-checking` master |
| [`references/screening-method.md`](references/screening-method.md) | Whole-list screen: involvement lexicon and de-noise rule |
| [`references/department-questions.md`](references/department-questions.md) | Whole-list screen: open points to put to the department |
| [`references/review-template.md`](references/review-template.md) | Whole-list screen: the review grouped by region |
| [`references/od-application-consulting/procedure.md`](references/od-application-consulting/procedure.md) | Application consulting: the absorbed procedure |
| [`references/od-application-consulting/assets/design-recommendation.md`](references/od-application-consulting/assets/design-recommendation.md) | Application consulting: the form for one design recommendation |
| [`references/od-application-consulting/references/application-maturity-profile.md`](references/od-application-consulting/references/application-maturity-profile.md) | Application consulting: rating a plant-local or foreign application on the IT/OT focus areas |
| [`references/od-application-consulting/references/build-path-options.md`](references/od-application-consulting/references/build-path-options.md) | Application consulting: the four build paths in Lane 3a with selecting question and gates |
| [`references/od-application-consulting/references/footprint-and-data-path.md`](references/od-application-consulting/references/footprint-and-data-path.md) | Application consulting: footprint and how the data reaches the application |
| [`references/od-application-consulting/references/legacy-application-landscape.md`](references/od-application-consulting/references/legacy-application-landscape.md) | Application consulting: legacy application landscape |
| [`references/od-application-consulting/references/process-chain-practice.md`](references/od-application-consulting/references/process-chain-practice.md) | Application consulting at steps 32 and 3a4: build-path questions, supplier selection, operations-concept precondition |
| [`references/background.md`](references/background.md) | You need provenance or the output table; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
