---
name: od-migration-cutover
description: >-
  Plan and run the migration of a legacy shop-floor application, server, middleware or platform to the
  target platform, location by location - as-is/to-be canvas, per-component risk and recovery-impact
  tables, OT application inventory with production-criticality and customer-impact ratings, staged
  migration, per-location checklist with RAG, key-user verification, outage window, parallel run, back-out
  plan and decommissioning. Use when a plant-local application or middleware is to be replaced or retired,
  a server or virtual machine moves, a platform changes across plants, or someone asks "what happens to the
  old system, and how do we get back if the cutover fails".
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-migration-cutover
  tier: practice
  lane: lane-3
  new_state_lane: "Extension, deepens Lane 3 front-end (32), Lane 3a (3a5, 3a6)"
  new_state_step: "Tool-decision / IT-footprint gate (make, buy, integrate or connect); Deploy to the platform, acceptance, Cyber Security sign-off; Rollout and adoption; ownership on formal acceptance"
  owner_role: human:jakob.gabriel
  authority_level: draft the assessment, the migration plan, the checklists and the back-out plan; recommend sequencing; the cutover, the back-out decision, Cyber Security sign-off and decommissioning are human
  status: draft
  origin: plan-draft
  sources_read: 2026-11-05
  requires: [dept-os]
  composes: [invest-screen, od-cybersec-gate, od-acceptance-test, od-handover-and-adoption, funnel-requirements, od-decision-routing, od-risk-watch, od-plant-onboarding, deploy-appstore]
  derived_from:
    - Operations Digitalization slide decks (legacy-application assessment and migration workshops, platform and server migration across plants, middleware retirement, back-out plan diagrams), abstracted into process guidance; no figures.
  okf:
    type: Agent Skill
    title: Migration and cutover
    tags: [migration, cutover, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Migration and cutover

Read `dept-os` first.

No existing skill owns the move itself. `invest-screen` and `invest-screen` decide
*whether* to replace, integrate or keep an application; `od-cybersec-gate` decides whether the target may go
live; `od-acceptance-test` proves it works; `od-handover-and-adoption` hands it to the operating model. This
skill sits between them: it turns "replace it" into an inventory, a risk-rated plan, a staged cutover
per location, a way back, and a retirement of the old thing.

Provenance: the assessment and per-location parts come from workshop and migration decks. The **back-out plan
content is a `PROPOSAL`**: the decks hold only diagrams of who does what, no content. Everything marked
`PROPOSAL` is synthesis, to be confirmed by the owner of the back-out process.

## Purpose and definition of done

Done when, for one migration:

- every component and interface of the old system is inventoried and each use case it serves is listed as "must be preserved", "can be dropped" or "replace later";
- each component has a risk row and a recovery-impact class; each OT application has a production-criticality and customer-impact rating **confirmed by its local owner**;
- the plan is staged (lowest-risk first), each stage with resources, cost, risk and an exit criterion;
- each location has a checklist with RAG, a communicated time plan, an outage window and a key-user verification meeting;
- a back-out plan exists per stage and was read by the people who would execute it;
- "continue as-is" is written down as a baseline scenario with its consequences;
- the old system is switched off by a named person, its server released and the application list updated; no parallel paper or shadow system remains.

## Where it sits in the chain

| Step | Role of this skill |
|---|---|
| 31 / 32 (`funnel-requirements`, `invest-screen`, `od-decision-routing`) | Receives the "replace or integrate" decision and the use-case list of the old system; adds the component assessment when the case is a legacy application |
| 3a4 / 3a5 (`it-demand-package`, `deploy-appstore`, `od-cybersec-gate`, `od-acceptance-test`) | Plans the migration stages and back-out; the target is deployed and signed off on this path |
| 3a6 (`od-handover-and-adoption`, `od-rollout-training`) | Per-location cutover, parallel run, key-user verification, then decommissioning; hands the operating model over |
| Spine (`od-plant-onboarding`, `od-risk-watch`) | A platform or server migration across plants runs as a series of per-location cutovers; risks are watched through `od-risk-watch` |

## References and assets

| File | Use it for |
|---|---|
| [`references/assessment-canvas-and-risk.md`](references/assessment-canvas-and-risk.md) | The workshop pattern, the as-is/to-be canvas, the component inventory, the per-component risk and recovery-impact tables, the OT application inventory and both qualitative rubrics |
| [`references/staged-migration-and-cutover.md`](references/staged-migration-and-cutover.md) | Staging logic, preconditions, per-location checklist and RAG, outage window, key-user verification, parallel run, licence check, middleware retirement flow, decommissioning, pitfalls |
| [`references/backout-plan-proposal.md`](references/backout-plan-proposal.md) | `PROPOSAL`: the structure of a back-out plan, its triggers, the points of no return and the rehearsal |
| [`assets/migration-assessment.md`](assets/migration-assessment.md) | Canvas, inventory, risk and impact tables, target mapping, staged plan |
| [`assets/cutover-checklist-and-backout.md`](assets/cutover-checklist-and-backout.md) | Per-location checklist with RAG, verification record, back-out plan, decommissioning record |

## Procedure

1. **Frame and decide the scenario.** Take the decision from `invest-screen` / `invest-screen` (replace, integrate, keep). Write the scenario list with **"continue as-is"** as a mandatory baseline and its consequences (security issues, patch and compatibility problems, loss of know-how, expiring support). `PROPOSAL`: no decision package without that baseline.
2. **Assess.** Run the assessment workshop or desk assessment (reference 1): use cases of the old system, component inventory focused on interfaces, impact per use case, as-is/to-be status of security, bus, recipe management and MES where relevant. For an application estate, fill the OT application inventory and rate it.
3. **Rate risk and recovery impact** per component; map each as-is component to its to-be component.
4. **Stage the migration.** Start with the lowest-risk machine or location; replicate the existing reporting on the new platform as the requirement baseline; move the high-impact component last and with minimal downtime. Aim at parallel functionality, not a one-to-one copy; "low barrier, high impact" first.
5. **Check preconditions** (artifact registry, source-code host, firewall changes, cloud-system approval, licences, security approval) before any stage starts. Missing ones are the first blockers, not later surprises.
6. **Plan per location**: scope assessment by the central server team with the application owner, time plan, announcement two weeks ahead, outage window, checklist with RAG, key-user meeting.
7. **Write the back-out plan** per stage (reference 3) and agree its trigger and decision owner before the outage window opens.
8. **Cut over** (human-executed), verify with the key users item by item, then run the old and new side by side only as long as the plan says, with a named person who stops the old process.
9. **Hand over and retire**: operating model and service concept to `od-handover-and-adoption`; then decommission (uninstall request, VM released, application list updated).

## Decision rules

- **Go for the cutover** only when preconditions are met, the back-out plan exists and was read, the outage window is announced, and the key user for that location is available.
- **Hold** if a customer audit or similar fixed external deadline falls near: a migration must not take a customer-facing line down before it. Fixed external deadlines outrank internal plans.
- **Do not migrate big-bang** a high-impact application; prefer risk-based prioritisation, evergreening or redeployment of the application to the target app platform, staged.
- **Hardest case**: a "new installation" location without a legacy baseline is a special site; plan extra time and support.
- **Missing ownership is the signal**, not a technical puzzle: no reply to follow-ups, nobody owns access to a registry, nobody asks why other sites worked. Ask who is responsible for the connection, what the other sites do, and what the alternative is if it never works.
- If the old stack carries customer-driven projects, a migration that pauses it stops benefits and use-case development at once: treat the pause as a cost in the plan.

## Handoff contract

| Receives | From |
|---|---|
| Replace / integrate / keep decision, use-case list of the old system | `invest-screen`, `invest-screen`, `funnel-requirements` |
| Target architecture and security status | `invest-screen`, `od-cybersec-gate` |
| Application and interface lists, machines concerned | plant ME, local owner, application list |

| Hands on | To |
|---|---|
| Deployment package and back-out plan for the target | `deploy-appstore`, `od-cybersec-gate` |
| Per-location verification list and test evidence | `od-acceptance-test` |
| Service concept, roles, retire-the-old-process owner, adoption checks | `od-handover-and-adoption` |
| Open risks, blocked locations | `od-risk-watch`, `od-decision-routing` |

## Questions to ask

- Which additional interfaces exist (for example a laboratory)? Who actually uses the recorded data?
- Does the current reporting need heavy manual correction? Capture the plant's wording verbatim; derive the requirement (for example automatic break and shift-end detection).
- If the old system is kept, what happens, and when does support end?
- Which software lives on the same machine (aggregation server, other tools) and does it stay?
- Which runtime licences are bound to one machine, and is the key available?
- Is any customer audit, shutdown or fixed external date near the window?

## AI agent operating notes

An agent can: inventory components from architecture exports and interface documentation; pre-fill application description, category and functional mapping from supplier pages; generate risk tables from the recurring risk classes; draft the as-is to-be mapping, the staged plan, the per-location checklist and the communication text; track checklist RAG and chase open items; list unknown flows or applications.

Required inputs: architecture or application list, interface documentation, support and licence status, the replace/integrate/keep decision.

**Human gates:** the local owner confirms every production-criticality and customer-impact rating; the OD lead and plant decide the target architecture, the scenario, budget and the staging; Cyber Security sign-off is human-only; the cutover, the back-out decision and the decommissioning are executed and approved by people. An agent never runs a migration, changes a firewall or system, or switches anything off.

Evidence to cite: source of the component list, interface documentation, support status, licence model, date of the key-user confirmation. Mark unknown as `<...>`; do not infer a rating. Hand over as the filled assets plus an open-items list per location.

## Still open

- `<Back-out plan content>`: owner and form of the existing back-out process; the structure here is a proposal.
- `<Lead times>` for security approval and purchasing: called longer than project timelines, no number in the sources.
- `<Who decides a back-out>` per platform component: the decks show two actors (central IT, central engineering) only.
- `<Whether the plant or the central server team owns the outage window>`.

## Do not

- Do not give a rating, a RAG status or a sign-off the owner has not confirmed.
- Do not start a stage before preconditions and the back-out plan exist.
- Do not take a customer-facing line down before a customer audit.
- Do not leave old and new systems, or paper, running in parallel without an end date and an owner for stopping the old one.
- Do not decommission before key-user verification and an agreed observation period.
- Do not put counts, spend, per-plant statuses or dates of the real estate into the assets; keep them as `<fields>`.
