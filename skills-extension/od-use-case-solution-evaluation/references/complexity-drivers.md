---
type: Skill Reference
title: Complexity drivers
description: The 27 drivers that describe why a use case's situation is complex, each mapped to the focus areas it makes a target-raise candidate.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [use-case-evaluation, maturity-model]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# The 27 complexity drivers — the problem side

Rate each against the use case's actual situation, not the plant in general: no
contribution (n) · little (l) · medium (m) · high (h) · dominant (d). Only **h** and **d**
feed step 2 of the method — they are what makes a focus area a candidate for a raised
target. Two people rate independently (the requester and the DBVE/IIAE), then reconcile; a
single self-rating is the weakest version of this step.

| Code | Driver | Category | Focus areas it points at |
|---|---|---|---|
| a1 | Changes in the order sequence | Planning | F15, F11, F3 |
| a2 | Functionalities and interfaces | Organization | F16, F10 |
| a3 | Multidimensionality of material flow connections | Processes | F4, F1 |
| a4 | Hierarchy levels and organization entities | Organization | — (no direct IT/OT lever) |
| a5 | Variety of warehouses, employees and machines to manage | Structure | F4, F1 |
| a6 | Variety of suppliers to manage | Network | — (no direct IT/OT lever) |
| a7 | Heterogeneity of customers and customer groups | Network | — (no direct IT/OT lever) |
| a8 | Strength of competitors | Network | — (no direct IT/OT lever) |
| a9 | Degree of automation | Processes | F6 |
| a10 | Diversity of the sourcing strategy | Organization | — (no direct IT/OT lever) |
| a11 | Dynamics of technology lifecycles | Technology | F10, F16 |
| a12 | Dynamics of product programs | Product | F1, F6 |
| a13 | Vertical integration | Structure | — (no direct IT/OT lever) |
| a14 | Control and monitoring requirements on the shop floor | Processes | F11, F13, F3 |
| a15 | Heterogeneity of the product program | Product | F1, F7 |
| a16 | Heterogeneity of resources | Product | F10, F2, F16 |
| a17 | Employee qualification | Organization | F7, F8 |
| a18 | Demand volatilities | Planning | F6, F5, F14 |
| a19 | Consistency of the information flow along the order process | Structure | F16, F11, F2 |
| a20 | Product variety | Product | F1, F7, F6 |
| a21 | Product complexity | Product | F1, F7 |
| a22 | Standardization of hardware and software | Structure | F10, F16, F2 |
| a23 | Disruptions and outages of production resources | Technology | F14, F11, F13 |
| a24 | Uncertainty of delivery dates | Planning | F14, F15 |
| a25 | Networking of processes and process steps | Processes | F2, F16, F11 |
| a26 | Dynamic of market competition | Network | — (no direct IT/OT lever) |
| a27 | Centralization of planning and control tasks | Planning | F15 |

Seven drivers (a4, a6, a7, a8, a10, a13, a26) are organizational or market factors with no
direct IT/OT lever. Rating them high explains the use case's business context; it names no
focus-area candidate and contributes nothing to step 2.

## How to use

1. Rate all 27 against this specific use case's situation, not the plant's in general.
2. Collect the focus areas mapped to every driver rated h or d — these are the candidates
   for a raised target (step 2 of the method). A use case with no driver above medium has no
   candidates: its envisioned solution should not need anything beyond what already exists,
   and a target set anyway is the over-engineering case `scripts/evaluate_fit.py` flags.
3. Everything not a candidate stays at "good enough" — do not raise a target to match a
   driver that was not actually rated high or dominant.
