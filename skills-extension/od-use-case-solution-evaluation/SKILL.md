---
name: od-use-case-solution-evaluation
description: >-
  Evaluate whether a use case's envisioned solution fits its need (Lane 2 step 22) — rank it against
  a library of known configurations, profile its complexity (27 drivers), find which of 16 IT/OT
  capability areas it depends on, compare required against the plant's as-is level with evidence, and
  sequence any gap. Produces a case ranking, a per-area gap chart and a total score that resolve to one
  of four verdicts: ready to build, raise a named capability first, over-engineered, or escalate as a
  platform investment. Use once a use case is scoped and before its business case, whenever a solution
  looks more complex than the need, or when a target is set "as high as possible" without a reason. Also
  profiles the as-is maturity of one machine, system or application on the same 16 areas (formerly
  od-maturity-assessment).
license: MIT
allowed-tools: Read Grep Glob Bash(python3 scripts/evaluate_fit.py:*)
metadata:
  id: od-use-case-solution-evaluation
  tier: practice
  lane: lane-2
  new_state_lane: "Lane 2 (22)"
  new_state_step: "Requirements, features and data check"
  owner_role: Digital-Business-Value-Engineer (DBVE)
  authority_level: draft on the evaluation and target levels; recommend on sequencing; never approve an investment
  status: stable
  origin: derived
  sources_read: 2026-10-22
  requires: [od-context]
  composes: [od-benefit-calculation, od-decision-routing, od-data-availability-check, od-equipment-integration, od-signal-standardization]
  derived_from:
    - Schott, P., Lederer, M., Eigner, I., Bodendorf, F. (2020). Case-based reasoning for complexity management in Industry 4.0. Journal of Manufacturing Technology Management, 31(5). DOI 10.1108/JMTM-08-2018-0262. Tables 4, 5, 7, 10, 11 — the driver set, the focus-area levels, the 70-case literature base and the realization-dependency table.
    - Schott, P., Schaft, T., Thomas, S., Bodendorf, F. (2017). Making IoT Run — Opportunities and Challenges for Manufacturing Companies. International Journal of Hyperconnectivity and the Internet of Things, 1(2), 25-44. DOI 10.4018/IJHIoT.2017070103.
    - Schott, P., Lederer, M., Niedermaier, S., Bodendorf, F., Hafner, M. (2017b). A Maturity Model to Organize the Multidimensionality of Digitalization in Smart Factories. In Handbook of Research on Applied Optimization Methodologies in Manufacturing Systems, IGI Global, pp. 354-374. Book DOI 10.4018/978-1-5225-2944-6. Original source of the 16 focus areas; not reviewed directly.
    - external literature review commissioned by human:jakob.gabriel, 2026-10-22, kept in the department documents/External Research/IT-IoT-Maturity-Model/. Generalized the papers' tables into this skill's method; the papers' own three-plant case study and its company attribution are not carried into this skill — only the method is.
  okf:
    type: Agent Skill
    title: Use-case solution evaluation
    tags: [use-case-support-service, practice]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# Use-case solution evaluation

## Purpose and where it sits

Answers the question `od-use-case-definition` does not: does the envisioned solution fit what the plant has and the
problem needs, or does it quietly require more capability than anyone named? It serves Lane 2 step **22** (features
and data check), before the business case (step 24), and feeds the Lane 3 fit test. Key user: DBVE; an AI agent can
run the script and draft the protocol. It always ends in a visualized ranking and one evaluation score, never prose
alone. Read `od-context` first.

## Inputs and output

- **Inputs:** the scoped use case from `od-use-case-definition`; the requirement and signal verdicts (`od-requirements-breakdown`, `od-data-availability-check`); a rough as-is or target sketch for step 0.
- **Output:** a filled [`assets/evaluation-protocol.md`](assets/evaluation-protocol.md) with the script output pasted in (one document per use case, written as the work happens), the total score and one of four verdicts. Input template for the script: [`assets/example-use-case.json`](assets/example-use-case.json).

## Procedure

0. **Pre-evaluate by case ranking.** Run what you know through `scripts/evaluate_fit.py` (top-5 of the 70-case library by configuration similarity). Triage, not a verdict: a close match (about 80% or more) means move faster through steps 1-4; no close match means a genuinely novel case, budget the full method. Always continue to step 1 ([`case-library.md`](references/case-library.md)).
1. **Profile the problem, not the solution.** Rate the 27 complexity drivers ([`complexity-drivers.md`](references/complexity-drivers.md)): none, little, medium, high, dominant. Requester and DBVE/IIAE rate independently, then reconcile. Only high or dominant drivers count for step 2; seven drivers are organizational or market factors with no IT/OT lever.
2. **Find the capability areas the solution depends on.** Each high/dominant driver maps to one or more of 16 focus areas ([`focus-areas.md`](references/focus-areas.md)). Most use cases touch three to six; if every area is a candidate, redo step 1.
3. **Assess as-is with evidence, set the target from need, per candidate area only.** A target above as-is needs a named driver or business need; "the platform supports it" is no reason. Gap = target minus as-is. No gap: ready, go to `od-benefit-calculation`.
4. **Sequence and classify any gap** using [`dependencies.md`](references/dependencies.md) (a target can be planned only once its prerequisites exist), then pick the verdict below.

```bash
python3 scripts/evaluate_fit.py my-use-case.json     # full report, ASCII visualization
python3 scripts/evaluate_fit.py my-use-case.json --json
python3 scripts/evaluate_fit.py --demo               # built-in worked example
```

The script mechanizes steps 0 and 2-4 and prints, in order: candidate areas with the drivers behind each, a ranked top-5 bar chart (step 0), a gap chart per area marked ready-now or blocked-on-a-named-prerequisite, and a **total evaluation score out of 100**: case-fit confidence (0-40, best match), driver-justified targets (0-30, share of set targets landing on a candidate area), gap feasibility (0-30, share of gaps ready or fully sequenceable). The score resolves to a verdict; the target itself stays a human judgement. Paste the output into the protocol, do not re-describe it from memory.

## Decision rules

| Verdict | When | Next |
|---|---|---|
| **Ready to build** | No gap in any candidate area | `od-benefit-calculation` |
| **Needs a capability raised first** | One or two gaps, each closeable inside this use case's scope and timeline | Name the gap, sequence position and owner; hand the work to the owning skill (below), return here before the business case |
| **Over-engineered** | A target exceeds every driver rated high or dominant | Lower the target to what the drivers justify, or name the previously unrated business need; never leave an unjustified target standing |
| **Escalate as platform investment** | The gap spans several areas, several use cases share it, or a dependency chain has no closeable end here | `od-decision-routing`; a roadmap decision, not one use case's business case |

**Gap owner:** F9 (interfaces), F10 (protocols) go to `od-equipment-integration`; F11 (data collection) and F2 (communication, push/poll half) to `od-data-availability-check`; F16 (information-model continuity) to `od-signal-standardization`; F1, F3, F6-F8, F12-F15 and anything unowned stay with the use case: name it in the protocol and carry it into the scope and cost of `od-benefit-calculation`.

**Operations-concept gate:** a tool without an operations concept (owner, service level, support level) is never "ready to build" whatever the levels say; the verdict is escalate. Put the tool boundary sentence and the concept status next to the verdict ([`process-chain-practice.md`](references/process-chain-practice.md)).

## Handoff

Verdict, score and protocol go to `od-benefit-calculation` (ready), to the owning skill (capability first), back to the definition (over-engineered) or to `od-decision-routing` (escalate). The receiver needs: per candidate area the as-is level with evidence, the target with its driver, the sequenced gaps with owner, the score. Done when step 0 is pasted, every candidate area has evidenced as-is and reasoned target, every gap is sequenced and classified with an owner and next skill, and the score is recorded.

## Human gate and AI-agent notes

- **Agent may:** run the script, draft driver ratings and the protocol, list evidence still missing. **Humans decide:** the driver ratings (two raters), the targets, the verdict, any investment; this skill never approves an investment.
- **Evidence to cite:** the observable evidence per as-is level, the driver behind each target, the script output.
- Quick fit tests (tool boundary, edge versus plain connection, PLC versus rule engine, make or buy): `references/process-chain-practice.md`.

## Pitfalls and open points

- Rating a driver from memory of a similar use case; each use case gets its own profile.
- A close case match used to skip steps 1-4; the ranking compares configurations, not whether these drivers justify this target.
- Setting every target to the top of its scale (the over-engineering failure the source papers name).
- Reading the dependency table as a mechanical sequencer; it has known gaps (`dependencies.md`); validate against this registry's architecture.
- Treating F5 (mobility), F9 (interfaces), F12 (storage), F13 (processing) as a ladder to the top; they are architecture choices, a "combined" or "partly mobile" target is often the end state.
- Presenting the undefined 4th levels (F10 standardized-plus-semantic, F15 decentralized) as confirmed requirements; they are best-guess fill-ins, say so.
- Using the library's literature statistics (2006-2017) as a benchmark for real plants; use it for ranking only.
- **Open points:** none recorded.

## References

| File | Open when |
|---|---|
| [`references/case-library.md`](references/case-library.md) | Step 0: how the ranking works, what the library is (literature cold-start), growing it with real cases |
| [`references/complexity-drivers.md`](references/complexity-drivers.md) | Step 1: the 27 drivers and the areas each points at |
| [`references/focus-areas.md`](references/focus-areas.md) | Steps 2-3: 16 areas, levels, evidence, target setting |
| [`references/dependencies.md`](references/dependencies.md) | Step 4: prerequisites between levels, reliability caveat, backbone chain |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Quick fit tests, operations-concept gate, handoff, agent notes |
| [`assets/evaluation-protocol.md`](assets/evaluation-protocol.md) | The protocol to fill |
| [`assets/example-use-case.json`](assets/example-use-case.json) | Filled input for the script |

## Absorbed: As-is maturity and complexity profile of one machine, system or application on the 16 IT/OT focus areas (formerly od-maturity-assessment)

Run [`references/od-maturity-assessment/procedure.md`](references/od-maturity-assessment/procedure.md) when you need the as-is profile of one machine, system or application rather than the fit of a use case's solution. It keeps its own references and assets under that folder and the authority it had.
