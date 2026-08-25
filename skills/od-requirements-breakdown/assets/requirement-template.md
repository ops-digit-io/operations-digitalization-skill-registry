---
type: Skill Asset
title: Requirement template
description: The blank requirement to copy, carrying the ten core sections and all four lane variants.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [requirements, template, blank]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Requirement: ⟨asset⟩ - ⟨artefact⟩

## §1 Identity

| | |
|---|---|
| Plant | ⟨plant⟩ |
| Machine(s) | ⟨name⟩ ⟨(EQ id)⟩ |
| Capability | ⟨one of the 11 templates⟩ |
| Process group | ⟨one of the 29⟩ |
| Lane | ⟨use-case / integration / project / analytical⟩ |
| Author / date | ⟨name⟩ · ⟨date⟩ |

## §2 Key Problem / Major Issue

⟨One paragraph, present tense, operational. If it names a technology, rewrite it.⟩

## §3 Use Case Target Overview

⟨What will be true when delivered — and who acts on it, at which moment in the day.⟩

## §4 Standard baseline

| | |
|---|---|
| Cluster | ⟨C01…C12⟩ |
| Standard KPIs | ⟨from the cluster KPI set⟩ |
| Requirements checklist | ⟨adopted / adopted with deltas / not applicable⟩ |
| Public data model | ⟨EUROMAP 77/83/84 · OPC UA for Machinery · PackML · none⟩ |
| Deltas from standard | ⟨only what this plant does differently⟩ |

## §5 Tags of Interest

| Signal | Direction | Source | Exists? | Unit | Collection |
|---|---|---|---|---|---|
| ⟨CanonicalName⟩ | in | ⟨PLC / edge / manual⟩ | ⟨yes ⟨uuid⟩ / no⟩ | ⟨unit⟩ | ⟨transition / sample @ interval⟩ |
| ⟨CanonicalName⟩ | out | derived | no — to register | ⟨unit⟩ | ⟨per cycle / per period⟩ |

## §6 Acceptance criteria

- **AC-1** Given ⟨state⟩, when ⟨trigger⟩, then ⟨observable result⟩.
- **AC-2** The value matches ⟨reference⟩ within ⟨tolerance⟩ over ⟨period⟩.
- **AC-3** ⟨named plant role⟩ has used it in a real shift, not a demonstration.

## §7 Blocking points

**Major blocking points**
- ⟨what stops delivery⟩ — owner ⟨name⟩ · class ⟨connectivity / hardware / external access / method undefined / parameter selection / software⟩ · expected ⟨date⟩

**Minor blocking points**
- ⟨what slows delivery⟩ — owner ⟨name⟩

## §8 System fit

| | |
|---|---|
| Systems required | ⟨list⟩ |
| Footprint verdict | ⟨inside / outside → refuse & route / substitute ⟨name⟩⟩ |
| Legacy applications touched | ⟨app⟩ · support ⟨concept⟩ · supplier ⟨status⟩ · licence ⟨status⟩ |
| Relationship | ⟨integrate with / replace / unaffected⟩ |
| Owner to consult | ⟨name⟩ |

## §9 Value

| | |
|---|---|
| Benefit type | ⟨savings / lead-time / cost avoidance⟩ |
| Figure | ⟨amount⟩ ⟨year⟩ |
| Reliability | ⟨CALCULATION / ESTIMATION / not yet assessed⟩ |
| Methodology | ⟨the formula, if CALCULATION⟩ |
| Dependency | ⟨what the money waits on⟩ |

## §10 Traces to

⟨plant roadmap item⟩ · ⟨capability⟩ · ⟨library entry, if taken⟩ · ⟨business process⟩

---

## §11 Lane variant — keep only the one that applies

### Handover packet to Information Integration  *(Use Case Support)*

| | |
|---|---|
| Machines + EQ ids | ⟨with current integration status⟩ |
| Signals required | ⟨see §5 — canonical names, in/out, existence verdict⟩ |
| Data path expected | machine → ⟨ingress variant⟩ → edge → offload → ⟨asset⟩ |
| Output data points to register | ⟨name⟩ ⟨uuid to be issued⟩ |
| Acceptance the integration must satisfy | ⟨subset of §6⟩ |
| Known barriers, classified | ⟨from §7⟩ |
| Business case reference | ⟨from §9⟩ |

### Equipment requirement  *(Information Integration)*

| | |
|---|---|
| PLC vendor / model / part number | ⟨joins the Machine List⟩ |
| Network protocol and interfaces | ⟨⟩ |
| Ingress variant | ⟨① edge device / ② connector / ③ aggregation server⟩ |
| Connector / driver | ⟨⟩ |
| **PLC program available?** | ⟨yes / no / requested ⟨date⟩⟩ ★ the breakpoint |
| Tag export available? | ⟨⟩ |
| Companion specification exposed? | ⟨OPC UA for Machinery / EUROMAP / none⟩ |
| Cyber Security / OT sign-off | ⟨required? requested? granted?⟩ |
| Signal standard / data model | ⟨⟩ |

### Project scope baseline  *(Project Support & Application Consultancy)*

| | |
|---|---|
| Stage / gate | ⟨Captured → Evaluated → Assessed → Planned → Handed over → Effective⟩ |
| Investment | ⟨figure⟩ · eCR route ⟨CTO ≤150k / Board >75k⟩ |
| Milestones with acceptance points | ⟨⟩ |
| Resources | ⟨named, per side⟩ |
| Dependencies | ⟨other projects, external decisions, licences⟩ |
| Training + competence requirement | ⟨who must run it afterwards⟩ |
| Flow owner | ⟨named⟩ |

### Request scope  *(Analytical Support)*

| | |
|---|---|
| Question | ⟨one sentence⟩ |
| Decision it supports | ⟨what changes depending on the answer⟩ |
| Data availability verdict | ⟨available / gap ⟨named⟩ / partial ⟨what can be answered⟩⟩ |
| Turnaround expected | ⟨⟩ |
| One-off or recurring? | ⟨decides ad-hoc vs promotion to a standard use case⟩ |
