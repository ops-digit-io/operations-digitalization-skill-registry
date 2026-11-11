---
name: od-use-case-intake-triage
description: >-
  Decide what OD does with an incoming request: accept into one of three lanes, refuse, or route to the owner. Not for decision rights of an accepted request (od-decision-routing).
license: MIT
metadata:
  id: od-use-case-intake-triage
  tier: practice
  lane: all
  new_state_lane: "Intake (i1)"
  new_state_step: "Classify the demand into exactly one lane"
  owner_role: OD lead
  tags: [all, practice]
  authority_level: recommend
  status: stable
  requires: [od-context]
  composes: [od-system-fit-check, catalog-usecase, od-use-case-definition, od-requirements-breakdown, od-first-aid-kit]
  okf:
    type: Agent Skill
    title: Use-case intake triage
    tags: [all, practice]
---

# Use-case intake triage

## Purpose

Decide what OD does with an incoming request: accept it into exactly one new-state lane, refuse it, or route it to the function that owns it. Use it whenever a request, demand or idea arrives and it is not clear whether it is OD work or which lane it belongs to.

## Inputs and output

Inputs: the request, the channel it arrived through, and the references in this skill. Output: a one-line triage record per request (channel, lane, owner role, trigger satisfied, definition of done, priority basis, gate expected, known blockers) - see "Output of a triage".

## Procedure

1. Check the channel and record it ("Channels a request legitimately arrives through").
2. Is it OD's at all? Refuse and name the owner if not (step 1 in "The triage").
3. Apply the refusal list and shape the statement (steps 2 and 2b).
4. Classify into exactly one lane (step 3), prioritize (step 4) and check against OD's position (step 5).
5. Write the triage record and name the expected gate for `od-decision-routing`.

Read `od-context` first. Without a defined entrance, the loudest channel steers the
department — this skill is the entrance.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/refusal-playbook.md`](references/refusal-playbook.md) | Request patterns that look legitimate but should be refused or re-scoped, the tell in each, and one pattern accepted that should have been refused |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | How step i1 is run in the AI-driven chain: SMART test and object/event reduction, standard versus special, three-way triage (just do / go forward / lead change), lane by demand shape, handoff record, agent notes |

## Channels a request legitimately arrives through

- Plant use-case demand collected in **Use Case Definition / Integration Workshops**
- **Digital investment projects** initiated per the plant roadmap and kicked off with the
  MPEE OD team
- Requests and feedback surfaced through **COP** (technical); ODEC (strategic) is a historical source of past requests and decks, not a current channel
- **Ad-hoc analytics / Process First-Aid Kit** requests

**There is no central ticket queue or mailbox, confirmed 2026-10-22** — these four channels
are the whole intake, not a partial list standing in for an unwritten one. A request arriving
outside them is not thereby invalid; record which channel it is being admitted through,
because that is what makes the queue readable later.

## The triage

**1 — Is it OD's at all?** Refuse and name the owner if it is:

| Belongs to | Not OD |
|---|---|
| Manufacturing Engineering | Functional lead of Plant ME; automation-solution development |
| Product & Process Industrialization | Customer-project industrialization, RFQ, P-FMEA / process-parameter standards |
| Facility Management & Green Production | Energy and facility topics, green production |
| Tool & Machine Center | Tool-center operations and KPIs |
| IT | ERP / S4HANA ownership |

OD supports these with digital solutions; it does not own them. "Support with a digital
solution" is an OD request. "Own the outcome" is not.

**2 — Apply the explicit refusal list.** Refuse:
- requests with **no plant-roadmap link and no nameable business case**;
- solutions requiring systems **outside the lean standardized footprint** — notably a
  non-standard MES rollout short or mid-term. A request rarely names the system; run
  `od-system-fit-check` whenever the ask sounds like a normal dashboard or integration
  request but implies cross-process scheduling, full order genealogy or similar;
- work owned by a sibling function (automation build, facility/energy, tool centers).

A refusal is returned to the demand owner with the reason and the route, not dropped.

**2b — Shape the statement before lane matching.** A request is admitted only if it passes
the SMART test (purpose, objective, real problem, timeframe, named stakeholder; a target
with no baseline fails) and has been reduced to object, event and time. Then set the class
(standard cross-process, standard per-process, non-standard unique) and, for a list, the
three-way bucket (just do, go forward, lead change). Detail in
[`references/process-chain-practice.md`](references/process-chain-practice.md).

**3 — Classify into exactly one new-state lane.** Each demand goes to one lane at intake;
branches chain later, but intake decides once (department new-state draft, open design question 2,
working assumption).

| If the request is… | Lane | Ownership | Next |
|---|---|---|---|
| A **catalogued** use case; the target machine is connected | **Lane 1a** run a known use case | Plant self-service; OD supplies catalog and guardrails | `catalog-usecase` |
| A catalogued use case; machine not connected, a **standardized system** fits | **Lane 1b** standardized onboarding | Plant self-service; cost template | `catalog-usecase` |
| A **genuinely new** recurring need on connected equipment, including ad-hoc analytics that turns out to recur | **Lane 2** develop a new use case | OD-led (DBVE) | `od-use-case-definition` |
| Something needed does **not exist yet**: a new system or app, and/or a new machine connection | **Lane 3** new system or connector | OD-led front-end; build OD + external; integrate IT, Cyber Security gated | `od-requirements-breakdown`, then `od-system-fit-check` (tool-decision gate) |
| A one-off process question that needs an answer now | First-aid request | DBVE; ad-hoc analytics is read-only on the sources | `od-first-aid-kit`, which routes it to Lane 1, Lane 2 or external support |

**Fall-through is not a second intake.** A Lane 1 case that is not truly catalogued moves to Lane 2;
one that needs a non-standard system or a new machine moves to Lane 3. A Lane 2 use case that needs new
software chains into 3a, one that needs a new connection into 3b. Record the move on the same demand.

**Old service lines.** The four functional lines are retired in the new state: Use Case Support splits
into Lane 1 and Lane 2, Analytical Support is no longer a standing lane, Information Integration becomes
Lane 3b, and Project Support & Application Consultancy becomes the Lane 3 front-end. When a requester
names an old line, translate it with this crosswalk (`od-context`).

**4 — Prioritize.** By measurable value against the plant or central engineering roadmap
— savings, lead-time reduction, cost avoidance — aligned with strategic-plant scope.
**Confirmed 2026-10-22: this is the whole rule** — there is no further written
formalization (no scoring model, no weighting) beyond value-against-roadmap aligned with
strategic-plant scope.

**5 — Check the request against OD's position** before accepting a large one. A proposed
action should use a strength, cover a weakness, capture an opportunity or mitigate a
threat. One that does none of these is worth questioning: check the department's current weaknesses and
threats in the strategy record (look up: OD lead / latest ODEC strategy deck). Typical
ones are integration running behind its yearly target and a value delivery cycle that is
not yet proven; work that lifts integration to target or demonstrates the cycle earns
priority over work that does neither.

## Output of a triage

Record, in one line each: **channel · lane · owner role · trigger satisfied · definition
of done · priority basis · gate expected** (see `od-decision-routing`) · **anything
already known to block it**.

Naming the gate at intake is the single strongest predictor of whether the work moves:
the work that reliably moves is the work where the gate was identified at intake and the
owner was named. The work that stalls is almost never stuck on engineering.

## Do not

- Do not accept a request because it is urgent to the person asking; urgency must be
  derivable from the roadmap link and the value basis.
- Do not silently widen a lane's scope to make a request fit.
- Do not record a priority you have inferred. Many use cases carry `UNKNOWN`
  priority and `UNKNOWN` is a truthful value.

## Human gate and AI-agent notes

An agent may draft the triage record, propose a lane and prepare a refusal with its reason and route. The decision to accept a large request, to set a priority and to refuse stays with the OD lead role; the DBVE role owns the intake record for Lane 1 and Lane 2; the demand owner role receives every refusal. An agent never records a priority it inferred.

## Example

Fictional example (all values invented for illustration):

```text
Input : "Can you just add a scrap-rate tile to the Plant X dashboard?" (via a plant workshop)
Triage: channel = Use Case Definition workshop; OD's: yes; refusal list: no hit;
        catalogued, machine connected -> Lane 1a
Output: channel workshop | lane 1a | owner DBVE + plant | trigger: catalogued use case |
        done: plant confirms adoption | priority: UNKNOWN | gate: plant go-live | blockers: none known
```

If it fails: a request that fails the SMART test or has no roadmap link is invalid for admission; return it to the demand owner with the reason and the route.

## Definition of done

The request has a recorded channel, exactly one lane (or a refusal returned to the demand owner with reason and route), an owner role, a priority basis (`UNKNOWN` is allowed) and the expected gate.
