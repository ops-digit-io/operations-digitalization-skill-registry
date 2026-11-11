---
type: Skill Reference
title: Master register
description: Guidance for reading the department resource register to resolve a template - which kinds of rows exist, who owns them, how to read the state markers, plus the templates produced inside registry skills; no state or date snapshot, look the live state up in the register.
resource: ../SKILL.md
status: draft
tags: [all, practice]
---

# Master register

How to read the department resource register, not a copy of it. The register lives at
`ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/15-resources.md`; it is reviewed quarterly.
This page deliberately holds **no state, no version dates and no counts**: a copy would drift from the register the
moment a row changes. Always read the register's current row for state, location and verification date.
Full links are in the source file and are not repeated here.

## How to read a register row

Columns to read: resource, type, serves (lane / use case), owner, version or verified date, location.

| Marker in the location or version cell | Meaning | What you do |
|---|---|---|
| A link and a date | Usable master | Use it; note the date |
| `to collect` | The master exists somewhere but is not yet registered | Stop; ask the owner role |
| `to confirm` / `to confirm or create` | Ownership, link or the template itself is not settled | Do not improvise; route to creation |
| Name present, link missing | The source is known but not reachable from the register | Ask the owner role for the link; do not guess a workspace |

## A. Kinds of rows in the register

### A1. Templates and boilerplate

Reference decks (for example the OD Outreach Strategy deck, owner: OD lead role) and the standard format to define,
prioritise and impact-evaluate a use case at intake (use-case one-pager / business-case template, owner: DBVE).
Check live whether the one-pager template is a real master or still a gap row.

### A2. Standards and reference documents

Requirement specification for machines and equipment (owner: Engineering Standards, a separate team site),
ProView support process (owner: OD lead role; a reference, not a fill-in template), IT Digital Platforms planning
documents (owner: OESL IT Digital Platforms; reference, dated by planning cycle), and the machine-connection / cyber
security sign-off standard (owner: OD lead role with Cyber Security). Some of these are references to read, not
templates to fill; the row's *Serves* cell says which.

### A3. Data sources and tools (the "canonical source to cite")

Power BI reports (scorecard, use-case integration, equipment integration; owners: OD lead role, DBVE, IIAE), the data
platform, the IIoT Edge / MSB platform (owner: IIAE) and the OD Teams site General library (owner: OD lead role).
Typical gap: report name known, workspace link missing. To know how many rows are in each state, count them in the
register on the day; do not quote a remembered figure.

## B. Templates produced inside registry skills


These are the fill-in protocols the skills ship. They are **skill-level protocols**, not entries in the resource register,
so none of them is an "approved master" in the register's sense. Use them as the working format named by the skill, and
cite the skill, not the register.

| Deliverable | Skill and file | Lane step it serves |
|---|---|---|
| Use-case definition protocol and questionnaire | `funnel-use-case`: `assets/use-case-definition-protocol.md`, `assets/use-case-definition-questionnaire.md` | Lane 2 step 1 |
| Solution evaluation protocol | `funnel-evaluation`: `assets/evaluation-protocol.md` | Lane 2 step 2 |
| Requirement, epic and stories | `funnel-requirements`: `assets/requirement-template.md`, `assets/epic-and-stories.md` (+ `.example.md`) | Lane 2 step 2 / Lane 3 step 1 |
| Data availability verdict | `mi-data-availability`: `assets/data-availability-verdict.md` | Lane 2 step 2 |
| System fit check | `invest-screen`: `assets/system-fit-check.md` | Intake / Lane 3 gate |
| Equipment assessment, connection guidance | `mi-equipment`: `assets/assessment-protocol.md`, `assets/guidance-protocol.md` | Lane 1b / Lane 3b |
| Signal analysis report | `mi-signals`: `assets/signal-analysis-report.md` | Lane 3b |
| Acceptance test protocol | `deploy-acceptance`: `assets/acceptance-test-protocol.md` | Lane 3b step 3 |
| Handover protocol | `deploy-handover`: `assets/handover-protocol.md` | Lane 2 step 6 / Lane 3 |
| Asset build protocol | `ops-analytics-asset`: `assets/asset-build-protocol.md` | Lane 1 |
| Standardization review | `catalog-standardization`: `assets/standardization-review.md` | Lane 2 graduation |
| Decision request | `dept-decision-rights`: `assets/decision-request.md` | any gate outside OD |
| Scorecard update protocol | `metrics-scorecard`: `assets/scorecard-update-protocol.md` | on request or on the department schedule / COP |
| Portfolio review protocol | `bc-portfolio`: `assets/portfolio-review-protocol.md` | portfolio review |
| Export run log | `know-sharepoint-export`: `assets/export-run-log.md` | list export |
| Investment input pack; prototype briefs | `bc-cost`, `funnel-prototype` (see each skill's assets folder) | Lane 1b / Lane 2 |

The information-integration lane's task list (`20-lanes/information-integration-service/tasks.md`) names four templates
as gaps in the department itself: *Equipment Assessment & Roadmap*, *Investment plan*, *Integration checklist* (each
`template - to confirm`). The skills above (`assessment-protocol`, `investment-input-pack`, `guidance-protocol`) are the
current working substitutes; whether they are adopted as the masters is `to confirm` with the IIAE role.

## C. Files found outside the register

The department knowledge base can hold master-slide files that the register does not list. A file found there is **not** an approved
master until the register (or the OD lead role) says so. Record its existence, do not use it as the master, and ask the
OD lead role which deliverable it serves and who owns it. Search the knowledge base's master-slide folder at the time of use; do
not rely on a remembered file list.

## D. Typical gaps and who can close them

| Kind of gap | Who can supply it |
|---|---|
| Use-case one-pager / business-case master | DBVE |
| Cyber Security sign-off standard | OD lead role with Cyber Security |
| Report links (scorecard, use-case integration, equipment integration) | OD lead role, DBVE, IIAE |
| Platform links (data platform, IIoT Edge / MSB) | IIAE |
| Whether skill-level protocols are adopted as masters | OD lead role, per lane owner |
| Status of a knowledge base master-slide file | OD lead role |

Whether a given gap is open today is read from the register, not from this page.
