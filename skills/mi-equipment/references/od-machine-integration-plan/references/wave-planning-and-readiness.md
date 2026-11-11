---
type: Skill Reference
title: Wave planning and readiness
description: The scale-known-types rule, wave allocation, the weekly capital-request micro-process, status taxonomy, phase sequence from machine list to flow design, and readiness criteria - process guidance, no figures.
resource: ../procedure.md
status: draft
tags: [information-integration-service, practice]
---
# Wave planning and readiness

## 1. The scale rule

Lesson from an earlier approach: integrating the difficult machines first while plants connected the
easy ones burned reputation and ended the local project. The corrected rule:

1. **Scale out known machine types** (a controller family or machine class with a documented, proven process).
2. **At most one unknown machine type per new deployment.** The unknown type is the learning item; everything else in the wave is routine.
3. **Document the process per controller type** after each deployment and feed it to the integration standard
   (`mi-signals`, `catalog-compatibility`).

How to apply: group the machine list by type (vendor, PLC family, protocol). Mark each type known (a
documented process and at least one success) or unknown. If the wave holds two or more unknown types,
split the wave or move one type to the next wave. A type that is hard and unknown is a barrier-log entry,
not a wave member.

## 2. Wave allocation

- Waves are planned per year, by quarter per plant, with budget, machine list and bundled components (bus, edge platform, central aggregation server, machine connectivity).
- Budget class follows the systems needed (small, medium, large); limits `<look up in the current approval policy>`.
- Eligibility follows request order within quarter and class. Central capacity goes first to first-mover plants that are staffed (a dedicated key user and the preconditions in section 6); fast followers get limited help.
- Wave size depends on the plant's budget class and on whether the IT infrastructure can carry more machines. A plant whose message bus is not complete connects first what it can carry.
- A connectivity budget can be approved while the plant lacks resource or skill. Put a staffing check (resource and skill: good, average, insufficient) into the wave decision.

## 3. The weekly micro-process (per wave)

Three recurring steps per plant, shifted by one calendar week from plant to plant:

1. Call with the local OT expert (machine list, method, preconditions).
2. Prepare the capital request with the local expert (`bc-capital-request`).
3. Upload the request with the local team, then close-loop communication until approval.

The capital request is milestone 1 of each integration wave. Minimum timing for the plan: start, end,
first version, first three milestones. Budget is never left open: make an educated guess.

## 4. Status taxonomy

One traffic-light scale per round (red / yellow / green); no other values.

| Value | Meaning | Action |
|---|---|---|
| green, on track | Phase on plan | None |
| yellow, close-loop update required | Waiting for a reply or document | Chase the named owner this week |
| red, phase delayed | Behind plan | Barrier log; escalate if a decision is missing |

Reasons such as "input collected" (plant delivered list, method, preconditions: prepare the request) or "at risk" (likely to slip: staffing, patch, order) go in the comment text, not in the status value.

Each row carries a call-for-action cell with a calendar week and an owner. The plant's own status
artefact is a checklist of connected versus ongoing equipment per area. In the status meeting ask each
plant for the key processes or equipment to connect, its focus or pain points, and the date by which
equipment and areas must be named so that the next wave request can be launched.

## 5. Phase sequence: machine list to flow design

Machine list (template) -> machine CVs (PLC program, version history, vendor) -> machine integration
guide per core process -> integration plan (hardware and software change per machine) -> rough time and
cost for the capital request -> kick-off with the plant -> initial tag list -> hardware integration ->
software integration (for example a data block in the PLC) -> flow design to the standard base model on
an OPC-UA server -> hand-over, next-wave recommendation, training for self-service.

Roles: the plant provides inputs; the machine-building tool shop is mandatory for own machines and
supports third-party machines; the central integration team leads flow design; execution may be in the
plant or external, decided in planning. Meetings are few in the guide and plan phases and many in the
tag-list and hardware phases: plan plant capacity per phase, not per project. A frame contract with tool
shops waits until the first rollouts have run on fixed-price positions.

Tag list per machine: decide transactional signals, streaming signals, what connected systems need and
what analytics or data-quality loops want. Tag selection follows the documented flow per controller
family; the plant supplies the latest PLC programs and tag lists to the central list.

Prefer whole processes or areas and reuse existing infrastructure. Measurement equipment (inline and
lab) joins the wave where possible, with the lab responsible in the team. Side effects worth recording:
suppliers with poor control of PLC programs surface (an insourcing decision), and PLC naming and
versioning habits start.

## 6. Readiness criteria (test before kick-off or ordering)

| Criterion | Ask |
|---|---|
| Machine list | Complete enough: location, layout, PLC model, program availability, interfaces, network, cyber-security update status |
| Layout stability | Is the area still being rearranged? Repeated relocation delays many machines |
| Controllers | Pending patch or approval that would delay go-live of the second wave? Run the Cyber Security sign-off as a parallel track, started early |
| IT platform | Reverse proxy, disk size, ordering, e-sign, jump hosts, firewall rules, apps running |
| Team | Staffed rollout team, local OT expert, key user; IT and OT assessments scheduled separately; kick-off date fixed |
| Compatibility | Old devices and signals checked before the cost line |
| Operations concept | Who runs it after go-live (`deploy-handover`) |
| Cyber Security path | Documentation package started (`deploy-cybersec`) |
| Unknown types | At most one |

Red on any row: log it in the barrier log with owner and wait state before calling the plan ready.

## 7. Pitfalls

- A patch or approval on installed controllers delays go-live of the second wave and the savings behind it; start the sign-off package early, it runs in parallel.
- Platform rollouts stall on proxy, disk size, ordering and cancelled e-signatures; use a local preparation checklist and an onsite visit.
- Use cases and sprint dates slip because connectivity is unfinished for some machines of a class.
- Connectivity budget approved but no resource: the wave runs late.
- Machine lists not updated: the response to a vulnerability notice is only as fast as the list is complete.
- Integrating an extra system without a standard machine-integration and interface layer yields no benefit.
