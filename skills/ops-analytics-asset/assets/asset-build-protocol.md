---
type: Skill Asset
title: Asset build protocol
description: The defined output of this skill - asset type, ritual, data path and validation record, so deploy-acceptance and deploy-handover can both read it as input rather than ask again.
resource: ../SKILL.md
status: stable
tags: [analytical-support-service, template, protocol]
---

# Analytics asset build — ⟨use case name⟩

Copy once per asset. Fill as the work happens, not afterward — a plant engineer or the next
skill's owner should be able to read this and know what was built, why, from what data, and
whether it has been validated, without opening the asset itself first.

| | |
|---|---|
| **Use case** | ⟨name, plant, line⟩ |
| **From** | ⟨`funnel-use-case` / `funnel-evaluation` protocol reference⟩ |
| **Builder / date** | ⟨name⟩ · ⟨date⟩ |

## 1 · Asset type and ritual

| | |
|---|---|
| **Asset type** | ⟨Dashboard · Report · Analytics workflow · App · Agent⟩ |
| **Why this type, not the default** | ⟨one sentence — see `references/asset-type-and-tier.md` if the default was a dashboard⟩ |
| **Ritual / moment consumed in** | ⟨Daily Gemba · shift check · escalation · other, named⟩ |
| **Decision it supports** | ⟨what the reader does differently because this exists⟩ |
| **If Dashboard — tier handed to `ops-dashboard-engine`** | ⟨manager / analyst / operations⟩ |

## 2 · Data path

| Figure / panel | Source (table, signal UUID or report row) | Confirmed fit-for-use |
|---|---|---|
| ⟨…⟩ | ⟨…⟩ | ⟨`mi-data-availability` verdict + date⟩ |

A figure with no source in the middle column is not ready to deliver — see
`references/lifecycle-and-validation.md`.

## 3 · Validation record

Run the checklist in `references/lifecycle-and-validation.md` and record the result here,
not just "done":

| Check | Result |
|---|---|
| Every figure traces to a nameable source | ⟨pass / gap, named⟩ |
| Data fitness confirmed | ⟨pass / gap, named⟩ |
| Fits inside the ritual (single screen / at a glance) | ⟨pass / gap, named⟩ |
| Non-data pixels reduced, data pixels not drowned | ⟨pass / gap, named⟩ |
| Display medium fits the question | ⟨pass / gap, named⟩ |
| Context supplied (target, trend or comparison) | ⟨pass / gap, named⟩ |
| Delivered and explained to the requester | ⟨pass / gap, named⟩ |

## 4 · Record for handover

| | |
|---|---|
| **Output asset** | ⟨as §1⟩ |
| **Business process** | ⟨…⟩ |
| **Utilization expectation** | ⟨e.g. daily, every shift⟩ |
| **Named plant owner** | ⟨name⟩ |
| **Data path** | ⟨pointer to §2⟩ |

Hand this document to `deploy-acceptance` next. `deploy-handover` reads the same
four fields above once acceptance passes — nothing here needs re-asking.
