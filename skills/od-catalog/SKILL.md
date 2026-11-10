---
name: od-catalog
description: >-
  Run the plant self-service catalog end to end (new-state Lane 1) and its Lane 2 graduation.
  Step 1a1 / 1b1: match a plant's request to a catalogued, proven use case (CSP decision recorded,
  capability template, preconditions: machine connected, signals present) and, on branch 1b,
  to a standardized system or connection kit, or say no standard system fits so the demand moves
  to Lane 3. Step 1a3: run the go-live guardrails (data present, platform boundary, lean footprint,
  no invented figures, named plant owner, three-question handover test, Cyber Security cleared for
  an external connection); the plant decides to go live. Step 26: state what a Lane 2 result must
  show before it graduates into the catalog. Use when a plant asks for something another plant
  already has, wants a dashboard or report self-served, asks which system to order, wants to go
  live with an applied template, or when an entry or a guardrail is proposed. Draft scaffold: no
  catalog data set, kit list or finished guardrail set exists yet.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-catalog
  tier: practice
  lane: [lane-1, lane-2]
  new_state_lane: "Lane 1a (1a1, 1a3), Lane 1b (1b1, 1b4), Lane 2 (26)"
  new_state_step: "Pick from the catalog; Guardrails, go live, confirm adoption; Pick the use case and the standard system; Standardized deployment, go live, confirm adoption; Implement, evaluate impact, ensure adoption, catalogue"
  owner_role: human:jakob.gabriel
  authority_level: draft the go-live check; report the result; recommend only - the plant decides what it runs and decides PRODUCTIVE, the CSP decision stays with its owner, ordering and connecting stay with the integration owner and the approval route
  status: draft
  sources_read: 2026-11-10
  requires: [od-context]
  composes: [od-use-case-standardization, od-use-case-intake-triage, od-data-availability-check, od-system-fit-check, od-handover-and-adoption, od-equipment-integration, od-decision-routing, od-acceptance-test]
  derived_from:
    - The new-state flow (docs/new-state-flow.md and the four diagrams in docs/new-state/), the Lane 1 steps "Pick from catalog", "Pick UC + std system" and "Validate and go live", the Lane 2 graduation and the gap register entries, read 2026-11-05
    - ops-knowledge-graph/_knowledge/10-Department/Decision rights.md
    - Skill od-use-case-standardization, which holds the eleven capability templates, the reference library and the CSP gate
    - Work vault (Work-OpsDigit-Knowledge), Graph/Use Cases frontmatter (use_case_level, csp_decision, use_case_template, status, plant, scalable), read 2026-11-05
    - Work vault, Graph/Use Case Views, the overview, the standardization note and the eleven template pages (delivery, standard data, boundaries), read 2026-11-05
    - Work vault, Graph/Target Types and the library notes with a recorded CSP Yes, read 2026-11-05
    - registry.yaml open_gaps, the integration routes marked TODO and the plants without an integration concept; Grafana is a local instance per plant while Databricks and the Azure Storage Account are the global layer
    - ops-knowledge-graph/.../00-core/03-objectives.md
    - ops-knowledge-graph/.../00-core/08-decision-rights.md
    - ops-knowledge-graph/.../20-lanes/use-case-support-service/agent-brief.md
    - Skill od-equipment-integration, references/decision-paths.md, the routes by controller and protocol
    - Work vault, Graph/Machines, the machine notes aggregated by controller vendor, model, protocol, integration status and method, read 2026-11-05
    - Work vault, Graph/Tools, Graph/Connectors and Graph/Legacy Applications (aggregated), read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), _knowledge/OperationsDigitalization-Department/10-modules/smart-factory-use-case, the systems-of-record note
    - Skill od-handover-and-adoption, the three-question test and the rule that the plant decides PRODUCTIVE
    - Work vault, Dashboard Exports/specs, SPEC-00 to SPEC-04 and the Hannover Stoecken KKA and Pulp Mixer requirements, all AI-drafted drafts, read 2026-11-05
    - Work vault, Vault Gap Analysis - Working Items and Content Depth, _knowledge/20-Done and 10-Department (Decision rights, Handover, Use case standardization), read 2026-11-05
    - Work vault, Graph/Use Case Views and the Microservice Apps (WIP) notes Cross-Cutting Platform Concerns and Platform Extensibility and Onboarding, read 2026-11-05
    - Skills od-data-availability-check (failure modes), od-handover-and-adoption, od-decision-routing (escalation worked examples), read 2026-11-05
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/Transcripts/2026-09-11_OD-IT-alignment_meeting-notes.txt, read 2026-11-10"
  okf:
    type: Agent Skill
    title: od-catalog
    tags: [all, practice, new-state, draft, catalog]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Catalog: use cases, standard systems, go-live guardrails

Read `od-context` first.

Merged from: `od-catalog`.

**Status: draft scaffold.** The new-state flow needs three net-new builds that belong together: a plant-facing catalog of proven use cases, a standardized connection-kit list a plant can match a use case against and order, and a self-check to go live. No catalog data set, kit list (kits, prices, lead times) or finished guardrail set exists in the sources. This skill defines how a request is matched, what an entry must hold and what the plant checks before go-live; it states no entry, names no kit and presents no guardrail set as complete.

## Where the flow puts it

| Step | Lane / branch | What this skill does | Part |
|---|---|---|---|
| 1a1 | Lane 1, machine connected | "Pick from catalog": match the request to an entry, check preconditions | A |
| 1b1 | Lane 1, machine not connected | "Pick UC + std system": entry, then a standardized system or no fit | A, B |
| 1b2, 1b3 | Lane 1b | Cost template and lightweight approval (`od-decision-routing`), then order and connect (`od-equipment-integration`); this skill hands over | B |
| 1a3 (and 1b4) | Lane 1 | "Validate and go live": the plant's self-check | C |
| 26 | end of Lane 2 | A proven, repeatable result graduates into the catalog and becomes a future Lane 1 case | A |

If no catalogued entry fits: Lane 2 (OD-led). If no standard system fits: Lane 3 (3b, new connector).

## Shared rules (stated once)

- The **plant decides** what it runs, owns the use case and decides daily use and `PRODUCTIVE`. The **CSP decision** (is a solution standard enough to roll out across plants) stays with its owner (`od-decision-routing`). Ordering and connecting stay with the integration owner and the approval route. **Cyber Security sign-off for an external connection is human-only.**
- Footprint: keep the **lean, standardized system footprint** (measured as the number of systems in operation; the target is to be confirmed). Anything outside it goes through `od-system-fit-check`.
- No invented entries, counts, kits, prices, lead times, savings or impact figures. Mark what is to be collected; every status carries its source and read date. Counts and statuses are re-derived live, never copied.
- A "Yes" without evidence counts as "not checked".

---

# Part A - Pick a use case and graduate (steps 1a1, 1b1, 26)

What the catalog builds on, and how to count library entries by CSP decision live: [`references/sources-and-entry-fields.md`](references/sources-and-entry-fields.md), [`references/library-and-csp-state.md`](references/library-and-csp-state.md). Re-count before quoting; at most the entries with a recorded CSP `Yes` are standard enough to take as they are.

## What counts as "catalogued"

All must hold. Points 1 and 4 come from the sources; **2 and 3 are proposals** to confirm with the OD lead.

1. A **CSP decision `Yes`** is recorded for it.
2. It maps to one of the eleven **capability templates**.
3. Its **signals are standardized** (`od-signal-standardization`), so a second plant can consume them.
4. It has a **plant owner** and a handover record that passed the three-question test (`od-handover-and-adoption`).

A library entry without a recorded CSP `Yes` is not catalogued: route it to Lane 2.

## Procedure - pick

1. **Load `od-context`.** Run `od-use-case-intake-triage` if the request is not yet classified. Reduce the plant's sentence to object, event and time axis.
2. **Find the capability template**, then the matching reference-library entries (`od-use-case-standardization`). Check the template page and the entry, not the title ([`references/placement-traps-and-documentation.md`](references/placement-traps-and-documentation.md)).
3. **Check the CSP status** of each candidate. No recorded `Yes` - stop, fall through to Lane 2.
4. **Check preconditions** (`od-data-availability-check`): machine connected, signals present. Connected - branch **1a**. Not connected - branch **1b** (Part B).
5. **Footprint.** A need outside the lean footprint: `od-system-fit-check` first. A plant does not self-serve such a use case.
6. **Write the match record** ([`assets/catalog-match-record.md`](assets/catalog-match-record.md)) and hand over: 1a to `od-analytics-asset-build`; 1b to Part B; fall-through to Lane 2 or Lane 3. Name the plant's **utilization moment** (who opens it, in which meeting, which action follows) or mark it `<to confirm>`.

Match record fields: request, plant, plant owner; candidate entry (library id, capability template); CSP status (`Yes` / `No` / not decided, with source); preconditions with the data-availability verdict; branch (1a / 1b / Lane 2 / Lane 3); next skill.

## Graduation into the catalog (step 26)

Use `od-use-case-standardization` for template, cluster and CSP step and `od-handover-and-adoption` for the plant handover.
Propose the entry only when the four conditions hold. A validated prototype alone is a **candidate**, not an entry:
graduation means the prototype has become a configurable, packaged application. A *unique* (site-specific) use case does not
graduate. Record the plant's utilization moment in the entry; a deployed but unused use case is not a success.
Stages, archetypes and entry content: [`references/process-chain-practice.md`](references/process-chain-practice.md) Part A.

---

# Part B - Pick a standardized system (step 1b1, hand to 1b2 / 1b3)

Branch 1b only: after the match record, flow continues with cost template and approval (`od-decision-routing`), "Order and connect"
(`od-equipment-integration`), then "Apply template and go live" (Part C).

Sources and the route-candidate pattern (a route "written in full and proven in at least two plants"; none has a kit, price or lead time on record, so they are **route candidates**, not standard systems): [`references/sources-and-entry-fields.md`](references/sources-and-entry-fields.md).

**Entry fields** (machine class, route, kit, cost, lead time, Cyber Security status, validated at, is / is-not, recommended-if, cost class, operations concept, known blockers): [`references/sources-and-entry-fields.md`](references/sources-and-entry-fields.md); blank entry in `assets/standard-system-entry.md`.

A **standardized system** is, until the OD lead says otherwise, a route written down in full **and** a purchasable kit. A route
marked TODO or stub is not a standard system. Any route that is not class A in `validated-routes.md` gets no entry until the procedure is written (B) or a second route is proven (C).

## Procedure - system match

1. **Take the match record** from Part A. Branch 1b only.
2. **Collect the machine facts**: controller vendor and model, protocol, program version, where the data should land. Add the machine to the machine list first.
3. **Look up the route** in `decision-paths.md`. Written in full - candidate standard system. TODO, stub or absent - **no standard system**: say so, hand to `od-system-fit-check` and Lane 3 (3b).
4. **Test the tool boundary**: what the tool is, what it is not, the "recommended if" trigger ([`references/tool-boundaries-mda-mes-mil-msb-qfpr.md`](references/tool-boundaries-mda-mes-mil-msb-qfpr.md)). A recommendation names the defined use case behind it; without one it is not made.
5. **Heavy request disguised as a dashboard**: order or recipe execution, labels, batch genealogy, material validation are execution-system territory. Map the asked functions to the shop-floor function list before choosing; where performance analysis overlaps with MES, choose the lighter solution and name the overlap.
6. **Pick the route by data class** (feeds `od-equipment-integration`, `od-signal-standardization`): transactional (events, counters, alarms) - service bus (OPC UA); time series - MQTT stream; master data - ERP leads and pushes by API, local systems are derived. Edge device versus plain OPC UA client and where logic lives: [`references/process-chain-practice.md`](references/process-chain-practice.md) Part B.
7. **Footprint**, **cost and approval**: hand the cost-template inputs to `od-decision-routing`. **Order and connect** is `od-equipment-integration`; acceptance is `od-acceptance-test`.
8. **Write the system match record** ([`assets/standard-system-entry.md`](assets/standard-system-entry.md)): request and plant; machine class; route and status; candidate kit or "no standard system"; cost-template inputs given or ⟨missing⟩; Cyber Security status; next step (1b order and connect, or Lane 3).

Recommendation vocabulary: recommended / recommended if ⟨condition⟩ / not recommended / not available, each with date and source.
**Operations-concept gate:** a tool without a named operations owner, service and support level is not matched for rollout. Security-relevant (connects to central systems, holds operational or customer data, profound effect on manufacturing) means `od-cybersec-gate`.

---

# Part C - Go-live guardrails (step 1a3, and 1b4)

In the new state a plant applies a catalogued template itself, so the check OD used to do by hand has to be something the plant
can run. The nearest existing skill is `od-handover-and-adoption`, run by OD; Part C is the plant-run version of the part that can be.
The guardrails are **seeded from rules the registry and the knowledge bundle already record**. They are not a finished set.

## The guardrails

| # | Guardrail | Source | A failure means |
|---|---|---|---|
| G1 | The signals the template reads exist and are fresh | `od-data-availability-check` verdict | Stop. Back to the data check; Lane 2 or Lane 3 if the data cannot be had |
| G2 | **Platform boundary:** a plant's manufacturing dashboards run on that plant's local Grafana; the global layer (Databricks, Azure Storage Account) is not wired into it, and no cross-plant view is built on a local instance | `registry.yaml`, open gaps | Stop. Undo the wiring, or ask OD for a cross-plant view |
| G3 | The solution stays inside the lean footprint, no system outside it | `od-system-fit-check` | Stop. Escalate as an exception through `od-decision-routing` |
| G4 | **No invented figures:** no savings or impact number unless a source and a capture date are named | `od-context` honesty rules; lane agent brief | Remove the number, or mark it as to be collected |
| G5 | A **named plant owner** exists, and the plant, not OD, decides daily use | Knowledge bundle, `Decision rights` | Stop. Name the owner first |
| G6 | The **three-question handover test** is answerable by the receiving side from the handover record alone, and the record names **who uses the screen, in which meeting, and which action follows** | `od-handover-and-adoption`; deck practice | Not done. Close the gap before go-live |
| G7 | An **external connection** has a Cyber Security sign-off. Human-only | Knowledge bundle, decision rights | Hold at the wait state. Do not go live |

The plant always answers G1 to G7. **G8 to G19** (screen-level: signal binding, time handling, data sources, panels, identity,
states, free text, no write-back; failure-case guardrail G19) and **P1 to P7** (process level: reconciliation with the paper
process, utilization ritual, action owner, operations concept, switching off the old process, early IT changes, flows under
version control) are **candidates** from AI-drafted draft specifications (SPEC-02 to SPEC-04) and recorded failure cases; the OD
lead has not confirmed them. The plant answers them when it has built or copied the screen itself.

## Procedure - go-live check

1. Take the Part A match record and, on branch 1b, the system match record.
2. The **plant** answers G1 to G7, each with evidence (a verdict, a source, a name). Do one deep dive against the paper process before declaring the screen live ([`references/process-chain-practice.md`](references/process-chain-practice.md) Part C).
3. Write the **go-live check record** ([`assets/go-live-check-record.md`](assets/go-live-check-record.md)): per guardrail the result (passed / failed / not checked), evidence, date, who answered; at the top the use case, plant, plant owner, and the final line "go-live decision: the plant's". Write the utilization expectation into the record before go-live.
4. Any failed guardrail - **no go-live**; route back as the table says (data to `od-data-availability-check`, footprint to `od-system-fit-check`, handover to `od-handover-and-adoption`, security to `od-cybersec-gate`; say which).
5. All passed - report it. **The plant decides to go live** (`PRODUCTIVE`); this skill never does.
6. After go-live, adoption is checked as `od-handover-and-adoption` describes.

---

## Open points - what only the OD lead can supply

- ⟨Where the catalog lives and in what form (list, library, portal)⟩ and ⟨who maintains it⟩. Partial answer from the vault: the nearest thing today is the SharePoint list `UseCase-Library` (the CSP field lives there) read through the eleven template pages in `Graph/Use Case Views`; no plant-facing portal is recorded.
- ⟨Whether a recorded CSP `Yes` is the right threshold for self-service⟩, given how few entries may have one.
- ⟨Which entries with a `Yes` a plant can take as is today⟩: conditions 3 and 4 (standardized signals, plant owner and handover) are not recorded in the entries - IIAE and plant owner.
- ⟨How a plant reaches the catalog⟩ and ⟨who may add an entry⟩.
- ⟨The standardized-system list itself⟩: kits, prices, lead times, validated plants, and ⟨who maintains it⟩. Route evidence is in `references/validated-routes.md`; the kit side is open.
- ⟨Whether "standardized" means a validated route plus a purchasable kit⟩.
- ⟨The Cyber Security sign-off standard document⟩ - listed in the bundle as still to be collected.
- ⟨Further technical guardrails⟩: naming, refresh interval and unit rules are proposed in `references/technical-guardrails.md` (SPEC-03, draft); **access rights and performance** are not recorded (performance of the proposed single-read function on the real telemetry table is "not known and must be measured", SPEC-02 D-04).
- ⟨Which guardrails block go-live and which only warn⟩. A proposal exists in SPEC-03 section 6 (S-01 to S-03, S-06, S-07, S-10, S-15, S-17), applied in `references/technical-guardrails.md`. G1 to G7 are "block" until the OD lead says otherwise.
- ⟨The utilization target after go-live⟩ for a self-served use case: the field is recorded, not a target.
- ⟨Who OD names as the contact when a guardrail fails⟩: nearest recorded answer is by role (IIAE, DBVE, OD lead, Plant IT) in `references/failure-cases-and-routing.md`.

## Pitfalls

- Present a reference-library entry as catalogued without a recorded CSP `Yes`.
- Invent entries, counts, kits, prices, lead times, savings or impact figures. Do not accept an unsourced figure to pass G4.
- Treat a route marked TODO or stub as a standard system. Beckhoff on the edge platform is the standing example.
- Let a plant self-serve a use case, or propose a system, outside the lean footprint without `od-system-fit-check`.
- Take the CSP decision, approve a connection, sign off Cyber Security, or decide go-live for the plant.
- Let a plant go live with a failed or unchecked guardrail, or present G1 to G7 as complete.

## References

| File | Open when |
|---|---|
| [`references/sources-and-entry-fields.md`](references/sources-and-entry-fields.md) | What the catalog builds on, route-candidate pattern, standardized-system entry fields |
| [`references/library-and-csp-state.md`](references/library-and-csp-state.md) | Counting library and CSP decisions live, which of the four conditions the vault shows |
| [`references/template-coverage.md`](references/template-coverage.md) | The eleven templates: delivered vs wanted coverage, peer plants, data needed, boundaries, screen components |
| [`references/placement-traps-and-documentation.md`](references/placement-traps-and-documentation.md) | Placement traps, what "Other Use Cases" resolves into, documentation standard of a usable peer |
| [`references/validated-routes.md`](references/validated-routes.md) | Classifying a route A to D, counting evidence live |
| [`references/tools-and-footprint.md`](references/tools-and-footprint.md) | Integration concepts, shop-floor tools, rollout status, lean footprint for a kit |
| [`references/legacy-application-position.md`](references/legacy-application-position.md) | What the kit meets on the floor: licence, support, criticality, cyber position |
| [`references/tool-boundaries-mda-mes-mil-msb-qfpr.md`](references/tool-boundaries-mda-mes-mil-msb-qfpr.md) | Is / is-not / recommended-if for MDA/PDA, MES, MIL, MSB, QFPR |
| [`references/technical-guardrails.md`](references/technical-guardrails.md) | Candidates G8 to G18 with source, failure prevented, block-or-warn |
| [`references/failure-cases-and-routing.md`](references/failure-cases-and-routing.md) | Failure patterns mapped to guardrails, proposed G19, who to call, post-go-live utilization |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Part A graduation stages; Part B edge vs OPC UA client; Part C P1 to P7, handoff, agent notes |
| `assets/catalog-match-record.md`, `assets/standard-system-entry.md`, `assets/go-live-check-record.md` | Match record, system entry, go-live record |
