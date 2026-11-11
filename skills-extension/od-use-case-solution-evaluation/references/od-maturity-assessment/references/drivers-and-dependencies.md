---
type: Skill Reference
title: Drivers and dependencies
description: How an object profile becomes complexity drivers and candidate areas, the prerequisite chain between areas as a backbone, plausibility checks on a profile, and how to sequence gaps without trusting the source dependency table mechanically.
resource: ../procedure.md
status: draft
owner: human:jakob.gabriel
tags: [practice, maturity, drivers, dependencies, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Drivers and dependencies - from profile to candidate areas to gap chain

Drivers are coded `a1` to `a27` as in the published problem model (Schott et al. 2020, Table 4); the mapping of drivers to areas is
the knowledge base's, not the paper's. The complete list and mapping is in `od-use-case-solution-evaluation` (`references/complexity-drivers.md`).
`PROPOSAL` = synthesis of this skill.

## 1 Rate the drivers (problem side)

- Scale per driver: **n** no contribution, **l** little, **m** medium, **h** high, **d** dominant.
- Two raters, independently, then reconcile: the plant-side owner and the IT/OT side. The source used one self-assessment per plant, which
  is its weakest point.
- Rate the **object in its context** (this machine on this line, this app in this process), not the plant in general.
- Only **h** and **d** matter for targets. Seven drivers (a4, a6, a7, a8, a10, a13, a26: hierarchy, suppliers, customers, competitors,
  sourcing, vertical integration, market competition) have no IT/OT lever: they explain context and similarity, not a roadmap item.

## 2 Fact to driver to area (object-level reading, PROPOSAL)

What you observe on the object, the driver family it points at, the areas that respond.

| You observe on the object | Driver family | Areas that respond |
|---|---|---|
| Many variants, changing product program, complex products | a12, a15, a20, a21 | F1, F7, F6 |
| Mixed vendors, mixed controllers, short technology lifecycles, no hardware or software standard | a2, a11, a16, a22 | F10, F2, F16 |
| Tight monitoring demand, frequent order changes, frequent stops, uncertain dates, central planning load | a1, a14, a23, a24, a27 | F11, F13, F3, F14, F15 |
| Information that breaks along the order process; many linked process steps | a19, a25 | F16, F11, F2 |
| Many machines, stores and people to manage; complex material flows | a3, a5 | F4, F1 |
| Low operator qualification | a17 | F7, F8 |
| Volatile demand | a18 | F6, F5, F14 |
| High degree of automation already | a9 | F6 |

Collect the areas of every **h** or **d** driver. They are the **candidate areas**. If nearly every area is a candidate, the ratings did
not discriminate: redo step 1. Typical objects touch a handful of areas, not all of them.

## 3 Prerequisite backbone (solution side)

The published dependency table (JMTM Table 10) is incomplete and inconsistent in its own indexing; the knowledge base reads it with prerequisite
levels shifted by one (the "best-fit reading") and still finds that it does not reproduce the published development paths. Use the
**backbone** below to order gaps, and the table only as a prompt. The order is the knowledge base's recommendation for the UNS and AI roadmap
(PROPOSAL until validated internally):

1. **Connectivity and segmentation**: F9, every relevant asset on a segmented OT network.
2. **Identity**: F1 level 3 for assets, unique IDs, one registry.
3. **Open protocols**: F10 level 3 and F2 level 3 (event-driven).
4. **Semantic model**: F16 level 2 per domain, a defined hierarchy and payload convention.
5. **Real-time state and history**: F11 level 3 for decision-relevant signals; F12 and F13 combined with a managed edge.
6. **Analytics ladder**: F14 descriptive, then diagnostic, then predictive, per use case.
7. **Assist before decide**: F3 level 3 broadly, level 4 per decision with a safety case; F15 hybrid.
8. **Point of use**: F7 digital stationary or mobile, F8 harmonized, assistants on top.

Steps 1 to 4 are the foundation (namespace); 5 to 7 are where the AI layer starts to pay off.

## 4 Plausibility checks on a profile (published prerequisites, best-fit reading)

A profile that breaks one of these has a rating error or a hidden component (a gateway, a historian, a manual step). Resolve before it
feeds a route; do not "fix" the profile to make it consistent.

| If rated | the published prerequisites are | Check |
|---|---|---|
| F2 passive | F1 anonymously known, F9 cable | Polled data without a network? |
| F2 active | F1 individually known | Push events without identifiable sources? |
| F1 managed as an entity | F2 passive, F12 outsourced | A twin record with no data path or store? |
| F3 data handling | F1 managed, F2 passive, F9 cable, F13 outsourced | Filtering with no processing point? |
| F3 information recognition | F2 active, F13 combined, F14 descriptive | Self-detected states with no push, edge or reporting? |
| F4 localizable | F1 individually known, F2 passive | Location of objects that have no ID? |
| F7 digital stationary | F8 technical, F16 partly continuous | Screens fed from unaligned models? |
| F10 level 4 | F16 partly continuous | Standard semantics without a shared model? |
| F11 historical | F2 passive | Logged data without a path? |
| F12 combined | F3 data handling | Local buffer without local handling? |
| F14 descriptive | F16 partly continuous | Dashboards on data with no common names? |
| F14 diagnostic | F11 real-time | Root-cause tooling on late data? |
| F6 modularly automated | F2 service-compliant, F5 partly mobile, F10 standardized, F15 centralized | Plug-and-produce claimed without these? |

A machine at "predictive" with "historical" collection is not impossible (training on history), but it is a question to ask.

## 5 Sequence the gaps

1. List every candidate area where a **need** (a use case, a tool request, a route) exceeds the as-is level. A gap needs a named driver or a
   named business need; "because the platform supports it" is not one.
2. For each gap read the prerequisites (backbone, then the table), and check whether the prerequisite levels are already met by this
   object.
3. Items with no open prerequisite go into step 1; the rest follow their prerequisites. Parallel steps are allowed where the object allows.
4. Attach each step to a use case, an owner role and a business case. Maturity without one is not planned.
5. Name the owning skill per gap (as in `od-use-case-solution-evaluation`): F9 and F10 to `od-equipment-integration`; F11 and the push half
   of F2 to `od-data-availability-check`; F16 to `od-signal-standardization`; the rest stays with the use case or tool request.

## 6 Target setting in one line per area family (the source's own guidance)

- Identity: level 3 where a problem can be contained by batch; level 4 only where warranty, recall or per-piece variants demand history.
- Protocols and communication: open standard for every new investment (write it into the machine specification); the semantic level only for
  asset types that exist in many plants. Push events for monitoring and analytics; service level only where recipes or setpoints flow down.
- Data: real-time for decisions inside the shift, historical for analysis and training; combined storage and processing with a managed edge by
  default; embedded only where product-carried data or vendor delivery makes it free.
- Intelligence and control: assist before decide; hybrid control with guardrails; analytics descriptive everywhere, diagnostic per value stream,
  predictive and prescriptive per use case with a business case.
- Point of use: stationary or mobile digital for most; AR only for specific training or complex maintenance; natural interfaces as assist.
