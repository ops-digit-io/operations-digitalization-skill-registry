---
type: Skill Reference
title: Platform and pilot status
description: What the vault records about the manufacturing app store, the container platform and the edge runtime, sorted into running, pilot, planned and design-only, so a deployment is never described as more mature than it is. Open it before you name a target platform.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [project-support-consultancy, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Platform and pilot status

Read 2026-11-05. Sources: the department deck `AI_Where_We_Apply_Today.pptx` (one slide), vault `Graph/Keynote Initiatives` (note "Manufacturing App Store (CMO)" and the notes X2, X3, X4), `Graph/Tools` (Concept 3), `_knowledge/OperationsDigitalization-Department/10-modules/smart-factory-use-case/systems-of-record.md`, and the vault folder `Microservice Apps (WIP)` (17 notes, AI-drafted, not reviewed by a human, generated 2026-09-27).

## The short answer

**The manufacturing app store with GitOps deployment is a pilot.** The only dated, first-hand statement is one line in the department's AI deck: under "MPEE / OD", *"Manufacturing App Store - GitOps deployment (pilot)"*. The same slide marks other lines "live" (AI Manufacturing Dashboards at two plants, in rollout), "building", "PoC" and "initiative", so "pilot" is a deliberate step between a PoC and a rollout. The deck gives no date, no list of plants and no number of apps. Everything below is sorted by how firm its source is.

## What is running, pilot, planned, design-only

| Item | Status | Source and how firm |
|---|---|---|
| IIoT Edge Computing Platform (Concept 3), the plant Kubernetes runtime that apps would run on | **Running.** Rollout status `Available` at 14 plants (tool note, export 2026-08-24); the systems-of-record note says "significantly deployed". The WIP landscape says the edge runtime exists at 16-17 of the 33 plants - not reconciled with the 14 (⟨which count is current⟩, IIAE) | Tool overview records; verified 2026-08-10 |
| Manufacturing apps and dashboards "in the manufacturing app store on the IIoT Edge platform", written by the dev team, per release, data owner OD | **Recorded as the current arrangement** in the systems-of-record note. The release rhythm is not given | Systems of record, last verified 2026-08-10 |
| Manufacturing App Store - GitOps deployment | **Pilot** | AI deck, one line |
| Manufacturing App Store (CMO), initiative X1: a central app marketplace; every plant app delivered as a container with declared interfaces, governance and cyber-security posture; replaces the decentralized "Mendix, VBA, FTP, Windows" collection over 24 to 36 months | **Planned.** Portfolio tier "Big Bet"; business case figures are the authors' own inputs and not verified (the note says so). Validation plan: one process family (25 camera inspection apps), consolidate at least 3 plant-variant apps into one container; pass criterion: cyber-security posture delta positive and maintenance hours delta favourable, and the first 5 plants adopt voluntarily before any mandate | Keynote initiative note; business case |
| Tools named for the app store: a container registry for images, a source-code host for app and deployment-set code, a GitOps tool "available across locations" - stated as enabled in 15 or more locations; a worked example is a LoRaWAN infrastructure app for low-cost sensors distributed to 15 or more locations | **Described** in two initiative decks (2026); archive decks not opened again in this session | Keynote initiative note, archive section (AI-curated) |
| Three onboarding scenarios: internal development; external development with the source owned by the department; external development without source access | **Described** (same decks) | same |
| X4 Cybersec Backlog Closure: every catalogued app through a formal IEC 62443-4-2 conformance gate, coordinated with the CRA enforcement window of 2027; 30 highest-risk apps first, a 90-day clearance sprint, pass criterion "certified or replaced" per app, at least 10 of 30 cleared in the first quarter | **Planned**, tier "Mandatory" | Keynote initiative note |
| X2 AI-coding assimilation: assimilate plant-local apps (Mendix, VBA-Excel chains, internal C# tools) into the catalog: requirements document (X3), container build with declared interfaces, cyber-security check (X4), plant pilot deployment | **Planned**; prerequisites X1, X3, X4 | Keynote initiative note |
| Fifteen domain microservices (ten on the templates, five extension services) and four shared-kernel services as "first tenants" of the app-store catalog | **Design only** (WIP, AI-drafted). Nothing in the notes says any of it is built or deployed | Microservice Apps (WIP) |

Do not describe the app store as "the platform" in a package for a plant. Say **"pilot"** and name the plant or app that is in the pilot if the requester knows it (⟨pilot plants and apps⟩ - OD lead; not in the deck).

## Are the "Container Orchestration Platform" and the IIoT Edge runtime the same thing?

The flow marks "Container Orchestration Platform" as "to confirm". The vault allows a better-grounded answer than the scaffold gave, though not a final one:

- The initiative note calls the app store platform **CMO, Container Management & Orchestration**. This is the nearest match by name to the flow's term.
- The same note lists the **IIoT edge runtime as a prerequisite that is "already deployed"**. The WIP landscape says the services would run "on the edge K8s runtime that already exists" and be "published through the same container registry and GitOps flow".
- So the sources describe **two layers**: the edge runtime (Kubernetes at the plant, Concept 3) is where an app runs; the app store / CMO (registry, source host, GitOps catalog) is how an app gets there. They are related, but they are not the same thing.
- ⟨Whether the flow's "Container Orchestration Platform" means CMO, the edge runtime, or both⟩ stays for the OD lead. Until then, name the target the way the requester does and record both layers in the package (see [../assets/deployment-package.md](../assets/deployment-package.md)).

## What this means for the four sourcing routes of Lane 3a

The three onboarding scenarios of the initiative decks line up with the flow, but the mapping below is **inferred**, not stated:

| Flow route | Nearest onboarding scenario | Note |
|---|---|---|
| 3a.1 Reuse | an app already in the catalog | the catalog is a pilot; check an entry exists |
| 3a.2 Self-developed | internal development | |
| 3a.3 External | external development with the source owned by the department | the department keeps the source in its own source host |
| 3a.4 Integrate foreign app | external development without source access | the only scenario with a closed box; the cyber-security check weighs most |

## Open

- ⟨Release cadence of the app store⟩ - the systems-of-record note says "per release" without a rhythm; the deck gives none.
- ⟨Scope and plants of the GitOps pilot⟩ and ⟨exit criteria of the pilot⟩ - OD lead.
- ⟨Whether the pass criterion of the validation plan (first five plants adopt voluntarily) has been tested⟩ - OD lead.
