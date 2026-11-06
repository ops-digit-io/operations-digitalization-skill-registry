---
type: Skill Reference
title: Ishikawa gap diagnosis
description: Why equal integration effort gives unequal savings - the four branches (people, method, machine and IT, environment) with the causes recorded in the gap analysis, the good and bad practice signature of a plant, fair comparison and the scaling test; open it to place a gap on a branch.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Ishikawa gap diagnosis

No figures. Causes below are those recorded in the department's plant-to-plant gap analysis; extend them only with
evidence from the plant and label additions `PROPOSAL`.

## The working rule

Compare plants with a similar system landscape and similar machine counts but different savings. **Equal integration
effort with zero or little saving points to people and method, not to technology.** Look at the people and method
branches first; use the machine and IT and environment branches to explain what remains.

## The four branches

| Branch | Causes recorded | Evidence to look for |
|---|---|---|
| **People** | "Not my responsibility"; unclear roles between OD, IT and engineering; functions (production, OPEX) not involved; a single engineer "only responsible for the technical part" | Who attends requirement meetings; who owns the use case after delivery; named key user and deputy; who asks for ideas |
| **Method** | No standard for the savings calculation; weak requirements management for systems and use cases; no systematic follow-up and escalation; approaches explained too complex; ideas-driven requests launched without pre-alignment with OD; requirements that change weekly | Is there a saving project registered per use case; is there a requirements-iteration loop after first delivery; does an open action have an owner and a date |
| **Machine and IT** | Scattered infrastructure; black-box legacy systems; no interoperability; slow feature updates; a system added without a standard machine-integration and interface layer; machines relocated repeatedly; recurring IT issues (reverse proxy and access, unknown cyber-security process for application approval, no update or lifecycle management) | Ticket age (use it as a risk indicator); barrier log (`od-barrier-triage`); layout stability before an integration wave |
| **Environment** | Cyber-security approval that does not integrate with the project; purchasing lead times longer than project timelines; no incident management for operational technology systems | Open approvals and their age; purchase order lead time against the project plan |

## Good-practice and bad-practice signature

Use as a plant-readiness checklist (people, methods, analysis, machines integrated).

| Signature of a plant that realises savings | Signature of a plant that does not |
|---|---|
| Production proactively drives ideas | Production demand unknown |
| The manufacturing engineer asks for blueprints from other plants | A contact "only responsible for the technical part" |
| Requirements are formalised with OD in dedicated meetings | Standards ignored |
| Savings are calculated together with controlling | "We do not know how to calculate savings" |
| Savings are pushed (registered) before the next project wave | Use cases delivered without any measurement of utilisation or saving |

A use case delivered without measurement of utilisation or saving is not "done" (see `od-handover-and-adoption`,
`od-impact-evaluation`).

## Fair comparison

1. Same kind of system landscape, similar machine and integration position, read the same day.
2. Look for the **splitting variable** first (for example who owns the machine programs): compare within segments.
3. Do not read a low change count at a locked site as stability.
4. Do not read a missing record as zero, tracked as proven, or implemented as in use (`od-portfolio-and-savings-analysis`).
5. A hand-registered savings list lags actual work and regional registration is uneven: before concluding "no saving",
   check whether a saving project exists for what is implemented.

## The scaling test (zero-saving use cases)

For a top use case, state three lists: **where it saved**, **where it was deployed without savings**, **where it still
has potential**. A scaled-out use case with deployments but no savings is *further investigation necessary*, not yet
*no potential*: write "to be evaluated until investigated". Only a human (the OD lead with the plant owner) may
decide "no potential"; an agent never writes it. Run the Ishikawa on each "deployed without savings" plant first.

## Output of the diagnosis

One line per gap: branch, cause, evidence (source and date), confidence (stated by the plant / observed in the lists /
inferred), action proposed, owner role. Gaps in the people and method branches usually become roadmap rows with a
call for action; technology gaps may go to `od-barrier-triage` or `od-cross-plant-compatibility`.
