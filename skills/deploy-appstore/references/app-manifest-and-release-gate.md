---
type: Skill Reference
title: App manifest and release gate
description: The fields an app should declare to join the platform, the interface and versioning rules the WIP design proposes, the security review triggers, and the release-gate checklist assembled from them. Open it when you assemble a deployment package or review one.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [project-support-consultancy, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# App manifest and release gate

**Status of the source:** everything in the first three sections is a **proposal** from AI-drafted work-in-progress notes in the vault folder `Microservice Apps (WIP)` (generated 2026-09-27, "not reviewed by a human"): *Platform Extensibility and Onboarding*, *Cross-Cutting Platform Concerns*, *Platform Services (Shared Kernel)*, *Recipe Values Service*, *User Interfaces and Interaction Layer*, read 2026-11-05. They describe the design of a possible landscape. They are **not** the recorded deployment procedure of the pilot. Use them as the best available checklist of what a package should declare, and say so in the package.

## The app manifest (proposed)

A short machine-readable manifest published beside the container image in the same catalog entry. The WIP note's example fields:

| Field | Meaning | Why the gate wants it |
|---|---|---|
| `name`, `version`, `owner` (team or vendor) | identity and who answers | rollback owner (SKILL.md step 3) |
| `consumes`, `publishes` | topics and their schema versions | what the app reads and writes, checked against `systems-of-record` |
| `api` | link to the API description | interface is a checkable artifact, not a promise |
| `writes_to_machines` | true or false | **true changes the review path**: segmentation review under ISA/IEC 62443 and NIST SP 800-82 before it goes live, however small the app |
| `data_owned` | the records the app owns | data owner OD or plant; one source per data object |
| `identity` | corporate identity provider via OIDC | no app keeps a password or role table of its own |
| `cybersec_review` | `pending` or `passed` | the human-only sign-off; an agent may not set `passed` |

The manifest is a design proposal. ⟨Whether the pilot uses a manifest, and its format⟩ - OD lead.

## Interface, versioning, operation (proposed)

- **Interfaces as documents.** Every app ships an OpenAPI 3.x description of its REST surface and an AsyncAPI 2.x description of the topics it publishes and consumes, in the same catalog entry as the image.
- **Versions.** Every topic and API carries a version (`.v1`). Changes inside a version are additive only. An incompatible change ships as `.v2` beside `.v1` until every consumer has moved, then `.v1` is deprecated with notice - never replaced in place.
- **Operation.** A standard health endpoint and a standard metrics endpoint per app. Which log and metric pipeline the edge clusters ship to "is not recorded in the vault notes read" - ⟨logging and metrics pipeline⟩, IIAE.
- **Edge resilience.** A plant-local app buffers its bus consumption locally and replays after a network outage. Locale is a per-plant configuration value, not a fork of the app per language.
- **Free text.** An app with a free-text field must not summarise, enrich or forward the text by an automated pipeline without filtering (the vault's rule on names; one recorded case). See guardrail G17 in `catalog-usecase`.
- **No new path.** Onboarding goes through one of the three scenarios in [platform-and-pilot-status.md](platform-and-pilot-status.md); the WIP note holds that a fourth, ad hoc path would defeat the purpose of the catalog.
- **Where a new thing belongs.** Apply the placement rules (R1 to R11) first; a use case that fits a template is a new plant instance of an existing service, not a new app. A one-off goes to the store as an individually catalogued container. A new service is justified only when a second unrelated use case needs the same function.

## What is NOT in the vault

No containerization requirements, no image or registry rules, no resource limits, no deployment commands, no list of who holds deploy rights, no release calendar. The WIP notes say "container-based, one to two small containers per service, deployed on the existing edge Kubernetes runtime" and nothing finer. These stay ⟨to be supplied⟩ (OD lead, IIAE, IT platform team) and the skill still writes no command.

## The release gate - checklist

Use with `od-acceptance-test`, `od-cybersec-gate` and `od-decision-routing`. A box needs evidence and a date.

| # | Gate | Evidence | Owner role | Human-only? |
|---|---|---|---|---|
| R1 | Front-end done: requirement (`funnel-requirements`), tool decision (`invest-screen`), business case (`bc-build`), capital approved where needed | links | OD lead / DBVE | the approvals are |
| R2 | Target named as the requester names it, both layers recorded (edge runtime and app store / CMO), and the sourcing route 3a.1 to 3a.4 | package fields 1 and 2 | DBVE | no |
| R3 | Manifest complete; `writes_to_machines` stated | manifest | app owner | no |
| R4 | Interfaces described (OpenAPI, AsyncAPI) and versioned | documents | app owner | no |
| R5 | Data read and written matches `systems-of-record` (one source per data object); no second source for the same object | table | IIAE | no |
| R6 | Acceptance protocol drafted before the build (`od-acceptance-test`) | protocol | DBVE | the sign-off is |
| R7 | Cyber Security sign-off requested via `od-cybersec-gate`; if the app writes to a machine, segmentation review requested | request, date | IIAE with Plant IT | **yes** |
| R8 | Approval for deployment to a shared platform named (`od-decision-routing`): who approves, when | decision record | OD lead | **yes** |
| R9 | Rollback owner and rollback step named | package | app owner | no |
| R10 | Plant sponsor and plant owner named; handover planned (`od-handover-and-adoption`) | package | plant | the plant decides daily use |
| R11 | Free-text and name check (G17); no credentials or sessions in the package (G19 in `catalog-usecase`) | check | DBVE | no |

The wait for R7 is "weeks" in the flow; the vault gives no figure. Do not quote one. For a foreign app (3a.4) the planned IEC 62443-4-2 conformance gate of initiative X4 would apply once it exists; today it is a plan, not a gate.

## Open

- ⟨Containerization, image and registry rules, resource limits⟩ - OD lead, IT platform.
- ⟨Who holds deploy rights on the app store and on the plant runtime⟩.
- ⟨Cyber Security requirements for an app⟩ and ⟨lead time⟩ - owner of the Cyber Security standard (listed in the bundle as still to be collected).
