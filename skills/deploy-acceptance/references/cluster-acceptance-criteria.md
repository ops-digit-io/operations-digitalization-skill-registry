---
type: Skill Reference
title: Cluster acceptance criteria
description: Guidance, no figures. For each use case cluster, the department's own standard turned into user acceptance items - what the plant owner should be able to see and do before the use case counts as accepted - with the verified external definitions the cluster notes rest on.
resource: ../SKILL.md
status: draft
tags: [project-support-consultancy, practice]
---

# Cluster acceptance criteria

UAT needs "a decision rule stated before the run" (`test-structure.md`).
For a dashboard or analytics asset the rule must come from somewhere. The department's cluster
notes state, per cluster, "the standard we hold a use case in this cluster to". This file
turns each standard into acceptance items a plant owner can check. The requirements side is
`funnel-requirements`; this is the receiving side.

**Grades.**

- **Standard (department):** the statement in the cluster note (`_knowledge/30-Nodes`, C01 to
  C12; each note says the full definition, KPI set and requirements checklist live in the
  standardization knowledge base, which was not read here).
- **Acceptance item (suggested):** this analysis restates the standard as a check. A proposal
  for the DBVE and the plant owner to confirm.
- **External, verified in the knowledge base:** definitions from ISO 22400-2 in the cluster note C01 (time
  elements only; **the KPI formulas are not verified there**; do not quote them).

Portfolio sizes per cluster are not kept here. Look them up on the live cluster notes
(`_knowledge/30-Nodes`) and quote their date.

## The clusters in use

| Cluster | Standard (department) | Acceptance items (suggested) |
|---|---|---|
| **C01 Real-time line and OEE monitoring** | OEE is availability times performance times quality; the use case shows the **three separately**, not a blended percentage. Two things are agreed once and written down per line: the **ideal cycle time** and the **micro-stop recording threshold**. OEE is a loss-diagnosis tool per asset, not a league table across shifts or plants | The three terms are visible separately. The ideal cycle time and the micro-stop threshold are written down for the line and the plant owner can name them. The dashboard is not used to rank shifts or plants. A change to either number leaves a trace |
| **C02 Digital Andon, Gemba and escalation** | A signal can be raised **by hand and automatically from the machine**. Two-step logic: the first signal asks for help without stopping the line; the second stops it if nobody came. Escalation tiers each have a time-boxed response. **Every event is logged**, not only displayed | Both trigger paths are tested. The two-step behaviour is shown on a real line. Each tier's time box is written down. An event raised in the test appears in the log after the board is closed |
| **C03 SPC and in-process quality** | Control limits come from the **process itself** and are distinct from the specification limits. A defined **reaction plan** exists for an out-of-control signal | The chart shows control limits and specification limits as different lines, with their source. The reaction plan is named and the person who acts is named. A test out-of-control point triggers the reaction |
| **C04 Manual data digitization** | Digitizing the entry is not the goal; the entry has to become **usable downstream**. A digital form nothing reads is the paper form with extra steps | Somebody downstream reads the entry in the plant's routine within the test period. The paper or spreadsheet it replaces is switched off or has a date to switch off |
| **C05 Downtime reporting and machine alerts** | An **agreed downtime reason catalogue**; without it every plant's stop reasons are unique and nothing rolls up. Alerts need a **defined recipient and a defined acknowledgement** | The catalogue in the tool is the agreed one. A test stop is classified by an operator. A test alert reaches the named recipient and is acknowledged. The micro-stop threshold from C01 is applied |
| **C06 Predictive maintenance** | A prediction has to reach a **maintenance plan** to be worth anything; it needs condition data over time | The history length in the data platform covers what the model needs (check the earliest integration date). A prediction in the test period appears in a maintenance plan or is explicitly declined by the planner |
| **C07 Recipe and traceability** | Which parameters a product was made with, and follow-back **one up, one down at minimum**. Parameter changes are logged; parameters and traceability fail together | A recipe change in the test is logged. A test unit is traced one step up and one step down. The recipe value shown equals the value on the machine |
| **C08 Energy management** | Consumption is **attributed** to a line, machine or product; a plant-level meter identifies no action. The baseline matters most | The attribution target is named. The baseline period and its source are written down before the saving is claimed |
| **C09 Analytics and cross-cutting reporting** | The report answers a question **no single-process dashboard can**. Much of what lands here is better as an addition to an existing dashboard | The question is stated; the plant owner confirms no existing dashboard answers it |
| **C10 Generative and agentic AI** | The data the model needs has to exist and be reachable | The data availability verdict (`mi-data-availability` (`../../mi-data-availability/SKILL.md`))) is attached and shows no unproven step |
| C12 Other and plant-specific | A catch-all; its size is a documentation signal | Name the nearest cluster and apply its items; if none fits, the acceptance items come from the requirement itself |
| C11 Digital twin and simulation | Reserved; check whether any use case is tagged | |

## What every cluster shares in the record

- **Delivery status.** Use cases move idea, planned, implemented, productive (and stopped).
  `IMPLEMENTED` and `PRODUCTIVE` are different claims; the gap between built and used is what
  acceptance and adoption exist to close. Count the gap on the live use case list (department
  note *Use case lifecycle*).
- **Workflow states.** Development, implementation and handover are tracked as separate states;
  handover tends to trail the other two.
- **Utilization.** Few use cases record how often their output is opened. Where recorded, check
  for daily use and for "never used" (department notes *Operating model* and *Handover*).
- **Baseline and KPI are the missing element.** In every case group, the derivation row
  "Baseline and KPI" reads *Not recorded*: it "needs a measured baseline per plant (for
  example scrap, downtime or reporting hours) before and after". Most delivered cases carry no
  recorded saving (`Case Groups - Overview`, AI-grouped; re-count on the live note).
  **Acceptance is the cheapest moment to record the baseline**: add it to the protocol as an
  item for every use case.

## External definitions that stand behind C01 and C05 (verified in the knowledge base)

- ISO 22400-2:2014 defines KPIs for manufacturing operations management; the knowledge base verified
  these time elements from clause 5.1: planned run time per item is "the planned time for
  producing one quantity unit"; actual production time "includes only the value-adding
  functions"; actual unit delay time covers "malfunction-caused interruptions, minor
  stoppages, and other unplanned time intervals"; actual unit setup time is the time consumed
  for the preparation of an order at a work unit. The KPI formulas are **not** verified.
- A peer-reviewed bottling-plant case study reports that micro downtime (downtime under 15
  minutes) was a major part of inefficiency there. One plant, one industry; do not generalise
  to rubber, plastics, metal or assembly.

## Further items from the standardization knowledge base

The knowledge base's source note `_knowledge/90-Sources/org-analysis/usecase-standardization-knowledgebase`
gives each cluster a standard KPI set and a requirements checklist
compiled from public references (ISO 22400-2, VDI 3423, ISA-95, ISO 22005, TPS literature, with
Wikipedia as entry point). **Grade: compiled from published literature; the cluster
assignments date from an earlier classification run and differ from the cluster notes, and the
KPI definitions are not verified here.** Use it to extend the items above, not to override them.

| Cluster | Standard KPIs (knowledge base) | Extra checklist items that translate into acceptance items |
|---|---|---|
| C01 | Availability, performance, quality, OEE, TEEP | Run/stop states, actual against ideal cycle time and good/defective counts collected automatically or semi-automatically; micro-stop recording threshold (an industry convention is given in the note) agreed per line |
| C02 | Andon-pull rate, time to acknowledge, time to resolve, share of escalations closed with root cause, line-stop minutes from andon events | Wireless buttons favoured over pull cords; tiers L1 operator or team lead, L2 supervisor, L3 engineering or management, each with a time-boxed response; one common standard across plants |
| C03 | Cp, Cpk, out-of-control event rate, rule violations, scrap and rework rate, first-pass yield | Specification limits and statistically derived control limits defined before go-live; right chart type; root-cause tooling attached to out-of-control signals; do not apply SPC to an unstabilised process |
| C04 | Share of records captured digitally at source, entry time per record, entry error rate, time to availability downstream | Mandatory fields matched to what the downstream use case needs (define the consumer before the form); version-controlled master data behind the form; a path to automatic capture |
| C05 | MTBF, MTTR, unplanned downtime share, alert-to-acknowledgement time, share auto-classified | Standard plant-wide reason taxonomy, not free text; alerts routed to the right role; downtime written to a historian, not only displayed; distinguish "starved" and "blocked" from a machine fault |
| C06 | Unplanned downtime reduction, maintenance cost reduction, false-positive rate, lead time between prediction and failure, spare-parts inventory reduction | Results feed a maintenance management system so a condition becomes a work order; start with the highest-criticality assets; track false positives explicitly |
| C07 | Recipe-verification error rate, traceability query response time, share of production covered, time to root cause on a complaint | Recipes version-controlled and verified electronically against the job order before a machine starts; a unique scannable identifier per lot or unit; traceability queryable forward and backward; retention period and access model documented |
| C08 | kWh per unit, idle or standby share, energy cost per line or shift, avoided consumption | Meter at the level the action needs (line or cell, not building); baseline per shift or product before flagging anomalies; energy data on the same timeline as OEE and downtime |
| C09 | not given | Consumes data from the domain-owning capability rather than collecting again; audience and decision defined first; few reusable report templates |
| C10 | not given | A named human-gated decision point ("agents draft, humans decide"); start read-only or draft-only; explicit data-access grant from IT before a live system connection |

## Procedure

1. Pick the cluster from the use case record; if only "Other" fits, see the last rows.
2. Copy the acceptance items into section 2 of the protocol for the use case and add the
   baseline item.
3. Name the plant owner as witness and the real shift in which it will be used
   (`deploy-handover`).
4. Record pass or fail per item; a partial pass is not a pass.

⟨The standard KPI set and requirements checklist per cluster in the standardization knowledge
base. Who could supply it: its owner. When it is read, these items should be reconciled with it.⟩

## Sources

- Knowledge base `_knowledge/30-Nodes` cluster notes C01 to C12 (read 2026-11-05), including the verified
  reference entries R01, R13, R32 in C01.
- Department notes *Use case lifecycle*, *Handover*, *Operating model*, *Use case
  standardization* (`ops-knowledge-graph/_knowledge/10-Department`).
- Knowledge base `Case Groups` overview and group notes (derivation sheet rows).
