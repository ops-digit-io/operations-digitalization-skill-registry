---
type: Skill Reference
title: Template coverage
description: The eleven capability templates with their delivery status, the plants that already run each one, where it is wanted but not yet delivered, what data it needs and which template a request belongs to. Open it to find a peer plant and the preconditions for a match.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Template coverage

Sources: vault `Graph/Use Cases` (650 plant use cases, frontmatter fields `use_case_template`, `status`, `plant`, `scalable`), `Graph/Use Case Views` (the eleven template pages, `Use Case Views.md`, `Use Case Views - Standardization.md`) and `Graph/Target Types`. Counts for plants and CSP were computed on 2026-11-05; the template pages are AI-drafted from the graph export of 2026-09-27 and not reviewed by a human.
"Delivered" means status `IMPLEMENTED` or `PRODUCTIVE` (296 of 650; the template pages use the same rule).
Plants are counted without the four non-plant labels the field also holds (`AI`, `All_Plants`, `General`, `Generic`; 30 use cases), so the plant counts are one to three lower than on the template pages. Spelling variants of two plant names (Hann. Muenden, Hannover Stoecken) are counted as the notes spell them.

## The eleven templates

| Template | Plant use cases: delivered / all | Plants that want it | Plants that have it delivered | Reference solutions (CSP Yes / No) | Dashboard families | Flagged `scalable` (all / delivered) |
|---|---:|---:|---:|---|---:|---|
| Process Values | 90 / 180 | 21 | 15 | 19 (0 / 6) | 30 | 52 / 39 |
| Andon Board | 69 / 134 | 23 | 20 | 15 (1 / 9) | 18 | 28 / 23 |
| Other Use Cases | 27 / 73 | 20 | 10 | 4 (0 / 4) | 2 | 13 / 9 |
| Process Quality Data | 16 / 55 | 17 | 8 | 10 (0 / 3) | 20 | 19 / 9 |
| Manual Quality Data | 10 / 46 | 13 | 6 | 1 (0 / 1) | 1 | 9 / 6 |
| Machine Alerts | 20 / 36 | 15 | 12 | 8 (0 / 3) | 12 | 8 / 8 |
| Analytics | 12 / 29 | 12 | 7 | 13 (1 / 7) | 7 | 6 / 3 |
| OEE Calculation | 15 / 29 | 12 | 7 | 8 (0 / 4) | 15 | 7 / 4 |
| Cycle Time | 15 / 28 | 12 | 9 | 12 (1 / 4) | 25 | 6 / 5 |
| Downtime Reporting | 16 / 27 | 14 | 8 | 10 (2 / 5) | 8 | 11 / 10 |
| Recipe Values | 6 / 13 | 6 | 4 | 0 | 4 | 3 / 1 |

Reading the table:

- Reference solutions and dashboard families are the figures of the template pages (a dashboard family that carries several templates counts under each). The CSP split counts library entries only; the rest of the reference solutions have no decision recorded (see [library-and-csp-state.md](library-and-csp-state.md)).
- **Where the pattern exists in most plants:** Andon Board (20 of the 26 plants that record a plant use case) and Process Values (15). **Least spread:** Recipe Values (4), Manual Quality Data (6), Analytics, OEE Calculation (7 each).
- **Where it is wanted but not delivered** the gap is widest for Other Use Cases (10 plants), Process Quality Data (9), Manual Quality Data (7), Process Values (6), Downtime Reporting (6). These are the plants a catalog entry would serve first.
- Delivery of the whole portfolio: 296 of 650 use cases are delivered; 167 `PRODUCTIVE`, 129 `IMPLEMENTED`, 229 `IDEA`, 122 `PLANNED`, 2 `STOPPED`, 1 group (computed).
- Documentation is uneven (template pages): across the templates 29 plant-and-template pairs with a delivered use case are fully described (reference solution and dashboard family), 31 partly, 46 only by the use case note. A thinly documented template is a weak match source however many plants run it.

## Peer plants per template (delivered use case recorded)

Use this to tell a requesting plant which plant to call. The note of the plant use case holds the owner role and the data path.

| Template | Plants with a delivered use case |
|---|---|
| Andon Board | Auburn, Caluire, Changchun, Changshu, Delicias, Dolne Vestenice, Hann. Muenden, Karben, Mako, Monterrey, Northeim, Ponta Grossa, Qingdao, Rennes, Somersworth, Subotica, Sun Prairie, Timisoara, Vac, Waltershausen |
| Process Values | Carei, Changchun, Changshu, Delicias, Hann. Muenden, Karben, Mako, Monterrey, Ponta Grossa, Qingdao, Somersworth, Sun Prairie, Timisoara, Vac, Waltershausen |
| Machine Alerts | Auburn, Changchun, Changshu, Delicias, Karben, Mako, Northeim, Ponta Grossa, Qingdao, Somersworth, Sun Prairie, Waltershausen |
| Other Use Cases | Auburn, Changshu, Monterrey, Northeim, Ponta Grossa, Rennes, Somersworth, Sun Prairie, Timisoara, Waltershausen |
| Cycle Time | Carei, Changchun, Delicias, Dolne Vestenice, Karben, Mako, Qingdao, Somersworth, Subotica |
| Downtime Reporting | Delicias, Mako, Monterrey, Qingdao, Rennes, Somersworth, Subotica, Sun Prairie |
| Process Quality Data | Delicias, Karben, Mako, Monterrey, Qingdao, Rennes, Somersworth, Waltershausen |
| Analytics | Caluire, Delicias, Karben, Monterrey, Rennes, Sun Prairie, Waltershausen |
| OEE Calculation | Changchun, Changshu, Delicias, Ponta Grossa, Qingdao, Rennes, Sun Prairie |
| Manual Quality Data | Changshu, Delicias, Mako, Monterrey, Subotica, Waltershausen |
| Recipe Values | Auburn, Carei, Northeim, Somersworth |

Wanted but not delivered (plants with a plant use case in the template and none delivered): Andon Board - Carei, San Luis Potosi, Tlalnepantla; Cycle Time - Changshu, San Luis Potosi, Timisoara; Downtime Reporting - Caluire, Carei, Changchun, Changshu, Timisoara, Tlalnepantla; OEE Calculation - Mako, Monterrey, San Luis Potosi, Somersworth, Vac; Machine Alerts - Carei, San Luis Potosi, Timisoara; Manual Quality Data - Carei, Changchun, Karben, Qingdao, San Luis Potosi, Timisoara, Tlalnepantla; Recipe Values - Mako, Waltershausen; Analytics - Carei, Changchun, Northeim, Subotica, Wiritec.
Longer lists (Process Values, Process Quality Data, Other Use Cases) are in the template pages.

## What each template needs - the preconditions for branch 1a

From the "standard data and realization" block of each template page (target types and machine links counted by the graph; keyword counts, not verified). Use it with `od-data-availability-check`.

| Template | Target types it needs to see (count of tagged use cases and families) | PLC vendors behind the linked machines (machine links) | Linked machines recorded as integrated |
|---|---|---|---|
| Andon Board | Andon Board 25, Machine Availability 14, Cycle Time Monitoring 11, Quality Losses 5 | Bachmann 136, Siemens 135, Beckhoff 63 | 237 of 383 |
| Process Values | Process Values 41, Machine Availability 13, Cycle Time Monitoring 12, Process Set Values 11, SPC Charts 9 | Siemens 155, Beckhoff 105, Bachmann 39 | 300 of 365 |
| Machine Alerts | Notification 11, Process Values 9, Cycle Time Monitoring 5, Machine Availability 4 | Siemens 61, Beckhoff 25, Bachmann 19 | 97 of 133 |
| Process Quality Data | SPC Charts 19, Process Values 19, Quality Losses 16, Cycle Time Monitoring 10, Image Data 7 | Siemens 40, Beckhoff 16, Engel 6 | 48 of 66 |
| Cycle Time | Cycle Time Monitoring 26, Process Values 13, Machine Availability 12, Quality Losses 9 | Siemens 41, Bachmann 19, Beckhoff 16 | 57 of 95 |
| Downtime Reporting | Machine Availability 10, Cycle Time Monitoring 3, Andon Board 3, Quality Losses 3 | Siemens 33, Beckhoff 25, Rockwell 19 | 78 of 106 |
| OEE Calculation | Machine Availability 16, Andon Board 8, Cycle Time Monitoring 6, Process Values 5 | Siemens 46, Bachmann 19, Rockwell 6 | 46 of 66 |
| Analytics | Process Values 6, Energy Data 2, Manual Quality Data Input 1 | Siemens 20, Rockwell 6, Omron 1 | 24 of 24 |
| Manual Quality Data | SPC Charts 4, Manual Data Input 3, Quality Losses 3, Manual Quality Data Input 3 | Siemens 17, Vipa 2 (and the QFPR tool 18) | 14 of 14 |
| Recipe Values | Process Set Values 4, Process Values 3, Machine Availability 1 | Beckhoff 27, Siemens 10 | 35 of 35 |
| Other Use Cases | Energy Data 2, Process Values 2, Notification 1 | Beckhoff 27, Siemens 20 | 40 of 41 |

Two readings for the match:

- A **Cycle Time**, **Downtime Reporting**, **OEE** or **Andon** match needs a *Machine Availability* or *Cycle Time Monitoring* signal; check these two first on the machine.
- Where the share of integrated machines is low (Andon 237 of 383, Cycle Time 57 of 95, Downtime 78 of 106) a plant's machine is more likely to land on branch **1b** than on 1a.

## Which template does the request belong to

Apply the placement rules of `Use Case Views - Standardization` (R1 to R13) in the order of rule R12: Recipe Values, Downtime Reporting, Machine Alerts, Andon Board, Cycle Time, OEE Calculation, Process Quality Data, Manual Quality Data, Process Values, Analytics, Other Use Cases. The purpose stated in the request beats the title. Short boundary table (from the template pages):

| Template | Belongs | Does not belong (go to) |
|---|---|---|
| Andon Board | status boards for line, cell, area or plant, output against target, escalation trigger | messages to people (Machine Alerts); stop log (Downtime Reporting); the OEE figure (OEE Calculation); parameter curves (Process Values) |
| OEE Calculation | OEE or availability, performance, quality per machine, line, plant | the stop events (Downtime Reporting); cycle time analysis (Cycle Time) |
| Cycle Time | cycle time, takt, step or throughput time against a standard | downtimes (Downtime Reporting) |
| Downtime Reporting | stop events with duration and reason, operator-entered or detected | notifications about a stop (Machine Alerts) |
| Machine Alerts | alarms, notifications, tolerance alerts to people, alert list | status-only boards (Andon Board) |
| Process Values | live process parameters, equipment overviews | SPC and inline quality (Process Quality Data); set values (Recipe Values); cross-machine analysis (Analytics) |
| Process Quality Data | inline measurement, SPC, vision, test results, scrap counting, per-part traceability | hand-entered data (Manual Quality Data) |
| Manual Quality Data | paper and Excel checklists, inspection sheets, manual measurement and lab entry | automatic collection (Process Quality Data) |
| Recipe Values | recipes, parameter sets, change tracking, set-value transfer | actual process values (Process Values) |
| Analytics | reports and analyses across machines, lines, plants; forecasts; models | live displays of one line (Andon, Process Values); AI helpers on documents (Other) |
| Other Use Cases | what fits none of the ten: IT tools, document AI helpers, administration, planning, mold and tool management, device status | anything that fits a named template |

## Typical components of a matching screen

Number of dashboard families per template that show the component (keyword count over their descriptions; a guide for what a plant should expect to see, not a requirement): Andon Board - status or state bar 13, per-shift breakdown 7, pie or donut 6, table or log 6, target comparison 3. Cycle Time - bar chart 12, per-shift breakdown 11, status bar 11, table or log 11. Downtime Reporting - status bar 6, trend 4, per-shift 4, table or log 4. Machine Alerts - table or log 10, bar chart 4, gauge or KPI tile 3. OEE - status bar 12, table or log 7, per-shift 7, gauge or KPI tile 5. Process Values - trend 16, table or log 14, status bar 11, bar chart 9. Process Quality Data - table or log 11, bar chart 10, status bar 6, trend 5. The figures a template page names most often: Andon - output against target (31 notes), cycle time (24), OK and NOK parts (23), availability (19); OEE - OEE (32), availability (14); Downtime - downtime (27).

## Open

- ⟨Which of these eleven templates the OD lead wants offered for self-service first⟩ - the table shows where the data is thickest (Andon Board, Process Values), not what OD has decided.
- ⟨Whether the `scalable` flag may serve as the entry gate for candidates⟩ - OD lead.
