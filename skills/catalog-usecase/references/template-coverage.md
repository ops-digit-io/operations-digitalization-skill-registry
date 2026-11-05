---
type: Skill Reference
title: Template coverage
description: Guidance, no figures - the eleven capability templates, how to find live which plants run or want each one, what data each template needs, the boundary rules for placing a request, and the typical components of a matching screen. Open it to find a peer plant and the preconditions for a match.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Template coverage

This file holds **no counts, plant lists or rankings**. Sources to read live: vault `Graph/Use Cases` (plant use cases;
frontmatter fields `use_case_template`, `status`, `plant`, `scalable`), `Graph/Use Case Views` (the eleven template pages,
`Use Case Views.md`, `Use Case Views - Standardization.md`) and `Graph/Target Types`. The template pages are AI-drafted from a
graph export and not reviewed by a human; state the export date when you quote them.

## The eleven templates

Process Values, Andon Board, Other Use Cases, Process Quality Data, Manual Quality Data, Machine Alerts, Analytics, OEE
Calculation, Cycle Time, Downtime Reporting, Recipe Values.

## How to read coverage live

- **"Delivered"** means status `IMPLEMENTED` or `PRODUCTIVE` (the template pages use the same rule).
- Filter `Graph/Use Cases` by `use_case_level = plant use case` and `use_case_template`. Per template, count: use cases
  delivered versus all, distinct plants that want it, distinct plants with a delivered use case, those flagged `scalable`.
- Exclude the non-plant labels the `plant` field also holds (`AI`, `All_Plants`, `General`, `Generic`) and normalise spelling
  variants of plant names before counting plants.
- Reference solutions and dashboard families per template come from the template pages (a dashboard family that carries
  several templates counts under each). The CSP split counts library entries only (see
  [library-and-csp-state.md](library-and-csp-state.md)).
- Documentation is uneven across templates: for each plant-and-template pair with a delivered use case, note whether it is
  described by a reference solution and a dashboard family, or only by the use case note. A thinly documented template is a
  weak match source however many plants run it.

Patterns to expect when you read it: the status-board and process-value patterns are usually spread over many plants, the
recipe, manual-quality, analytics and OEE patterns over few; the gap between "wanted" and "delivered" is where a catalog entry
would serve first.

## Peer plants per template

To tell a requesting plant which plant to call: list the plants with a delivered plant use case in the requested template
(live filter above). The note of that plant use case holds the owner role and the data path. To find where it is wanted but not
delivered: plants with a plant use case in the template and none delivered.

## What each template needs - the preconditions for branch 1a

From the "standard data and realization" block of each template page (target types and machine links counted by the graph;
keyword counts, not verified). Use with `od-data-availability-check`; read the actual counts and controller vendors on the
page, they are not repeated here.

| Template | Target types it needs to see (typical) |
|---|---|
| Andon Board | Andon Board, Machine Availability, Cycle Time Monitoring, Quality Losses |
| Process Values | Process Values, Machine Availability, Cycle Time Monitoring, Process Set Values, SPC Charts |
| Machine Alerts | Notification, Process Values, Cycle Time Monitoring, Machine Availability |
| Process Quality Data | SPC Charts, Process Values, Quality Losses, Cycle Time Monitoring, Image Data |
| Cycle Time | Cycle Time Monitoring, Process Values, Machine Availability, Quality Losses |
| Downtime Reporting | Machine Availability, Cycle Time Monitoring, Andon Board, Quality Losses |
| OEE Calculation | Machine Availability, Andon Board, Cycle Time Monitoring, Process Values |
| Analytics | Process Values, Energy Data, Manual Quality Data Input |
| Manual Quality Data | SPC Charts, Manual Data Input, Quality Losses, Manual Quality Data Input |
| Recipe Values | Process Set Values, Process Values, Machine Availability |
| Other Use Cases | Energy Data, Process Values, Notification |

Two readings for the match:

- A **Cycle Time**, **Downtime Reporting**, **OEE** or **Andon** match needs a *Machine Availability* or *Cycle Time
  Monitoring* signal; check these two first on the machine.
- Where the share of linked machines recorded as integrated is low for the template (read it on the template page), a
  plant's machine is more likely to land on branch **1b** than on 1a. A blank integration status is unknown, not "No".

## Which template does the request belong to

Apply the placement rules of `Use Case Views - Standardization` (R1 to R13) in the order of rule R12: Recipe Values, Downtime
Reporting, Machine Alerts, Andon Board, Cycle Time, OEE Calculation, Process Quality Data, Manual Quality Data, Process
Values, Analytics, Other Use Cases. The purpose stated in the request beats the title. Short boundary table (from the
template pages):

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

A guide for what a plant should expect to see, not a requirement (the template pages list the components found in the
dashboard families' descriptions; read them there): Andon Board - status or state bar, per-shift breakdown, pie or donut,
table or log, target comparison. Cycle Time - bar chart, per-shift breakdown, status bar, table or log. Downtime Reporting -
status bar, trend, per-shift, table or log. Machine Alerts - table or log, bar chart, gauge or KPI tile. OEE - status bar,
table or log, per-shift, gauge or KPI tile. Process Values - trend, table or log, status bar, bar chart. Process Quality Data -
table or log, bar chart, status bar, trend. Figures a template page names most often: Andon - output against target, cycle
time, OK and NOK parts, availability; OEE - OEE, availability; Downtime - downtime.

## Open

- ⟨Which of the eleven templates the OD lead wants offered for self-service first⟩ - the live coverage shows where the data is
  thickest, not what OD has decided.
- ⟨Whether the `scalable` flag may serve as the entry gate for candidates⟩ - OD lead.
