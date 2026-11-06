---
type: Skill Reference
title: Platform and pilot status
description: How to classify the manufacturing app store, the container platform and the edge runtime as running, pilot, planned or design-only, where to look the current status up, and how the two platform layers relate - guidance only, no status snapshot. Open it before you name a target platform.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [project-support-consultancy, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Platform and pilot status

Sources to read for the *current* picture (this file does not copy their content): the department deck
`AI_Where_We_Apply_Today.pptx` (the "MPEE / OD" slide), vault `Graph/Keynote Initiatives` (note "Manufacturing App Store (CMO)" and the
notes X2, X3, X4), `Graph/Tools` (Concept 3), `_knowledge/OperationsDigitalization-Department/10-modules/smart-factory-use-case/systems-of-record.md`,
and the vault folder `Microservice Apps (WIP)` (AI-drafted, not reviewed by a human). Note each source's own date when you quote it.

## The rule

**A deployment is never described as more mature than its source says.** Classify every element on this ladder, using the
firmest source available, and say which source:

| Level | Meaning | What counts as evidence |
|---|---|---|
| **Running** | In use at plants | A tool-overview record with an `Available` rollout status, or an owner's dated statement |
| **Recorded as current arrangement** | The systems-of-record module states it as how things work | The module's text and its `last-verified` date |
| **Pilot** | A deliberate step between a PoC and a rollout | A dated first-hand statement (the department AI deck marks lines "live", "building", "PoC", "pilot", "initiative" - read the label, not the headline) |
| **Planned** | An initiative with a tier and a validation plan, not yet built | The keynote initiative note; its business-case inputs are the authors' own and unverified unless the note says otherwise |
| **Described** | Written up in initiative decks but not confirmed | The decks; re-open the archive deck before relying on it |
| **Design only** | WIP notes, AI-drafted, nothing says it is built or deployed | The Microservice Apps (WIP) folder |

Typical placement (re-check before quoting): the IIoT edge runtime (Concept 3, the plant Kubernetes runtime) is **running**, but plant
counts differ between sources (tool overview versus the WIP landscape) - state the source and mark `⟨which count is current⟩` for the IIAE
instead of picking one. The manufacturing app store with GitOps deployment is a **pilot**; the wider app-store initiative (CMO) is **planned**;
the microservice landscape that would use it is **design only**. The deck gives no plant list, so name the pilot plant or app only if the
requester knows it (`⟨pilot plants and apps⟩` - OD lead).

Initiative notes also describe, qualitatively: a central app marketplace where every plant app is delivered as a container with
declared interfaces, governance and cyber-security posture, replacing a decentralized collection of ad-hoc tools; a validation plan built on
one process family, consolidation of plant-variant apps into one container, and voluntary adoption by early plants before any mandate;
a cyber-security backlog-closure initiative sending every catalogued app through a formal IEC 62443-4-2 conformance gate (coordinated with the
EU Cyber Resilience Act enforcement window), highest-risk apps first; and an AI-coding assimilation initiative that brings plant-local apps
into the catalog (requirements document, container build with declared interfaces, cyber-security check, plant pilot). Read the initiative
notes for their current scope, sizing and criteria; do not quote them from memory.

Do not describe the app store as "the platform" in a package for a plant. Say **"pilot"** where that is the level.

## "Container Orchestration Platform" and the IIoT Edge runtime

The flow's term "Container Orchestration Platform" means the edge runtime of the IIoT Edge platform (Concept 3); use both terms as synonyms. The sources describe two layers:

- The initiative note calls the app store platform **CMO, Container Management & Orchestration** (registry, source host, GitOps catalog).
- The same note lists the **IIoT edge runtime as a prerequisite that is "already deployed"**. The WIP landscape says the services would run "on the edge K8s runtime that already exists" and be "published through the same container registry and GitOps flow".
- So there are **two layers**: the edge runtime (Kubernetes at the plant, Concept 3; the "Container Orchestration Platform") is where an app runs; the app store / CMO is how an app gets there. Record both layers in the package (see [../assets/deployment-package.md](../assets/deployment-package.md)).

## What this means for the four sourcing routes of Lane 3a

The three onboarding scenarios of the initiative decks (internal development; external development with the source owned by the department;
external development without source access) line up with the flow, but the mapping below is **inferred**, not stated:

| Flow route | Nearest onboarding scenario | Note |
|---|---|---|
| 3a.1 Reuse | an app already in the catalog | the catalog is a pilot; check an entry exists |
| 3a.2 Self-developed | internal development | |
| 3a.3 External | external development with the source owned by the department | the department keeps the source in its own source host |
| 3a.4 Integrate foreign app | external development without source access | the only scenario with a closed box; the cyber-security check weighs most |

## Open

- ⟨Release cadence of the app store⟩ - the systems-of-record note says "per release" without a rhythm; the deck gives none.
- ⟨Scope and plants of the GitOps pilot⟩ and ⟨exit criteria of the pilot⟩ - OD lead.
- ⟨Whether the validation plan's adoption criterion has been tested⟩ - OD lead.
