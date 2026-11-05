---
name: od-use-case-solution-evaluation
description: >-
  Evaluate whether a use case's envisioned solution actually fits its need — rank it against
  a library of known configurations as a fast pre-evaluation, profile the underlying
  complexity (27 drivers), find which of 16 IT/OT capability areas the solution depends on,
  compare the required level against the plant's as-is level with evidence, and sequence any
  gap through its realization dependencies. Produces a visualized case ranking, a per-area
  gap chart and a total evaluation score (0-100) that together resolve to one of four
  verdicts: ready to build, needs a named capability raised first, over-engineered for what
  the drivers justify, or escalate as a platform investment. Use once a use case is scoped
  (`od-use-case-definition`) and before its business case is calculated, whenever a solution
  looks more complex than the stated need, or when a target keeps getting set to "as high as
  possible" instead of from a stated reason.
license: MIT
allowed-tools: Read Grep Glob Bash(python3 scripts/evaluate_fit.py:*)
metadata:
  id: od-use-case-solution-evaluation
  tier: practice
  lane: use-case-support-service
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
    - external literature review commissioned by human:jakob.gabriel, 2026-10-22, kept in the personal Obsidian vault under Work-OpsDigit-Knowledge/External Research/IT-IoT-Maturity-Model/. Generalized the papers' tables into this skill's method; the papers' own three-plant case study and its company attribution are not carried into this skill — only the method is.
  okf:
    type: Agent Skill
    title: Use-case solution evaluation
    tags: [use-case-support-service, practice]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---

# Use-case solution evaluation

Read `od-context` first. This skill answers one question `od-use-case-definition` does not:
**does the envisioned solution actually fit what the plant has and what the problem needs —
or does it quietly require more capability than anyone has named?**

A use case can be perfectly scoped (Phase 2's objective, Phase 3's system assessment) and
still be mis-sized: built for a need nobody rated as severe, or blocked on a capability gap
nobody wrote down until the integration date. This is the systematic check for both, and it
always ends in a visualized ranking and a single evaluation score — never prose alone.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/case-library.md`](references/case-library.md) | **Step 0.** How the pre-evaluation ranking works, what the 70-case library actually is (literature cold-start, not a benchmark), and how to grow it with real cases |
| [`references/complexity-drivers.md`](references/complexity-drivers.md) | The 27 drivers that describe *why* a use case is complex, and which of the 16 areas each one points at — the problem side |
| [`references/focus-areas.md`](references/focus-areas.md) | All 16 IT/OT capability areas: levels, what each level looks like in a plant, and where to set the target from need — the solution side |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Quick fit tests used in the chain next to the capability model (tool boundary, edge versus plain connection, PLC versus rule engine, make or buy), the operations-concept gate, handoff and agent notes |
| [`references/dependencies.md`](references/dependencies.md) | Which capability levels require which others first, the source table's own reliability caveat, and the recommended backbone chain |

## The method — one fast pre-check, then four steps, same order every time

### Step 0 · Pre-evaluate by case ranking (fast)

Before anything else, run what you already know — even a rough as-is or target sketch
across a few areas — through `scripts/evaluate_fit.py`. It ranks the use case against a
70-case library by configuration similarity and prints a visualized top-5.

**This is a triage, not a verdict.** A close match (≈80%+) says the shape is already
documented — move faster through steps 1-4. No close match is itself a finding: treat the
use case as genuinely novel and budget the full method's time, not a quick pass. Either way,
continue to step 1 — ranking alone never sets a target or sequences a gap. See
`references/case-library.md` for what the library is and is not (it starts as literature,
not an internal benchmark).

### 1 · Profile the problem, not the solution

Rate the use case's situation against the **27 complexity drivers**
(`references/complexity-drivers.md`) on a five-step scale: no contribution · little ·
medium · high · dominant. Two people rate independently — the requester and the
DBVE/IIAE — then reconcile; a single self-rating is the weakest version of this step.

**Only drivers rated high or dominant matter for step 2.** Seven of the 27 are
organizational or market factors with no IT/OT lever (named in the reference) — rating
those high explains context, not a target.

### 2 · Find which capability areas the solution actually depends on

Each high/dominant driver maps to one or more of the **16 focus areas**
(`references/focus-areas.md`) — the candidates for a raised target. A use case rated high
only on, say, *product variety* and *employee qualification* has candidates in a handful of
areas, not all 16. **Most use cases touch three to six areas.** If every area looks like a
candidate, the driver ratings were not discriminating; redo step 1 before going further.

### 3 · Assess as-is, set target from need — per candidate area only

For each candidate area: record the **as-is level with evidence** (not a guess), then set
the **target from the driver that justified the area as a candidate**, never from the top of
the scale. `references/focus-areas.md` gives per-area target-setting guidance and the
observable evidence to look for.

**The target-setting rule, stated once because every area repeats it:** a target above as-is
needs a named driver or a named business need behind it. "Because the platform supports it"
is not a reason. This is the papers' own central argument — the 1980s CIM wave failed partly
by building what was technically possible rather than what the market needed, and an
assistance system (F3 level 3) beats a fully autonomous one (F3 level 4) more often than not.

**Gap = target − as-is, per area.** No gap anywhere → the solution is ready to build as
scoped; go to `od-benefit-calculation`. A gap anywhere is the finding this skill exists to
surface: the use case, as envisioned, needs a capability nobody has built yet.

### 4 · Sequence any gap, and classify it

Order the gaps using `references/dependencies.md` — a target can only be planned once its
prerequisites exist. Then classify what the sequenced gap actually is:

| Verdict | When | Next |
|---|---|---|
| **Ready to build** | No gap in any candidate area | `od-benefit-calculation` |
| **Needs a capability raised first** | One or two gaps, each closeable within this use case's own scope and timeline | Name the gap, its sequence position and its owner; hand the capability work to the composing skill it belongs to (see below), then return here before calculating the business case |
| **Over-engineered** | A target exceeds every driver that was rated high or dominant | Lower the target to what the drivers actually justify, or name the previously-unrated business need that justifies it — do not leave an unjustified target standing |
| **Escalate as a platform investment** | The gap spans several areas, several use cases would share it, or it touches a dependency chain with no closeable end inside this use case's scope | `od-decision-routing` — this is a roadmap decision, not a single use case's business case |

**Which skill owns which gap**, once named:

- F9 (communication interfaces), F10 (protocols) → `od-equipment-integration`
- F11 (data collection), F2 (communication capabilities, the push/poll half) → `od-data-availability-check`
- F16 (information-model continuity) → `od-signal-standardization`
- F1, F3, F6-F8, F12-F15 and anything with no obvious owner → stays with the use case itself; name it in the protocol and carry it into `od-benefit-calculation`'s scope and cost

## Script — visualization and the total evaluation score

[`scripts/evaluate_fit.py`](scripts/evaluate_fit.py) mechanizes step 0 and steps 2-4 from a
small JSON input ([`assets/example-use-case.json`](assets/example-use-case.json) is a filled
template):

```bash
python3 scripts/evaluate_fit.py my-use-case.json     # full report, ASCII visualization
python3 scripts/evaluate_fit.py my-use-case.json --json
python3 scripts/evaluate_fit.py --demo               # built-in worked example
```

It prints, in order: the candidate focus areas with the drivers behind each one, a **ranked
bar chart of the top 5 cases** from the library (step 0), a **gap chart per candidate area**
with each gap marked ready-now or blocked-on-a-named-prerequisite (steps 3-4), and a **total
evaluation score out of 100** — case-fit confidence (0-40, from the best case match),
driver-justified targets (0-30, the share of set targets that land on a candidate area) and
gap feasibility (0-30, the share of gaps that are ready now or fully sequenceable) — which
resolves to one of the four verdicts above. It does not replace judgement on the target
itself; that stays human, per the guardrails below. Fill
[`assets/evaluation-protocol.md`](assets/evaluation-protocol.md) by pasting the script's own
output into it, not by re-describing the run from memory.

## Guardrails

- **A tool without an operations concept (owner, service level, support level) is not "ready to
  build"** whatever the capability levels say; verdict is escalate. Tool boundary sentences and
  the operations-concept status go next to the verdict (`references/process-chain-practice.md`).
- **Never rate a driver from memory of a similar use case.** Each use case gets its own
  driver profile; two use cases at the same plant can be rated differently and both be right.
- **A close case-ranking match is a reason to move faster, never a reason to skip steps 1-4.**
  The ranking compares configurations, not whether this specific use case's drivers justify
  this specific target.
- **Never set every target to the top of its scale.** That is the over-engineering failure
  mode both papers warn about by name — see step 3.
- **Never read the realization-dependency table as a mechanical sequencer.** It is a starting
  point with known gaps (`references/dependencies.md` says which); validate the sequence
  against this registry's own architecture before committing a roadmap to it.
- **Never treat F5 (mobility), F9 (interfaces), F12 (storage) or F13 (processing) as a
  maturity ladder to climb to the top.** These four are architecture choices from a 2017
  decentralization paradigm, not goals — `references/focus-areas.md` says so per area. A
  "combined" or "partly mobile" target is frequently the right end state, not a waypoint.
- **Never present the undefined 4th levels (F10's standardized-plus-semantic level, F15's
  "decentralized") as a confirmed requirement.** They are the operationalization's own
  best-guess fill-in where the source material under-specifies; say so when you use them.
- **Never generalize the case library's literature statistics as if they describe this
  estate's plants.** They describe what the academic literature reported from 2006-2017; use
  the library only for ranking, never as a benchmark for a real plant.

## Definition of done

Step 0's case ranking has been run and pasted into the protocol. Every candidate focus area
(step 2) carries an as-is level with evidence and a target level with a stated reason tied to
a rated driver or a named business need — never "as high as possible." Where target exceeds
as-is, the gap is sequenced against its dependencies and classified into one of the four
verdicts above, with an owner and a next skill named. The total evaluation score is recorded,
not just the verdict it resolves to. Fill
[`assets/evaluation-protocol.md`](assets/evaluation-protocol.md) as the work happens, not
afterward — one document per use case, written so someone who was not in the room can see
what was decided, why, and what still depends on what.
