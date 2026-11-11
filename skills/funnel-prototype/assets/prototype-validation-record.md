---
type: Skill Asset
title: Prototype validation record
description: The output of funnel-prototype - the open question, the pass criterion written first, the result, the status label and the open items, in a form the business case and capital request can read.
resource: ../SKILL.md
status: draft
tags: [use-case-support-service, template, protocol]
---
# Prototype validation record - ⟨use case name⟩

Copy once per prototype or PoC. Fill sections 1 and 2 **before** building, sections 3 to 5 after.

| | |
|---|---|
| **Use case** | ⟨name, plant, line⟩ |
| **From** | ⟨`funnel-use-case` / `funnel-requirements` / `mi-data-availability` records⟩ |
| **Drafted by / date** | ⟨role⟩ · ⟨date⟩ |
| **Plant validator** | ⟨role at the plant, not the builder⟩ |

## 1 · Question and type

| | |
|---|---|
| **Open question** | ⟨one sentence⟩ |
| **Question class** | ⟨usability · scope · data · model⟩ |
| **Type** | ⟨click-dummy · PoC · pilot · none, with the reason⟩ |
| **Library check** | ⟨proven reference solution exists: yes (adopt, stop) / no⟩ |

## 2 · Pass criterion (written before the build)

| | |
|---|---|
| **Scope and time box** | ⟨one plant, line or machine family; weeks⟩ |
| **Measure and threshold** | ⟨number, unit⟩ |
| **Baseline compared with** | ⟨current method, or "none - say why"⟩ |
| **False-positive / rework limit** | ⟨if a detector or generator⟩ |
| **On pass / on fail / on inconclusive** | ⟨next step for each⟩ |
| **Criterion agreed with the validator on** | ⟨date⟩ |

## 3 · What was built

⟨Artifact or link, the tool used, what is real (data, signals) and what is invented. Mock-ups: state that the
values are example data.⟩

## 4 · Result

| | |
|---|---|
| **Run period / users involved** | ⟨dates; roles and count⟩ |
| **Measured result** | ⟨value against the threshold⟩ |
| **What users said and did** | ⟨observed behaviour first, opinions second⟩ |
| **Status** | ⟨passed · failed · inconclusive⟩ |
| **Label to use outward** | ⟨mock-up · PoC · pilot - never "proven"⟩ |
| **Plant confirmation** | ⟨the validator confirms or declines the value, in writing; date⟩ |

## 5 · Hand-on

| To | What it takes from this record |
|---|---|
| `bc-build` | The result as evidence for a saving row; the methodology field is still written there. Value is ⟨to be collected⟩ here |
| `bc-capital-request` | Passed, and money is needed: this record goes in the package |
| `funnel-use-case` | Failed or inconclusive: what to re-scope |
| `deploy-acceptance` | Nothing yet; acceptance applies to the later build |

## 6 · Open items

⟨Anything the sources or the test did not answer, and who can answer it.⟩
