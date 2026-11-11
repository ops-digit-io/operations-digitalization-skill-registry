---
type: Skill Reference
title: Routing and handoff
description: How the object profile becomes a route signal at chain steps 1b1, 22, 32 and 3b4 - decision rules, the handoff contract with neighbouring skills, pitfalls, questions to ask and the definition of done.
resource: ../procedure.md
status: draft
owner: human:jakob.gabriel
tags: [practice, maturity, routing, process-chain, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Routing and handoff - the profile as a signal, not a verdict

All rules below are `PROPOSAL`: the knowledge base gives the model, the rubric and the target guidance; the mapping onto the route decisions is this
skill's synthesis, to be confirmed with the OD lead (`<to confirm>`). A signal is evidence for the neighbouring skill, which owns the verdict;
quote the rule with the signal.

## 1 Route signals per step

### 1b1 Pick the use case and the standard system (machine not connected)

| Profile | Signal | Hand to |
|---|---|---|
| F9 at least cable, F10 at least proprietary with a known connector, F1 for assets at least 3 | A standard system can be matched; proceed to the kit pick | `catalog-usecase`, then `od-equipment-integration` |
| F9 not networked or no usable drop | The kit cannot be fitted yet; a connection prerequisite is missing | `od-equipment-integration` (legacy hardware or information class) |
| F10 level 1 or 2 with no connector on the fallback ladder | No route; substitution or roadmap question | `od-equipment-integration` |
| Many `unknown` on F9, F10, F2 | Information gap; do not match a kit on assumptions | the plant ME to fill the Machine List fields |

### 22 Features and data check (new use case on a connected machine)

| Profile | Signal | Hand to |
|---|---|---|
| Source object F11 below the level the use case needs (real-time for a within-shift decision) | Data gap, not an app problem | `od-data-availability-check` |
| F16 level 1 on the signals the use case joins | Connected but not standardized | `od-signal-standardization` |
| F1 level 2 where the use case needs per-part or per-asset joins | Identity gap; plan the registry or the ID capture first | `od-use-case-solution-evaluation`, owner named |
| F14 requested at predictive or prescriptive while the source sits at descriptive or below | Out of order; reporting and data model first | `od-use-case-solution-evaluation` (over-engineered or capability first) |
| Profile as-is per area complete with evidence | Input for the gap analysis | `od-use-case-solution-evaluation` (as-is levels per candidate area) |

### 32 Tool decision and IT gate (system or application)

Rate the requested or existing system on the areas that describe it (F2, F10, F12, F13, F15, F16, F1, F7, F8; F4 to F6 usually `n/a`).

| Profile | Signal | Hand to |
|---|---|---|
| The asked function is order or recipe execution, sequencing, genealogy, material validation (F15 central control territory) | MES-shaped need, whatever the request calls it | `od-system-fit-check` (escalate unless a lighter tool covers it) |
| An existing plant-local application with F10 proprietary and F16 level 1 | Integration costs a mapping per interface; compare with replace | `od-system-fit-check` (integrate, keep or replace) |
| An existing application with F12 central only and a traceability or high-rate demand | Data lost on outage; edge needed in front of it | `od-system-fit-check` (data path) |
| Application with F10 open standard, F16 at least 2, a named owner and support level | Cheap to integrate; reuse or integrate foreign app is plausible | `od-system-fit-check` (build path) |
| Application with no named business owner, IT owner and support level | Service gap, not a profile question | `od-system-fit-check` (operations-concept precondition), `od-decision-routing` |

### 3b4 Connector and pipeline (new machine)

| Profile | Signal | Hand to |
|---|---|---|
| F10 standard protocol, F2 at least active | OPC UA or equivalent route; configure, do not build | `od-equipment-integration` |
| F10 proprietary, F2 passive | Vendor connector or file drop; a gateway turns polling into events; name its owner | `od-equipment-integration`, `od-equipment-integration` |
| F12 central only on a machine with high-rate or traceability signals | Edge device rather than plain client | `od-equipment-integration` (edge versus plain connection rule in `od-system-fit-check`) |
| F16 level 1 | Signal standard before pipeline | `od-signal-standardization` |
| Several machines of one type with the same profile | One connector and one standard for the type | `od-equipment-integration` (scale known types) |
| Ordering a new machine | Write F10 standard protocol and F2 active into the specification | `od-requirements-breakdown`, procurement route of `od-equipment-integration` |

## 2 Decision rules

- **Profile first, route second.** Never choose a kit, tool or connector before the profile exists for the question; never rate to fit a route.
- **Need before level.** A level is a gap only against a named need. As-is below the top is the normal case.
- **Stop at the first missing prerequisite.** The route is decided by the lowest unmet area on the backbone (connectivity, identity, protocol,
  model, real time), not by the area the request talks about.
- **Unknown blocks, assumed warns.** `unknown` on a decisive area stops the route signal and creates a question with an owner; `A` evidence may
  be used to open a question only.
- **Group before you repeat.** Objects of one type with the same profile share one record and one route; list the exceptions.
- **A high-level claim without its prerequisites is a question**, not a finding (plausibility table in `drivers-and-dependencies.md`).

## 3 Handoff contract

| Receive | From | Must contain |
|---|---|---|
| Object and question | `od-use-case-intake-triage`, `od-requirements-breakdown`, `od-equipment-integration`, `od-system-fit-check` | The object (machine, system or application), the plant, the question the profile serves, the use case or request behind it, the Machine List, tool or legacy-list row |
| Hand on: profile | `od-use-case-solution-evaluation`, `od-data-availability-check`, `od-system-fit-check`, `od-system-fit-check`, `od-equipment-integration`, `od-equipment-integration` | Per area: level or `unknown` or `n/a`, evidence grade, source and date, owner role; the open unknowns |
| Hand on: drivers and gaps | `od-use-case-solution-evaluation` (targets and verdict), `od-equipment-integration` (sequence) | Driver ratings with both raters, candidate areas, gap chain with prerequisites and named need |
| Hand on: stalled route | `od-equipment-integration` | The unmet prerequisite on the backbone and the evidence for it, so the class is not re-derived |

The record is filed with the object. Anyone who needs the same object later reads it first, checks the date and refreshes only the areas that
changed.

## 4 Pitfalls and lessons

- **Rating the brochure.** The data sheet says a protocol is supported; the machine runs the proprietary one. Rate use, mark potential.
- **Averaging a mixed object.** One cell with new and old machines is not "level 2.5"; split it.
- **Mistaking the plant's best machine for the type.** One well-connected line says nothing about the next machine; the profile is per object or
  type, never per plant.
- **Self-assessment of one person.** The plant-side owner and the IT/OT side see different things; independent ratings then reconciliation.
- **Treating the top of the scale as the goal.** The over-engineering failure of earlier integration waves is the central warning of the source;
  assist before decide, combined before embedded.
- **Reading the literature as a benchmark.** The source's case distributions are research and pilot cases; they say what was described, not what is
  typical (`model-caveats.md`).
- **Maturity for its own sake.** A raised level with no use case, owner and business case is not a plan.
- **A profile gone stale.** Firmware, retrofit, rollout state and tool status change; date every rating.

## 5 Questions to ask and definition of done

- Which decision does this profile serve, and who takes it? What is the use case or request behind it?
- Which areas could the interviewee not answer, and who can?
- What is seen (S) and what is only told (T) or assumed (A)?
- Which drivers are high or dominant, rated by whom?
- Which prerequisite is the lowest unmet one on the backbone?

Done = object and question stated; the areas relevant to the object rated with level, evidence grade, source and date, or marked `n/a` or
`unknown` with an owner; plausibility checked; drivers rated by two raters and candidate areas listed; the gap chain tied to a need, an owner
role and a skill; the route signal written with its rule quoted; the record filed with the object; the human gate named.
