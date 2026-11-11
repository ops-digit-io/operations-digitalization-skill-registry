---
type: Skill Reference
title: IT touchpoints
description: What the knowledge base records about where OD meets IT - the rule for which demands go through demand management, the asks OD has put to IT per initiative (by role), the IT roles of the platform operations concept, and what stays unknown. Open it before you write the IT-facing part of a package.
resource: ../procedure.md
status: draft
tags: [all, practice]
---
# IT touchpoints

Sources, read 2026-11-05: bundle notes `Decision rights`, `Operating model` and `Roles and organization` (`_knowledge/10-Department`); `00-core/08-decision-rights.md`; the department deck `AI_Initiatives_IT_Contact_Points.pptx` (one slide, text extracted); knowledge base `Graph/Keynote Initiatives`; knowledge base `Graph/Tools`, note "Concept 3 - IIoT Edge Computing Platform" (archive section on the platform operations concept); skills `od-decision-routing`, `od-requirements-breakdown`. Roles only; no names.

## When a demand belongs here

| Rule | Source |
|---|---|
| Requests that need something from IT go through **IT demand management** with a demand evaluation board; this is the route for anything touching a platform the function does not own | `Decision rights`, section Demand |
| The function does not own the ERP or the core systems; a change there goes through the demand and investment routes | `Operating model`, "What it does not do" |
| IT means "platforms, data access and the demand route"; the function does not run platforms | `Roles and organization` |
| Spend is a separate gate (eCR; approver per the current approval policy, look up: `od-decision-routing` and the OD lead) and can run in parallel; the package should name it, not replace it | `Decision rights`, section Spend; `od-decision-routing` |
| Tool or system rollout (MES, MSB, IIoT Edge, the data platform) is an OD lead decision, taken in tandem with the IT-responsible role of the business side | `08-decision-rights.md` |

A demand that stays inside platforms OD owns or operates with its own tools does not need this package.

## The asks OD has put to IT

The department deck "AI Initiatives - IT contact points and asks" is a single pitch slide listing, per initiative, what
OD asks of IT. Re-open it before quoting, because the asks change. Do not copy its licence counts or targets. By kind:

| Kind of ask | What it looks like |
|---|---|
| Licences and budget | an initiative depends on IT licences and needs a per-head budget defined |
| Platform integration | an initiative needs deeper integration with the data platform |
| Capacity | more DevOps capacity for concept implementation or backlog closure |
| Tool consolidation | consolidation of legacy tools |
| Delivery predictability | faster and more predictable execution by the Business Applications function |

What the slide shows, and what a package can use from it:

- IT asks come in a few kinds: **licences or budget**, **platform integration**, **capacity**. A package should say which kind each of its items is, so the board can place it.
- The deck names a *function* (for example Business Applications) for one ask, and the data platform for another; it names **no contact person or mailbox**. ⟨The IT contact for each kind of ask⟩ - OD lead.
- The slide is a pitch slide, not a form. It does not say what IT requires of a demand.

## IT roles in the platform operations concept

The archive deck on the IIoT and edge platform operations concept (recorded in the Concept 3 tool note, AI-curated link) defines a **Local Key User, BA/BU Key User, Governance Board, Central Key User, Divisional Engineering Support, Divisional IT, Local IT and an IT AMS / platform service provider**, each with operational and project responsibilities, plus incident, change and security-incident flows. It separates:

- a **Divisional Standard** application: global IT application management support;
- a **local or BU application**: no IT application management support, only local IT infrastructure;
- and says interfaces between the two need **governance-board approval**.

Use: for route 3a.4 the first question to the requester is whether the foreign app is a divisional standard or a local application, because that decides who supports it and whether an interface needs the governance board. Open the concept deck before relying on this summary (the Concept 3 note cites the relevant slides).

## Initiatives that lean on IT

From `Graph/Keynote Initiatives` (read live; the notes' value figures are the authors' own inputs and are not repeated). The
initiatives (X1 to X4: a manufacturing app store, AI-coding assimilation, an AI requirements engineering pipeline, closure
of the cybersecurity backlog) each state IT-side prerequisites. The kinds of dependency to look for:

| Initiative | Kind of IT-side dependency stated |
|---|---|
| X1 Manufacturing App Store | an edge runtime already deployed; sibling initiatives funded in parallel; one process family pilot; the key risk is plants accepting central orchestration of plant-level tools. Mitigation named: start from the cyber-security obligation rather than the value argument |
| X2 AI-coding assimilation | assimilate plant-local apps into the catalog with a cyber-security check per app; hardened development environment with container guardrails |
| X3 AI requirements engineering pipeline | requirements database in place; a pilot onboarding flow; output usable downstream without heavy rework |
| X4 Cybersec backlog closure | regional cyber-security capacity; plant change-process documentation; the highest-risk apps identified first |

If a demand is a camera, quality, SCADA or custom MES application in the legacy list, it probably sits inside the X1/X2/X4 chain; say so in the package so the board does not treat it as a one-off.

## Where a demand typically waits (recurring patterns)

- Platform access: machines stay unintegrated while access to the aggregation server is open; this works as a technical follow-up with Central IT, never a governance-forum item (`od-decision-routing`, escalation worked examples). Lesson: name Central IT or Plant IT as the unblocking role in the package.
- Unknown licence: many legacy applications have an unknown licence status (see [../../catalog-usecase/references/legacy-application-position.md](../../../../catalog-usecase/references/legacy-application-position.md))); a demand that rests on one has a licence dependency with a lead time. Count the unknowns live before quoting.
- MES: a rollout that is on hold or ERP-dependent blocks a demand that depends on it; the demand is blocked, not planned (`od-requirements-breakdown`).

## Open

- ⟨IT's demand form fields⟩, ⟨the evaluation board's criteria and rhythm⟩ and ⟨the usual lead time⟩ - not in any source read. The deck, the bundle and the knowledge base carry the *route*, not the form. Owner: OD lead, with the IT demand management contact.
- ⟨The IT contact in demand management⟩ - no source names a role or a mailbox for it.
