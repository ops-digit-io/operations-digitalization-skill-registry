---
name: od-use-case-intake-triage
description: >-
  Decide what OD does with an incoming request — accept it into one of the four service
  lines, refuse it, or route it to the function that actually owns it. Applies OD's
  intake channels, its prioritization rule and its explicit refusal list, and names the
  lane, the owner role and the trigger the request satisfies. Use whenever a request,
  demand, idea or "can you just…" arrives and it is not yet clear whether it is OD work,
  which lane it belongs to, or whether it should be refused. Also use to check that a
  request already in flight was admitted on legitimate grounds.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-use-case-intake-triage
  tier: practice
  lane: all
  owner_role: OD lead (Thomas Zipf)
  authority_level: recommend
  status: stable
  sources_read: 2026-08-10
  requires: [od-context]
  derived_from:
    - ops-knowledge-graph/.../00-core/05-intake.md
    - ops-knowledge-graph/.../00-core/04-service-catalog.md
    - ops-knowledge-graph/.../00-core/01-charter.md
  okf:
    type: Agent Skill
    title: Use-case intake triage
    tags: [all, practice]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Use-case intake triage

Read `od-context` first. Without a defined entrance, the loudest channel steers the
department — this skill is the entrance.

## Channels a request legitimately arrives through

- Plant use-case demand collected in **Use Case Definition / Integration Workshops**
- **Digital investment projects** initiated per the plant roadmap and kicked off with the
  MPEE OD team
- Requests and feedback surfaced through **ODEC** (strategic) and **COP** (technical)
- **Ad-hoc analytics / Process First-Aid Kit** requests

⟨A central ticket queue or mailbox is not confirmed — to confirm.⟩ A request arriving
outside these channels is not thereby invalid; record which channel it is being admitted
through, because that is what makes the queue readable later.

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
  non-standard MES rollout short or mid-term;
- work owned by a sibling function (automation build, facility/energy, tool centers).

A refusal is returned to the demand owner with the reason and the route, not dropped.

**3 — Match the trigger to exactly one lane.**

| If the request is… | Lane | Owner |
|---|---|---|
| Plant use-case demand, or a definition/integration workshop request | Use Case Support Service | DBVE |
| An equipment-integration or data-model-harmonization need per roadmap | Information Integration Service | IIAE |
| A digital investment project kick-off | Project Support & Application Consultancy | IIAE |
| An analytical or ad-hoc process-insight need | Analytical Support Service | DBVE |

If two lanes seem to fit, the **definition of done** decides — one lane, one trigger, one
DoD, one autonomy profile. A request that needs both an answer now and a solution later
is admitted to Analytical Support first and promoted afterwards, not run as one item.

**4 — Prioritize.** By measurable value against the plant or central engineering roadmap
— savings, lead-time reduction, cost avoidance — aligned with strategic-plant scope.
⟨The formal prioritization rule is not written down — to confirm.⟩

**5 — Check the request against OD's position** before accepting a large one. A proposed
action should leverage a strength, cover a weakness, capture an opportunity or mitigate a
threat. One that does none of these is worth questioning: notably, integration is behind
the yearly target (W4) and the value delivery cycle is not yet proven (W5), so work that
lifts integration to target or demonstrates the cycle earns priority over work that does
neither.

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
- Do not record a priority you have inferred. 362 of 650 use cases carry `UNKNOWN`
  priority and `UNKNOWN` is a truthful value.
