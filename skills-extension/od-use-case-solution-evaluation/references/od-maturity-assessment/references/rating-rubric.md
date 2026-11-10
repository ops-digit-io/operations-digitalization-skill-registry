---
type: Skill Reference
title: Rating rubric
description: The 16 IT/OT focus areas read as a qualitative rating rubric for one machine, system or application - level cues, the question to ask, the evidence that counts, the route signal of a low level, the evidence grade and the data and interface inventory.
resource: ../procedure.md
status: draft
owner: human:jakob.gabriel
tags: [practice, maturity, rubric, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Rating rubric - the focus areas applied to one object

Level labels follow the published model (Schott et al. 2020, Table 5); the cues, questions, evidence and route signals are the
vault's operationalization, restated for a single machine, system or application. `PROPOSAL` = synthesis of this skill, not in the
source. The full level tables and target guidance per area are in `od-use-case-solution-evaluation` (`references/focus-areas.md`).

## Rating rules

1. **Rate what is in use today**, in the configuration that actually runs. A capability that is licensed, installed or merely
   possible but not switched on does not raise the level; note it as potential.
2. **Level = the highest level whose cue is observed**, and the levels below it are not contradicted. If cue 3 is seen but cue 2 is
   not, find out why before accepting level 3.
3. **Three states besides a level**: `n/a` (the area does not apply to this object type, with a reason), `unknown` (nobody could
   say; an open question with an owner) and `mixed` (parts of the object differ; split the object instead of averaging).
4. **Evidence grade** on every rating (PROPOSAL, mirrors the source's "observable evidence" habit):
   - **S** seen: read in the system, the configuration, the network, a flow, a manual, or witnessed;
   - **T** told: stated by a named role, not checked;
   - **A** assumed: inferred from type, vendor or estate habit.
   A profile that rests mostly on A is a list of questions, not a profile. Only S and T may feed a route signal; A may only open a question.
5. **Split where the source says so**: identity of assets versus identity of products (F1) often differ; so do polled signals
   versus pushed events on one machine (F2).
6. **Higher is not better.** F5, F9, F12 and F13 are architecture choices from a decentralization paradigm, not goals; the top level
   there is often wrong. F10 and F15 each carry a level the published table leaves undefined (`model-caveats.md`).

## Foundation: connect, identify, speak, mean the same thing

| Area | Ask about the object | Level cues (low to high) | Route signal of a low level |
|---|---|---|---|
| **F9 Communication interfaces** (architecture choice) | Is it on a network? Wired or wireless? In which segment, behind what DMZ? | 1 not networked; 2 cable (Ethernet, fieldbus); 3 wireless (Wi-Fi, private cellular) | Level 1 or no usable network drop: nothing downstream works; a barrier of the legacy-hardware or information class (`od-equipment-integration`) |
| **F1 System familiarity** | Which objects does it identify, by what ID, and which system is master for the ID? | 1 unknown; 2 by type, lot or batch; 3 each instance has a readable ID; 4 each instance has a managed digital record with an owner | Level 2: batch-level answers only; per-part joins and genealogy are out of reach. Level 4 needs a registry the namespace can reference |
| **F10 Communication protocols** | Which protocol and which information model, per interface? Any custom driver or gateway, and who keeps it? | 1 none; 2 proprietary (vendor-specific); 3 open standard (OPC UA, MQTT, Modbus TCP, vendor-neutral machine interfaces); 4 undefined in the source, read as standard protocol plus standard semantics | Level 2: route through a vendor connector or fallback ladder (`od-equipment-integration`); level 1: no route |
| **F2 Communication capabilities** | Is data read only when polled, pushed on change, or exchanged as defined services (commands, recipes, state)? | 1 none; 2 passive (polled, file drop); 3 active (push, subscribe); 4 service-compliant (defined services with contracts) | Level 2: a gateway or edge step is needed to get events; level 4 only where setpoints or recipes must flow down |
| **F16 Continuity of the information model** | Do asset, order, material and signal names mean the same in every system it touches? Who owns the model? | 1 each system has its own model, mapping by hand; 2 partly shared (common master, partial naming standard); 3 one consistent model across systems | Level 1: connected but not standardized; hand to `od-signal-standardization` before any dashboard |

## Data: collect, store, process, analyse

| Area | Ask about the object | Level cues | Route signal of a low level |
|---|---|---|---|
| **F11 Data collection** | Which signals, at what rate, with what delay to the consumer? Is the time stamp applied at the source? | 1 none; 2 historical (logged, available later); 3 real-time (seconds or less) | Level 2 cannot carry a within-shift decision; a "live" ask on it is a data gap for `od-data-availability-check` |
| **F12 Information storage** (architecture choice) | Where is the system of record per data type? What happens to data when the network fails? | 1 none; 2 central only (outsourced); 3 local buffer plus central (combined); 4 in the asset or product itself | Level 2 and a traceability or high-rate need: data loss on outage, which is an edge signal |
| **F13 Information processing** (architecture choice) | Which calculations must work without the central systems? Who owns the edge applications? | 1 none; 2 all logic central; 3 edge pre-processing plus central; 4 inside the asset | Level 2 and local logic needed: edge platform or controller logic; level 3 needs a managed edge with an owner |
| **F14 Data analytics** | Which analyses run on this object's data today, on which tool, built and run by whom? | 1 none; 2 descriptive (reports, dashboards); 3 diagnostic (root cause, drill-down); 4 predictive; 5 prescriptive | A request for level 4 or 5 on a source that is not yet at level 2 and F11 level 3 is out of order (`od-system-fit-check` AI-above-reporting rule) |

## Intelligence and control

| Area | Ask about the object | Level cues | Route signal of a low level |
|---|---|---|---|
| **F3 Degree of intelligence** | Where are derived states computed (controller, edge, MES, spreadsheet)? Which decisions are automated, which taken by people from data? | 1 none; 2 buffers, filters, forwards raw data; 3 recognizes states and deviations itself; 4 decides within a defined scope | Default is assist (level 3); level 4 only per decision, with a safety case |
| **F15 Structure of the control system** | Who plans and who decides locally? How does a short-term order change propagate? | 1 no systematic control; 2 centralized (central planner or MES controls all); 3 hybrid (central plan, local autonomy within guardrails); 4 decentralized (undefined in the source, agent-based) | A requested function that is control-system territory (execution, sequencing) signals MES shape in `od-system-fit-check` |
| **F6 Degree of automation** | Where are manual steps a bottleneck or a quality risk? Are automation modules standard across plants? | 1 manual; 2 partly automated; 3 fully automated within its scope; 4 modularly automated from standard modules | Driven by volume and variant mix, not by IT; IT/OT only ensures what exists is integrable (F2, F10, F16) |

## Point of use and physical

| Area | Ask about the object | Level cues | Route signal of a low level |
|---|---|---|---|
| **F7 Information provision** | Where do people get information: nothing, paper, fixed screen, mobile device, AR? Is content role-based? | 1 none; 2 analogous (paper, boards); 3 digital stationary; 4 digital mobile; 5 augmented or virtual | Paper as master: the result needs a digital point of use before a dashboard has value |
| **F8 Human-machine interface** | How many different HMIs does an operator use per shift? Harmonized across vendors and plants? | 1 none; 2 technical (panel, SCADA, keyboard); 3 natural (voice, gesture, conversational) | Harmonize technical HMIs first; natural interfaces as assist only, never in place of safety-relevant panels |
| **F4 Localization** | Which objects are searched for regularly? Location captured at checkpoints or continuously? | 1 none (known by people or layout); 2 determined automatically | Checkpoint level is usually enough; continuous tracking only for high-value or often-lost objects |
| **F5 Mobility** (architecture choice) | Which assets move, and how are they coordinated? Is wireless coverage sufficient where they move? | 1 stationary; 2 relocated between orders or shifts; 3 moves during operation | Pursue only where layout flexibility is a real business need |

For a pure software object (an application, a dashboard) F4, F5 and F6 are usually `n/a`; for a machine F7 and F8 describe its own
panel and how its data reaches people, not the plant's dashboards.

## Data and interface inventory (questions that feed several areas)

Ask these once per object, they feed the areas named.

| Topic | Questions | Feeds |
|---|---|---|
| Network infrastructure | Structure; components and their services; how provider and consumer connect; can the service quality be influenced? | F9, F2 |
| Computing capacity | Capacity available; equipment of the work systems; local buffering; can modules be rolled out to the work systems? | F12, F13 |
| Software | Which components are available; what infrastructure they expect; how they are installed | F10, F13 |
| Domain models | The meta-models behind them; how products are modelled | F16, F1 |
| Process models | How process models are designed; which process definitions exist | F16, F15 |
| Data suppliers | Which services deliver which data, in which quality, quantity and timing | F11, F2, F10 |
| Data consumers | Which services need which data, in which quality, quantity and timing | F11, F14, F7 |

## Interview order (PROPOSAL)

Foundation first (F9, F1, F10, F2, F16), then data (F11 to F14), then the rest. Ask the controls and network questions of the
IT/OT side, the process and decision questions of the plant owner, and take the manual and the configuration as the tie-breaker.
Stop an interview area at the first level whose cue is not seen; there is no point probing level 4 above an unseen level 2.
