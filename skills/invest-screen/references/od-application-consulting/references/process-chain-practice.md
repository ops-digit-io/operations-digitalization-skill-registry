---
type: Skill Reference
title: Process chain practice
description: How the design recommendation is produced at chain steps 32 and 3a4 - build-path questions, supplier-built app practice, supplier selection round, legacy application component assessment, operations-concept precondition, handoffs and agent notes.
resource: ../procedure.md
status: draft
tags: [project-support-consultancy, practice, process-chain, draft]
---
# Process-chain practice - application consulting in the chain

Derived from the Operations Digitalization slide decks (tool, legacy-application, supplier-exchange and strategy decks),
abstracted into process guidance. No figures. `PROPOSAL` = synthesis not stated in a deck; `<...>` = unknown.

## Where it sits in the chain

32 tool decision and IT gate (proposed), 3a4 package or build the app (proposed). Upstream: 31 requirements and
`invest-screen`. Downstream: `deploy-it-demand`, `deploy-appstore`, `deploy-cybersec`, `bc-capital-request`.

## 1 Method in practice

1. **Rule chain for a tool or module.** Use cases create the demand for tools; use cases determine the functions; several
   functions form a module; functions determine the interfaces; the module decides make or buy. Iterate the requirements by
   iterating the use cases, collect candidate suppliers, then prepare pilot sourcing.
2. **Stay inside the standard reference architecture.** New software follows the reference architecture; new use cases use
   existing templates; a legacy system may keep running while Cyber Security assesses it and interface compatibility is assured;
   a prototype outside the standard is allowed only if a path back to the reference architecture exists, it is piloted there once
   benefit shows, and the central functions are informed.
3. **Source ownership decides the effort** (see `build-path-options.md`): internal development is lowest effort and automated;
   an external developer who delivers source works like internal; an external developer without source ownership means image plus
   deployment files only, highest effort. Ask for source ownership in the supplier contract; otherwise accept the highest-effort
   path and its cost in the recommendation.
4. **AI-built applications.** A prompt-to-prototype shows value fast, but the path is: generated solution, IT takeover, Cyber
   Security approval. Assume supplier code is partly AI-generated. A small custom assistant fits when the task is repetitive, the
   skill set is public or general, and internal documentation is good.
5. **Operations concept before a productive use** (the recurring blocker): every application needs a business owner, an IT owner, a
   service concept, roles and responsibilities, a change-management process and a risk process. Put the owner and the support
   level in the recommendation; "who runs it afterwards" is a required field, not a courtesy.
6. **Application approval.** Any plant software solution is approved by OD and IT so that data, interface and knowledge domains
   fit; unapproved plant-local additions repeat the standardisation debt.
7. **Know-how protection items** (for example version control for machine programs): limit the first scope to governance, version
   control and code understanding; defer live shop-floor connection explicitly; settle security, data protection, AI data use and
   purchasing alignment before the purchase.

### Supplier-built app: how it runs

- The backlog is the written requirements; the offer is the input to the purchase order and the purchase order precedes
  development.
- Short sprints, each with plan, implementation, review and retrospective; a weekly supplier meeting; internal testing between
  sprints; strong location support is needed for speed.
- Milestone list: requirements, purchase order, environment set up, installation, configuration, function and integration tests,
  dashboards, key-user training, security approval, go-live and handover, lessons learned.
- Procurement chain for a bought solution: non-disclosure agreement, first quotation round, supplier Q&A and selection, equipment
  request launched and approved, quotation update, second round, sourcing complete, go-live within a fixed window after the order.
- Delivery plan shape: requirement and design first, then admin, operator and management modules, user acceptance test,
  integration test, a longer system test, short production deployment, go-live.

### Supplier selection round (same agenda for every supplier)

A short demo of the standard solution (or a similar manufacturing use case); a feature-solution session on one or two requirement
stories where the supplier explains how it would implement them; advantages and disadvantages for the pilot plant and for
scale-out; a Q&A on a question sheet sent beforehand. Identical agenda keeps the comparison fair. Where no competitive comparison
was run, say so, limit the commitment (time cap, restricted scope), plan the comparison along the work and obtain a quote before
accepting the cost risk.

### Operator-entry apps (downtime example)

The service bus detects gaps but cannot capture reasons; a reason capture needs an extra module with rule-based or manual
detection and a timeout-based status (an undefined status needs a reason). Hybrid capture: record automatically what the PLC
gives, add a standardized reason list owned by an admin for the rest. Check the production structure before accepting a
machine-centred app: where planning works per cell, not per machine, the data model must carry cell, part number, shift and
piece count. Diagnosis questions to put to the plant: is one tablet assigned to several machines; how is a downtime closed
with several machines and operators; which KPIs break if the planning module is not used; is the planning module relevant at
all; what happens when a machine is idle for a whole shift?

### Legacy application: component assessment

Aim at parallel functionality, not a one-to-one replacement. Method: situational briefing; use cases of the application (the
functions that must be preserved become the use-case list); architecture components with the interfaces in focus; impact analysis
per use case; as-is and to-be status of security, service bus, recipe management and MES; wrap-up with a follow-up meeting.
Participants: plant ME and process planning, the original software owner, the central OD, external supplier experts.

Output: situational briefing, key issues, an **explicit "continue as is" scenario with its consequences** (PROPOSAL: mandatory
baseline scenario in every legacy decision package), as-is and target architecture side by side, component tables with function
lists, a risk table per component type (risk, trigger, likelihood), an impact summary (what fails, minimum recovery lead time),
as-is to to-be component mapping, key roles. Rate risk **per component, not per application**.

Recurring risk classes: client software failure, operating-system updates, application updates, interaction of both, complex
interface management, loss of interface knowledge, missing documentation, limited PLC-vendor knowledge, missing security
approval, licence management. Impact classes: production stop, traceability loss, data loss with workaround, convenience loss.
Migration order shown: start with the lowest-risk machine interface, read PLC data through the edge platform, replicate the
existing reporting as the requirement baseline, prepare the MES with the integrator, integrate with minimal downtime, migrate the
rest.

OT application inventory fields (local fills): name and used functions, location, responsible, interfaces (protocol), interfaced
equipment, supplier and its software status, version, security status, network status, production criticality, customer impact,
support concept, licence, number of deployments. OD fills: category, functional mapping to a standard application, scaling
potential. Production criticality: critical (core production, immediate stop, safety or legal, no workaround), moderate
(efficiency or maintenance, workaround exists), minimal (convenience or reporting). The rating is a local human call.

## 2 Decision rules

| Situation | Rule |
|---|---|
| Need fits an existing tool or app | Reuse (3a.1); no build |
| Heavier than the lean footprint | Escalate through `invest-screen`, do not recommend as available |
| Tool has no operations owner or support level | Do not recommend a rollout; escalate as a service gap |
| Tool landscape review | Verdict per tool: continue, stop, stop until condition, substitute with a lightweight one; criteria: deployment scale, rollout cost, missing operations concept, dependence on ERP or platform, licensing |
| Legacy application | Replacement scoped low barrier, high impact first; risk-based prioritisation with evergreening and redeployment through the app store, not a big-bang migration |
| Scale-out of a tool | Gauge value delivery on the current small deployment before widening |

## 3 Handoff contract

- **Receive** from `funnel-requirements` / `invest-screen`: requirement in plain terms, fit verdict with the boundary
  quoted, plant availability dated, data sources per object (one source per object).
- **Hand on**: to `deploy-it-demand` (3a.3, 3a.4: route, owner, front-end parts, open items); to `deploy-appstore` (3a.1, 3a.2:
  sourcing route, owner); to `deploy-cybersec` (data path and components list); to `bc-capital-request` / `bc-cost`
  (cost build-up inputs); to `deploy-handover` (named run owner and support level).

## 4 Pitfalls and lessons

- A design recommendation without a run owner is the most repeated gap; an app handed over with the only technical key user leaving
  within weeks, no dedicated workspace, no documented transformation and access outside own control cannot be accepted. Before
  accepting a handover from another organisation require: documented transformation, owned workspace, access control, named
  successor, runbook for the data flow, a requirements funnel.
- Dongle-bound or single-system lab software: check licence and hardware constraints in the data-availability step.
- Moving data to a new central environment changes every workflow and connection at every location.
- Proof of concept for a machine-program repository: keep the scope to governance; live connectivity is a separate decision that needs
  further security approval.

## 5 Questions to ask and definition of done

Is there a similar app already running at another plant? Which data object is the source and where does it live? Who is the business
owner and the IT owner? Who supports it after go-live? Is source ownership in the contract? What happens if it is not approved?

Done = the recommendation names need, covering tool, build path, data path, gates, run owner, open items, and the "continue as is"
alternative where an existing application is involved.

## 6 AI agent operating notes

- **Can do**: restate the need, match against reference solutions and the legacy list, draft the component inventory from an
  architecture export, draft the risk table from the recurring classes, draft the as-is to to-be mapping, prefill the OT inventory
  fields from supplier pages.
- **Inputs required**: requirement, fit verdict, plant tool availability, legacy list row, supplier documentation.
- **Evidence to cite**: component list source, interface documentation, support status, boundary sentence.
- **Human gates**: the criticality rating (local owner), target architecture, scenario choice, budget, supplier selection, and the
  acceptance of the design (plant and OD lead).
- **Handover**: the design recommendation with open items and owners.
