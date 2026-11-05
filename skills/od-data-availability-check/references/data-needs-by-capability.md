---
type: Skill Reference
title: Data needs by capability
description: For each of the eleven use case capability templates, what data it reads, the department's own standard for it, how many recorded use cases name no machine at all, and what the capability and process epic records can and cannot tell you about data.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [analytical-support-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Data needs by capability

Use this at step 1 and step 6 of the six steps: *which signals does this kind of use case
need, and which part of that is already known to be fragile?* A request arrives as "we want an
Andon board" or "we want OEE". The capability template tells you the data classes behind it,
and the department's own cluster standard tells you which agreement must exist before the data
means anything.

**Grades.**

- **Rule (department standard):** from the vault's `_knowledge/30-Nodes` cluster notes
  (C01 to C12), which state "the standard we hold a use case in this cluster to". These are
  the department's statements, not independent verification. Their KPI definitions rest on
  ISO 22400-2 (see the cluster notes for which parts are verified; the formulas are not).
- **Record count:** counted from `Case Groups` (36 groups, generated 2026-11-04, "AI-grouped
  from SharePoint list fields; indicative arithmetic only; not reviewed by a human") on
  2026-11-05.

## The eleven templates

"Members listing no machine" is the number of recorded plant use cases of that template whose
record links no machine. It is a **documentation fact, not a data fact**: the use case may
still read machine data. It means step 1 of the six steps cannot be answered from the use
case record and has to be asked.

| Template | Plant use cases | Delivered (productive or implemented) | Members listing no machine | What the case groups say it covers | Cluster and department standard |
|---|--:|--:|--:|---|---|
| Process Values | 180 | 90 | 97 | Live machine and process parameters (temperatures, pressures, speeds, counters, energy and utility readings), process overviews per machine, line or oven, export of values | C01/C03/C07: the raw signal set that OEE reads, SPC charts and recipe comparison use. Standard for C03: control limits come from the process, distinct from specification limits |
| Andon Board | 134 | 69 | 63 | A board showing the current state of a line, cell, area or plant: Andon and Gemba boards (levels 1 to 3), production overview boards, card views with output against target, call or escalation triggers | C02: a signal must be raisable by hand **and** automatically from the machine; two-step logic (first signal asks for help without stopping the line, the second stops it if nobody came); escalation tiers with a time-boxed response; every event logged, not only displayed |
| Other Use Cases | 73 | 27 | 63 | Everything that fits none of the ten: IT platforms, AI helpers on documents, administration, planning, mold and tool management, device and camera status | C12: a catch-all; its size is a documentation measure, not a topic |
| Process Quality Data | 55 | 16 | 34 | Automated in-process quality data: inline measurements, SPC and capability, vision inspection, test results, scrap counting, jidoka stops, traceability per part or serial | C03: control limits from the process, a defined reaction plan for an out-of-control signal |
| Manual Quality Data | 46 | 10 | 39 | Digitizing quality and production data people record by hand: paper and Excel checklists, inspection sheets, lab test results | C04: digitizing the entry is not the goal; the entry has to become usable downstream |
| Machine Alerts | 36 | 20 | 18 | Alarms, notifications and tolerance-deviation alerts to people: machine faults, Teams or SMS notifications, maintenance-due triggers | C05: an alert needs a defined recipient and a defined acknowledgement |
| Analytics | 29 | 12 | 20 | Reports and analyses across machines, lines or plants: KPI reporting, Power BI reports, forecasts, machine-learning models, image analysis | C09: a cross-cutting report earns its place when it answers something no single-process dashboard can |
| OEE Calculation | 29 | 15 | 15 | OEE or its components (availability, performance, quality) per machine, line or plant | C01: show the three terms separately; agree the **ideal cycle time** and the **micro-stop recording threshold** once per line and write them down |
| Cycle Time | 28 | 15 | 9 | Cycle time, takt, loading time, step duration or throughput against a standard, including waiting times | C01: the ideal is a number agreed once; where it drifts silently everything built on it drifts (feeds the performance term of OEE) |
| Downtime Reporting | 27 | 16 | 13 | Capture and classification of stop events with duration and reason, entered by the operator or detected from machine data, including microstops | C05: an agreed downtime **reason catalogue**; without one every plant's reasons are unique and nothing rolls up |
| Recipe Values | 13 | 6 | 6 | Recipes, specifications and parameter sets: display of values, change logs, tracking of changes, transfer of set values to machines | C07: parameters and traceability are recorded together because they fail together; one-up one-down traceability at minimum |
| **Total** | **650** | **296** | **377** | | |

Three further clusters, from the cluster notes, are not capability templates but matter when a
request is phrased in their words:

- **C06 predictive maintenance** (9 use cases at 4 plants, 1 productive): needs condition data
  over time, "gated on machine integration more directly than any other cluster".
- **C08 energy management** (16 use cases at 11 plants): consumption must be **attributed** to a
  line, machine or product; a plant-level meter reading identifies no action; the baseline
  matters most.
- **C10 generative and agentic AI** (22 use cases at 7 plants, 0 productive): "the data the model
  needs has to exist and be reachable", gated on the same integration and digitization as the
  rest. C11 digital twin: reserved, no use case tagged.

## How to use the table at the data check

1. Identify the template (or the cluster) the request belongs to. If it fits only "Other Use
   Cases" or C12, ask for a nameable need before checking data (see `od-use-case-intake-triage`).
2. Read the standard column and check the **agreement** it names exists at this plant before
   checking any signal: ideal cycle time and micro-stop threshold (C01), reason catalogue
   (C05), recipient and acknowledgement (C05), control-limit source and reaction plan (C03).
   These are definition gaps, not data gaps ([`failure-modes.md`](failure-modes.md)).
3. For *Manual Quality Data* the data does not come from a machine; use
   [`non-machine-data-sources.md`](non-machine-data-sources.md).
4. For *Process Values*, *Andon*, *Process Quality* and *Alerts*, the machine path applies:
   walk the six steps and use [`machine-list-completeness.md`](machine-list-completeness.md)
   for the plant.
5. Check step 6 against the delivered count in your template: 296 delivered cases already
   exist in the same eleven templates (see `od-use-case-standardization` and the reference
   library). Many requests are already answered at another plant.

## What the capability and process epic records tell you (and do not)

- **Capability Epics (355 notes) are template shells.** Each is one template instantiated
  for one plant (11 templates across 32 plants, category `GROUP`, status `GROUP`). 123 of the
  355 have at least one member use case; 232 have none. 349 carry priority and potential
  `UNKNOWN`; development and implementation are `NOT STARTED` on 353; handover is `NOT STARTED`
  on all 355. **Do not read an empty or `NOT STARTED` capability epic as "this plant has no
  such use case"**: the use cases hang off the shell, and the shell fields were not maintained.
  Counting with members: Process Values 19, Andon Board 18, Manual Quality Data 13,
  Process Quality Data 13, Other Use Cases 12, Analytics 10, Downtime Reporting 10, Machine
  Alerts 9, Cycle Time 7, OEE Calculation 7, Recipe Values 5.
- **Process Epics (96 notes) are the process-group shells**, 23 process groups at 18 plants
  (largest: Assembly Complex 11, Assembly Testing 9, Rubber Vulcanization 9, Rubber Others 8,
  Metal Bending 6); 84 of 96 have a member. They give the process family, which the case
  groups use to group use cases; where a use case has no recorded family 251 of 334 were
  inferred by a model (87% overall accuracy on recorded cases, not a verification of any
  single case; method note `Case Groups/Process Family Inference`).
- **Neither carries a blocker or a data source.** Blocker and comment fields are empty on the
  shells. The place for a data dependency is the use case record
  (`MACHINE INTEGRATION` is a recorded dependency class on savings rows) and the Machine List.

## What stays open

⟨Which signals each template needs as a minimum (names, units, sampling). The cluster notes
state standards, not signal lists; the signal catalogue belongs to
`od-signal-standardization`. Who could supply it: DBVE with the IIAE.⟩

## Data items named by the standardization knowledge base

The vault's source note `_knowledge/90-Sources/org-analysis/usecase-standardization-knowledgebase`
(generated 2026-08-24; compiled from public references, classification run older than the
cluster notes, so its use case counts differ) lists requirements per cluster. Those that name
**data** are the ones to check at step 1 and step 5 (grade: published-literature-derived, not
verified here):

| Cluster | Data the checklist names |
|---|---|
| C01 OEE | Run and stop states, actual against ideal cycle time, good and defective unit counts, collected automatically or semi-automatically (manual entry is a valid fallback that degrades accuracy) |
| C03 SPC | A characteristic with specification limits and statistically derived control limits; data of a stabilised process |
| C04 Manual data | Mandatory fields matched to what the downstream use case needs |
| C05 Downtime | A plant-wide reason taxonomy (not free text); downtime written to a historian; "starved" and "blocked" states distinguishable from a fault |
| C06 Predictive maintenance | Sensing matched to the failure mode (vibration, infrared, oil analysis, motor current); a link to a maintenance management system |
| C07 Recipe, traceability | Recipes held centrally and version-controlled; a unique scannable identifier per lot or unit; forward and backward queries; retention period |
| C08 Energy | Metering at line or cell level, not building level; baseline per shift or product; energy data on the same timeline as OEE and downtime |
| C10 AI | An explicit data-access grant from IT before any live connection |

⟨The signal names and sampling rates behind these items. Who could supply it: DBVE with the
IIAE; see `od-signal-standardization`.⟩

## Sources

- Vault `_knowledge/30-Nodes` cluster notes C01 to C12 and the template notes (read 2026-11-05).
- Vault `Case Groups` (overview and 36 group notes; need-and-scope rows; member and machine
  counts totalled 2026-11-05).
- Vault `Graph/Capability Epics` (355) and `Graph/Process Epics` (96), counted 2026-11-05.
- Department note *Use case standardization* (`_knowledge/10-Department`).
