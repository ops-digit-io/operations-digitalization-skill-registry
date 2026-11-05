---
name: catalog-usecase
description: >-
  Match a plant's request to a use case that is already catalogued and proven, so the plant
  can run it itself (new-state Lane 1) - pick the entry, check its preconditions (machine
  connected, signals present), and name the branch: 1a connected, 1b needs a standardized
  system, or fall through to Lane 2 or Lane 3. Also states what a Lane 2 result must show
  before it graduates into the catalog. Use when a plant asks for something another plant
  already has, when a plant wants to self-serve a dashboard or report, or when a proven use
  case is proposed for the catalog. Draft scaffold: the self-service catalog does not exist
  yet as a data set.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
allowed-tools: Read Grep Glob
metadata:
  id: catalog-usecase
  tier: practice
  lane: all
  new_state_lane: Lane 1 (1a, 1b) and the Lane 2 graduation target
  new_state_step: Pick from catalog
  owner_role: human:jakob.gabriel
  authority_level: recommend - the plant decides what it runs; the CSP decision stays with its owner
  status: draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-use-case-standardization, od-use-case-intake-triage, od-data-availability-check, od-system-fit-check, od-handover-and-adoption]
  derived_from:
    - The new-state flow (docs/new-state-flow.md and the four diagrams in docs/new-state/), the Lane 1 step "Pick from catalog", the Lane 2 graduation and the gap register entry, read 2026-11-05
    - ops-knowledge-graph/_knowledge/10-Department/Decision rights.md
    - Skill od-use-case-standardization, which holds the eleven capability templates, the reference library and the CSP gate
    - Work vault (Work-OpsDigit-Knowledge), Graph/Use Cases frontmatter (use_case_level, csp_decision, use_case_template, status, plant, scalable), read 2026-11-05
    - Work vault, Graph/Use Case Views, the overview, the standardization note and the eleven template pages (delivery, standard data, boundaries), read 2026-11-05
    - Work vault, Graph/Target Types and the library notes with a recorded CSP Yes, read 2026-11-05
  okf:
    type: Agent Skill
    title: Use-case catalog
    tags: [all, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Use-case catalog

Read `od-context` first.

**Status: draft scaffold.** The new-state flow names this skill as a net-new build: a plant-facing
catalog of proven use cases that a plant can pick and run without OD labour. No such catalog exists as a
data set today. This skill defines how a request is matched against it and what an entry must hold.
It does not state that any particular entry exists.

## Where the flow puts it

- **Lane 1, first step** - "Pick from catalog" (1a, machine connected) and "Pick UC + std system" (1b, not connected).
- **Lane 2, last step** - a proven, repeatable result graduates into the catalog and becomes a future Lane 1 case.

## What exists today to build on

| Source | What it gives |
|---|---|
| `od-use-case-standardization` | The eleven cross-plant capability templates, the reference library, the cluster tags and the CSP gate - run by OD, not by plants |
| Knowledge bundle, `Decision rights` | Whether a solution is standard enough to roll out across plants is the **CSP** decision, recorded per reference-library entry. The bundle states how many entries have been decided so far, split into `Yes` and `No` (check its date and re-count in the vault) |
| Same | A use case has a plant owner, and the plant decides whether it goes into daily use |

So today, at most the entries with a recorded CSP `Yes` are standard enough for another plant to take as they are.

To see the current state, count the library entries in `Graph/Use Cases` by `csp_decision` (`Yes`, `No`, no recorded
decision) and name the entries with a `Yes`; how to do this and what to watch for is in
[`references/library-and-csp-state.md`](references/library-and-csp-state.md). Re-count before quoting.

## The references

| File | Use it for |
|---|---|
| [`references/library-and-csp-state.md`](references/library-and-csp-state.md) | How to count the library and the CSP decisions live, how to find the entries with a recorded CSP `Yes`, which of the four "catalogued" conditions the vault shows for them |
| [`references/template-coverage.md`](references/template-coverage.md) | The eleven templates: how to read delivered versus wanted coverage and find peer plants live, data each template needs, boundary table, typical screen components |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | How the pick and the graduation are run in practice: archetypes (cross-process, per-process, unique), prototype to configurable container app, triage buckets, entry content, handoff contract, agent notes |
| [`references/placement-traps-and-documentation.md`](references/placement-traps-and-documentation.md) | Placement traps (same title, mis-templated, boundary pairs), what "Other Use Cases" resolves into, the documentation standard that makes a peer a usable match, choosing the reference solution |
| [`assets/catalog-match-record.md`](assets/catalog-match-record.md) | The match record to fill per request, with an illustrative worked example |

## What counts as "catalogued"

An entry is catalogued only if all of these hold. Points 1 and 4 come from the sources; **2 and 3 are
proposals** to confirm with the OD lead.

1. A **CSP decision `Yes`** is recorded for it.
2. It maps to one of the eleven **capability templates**.
3. Its **signals are standardized** (`od-signal-standardization`), so a second plant can consume them.
4. It has a **plant owner** and a handover record that passed the three-question test (`od-handover-and-adoption`).

A library entry without a recorded CSP `Yes` is not catalogued. Route it to Lane 2 (OD-led).

## Procedure

1. **Load `od-context`.** Run `od-use-case-intake-triage` if the request is not yet classified.
2. **Find the capability template** the request belongs to, then the matching reference-library entries (`od-use-case-standardization`).
3. **Check the CSP status** of each candidate. No recorded `Yes` - stop, fall through to Lane 2.
4. **Check preconditions** for the plant: is the machine connected, are the signals there (`od-data-availability-check`)?
   Connected - branch **1a**. Not connected - branch **1b** (`catalog-systems` for the standard system).
5. **Footprint.** If the use case needs a system outside the lean footprint, run `od-system-fit-check` before going on.
6. **Write the match record** and hand over: 1a to `od-analytics-asset-build`; 1b to `catalog-systems`; fall-through to Lane 2 or Lane 3.

## Output - the catalog match record

| Field | Content |
|---|---|
| Request, plant, plant owner | as stated |
| Candidate entry | reference-library id and capability template |
| CSP status | `Yes` / `No` / not decided, with the source |
| Preconditions | machine connected, signals present, with the data-availability verdict |
| Branch | 1a / 1b / falls through to Lane 2 / falls through to Lane 3 |
| Next skill | one of the above |

## Graduation into the catalog (end of Lane 2)

Use `od-use-case-standardization` for the template, cluster and CSP step and `od-handover-and-adoption`
for the plant handover. Propose the entry only when the four conditions above hold. A validated prototype alone is a
candidate, not an entry: graduation means the prototype has become a configurable, packaged application, and a
*unique* (site-specific) use case does not graduate (`references/process-chain-practice.md`). Record the plant's
utilization moment in the entry - a catalogued use case that is deployed but not used is not a success.

## Open - what only the OD lead can supply

- ⟨Where the catalog lives and in what form (list, library, portal)⟩ and ⟨who maintains it⟩.
  Partial answer from the vault: the nearest thing to a catalog today is the SharePoint list `UseCase-Library` (the CSP field lives there) read through
  the eleven template pages in `Graph/Use Case Views`; no plant-facing portal is recorded. The marker stays for the intended form and the maintainer.
- ⟨Whether a recorded CSP `Yes` is the right threshold for self-service⟩, given how few entries may have one.
- The entries with a `Yes` are found live (see `references/library-and-csp-state.md`).
  ⟨Which of them a plant can take as it is today⟩ stays open: conditions 3 and 4 above (standardized signals, plant owner and handover) are not recorded in the entries - IIAE and plant owner.
- ⟨How a plant reaches the catalog⟩ and ⟨who may add an entry⟩.

## Do not

- Present a reference-library entry as catalogued without a recorded CSP `Yes`.
- Invent entries, entry counts, savings or impact figures. Mark what is to be collected.
- Let a plant self-serve a use case that needs a system outside the lean footprint.
- Take the CSP decision. It stays with its owner (`od-decision-routing`).
