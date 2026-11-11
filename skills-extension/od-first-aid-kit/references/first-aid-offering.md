---
type: Skill Reference
title: First aid offering
description: Guidance on the Process First-Aid Kit - purpose, the two data scenarios, how to handle the cost question, and the shape of typical ad-hoc analyses that show how a plant issue becomes an analytical question. Guidance only, no company figures.
resource: ../SKILL.md
status: draft
tags: [use-case-support-service, practice]
---
# First aid offering

Guidance only. Derived from the IIoT Edge Computing Platform "First AID Kit" slides
in the Data Science Factory tool deck, the Slide Index for the ad-hoc analysis decks, and the lane
documents named in `SKILL.md` (see `derived_from`). The decks are presentations. Nothing here has
been confirmed by a human at OD. Prices, counts and dates from the decks are deliberately not
repeated; look them up at the source when needed.

## 1 · Purpose and activities

| Item | Content |
|---|---|
| Purpose | Process or product ramp-up support; process or product trouble shooting |
| What we do | Prepare process data acquisition fulfilling the analytics requirements; make problems S.M.A.R.T.; generate insights |
| Pricing | Depends on preconditions (what already exists at the plant). The tool deck carries an indication; it is not a quote. Look up: OD lead |
| Typical example | Performance analysis of an assembly line (balancing) at a line that had been separated from the network |

Cost components of a first-aid case, as a structure: an edge device installed; the device
reconfigured to run stand-alone data acquisition; an analytical template developed for the machine.
Which of these apply depends on the scenario below. Do not quote amounts; the sources do not say
who pays, and prices change.

## 2 · The two scenarios

| | A: edge platform and network available | B: edge platform and network not available |
|---|---|---|
| Condition | Plant has basic capabilities and an installed edge platform, including a cyber security conform network installation | No possibility to connect the machine to an available edge installation |
| What is needed | The edge device satisfies the technical requirements for first aid. Marked "preferred variant" | An edge device installed at the machine; an additional service for short-term data aggregation on the device itself |
| How the analysis runs | On data from the platform | By transferring the data from the device manually |
| Later | | Integration of the device into a later installed edge platform is described as possible and straightforward |
| Open effort | | Additional effort might need to be determined by PLC type; a concept exists for one PLC family |

Reading for a key user: scenario A is a data-availability question (is the signal on the platform);
scenario B is an installation question, and the installation is a connection to a machine, which
needs the Cyber Security sign-off before go-live (`od-cybersec-gate`, in parallel) and the Information Integration lane
(`od-equipment-integration`). The first-aid request only records which scenario applies.

## 3 · Two typical ad-hoc analyses (patterns, not data)

Two past ad-hoc analyses show the shape of the work. They are described by the pattern they teach,
not by their data.

| Pattern | Starting problem | What the analysis did | What it teaches the form |
|---|---|---|---|
| Statistical analysis of test results against a global reference | A local dataset from one plant is compared with a larger global dataset of the same lab test | Descriptive statistics, distribution detection on the global set, comparison local versus global per class | The local dataset lacked some classes: a **data gap discovered during analysis**. The form asks about data coverage first |
| Unstable control loop on a production line | A measured product dimension oscillates; the operator tunes dead band, set value increment and interval; the process stays unstable | A dashboard to deep-dive PLC inputs and outputs ("problem transparency"); open questions about how the control loop is implemented; next steps (information on the control cycle, tests during ramp-up of a second line, other influencers) | The restated question moved from "the dimension oscillates" to "how is the control loop implemented and what else influences the dimension". The form's S.M.A.R.T. step asks for exactly this move |

## 4 · Where it sits in the lanes

| Document | Statement |
|---|---|
| `04-service-catalog.md` | Use Case Support Service includes the Process First-Aid Kit; Analytical Support Service includes Ad-Hoc Analytics |
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
- How many first-aid cases have run and what they led to. Measure it from the intake log, not from
  this skill.
- Whether first aid is subject to the intake refusal rule.
Supplier of all four: the DBVE or the OD lead.
