---
name: dept-intake
description: >-
  Decides what OD does with an incoming request, demand or idea: accepts it into exactly one of three lanes (known use case, new use case, new system or connector), refuses it with a reason and route, or hands it to the function that owns it. Use when a plant, key user or colleague brings something and it is unclear whether it is OD work, which lane it belongs to, what its priority basis is, or which gate it will hit. Also use when a request sounds like a normal dashboard but may need a system outside the lean footprint. Drafts the triage record; the OD lead decides large requests. Not for who approves an accepted request (dept-decision-rights) or for building the solution (catalog-usecase, funnel-use-case).
license: MIT
metadata:
  id: dept-intake
  aliases: [od-use-case-intake-triage]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Intake (i1)"
  new_state_step: "Classify the demand into exactly one lane"
  owner_role: OD lead
  tags: [all, practice]
  authority_level: recommend
  status: stable
  requires: [dept-context]
  composes: [invest-screen, catalog-usecase, funnel-use-case, funnel-requirements, funnel-first-aid]
  okf:
    type: Agent Skill
    title: Use-case intake triage
    tags: [all, practice]
---

# Use-case intake triage

## Purpose

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.
- Decide what OD does with an incoming request: accept it into exactly one new-state lane, refuse it, or route it to the function that owns it.
- Use it whenever a request, demand or idea arrives and it is not clear whether it is OD work or which lane it belongs to.

## Inputs and output

- Inputs: the request, the channel it arrived through, and the references in this skill.
- Output: a one-line triage record per request (channel, lane, owner role, trigger satisfied, definition of done, priority basis, gate expected, known blockers) - see "Output of a triage".

## Procedure

1. Check the channel and record it ("Channels a request legitimately arrives through").
2. Is it OD's at all? Refuse and name the owner if not (step 1 in "The triage").
3. Apply the refusal list (step 2, with `references/refusal-playbook.md` for look-alike requests) and shape the statement (step 2b).
4. Classify into exactly one lane (step 3), prioritize (step 4) and check against OD's position (step 5).
5. Write the triage record and name the expected gate for `dept-decision-rights`.
6. Check the record: channel, exactly one lane or a refusal with route, owner, priority basis (`UNKNOWN` allowed), gate. Fix and recheck until all are present.

- Read `dept-context` first.
- Without a defined entrance, the loudest channel steers the department; this skill is the entrance.

## Channels a request legitimately arrives through

- Plant use-case demand collected in **Use Case Definition / Integration Workshops**
- **Digital investment projects** initiated per the plant roadmap and kicked off with the
  MPEE OD team
- Requests and feedback surfaced through **COP** (technical); ODEC (strategic) is a historical source of past requests and decks, not a current channel
- **Ad-hoc analytics / Process First-Aid Kit** requests

- **There is no central ticket queue or mailbox** (confirmation date: `references/background.md`) — these four channels are the whole intake, not a partial list standing in for an unwritten one.
- A request arriving outside them is not thereby invalid; record which channel it is being admitted through, because that is what makes the queue readable later.

## The triage

- **1 — Is it OD's at all?** Refuse and name the owner if it is:

| Belongs to | Not OD |
|---|---|
| Manufacturing Engineering | Functional lead of Plant ME; automation-solution development |
| Product & Process Industrialization | Customer-project industrialization, RFQ, P-FMEA / process-parameter standards |
| Facility Management & Green Production | Energy and facility topics, green production |
| Tool & Machine Center | Tool-center operations and KPIs |
| IT | ERP / S4HANA ownership |

- OD supports these with digital solutions; it does not own them. "Support with a digital solution" is an OD request. "Own the outcome" is not.

- **2 — Apply the explicit refusal list.** Refuse, and use `references/refusal-playbook.md` when a request looks legitimate but fits none of these:
  - requests with **no plant-roadmap link and no nameable business case**;
  - solutions requiring systems **outside the lean standardized footprint**, notably a non-standard MES rollout short or mid-term;
  - work owned by a sibling function (automation build, facility/energy, tool centers).
- A request rarely names the system; run `invest-screen` whenever the ask sounds like a normal dashboard or integration request but implies cross-process scheduling, full order genealogy or similar.
- A refusal is returned to the demand owner with the reason and the route, not dropped, because a silent drop reads as an unanswered request and returns through a louder channel.

- **2b — Shape the statement before lane matching.** A request is admitted only if it passes the SMART test (purpose, objective, real problem, timeframe, named stakeholder;
- a target with no baseline fails) and has been reduced to object, event and time.
- Then set the class (standard cross-process, standard per-process, non-standard unique) and, for a list, the three-way bucket (just do, go forward, lead change).
- Detail: `references/process-chain-practice.md`.

- **3 — Classify into exactly one new-state lane.** Each demand goes to one lane at intake; branches chain later, but intake decides once (department new-state draft, open design question 2, working assumption).

| If the request is… | Lane | Ownership | Next |
|---|---|---|---|
| A **catalogued** use case; the target machine is connected | **Lane 1a** run a known use case | Plant self-service; OD supplies catalog and guardrails | `catalog-usecase` |
| A catalogued use case; machine not connected, a **standardized system** fits | **Lane 1b** standardized onboarding | Plant self-service; cost template | `catalog-usecase` |
| A **genuinely new** recurring need on connected equipment, including ad-hoc analytics that turns out to recur | **Lane 2** develop a new use case | OD-led (DBVE) | `funnel-use-case` |
| Something needed does **not exist yet**: a new system or app, and/or a new machine connection | **Lane 3** new system or connector | OD-led front-end; build OD + external; integrate IT, Cyber Security gated | `funnel-requirements`, then `invest-screen` (tool-decision gate) |
| A one-off process question that needs an answer now | First-aid request | DBVE; ad-hoc analytics is read-only on the sources | `funnel-first-aid`, which routes it to Lane 1, Lane 2 or external support |

- **Fall-through is not a second intake.** A Lane 1 case that is not truly catalogued moves to Lane 2; one that needs a non-standard system or a new machine moves to Lane 3.
- A Lane 2 use case that needs new software chains into 3a, one that needs a new connection into 3b.
- Record the move on the same demand.

- **Old service lines.** The four functional lines are retired. When a requester names one, translate it with the crosswalk in `dept-context` (`references/background.md`).

- **4 — Prioritize.** By measurable value against the plant or central engineering roadmap — savings, lead-time reduction, cost avoidance — aligned with strategic-plant scope.
- **This is the whole rule** (confirmation date: `references/background.md`) — there is no further written formalization (no scoring model, no weighting) beyond value-against-roadmap aligned with strategic-plant scope.

- **5 — Check the request against OD's position** before accepting a large one.
- A proposed action should use a strength, cover a weakness, capture an opportunity or mitigate a threat.
- One that does none of these is worth questioning: check the department's current weaknesses and threats in the strategy record (look up: OD lead / latest ODEC strategy deck).
- Typical ones are integration running behind its yearly target and a value delivery cycle that is not yet proven; work that lifts integration to target or demonstrates the cycle earns priority over work that does neither.

## Output of a triage

- Record, in one line each: **channel · lane · owner role · trigger satisfied · definition of done · priority basis · gate expected** (see `dept-decision-rights`) · **anything already known to block it**.

- Naming the gate at intake is the single strongest predictor of whether the work moves: the work that reliably moves is the work where the gate was identified at intake and the owner was named.
- The work that stalls is almost never stuck on engineering.

## Do not

- Do not read "just a small tile" as Lane 1: check that the use case is catalogued and the machine connected, because otherwise it falls to Lane 2 or 3.

- Do not accept a request because it is urgent to the person asking; urgency must be
  derivable from the roadmap link and the value basis.
- Do not silently widen a lane's scope to make a request fit, because the lane's gate and cost profile no longer apply.
- Do not drop a refused request without telling the demand owner the reason and the route.
- Do not record a priority you have inferred. Many use cases carry `UNKNOWN`
  priority and `UNKNOWN` is a truthful value.

## Human gate and AI-agent notes

- An agent may draft the triage record, propose a lane and prepare a refusal with its reason and route.
- The decision to accept a large request, to set a priority and to refuse stays with the OD lead role; the DBVE role owns the intake record for Lane 1 and Lane 2; the demand owner role receives every refusal.
- An agent never records a priority it inferred.

## Example

```text
Input : "Can you just add a scrap-rate tile to the Plant X dashboard?" (via a plant workshop)
Triage: channel = Use Case Definition workshop; OD's: yes; refusal list: no hit;
        catalogued, machine connected -> Lane 1a
Output: channel workshop | lane 1a | owner DBVE + plant | trigger: catalogued use case |
        done: plant confirms adoption | priority: UNKNOWN | gate: plant go-live | blockers: none known
```

## Example: refusal and fall-through (fictional)

```text
Input : "Please own the energy dashboard for the whole site and keep it running." (email to an OD member)
Triage: channel = none of the four (record it as admitted by email, to be moved into a workshop);
        OD's: no, energy and facility topics belong to Facility Management & Green Production
Output: refusal returned to the demand owner: reason = not OD-owned; route = Facility Management;
        offer = OD can support with a digital solution if that function owns the outcome

Input : "Roll out the standard downtime tile at Plant Y" (via a workshop)
Triage: catalogued, but the press is not connected -> Lane 1b; no standardized system fits -> falls to Lane 3
Output: channel workshop | lane 3 (moved from 1b, recorded on the same demand) | trigger: new connection |
        gate: Cyber Security sign-off, tool-decision gate | priority: UNKNOWN
```

## Definition of done

- The request has a recorded channel, exactly one lane (or a refusal returned to the demand owner with reason and route), an owner role, a priority basis (`UNKNOWN` is allowed) and the expected gate.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/refusal-playbook.md`](references/refusal-playbook.md) | A request looks legitimate but fits no refusal category (step 2), or the requester pushes back on a refusal |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | You apply the SMART test, reduce to object and event, choose the three-way bucket, or write the handoff record (steps 2b and 5) |
| [`references/background.md`](references/background.md) | You want the why, the confirmation dates behind the no-queue and priority statements; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
