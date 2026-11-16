---
type: Skill Asset
title: Process derivation package
description: The output of process-derivation - the gate record, the change and redesign evidence, the to-be model, the standard work, the adoption and change-control plan, the landscape entry and the monitoring design, in a form the process owner can accept or send back.
resource: ../SKILL.md
status: draft
tags: [use-case-support-service, template, protocol]
---
# Process derivation package - ⟨process name: verb and object⟩

Copy once per process. Fill section 0 first: if any gate item is empty or the prototype result is not "passed", write the refusal note at the end of section 0 and stop. Source keys [PDn] are in `references/public-methods.md`. Mark your own reasoning **Inference**. Never write "proven", and never write a figure that no record gives.

| | |
|---|---|
| **Use case** | ⟨name, plant, line⟩ |
| **Drafted by / date** | ⟨role⟩ · ⟨date⟩ |
| **Process owner (a role)** | ⟨role, never a person⟩ |

## 0 · Gate record

| | |
|---|---|
| **Use-case request** | ⟨record of `funnel-use-case`: reference, requester role, plant⟩ |
| **Use-case demand** | ⟨record of `funnel-requirements`: reference, requirement, acceptance criteria⟩ |
| **Validated prototype** | ⟨record of `funnel-prototype`: reference, status label (click-dummy, PoC or pilot), plant validator role⟩ |
| **Prototype result** | ⟨passed / failed / inconclusive, as the record says⟩ |

**Refusal note** (only if the gate is not met): ⟨which item is missing, who owns it, what would fill it⟩

## 1 · Process identity

| | |
|---|---|
| **Name** | ⟨verb and object⟩ |
| **Scope** | ⟨plants or lines in scope; what is out of scope⟩ |
| **Process landscape that applies** | ⟨the organisation's landscape, or "none: proposal only"⟩ |

## 2 · As-is evidence from the prototype

| Read from the validation record | Content |
|---|---|
| What the users did, step by step | ⟨the as-is sequence the use case replaces or extends⟩ |
| Roles that took part | ⟨roles⟩ |
| Pass criterion and result | ⟨the criterion, the result, why the change is worth making⟩ |
| What was not tested | ⟨mock data, no integration, one shift ...⟩ |

## 3 · The change and the redesign

**The change in one sentence:** Today ⟨role⟩ does ⟨work⟩ with ⟨system or paper⟩; after the change ⟨role⟩ does ⟨work⟩ with ⟨use case output⟩.

| Redesign heuristic (by its name in [PD2]) | Change | Effect on cost / flexibility / time / quality | Evidence (record or plant source, with place) |
|---|---|---|---|
| ⟨name⟩ | ⟨what changes⟩ | ⟨qualitative effect per dimension⟩ | ⟨evidence or `⟨not evidenced⟩`: then it is an open item⟩ |

**Trade-off the owner decides** (**Inference**): ⟨one line⟩

## 4 · To-be model

| | |
|---|---|
| **BPMN file** | ⟨path, version⟩ |
| **Check** | ⟨`python scripts/check_derivation.py package.md process.bpmn` -> READY, date⟩ |
| **Lanes (roles)** | ⟨roles⟩ |
| **Exception paths shown** | ⟨which⟩ |
| **Decision table (DMN) or case model (CMMN)** | ⟨file and reason, or "not needed"⟩ |

## 5 · Standard work (repetitive operator tasks only)

| Task | Role | Trigger | Sequence | What the use case shows | Who may change it, review interval |
|---|---|---|---|---|---|
| ⟨task⟩ | ⟨role⟩ | ⟨trigger⟩ | ⟨steps⟩ | ⟨output at that moment⟩ | ⟨role, interval⟩ |

If not used: ⟨reason⟩. Takt time: ⟨value from a record, or `⟨not recorded⟩`⟩.

## 6 · Adoption and change control

| Role group | Earliest unmet ADKAR element [PD10] | Evidence | Action and owner (a role) |
|---|---|---|---|
| ⟨role group⟩ | ⟨Awareness / Desire / Knowledge / Ability / Reinforcement⟩ | ⟨statement, observation or prototype session⟩ | ⟨action, role⟩ |

**Programme-level check [PD11], if the change spans more than one team:** ⟨which of the eight steps are used and why⟩

**Change control, if the process alters how a line or machine is operated [PD12 pattern; the plant's safety role names any legal requirement]:**

| Point | Answer |
|---|---|
| Technical basis for the change | ⟨⟩ |
| Impact on safety and health | ⟨⟩ |
| Modifications to operating procedures | ⟨⟩ |
| Necessary time period for the change | ⟨⟩ |
| Authorization required | ⟨role⟩ |
| People informed and trained before start-up | ⟨who, when⟩ |

If the process only moves information: ⟨one line saying why this is not needed⟩.

**Embedded when** (all must be true): owner role named · standard posted where used, with a role who can change it · training done for the role groups with Knowledge or Ability barriers · monitoring running with a first review date · the old way switched off or written down as a fallback.

## 7 · Landscape entry

| Field | Content |
|---|---|
| Process id | ⟨stable id or proposed⟩ |
| Name | ⟨⟩ |
| Level and parent [PD7] | ⟨level, parent process group⟩ |
| Owner role | ⟨⟩ |
| Model | ⟨path, version, date⟩ |
| Interfaces | ⟨upstream process and the object it hands over; downstream process and the object it receives⟩ |
| Use case | ⟨id in `catalog-usecase`, skill chain⟩ |
| Standard work | ⟨path or none with reason⟩ |
| Review | ⟨next review date, reviewing role⟩ |

**Accepted by a human owner:** ⟨yes, role, date / not yet: this is a proposal⟩

## 8 · Monitoring [PD13]

| | |
|---|---|
| **Events the use case system records** (timestamp, case id) | ⟨events, or "none: open item"⟩ |
| **Three questions the owner will ask** | ⟨1 · 2 · 3⟩ |
| **Event-to-model mapping** | ⟨event -> task or event of the BPMN model⟩ |
| **Who looks, how often** | ⟨role, interval⟩ |
| **Trigger for a new model version** | ⟨new machine, new role, repeated exceptions ...⟩ |
| **Indicators for the scorecard** | ⟨indicator, source, date, or `⟨to collect⟩`⟩ |

## 9 · Open items and human decisions

| Item | Owner (a role) | Needed by |
|---|---|---|
| ⟨open item or decision⟩ | ⟨role⟩ | ⟨date or step⟩ |

Decisions that stay with humans: ⟨accept the process and the landscape entry · confirm the as-is and the standard · scope and priority · investment · local legal change-control requirement · publish to the landscape · go-live⟩

## 10 · Sources

Public methods used: ⟨keys from `references/public-methods.md`⟩. Internal records: ⟨paths and ids⟩. Anything not backed by a record or a source above is **Inference**.

**Maturity verdict (recommendation only):** ⟨Ready for the owner to accept / Accept the model only (adoption not yet planned) / Not ready⟩
