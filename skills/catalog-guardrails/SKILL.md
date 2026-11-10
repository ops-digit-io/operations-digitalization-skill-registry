---
name: catalog-guardrails
description: >-
  Enforce the boundaries of plant self-service (new-state Lane 1, the department's catalog-guardrails): run the go-live self-check on a catalogued use case the plant applied itself - data present and fresh, platform boundary, lean footprint, no invented figures, a named owner, handover, Cyber Security - plus the screen-level and IT technology guardrails (stack, CMO, approved interfaces, observability, growth boundaries). Use at steps 1a3 and 1b4, when a plant wants to go live, or when a new guardrail is proposed.
license: MIT
metadata:
  id: catalog-guardrails
  tier: practice
  lane: lane-1
  new_state_lane: "Lane 1a (1a3), Lane 1b (1b4)"
  new_state_step: "Guardrails, go live, confirm adoption"
  department_names: ["catalog-guardrails"]
  owner_role: Digital-Business-Value-Engineer (DBVE); the plant runs the check
  authority_level: draft the go-live check and report it; the plant decides PRODUCTIVE; a block-level failure stops go-live
  status: draft
  sources_read: 2026-11-10
  requires: [od-context]
  derived_from:
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/lane-1-run-known-uc.md (skills table, gap), read 2026-11-10"
    - "Split from catalog-usecase (formerly od-catalog), 2026-11-10"
  okf:
    type: Agent Skill
    title: Catalog guardrails
    tags: [department-core, lane-1]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Catalog guardrails

Read `od-context` first. The department's `catalog-guardrails`: the boundaries inside which a plant runs a catalogued use case itself, and the go-live self-check (steps 1a3 and 1b4). Self-service stays inside pre-approved guardrails; anything outside them is not self-service.

## Go-live guardrails (step 1a3, and 1b4)

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
| G7a | **No change to the data model or signal standard:** the plant uses the catalogued model as it is (Lane 1 "may not change data models") | Lane 1 lane file; `od-signal-standardization` | Stop. A changed model is not self-service: Lane 2 or Lane 3 via `od-signal-standardization`, decided through `od-decision-routing` |

The plant always answers G1 to G7 and G7a. **G8 to G19** (screen-level: signal binding, time handling, data sources, panels, identity,
states, free text, no write-back; failure-case guardrail G19) and **P1 to P7** (process level: reconciliation with the paper
process, utilization ritual, action owner, operations concept, switching off the old process, early IT changes, flows under
version control) are **candidates** from AI-drafted draft specifications (SPEC-02 to SPEC-04) and recorded failure cases; the OD
lead has not confirmed them. The plant answers them when it has built or copied the screen itself.

## Procedure - go-live check

1. Take the Part A match record and, on branch 1b, the system match record.
2. The **plant** answers G1 to G7 and G7a, each with evidence (a verdict, a source, a name). Do one deep dive against the paper process before declaring the screen live ([`references/process-chain-practice.md`](../catalog-usecase/references/process-chain-practice.md)) Part C).
3. Write the **go-live check record** ([`assets/go-live-check-record.md`](assets/go-live-check-record.md)): per guardrail the result (passed / failed / not checked), evidence, date, who answered; at the top the use case, plant, plant owner, and the final line "go-live decision: the plant's". Write the utilization expectation into the record before go-live.
4. Any failed guardrail - **no go-live**; route back as the table says (data to `od-data-availability-check`, footprint to `od-system-fit-check`, handover to `od-handover-and-adoption`, security to `od-cybersec-gate`; say which).
5. All passed - report it. **The plant decides to go live** (`PRODUCTIVE`); this skill never does.
6. After go-live, adoption is checked as `od-handover-and-adoption` describes.

---


## References

| File | Use it for |
|---|---|
| [`references/technical-guardrails.md`](references/technical-guardrails.md) | Candidate screen-level guardrails and the IT technology guardrails (stack, CMO, interfaces, observability, self-assessment, mission creep) |
| [`assets/go-live-check-record.md`](assets/go-live-check-record.md) | The record the plant fills at go-live |

## Do not

- Do not present the seeded guardrails as a finished, approved set.
- Do not let a failed guardrail pass as a warning when it is marked block.
