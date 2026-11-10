---
type: Skill Reference
title: Legacy system assessment
description: "Guidance, no figures. The other half of the requirement: checking the legacy applications a demand touches and whether it fits the lean footprint."
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [requirements, legacy, it-systems]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# The (legacy) MF IT system assessment

Half of UC-03's stated output: *"integration-ready requirement spec **+ legacy MF IT system
assessment**"*. It answers one question — **does this requirement need, replace, or collide
with something already installed?** — and it is the step that catches a requirement about to
rebuild what exists.

**The Legacy Application List tracks the installed applications.** Check against it before
specifying anything. Re-count on the live list and quote the export date; no figures are kept
here.

---

## What the list holds

| Field | Typical values | How to read it |
|---|---|---|
| Category | PLC programming / configuration, laboratory software, equipment configuration, camera system configuration, custom SCADA, printer, quality software, MES, dashboarding, and others | Most of the list is engineering and laboratory tooling; the SCADA, MES and dashboard classes matter most for a requirement |
| Functional mapping | PLC programming and configuration, quality laboratory data acquisition, MES, quality data acquisition, logistics, MDA/PDA, traceability, and others | Search here first; it may hold mixed entries |
| Plants | One or several plants per application | **An application deployed at exactly one plant** is both the easiest to replace and the most likely to be somebody's daily tool that nobody outside that plant knows about |

---

## The four questions

### 1 · Does something already do this?

Search the list by **functional mapping** first, then category. A requirement whose function
is already covered is one of three things, and they are not the same:

| Finding | Then |
|---|---|
| The existing app does it well | **Refuse the build.** Integrate with it, or do nothing |
| The existing app does it badly | The requirement is a *replacement* — say so, and scope the migration |
| The existing app does part of it | Scope the delta only, and state the boundary explicitly |

### 2 · Is it supported?

| Support concept | Means |
|---|---|
| Internal Support | Somebody here maintains it — find out who |
| External Support Contract | A contract exists; check its scope |
| Maintenance & Run Concept | Documented run concept |
| *(not recorded)* | **Unknown — usually the largest group.** Blank is not "no support" |

Supplier status is `IN SERVICE` or `SERVICE STOPPED`, and is often unrecorded.

> A `SERVICE STOPPED` application in the requirement's path is a **major blocking point**, not
> a footnote. So is an unrecorded one until somebody checks.

### 3 · What does the licence cost?

| Licence | Means |
|---|---|
| **unknown** | Common. A real dependency with a real lead time |
| No licence required | |
| Local licence available | |
| OESL licence required | Needs the central licence process |

If the requirement depends on an application with an unknown licence position, record it in §7
and give it an owner. Licensing is a recurring blocker class in the corpus.

### 4 · Does it fit the footprint?

The strategy is a deliberately **small operational footprint**, and broad tool proliferation
is an explicit non-bet. Apply the deployment reality (the live position is in the Tool Overview
and `od-system-fit-check`; status below is guidance on how to treat each system, not a
snapshot):

| System | How to treat it | Consequence for a requirement |
|---|---|---|
| **MES** | Rollout on hold, ERP/S4HANA-dependent; only the pilot plants carry one | A requirement depending on MES rollout is **blocked, not planned**. Check light-weight substitutes such as QFPR |
| **MSB** | Limited | Confirm availability at *this* plant before depending on it |
| **MDA/PDA** | Deployed at many plants | Likely available; verify per plant |
| **MIL** | High demand, limited deployment | Do not depend on it until the plant row shows it |
| **EMS** | Rollout subject to operational criteria; confirm the current position | Do not extend it without confirming |
| **IIoT Edge** | The widely deployed base | The safe assumption; still verify per plant |

**A requirement that needs a system outside the footprint is refused at intake** and routed
to strategy as a tool-rollout decision. It is not a use case, and treating it as one produces
an item that sits in the portfolio for a year.

---

## What the assessment records

Add this to §8 of the requirement:

```text
Systems required:        ⟨list⟩
Footprint verdict:       inside · outside → refuse & route · substitute available ⟨name⟩
Legacy applications touched:
  ⟨app⟩ | ⟨category⟩ | ⟨plants⟩ | support: ⟨concept⟩ | supplier: ⟨status⟩ | licence: ⟨status⟩
Relationship:            integrate with · replace · unaffected
Owner to consult:        ⟨name⟩
```

**"Unaffected" is a valid and useful answer** — but only once it has been checked. The legacy
list is long precisely because nobody checked, repeatedly.

---

## The trap this step exists to catch

A requirement that looks new and is not. The corpus records blockers like
*"potentially needed: QFPR?"* and *"open access to ⟨vendor⟩ system (API)"* — both are this
assessment surfacing late, as a blocker, instead of early, as a decision.

Doing it at requirement time costs an hour. Doing it at integration time costs the slot.
