---
type: Skill Reference
title: Legacy applications landscape
description: Guidance, no figures. How to read the Legacy Application List (fields, blank-cell traps, cross-readings) and use it in a fit check to spot the plant that already runs a parallel MES, SCADA or dashboard system.
resource: ../SKILL.md
status: draft
tags: [all, practice]
---

# Legacy applications landscape

A request that "quietly needs a system outside the lean footprint" is sometimes already
served, badly or locally, by a legacy application at that plant. The fit check should know
that before it recommends a redesign or an escalation: it changes the question from "can we
build this" to "what does the existing application do, who supports it, and what would retiring
it take".

**Where it lives.** The Legacy Application List, as quoted in the knowledge base's `Graph/Legacy
Applications` notes (one note per application; `LegacyApplication-List` export). The department
describes it as "what each one is, where it runs, which function it serves, and what would have
to happen to retire it" (*Legacy application inventory*, `_knowledge/20-Done`). Re-count on
the live list and quote the export date; no figures are kept here.

## What the list holds

| Field | Values | How to read it |
|---|---|---|
| Application category | e.g. PLC programming / configuration, laboratory software, equipment configuration, camera system configuration, custom SCADA, SCADA, custom MES, MES, custom dashboarding, quality software, internal Mendix apps, printer, material flow / logistics, energy monitoring | The MES-, SCADA- and dashboard-class categories matter for a fit check. Most of the list is engineering and laboratory tooling, not parallel MES |
| Production criticality / customer impact | critical, moderate, minimal, not applicable | Decides whether touching the application is possible at all |
| Network status | standalone, IT, OT/IT, OT | A standalone application cannot be reached by a data pipeline without a network decision |
| Cyber-security status | not started, in progress, approved, not applicable (standalone) | "Not started" is the common value; it triggers the Cyber Security / OT gate |
| Support concept | internal support, external support contract, maintenance and run concept | **Blank is not "no support"**; it is not recorded |
| Licence required | unknown, none, local, OESL | "Unknown" is common; it blocks any reuse conversation |
| Supplier software status | in service, service stopped | |
| Scaling potential | yes / no | Sparsely filled |
| Functional mapping | e.g. PLC programming, quality laboratory data acquisition, MES, logistics, MDA/PDA, traceability, recipe management, energy monitoring, MIL | May hold mixed entries |
| Department mapping | e.g. quality digitalization | Sparsely filled |

**Reading the fill rates.** Many fields are sparsely filled. Before quoting any share, count
filled versus blank on the live list and say how many rows are blank. A blank is a data-quality
gap, not a negative finding.

## Cross-readings worth running live

- Critical applications by cyber-security status, network status and support concept: the
  critical, unsecured, unsupported combination is the risk list.
- Network status by category: laboratory software tends to be networked, PLC programming
  software and camera system configuration tend to be standalone.
- Licence by category: "unknown" is common for PLC and laboratory software.
- Applications by plant: a ranking by plant says where the inventory work was done as much as
  where applications exist; some applications sit at more than one plant and some at none.

## Using it in the fit check

### Spot the parallel system

A need that sounds MES-, SCADA- or dashboard-shaped may already have a legacy home. Filter by
the classes custom SCADA, SCADA, custom MES, MES, custom dashboarding, or functional mapping MES,
for the plant in question (an application at two plants counts once per plant link). Plants with
a large inventory typically carry the most MES-class applications. Watch applications mapped to
both MES and recipe management (for example ProView, which has a documented target architecture
on IIoT Edge Platform, Manufacturing Service Bus, a recipe management system and SAP DMC; see the
tool note `MES 1.0`, archive-based, AI-drafted).

Procedure:

1. At the fit check's step 2 ("walk the tool boundaries"), if the need falls outside every
   lightweight tool, look the plant up in the list before concluding MES-shaped.
2. If a legacy application at the plant already covers the function, the verdict is "fits the
   lean footprint" (the application is the covering system) or "redesign onto a lighter tool"
   for the part it does not cover. Name the application. Replacing or changing it is a
   decision for the tool or system rollout row of `od-decision-routing`, not for this check.
3. Record the application's criticality, network status, support concept and cyber-security
   status in the check (they decide whether touching it is possible at all).

### Department direction (record)

Two sources state the department's direction on legacy applications; neither is a procedure:

- The OD initiative one-pager **"Cyber Security: Legacy Application As-Is-Analysis"** (slide
  index): perform an as-is analysis of legacy applications to identify risks, overlapping
  functionalities and mitigation plans or migration opportunities; develop a **bundled
  migration plan addressing the largest overlapping functionalities** and a one-pager on risks
  for high-impact applications. Lead, team and KPIs are in the slide; the body slides of the
  deck are empty templates.
- ODEC slides (ODEC Facts staging, unverified) repeat the same direction.

**Rule (existing `non-bets.md`):** no standardized MES rollout across the estate in the short
or mid term. A plant-level MES-class legacy application is therefore not an invitation to
roll out a standard MES; it is a prompt to ask what the existing application is for.

## What is not in the records

⟨Retirement conditions per application. The department's description says the inventory records
"what would have to happen to retire it"; the fields read here (category, supplier, version,
status, interfaces, support, cyber security) do not include a retirement field. Who could
supply it: the owner of the Legacy Application List.⟩

⟨Cost of running or replacing any application.⟩

## Sources

- Knowledge base `Graph/Legacy Applications`.
- Department note *Legacy application inventory* (`_knowledge/20-Done`).
- Knowledge base `Slide Index` (deck `OD Initiative - CS Legacy Application As_Is_Analysis`).
- Knowledge base `ODEC Facts - Department KPIs and Roadmap Status` (staging, unverified).
- Knowledge base `Graph/Tools/MES 1.0` archive-evidence block (AI-drafted from archive slides).
- Registry reference `non-bets.md`.
