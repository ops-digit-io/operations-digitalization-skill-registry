---
type: Skill Reference
title: First aid offering
description: What OD's documents say about the Process First-Aid Kit - purpose, the two data scenarios, the priced example, and two ad-hoc analyses that show how a plant issue becomes an analytical question - with what the sources do not say.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# First aid offering

Sources, all read 2026-11-05: the IIoT Edge Computing Platform "First AID Kit" slides 11 and 12 in
the Data Science Factory tool deck of the Standard Agenda folder (deck date 2024-07-14; the same
two slides recur in a deck of 2025-01-17 and a deck of 2025-05-07); the Slide Index note for
`25-Adhoc_Analysis` (two decks of 2024); the lane documents named in `SKILL.md`. The decks are
presentations. Nothing here has been confirmed by a human at OD.

## 1 · Purpose and activities (slide 11)

| Item | Text of the slide, condensed |
|---|---|
| Purpose | Process or product ramp-up support; process or product trouble shooting |
| What we do | Prepare process data acquisition fulfilling the analytics requirements; make problems S.M.A.R.T.; generate insights |
| Pricing indication | "Depending on preconditions between 3k EUR additional invest up to 20k EUR" |
| Example named on the slide | Performance analysis of an assembly line (balancing); a coolant jacket line at one plant had been separated from the network |

The example's cost build-up as the slide states it: an edge device installed (2.8k EUR); the device
reconfigured to run stand-alone data acquisition (5k EUR); an analytical template developed for the
machine (5k EUR). The sum is the slide's example, not a standard price list; the sources do not say
who paid, nor the period. Treat it as an order of magnitude and quote it with its date and scope.

## 2 · The two scenarios (slide 12)

| | A: edge platform and network available | B: edge platform and network not available |
|---|---|---|
| Condition | Plant has basic capabilities and an installed edge platform, including a cyber security conform network installation | No possibility to connect the machine to an available edge installation |
| What is needed | The edge device satisfies the technical requirements for first aid. Marked "preferred variant" | An edge device installed at the machine; an additional service for short-term data aggregation on the device itself |
| How the analysis runs | On data from the platform | By transferring the data from the device manually |
| Later | | Integration of the device into a later installed edge platform is "possible and straightforward" |
| Open effort | | Additional effort "might need to be determined by PLC type"; a concept is available for one PLC family (the slide names Siemens S7-1500) |

Reading for a key user: scenario A is a data-availability question (is the signal on the platform);
scenario B is an installation question, and the installation is a connection to a machine, which
needs the Cyber Security gate (`od-cybersec-gate`) and the Information Integration lane
(`od-equipment-integration`). The first-aid request only records which scenario applies.

## 3 · Two ad-hoc analyses that show the shape of the work (`25-Adhoc_Analysis`, 2024)

These are the only worked traces of ad-hoc analysis in the vault index; they are described by their
slide titles and text snippets, not by their data.

| Case | Starting problem (slide text) | What the analysis did | What it teaches the form |
|---|---|---|---|
| Cleanliness statistical analysis at a plant, January 2024 | A statistical analysis of particle test results; baseline: a global dataset of about 14,000 test results and a local dataset of 91 results from one plant, from several lab locations | Descriptive statistics, distribution detection on the global set, comparison of the local with the global dataset by particle class | The local dataset lacked four small particle classes ("data not available for those classes"): a **data gap discovered during analysis**. The form asks about data coverage first |
| Extrusion line vacuum and diameter, March 2024 | Product diameter measurement oscillates; the operator sets dead band, vacuum set value increment and interval; the process is unstable; question: how can the control loop in the PLC be improved | A dashboard was built to deep-dive PLC inputs and outputs ("problem transparency"); open questions were listed about how the control loop is implemented; next steps were set (information on the control cycle, tests during ramp-up of a second line, other influencers on the diameter) | The restated question moved from "diameter oscillates" to "how is the control loop implemented and what else influences the diameter". The form's S.M.A.R.T. step asks for exactly this move |

## 4 · Where it sits in the lanes

| Document | Statement |
|---|---|
| `04-service-catalog.md` | Use Case Support Service "(incl. Process First-Aid Kit)"; Analytical Support Service "(incl. Ad-Hoc Analytics)" |
| `14-glossary.md` | Process First-Aid Kit: rapid diagnostic offering within Use Case Support Service; related term Ad-Hoc Analytics |
| `05-intake.md` | "Ad-hoc analytics / Process First-Aid Kit requests" is one of the intake channels |
| `08-decision-rights.md` | Ad-hoc analytics delivery: DBVE alone, no approval, reversible, read-only on source systems, authority `execute-autonomously` |
| Analytical Support playbook | Step 1 request received (Process First-Aid Kit); error paths: data not available means a data gap routed to Information Integration; a one-off insight is closed as ad-hoc, not industrialized |
| Analytical Support tasks | Ad-hoc analytics / Process First-Aid: template "to confirm" |

Note the difference in authority: this skill is **draft** (it prepares a request and a route);
delivering the analytics itself is the Analytical Support Service's autonomy and is read-only on
source systems.

## 5 · Not in the sources

- A first-aid request form, turnaround, who may request, a limit on requests per plant.
- Who pays for devices and templates, and from which budget.
- How many first-aid cases have run and what they led to (the vault index shows two ad-hoc analyses
  and one priced example; nothing counts the rest).
- Whether first aid is subject to the intake refusal rule.
Supplier of all four: the DBVE or the OD lead.
