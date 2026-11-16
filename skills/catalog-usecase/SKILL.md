---
name: catalog-usecase
description: >-
  Match a plant request to a proven catalogued use case (Lane 1): reduce the request, find the capability template and library entry, check the CSP status and data preconditions, and write the match record with the branch and next skill. If it is not catalogued, say so and route it to Lane 2 or Lane 3. Also sets what a proven Lane 2 result needs to graduate into the catalog. Use when a plant asks "does another plant already have this", wants a dashboard or screen that may exist, when an entry is proposed for the catalog, or when a Lane 2 result should become repeatable. Recommends only; the plant decides what it runs and the CSP decision stays with its owner. Not for standard systems or kits (catalog-systems), the go-live check (catalog-guardrails) or rollout standardization (catalog-standardization).
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
  tags: [all, practice, new-state, ready, catalog]
  authority_level: draft the go-live check; report the result; recommend only - the plant decides what it runs and decides PRODUCTIVE, the CSP decision stays with its owner, ordering and connecting stay with the integration owner and the approval route
  status: ready
  requires: [dept-context]
  composes: [catalog-systems, catalog-guardrails, catalog-standardization, dept-intake, mi-data-availability, invest-screen, deploy-handover, mi-equipment, dept-decision-rights, deploy-acceptance]
  okf:
    type: Agent Skill
    title: catalog-usecase
    tags: [all, practice, new-state, ready, catalog]
---

# Catalog: match a request to a use case, and graduate

## Purpose

- Match a plant's request to a catalogued use case, or say plainly that it is not catalogued so the demand falls to Lane 2 or Lane 3.
- Record what a proven Lane 2 result must show to graduate into the catalog.
- Use it when a plant asks for something another plant already has, when a Lane 2 result should graduate, or when an entry is proposed.
- Systems are `catalog-systems`; the go-live self-check is `catalog-guardrails`.
- Read `dept-context` first.

## Terms used here

- **Catalog**: the plant-facing set of proven use cases; **catalogued** means all four conditions below hold.
- **Library entry**: a reference-library solution; it carries the CSP decision. A plant use case or dashboard family does not.
- **Capability template**: one of the eleven cross-plant templates.
- **Candidate**: a library entry or validated prototype that does not yet meet all four conditions.

## Inputs and output

- **Inputs**: the plant's request (reduced to object, event and time axis), the library entries and their CSP status, the capability templates, and the data-availability result (machine connected, signals present).
- **Output**: the match record [`assets/catalog-match-record.md`](assets/catalog-match-record.md) with the branch (1a, 1b, Lane 2 or Lane 3) and the next skill, or a graduation proposal when the four conditions hold.
- Output contract: [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Where the flow puts it

| Step | Lane / branch | What this skill does |
|---|---|---|
| 1a1 | Lane 1, machine connected | "Pick from catalog": match the request to an entry, check preconditions |
| 1b1 | Lane 1, machine not connected | "Pick UC + std system": match the entry, then hand to `catalog-systems` |
| 26 | end of Lane 2 | A proven, repeatable result graduates into the catalog and becomes a future Lane 1 case |

## Shared rules

- The **plant decides** what it runs, owns the use case and decides daily use and `PRODUCTIVE`.
- The **CSP decision** (is a solution standard enough to roll out across plants) stays with its owner (`dept-decision-rights`).
- Ordering and connecting stay with the integration owner and the approval route. **Cyber Security sign-off for an external connection is human-only.**
- Footprint: keep the **lean, standardized system footprint**; anything outside it goes through `invest-screen` first.
- No invented entries, counts, kits, prices, lead times, savings or impact figures. Mark what is to be collected.
- Every status carries its source and read date; counts are re-derived live, never copied, because the library changes.
- A "Yes" without evidence counts as "not checked", because a copied Yes may be stale or belong to another entry.

## What counts as "catalogued"

- All four must hold. Conditions 1 and 4 come from the sources; **2 and 3 are proposals** to confirm with the OD lead.

1. A **CSP decision `Yes`** is recorded for it (read from the library entry; `references/library-and-csp-state.md`).
2. It maps to one of the eleven **capability templates** (`references/template-coverage.md`).
3. Its **signals are standardized** (`mi-signals`), so a second plant can consume them.
4. It has a **plant owner** and a handover record that passed the three-question test (`deploy-handover`).

- A library entry without a recorded CSP `Yes` is not catalogued: route it to Lane 2.

## Procedure - pick

1. **Load `dept-context`.** Run `dept-intake` if the request is not yet classified. Reduce the plant's sentence to object, event and time axis.
2. **Find the capability template**, then the matching library entries (`catalog-standardization`). Check the template page and the entry, not the title, because the same title sits in different templates (`references/placement-traps-and-documentation.md`).
3. **Check the CSP status** of each candidate. No recorded `Yes`: stop, fall through to Lane 2.
4. **Check preconditions** (`mi-data-availability`): machine connected, signals present. Connected: branch **1a**. Not connected: branch **1b** (`catalog-systems`).
5. **Footprint.** A need outside the lean footprint: `invest-screen` first. A plant does not self-serve such a use case.
6. **Write the match record** and hand over: 1a to `ops-analytics-asset`; 1b to `catalog-systems`; fall-through to Lane 2 or Lane 3.
   - Name the plant's **utilization moment** (who opens it, in which meeting, which action follows) or mark it `<to confirm>`.

- Match record fields: request, plant, plant owner; candidate entry (library id, capability template); CSP status (`Yes` / `No` / not decided, with source); preconditions with the data-availability verdict; branch; next skill.

### Check before handoff

- [ ] CSP status is stated with its source and read date.
- [ ] Each of the four conditions is marked met, not met or not checked.
- [ ] The branch and the next skill are named.
- [ ] The utilization moment is named or marked `<to confirm>`.

## Procedure - graduate (step 26)

1. Run `catalog-standardization` for template, cluster and the CSP step; `deploy-handover` for the plant handover.
2. Propose the entry only when the four conditions hold.
3. Treat a validated prototype alone as a **candidate**, not an entry: graduation means it has become a configurable, packaged application.
4. Do not graduate a *unique* (site-specific) use case.
5. Record the plant's utilization moment in the entry, because a deployed but unused use case is not a success.
6. Stages, archetypes and entry content: `references/process-chain-practice.md`, Part A.

## Examples

```text
Request : "hour-by-hour output board for one assembly line" (fictional)
Match   : capability template = Andon Board; candidate = library entry E-1 (fictional)
          CSP Yes (library note, with read date); conditions 2 met, 3 not checked, 4 met
          machine connected, signals present -> branch 1a -> ops-analytics-asset
```

```text
Request : "show scrap per shift on line X" (fictional)
Match   : candidate = library entry E-0 (fictional), capability template = quality
          CSP status = not decided -> not catalogued -> fall through to Lane 2
```

```text
Graduation (Lane 2 result, fictional): stop-reason tablet app proven at plant Alpha.
Conditions: CSP not yet recorded -> proposal prepared for the CSP decision, not an entry.
Next: catalog-standardization (CSP readiness), deploy-handover (owner and handover record).
```

## Human gate and AI-agent notes

- **An agent may**: reduce the request, find the template and library entries, check CSP status and preconditions, and draft the match record or a graduation proposal.
- **Stays with roles**: the plant decides what it runs and when it is `PRODUCTIVE`; the CSP decision stays with its owner; Cyber Security sign-off for an external connection is human-only.

## Pitfalls

- Presenting a library entry as catalogued without a recorded CSP `Yes`: the plant then self-serves something not standard enough to roll out.
- Inventing entries, counts, kits, prices, lead times, savings or impact figures, or accepting an unsourced figure.
- Reading a blank integration status as "not integrated": many machines carry no status; ask the integration owner (`mi-data-availability`).
- Matching on the title: the same title sits in different templates, so the match must be on the template page and the entry.
- Letting a plant self-serve a use case outside the lean footprint without `invest-screen`.
- Taking the CSP decision, approving a connection, signing off Cyber Security, or deciding go-live for the plant.

## Definition of done

- The match record names the branch and the next skill, with the CSP status and its source and read date; or a fall-through to Lane 2 or Lane 3 is stated plainly.
- A graduation proposal is done when all four conditions hold and the plant's utilization moment is recorded.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`assets/catalog-match-record.md`](assets/catalog-match-record.md) | Step 6: the blank match record and its worked example |
| [`references/library-and-csp-state.md`](references/library-and-csp-state.md) | Step 3: counting library entries and CSP decisions live, before you tell a plant something is catalogued |
| [`references/template-coverage.md`](references/template-coverage.md) | Step 2: the eleven templates, peer plants, data needed, boundary rules |
| [`references/placement-traps-and-documentation.md`](references/placement-traps-and-documentation.md) | Step 2: placement traps, what "Other Use Cases" resolves into, documentation standard of a usable peer |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Graduation: Part A stages and archetypes (Parts B and C serve `catalog-systems` and `catalog-guardrails`) |
| [`references/sources-and-entry-fields.md`](references/sources-and-entry-fields.md) | What the catalog builds on and the entry fields; shared with `catalog-systems` |
| [`references/legacy-application-position.md`](references/legacy-application-position.md) | A kit must coexist with an installed application (shared with `catalog-systems`) |
| [`references/failure-cases-and-routing.md`](references/failure-cases-and-routing.md) | A guardrail fails or a post-go-live utilization question comes up (shared with `catalog-guardrails`) |
| [`references/background.md`](references/background.md) | Context, rationale, split history and open questions; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
