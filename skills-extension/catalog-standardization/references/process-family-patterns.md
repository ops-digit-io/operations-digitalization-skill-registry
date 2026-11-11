---
type: Skill Reference
title: Process family patterns
description: What a use case looks like per process family (rubber, plastic, metal, assembly, cross-process) - the process groups, the capabilities that usually apply, the data needed, how much standardization to expect and the traps. Pattern only, no counts. Open it when you place a use case, judge whether it can be a standard, or brief a plant on what peers usually ask for.
resource: ../SKILL.md
status: draft
tags: [all, practice]
---
# Process family patterns

Source: knowledge base `Graph/Process Groups` (one note per process group, with an authored definition and the target types aimed at it),
`Graph/Use Case Views` (the capability pages and `Use Case Views - Standardization`), `Case Groups` (including `Process Family
Inference`) and the workshop requirement note for the shared vulcanization use case (cited on the Rubber Vulcanization
process-group note). All AI-drafted or authored domain knowledge, not reviewed by a human. This file holds **no counts, plant lists
or savings**; read those live and quote the read date.

## The two axes

A plant use case sits on a **capability** (eleven templates, see `catalog-usecase` `references/template-coverage.md`) and on a
**process group** inside a **family**. The family tells you what the machine does; the capability tells you what the screen does.
Standardization potential comes from the combination: a capability that does not depend on the process (a status board) travels
across families; a capability that reads process parameters travels only inside one process group.

| Family | Process groups in the template (names as in the knowledge base) |
|---|---|
| Rubber | Calendering and wrapping; Extrusion braided; Extrusion knitted; Injection molding; Ultraflex line; Vulcanization; Others |
| Plastic | Blow molding; Extrusion; Extrusion over a knitted layer; Injection molding automated and complex; Injection molding non-automated and simple; Thermoforming automated; Thermoforming non-automated; Welding; Others |
| Metal | Bending; Forming (stamping, drawing); Hydroforming; Welding; Laser welding; Brazing flame; Brazing induction; Furnace; Others |
| Assembly | Simple; Complex; Testing; Others |
| Cross-process | no family recorded and none inferable: the use case is a pattern, not a property of one process |

The "Others" groups are catch-alls, like the capability "Other Use Cases". Do not create a new process group to fit one plant.
Several groups have no use case recorded directly against them in the knowledge base: that means "not recorded", not "no demand".

## Pattern per family

Read the columns as a prior for an undocumented use case, to be checked against the plant's machine list.

### Rubber

| Aspect | Pattern |
|---|---|
| Typical capabilities | Process Values (ovens, autoclaves, extruders), Machine Alerts (tolerance deviation), Andon Board per machine of a line, Cycle Time of the curing cycle, Recipe Values, energy and utility monitoring |
| Data needed | Vulcanization: temperature, pressure, a generated cycle id and the cut of each cycle into phases (pre-heating, main heating, cooling, optional water cooling) with start, end and duration; set values against recipe values with soft and specification limits; a rating of violations by a rule set. Extrusion and braiding: line speed, zone temperatures, per-machine states along the line, yarn or break events, inline images where a camera exists. Energy: meter values, steam and pressure readings |
| Standardization potential | Highest for vulcanization and extrusion: the knowledge base's workshop material proposes a process-specific data model per core process, so that the same views serve all machines of one process at several plants. Equipment of the same kind (an oven type, an autoclave) repeats inside a plant: build once per equipment type, then instantiate |
| Traps | One use case recorded per oven or per autoclave (the same pattern counted many times): group by equipment type before you judge breadth. Batch curing (cycle-based) and continuous ovens (time-based) need different cycle definitions: do not reuse one. The autoclave start precondition (inner temperature below a limit or a pre-heating program without product) is a process rule, not a dashboard detail: ask for it. Energy monitoring versus energy analysis is split between Process Values and Analytics by rule R5 |

### Plastic

| Aspect | Pattern |
|---|---|
| Typical capabilities | Blow molding is the widest: Andon Board, Cycle Time, availability, manual data input, Machine Alerts, Process Values, quality losses, SPC, parameter-change monitoring. Injection molding: cycle time, shot or material weight reports, parameter tracking. Thermoforming and welding: fewer, SPC and availability. Material drying and conveying: monitoring and alerts |
| Data needed | Cycle time per machine, inline or off-line measurement of geometry, set versus actual machine parameters and their change log, per-cavity results where the tool has cavities, material and dryer readings |
| Standardization potential | Medium to high within blow molding and injection molding; the automation level decides the data path. Automated complex injection molding has robot, in-mold sensors and multi-cavity data: richer, but each tool differs. Manually tended simple injection molding has little machine signal: it tends to become manual data input |
| Traps | Per-cavity quality needs a cavity key in the data; without it the SPC chart averages the problem away. A parameter-change monitor is a Recipe Values or Process Values case depending on whether set values are managed (R8) or only watched: use the precedence rule R12. Camera and inline measurement systems often need extra hardware and a network change: ask before promising a date |

### Metal

| Aspect | Pattern |
|---|---|
| Typical capabilities | Cycle Time and Downtime Reporting around presses, bending and cutting cells; Machine Alerts on forming equipment; Process Values on furnaces and brazing (temperature, energy); Recipe Values for furnace programs; hourly output boards for cells; Process Quality Data for bending angle and inspection reduction |
| Data needed | Stroke or cycle counters and run state, stop events with reason, furnace temperature profile and program id, induction or flame process parameters where measured, measured angle or dimension per part |
| Standardization potential | Medium. Forming and cutting cells repeat and suit cycle time, downtime and availability. Brazing and welding vary by method: flame brazing is manual and usually gives availability only; induction and laser have measurable process data |
| Traps | A downtime use case needs an agreed reason taxonomy before it needs a tool: "definitions and approvals still to be agreed" is the recurrent blocker, and it is governance, not technology. "Metal Others" absorbs everything; place by the precedence rule, not by habit. Bending-angle correction and inspection reduction are quality use cases that need a data model and tooling the plant often lacks |

### Assembly

| Aspect | Pattern |
|---|---|
| Typical capabilities | Andon Board (the most numerous: cell, line and Gemba boards at levels 1 to 3), Cycle Time, OEE, Process Quality Data (end-of-line test, leak test, screwing, image data), Manual Quality Data, traceability per serial number, label and inventory control |
| Data needed | Part counters and OK/NOK per hour against target, station cycle time, test results per serial (leak rate, torque, electrical), image per part, scrap and rework with reason, operator-entered inspection data where the station is manual |
| Standardization potential | Highest across plants for status boards and cycle time (the assembly cell is the most repeated variant). Testing is the quality gate and the richest data source; test benches differ by product, so the data model should carry the serial key and a characteristic list, not a fixed screen |
| Traps | Cells are often integrated through the customer's or the supplier's own controller: access to the machine list or PLC is the most frequent blocker. Added hardware (counters, scanners, screwing controllers) is a rollout item, not a configuration item. Labelling and traceability systems can trigger a Cyber Security approval of their own. Complex assembly is the highest value density but the most station-specific: standardize the board and the test-result record, not the station |

### Cross-process

A use case with no family is usually a capability pattern: a status board, an OEE view, a report, an analysis, a notification
channel. These travel best and are the natural first candidates for a library entry. For these the inferred family only describes
where the pattern is deployed, not a property of the pattern; say so when you quote a family for one.

## What the family inference is worth

The knowledge base infers a family for use cases that have none recorded, from title, outcome, machine names and dashboard content, with a
probability threshold. Its cross-validation accuracy on recorded cases is high but, as the knowledge base notes say, it is not verification
of a single case. Rules for use:

- Treat an inferred family as a pointer; mark it "inferred" in any record and confirm with the Plant ME before it drives a decision.
- Use cases with no machine, dashboard or process term stay open: do not force a family on them.
- AI use cases and cases without a plant are left alone by the method; do not read their missing family as a gap.

## What recurs as a blocker, by capability (themes, not counts)

Use this to ask the right question early (step 21 intake, step 3 requirements). Themes are the knowledge base's keyword reading of recorded
blocker texts, not verified.

| Capability | Blocker themes to expect | First question |
|---|---|---|
| Andon Board, Process Values, Machine Alerts, Downtime Reporting | machine list or PLC access; third-party system access; added hardware | Is the machine in the machine list and integrated? Who owns the PLC access? |
| Process Quality Data | tools, platform or data model not available; added hardware (camera, inline gauge); connectivity | Which measurement channel, with which key (serial, cavity)? |
| Manual Quality Data | missing details or scope; access to a quality or ERP system | Which sheet, which fields, who signs? |
| Machine Alerts | definitions and approvals still to be agreed; third-party channel (chat, SMS) | Who is told, under which rule, who acknowledges? |
| OEE Calculation | missing scope; definitions to agree; people or capacity | Which OEE definition, and are the stop and quality sources there? |
| Recipe Values | tools or data model; approvals | Is the value only shown, or written to the machine? |
| Analytics, Other Use Cases | tools or platform not available; missing scope; third-party systems | Is this production data at all, or a document or office use case? |

## Using this in the chain

- Step 21 intake and `catalog-standardization` step 2: place the use case on capability and process group with R1 to R13; use the
  family row as the prior for data and blockers.
- Step 24 ranking: breadth is counted per equipment type or per pattern, not per recorded row (see the rubber trap).
- Step 3 requirements: start from the family's "data needed" row and record only the plant's deltas.
- AI agent: may propose capability, process group and an inferred family with the evidence (title, machine names) and mark every
  proposal "to confirm with the Plant ME". It does not decide the family of a record.
