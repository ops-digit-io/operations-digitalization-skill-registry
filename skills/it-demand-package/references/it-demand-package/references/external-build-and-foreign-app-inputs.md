---
type: Skill Reference
title: External build and foreign app inputs
description: What to collect for route 3a.3 (external development) and 3a.4 (foreign app) - the record fields the legacy application list already uses, the four assessment questions, the requirement parts an external developer can be handed, and the typical foreign-app cases in the legacy list. Open it when you assemble the specification or the foreign-app description.
resource: ../procedure.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# External build and foreign app inputs

Sources, read 2026-11-05: vault `Graph/Legacy Applications` (notes with the columns of the SharePoint list `LegacyApplication-List`, aggregated), skill `funnel-requirements` (`references/legacy-system-assessment.md`, `assets/requirement-template.md`, `references/epic-and-user-stories.md`), skill `od-decision-routing`, vault `Graph/Keynote Initiatives` (X1 to X4), and the WIP notes on the app manifest (see `deploy-appstore`).
The IT demand form is not in any source. This note therefore gives OD's side: what OD can describe about the demand, in the vocabulary the legacy list already uses, so that IT's own fields can be added later without rework.

## Describe the foreign app (3a.4) in the list's own columns

The legacy application list is the only place the vault records third-party and plant-local applications. Its columns are a ready description frame. For each foreign app ask the requester to fill them; whatever is not given stays ⟨missing⟩.

| Column in the list | Values the list uses | Why IT and Cyber Security ask |
|---|---|---|
| Application name, software version, software supplier | free text | identity; supplier support (a supplier status `IN SERVICE` / `SERVICE STOPPED` is recorded for some) |
| Application category, functional mapping | PLC programming / configuration, laboratory, equipment configuration, camera system configuration, custom SCADA, printer, quality software, internal Mendix apps, custom MES, material flow / logistics, SCADA, custom dashboarding, energy monitoring, MES | decides which existing family it joins |
| Production criticality | Critical / Moderate / Minimal / NA | weighs the change risk; count the Critical ones live |
| Licence required | no license required / Local License Available / OESL license required / unknown | a licence dependency has a lead time; unknown is common, count it live |
| Support concept and availability | Internal Support / External Support Contract / Maintenance & Run Concept; availability Yes / Possible | often not recorded; report blanks separately |
| Cyber-security status | Not started / In Progress / Approved / NA - Standalone | "Not started" is common; count it live, and do not read blank as "Not started" |
| Network status | Standalone / IT / OT/IT / OT | decides which sign-off route applies |
| Interfaced machines | free text (for example "<n> machines" or "all <n> machines of <vendor>") | what the app reads or writes on the floor |
| Status | in use, etc. | |

Aggregates and what they imply are in [catalog-usecase legacy-application-position](../../../../catalog-usecase/references/legacy-application-position.md). Add to the list of questions:

1. Divisional standard or local application? (the operations concept separates global IT support from local-only support; interfaces between the two need governance-board approval - see [it-touchpoints.md](it-touchpoints.md))
2. What does it read and write, from which system, in which direction, and does it write to a machine? (a write to a machine goes to the segmentation review and is not a plain IT demand)
3. Where does it run, and who runs it (plant IT, central IT, supplier)?
4. Which data object does it own, and does any other source hold the same object? (`systems-of-record`: two sources for one data object is the surest way to wrong answers)

## The four assessment questions (from the requirement skill)

Before specifying anything, `funnel-requirements` asks: does something already do this; is it supported; what does the licence cost; does it fit the footprint. Carry the answers into the package:

| Finding | What the package says |
|---|---|
| Existing app does it well | refuse the build; integrate or do nothing |
| Existing app does it badly | the demand is a replacement; scope the migration |
| Existing app does part of it | scope the delta only, state the boundary |
| System outside the footprint | not a use case; a tool-rollout decision for the OD lead |

## What an external developer (3a.3) can be handed

From OD's own skills, not from a vendor rule:

| Part | Source in the registry |
|---|---|
| The requirement in the standard ten-section form | `funnel-requirements`, `assets/requirement-template.md` |
| The epic with its user stories and the acceptance criteria | same, `assets/epic-and-stories.md`; `od-acceptance-test` for the protocol |
| The legacy and footprint assessment (section 8 of the requirement) | `references/legacy-system-assessment.md` |
| Data read and written, against the systems of record | `deploy-appstore`, deployment package |
| Interface and versioning expectations | `deploy-appstore`, `references/app-manifest-and-release-gate.md` (proposal) |
| Source ownership: the department keeps the source, or the app is a closed box | the three onboarding scenarios in `deploy-appstore`, `references/platform-and-pilot-status.md` |
| Business case with sources and capture dates | `bc-build` |

The security terms, environment access, spec format accepted by IT and any contract clauses are **not recorded**: ⟨what an external developer must receive⟩ - OD lead, IT demand management, Cyber Security.

## Cases the legacy list suggests (patterns, not counts)

Group the live legacy list by application category and read these patterns; count each group and its Critical and
unknown-licence members on the day you assemble the package.

| Pattern in the list | Implication for a package |
|---|---|
| Camera system configuration | likely X1/X2/X4 chain; the first X1 validation family is camera inspection apps |
| Custom SCADA | custom code, often with unknown licence: say so, ask supplier status |
| Custom MES | MES rollout is on hold; a package that depends on MES is blocked |
| Internal Mendix apps | assimilation candidate under X2; source is held by the department |
| Quality software | check which entries require an OESL licence |
| Laboratory software | usually standalone; low IT interface; licence status often unknown |

## Open

- ⟨IT's form fields, criteria, rhythm, lead time, contact⟩ - see `it-touchpoints.md`.
- ⟨The format of the specification IT accepts for an external build⟩.
- ⟨Whether a foreign app that is already in the legacy list needs a new demand or a change request on the existing entry⟩ - OD lead, IT.
