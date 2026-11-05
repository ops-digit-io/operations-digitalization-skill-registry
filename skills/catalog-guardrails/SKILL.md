---
name: catalog-guardrails
description: >-
  Run the self-check a plant completes before it declares a catalogued use case live
  without OD labour (new-state Lane 1, "Validate and go live"): data present, platform
  boundary respected, system footprint kept, no invented figures, a named plant owner, the
  three-question handover test passed, Cyber Security cleared where a connection is external.
  Drafts the go-live check and reports the result; the plant decides to go live. Use when a
  plant has applied a catalogued template and wants to go live, when someone asks whether a
  self-served use case is safe to adopt, or when a guardrail is proposed. Draft scaffold:
  the guardrail set is seeded from rules already recorded and needs the OD lead's review.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
allowed-tools: Read Grep Glob
metadata:
  id: catalog-guardrails
  tier: practice
  lane: all
  new_state_lane: Lane 1 (1a, 1b)
  new_state_step: Validate and go live
  owner_role: human:jakob.gabriel
  authority_level: draft the go-live check; report the result; the plant decides PRODUCTIVE
  status: draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [catalog-usecase, od-data-availability-check, od-system-fit-check, od-handover-and-adoption, od-acceptance-test]
  derived_from:
    - The new-state flow (docs/new-state-flow.md and the four diagrams in docs/new-state/), the Lane 1 step "Validate and go live" and the gap register entry, read 2026-11-05
    - Skill od-handover-and-adoption, the three-question test and the rule that the plant decides PRODUCTIVE
    - registry.yaml open_gaps, Grafana is a local instance per plant while Databricks and the Azure Storage Account are the global layer
    - ops-knowledge-graph/_knowledge/10-Department/Decision rights.md
    - ops-knowledge-graph/.../20-lanes/use-case-support-service/agent-brief.md
    - Work vault (Work-OpsDigit-Knowledge), Dashboard Exports/specs, SPEC-00 to SPEC-04 and the Hannover Stoecken KKA and Pulp Mixer requirements, all AI-drafted drafts, read 2026-11-05
    - Work vault, Vault Gap Analysis - Working Items and Content Depth, _knowledge/20-Done and 10-Department (Decision rights, Handover, Use case standardization), read 2026-11-05
    - Work vault, Graph/Use Case Views and the Microservice Apps (WIP) notes Cross-Cutting Platform Concerns and Platform Extensibility and Onboarding, read 2026-11-05
    - Skills od-data-availability-check (failure modes), od-handover-and-adoption, od-decision-routing (escalation worked examples), read 2026-11-05
  okf:
    type: Agent Skill
    title: Go-live guardrails
    tags: [all, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Go-live guardrails

Read `od-context` first.

**Status: draft scaffold.** In the new state a plant applies a catalogued template itself, so the check that
OD used to do by hand has to be something the plant can run. The flow lists "a self-check to go live without
OD labour" as a net-new build. The guardrails below are **seeded from rules the registry and the knowledge
bundle already record**. They are not a finished set.

The nearest existing skill is `od-handover-and-adoption`, which is run by OD. This skill is the plant-run
version of the part that can be.

## The guardrails

| # | Guardrail | Source | A failure means |
|---|---|---|---|
| G1 | The signals the template reads exist and are fresh | `od-data-availability-check` verdict | Stop. Back to the data check; Lane 2 or Lane 3 if the data cannot be had |
| G2 | **Platform boundary:** a plant's manufacturing dashboards run on that plant's local Grafana; the global layer (Databricks, Azure Storage Account) is not wired into it, and no cross-plant view is built on a local instance | `registry.yaml`, open gaps | Stop. Undo the wiring, or ask OD for a cross-plant view |
| G3 | The solution stays inside the lean footprint, no system outside it | `od-system-fit-check` | Stop. Escalate as an exception through `od-decision-routing` |
| G4 | **No invented figures:** no savings or impact number appears unless a source and a capture date are named | `od-context` honesty rules; lane agent brief | Remove the number, or mark it as to be collected |
| G5 | A **named plant owner** exists, and the plant, not OD, decides daily use | Knowledge bundle, `Decision rights` | Stop. Name the owner first |
| G6 | The **three-question handover test** is answerable by the receiving side from the handover record alone | `od-handover-and-adoption` | Not done. Close the gap before go-live |
| G7 | An **external connection** has a Cyber Security sign-off. This is human-only | Knowledge bundle, decision rights | Hold at the wait state. Do not go live |

## The references

| File | Use it for |
|---|---|
| [`references/technical-guardrails.md`](references/technical-guardrails.md) | Candidate guardrails G8 to G18 for the screen itself (signal binding, time handling, data sources, panels, identity, states, free text, no write-back), each with its source rule and the failure pattern it prevents, and a proposed block-or-warn setting |
| [`references/failure-cases-and-routing.md`](references/failure-cases-and-routing.md) | The failure patterns the vault has recorded, each mapped to the guardrail that would have caught it; proposed G19; who to call when a guardrail fails; the utilization expectation after go-live |
| [`assets/go-live-check-record.md`](assets/go-live-check-record.md) | The record to fill: G1 to G19, a content check against the template, the post-go-live fields, the result line |

Status of the extra guardrails: they come from AI-drafted draft specifications (SPEC-02 to SPEC-04) and from recorded failure cases. They are **candidates** that the OD lead has not confirmed. The plant answers G1 to G7 always; G8 to G19 are answered when the plant has built or copied the screen itself.

## Procedure

1. Take the `catalog-usecase` match record and, on branch 1b, the `catalog-systems` record.
2. The **plant** answers G1 to G7, each with its evidence (a verdict, a source, a name). "Yes" without evidence counts as "not checked".
3. Write the **go-live check record**. Any failed guardrail - **no go-live**, route as the table says.
4. All passed - report it. **The plant decides to go live** (`PRODUCTIVE`); this skill never does.
5. After go-live, adoption is checked the way `od-handover-and-adoption` describes.

## Output - the go-live check record

Per guardrail: result (passed / failed / not checked), the evidence, the date, who answered. At the top: the use case,
the plant, the plant owner, and the final line "go-live decision: the plant's".

## Open - what only the OD lead can supply

- ⟨Further technical guardrails⟩ a plant needs: naming, refresh interval, access rights, performance. Naming, refresh interval and unit rules are now proposed in `references/technical-guardrails.md` (source: SPEC-03, draft); **access rights and performance** are still not recorded in the sources read (the performance of the proposed single-read function on the real telemetry table is "not known and must be measured", SPEC-02 D-04).
- ⟨Which guardrails block go-live and which only warn⟩. A proposal exists: SPEC-03 section 6 lists the rules every new dashboard must pass (S-01 to S-03, S-06, S-07, S-10, S-15, S-17); the table in `references/technical-guardrails.md` applies it. G1 to G7 are "block" here until the OD lead says otherwise.
- ⟨The utilization target after go-live⟩ for a self-served use case. What is recorded is the field, not a target: the expectation is written into the record before go-live (`references/failure-cases-and-routing.md`).
- ⟨Who OD names as the contact when a guardrail fails⟩. The nearest recorded answer is by role (IIAE, DBVE, OD lead, Plant IT), in `references/failure-cases-and-routing.md`.

## Do not

- Let a plant go live with a failed or unchecked guardrail.
- Accept an unsourced savings or impact figure to pass G4.
- Decide for the plant, or sign off Cyber Security for it.
- Present these seven guardrails as complete.
