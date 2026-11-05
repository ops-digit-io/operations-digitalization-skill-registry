---
type: Skill Reference
title: Legacy application landscape
description: What the 268 recorded plant-local applications show - categories, functional mapping, support, licences, network placement - and how to use it when the question is replace, integrate or keep.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [project-support-consultancy, practice, aggregate]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Legacy application landscape

Aggregate of the 268 `LegacyApplication` records in the bundle file `kg_nodes.csv`, read 2026-11-05 (the
work vault keeps one note per application; they are read as a pattern here, not one by one). Counts
describe what was recorded. Many fields are blank; blanks are shown, not guessed. Plant and region are not
recorded on any of the 268.

## What they are

| Category (as recorded) | Apps |
|---|--:|
| PLC programming / configuration | 73 |
| Laboratory software | 52 |
| Equipment configuration | 33 |
| Camera system configuration | 25 |
| Custom SCADA | 15 |
| Printer | 12 |
| Quality software | 10 |
| Internal Mendix apps | 9 |
| Custom MES | 8 |
| SCADA | 6 |
| Material flow / logistics | 6 |
| Custom dashboarding, MES, energy monitoring | 2, 1, 1 |
| Category blank | 15 |

Functional mapping to the OD tool vocabulary (a record can have several): PLC programming and
configuration 124; quality laboratory data acquisition 41; MES 19 (plus 2 with MDA/PDA); quality data
acquisition 15; logistics 13; MDA/PDA 5; traceability 4; environmental safety and health 4; recipe
management 3; image library 1; building management 2; energy monitoring 2; blank 18.

## Support, licences, placement

| Field | Values |
|---|---|
| Support concept | Internal support 86; external support contract 35; maintenance and run concept 33; blank 114 |
| Support concept availability | Possible 44; yes 40; not available 7; blank 177 |
| Supplier software status | In service 48; service stopped 2; blank 218 |
| Licence required | Unknown 128; no licence required 67; local licence available 57; OESL licence required 15 |
| Network status | Standalone 94; IT 65; OT/IT 25; OT 21; blank 63 |
| Cyber security status | Not started 172; NA - standalone 15; approved 7; in progress 3; blank 71 |
| Customer impact | Critical 110; NA 56; moderate 26; minimal 12; blank 64 |
| Most frequent suppliers | Keyence 31; Siemens 18; internal 13; ContiTech 12; Mitsubishi 11; Hexagon 8; Rockwell / Allen Bradley 13 (two spellings); blank 67 |
| Status | In use about 140 (spelling variants); not started 1; blank 114 |

## Reading it for an application question

- **Most are tools for a machine, not business applications.** Nearly half are PLC and equipment
  configuration or camera configuration software: an "app design question" about one of them is usually an
  integration question for the machine, so it belongs with `od-equipment-integration` and
  `od-barrier-triage`, not with a build path.
- **The MES-shaped ones are a system-fit matter.** The 19 mapped to MES and the 8 custom MES plus 15 custom
  SCADA are plant-built systems doing what the lean footprint declines to roll out as a standard. A request
  to extend or replace one is a footprint check before it is a design (`od-system-fit-check`; strategy
  non-bet on MES). Do not recommend replacing one with a central MES.
- **Licence is unknown for 128 of 268.** A recommendation that keeps or integrates an application must say
  `⟨licence status unknown⟩` rather than assume; licensing commitments are not the consultant's
  (`od-project-support-consultancy`, "may not").
- **Support is the usual gap.** 114 of 268 record no support concept. An integrate-or-keep recommendation
  names who supports the interface (see the support tiers in `footprint-and-data-path`).
- **Placement matters for Cyber Security.** 25 are OT/IT and 21 OT: an interface to these is an
  external-connection question for `od-cybersec-gate`. 94 are standalone: integrating them first needs a
  network decision.
- **Criticality is skewed.** 110 are recorded as having critical customer impact, which makes "replace"
  a high-risk option; the record does not say why each is critical.

## Business-case context (proposals, not decisions)

The AI-at-operations business case list carries two cases about this stock (work vault, Graph/Business Cases,
list items created 2026-05-13, export 2026-08-24): *Legacy App Assimilation* (assimilate plant-local apps
such as Mendix apps and spreadsheet macro chains into a containerised app catalogue; cost range EUR 0.3M to
0.6M, value range EUR 0.5M to 2M per year, confidence "Med", a 3-year horizon) and *Cybersec Backlog
Closure* (run catalogued apps through a conformance gate; stated as mandatory spend, tied to a 2027 EU
regulation deadline). The same case says about 65 percent of the shop-floor apps are "Not Started" on
cybersecurity status; the application records agree in order of magnitude: cyber security status "Not
started" 172, "NA - standalone" 15, "Approved" 7, "In progress" 3, blank 71 (of 268). Only 7 are recorded
as approved. Quote the business cases only as proposals with their confidence notes.

An application whose cyber security status is "Not started" is a Cyber Security question before it is a
design question: put it in the gate table of the recommendation (`od-cybersec-gate`).
