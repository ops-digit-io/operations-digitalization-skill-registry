---
type: Skill Reference
title: Legacy application landscape
description: Guidance, no figures. How to read the recorded plant-local applications (categories, functional mapping, support, licences, network placement) and use it when the question is replace, integrate or keep.
resource: ../procedure.md
status: draft
tags: [project-support-consultancy, practice, aggregate]
---
# Legacy application landscape

The `LegacyApplication` records (bundle file `kg_nodes.csv`; the department knowledge base keeps one note per
application) are read here as a pattern, not one by one. Many fields are blank; blanks are shown as
blanks, never guessed. Plant and region may be missing on many records. Re-count on the live list and
quote the export date when a figure is needed; none is kept here.

## What the fields hold

| Field | Typical values | How to read it |
|---|---|---|
| Category (as recorded) | PLC programming / configuration, laboratory software, equipment configuration, camera system configuration, custom SCADA, printer, quality software, internal Mendix apps, custom MES, SCADA, material flow / logistics, custom dashboarding, MES, energy monitoring | Most are tools for a machine, not business applications |
| Functional mapping (a record can have several) | PLC programming and configuration, quality laboratory data acquisition, MES, quality data acquisition, logistics, MDA/PDA, traceability, environmental safety and health, recipe management, image library, building management, energy monitoring | The vocabulary matches the OD tools, which makes it the first search field |
| Support concept | Internal support, external support contract, maintenance and run concept | **Often blank. Blank is not "no support"** |
| Support concept availability | possible, yes, not available | Mostly blank |
| Supplier software status | in service, service stopped | Mostly blank |
| Licence required | unknown, no licence required, local licence available, OESL licence required | "Unknown" is common |
| Network status | standalone, IT, OT/IT, OT | Decides the Cyber Security question |
| Cyber security status | not started, NA - standalone, approved, in progress | "Not started" is the common value |
| Customer impact | critical, moderate, minimal, NA | Often critical, which raises the risk of "replace" |
| Supplier | Keyence, Siemens, internal, ContiTech, Mitsubishi, Hexagon, Rockwell / Allen Bradley (two spellings), and others | Spelling variants must be merged before counting |
| Status | in use (spelling variants), not started | Many blanks |

## Reading it for an application question

- **Most are tools for a machine, not business applications.** PLC and equipment configuration
  software and camera configuration software dominate: an "app design question" about one of them is
  usually an integration question for the machine, so it belongs with `od-equipment-integration` and
  `od-equipment-integration`, not with a build path.
- **The MES-shaped ones are a system-fit matter.** Applications mapped to MES, custom MES and custom
  SCADA are plant-built systems doing what the lean footprint declines to roll out as a standard. A
  request to extend or replace one is a footprint check before it is a design (`od-system-fit-check`;
  strategy non-bet on MES). Do not recommend replacing one with a central MES.
- **Licence is often unknown.** A recommendation that keeps or integrates an application must say
  `⟨licence status unknown⟩` rather than assume; licensing commitments are not the consultant's
  (`it-demand-package`, "may not").
- **Support is the usual gap.** A large share of records have no support concept. An integrate-or-keep
  recommendation names who supports the interface (see the support tiers in `footprint-and-data-path`).
- **Placement matters for Cyber Security.** OT/IT and OT applications: an interface to these is an
  external-connection question for `od-cybersec-gate`. Standalone applications: integrating them first
  needs a network decision.
- **Criticality is skewed.** Many are recorded as having critical customer impact, which makes "replace"
  a high-risk option; the record does not say why each is critical.

## How to measure live

Filter the list by category, functional mapping, network status, cyber security status, support concept
and customer impact; count filled versus blank per field and say how many rows are blank. Compare
the order of magnitude with the AI-at-operations business case before quoting either.

## Business-case context (proposals, not decisions)

The AI-at-operations business case list carries cases about this stock (department knowledge base, Graph/Business
Cases): one on assimilating plant-local apps (such as Mendix apps and spreadsheet macro chains) into a
containerised app catalogue, and one on closing the cyber-security backlog by running catalogued apps
through a conformance gate, tied to a regulatory deadline. Cost, value and confidence ranges are in the
cases themselves (look up: Graph/Business Cases); do not copy them here or quote them as approved.
Quote the business cases only as proposals with their confidence notes.

An application whose cyber security status is "Not started" is a Cyber Security question before it is a
design question: put it in the gate table of the recommendation (`od-cybersec-gate`).
