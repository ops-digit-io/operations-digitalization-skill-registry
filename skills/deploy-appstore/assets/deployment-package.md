---
type: Skill Asset
title: Deployment package
description: The blank deployment package and gate table for an app going to the platform, with the facts the vault supports pre-filled and every unknown marked. Copy one per app.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [project-support-consultancy, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Deployment package

Draft only. The package does not deploy anything and contains no deployment command. A human with deploy rights deploys, after the named approval. Mark pilot status in the header: the app store is a **pilot** (see [platform-and-pilot-status](../references/platform-and-pilot-status.md)).

```text
APP
Name / version / owner (role):                      Plant sponsor (role):         Plant owner (role):
What it does in one paragraph, and the decision it supports:
Template or capability it belongs to (R1-R11), or "one-off":
Sourcing route:   3a.1 reuse / 3a.2 self-developed / 3a.3 external, source owned / 3a.4 foreign app
Nearest onboarding scenario (inferred): internal / external with source / external without source

TARGET (record both layers; "Container Orchestration Platform" = the edge runtime of the IIoT Edge platform, Concept 3)
Runtime the app runs on:          plant edge Kubernetes runtime (Concept 3)?  plant ____  Concept 3 status Available? ____
Catalog it is published through:  manufacturing app store / CMO (pilot) ____

DATA (against systems-of-record - one source per data object)
Reads:   ____  source ____  freshness ____
Writes:  ____  to ____  write right ____
Writes to a machine?  yes / no       (yes -> segmentation review, human-only; not Lane 1)
Free-text fields?  yes / no          (yes -> name check, G17)

MANIFEST AND INTERFACES (proposal in the WIP notes; fill what the pilot requires)
consumes / publishes / api description / version / identity / health and metrics endpoints:
Container, image and registry rules, resource limits:   ⟨to be supplied⟩ (OD lead, IT platform)

DEPENDENCIES
Systems outside the lean footprint?  no / yes -> od-system-fit-check
Legacy applications touched (legacy-application-position in catalog-usecase):

ROLLBACK
Rollback owner (role):       Rollback step:

ACCEPTANCE
Protocol drafted (od-acceptance-test):  yes / no       Link:

OPEN QUESTIONS with owners
```

## Gate table (references/app-manifest-and-release-gate.md has the full list R1 to R11)

| Gate | Status | Evidence and date | By whom | Human-only |
|---|---|---|---|---|
| Front-end complete (requirement, tool decision, business case, capital) | | | | approvals |
| Acceptance protocol drafted | | | | sign-off |
| Cyber Security sign-off requested (`od-cybersec-gate`) | requested / granted | | Cyber Security | **yes** |
| Segmentation review (only if it writes to a machine) | n/a / requested / granted | | Cyber Security / OT | **yes** |
| Deployment approval for a shared platform (`od-decision-routing`) | | | named approver | **yes** |
| Deploy done | not started | | a human with deploy rights | **yes** |
| Handover to rollout (`od-handover-and-adoption`) | | | plant owner | the plant decides |

Wait state at the Cyber Security gate: "weeks" per the flow; ⟨lead time⟩ not recorded. Line at the foot, always: "Deployed by a human on ⟨date⟩ - not yet".
