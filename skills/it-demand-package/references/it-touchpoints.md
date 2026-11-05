---
type: Skill Reference
title: IT touchpoints
description: What the vault records about where OD meets IT - the rule for which demands go through demand management, the asks OD has put to IT per initiative (by role), the IT roles of the platform operations concept, and what stays unknown. Open it before you write the IT-facing part of a package.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# IT touchpoints

Sources, read 2026-11-05: bundle notes `Decision rights`, `Operating model` and `Roles and organization` (`_knowledge/10-Department`); `00-core/08-decision-rights.md`; the department deck `AI_Initiatives_IT_Contact_Points.pptx` (one slide, text extracted); vault `Graph/Keynote Initiatives`; vault `Graph/Tools`, note "Concept 3 - IIoT Edge Computing Platform" (archive section on the platform operations concept); skills `od-decision-routing`, `od-requirements-breakdown`. Roles only; no names.

## When a demand belongs here

| Rule | Source |
|---|---|
| Requests that need something from IT go through **IT demand management** with a demand evaluation board; this is the route for anything touching a platform the function does not own | `Decision rights`, section Demand |
| The function does not own the ERP or the core systems; a change there goes through the demand and investment routes | `Operating model`, "What it does not do" |
| IT means "platforms, data access and the demand route"; the function does not run platforms | `Roles and organization` |
| Spend is a separate gate (eCR; the record says CTO approves up to EUR 150k and the Board above EUR 75k, a ladder not alternatives) and can run in parallel; the package should name it, not replace it | `Decision rights`, section Spend; `od-decision-routing` |
| Tool or system rollout (MES, MSB, IIoT Edge, the data platform) is an OD lead decision with ⟨counterpart to confirm⟩ | `08-decision-rights.md` |

A demand that stays inside platforms OD owns or operates with its own tools does not need this package.

## The asks OD has put to IT (the deck "AI Initiatives - IT contact points and asks")

One slide, five rows, no date and no names. Reproduced by role and kind of ask:

| Initiative | Ask to IT | Kind of ask |
|---|---|---|
| Department OS | depend on IT licences - currently 2, target 10 (marked with a question mark in the deck itself); define a per-head budget | licences and budget |
| GenAI Manufacturing Dashboards | deeper integration with the data platform | platform integration |
| Shopfloor AI | more DevOps capacity for concept implementation | capacity |
| Cybersecurity backlog | consolidation of legacy tools; more DevOps capacity | tool consolidation, capacity |
| Gemba App | faster and more predictable execution by Business Applications | delivery predictability |

What the slide shows, and what a package can use from it:

- IT asks come in three kinds: **licences or budget**, **platform integration**, **capacity**. A package should say which kind each of its items is, so the board can place it.
- The deck names a *function* ("Business Applications") for one ask, and the data platform for another; it names **no contact person or mailbox**. ⟨The IT contact for each kind of ask⟩ - OD lead.
- The slide is a pitch slide, not a form. It does not say what IT requires of a demand.

## IT roles in the platform operations concept

The archive deck on the IIoT and edge platform operations concept (recorded in the Concept 3 tool note, AI-curated link) defines a **Local Key User, BA/BU Key User, Governance Board, Central Key User, Divisional Engineering Support, Divisional IT, Local IT and an IT AMS / platform service provider**, each with operational and project responsibilities, plus incident, change and security-incident flows. It separates:

- a **Divisional Standard** application: global IT application management support;
- a **local or BU application**: no IT application management support, only local IT infrastructure;
- and says interfaces between the two need **governance-board approval**.

Use: for route 3a.4 the first question to the requester is whether the foreign app is a divisional standard or a local application, because that decides who supports it and whether an interface needs the governance board. The concept deck itself was not re-opened in this session; open it before relying on it (the Concept 3 note cites its slides 2-3 and 5-15).

## Initiatives that lean on IT

From `Graph/Keynote Initiatives` (descriptions and prerequisites only; the notes' value figures are the authors' own inputs and are not repeated):

| Initiative | IT-side dependency stated |
|---|---|
| X1 Manufacturing App Store (CMO) | prerequisites: the IIoT edge runtime already deployed; X3 and X4 funded in parallel; one process family pilot. Key risk: all plants accepting central orchestration of plant-level tools. Mitigation named: start from the cyber-security obligation rather than the value argument |
| X2 AI-coding assimilation | assimilate plant-local apps into the catalog with a cyber-security check (X4) per app; hardened development environment with container guardrails |
| X3 AI requirements engineering pipeline | requirements database in place; one pilot onboarding flow; the output must be usable downstream without heavy rework |
| X4 Cybersec backlog closure | regional cyber-security capacity; plant change-process documentation; 30 highest-risk apps identified |

If a demand is a camera, quality, SCADA or custom MES application in the legacy list, it probably sits inside the X1/X2/X4 chain; say so in the package so the board does not treat it as a one-off.

## Where a demand typically waits (recorded cases)

- Platform access: 0 of 10 machines integrated at one plant while the access to the aggregation server was open; worked as a technical follow-up with Central IT, never an ODEC item (`od-decision-routing`, escalation worked examples). Lesson: name Central IT or Plant IT as the unblocking role in the package.
- Unknown licence: 128 of 268 legacy applications (see [../../catalog-systems/references/legacy-application-position.md](../../catalog-systems/references/legacy-application-position.md)); a demand that rests on one has a licence dependency with a lead time.
- MES: rollout on hold, ERP-dependent; a demand that depends on it is blocked, not planned (`od-requirements-breakdown`).

## Open

- ⟨IT's demand form fields⟩, ⟨the evaluation board's criteria and rhythm⟩ and ⟨the usual lead time⟩ - not in any source read. The deck, the bundle and the vault carry the *route*, not the form. Owner: OD lead, with the IT demand management contact.
- ⟨The IT contact in demand management⟩ - no source names a role or a mailbox for it.
- ⟨Who is the counterpart of the OD lead for tool and system rollout decisions⟩ - `08-decision-rights.md` leaves it open.
