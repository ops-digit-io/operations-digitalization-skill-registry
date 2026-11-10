---
type: Skill Reference
title: Capability templates and placement
description: The 11 use case templates a dashboard or report is filed under, the 13 placement rules and their precedence, how case groups work, and how to place a new asset so it is counted once. Method only - no member counts, savings or per-group tables; re-count on the live views.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [analytical-support-service, practice, templates]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Capability templates and placement

An asset that is not placed in a template is not counted in the portfolio. This file is the rule
set (`Graph/Use Case Views/template-standards.json`, "AI-drafted; not reviewed by a human"; the
Standardization note lists the cases for review), so the key user can file a new dashboard the same
way existing use cases and dashboards were filed. The rules **describe what recorded placements
mostly do**; they are not yet a decision of the department. Placement itself is
`od-use-case-standardization`'s job; this file is what `od-analytics-asset-build` needs when it
builds the asset.

**Sizes are not held here.** The number of use cases, library entries and dashboard families per
template, and the number of case groups, are in the `Use Case View` notes and `Case Groups -
Overview` in the work vault. Re-count there and quote a figure only with its date.

## 1. The 11 templates

| Template | One line: belongs here | Not here (go to) |
|---|---|---|
| Process Values | live machine and process parameters, process overviews per machine, line or oven, utility readings | SPC (Process Quality Data), set values (Recipe Values), cross-machine analysis (Analytics) |
| Andon Board | a visual board of current status of a line, cell, area or plant; Andon/Gemba levels 1-3, production overview, card view, output against target | alerts as messages (Machine Alerts), stop log (Downtime Reporting), the OEE figure (OEE Calculation) |
| Other Use Cases | catch-all: IT tools, AI helpers on documents, planning, device and camera status | anything that fits a named template |
| Process Quality Data | automatic in-process quality: inline measurement, SPC and capability, vision, test results, scrap, jidoka, per-part traceability | data typed by hand (Manual Quality Data) |
| Manual Quality Data | digitising what people record by hand: checklists, inspection sheets, lab results, calendars | automatic collection |
| Machine Alerts | alarms and notifications sent to people or shown as an alert list; tolerance alerts; maintenance-due | status-only boards, stop logs |
| Analytics | reports and analyses across machines, lines or plants; KPI and Power BI reports; forecasts; models | live displays of one machine, AI helpers on documents |
| OEE Calculation | OEE or its components per machine, line or plant, availability tracking | stop events (Downtime Reporting), cycle-time analysis, boards without an OEE figure |
| Cycle Time | cycle time, takt, loading time, step or throughput time against a standard | downtime, the OEE performance figure as a whole |
| Downtime Reporting | stop events with duration and reason, operator-entered or detected, micro-stops | notifications about a stop, the availability figure |
| Recipe Values | recipes, specifications, parameter sets, change tracking, transfer of set values | actual process values |

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
7. A dashboard that fits none of the ten named templates is Other Use Cases (R11). If you keep
   placing assets there, the portfolio is missing a template - raise it.

**Worked placements (illustrative; inferences to be checked by the use case owner):**

| Dashboard (illustrative description) | Recorded as | By the rules | Review |
|---|---|---|---|
| A downtime report with detected stops and operator reasons | Andon Board | R9: stop events with duration and reason are Downtime Reporting | candidate for review |
| An extrusion-line focus-parameter board | Analytics | R4: parameters and status of one kind of equipment are Process Values | candidate for review |
| An availability-per-machine board | Downtime Reporting | R9: availability figures are OEE Calculation | candidate for review |
| A blow-moulding downtime board | Recipe Values | R9, and R12 puts Recipe Values first only if R8 applies | candidate for review |
| An autoclave shopfloor and process-value board | Process Values | R4 | consistent |
| A plant production-overview Andon board | Andon Board | R2 | consistent |

Expect a share of dashboard notes to be **unplaced**; the template of a note comes from the linked use
case or, if none, a keyword hint on the title (inferred). Measure the share on the current notes.

## 4. Case groups (template x process family)

A case group is one template in one process family (Rubber, Assembly, Plastic, Metal, cross-process,
other families): the unit for which a business case can be derived. Every use case belongs to
exactly one group. Look up the groups and their members in `Case Groups/Case Groups - Overview.md`
(per group: cases, delivered, plants delivered / planned / idea / white space).

**Reading for a builder.**
- "White space" is the number of plants with the process family but no member. Where white space is
  large (typically in cross-process groups), an existing asset would be adopted, not rebuilt
  (`SKILL.md`, "When not to build").
- Process family may have been **inferred** for use cases that had none recorded; inferred members
  are marked in the group notes (Case Groups, Process Family Inference).
- **Recorded savings are thin and unaudited**: only a minority of use cases carry a saving, the list
  does not say whether yearly, and costs were taken as zero by owner statement. Do not quote a
  group's value without its "basis" column (Moderate / Weak / Very weak / None) - see
  `od-benefit-calculation`; look the amounts up there, not here.
- Delivered use cases without a recorded saving are the cheapest evidence to collect.

## 5. Documentation standard (what "described" means)

A delivered use case is **fully described** when its plant has both a reference solution (a library
entry or archive-derived note) and a dashboard family in the same template, and archive evidence is
curated onto at least one note. **Partly** when only one exists; **bare** when the use case note is
the only description. When you deliver a dashboard, you close this gap by writing the family note and
the reference-solution link (`od-handover-and-adoption`).

## Sources

`Work-OpsDigit-Knowledge/Graph/Use Case Views/` (`template-standards.json`, the 11 views),
`Case Groups/Case Groups - Overview.md`, `Dashboard Exports/Dashboard Notes/`. Read 2026-11-05; used
for rules only.
