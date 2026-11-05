---
type: Skill Reference
title: Capability templates and placement
description: The 11 use case templates a dashboard or report is filed under, the 13 placement rules and their precedence, member counts per template, the 36 case groups, and how to place a new asset so it is counted once.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [analytical-support-service, practice, templates]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Capability templates and placement

An asset that is not placed in a template is not counted in the portfolio. This file is the
rule set (`Graph/Use Case Views/template-standards.json`, authored 2026-09-26, "AI-drafted; not
reviewed by a human"; the Standardization note lists the cases for review) plus the size of each
template, so the key user can file a new dashboard in the same way the 650 existing use cases and
1,010 dashboards were filed. The rules **describe what recorded placements mostly do**; they are
not yet a decision of the department. Placement itself is `od-use-case-standardization`'s job; this
file is what `od-analytics-asset-build` needs when it builds the asset.

## 1. The 11 templates and what is in each (count: 650 plant use cases, 2026-11-05)

| Template | Use cases | Library entries | Dashboard families | One line: belongs here | Not here (go to) |
|---|--:|--:|--:|---|---|
| Process Values | 180 | 19 | 30 | live machine and process parameters, process overviews per machine, line or oven, utility readings | SPC (Process Quality Data), set values (Recipe Values), cross-machine analysis (Analytics) |
| Andon Board | 134 | 15 | 18 | a visual board of current status of a line, cell, area or plant; Andon/Gemba levels 1-3, production overview, card view, output against target | alerts as messages (Machine Alerts), stop log (Downtime Reporting), the OEE figure (OEE Calculation) |
| Other Use Cases | 73 | 4 | 2 | catch-all: IT tools, AI helpers on documents, planning, device and camera status | anything that fits a named template |
| Process Quality Data | 55 | 10 | 20 | automatic in-process quality: inline measurement, SPC and capability, vision, test results, scrap, jidoka, per-part traceability | data typed by hand (Manual Quality Data) |
| Manual Quality Data | 46 | 1 | 1 | digitising what people record by hand: checklists, inspection sheets, lab results, calendars | automatic collection |
| Machine Alerts | 36 | 8 | 12 | alarms and notifications sent to people or shown as an alert list; tolerance alerts; maintenance-due | status-only boards, stop logs |
| Analytics | 29 | 13 | 7 | reports and analyses across machines, lines or plants; KPI and Power BI reports; forecasts; models | live displays of one machine, AI helpers on documents |
| OEE Calculation | 29 | 8 | 15 | OEE or its components per machine, line or plant, availability tracking | stop events (Downtime Reporting), cycle-time analysis, boards without an OEE figure |
| Cycle Time | 28 | 12 | 25 | cycle time, takt, loading time, step or throughput time against a standard | downtime, the OEE performance figure as a whole |
| Downtime Reporting | 27 | 10 | 8 | stop events with duration and reason, operator-entered or detected, micro-stops | notifications about a stop, the availability figure |
| Recipe Values | 13 | 0 | 4 | recipes, specifications, parameter sets, change tracking, transfer of set values | actual process values |

(Use cases + library entries + dashboard families per template from the 11 `Use Case View` notes,
generated 2026-09-27; a dashboard family with several templates counts under each.)

## 2. The 13 placement rules

| Rule | Text (shortened) |
|---|---|
| R1 | **Named subject.** The title or stated purpose names the subject: Andon/Gemba/PCB board, OEE, cycle time, downtime, alert or notification, recipe, SPC or inline measurement, process value monitoring |
| R2 | **Output boards.** A board showing output against target, production status or an overview of a line, cell, area or plant is Andon Board |
| R3 | **Reports and analysis.** A report, KPI or management report, Power BI report, export for analysis, forecast, model or cross-machine analysis is Analytics |
| R4 | **Equipment process dashboards.** Parameters and status of one kind of equipment (oven, autoclave, extruder, press, robot, dryer, washing machine) and a level-3 process overview are Process Values |
| R5 | **Energy.** Monitoring measured energy or utility values is Process Values; analysis of usage, peaks or savings is Analytics |
| R6 | **Paper to digital.** Replacing a paper or Excel record, checklist, inspection sheet, manual measurement entry, lab result entry or calendar is Manual Quality Data |
| R7 | **Automated quality.** Inline measurement, SPC, vision inspection, test and leak test results, scrap counting, jidoka and per-part traceability are Process Quality Data |
| R8 | **Parameter sets.** Recipes, specifications, set values, parameter change tracking and transfer of set values are Recipe Values |
| R9 | **Time and stops.** Cycle time, takt, loading, step or throughput time are Cycle Time; availability and efficiency figures are OEE Calculation; stop events with duration and reason are Downtime Reporting |
| R10 | **Alerts.** Alarms, notifications, tolerance deviations, maintenance-due and condition triggers that go to people are Machine Alerts |
| R11 | **Other.** Platform and IT tools, AI helpers on documents, administration, planning, mold and tool management, HR and safety administration, device and camera status, integration work |
| R12 | **Precedence.** When several rules apply, the purpose in the target text beats the title, the title's head noun beats the tool, and the order is: Recipe Values, Downtime Reporting, Machine Alerts, Andon Board, Cycle Time, OEE Calculation, Process Quality Data, Manual Quality Data, Process Values, Analytics, Other Use Cases |
| R13 | **Same solution.** A use case and a library entry or dashboard family that describe the same solution take the template recorded for the other level |

## 3. How to place a new asset (procedure)

1. Write the asset's **purpose in one sentence** (the "issue solved"). The purpose beats the title (R12).
2. Walk R1 to R11 and note every template that applies. One match: done.
3. Several matches: apply the R12 order, top to bottom; the first template in the list wins.
4. Check the "not here" column of the winner. If your asset is on that list, you mis-filed it.
5. Look for an existing asset of the same solution (R13); take its template.
6. Write the template as a tag (SPEC-03 S-03: status, template, plant) and in the use case.
7. A dashboard that fits none of the ten named templates is Other Use Cases (R11). If you are
   placing more than one asset per quarter there, the portfolio is missing a template - raise it.

**Worked placements from the dashboard notes** (inferences, to be checked by the use case owner):

| Dashboard | Placed as | By the rules | Review |
|---|---|---|---|
| Downtime Report_BMW_FAAR (Mako) | Andon Board | R9: stop events with duration and reason are Downtime Reporting | candidate for review |
| TPV 1 - Focus Parameters (Waltershausen) | Analytics | R4: parameters and status of one kind of equipment are Process Values | candidate for review |
| Availability per Machine (Qingdao) | Downtime Reporting | R9: availability figures are OEE Calculation | candidate for review |
| Downtime BM_Board (Somersworth) | Recipe Values | R9, and R12 puts Recipe Values first only if R8 applies | candidate for review |
| Autoclave Shopfloor and Process Values (Carei) | Process Values | R4 | consistent |
| Plant Andon Board (Production Overview) | Andon Board | R2 | consistent |

Placement of the 1,010 dashboard notes: Process Values 201, Analytics 149, Andon Board 146, OEE
Calculation 66, Process Quality Data 46, Machine Alerts 30, Cycle Time 22, Downtime Reporting 21,
Other 18, Recipe Values 13, Manual Quality Data 12, **unplaced 286 (28%)**. The template of a note
comes from the linked use case or, if none, a keyword hint on the title (inferred).

## 4. The 36 case groups (template x process family)

A case group is one template in one process family (Rubber, Assembly, Plastic, Metal,
cross-process, other families): the unit for which a business case can be derived. 36 groups cover
all 650 use cases. The groups for the three templates most asked about:

| Group | Cases | Delivered | Plants delivered / planned / idea / white space |
|---|--:|--:|---|
| CG-01 Process Values - Rubber | 62 | 39 | 7 / 1 / 2 / 1 |
| CG-02 Process Values - Assembly | 45 | 17 | 8 / 3 / 2 / 7 |
| CG-04 Process Values - Plastic | 34 | 23 | 6 / 1 / 1 / 6 |
| CG-09 Process Values - Metal | 26 | 5 | 4 / 2 / 3 / 3 |
| CG-19 Process Values - cross-process | 13 | 6 | 4 / 1 / 2 / 18 |
| CG-16 Process Quality Data - Assembly | 15 | 7 | 6 / 0 / 3 / 11 |
| CG-18 Process Quality Data - Rubber | 14 | 4 | 2 / 2 / 2 / 5 |
| CG-27 Process Quality Data - cross-process | 10 | 0 | 0 / 0 / 1 / 24 |
| CG-34 Process Quality Data - Metal | 9 | 1 | 1 / 1 / 3 / 7 |
| CG-36 Process Quality Data - other families | 7 | 4 | 3 / 2 / 0 / 20 |
| CG-11 Cycle Time - other families | 18 | 10 | 7 / 1 / 1 / 16 |
| CG-23 Cycle Time - Metal | 10 | 5 | 2 / 2 / 1 / 7 |

Other groups: Andon Board CG-03 (Assembly, 44 cases, 27 delivered), CG-05 (Rubber 32/17), CG-08
(Plastic 26/11), CG-10 (Metal 23/9), CG-30 (cross 9/5); Downtime CG-12 (17/12) and CG-24 (Metal
10/4); Machine Alerts CG-13 (17/9), CG-25 (Plastic 10/6), CG-31 (Rubber 9/5); OEE CG-15 (15/8),
CG-17 (Assembly 14/7); Manual Quality Data CG-14 (Rubber 16/1), CG-21 (Assembly 12/1), CG-32 (Metal
9/2), CG-33 (9/6); Recipe CG-20 (13/6); Analytics CG-22 (11/3), CG-28 (9/5), CG-29 (9/3); Other
CG-06, CG-07, CG-26, CG-35.

**Reading for a builder.**
- "White space" is the number of plants with the process family but no member: the 18 for
  Process Values cross-process and the 24 for Process Quality Data cross-process are where an
  existing asset would be adopted, not rebuilt (`SKILL.md`, "When not to build").
- Process family was **inferred for 251 use cases** that had none recorded; inferred members are
  marked in the group notes (Case Groups, Process Family Inference).
- **Recorded savings are thin**: 62 of 650 use cases carry a saving, EUR 2,384,217 in total
  (unaudited; the list does not say whether yearly); 269 delivered cases have none. Costs are
  taken as zero by owner statement of 2026-11-04. Do not quote a group's value without its
  "basis" column (Moderate / Weak / Very weak / None) - see `od-benefit-calculation`.
- Delivered use cases without a recorded saving are the cheapest evidence to collect.

## 5. Documentation standard (what "described" means)

A delivered use case is **fully described** when its plant has both a reference solution (a
library entry or archive-derived note) and a dashboard family in the same template, and archive
evidence is curated onto at least one note. **Partly** when only one exists; **bare** when the use
case note is the only description. When you deliver a dashboard, you close this gap by writing the
family note and the reference-solution link (`od-handover-and-adoption`).

## Sources

`Work-OpsDigit-Knowledge/Graph/Use Case Views/` (`template-standards.json`, the 11 views,
`Use Case Views - Standardization` not read in full), `Case Groups/Case Groups - Overview.md`,
`Dashboard Exports/Dashboard Notes/` (placement counts), read 2026-11-05.
