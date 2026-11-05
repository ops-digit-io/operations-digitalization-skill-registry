---
type: Skill Reference
title: Master register
description: The lookup of every template, standard and tool the resource register lists, with owner, state and gap markers, plus the templates produced inside registry skills and one vault file the register does not list; open it to resolve a template.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Master register

Source: `ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/15-resources.md`
(register last verified 2026-08-10, review cadence quarterly). Locations are named by the library they live in;
the full links are in the source file and are not repeated here, so that this page cannot drift from it.
Mark as the register marks: `to collect` = the master exists but is not yet registered; `to confirm` /
`to confirm or create` = ownership, link or the template itself is not settled.

## A. Rows of the resource register

### A1. Templates and boilerplate

| Resource | Type | Serves | Owner | Version / verified | State |
|---|---|---|---|---|---|
| OD Outreach Strategy deck | pptx | Reference master for how OD presents what it delivers and expects; reuse its structure for outreach and strategy updates. All lanes (comms) | OD lead role | 2025-03-04 | **Usable.** Link present (OD Teams site, General library) |
| Use-case one-pager / business-case template | pptx / xlsx | Standard format to define, prioritize and impact-evaluate a use case at intake. Use Case Support Service | DBVE | to confirm | **No master.** Location reads "dedicated OD template - to confirm or create" |

### A2. Standards and reference documents

| Resource | Type | Serves | Owner | Version / verified | State |
|---|---|---|---|---|---|
| Requirement Specification for Machines & Equipment (PRS), Doc ID 215534 | docx | Standard requirement-spec template for integrating machines and equipment. Information Integration Service | Engineering Standards (a separate team site) | 2025-04-22 | **Usable.** Link present (Engineering Standards library) |
| ProView Support Process | pptx | Incident-management process for ProView; reference for support and handover. Project Support & Consultancy | OD lead role | 2026-01-13 | **Usable** (reference, not a fill-in template) |
| OESL IT Digital Platforms - PI Planning targets and priorities | pdf | Alignment of OD roadmap with IT Digital Platforms. All lanes | OESL IT, Digital Platforms | 2025-12-02 | **Usable** (reference). Dated Q1 planning cycle |
| Machine-connection / Cyber Security sign-off standard | docx / pdf | Gate for compliant OT machine connection. Information Integration Service | OD lead role with Cyber Security | to confirm | **Not collected.** Location reads "standard doc - to collect (with Cyber Security)" |

### A3. Data sources and tools (the "canonical source to cite")

| Resource | Type | Serves | Owner | Verified | State |
|---|---|---|---|---|---|
| Digitalization Scorecard ("MPEE-OD-Plant_Scorecard") | Power BI | Authoritative targets vs actuals and readiness matrix | OD lead role | 2026-08-10 | Name present, **workspace link to confirm** |
| Use Case Integration report ("OD-Report-Use_Case_Integration") | Power BI | Use-case counts, asset mix, by region and process | DBVE | 2026-08-10 | Name present, **link to confirm** |
| Equipment Integration report ("OD-Report-Equipment_Integration") | Power BI | Equipment counts by region and process | IIAE | 2026-08-10 | Name present, **link to confirm** |
| Data platform (Databricks to Azure Storage Account, Parquet) | platform | Global layer, cross-plant analysis | IIAE | to confirm | **Access / portal link to collect** |
| IIoT Edge / MSB | platform | Data acquisition runtime and integration backbone | IIAE | to confirm | **Portal link to collect** |
| OD Teams site, General library | SharePoint | Home of OD context, decks and shared documents | OD lead role | 2026-08-10 | Usable (link present) |

Count of the register's 12 rows: 5 usable with a link and date, 1 with no master (the one-pager), 1 not collected
(Cyber Security standard), 3 with a missing report link, 2 with a missing platform link. Counted by hand from the file
read 2026-11-05; recount when the register changes.

## B. Templates produced inside registry skills

These are the fill-in protocols the skills ship. They are **skill-level protocols**, not entries in the resource register,
so none of them is an "approved master" in the register's sense. Use them as the working format named by the skill, and
cite the skill, not the register.

| Deliverable | Skill and file | Lane step it serves |
|---|---|---|
| Use-case definition protocol and questionnaire | `od-use-case-definition`: `assets/use-case-definition-protocol.md`, `assets/use-case-definition-questionnaire.md` | Lane 2 step 1 |
| Solution evaluation protocol | `od-use-case-solution-evaluation`: `assets/evaluation-protocol.md` | Lane 2 step 2 |
| Requirement, epic and stories | `od-requirements-breakdown`: `assets/requirement-template.md`, `assets/epic-and-stories.md` (+ `.example.md`) | Lane 2 step 2 / Lane 3 step 1 |
| Data availability verdict | `od-data-availability-check`: `assets/data-availability-verdict.md` | Lane 2 step 2 |
| System fit check | `od-system-fit-check`: `assets/system-fit-check.md` | Intake / Lane 3 gate |
| Equipment assessment, connection guidance | `od-equipment-integration`: `assets/assessment-protocol.md`, `assets/guidance-protocol.md` | Lane 1b / Lane 3b |
| Signal analysis report | `od-signal-standardization`: `assets/signal-analysis-report.md` | Lane 3b |
| Acceptance test protocol | `od-acceptance-test`: `assets/acceptance-test-protocol.md` | Lane 3b step 3 |
| Handover protocol | `od-handover-and-adoption`: `assets/handover-protocol.md` | Lane 2 step 6 / Lane 3 |
| Asset build protocol | `od-analytics-asset-build`: `assets/asset-build-protocol.md` | Lane 1 |
| Standardization review | `od-use-case-standardization`: `assets/standardization-review.md` | Lane 2 graduation |
| Decision request | `od-decision-routing`: `assets/decision-request.md` | any gate outside OD |
| Scorecard update protocol | `od-scorecard-reporting`: `assets/scorecard-update-protocol.md` | monthly / ODEC / COP |
| Portfolio review protocol | `od-portfolio-and-savings-analysis`: `assets/portfolio-review-protocol.md` | portfolio review |
| Export run log | `od-sharepoint-list-export`: `assets/export-run-log.md` | list export |
| Investment input pack; prototype briefs | `od-investment-input`, `od-prototype-poc` (assets present on disk 2026-11-05; written by others in this build, contents not read here) | Lane 1b / Lane 2 |

The information-integration lane's task list (`20-lanes/information-integration-service/tasks.md`) names four templates
as gaps in the department itself: *Equipment Assessment & Roadmap*, *Investment plan*, *Integration checklist* (each
`template - to confirm`). The skills above (`assessment-protocol`, `investment-input-pack`, `guidance-protocol`) are the
current working substitutes; whether they are adopted as the masters is `to confirm` with the IIAE role.

## C. Found in the vault, not in the register

| File | Where | State |
|---|---|---|
| `Digitalization-IT-OT-Master-Templates.pptx` | Work vault, folder `Master-Slide-Templates` (the only file there besides a thumbnail cache) | Name only; **not opened**, not in the register. Whether it is the approved master for IT / OT demand slides, and who owns it: `to confirm` with the OD lead role |

## D. Gaps summarised, with who can close them

| Gap | Who can supply it |
|---|---|
| Use-case one-pager / business-case master | DBVE (register owner of the row) |
| Cyber Security sign-off standard | OD lead role with Cyber Security |
| Report links (Scorecard, Use Case Integration, Equipment Integration) | OD lead role, DBVE, IIAE |
| Platform links (data platform, IIoT Edge / MSB) | IIAE |
| Whether skill-level protocols are adopted as masters | OD lead role, per lane owner |
| Status of the vault master-slide file | OD lead role |
