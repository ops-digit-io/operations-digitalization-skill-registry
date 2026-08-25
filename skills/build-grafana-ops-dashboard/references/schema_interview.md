---
type: Skill Reference
title: Schema interview
description: The interview that stops a dashboard being rebuilt because the first version assumed the wrong schema.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [grafana, schema, elicitation]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# schema_interview.md — Questions to ask before writing any SQL

Most dashboard rebuilds happen because the first version was built on assumptions about the schema that turned out to be wrong. The interview below covers what you actually need to know before writing the first query.

This file is a question bank. The matching short version (Step 0) lives in `SKILL.md`.

---

## When to run the full interview

- First-time dashboard for a new schema — always.
- Adding a major new domain to an existing dashboard family — partial (skip questions you've already answered).
- Migrating a dashboard between environments where the schema is "the same but different" — partial, focused on the differences.

The full interview takes 10–20 minutes if the user has the answers. If they don't have all the answers, the missing ones are exactly the spots where the dashboard will fail later — flag them explicitly rather than guessing.

---

## Block A — Domain framing (always)

Before any technical question, agree on what the dashboard is for. If the user can't answer these in two sentences each, the dashboard isn't well-defined yet.

1. **What's the operational question this dashboard answers?** One sentence. Ideally starts with a verb: "Decide which line to send the maintenance crew to," "Investigate why throughput dropped last week," "Confirm production targets are tracking on shift."
2. **Who reads this dashboard?** Role + frequency. "Plant manager, weekly Monday standup." "Shift lead, glanced at every 15 minutes."
3. **What action do they take based on what they see?** If the answer is "look at it," the dashboard is decoration. Push back gently.
4. **What time horizon is it scoped to?** Real-time / rolling 24h / week-over-week / month-over-month / arbitrary.

These four answers determine the tier (manager / analyst / operations) before any schema question matters.

---

## Block B — Identifying the archetype

Determines whether the dashboard reads from `relational_patterns.sql` or `timeseries_patterns.sql`. Often the user has both and you'll build separate queries against each.

5. **Is the operational data stored as one wide telemetry table with UUID-keyed signals, or as one or more domain-specific fact tables?** If both, ask which the dashboard reads from primarily.
6. **If timeseries: is there a metadata table mapping UUIDs to human-readable signal names?** Without one, every signal has to be hardcoded by UUID — fragile.
7. **If relational: how many fact tables does the dashboard need to read from?** One is normal. Two or more requires deciding how to align them (typically on time + machine_id).

---

## Block C — Time semantics (always)

Every panel hinges on these. Get them right early.

8. **What is the timestamp column on each fact table?** Common names: `start_time`, `event_time`, `created_at`, `systime`, `ts`. Pick one canonical name per table; some tables have multiple time columns and you need to know which represents "when did the thing happen."
9. **What timezone is the column stored in?** `timestamptz` (UTC + offset metadata) is normal. Naive `timestamp` without tz is a footgun — you'll need to know the implicit timezone to correctly handle DST, shift boundaries, etc.
10. **Are there any cases where the timestamp can be NULL or in the future?** Some pipelines fill `created_at` from the producer's clock; clock skew produces future-dated rows. Decide explicitly: ignore future-dated, clip to NOW(), or flag.

---

## Block D — Interval semantics (relational archetype only)

Skip this block if the fact table is point-shaped (each row is a single timestamp, no duration).

11. **For interval-shaped facts: what column represents the end time?** `end_time`, `closed_at`, `ended`, etc.
12. **Can `end_time` be NULL? What does NULL mean?** Two cases: (a) the event is still ongoing — coalesce to NOW(); (b) the event was abandoned without proper closure — exclude.
13. **What's the typical and maximum duration?** Affects whether window-clipping is necessary. If the maximum incident duration is 2 hours and dashboard windows are always longer, clipping rarely matters in practice. If incidents can span days and dashboards show short windows, clipping is essential.
14. **Are there gaps where `end_time < start_time` due to data-quality issues?** If so, decide explicitly how to handle them — exclude, clamp, flag.

---

## Block E — Multi-tenancy and access (always)

15. **Is the data multi-tenant?** I.e. does one fact table contain rows for multiple customers / sites / business units that should never see each other's data?
16. **What's the tenant column?** Usually `account_id`, `tenant_id`, `customer_id`, `site_id`, `org_id`. Sometimes hierarchical (account_id + region_id).
17. **Can the dashboard's user belong to multiple tenants?** If yes, `$account` must be multi-select with includeAll. If no, single-select with no "All" option.

Skipping this question is the most common cause of one customer seeing another customer's numbers in production.

---

## Block F — Soft-deletes and visibility flags (always)

Every fact table accumulates rows that should be hidden from analytics — archived, deleted, ignored, test data, etc.

18. **What flags determine whether a fact-table row should be visible in dashboards?** Common: `is_archived`, `is_deleted`, `deleted_at IS NOT NULL`, `is_test`, `is_ignored`.
19. **What flags exist on the dimension tables?** Machines that have been decommissioned (`machines.is_active = false`), reasons that have been retired (`reasons.is_archived = true`).
20. **Is there a "currently active" snapshot vs full history concept?** Some schemas keep historical rows for retired entities; the dashboard may want to show those for old data but exclude them from current-state panels.

Add every applicable flag to the canonical WHERE clause. Forgetting one means showing test data, deleted incidents, or decommissioned machines in production dashboards.

---

## Block G — Categorical dimensions (analyst tier only)

For dashboards that need filtering or grouping by category.

21. **What are the categorical filters the user wants?** Machine, line, department, reason, severity, defect type — list them by name.
22. **Are any of them hierarchical?** E.g. `parent_reason_id` chains forming a tree. If so, decide whether the dashboard rolls up to parent or shows leaves.
23. **Are any of them nullable foreign keys on the fact table?** Critical — `IN ($var)` filters silently drop NULL FK rows. List which FKs can be NULL and what NULL means semantically (unclassified, doesn't apply, awaiting review).

---

## Block H — Specific metrics requested

24. **What are the 3–5 KPIs the user expects to see on the dashboard?** "Total downtime," "MTTR," "incident count," "OEE," "P95 cycle time," etc.
25. **For each KPI, agree on the exact computation.** "Total downtime" can mean: sum of all incident durations / sum window-clipped to the visible range / sum excluding incidents flagged auto-closed / etc. The answers differ by 10–30%; the user has an opinion even if they don't realize it.
26. **What's the expected order of magnitude?** "MTTR is around 45 minutes for our fleet." Disagreement between this answer and what the dashboard shows is one of the fastest ways to catch a logic bug.

---

## Block I — Out-of-band knowledge (often skipped, often important)

27. **What's the production calendar?** Shift starts and ends, weekend coverage, holidays. Dashboards that show "stoppage minutes" without a shift filter conflate planned downtime with unplanned downtime.
28. **Are there known data-quality issues?** Periods of missing data, sensors that drift, manual data entry that produces typos. Calling them out lets the dashboard either include data-quality KPIs or exclude affected periods.
29. **What's the existing dashboarding solution this replaces, if any?** If the user has been looking at numbers from another tool for years, those numbers are anchored in their head. Reproduce them first, improve from there.

---

## How to use the answers

By the time the interview is complete, you have:

- A target tier (manager / analyst / operations) — from Block A
- A canonical SQL "WHERE" template — from Blocks E and F
- A duration formula — from Block D
- A variable list — from Blocks E and G
- A KPI definition list with agreed semantics — from Block H

Write these down before writing any panel SQL. They become the canonical references throughout the dashboard. Every panel uses the same WHERE template, the same duration formula, the same variable expansions. Inconsistency between panels — different filters in different panels showing different numbers — is the most common defect.

---

## Short version (3-question fallback)

When the user has 5 minutes, not 20, ask only:

1. **What question does this dashboard answer, and who reads it?** (compresses Block A)
2. **What's the fact table's name, timestamp column, soft-delete flag, and tenant column?** (compresses Blocks B, C, E, F)
3. **What are the top 3 KPIs and their exact definitions?** (compresses Block H)

Build a draft. Iterate from real questions raised when the user reads the draft.
