---
type: Skill Reference
title: It expected inputs
description: "What IT asked OD to deliver with a demand in the OD x IT alignment of 2026-09-11, item by item, where each lands in the handover package, which items block a handover, and the open IT action items that will firm them."
resource: ../SKILL.md
status: draft
tags: [it-alignment, handover, transcript]
---
# What IT expects from OD

Source: the OD x IT alignment, 2026-09-11 (AI-generated notes, not verbatim; verify a point with the
participants before quoting it as agreed policy). The meeting set direction; most rules are still open
action items on the IT side, listed at the end.

## Inputs the annex carries

| # | Input | What the meeting said | Blocking? | Annex section |
|---|---|---|---|---|
| 1 | Requirements | Requirements from the funnel are the first artefact IT expects; they fix objective, scope, interfaces and growth boundaries (mission creep) | yes | 1 |
| 2 | Source code | Where it lives and who owns it; in guided buy the company keeps the code where appropriate | yes for 3a.2 / 3a.3 | 2 |
| 3 | Deployment assumptions | CMO (Kubernetes) with the standard manifests is the preferred path; approved stacks; observability | yes | 3 |
| 4 | Cyber Security inputs | Pre-evaluated, missing inputs named before the formal review; which approved platform pattern is reused | yes | 4 |
| 5 | Access rights | Who may read and write which data | yes | 5 |
| 6 | Data models | The data the system reads and publishes, in the agreed model | yes | 6 |
| 7 | Data catalog entry | Dataset description, authoritative master system, format, who may access it; for new **and** existing apps | no (structure open) | 7 |
| 8 | Interface catalog entry | How the system exchanges data with others; approved OT interfaces (MQTT to the edge), reuse of central systems and data stores | no (structure open) | 7 |
| 9 | Business case | Bankable impact apart from assumption-dependent benefit; actionable impact, dependencies, investment envelope; build and run cost; minimum viable rollout, maximum scale-out, resources, cloud consumption, TCO | yes | 8 |
| 10 | Sourcing decision | Solution-design stage done; build / buy / guided buy / integrate, and why | yes | 9 |
| 11 | Ownership terms | Build-and-run; shared responsibility split for complex apps; criticality; ownership moves on formal acceptance; handover checklist (legacy status, backlog, version currency, architecture, business logic, logging, observability) | yes | 10 |
| 12 | Collaboration and capacity | Specialist participation and reserved PI capacity are planned, not pressured | no | 11 |
| 13 | Legacy link | Whether it replaces or touches one of the legacy applications; its requirements baseline | no | 12 |
| 14 | Commitment status | No delivery date to the business until a team has committed the work in sprint or PI planning | yes (state it) | 13 |

## Lessons the package guards against (Gemba app case)

About a year in the funnel, informal delivery promises, one developer, development outside the delivery
setup. The package answers the root-cause questions up front: is the requirement clear, is the business
case firm, is the scope stable, is the solution defined, and was it prioritized in a committed plan.

## Open IT action items that will firm the inputs

| Action | Owner (as recorded) | Firms input |
|---|---|---|
| Structure and contents of the data and interface catalogs | IT | 7, 8 |
| Consolidate the artefacts IT expects from the funnel and where each is stored or exchanged | IT | all; the receiving location for OpenSpec changes |
| Cyber Security pre-evaluation approach, aligned with Cyber Security | OD lead, IT | 4 |
| Platform-level Cyber Security approval model | IT | 4 |
| Ownership and handover gates | IT, OD lead | 11 |
| Technology guardrails (stacks, Kubernetes / CMO, interfaces, OT) | IT, OD | 3 |
| Recurring application self-assessment | IT, OD lead | 11 |
| CMO roadmap and target blueprint | IT | 3 |
| Minimum and maximum deployment scenarios per use case | OD lead, IT | 9 |
| Build / buy / guided delivery sourcing criteria with TCO | IT, OD lead | 10 |
| Requirements and technology baseline for the legacy applications | unassigned | 13 |
