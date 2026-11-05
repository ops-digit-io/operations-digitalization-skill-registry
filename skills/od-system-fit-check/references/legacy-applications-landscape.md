---
type: Skill Reference
title: Legacy applications landscape
description: Aggregate view of the 268 recorded legacy applications - categories, functional mapping, criticality, network and support position - and how to use it in a fit check to spot the plant that already runs a parallel MES, SCADA or dashboard system.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Legacy applications landscape

A request that "quietly needs a system outside the lean footprint" is sometimes already
served, badly or locally, by a legacy application at that plant. The fit check should know
that before it recommends a redesign or an escalation: it changes the question from "can we
build this" to "what does the existing application do, who supports it, and what would retiring
it take".

**Record counts.** Source: the Legacy Application List as quoted in the vault's `Graph/Legacy
Applications` notes (268; `LegacyApplication-List` export of 2026-08-24), counted on
2026-11-05. The department describes the list as "what each one is, where it runs, which
function it serves, and what would have to happen to retire it" (*Legacy application
inventory*, `_knowledge/20-Done`). Many fields are sparsely filled; the counts below say how
many rows are blank.

## What the list holds

| Field | Filled on | Values (count) |
|---|--:|---|
| Application category | 253 | PLC programming / configuration 73; laboratory software 52; equipment configuration 33; camera system configuration 25; custom SCADA 15; printer 12; quality software 10; internal Mendix apps 9; custom MES 8; material flow / logistics 6; SCADA 6; custom dashboarding 2; energy monitoring 1; MES 1; blank 15 |
| Production criticality | 227 | critical 109; not applicable 61; moderate 34; minimal 23; blank 41 |
| Customer impact | 204 | critical 110; not applicable 56; moderate 26; minimal 12 |
| Network status | 205 | standalone 94; IT 65; OT/IT 25; OT 21; blank 63 |
| Cyber-security status | 197 | not started 172; not applicable (standalone) 15; approved 7; in progress 3; blank 71 |
| Support concept | 154 | internal support 86; external support contract 35; maintenance and run concept 33; blank 114 |
| Licence required | 267 | unknown 128; no licence required 67; local licence available 57; OESL licence required 15 |
| Supplier software status | 50 | in service 48; service stopped 2 |
| Scaling potential | 73 | yes 62; no 11 |
| Functional mapping (all rows) | 250 | PLC programming and configuration 124; quality laboratory data acquisition 41; MES 19 (+ mixed entries); quality data acquisition 15; logistics 13; MDA/PDA 5; traceability 4; environment, safety and health 4; recipe management 3; building management 2; energy monitoring 2; MIL 1 |
| Department mapping | 24 | quality digitalization 22; others 2 |

**Reading the fill rates.** Support concept is blank on 114 of 268 (43%), cyber-security status
on 71. A blank support concept is not "no support". It is not recorded. The headline cyber
number is the more solid one: of the 197 rows with a status, 172 say *not started*.

## Cross-readings (record counts)

- Of the **109 critical applications**, **70 have cyber-security status "not started"**, 41 are
  standalone, 47 are covered by internal support, and 37 have no support concept recorded.
- Network status by category: laboratory software is mostly networked (IT 23, OT/IT 15,
  OT 4, standalone 9); PLC programming software is mostly standalone (29) or blank (30);
  camera system configuration is mostly standalone (15).
- Licence by category: PLC programming software `unknown` 34, `local licence available` 30;
  laboratory software `unknown` 30, `local licence available` 14; quality software `OESL
  licence required` 4 of 10.

Where they sit: Hannover Stöcken 48, Subotica 45, Ponta Grossa 38, Monterrey 37,
Montemorelos 22, Caluire 16, Vac 15, Delicias 9; 10 applications are at more than one plant
and 2 are at none.

## Using it in the fit check

### Spot the parallel system

A need that sounds MES-, SCADA- or dashboard-shaped may already have a legacy home. 35
applications (38 plant links, because some sit at two plants) are in the classes custom SCADA (15), SCADA (6), custom MES (8), custom
dashboarding (2), MES (1) or mapped to the MES function:

| Where | Count | Reading |
|---|--:|---|
| Hannover Stöcken | 11 | The plant with by far the most legacy applications (48) and the most MES-class ones. Includes an application named ProView (also located at Hann. Münden) mapped to MES and recipe management |
| Ponta Grossa | 4 | |
| Waltershausen | 3 | one of them a custom MES |
| Karben, Jeonju, Vac | 2 each | Vac: a custom MES named Naturasoft |
| 14 further plants | 1 each | including Northeim ("TIG (MES)") and Montemorelos and Monterrey (one downtime-order application located at both) |

Procedure:

1. At the fit check's step 2 ("walk the tool boundaries"), if the need falls outside every
   lightweight tool, look the plant up here before concluding MES-shaped.
2. If a legacy application at the plant already covers the function, the verdict is "fits the
   lean footprint" (the application is the covering system) or "redesign onto a lighter tool"
   for the part it does not cover. Name the application. Replacing or changing it is a
   decision for the tool or system rollout row of `od-decision-routing`, not for this check.
3. Record the application's criticality, network status, support concept and cyber-security
   status in the check (they decide whether touching it is possible at all).

### Department direction (record)

Two sources state the department's direction on legacy applications; neither is a procedure:

- The OD initiative one-pager **"Cyber Security: Legacy Application As-Is-Analysis"** (slide
  index, 2025-05-08): perform an as-is analysis of legacy applications to identify risks,
  overlapping functionalities and mitigation plans or migration opportunities; develop a
  **bundled migration plan addressing the largest overlapping functionalities** and a
  one-pager on risks for high-impact applications. Lead, team and KPIs are in the slide; the
  body slides of the deck are empty templates.
- The ODEC slides of 2025-10-15, 2025-10-20 and 2025-11-19 (ODEC Facts staging, unverified):
  "Cyber Security: Legacy Application As-Is-Analysis. Legacy Applications and Bundled Migration
  Plan based on largest overlapping functionalities."
- The **ProView target architecture** (tool note `MES 1.0`, archive-based, AI-drafted): a
  December 2025 architecture review for one plant's mixing shop floor describes ProView as the
  current shop-floor application and a target of IIoT Edge Platform, Manufacturing Service
  Bus, a recipe management system and SAP DMC as MES, "Scope 2025" and not delivered.

**Rule (existing `non-bets.md`):** no standardized MES rollout across the estate in the short
or mid term. A plant-level MES-class legacy application is therefore not an invitation to
roll out a standard MES; it is a prompt to ask what the existing application is for.

## What is not in the records

⟨Retirement conditions per application. The department's description says the inventory records
"what would have to happen to retire it"; the fields read here (category, supplier, version,
status, interfaces, support, cyber security) do not include a retirement field. Who could
supply it: the owner of the Legacy Application List.⟩

⟨Cost of running or replacing any of the 268 applications.⟩

## Sources

- Vault `Graph/Legacy Applications` (268 notes), counted 2026-11-05.
- Department note *Legacy application inventory* (`_knowledge/20-Done`).
- Vault `Slide Index` (deck `OD Initiative - CS Legacy Application As_Is_Analysis`, slide 2).
- Vault `ODEC Facts - Department KPIs and Roadmap Status` (staging, unverified).
- Vault `Graph/Tools/MES 1.0` archive-evidence block (AI-drafted from archive slides).
- Registry reference [`non-bets.md`](non-bets.md).
