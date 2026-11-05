---
type: Skill Reference
title: Failure cases and routing
description: The failures the vault has actually recorded, each mapped to the guardrail it would have caught, plus the role to call and the lane to route to when a guardrail fails. Open it to justify a guardrail or to decide what a failed check means.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Failure cases and routing

A guardrail earns its place only if a failure has been recorded that it would have caught. The list below is what the sources read on 2026-11-05 actually hold. Guardrails G1 to G7 are in `SKILL.md`; G8 to G18 are the candidates in [technical-guardrails.md](technical-guardrails.md).

## Recorded failure cases

| Recorded case | Source | Caught by |
|---|---|---|
| An empty panel looks the same whether the machine is not connected, the point is not standardized, or the data is not fit for use; the worst of the three is the one that renders a number and is wrong (a shift-level figure read as hourly, a gauge that stops updating, a counter that resets on restart) | `od-data-availability-check`, `references/failure-modes.md` | G1 (name the step it dies at), G15 |
| A blank status is read as "not integrated": 451 of 1,715 machines carry no status (821 integrated, 395 not, 48 ongoing) | `od-data-availability-check` | G1 |
| A connector that exists is not a connector one may use: 19 of the 26 are `Productive` and `USE`, 6 are not available, 1 is `DO NOT USE` | `od-data-availability-check` | G1, G3 |
| An aggregation server with no edge platform behind it delivers nothing onward | `od-equipment-integration`, `decision-paths.md` | G1, G3 |
| No PLC program, no connection ("we can not connect the PLC"); asking the machine supplier has a lead time of weeks | same | G1 |
| A plant wave stalled on access to the platform: 0 of 10 machines at one plant while the access issue to the aggregation server was open (CoP call, 2024) | `od-decision-routing`, `references/escalation-worked-examples.md` | G1 (platform access is a precondition), G7 |
| Cyber Security / OT sign-off: "the machine waits. There is no expedited path" | `od-equipment-integration`, Gate 3 | G7 |
| Built is not handed over, and handed over is not in use: 272 use cases record handover `DONE`, 38 `ONGOING`; 129 `IMPLEMENTED` against 167 `PRODUCTIVE`; 8 of the use cases that record a utilization rate are `NEVER` | `od-handover-and-adoption` | G5, G6 |
| Savings booked but not real: the spend gate (eCR) is the most common recorded reason; 19 of 553 saving rows are proven through the review | `od-decision-routing` | G4 |
| A good state shown red, "no data" shown as 0, a dashboard saved with a fixed absolute time range, refresh off, trend lines ending 10 to 40 minutes before now | Hannover requirements (reverse-engineered review, `Dashboard Exports/specs`) | G14, G15, G16 |
| Same name, different content: the Andon Board exists in 6 plants with 6 distinct query sets; Operations Dashboard in 9 plants with 8 | SPEC-04 | the match in `catalog-usecase`, G13 |
| A dashboard copied from another plant breaks because signals are literal UUIDs in the SQL (6,590 distinct UUIDs; 2,375 appear in two or more dashboards, 67 in two or more plants) | SPEC-02 | G8, G11 |
| 450 empty UUID bindings in 49 dashboards return no data silently | SPEC-02 | G9 |
| 670 queries in 67 dashboards ignore the time picker | SPEC-02 | G10 |
| A use case note carries an individual's name because a raw free-text export was not filtered; the vault records it as known and not yet fixed | WIP spec "Cross-Cutting Platform Concerns" | G17 |
| A browser profile with login cookies was once committed beside the dashboard screenshot script; the session it captured "should be treated as exposed" | `_knowledge/20-Done`, "Grafana dashboard screenshot automation" | proposed G19 below |
| Staleness mistaken for non-use: usage is not recorded in the exports, so a dashboard unsaved for 180 days (456 of them) cannot be called stale | SPEC-00 | do not use "not opened" as evidence in a check |

**Proposed G19: no credentials, sessions or tokens are stored beside a script or a dashboard export that a plant keeps in a shared place.** Source: the case above; not a recorded rule. Block.

## When a guardrail fails - who to call and where to route

Roles come from `08-decision-rights.md` (DBVE, IIAE, OD lead, Plant ME, Plant IT) and the lane map; the vault records no named duty contact for this check.

| Failed guardrail | Route | Role to call |
|---|---|---|
| G1 not integrated (step 2) | Lane 1b if a standard system fits (`catalog-systems`), else Lane 3b | IIAE |
| G1 not standardized (step 4) | `od-signal-standardization` | IIAE |
| G1 not fit for use (step 5) | analytical lane with the data platform | DBVE with the platform contact |
| G2 platform boundary | undo the wiring; cross-plant views are built by OD | DBVE |
| G3 footprint | exception through `od-decision-routing`; tool rollout is an OD lead decision | OD lead |
| G4 unsourced figure | remove it or mark it to be collected | DBVE |
| G5, G6 owner or handover | back to the plant; `od-handover-and-adoption` | DBVE with the plant owner |
| G7 external connection | hold at the wait state; the sign-off is human-only (`od-cybersec-gate`) | IIAE with Plant IT; Cyber Security signs |
| G8 to G16 (build quality) | fix in the plant, or ask OD for the class A/B template | DBVE; data platform contact for G8, G11 |
| G17, G18, G19 | stop; G18 goes to Lane 3 | IIAE for G18; OD lead for a policy question |

⟨A named contact or mailbox for "guardrail failed"⟩ stays open - OD lead. The roles above are the nearest the vault records.

## The utilization expectation after go-live

`od-handover-and-adoption` already fixes what is recorded: the use case's record carries its output asset, its business process and its **utilization expectation**; and it reports utilization against `DAILY`, `WEEKLY`, `MONTHLY`, `ON DEMAND`, `ONE-TIME` and `NEVER` as recorded values on the 650 plant use cases (frontmatter count 2026-11-05: `DAILY` 125, `WEEKLY` 26, `ON DEMAND` 17, `MONTHLY` 13, `NEVER` 8, `ONE-TIME` 2 = 191 with a value, none on 459; `od-handover-and-adoption` quotes 202 with a rate - ⟨why 191 and 202 differ⟩, DBVE).
For a self-served use case the check is therefore: **the expectation is written into the record before go-live, in one of those values**, and is read again at the first scorecard review. The vault gives no target (for example a share of `DAILY`) for self-served cases - ⟨utilization target for a self-served use case⟩, OD lead. The most common recorded moment for a use case is the daily Gemba walk (125 of the 202 that record a rate are used daily, per `od-handover-and-adoption`).
