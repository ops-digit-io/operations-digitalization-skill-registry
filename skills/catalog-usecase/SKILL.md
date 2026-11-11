---
name: catalog-usecase
description: >-
  Match a plant request to a proven catalogued use case (Lane 1), or say it is not catalogued and route it to Lane 2/3; set what a Lane 2 result needs to graduate. Not for systems (catalog-systems).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: catalog-usecase
  tier: practice
  lane: [lane-1, lane-2]
  new_state_lane: "Lane 1a (1a1, 1a3), Lane 1b (1b1, 1b4), Lane 2 (26)"
  new_state_step: "Pick from the catalog; Guardrails, go live, confirm adoption; Pick the use case and the standard system; Standardized deployment, go live, confirm adoption; Implement, evaluate impact, ensure adoption, catalogue"
  department_names: ["catalog-usecase", "use-case-catalog"]
  formerly: od-catalog
  owner_role: human:jakob.gabriel
  tags: [all, practice, new-state, draft, catalog]
  authority_level: draft the go-live check; report the result; recommend only - the plant decides what it runs and decides PRODUCTIVE, the CSP decision stays with its owner, ordering and connecting stay with the integration owner and the approval route
  status: draft
  requires: [od-context]
  composes: [catalog-systems, catalog-guardrails, od-use-case-standardization, od-use-case-intake-triage, od-data-availability-check, od-system-fit-check, od-handover-and-adoption, od-equipment-integration, od-decision-routing, od-acceptance-test]
  okf:
    type: Agent Skill
    title: catalog-usecase
    tags: [all, practice, new-state, draft, catalog]
---

# Catalog: use cases, standard systems, go-live guardrails

Read `od-context` first.

Merged from: `catalog-usecase`.

## Purpose

Matches a plant's request to a catalogued use case, or says plainly that it is not catalogued so the demand falls to Lane 2 or Lane 3, and records what a proven Lane 2 result must show to graduate into the catalog. Use it when a plant asks for a use case another plant already has, when a result should graduate, or when an entry is proposed.

## Inputs and output

- **Inputs**: the plant's request (reduced to object, event and time axis), the reference-library entries and their CSP status, the capability templates, and the data-availability result (machine connected, signals present).
- **Output**: the match record [`assets/catalog-match-record.md`](assets/catalog-match-record.md) with the branch (1a, 1b, Lane 2 or Lane 3) and the next skill, or a graduation proposal when the four conditions hold.

Fictional example (invented entry, not a catalog record):

```text
Request : "show scrap per shift on line X" (fictional)
Match   : candidate = library entry E-0 (fictional), capability template = quality
          CSP status = not decided -> not catalogued -> fall through to Lane 2
```

If it fails: a candidate without a recorded CSP `Yes`, or a precondition that fails validation, is not catalogued; route it to Lane 2 rather than matching it.

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

# Part B - Standardized systems and Part C - Go-live guardrails

Split into their own department skills (2026-11-10): **`catalog-systems`** (pick a standardized system, step 1b1, hand to 1b2 and 1b3) and **`catalog-guardrails`** (the go-live self-check, steps 1a3 and 1b4). This skill keeps the catalog of use cases and the graduation into it.

## Human gate and AI-agent notes

- **An agent may**: reduce the request, find the template and library entries, check CSP status and preconditions, and draft the match record or a graduation proposal.
- **Stays with roles**: the plant decides what it runs and when it is `PRODUCTIVE`; the CSP decision stays with its owner; the OD lead confirms the open points below; Cyber Security sign-off for an external connection is human-only.

## Done when

The match record names the branch and the next skill, with the CSP status and its source and read date; or a fall-through to Lane 2 or Lane 3 is stated plainly. A graduation proposal is done when all four conditions hold and the plant's utilization moment is recorded.

## Open points - what only the OD lead can supply

- ⟨Where the catalog lives and in what form (list, library, portal)⟩ and ⟨who maintains it⟩. Partial answer from the knowledge base: the nearest thing today is the SharePoint list `UseCase-Library` (the CSP field lives there) read through the eleven template pages in `Graph/Use Case Views`; no plant-facing portal is recorded.
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
| [`references/library-and-csp-state.md`](references/library-and-csp-state.md) | Counting library and CSP decisions live, which of the four conditions the knowledge base shows |
| [`references/template-coverage.md`](references/template-coverage.md) | The eleven templates: delivered vs wanted coverage, peer plants, data needed, boundaries, screen components |
| [`references/placement-traps-and-documentation.md`](references/placement-traps-and-documentation.md) | Placement traps, what "Other Use Cases" resolves into, documentation standard of a usable peer |
| [`references/validated-routes.md`](../catalog-systems/references/validated-routes.md)) | Classifying a route A to D, counting evidence live |
| [`references/tools-and-footprint.md`](../catalog-systems/references/tools-and-footprint.md)) | Integration concepts, shop-floor tools, rollout status, lean footprint for a kit |
| [`references/legacy-application-position.md`](references/legacy-application-position.md) | What the kit meets on the floor: licence, support, criticality, cyber position |
| [`references/tool-boundaries-mda-mes-mil-msb-qfpr.md`](../catalog-systems/references/tool-boundaries-mda-mes-mil-msb-qfpr.md)) | Is / is-not / recommended-if for MDA/PDA, MES, MIL, MSB, QFPR |
| [`references/technical-guardrails.md`](../catalog-guardrails/references/technical-guardrails.md)) | Candidates G8 to G18 with source, failure prevented, block-or-warn |
| [`references/failure-cases-and-routing.md`](references/failure-cases-and-routing.md) | Failure patterns mapped to guardrails, proposed G19, who to call, post-go-live utilization |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Part A graduation stages; Part B edge vs OPC UA client; Part C P1 to P7, handoff, agent notes |
| `assets/catalog-match-record.md`, `assets/standard-system-entry.md`, `assets/go-live-check-record.md` | Match record, system entry, go-live record |
