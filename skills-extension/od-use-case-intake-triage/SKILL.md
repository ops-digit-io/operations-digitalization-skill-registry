---
name: od-use-case-intake-triage
description: >-
  Decide what OD does with an incoming request — accept it into exactly one of the three
  new-state lanes (1a/1b known use case, 2 new use case, 3 new system or connector), refuse it,
  or route it to the function that actually owns it. Applies OD's
  intake channels, its prioritization rule and its explicit refusal list, and names the
  lane, the owner role and the trigger the request satisfies. Use whenever a request,
  demand, idea or "can you just…" arrives and it is not yet clear whether it is OD work,
  which lane it belongs to, or whether it should be refused. Also use to check that a
  request already in flight was admitted on legitimate grounds.
license: MIT
metadata:
  id: od-use-case-intake-triage
  tier: practice
  lane: all
  new_state_lane: "Intake (i1)"
  new_state_step: "Classify the demand into exactly one lane"
  owner_role: OD lead
  authority_level: recommend
  status: stable
  sources_read: 2026-11-10
  requires: [dept-os]
  composes: [invest-screen, catalog-usecase, od-use-case-definition, funnel-requirements, od-first-aid-kit]
  derived_from:
    - ops-knowledge-graph/.../00-core/05-intake.md
    - ops-knowledge-graph/.../00-core/04-service-catalog.md
    - ops-knowledge-graph/.../00-core/01-charter.md
    - personal vault, Work-OpsDigit-Knowledge/Split Slides/10-Workshops--2025-01-21-2.1-What_are_UseCases-Overview_Reporting_Bondaries*.pptx and --2024_04_04_Summary_Carei_SmartFactory_UseCase_Definition_Workshop*.pptx, read 2026-10-22 — resolves PHASE1-ELICITATION.md topic 1 (refusal in practice) from the department's own record.
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT (README, lane 1-3), read 2026-11-10"
  okf:
    type: Agent Skill
    title: Use-case intake triage
    tags: [all, practice]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---

# Use-case intake triage

Read `dept-os` first. Without a defined entrance, the loudest channel steers the
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
  `invest-screen` whenever the ask sounds like a normal dashboard or integration
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
| Something needed does **not exist yet**: a new system or app, and/or a new machine connection | **Lane 3** new system or connector | OD-led front-end; build OD + external; integrate IT, Cyber Security gated | `funnel-requirements`, then `invest-screen` (tool-decision gate) |
| A one-off process question that needs an answer now | First-aid request | DBVE; ad-hoc analytics is read-only on the sources | `od-first-aid-kit`, which routes it to Lane 1, Lane 2 or external support |

**Fall-through is not a second intake.** A Lane 1 case that is not truly catalogued moves to Lane 2;
one that needs a non-standard system or a new machine moves to Lane 3. A Lane 2 use case that needs new
software chains into 3a, one that needs a new connection into 3b. Record the move on the same demand.

**Old service lines.** The four functional lines are retired in the new state: Use Case Support splits
into Lane 1 and Lane 2, Analytical Support is no longer a standing lane, Information Integration becomes
Lane 3b, and Project Support & Application Consultancy becomes the Lane 3 front-end. When a requester
names an old line, translate it with this crosswalk (`dept-os`).

**4 — Prioritize.** By measurable value against the plant or central engineering roadmap
— savings, lead-time reduction, cost avoidance — aligned with strategic-plant scope.
**Confirmed 2026-10-22: this is the whole rule** — there is no further written
formalization (no scoring model, no weighting) beyond value-against-roadmap aligned with
strategic-plant scope.

**5 — Check the request against OD's position** before accepting a large one. A proposed
action should leverage a strength, cover a weakness, capture an opportunity or mitigate a
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
