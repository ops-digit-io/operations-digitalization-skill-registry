---
type: Skill Reference
title: Data needs by capability
description: For each of the eleven use case capability templates, what data it reads, the department's own standard for it, how to count live which recorded use cases name no machine, and what the capability and process epic records can and cannot tell you about data. No figures.
resource: ../SKILL.md
status: draft
tags: [analytical-support-service, practice]
---

# Data needs by capability

Use this at step 1 and step 6 of the six steps: *which signals does this kind of use case
need, and which part of that is already known to be fragile?* A request arrives as "we want an
Andon board" or "we want OEE". The capability template tells you the data classes behind it,
and the department's own cluster standard tells you which agreement must exist before the data
means anything.

**Grades.**

- **Rule (department standard):** from the knowledge base's `_knowledge/30-Nodes` cluster notes
  (C01 to C12), which state "the standard we hold a use case in this cluster to". These are
  the department's statements, not independent verification. Their KPI definitions rest on
  ISO 22400-2 (see the cluster notes for which parts are verified; the formulas are not).
- **Record count:** counted live from `Case Groups` ("AI-grouped from SharePoint list fields;
  indicative arithmetic only; not reviewed by a human"). Re-count before quoting and name the
  count date.

## The eleven templates

"Members listing no machine" is a live count of the recorded plant use cases of that template
whose record links no machine. It is a **documentation fact, not a data fact**: the use case may
still read machine data. It means step 1 of the six steps cannot be answered from the use
case record and has to be asked.

| Template | What the case groups say it covers | Cluster and department standard |
|---|---|---|
| Process Values | Live machine and process parameters (temperatures, pressures, speeds, counters, energy and utility readings), process overviews per machine, line or oven, export of values | C01/C03/C07: the raw signal set that OEE reads, SPC charts and recipe comparison use. Standard for C03: control limits come from the process, distinct from specification limits |
| Andon Board | A board showing the current state of a line, cell, area or plant: Andon and Gemba boards (levels 1 to 3), production overview boards, card views with output against target, call or escalation triggers | C02: a signal must be raisable by hand **and** automatically from the machine; two-step logic (first signal asks for help without stopping the line, the second stops it if nobody came); escalation tiers with a time-boxed response; every event logged, not only displayed |
| Other Use Cases | Everything that fits none of the ten: IT platforms, AI helpers on documents, administration, planning, mold and tool management, device and camera status | C12: a catch-all; its size is a documentation measure, not a topic |
| Process Quality Data | Automated in-process quality data: inline measurements, SPC and capability, vision inspection, test results, scrap counting, jidoka stops, traceability per part or serial | C03: control limits from the process, a defined reaction plan for an out-of-control signal |
| Manual Quality Data | Digitizing quality and production data people record by hand: paper and Excel checklists, inspection sheets, lab test results | C04: digitizing the entry is not the goal; the entry has to become usable downstream |
| Machine Alerts | Alarms, notifications and tolerance-deviation alerts to people: machine faults, Teams or SMS notifications, maintenance-due triggers | C05: an alert needs a defined recipient and a defined acknowledgement |
| Analytics | Reports and analyses across machines, lines or plants: KPI reporting, Power BI reports, forecasts, machine-learning models, image analysis | C09: a cross-cutting report earns its place when it answers something no single-process dashboard can |
| OEE Calculation | OEE or its components (availability, performance, quality) per machine, line or plant | C01: show the three terms separately; agree the **ideal cycle time** and the **micro-stop recording threshold** once per line and write them down |
| Cycle Time | Cycle time, takt, loading time, step duration or throughput against a standard, including waiting times | C01: the ideal is a number agreed once; where it drifts silently everything built on it drifts (feeds the performance term of OEE) |
| Downtime Reporting | Capture and classification of stop events with duration and reason, entered by the operator or detected from machine data, including microstops | C05: an agreed downtime **reason catalogue**; without one every plant's reasons are unique and nothing rolls up |
| Recipe Values | Recipes, specifications and parameter sets: display of values, change logs, tracking of changes, transfer of set values to machines | C07: parameters and traceability are recorded together because they fail together; one-up one-down traceability at minimum |

Three further clusters, from the cluster notes, are not capability templates but matter when a
request is phrased in their words:

- **C06 predictive maintenance** : needs condition data
  over time, "gated on machine integration more directly than any other cluster".
- **C08 energy management** : consumption must be **attributed** to a
  line, machine or product; a plant-level meter reading identifies no action; the baseline
  matters most.
- **C10 generative and agentic AI** : "the data the model
  needs has to exist and be reachable", gated on the same integration and digitization as the
  rest. C11 digital twin: reserved, no use case tagged.

## How to use the table at the data check

1. Identify the template (or the cluster) the request belongs to. If it fits only "Other Use
   Cases" or C12, ask for a nameable need before checking data (see `od-use-case-intake-triage`).
2. Read the standard column and check the **agreement** it names exists at this plant before
   checking any signal: ideal cycle time and micro-stop threshold (C01), reason catalogue
   (C05), recipient and acknowledgement (C05), control-limit source and reaction plan (C03).
   These are definition gaps, not data gaps (`failure-modes.md`).
3. For *Manual Quality Data* the data does not come from a machine; use
   `non-machine-data-sources.md`.
4. For *Process Values*, *Andon*, *Process Quality* and *Alerts*, the machine path applies:
   walk the six steps and use `machine-list-completeness.md`
   for the plant.
5. Check step 6 against the delivered cases in your template (count the productive or
   implemented ones live; see `od-use-case-standardization` and the reference library). Many
   requests are already answered at another plant.

## What the capability and process epic records tell you (and do not)

- **Capability Epics are template shells.** Each is one template instantiated for one plant
  (category `GROUP`, status `GROUP`). Many have no member use case, and priority, potential,
  development, implementation and handover fields are typically `UNKNOWN` or `NOT STARTED`.
  **Do not read an empty or `NOT STARTED` capability epic as "this plant has no such use
  case"**: the use cases hang off the shell, and the shell fields were not maintained. To see
  what a plant has, count the member use cases live.
- **Process Epics are the process-group shells** (a process group at a plant, for example
  assembly, rubber vulcanization, metal bending). They give the process family, which the case
  groups use to group use cases; where a use case has no recorded family it was inferred by a
  model - treat that as an indication, not a verification of any single case (method note
  `Case Groups/Process Family Inference`).
- **Neither carries a blocker or a data source.** Blocker and comment fields are empty on the
  shells. The place for a data dependency is the use case record
  (`MACHINE INTEGRATION` is a recorded dependency class on savings rows) and the Machine List.

## What stays open

⟨Which signals each template needs as a minimum (names, units, sampling). The cluster notes
state standards, not signal lists; the signal catalogue belongs to
`od-signal-standardization`. Who could supply it: DBVE with the IIAE.⟩

## Data items named by the standardization knowledge base

The knowledge base's source note `_knowledge/90-Sources/org-analysis/usecase-standardization-knowledgebase`
(compiled from public references; its classification run is older than the cluster notes, so
its groupings may differ) lists requirements per cluster. Those that name
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

- Knowledge base `_knowledge/30-Nodes` cluster notes C01 to C12 and the template notes.
- Knowledge base `Case Groups` (overview and group notes; need-and-scope rows; member and machine counts).
- Knowledge base `Graph/Capability Epics` and `Graph/Process Epics`.
- Department note *Use case standardization* (`_knowledge/10-Department`).
