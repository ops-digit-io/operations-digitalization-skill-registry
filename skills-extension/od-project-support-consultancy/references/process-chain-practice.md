---
type: Skill Reference
title: Process chain practice
description: Method, decision rules, handoff contract, pitfalls and agent notes for the project-support lane, abstracted from the Operations Digitalization slide decks - project order and plan structure, kick-off workshop, status colours, milestone and closure reports, equipment-integration workshop preparation, wave rules, application consultancy gates, handover lessons. Guidance only, no figures; approved masters come from the register.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [project-support-consultancy, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - project order, kick-off and consultancy

Deck-derived practice for steps 25 and 31 to 33 (project order, requirements, tool decision, capital) and for the lane's happy path. `PROPOSAL` = registry synthesis; `<to confirm>` = decks disagree. The structures below are what the decks show; the approved master of each form is looked up with `od-template-resolution`.

## 1. Method in practice

**Two governance artefacts.** The *project order* is written from the steering committee's perspective; the *project plan* is the kick-off workshop's output, with the project schedule as its second part.

| Project order chapter | Rule |
|---|---|
| History / initial situation | what happened before; stakeholder expectations in the newer variant |
| Requirements: scope, timing, budget | **budget is never left open**, even internally: make an educated guess and label it; timing has at least start, end, first version and the first three milestones |
| Benefit | linked to a concrete use case or capability |
| Good practices and lessons learned | reuse earlier projects; avoid double work |
| Relationship to other projects | anticipate critical areas and synergies |
| Out of scope | written out; avoid grey zones (parallel data sources, pauses, ramp up and down, tool changes) |
| Opportunities and risks | separate lists; probability x impact on scope, timing, financials, quality, as high / medium / low; a high risk needs a treatment reflected in plan and budget; always ask whether team members are available and trained |
| Project organisation | requesting side (steering committee with sponsor) and contracting side (project team with project manager); real roles named, or marked `<...>` |
| Approval | dated; signature, e-sign or e-mail |

Newer variant adds boundary conditions, dependencies and synergies, and an information-classification questionnaire. Not-applicable pages are hidden or moved to the back.

**Kick-off workshop** (about two half-days for a complex project; one day for a low-complexity one): welcome and order recap -> initial situation -> objectives (opportunities and risks, classification, main target, sub-targets, success criteria) -> work breakdown, responsibilities, timing, milestones -> review structure (communication, parking lot, open questions to the steering committee) -> organisation -> approval; wrap-up and workshop assessment.

- **Main target as a 30-second message:** who does what for whom with which intention, phrased "at the end of the project we will have ...".
- **Sub-targets each hold at least three work packages;** more than twelve sub-targets means the granularity is wrong. Success criteria are fixed and agreed by all parties.
- For a standardization project: only plants with the same process work together; collect, compare, derive best practice, then roll out.

**Status and reports.** Milestone report: status colour, milestone plan, objectives, timing, costs (plan, actual accumulated, forecast, difference), the five major risks with countermeasure, owner and due date, lessons learned (topic, experience, proven solution, originator), organisation changes, items for approval (prepared before) and decisions (filled during). Closure report adds a closure checklist including "handover completed yes / no".
Colours: red = out of plan, result endangered, steering decision required; yellow = minor deviation handled by the team with an action; green = per plan (traffic light, one scale per round; "not applicable" or "no data" goes in the comment). The project manager owns the colour and budget within sign-off rules; the steering committee decides on changes.

**One-page initiative sheet** for small initiatives: scope, target, value add, KPIs, savings, actions (kick-off, build, evaluate, closing), lead, team, sponsor, documents location.

**Equipment-integration workshop (preparation checklist):** access to jump hosts and servers (internal and external support); firewall rules in place; platform apps running; physical access to all edge devices including unmounted ones; a priority list with best starting and stopping point; equipment configuration list with technical interfaces. Order of the day: status of priority equipment and IT infrastructure -> project plan and budget -> use-case requirements from production, engineering, operational excellence with examples from other plants -> plant tour -> side topics -> wrap-up. Output: machine list and baseline, use cases per area, IT preconditions, next steps toward the capital request. Production and quality need not attend the hands-on part.

**Wave plan for integration:** plants grouped per quarter; scope bundles (bus, edge platform, aggregation server, connectivity); status as traffic light (red / yellow / green; "input collected", "delayed" or "at risk" only as reason text) before the request is uploaded; the capital request is milestone one of each wave. Recommendation: connect whole processes or areas at once and reuse existing infrastructure.

**Application consultancy** (the step "never built as its own skill"): before an application goes to productive use it needs a business owner, an IT owner, a service concept, roles and responsibilities, demands and requirements, a change process and a risk process. Approval rule: any plant software solution is approved by OD and IT so that data, interface and knowledge domains integrate. Make-or-buy: use cases create demand for tools; use cases determine functions; functions form modules; functions determine interfaces; modules determine make or buy.

## 2. Decision rules

- **Small change versus project.** A small change (a few days of effort, budget available, standard interface) is requested by the local key user in the ticket tool and approved in the change process. Anything larger, needing central budget or a non-standard interface, becomes a project and goes to the governance board with the product owner.
- **Initiative without lead, team, sponsor or document location does not enter routing.** Say so; do not invent one.
- **Time-boxed first step for an unfamiliar field:** fund only the platform or framework for about a year, assess benefit, then decide continuation at minimum cost.
- **Decisions as pairs:** decision - proposal (with limiting conditions such as a time limit) - risk of not doing. State whether alternatives were compared; if no comparison was run, say so and limit the commitment.
- **Cost of non-decision.** For a barrier, plot the holding-back item and the cost of waiting to the decision makers; propose a rapid decision board for holdbacks; keep an error log with a regular review.
- **Operations-concept gate.** No rollout without a named operations owner, service level and support level. Rollout continues only where an operations concept exists.
- **Steering open questions** are often decisive: can budget be used with external suppliers for use-case creation or standardization; can supplier selection for future contracts start.
- **Blocked is steering information,** not a failure to hide. Record the blocking point with its owner and class.

## 3. Handoff contract

| Receives | From |
|---|---|
| decided use case, business case and capital status | `od-benefit-calculation`, `od-capital-request` |
| requirements and tool decision | `od-requirements-breakdown`, `od-system-fit-check` |
| machine list, controller facts | `od-equipment-integration` |

| Hands on | To |
|---|---|
| project order, plan, schedule, milestone and closure reports | steering committee; `od-decision-routing` |
| acceptance-ready solution with the checklist of owners and concepts | `od-acceptance-test` |
| handover record naming plant owner and utilization moment | `od-handover-and-adoption` |
| progress and impact lines | `od-scorecard-reporting` |
| lessons learned | `od-retro` (planned) |

## 4. Pitfalls and lessons

- **Handover between organisations** (a dashboard or data product): the only technical key user left within weeks; no dedicated workspace; the underlying transformation unknown; access outside own control; no run concept; poor data quality. Before accepting a handover require documented transformation, an owned workspace, access control, a named successor, an ETL runbook "in case of trouble", and a continuous requirements funnel (collect always, evaluate and improve periodically).
- **System rollouts that failed at the plant:** old and new processes run in parallel because nobody trusted the new one and nobody was assigned to stop the old one; an unstable rollout team; no shop-floor IT or ERP key-user role, so use-phase responsibilities were unassigned; interface faults and slow supplier reaction; no round-the-clock service.
- **Commercial sequencing:** obtain the offer first (a second quotation where the policy asks), then raise the capital request. A capital request launched before a contract separation was stopped; offer, request and contract versions disagreed; nobody owned purchasing. Before ordering, check that offer = capital request = contract and a named purchasing owner exists.
- **Incomplete capital requests** that deviate from standard templates and frame contracts cause long budget discussions; estimate with a cost calculator before the project.
- **Budget approved at a fraction;** expect staging by approval.
- **Resource and staffing gaps:** rollout intensity limited by plant and central resources.
- **Ownership signals:** no reply to follow-ups for weeks, unclear owner for access, nobody asking why other sites worked, mean a missing owner, not a technical puzzle.
- **Hard external deadlines** (a customer audit, a grant window) outrank internal plans; list them as constraints in the timeline.
- **A migration must not take a customer-facing line down before an audit.**
- **Migration across locations:** scope per location (network, certificates, interfaces, directory, licences); time plan with notice two weeks ahead; per-location checklist with status colour; a verification meeting with key users after cutover; a reserved outage window per location; licence check before moving a server; refresh the service concept per application.
- **Supplier-built app:** requirements are the backlog; the purchase order precedes development; sprints of a few weeks with plan, implementation, review, retrospective; weekly supplier meetings; milestone list from requirements to lessons learned, including security approval and key-user training. Supplier selection: the same agenda for every supplier (demo, feature-solution session on one or two requirement stories, question sheet).
- **Software-defined or AI-built apps:** the path is generated solution -> IT takeover -> security approval; assume supplier code is partly AI-generated.

## 5. Questions to ask and definition of done

What is the main target in thirty seconds? Which sub-targets and work packages? What is out of scope? Who is sponsor, lead and team? What is the budget guess and its basis? Which risks are high and what is the treatment? Who runs it afterwards? Which deadline is external?

**Done for the order:** every chapter filled or marked `<...>`; no empty budget, sponsor or out-of-scope without a flag; approval recorded. **Done for the project:** accepted, handed over with a named plant owner and utilization moment, reported, lessons captured.

## 6. AI agent operating notes

- **Can do:** draft the project order from the initiative sheet and earlier projects, leaving unknowns as `<...>`; flag empty budget, sponsor, owner or out-of-scope before sending to approval; assemble milestone and closure reports from the tracker; walk the demand-management question list and mark unanswered items; prepare the integration-workshop checklist; build the blocker one-pager (technical, commercial, customer sections; three separate deadlines; unowned items) from tickets and mail.
- **Needs:** initiative sheet, tracker export, earlier project orders, read dates.
- **Human gate:** sponsor approval and budget; investment commitment; acceptance sign-off; licensing; Cyber Security sign-off; escalation wording.
- **Must cite:** the earlier project reused for lessons learned and relationships, tracker rows, quotation and contract versions.
- **Hands over:** the order or report with gaps visible; a "cost of non-decision" line only with its source and read date.
