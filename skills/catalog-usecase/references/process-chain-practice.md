---
type: Skill Reference
title: Process chain practice
description: Method, decision rules, handoff contract, pitfalls and agent notes for the catalog skill, abstracted from the Operations Digitalization slide decks - pick and graduation, standardized-system match, go-live self-check. Guidance only, no figures, no kit or price.
resource: ../SKILL.md
status: draft
tags: [all, practice]
---
# Process chain practice

Three parts, one per merged skill. `PROPOSAL` marks the registry's own synthesis; `<to confirm>` marks a safer reading where decks disagree. Section numbers restart in each part.

## Part A - Picking and graduating (steps 1a1, 1b1, 26)

Deck-derived practice for steps 1a1, 1b1 (pick) and 26 (graduate). Statements marked `PROPOSAL` are the registry's own synthesis.
Where the decks disagree the safer reading is written and tagged `<to confirm>`.

### 1. Method in practice

**Picking (Lane 1).**
1. The plant states the need in its own words. Reduce the sentence to **object** (part, order, tool, recipe, batch, carrier), **event** (error, change, stop, NOK part) and **time axis**.
   Many "unique" requests collapse to a few shapes this way; ask for object and event before judging uniqueness (`od-use-case-intake-triage`).
2. Match the shape to a capability template and a library entry. A request that only changes the look of an existing screen is not a catalog match.
3. Check the two preconditions the decks repeat: **the machine is connected** and **the needed signals are selected**. A use case is available only for machines that are already connected;
   a requirement beyond the agreed timeframe becomes an additional use-case phase, not scope creep.
4. Branch 1a or 1b as in `SKILL.md`. Ask who at the plant will use the result and in which meeting (see section 5).

**Graduating (end of Lane 2).** The decks describe one graduation pattern:

| Stage | What exists | Counts as catalogued? |
|---|---|---|
| Proof of concept | a minimal test that de-risks the idea | no |
| Validated prototype | works for one plant, validated with its owner | no - it is a candidate |
| Configurable container app | flexible algorithms and configurable rule sets, packaged, deployed through the app store | yes, once the four conditions in `SKILL.md` hold |
| Standard | the app is the thing other plants take | yes |

A use case is **standard** when a validated prototype exists and only the more flexible, configurable container or app is missing. It is **special** when its data source is
proprietary or external, or when it is process-specific and the generic method is still undefined. Machine-learning-based standards additionally need: a requirements document,
data from several plants, a validated model, the model packaged with a defined interface to its trained parameters, a monitoring and retraining process and a visualization concept validated with the plant.

### 2. Decision rules

**Archetypes - three classes, one action each** (deck rule, restated):

| Archetype | Depends on | Typical constraint | Action in the catalog |
|---|---|---|---|
| Standard, **cross-process** | nothing about the core process | has limits (for example not meaningful for continuous processes) and needs integration work because data models differ | catalogue with priority; state the limits in the entry |
| Standard, **per-process** | process values of one core process | fewest constraints; scales fastest | catalogue; instantiate from the process data model |
| **Unique** | factory conditions, a legacy system, a one-off problem | not scalable beyond the site | do not catalogue; run an impact analysis first, then decide |

Custom use cases are possible only if the expected value is very high; they may be prototyped, and count as mature only after integration into the standard systems.

**Triage buckets** (deck, `PROPOSAL` for using them as catalog routing): *just do* - generic dashboard, notification or energy case on already integrated equipment, copy from another site,
no new development; *go forward* - continue or integrate an earlier proof of concept that depends on a shared enabler; *lead change* - exploratory, needs a prototype first, human call.

**Kill and hold.** A request can end as cancelled with a recorded reason (no data foundation, insufficient savings, another party already collects the data). Keep the reason so the idea is not re-raised from scratch.

**Plant tiering decides capacity, not eligibility.** A first-mover plant gets central support first; a fast follower picks from the catalog with central help only when capacity allows.
First-mover criteria in the decks: high estimated value-add, coverage of regions, segments and technologies, capacity and knowledge in the plant, integration synergies, and a dedicated, staffed key user.
The tier is a property of the plant, looked up live (`od-context-freshness`); never copy a plant list into a skill.

**Zero-saving scaled entries.** Where an entry is deployed widely and reports no saving, do not write "no potential" - write "to be evaluated" and list three things: where it saved, where it was deployed without saving, where it still has potential.
Until investigated the entry stays "to be evaluated". Only a human (the OD lead with the plant owner) may decide "no potential" or retirement; an agent never writes it.

### 3. Handoff contract

| From | Must hand over | Receives from this skill |
|---|---|---|
| `od-use-case-intake-triage` | object / event / time, archetype guess, machine-connected flag | - |
| `od-data-availability-check` | verdict on signals, per plant | - |
| `od-use-case-standardization` / `od-use-case-standardization` | template, cluster, CSP status, graduation checklist | - |
| to `od-analytics-asset-build` (1a) | match record, entry id, reference plant, deltas to record | the baseline to copy |
| to the system part (1b) | match record, machine class, where the data should land | - |
| to Lane 2 / Lane 3 | reason for fall-through, what was missing | - |
| to `od-handover-and-adoption` | **named utilization moment** (who opens it, in which meeting, which action follows) | - |

### 4. Pitfalls and lessons

- **Deployed is not used.** Many widely scaled use cases ran with no reported saving. The count of delivered entries is not an impact indicator; a high count can hide unreported impact or unused potential. A catalog is judged by utilization and by savings where they exist.
- **Visibility alone creates no saving.** Savings appeared where the screen drove a defined action by a named owner. A catalog entry without an action owner is a build smell.
- **Local solutions are input, not new demand.** A plant may already run a local solution that fits the method but is not standard. Treat it as input to standardization.
- **Dashboards per plant, never harmonized** is a recurring debt. Manual-entry use cases (lab data, quality data) need data model, storage, input screen and analytics in one standard, otherwise every plant builds its own variant.
- **Rollout is gated by integration, not by the dashboard.** A dashboard "ready" for a second process is pending until that process's machines and tags are selected.
- **Entry rots.** Use-case lists and libraries hold stale or low-value entries and drafts with empty data and dependency boxes. A canvas with empty data and dependency boxes is not ready for the data check.

### 5. Questions to ask and definition of done

- Which object does the answer need to be keyed on, and where does its identifier live today (signal, MES or ERP, manual entry)?
- Live view, report on a cadence, or a record to be entered? What decision follows the number, and who is the named plant owner?
- Is there a plant-side method the screen feeds (changeover method, digital Gemba, switch-off campaign)? The pairing of *standard method + digital standard use case + standard process* is what makes an entry get used.
- What can the use case do, and what can it not do (for example: explain an equipment issue and notify, but not recommend or solve)? Put both in the entry.

**Entry content the decks want** (a catalog entry is also its own marketing page): used for what; why (the story behind it); how it helps (functions); what it can do; what it cannot do; an example screen; reference plant; maturity;
where applied; next call to action; and *can it substitute an existing manual practice*.

**Done for a pick:** match record written; branch named; preconditions evidenced; utilization moment named; no figure without source.

### 6. AI agent operating notes

- **Can do:** reduce the plant's sentence to object / event / time; propose template and library entry; list which preconditions are evidenced; flag empty canvas boxes (data, dependencies, success criteria); check graduation conditions and list the missing ones; draft the entry text from the plant's answers.
- **Needs:** use-case list row, machine list status, library entry, CSP field, read dates.
- **Human gate:** the plant decides what it runs; the CSP decision stays with its owner; assigning *lead change* and keeping a *unique* case alive are human calls.
- **Must cite:** library entry id, list row, source of the connected-machine fact, read date.
- **Hands over:** the match record to the next skill named in `SKILL.md`, with the utilization moment filled or marked `<to confirm>`.

## Part B - Matching a system to a use case (step 1b1 and the hand to 1b2 / 1b3)

Deck-derived practice for steps 1b1 and the hand to 1b2 / 1b3. `PROPOSAL` marks the registry's own synthesis; `<to confirm>` marks a safer reading where decks disagree.
Tool status changes over time: **look it up live, time-stamp it, never copy a status into a skill** (see section 4).

### 1. Method in practice

1. Start from the the use-case part match record (branch 1b: machine not connected). The machine list is the planning backbone: add the machine there first, optionally with its connection method.
2. **Test the tool boundary.** Every shop-floor tool has two lines the entry must carry: what it **is**, what it **is not**, and an **"integration recommended if"** trigger. Examples of the pattern (not a status):
   - quality feedback app: collects part / box / batch quality feedback; is not a KPI calculator and not a master-data store;
   - rule engine: transforms and standardizes streams; is not a substitute for the service bus, for dashboarding or for application connectivity;
   - image library: stores and serves images and inspection results; is not for process parameters and does not run model training;
   - service bus: carries and routes signals; it does not calculate or interpret them; edge platform: not a substitute for data acquisition or an execution system.
3. **Heavy request disguised as a dashboard.** Order or recipe execution, labels, batch genealogy, material validation are execution-system territory. Map the asked functions onto the shop-floor function list
   (data acquisition, scheduling, equipment, materials, information, performance analysis, energy) before choosing a system. Where performance analysis overlaps with an execution system (MES), choose the lighter solution and name the overlap explicitly; do not build in parallel what the execution system already does.
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

### 2. Decision rules

- **Footprint first.** A standard system is a validated route plus a purchasable kit (see `SKILL.md`). A tool recommendation must name the **defined use case** behind it; a recommendation without a use case is not made.
- **Use one controlled recommendation vocabulary.** The scale is: recommended / recommended if ⟨condition⟩ / not recommended / not available. The decks use other words for the same tool (planned, needed for several use cases, not necessary, stop / continue); translate them to this scale. Every status carries its date and its source.
- **Operations-concept gate.** A tool without an operations concept (named operations owner, service level, support level, change and incident process) is not matched for rollout. The decks name "operations concept missing" as the most repeated barrier;
  rollout needs an operations concept and a named run owner; without both, stop until they exist. A request that is really a service gap on an existing tool is not a use-case match - route it to the system and operations-concept discussion.
- **Security-relevant?** Indicators: connects to central systems or holds relevant data; profound effect on manufacturing; holds operational or customer data (exports, pictures, quality data). Yes means the cyber-security route applies (`od-cybersec-gate`), including patch and update management; two paths: substitute the solution, or approve it.
- **Known machine types first.** Scaling known machine types, with at most one unknown type per new deployment, worked; connecting the most difficult machines first burned reputation. Scale known machine types first.
- **Wave size follows budget class and local resources.** Check the plant's staffing and skill for the connection, not only budget. Patch status of installed controllers is a **precondition** on the plan, not a later gate.
- **Layout stability.** Check that the area will not be re-arranged repeatedly before committing an integration wave.

### 3. Handoff contract

| Receives | From |
|---|---|
| match record with branch 1b, plant owner, use case | the use-case part |
| machine facts: controller vendor and model, protocol, program version, target landing | machine record / machine list |
| status of the plant's operations concept for the tool | IT / application owner |

| Hands on | To |
|---|---|
| system match record; cost-template inputs marked given or `<missing>`; security-relevance answer | `od-decision-routing` (1b2) |
| route, tag-list intent per data class, machine "CV" (program, version history, vendor) | `od-equipment-integration` (1b3) |
| no standard system: reason and missing item | `od-system-fit-check`, Lane 3 front-end |

### 4. Pitfalls and lessons

- **Tool strategy changes over time.** Early material prioritizes one platform and stops others; later material migrates and keeps others; execution-system rollout is described as paused in some places and continued for strategic plants in others. Treat tool status as time-stamped and look it up live.
- **Tool with "recommended if" but no cost class invites scope creep.** Record the cost class (free, per-camera connector, per-plant development and deployment), not a number.
- **Compatibility before cost.** Underestimated cost of connecting existing devices came from incompatible old signals; check protocol and bus compatibility before the cost line.
- **Approval is a request, not research.** For new hardware prepare the security documentation (and a hardened image) up front.
- **Approved is not staffed.** Connectivity budget approved but the plant lacks resources or skill; include the staffing check in the wave decision.
- **Reuse existing infrastructure** and connect whole processes or areas at once, rather than single machines scattered over a plant.

### 5. Questions to ask and definition of done

Machine class and program version? Which data classes does the use case need? High-frequency or vision signals? Is a customer traceability expectation involved? Which tool does the plant already operate and who runs it? Is the connection security-relevant?
Is the area stable? Who at the plant owns the machine side?

**Done:** boundary test written with the matching "is not" line; route stated by data class; cost class (not number) noted; security-relevance answered; operations-concept status named; next step is 1b2 or Lane 3, never silent.

### 6. AI agent operating notes

- **Can do:** match the stated need against the tool boundary table and the recommended-if triggers and return *fit / redesign / escalate* with the boundary sentence cited; classify signals into data classes; list what the match record is missing; draft the machine "CV" and the tag-list proposal from a PLC export; check protocol compatibility.
- **Needs:** machine record, tool entry with date, route evidence from `references/validated-routes.md`.
- **Human gate:** the verdict, any order, any external connection (Cyber Security sign-off), and the choice of a route that is not written down.
- **Must cite:** tool entry and its date, machine list row, route class.
- **Hands over:** the system match record with unknowns left as `<...>`.

## Part C - Going live without OD labour (step 1a3, and 1b4)

Deck-derived practice for steps 1a3 and 1b4 (and the same checks at the end of step 26). The numbered guardrails G1 to G19 stay in `SKILL.md` and the other references.
This file adds **process-level candidates**, labelled P1 to P7 so they do not collide with the G numbers. All are `PROPOSAL`: the decks support the lesson, the OD lead decides whether it blocks or warns.

### 1. Method in practice

1. The plant owner (a role) opens the match record from the use-case part and, on branch 1b, the system match record.
2. Run G1 to G7, then the P-candidates below when the plant has built or copied the screen itself.
3. Do one **deep dive against the paper process** before declaring the screen live: compare the screen with the plant's production records (and, for cycle time, the engineering records), explain every difference
   (breaks, shift changes, tolerance not yet applied), then settle signal selection and categories. Run one deep dive with production and one with engineering.
4. Name the **utilization ritual** in the record: who opens the screen, in which meeting, which action follows and who owns it. Write the expectation into the record before go-live.
5. The plant decides to go live. The skill never does.

### 2. Process-level guardrail candidates

| # | Candidate | Lesson behind it | Suggested setting |
|---|---|---|---|
| P1 | **Reconciled with the paper process** - differences between screen and record are explained, not ignored | dashboards were accepted only after reconciliation; unexplained downtime differences destroy trust | block |
| P2 | **Utilization ritual named** - who opens it, when, which action follows | deployment without a defined routine produced no saving; the successful plants defined the utilization process with production and the operational-excellence function first | block |
| P3 | **Action owner named** - a screen with no owner for the action it should trigger | visibility alone created no saving; savings appeared where a screen drove a defined action | warn |
| P4 | **Operations concept present** - business owner, IT owner, service concept, roles, change and risk process | tools without an operations concept were the most repeated rollout barrier | block for a new system; warn for a catalogued template on existing systems |
| P5 | **Old process has an owner for switching it off** | parallel running of old and new because nobody trusted the new process and nobody was assigned to stop the old one | block |
| P6 | **IT changes requested early** - notification channel, data historization, reverse proxy, user access | alert use cases stalled on late change requests; architecture changes mid-sprint cost weeks | warn |
| P7 | **Flows under version control** - redeploying the flow runtime lost the production flow configuration | keep flows versioned and check the redeploy impact | warn |

Two further checks come from the same lessons and belong in the G-set once the OD lead agrees: **personal-data and worker-performance question answered** (does the screen process personal data or measure workers' performance; is the works council or data-protection notification needed - notification content: purpose, functions, data fields, access rules, retention, council category),
and **savings forecast and registered project present** (a use case implemented without forecast or registered savings project is invisible to the savings ledger; the forecast is checked before the sprint closes). Both `PROPOSAL`.

### 3. Decision rules

- **Go-live = all G1 to G7 passed, evidence cited.** "Yes" without evidence counts as not checked.
- **Requirements still moving?** A first delivery is not fully right. Plan the requirements-iteration loop after first delivery; it is not a reason to withhold go-live and not a reason to let scope grow silently.
- **Change of look is not a guardrail topic.** Requests about fonts, colours and headlines are capacity burners: route by cost-saving impact and time-box them.
- **Failed guardrail routes back:** data to `od-data-availability-check`; footprint to `od-system-fit-check`; handover to `od-handover-and-adoption`; security to `od-cybersec-gate`. Say which.
- **Human-dependent automation caps what a screen can show** (for example a machine that works one item at a time without fast-forward during breaks). Check for organizational loss before proposing technology.

### 4. Handoff contract

| Receives | From |
|---|---|
| match record, system match record, data verdict, security status | the use-case part, the system part, `od-data-availability-check` |
| deltas the plant recorded against the baseline | `od-analytics-asset-build` |

| Hands on | To |
|---|---|
| go-live check record with the final line "go-live decision: the plant's", utilization ritual, action owner, savings-forecast status | `od-handover-and-adoption`, `od-rollout-training` (1a3) |
| failed guardrail and its route | the skill named in section 3 |
| utilization expectation | `od-scorecard-reporting` (utilization is reported next to the count of deliveries) |

### 5. Pitfalls and lessons

- **Low trust is expensive to win back.** Where earlier integrations were not trusted, stabilize before putting more use cases on top.
- **Nobody trusts a number nobody can explain.** Unexplained differences to the paper record end adoption early.
- **Plant scepticism at the start is normal**; acceptance grew by raising awareness step by step and showing the first real use. Do not read early silence as agreement.
- **Missing training or enabling knowledge** at the plant makes a correct screen unusable.
- **Quality dashboards that do not depend on machine connectivity** (lab tests) run on another path owned by the local quality team; do not push them through the machine-integration checks.

### 6. Questions to ask and definition of done

Who opens it and when? What do they do when the number is red? Where does the number differ from the paper record and why? Who runs the tool when it breaks? Who switches the old way off? Is any personal data or worker-performance measure involved?

**Done:** record complete, every result has evidence, date and answerer; the P-candidates are answered or marked not applicable with a reason; the utilization expectation is written down.

### 7. AI agent operating notes

- **Can do:** draft the check record from the match records; run the evidence check ("Yes" without evidence becomes *not checked*); compare screen output with a paper-record extract the plant supplies and list the differences; check that no figure lacks a source and read date; list unanswered P-candidates.
- **Needs:** the two match records, the verdict of the data check, the plant owner's role, the paper-record extract.
- **Human gate:** the plant owner answers G1 to G7 and decides `PRODUCTIVE`; Cyber Security sign-off is human-only; the OD lead decides which candidate blocks.
- **Must cite:** evidence for each answer (verdict id, list row, dated statement), read dates.
- **Hands over:** the check record plus the list of failed guardrails and where each was routed.
