---
name: funnel-evaluation
description: >-
  Answers "does the envisioned solution fit the need and what the plant has, or does it quietly require
  more capability than anyone named?". Ranks the use case against a library of known configurations,
  rates its complexity, finds the IT/OT focus areas it depends on, compares the required level with the
  plant's as-is level with evidence, and sequences any gap. Ends in a score and one of four verdicts: ready
  to build, raise a named capability first, over-engineered, or escalate as a platform investment. Use
  once a use case is scoped and before its business case, when a solution looks more complex than the
  need, or when a target is set "as high as possible". Also profiles the as-is maturity of one machine,
  system or application. Not for costing (bc-build) or defining the use case (funnel-use-case).
license: MIT
allowed-tools: Read Grep Glob Bash(python3 scripts/evaluate_fit.py:*)
metadata:
  id: funnel-evaluation
  aliases: [od-use-case-solution-evaluation]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: lane-2
  new_state_lane: "Lane 2 (22)"
  new_state_step: "Requirements, features and data check"
  owner_role: Digital-Business-Value-Engineer (DBVE)
  authority_level: draft on the evaluation and target levels; recommend on sequencing; never approve an investment
  status: stable
  origin: derived
  requires: [dept-context]
  composes: [bc-build, dept-decision-rights, mi-data-availability, mi-equipment, mi-signals]
  okf:
    type: Agent Skill
    title: Use-case solution evaluation
    tags: [use-case-support-service, practice]
---
# Use-case solution evaluation

## Purpose and where it sits

- Answers the question `funnel-use-case` does not: does the envisioned solution fit what the plant has and the problem needs, or does it quietly require more capability than anyone named?
- Position: Lane 2 step 22, before the business case.
- Terms used throughout: **focus area** (one of 16 IT/OT areas, F1 to F16), **driver** (one of 27 complexity drivers), **protocol** (the filled evaluation document), **gap** (target minus as-is).
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Inputs and output

- **Inputs:** the scoped use case from `funnel-use-case`; the requirement and signal verdicts (`funnel-requirements`, `mi-data-availability`); a rough as-is or target sketch for step 0.
- **Output:** a filled [`assets/evaluation-protocol.md`](assets/evaluation-protocol.md) with the script output pasted in (one protocol per use case, written as the work happens), the total score and one of four verdicts. Input template for the script: [`assets/example-use-case.json`](assets/example-use-case.json).
- **Requirements:** Python 3.9 or newer, standard library only. Run from this skill's folder.

## Procedure

0. **Pre-evaluate by case ranking.** Run what you know through `scripts/evaluate_fit.py` (top-5 of the 70-case library by configuration similarity).
   - Triage, not a verdict: a close match (about 80% or more) means move faster through steps 1-4; no close match means a genuinely novel case, budget the full method.
   - Always continue to step 1 (`references/case-library.md`), because the ranking compares configurations, not whether these drivers justify this target.
1. **Profile the problem, not the solution.** Rate the 27 complexity drivers (`references/complexity-drivers.md`): none, little, medium, high, dominant.
   - Requester and DBVE/IIAE rate independently, then reconcile.
   - Only high or dominant drivers count for step 2; seven drivers are organizational or market factors with no IT/OT lever.
2. **Find the focus areas the solution depends on.** Each high or dominant driver maps to one or more of 16 focus areas (`references/focus-areas.md`). Most use cases touch three to six; if every area is a candidate, redo step 1.
3. **Assess as-is with evidence, set the target from need, per candidate area only.** A target above as-is needs a named driver or business need; "the platform supports it" is no reason.
   - Gap = target minus as-is.
   - No gap: ready, go to `bc-build`.
4. **Sequence and classify any gap** using `references/dependencies.md` (a target can be planned only once its prerequisites exist), then pick the verdict below.
5. **Validate before handover.** Run the script on the final input and paste its output; fix and rerun until all of these hold.
   - Every candidate area has evidenced as-is and a reasoned target; no target stands without a driver.
   - Every gap has an owner and next skill; the score and verdict are recorded.

```bash
python3 scripts/evaluate_fit.py my-use-case.json     # full report, ASCII visualization
python3 scripts/evaluate_fit.py my-use-case.json --json
python3 scripts/evaluate_fit.py --demo               # built-in worked example
python3 scripts/evaluate_fit.py --help               # usage; exit 2 on a missing or invalid input file
```

- The script mechanizes steps 0 and 2-4 and prints, in order:
  - candidate areas with the drivers behind each, a ranked top-5 bar chart (step 0), and a gap chart per area marked ready-now or blocked-on-a-named-prerequisite;
  - a **total evaluation score out of 100**: case-fit confidence (0-40, best match), driver-justified targets (0-30, share of set targets landing on a candidate area), gap feasibility (0-30, share of gaps ready or fully sequenceable).
- The score resolves to a verdict; the target itself stays a human judgement.
- Paste the output into the protocol, do not re-describe it from memory.

## Example (fictional)

```text
Input:  drivers {a14: high, a23: dominant}; as_is {F3: 2, F11: 2, F13: 2, F14: 2, F16: 1};
        target {F3: 3, F11: 3, F13: 3, F14: 4, F16: 2}   (predictive quality alert, fictional)
Output: candidate areas F3, F11, F13, F14 (F16 has no driver behind it -> over-engineered target)
        gaps: F11, F13, F14, F16 ready now; F3 blocked on C2-3 (communication level)
        score 88 / 100  ->  VERDICT: needs a capability raised first
Next:   lower the F16 target or name the business need; raise F2 first (owner: mi-data-availability);
        return here before the business case.
```

## Decision rules

| Verdict | When | Next |
|---|---|---|
| **Ready to build** | No gap in any candidate area | `bc-build` |
| **Needs a capability raised first** | One or two gaps, each closeable inside this use case's scope and timeline | Name the gap, sequence position and owner; hand the work to the owning skill (below), return here before the business case |
| **Over-engineered** | A target exceeds every driver rated high or dominant | Lower the target to what the drivers justify, or name the previously unrated business need; never leave an unjustified target standing |
| **Escalate as platform investment** | The gap spans several areas, several use cases share it, or a dependency chain has no closeable end here | `dept-decision-rights`; a roadmap decision, not one use case's business case |

- **Gap owner:** F9 (interfaces), F10 (protocols) go to `mi-equipment`; F11 (data collection) and F2 (communication, push/poll half) to `mi-data-availability`; F16 (information-model continuity) to `mi-signals`.
- F1, F3, F6-F8, F12-F15 and anything unowned stay with the use case: name it in the protocol and carry it into the scope and cost of `bc-build`.
- **Operations-concept gate:** a tool without an operations concept (owner, service level, support level) is never "ready to build" whatever the levels say; the verdict is escalate.
- Put the tool boundary sentence and the concept status next to the verdict (`references/process-chain-practice.md`).

## Handoff

- Verdict, score and protocol go to `bc-build` (ready), to the owning skill (capability first), back to the definition (over-engineered) or to `dept-decision-rights` (escalate).
- The receiver needs: per candidate area the as-is level with evidence, the target with its driver, the sequenced gaps with owner, the score.
- Done when step 0 is pasted, every candidate area has evidenced as-is and reasoned target, every gap is sequenced and classified with an owner and next skill, and the score is recorded.

## Human gate and AI-agent notes

- **Agent may:** run the script, draft driver ratings and the protocol, list evidence still missing. **Humans decide:** the driver ratings (two raters), the targets, the verdict, any investment; this skill never approves an investment.
- **Evidence to cite:** the observable evidence per as-is level, the driver behind each target, the script output.
- Quick fit tests (tool boundary, edge versus plain connection, PLC versus rule engine, make or buy): `references/process-chain-practice.md`.

## Pitfalls

- **Rating a driver from memory of a similar use case.** Each use case gets its own profile, because drivers differ even when the solution looks alike.
- **A close case match used to skip steps 1-4.** The ranking compares configurations, not whether these drivers justify this target.
- **Setting every target to the top of its scale.** This is the over-engineering failure the source papers name.
- **Reading the dependency table as a mechanical sequencer.** It has known gaps (`references/dependencies.md`); validate against this registry's architecture.
- **Treating F5 (mobility), F9 (interfaces), F12 (storage), F13 (processing) as a ladder to the top.** They are architecture choices; a "combined" or "partly mobile" target is often the end state.
- **Presenting the undefined 4th levels (F10 standardized-plus-semantic, F15 decentralized) as confirmed requirements.** They are best-guess fill-ins; say so.
- **Using the library's literature statistics (2006-2017) as a benchmark for real plants.** Use it for ranking only.
- **Open points:** none recorded.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/case-library.md`](references/case-library.md) | Step 0: how the ranking works, what the library is (literature cold-start), growing it with real cases |
| [`references/complexity-drivers.md`](references/complexity-drivers.md) | Step 1: the 27 drivers and the areas each points at |
| [`references/focus-areas.md`](references/focus-areas.md) | Steps 2-3: 16 areas, levels, evidence, target setting |
| [`references/dependencies.md`](references/dependencies.md) | Step 4: prerequisites between levels, reliability caveat, backbone chain |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Quick fit tests, operations-concept gate, handoff, agent notes |
| [`assets/evaluation-protocol.md`](assets/evaluation-protocol.md) | You write the protocol |
| [`assets/example-use-case.json`](assets/example-use-case.json) | You prepare the script input |
| [`assets/case-library.csv`](assets/case-library.csv) | You inspect or extend the 70-case library the script reads |
| [`scripts/model_data.json`](scripts/model_data.json) | You check the model data (levels, driver-to-area mapping, dependencies) the script loads |
| [`references/background.md`](references/background.md) | You need context, the required-output table or the handoff text; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |

## As-is maturity profile of one object (absorbed, formerly od-maturity-assessment)

- Use this path only when the task is the as-is profile of one machine, system or application, not the fit of a use case's solution.
- Open [`references/od-maturity-assessment/procedure.md`](references/od-maturity-assessment/procedure.md) and follow it; it keeps its own references and assets and the authority it had.

| File | Open when |
|---|---|
| [`references/od-maturity-assessment/assets/maturity-assessment-record.md`](references/od-maturity-assessment/assets/maturity-assessment-record.md) | You record the as-is profile on the 16 focus areas (level, evidence grade, source, owner) |
| [`references/od-maturity-assessment/assets/driver-and-gap-sheet.md`](references/od-maturity-assessment/assets/driver-and-gap-sheet.md) | You note driver ratings, candidate areas, the gap chain and the route signal on one page |
| [`references/od-maturity-assessment/references/rating-rubric.md`](references/od-maturity-assessment/references/rating-rubric.md) | You rate one object: level cues, the question to ask, the evidence that counts |
| [`references/od-maturity-assessment/references/drivers-and-dependencies.md`](references/od-maturity-assessment/references/drivers-and-dependencies.md) | You turn a profile into drivers, candidate areas and a sequenced gap chain |
| [`references/od-maturity-assessment/references/routing-and-handoff.md`](references/od-maturity-assessment/references/routing-and-handoff.md) | You turn the profile into a route signal at chain steps 1b1, 22, 32 or 3b4 |
| [`references/od-maturity-assessment/references/model-caveats.md`](references/od-maturity-assessment/references/model-caveats.md) | You must state what the model is and is not: provenance, undefined levels, literature distributions |
