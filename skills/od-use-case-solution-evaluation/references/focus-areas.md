---
type: Skill Reference
title: Focus areas
description: The 16 IT/OT capability areas a use case's solution can depend on — levels, what each level looks like, and where to set the target from need rather than from the top of the scale.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [use-case-evaluation, maturity-model]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# The 16 focus areas

Each area has discrete levels; higher is not automatically better — see each area's
**Target-setting** line. Four areas (F5, F9, F12, F13, marked **architecture choice**) are
not a ladder to climb at all: they describe a design decision, and the "top" level is
frequently wrong for a stable, high-volume line. `scripts/evaluate_fit.py` reads these levels
and the driver mapping from `model_data.json`; this file is the human-readable form of the
same source.

## F1 · Degree of system familiarity

**Definition.** How well the system knows its own objects (assets, carriers, parts, orders).
**Levels.** 1 unknown — not registered · 2 anonymously known — tracked by type/batch · 3
individually known — unique ID per instance (serial, DMC, RFID) · 4 managed as an entity —
a governed digital record (asset/product twin).
**Candidate when:** a3, a5, a12, a15, a20, a21 rated high/dominant (variant and product-
program complexity, tracking requirements).
**Target-setting.** Level 3 is enough where quality issues can be contained by batch; level
4 only where warranty, recalls or per-piece customer variants demand individual history.

## F2 · Communication capabilities

**Definition.** How an element takes part in information exchange: not at all, only when
polled, by itself, or as a full service-system participant.
**Levels.** 1 none · 2 passive — polled (classic PLC polling, file drops) · 3 active —
pushes on change (OPC UA subscriptions, MQTT) · 4 compliant to the service system — exposes
and consumes defined services with contracts.
**Candidate when:** a16, a19, a22, a25 (resource heterogeneity, information-flow
consistency, hardware/software standardization, process networking).
**Target-setting.** Level 3 for monitoring and analytics; level 4 only where recipes, orders
or setpoints must flow down automatically. Separate "publishes state" from "accepts
commands" in practice — the security and safety implications differ.

## F3 · Degree of intelligence

**Definition.** How much the element does with its own data: nothing, buffer/forward,
recognize states, or decide and act.
**Levels.** 1 none · 2 data handling — buffers/filters/forwards · 3 information
recognition — recognizes states or deviations itself (condition rules, edge analytics,
quality flags) · 4 decision ability — decides within a defined scope.
**Candidate when:** a1, a14 (order-sequence changes, shop-floor control/monitoring
requirements).
**Target-setting.** Default to level 3 (assist). Go to level 4 only per decision, with a
safety case — the papers' own anti-over-engineering message: an assistance system beats a
fully autonomous one more often than not.

## F4 · Localization

**Definition.** Whether an object's position can be determined by the system.
**Levels.** 1 none · 2 localizable — automatic (RFID gates, RTLS, barcode checkpoints,
AGV positions). Binary in the source; in practice distinguish checkpoint-level from
continuous positioning.
**Candidate when:** a3, a5 (material-flow multidimensionality, warehouse/machine variety).
**Target-setting.** Checkpoint-level is usually enough; continuous RTLS only for high-value
or frequently-lost objects.

## F5 · Mobility — architecture choice, not a ladder

**Definition.** Whether elements change position as part of operation.
**Levels.** 1 stationary · 2 partly mobile — relocated between orders/shifts (mobile
carts, modular cells) · 3 mobile — moves during operation (AGV/AMR, mobile robots/devices).
Level 3 has never been observed in the literature case base; treat it as an enabling
property for a specific business need, not a maturity target to climb toward.
**Candidate when:** a18 (demand volatility — mobile resources make reconfiguration cheaper).
**Target-setting.** Pursue only where layout flexibility is a real, named business need.

## F6 · Degree of automation

**Definition.** Share and structure of automated process steps.
**Levels.** 1 manual · 2 partly automated · 3 fully automated — end to end within scope ·
4 modularly automated — standardized, recombinable modules (plug-and-produce, MTP-like).
**Candidate when:** a9, a12, a18, a20 (automation degree, product-program dynamics, demand
volatility, product variety).
**Target-setting.** Driven by volume and variant mix, not by IT maturity — "fully
automated" is frequently the correct end state for a stable, high-volume line; level 4 is
for flexibility, not a universal goal. IT/OT's job is making sure whatever automation exists
is integrable (F2, F10, F16).

## F7 · Style of information provision

**Definition.** How information reaches the people who need it.
**Levels.** 1 none · 2 analogous — paper, shift boards · 3 digital (stationary) — fixed
terminals, line dashboards, andon screens · 4 digital (mobile) — tablets, phones,
role-based content · 5 augmented/virtual reality.
**Candidate when:** a15, a17, a20, a21 (product-program heterogeneity, employee
qualification, product variety/complexity).
**Target-setting.** Level 3-4 for most plants. AR/VR reflects 2017-era framing; in current
practice a conversational assistant on a mobile device is usually more useful — treat AR as
a use-case option, not a maturity level to reach for its own sake.

## F8 · Human-machine interface

**Definition.** How people interact with the system.
**Levels.** 1 none · 2 technical — panels, SCADA screens, keyboard/mouse · 3 natural —
voice, gesture, conversational, intuitive touch.
**Candidate when:** a17 (employee qualification).
**Target-setting.** Harmonized technical HMIs first; natural interfaces as an assistive
layer, not a replacement for safety-relevant panels. "Natural" is now technically cheap —
the hard part is the data and authority behind it (assess alongside F3 and F16).

## F9 · Communication interfaces — architecture choice, not a ladder

**Definition.** The physical layer by which elements connect.
**Levels.** 1 none · 2 cable-based — wired Ethernet or fieldbus · 3 wireless — Wi-Fi,
private 5G, LPWAN. Wireless is a different medium, not a "more mature" one than cable.
**Candidate when:** precondition for F5/F7's mobile levels.
**Target-setting.** Every relevant asset connected and in a segmented OT network (IEC
62443 zones and conduits); wireless where mobility or retrofit requires it, not by default.

## F10 · Communication protocols

**Definition.** Which protocols elements use.
**Levels.** 1 none · 2 proprietary — vendor-specific drivers/formats · 3 standardized —
open standards (OPC UA, MQTT, Modbus TCP, EUROMAP 77/83, umati) · 4 — **not defined in the
source table.** Best-guess operationalization: standardized protocol plus a standardized
semantic information model (companion specs, Sparkplug B, AAS submodels). Treat level 4 as
unconfirmed when you cite it.
**Candidate when:** a2, a11, a16, a22 (interface count, technology-lifecycle dynamics,
resource heterogeneity, hardware/software standardization).
**Target-setting.** Level 3 everywhere for new investments — write it into machine specs.
Level 4 for asset types that recur across many plants, where shared semantics pay off.

## F11 · Degree of data collection

**Definition.** Whether data is collected, collected for later analysis, or real time.
**Levels.** 1 none · 2 historical — logged, available later (historian exports, batch
uploads) · 3 real-time — available in seconds or less to consumers.
**Candidate when:** a1, a14, a19, a23, a25 (order-sequence changes, shop-floor
control/monitoring, information-flow consistency, disruptions, process networking).
**Target-setting.** Real-time for signals that drive decisions within the shift; historical
for analysis and model training — the two are complementary, not sequential steps on one
ladder.

## F12 · Point of information storage — architecture choice, not a ladder

**Definition.** Where data is stored.
**Levels.** 1 none · 2 outsourced — central server/data center/cloud · 3 combined —
local buffer/edge store plus central · 4 embedded — inside the asset or product itself.
The ordering reflects a 2017 decentralization preference; "embedded" is not automatically
better, it is an architecture decision per data type.
**Candidate when:** supports resilience against outages and cross-asset analysis together.
**Target-setting.** Combined (edge buffer + central historian/data platform) as the default;
embedded only where product-carried data is an actual requirement.

## F13 · Point of information processing — architecture choice, not a ladder

**Definition.** Where data is processed.
**Levels.** 1 none · 2 outsourced — all logic central (MES, server, cloud) · 3 combined —
edge pre-processing plus central analytics · 4 embedded — inside the asset (smart sensors,
PLC-embedded analytics). Same caveat as F12: a design decision, not a monotonic ladder.
**Candidate when:** a14, a23 (shop-floor control/monitoring requirements, disruptions).
**Target-setting.** Combined, with a managed edge platform, as the default; embedded only
where a machine vendor delivers it.

## F14 · Data analytics

**Definition.** Analytical depth applied to data.
**Levels.** 1 none · 2 descriptive — reports/dashboards (OEE, scrap) · 3 diagnostic —
root-cause, correlations, drill-downs · 4 predictive — forecasts (predictive
maintenance/quality) · 5 prescriptive — recommendations or optimized actions.
**Candidate when:** a18, a23, a24 (demand volatility, disruptions, delivery-date
uncertainty).
**Target-setting.** Descriptive everywhere; diagnostic per value stream; predictive and
prescriptive per use case, each with its own business case — not as a default escalation.
Note the dependency: descriptive analytics already requires a partly-continuous information
model (F16 level 2) — a use case that wants a dashboard before the data model exists is
scoping the dashboard, not the prerequisite.

## F15 · Structure of the control system

**Definition.** How planning and control decisions are organized.
**Levels.** 1 no control system — manual planning · 2 centralized — one MES/planning
system controls all units · 3 hybrid — central planning, local autonomy for defined
decisions · 4 — **"decentralized", not defined in the source table** beyond the fractal-
factory reference (autonomous units negotiate and decide; roles: observer, analyzer,
resolver, organizer, reporter — close to an agent loop). Reflects a 2017 research agenda;
treat as aspirational, not a confirmed target, when you cite it.
**Candidate when:** a1, a24, a27 (order-sequence changes, delivery-date uncertainty,
planning/control centralization).
**Target-setting.** Hybrid is usually the right target: central planning publishes orders,
local units publish state and decide within defined guardrails.

## F16 · Continuity of the information model

**Definition.** Whether one consistent semantic model spans systems and levels (shop floor,
MES, ERP).
**Levels.** 1 no continuity — each system its own model, interfaces mapped manually · 2
partly continuous — shared models in parts (common material master, partial naming
standards) · 3 continuous — one semantic model end to end; the same asset, order and
product mean the same thing everywhere.
**Candidate when:** a2, a11, a16, a19, a22, a25 — the broadest driver set of any area.
**Target-setting.** The single most strategically important axis and the one the literature
case base barely discriminates on (almost every case sits at "partly continuous"), which
means there is no benchmark to hide behind: level 3 has to be justified from this registry's
own roadmap, planned as a multi-year program with partial continuity per domain as
milestones, not inferred from what similar plants reached.
