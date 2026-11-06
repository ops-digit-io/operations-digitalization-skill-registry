---
type: Skill Reference
title: Process chain practice
description: Method, decision rules, handoff contract, pitfalls and agent notes for the standardized-system step, abstracted from the Operations Digitalization slide decks - the is / is-not boundary and recommended-if trigger per tool, data-class routes, edge versus plain client, wave planning, the operations-concept gate. Guidance only, no figures, no kit or price.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - matching a system to a use case

Deck-derived practice for steps 1b1 and the hand to 1b2 / 1b3. `PROPOSAL` marks the registry's own synthesis; `<to confirm>` marks a safer reading where decks disagree.
Tool status changes over time: **look it up live, time-stamp it, never copy a status into a skill** (see section 4).

## 1. Method in practice

1. Start from the `catalog-usecase` match record (branch 1b: machine not connected). The machine list is the planning backbone: add the machine there first, optionally with its connection method.
2. **Test the tool boundary.** Every shop-floor tool has two lines the entry must carry: what it **is**, what it **is not**, and an **"integration recommended if"** trigger. Examples of the pattern (not a status):
   - quality feedback app: collects part / box / batch quality feedback; is not a KPI calculator and not a master-data store;
   - rule engine: transforms and standardizes streams; is not a substitute for the service bus, for dashboarding or for application connectivity;
   - image library: stores and serves images and inspection results; is not for process parameters and does not run model training;
   - service bus: carries and routes signals; it does not calculate or interpret them; edge platform: not a substitute for data acquisition or an execution system.
3. **Heavy request disguised as a dashboard.** Order or recipe execution, labels, batch genealogy, material validation are execution-system territory. Map the asked functions onto the shop-floor function list
   (data acquisition, scheduling, equipment, materials, information, performance analysis, energy) before choosing a system. Where performance analysis overlaps with an execution system, no decision rule is given: `<to confirm with the OD lead>`.
4. **Pick the route by data class** (feeds `od-equipment-integration`, `od-signal-standardization`):

   | Data class | Examples | Default hub | Note |
   |---|---|---|---|
   | Transactional | events, cycle time, counters, set values, limits, alarms | service bus (OPC UA) | changes are hard to propagate |
   | Time series | curves, process values | MQTT stream | changes easy to propagate |
   | Master data | material, order and product master data (recipes, meter structures, work-centre naming) | ERP is the master; pushes by API | local systems (MES etc.) are derived and report back; a local master does not lead |

5. **Edge device versus plain OPC UA client.** An edge device is needed if: a vision system or robot is involved; the customer expects full traceability (data loss means rejecting parts); high-resolution time series from process-critical sensors;
   inline measurement; advanced analytics (anomaly detection, predictive quality or maintenance) is planned. Not needed if the machine has no high-frequency signals and OPC UA can carry the series.
   For cameras prefer the per-camera edge connector (cheap, quick) over a vendor turnkey adjustment of third-party software; extract features on the edge and forward features or images only.
6. **Where logic lives.** Keep in the PLC what controls the process or depends on equipment condition or safety. Put in the rule engine what needs context across machines or systems, a single-source naming concept, or logic likely to be iterated.
7. **Low-cost reuse option.** Where data frequency is low, one existing edge device or switch with address translation can serve many machines with a single configuration (PLC and screen addresses unchanged). Trial one low-cost device on one machine before ordering more.
8. Hand the cost-template inputs to `od-decision-routing`; write the system match record.

## 2. Decision rules

- **Footprint first.** A standard system is a validated route plus a purchasable kit (see `SKILL.md`). A tool recommendation must name the **defined use case** behind it; a recommendation without a use case is not made.
- **Use one controlled recommendation vocabulary.** The decks use several for the same tool (planned, needed for several use cases, not necessary, not recommended as of now, stop / continue). Until the OD lead fixes one, write the status plus its date plus its source and mark `<vocabulary to confirm>`.
- **Operations-concept gate.** A tool without an operations concept (named operations owner, service level, support level, change and incident process) is not matched for rollout. The decks name "operations concept missing" as the most repeated barrier;
  rollout needs an operations concept and a named run owner; without both, stop until they exist. A request that is really a service gap on an existing tool is not a use-case match - route it to the system and operations-concept discussion.
- **Security-relevant?** Indicators: connects to central systems or holds relevant data; profound effect on manufacturing; holds operational or customer data (exports, pictures, quality data). Yes means the cyber-security route applies (`od-cybersec-gate`), including patch and update management; two paths: substitute the solution, or approve it.
- **Known machine types first.** Scaling known machine types, with at most one unknown type per new deployment, worked; connecting the most difficult machines first burned reputation. Scale known machine types first.
- **Wave size follows budget class and local resources.** Check the plant's staffing and skill for the connection, not only budget. Patch status of installed controllers is a **precondition** on the plan, not a later gate.
- **Layout stability.** Check that the area will not be re-arranged repeatedly before committing an integration wave.

## 3. Handoff contract

| Receives | From |
|---|---|
| match record with branch 1b, plant owner, use case | `catalog-usecase` |
| machine facts: controller vendor and model, protocol, program version, target landing | machine record / machine list |
| status of the plant's operations concept for the tool | IT / application owner |

| Hands on | To |
|---|---|
| system match record; cost-template inputs marked given or `<missing>`; security-relevance answer | `od-decision-routing` (1b2) |
| route, tag-list intent per data class, machine "CV" (program, version history, vendor) | `od-equipment-integration` (1b3) |
| no standard system: reason and missing item | `od-system-fit-check`, Lane 3 front-end |

## 4. Pitfalls and lessons

- **Tool strategy changes over time.** Early material prioritizes one platform and stops others; later material migrates and keeps others; execution-system rollout is described as paused in some places and continued for strategic plants in others. Treat tool status as time-stamped and look it up live.
- **Tool with "recommended if" but no cost class invites scope creep.** Record the cost class (free, per-camera connector, per-plant development and deployment), not a number.
- **Compatibility before cost.** Underestimated cost of connecting existing devices came from incompatible old signals; check protocol and bus compatibility before the cost line.
- **Approval is a request, not research.** For new hardware prepare the security documentation (and a hardened image) up front.
- **Approved is not staffed.** Connectivity budget approved but the plant lacks resources or skill; include the staffing check in the wave decision.
- **Reuse existing infrastructure** and connect whole processes or areas at once, rather than single machines scattered over a plant.

## 5. Questions to ask and definition of done

Machine class and program version? Which data classes does the use case need? High-frequency or vision signals? Is a customer traceability expectation involved? Which tool does the plant already operate and who runs it? Is the connection security-relevant?
Is the area stable? Who at the plant owns the machine side?

**Done:** boundary test written with the matching "is not" line; route stated by data class; cost class (not number) noted; security-relevance answered; operations-concept status named; next step is 1b2 or Lane 3, never silent.

## 6. AI agent operating notes

- **Can do:** match the stated need against the tool boundary table and the recommended-if triggers and return *fit / redesign / escalate* with the boundary sentence cited; classify signals into data classes; list what the match record is missing; draft the machine "CV" and the tag-list proposal from a PLC export; check protocol compatibility.
- **Needs:** machine record, tool entry with date, route evidence from `references/validated-routes.md`.
- **Human gate:** the verdict, any order, any external connection (Cyber Security sign-off), and the choice of a route that is not written down.
- **Must cite:** tool entry and its date, machine list row, route class.
- **Hands over:** the system match record with unknowns left as `<...>`.
