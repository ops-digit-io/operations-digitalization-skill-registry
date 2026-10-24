---
type: Skill Reference
title: Asset type and tier
description: Working through the asset-type decision past the table in SKILL.md, and exactly where this skill's job ends and build-grafana-ops-dashboard's begins once the type is Dashboard.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [analytical-support-service, use-case-support-service, dashboard]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# Asset type and tier

## The decision, worked through

`SKILL.md`'s table gives the five asset types and when each fits. The question that
actually separates them in practice is **what does the person do the moment after they look
at it** — read, decide, enter, or hand judgement to a running process:

| If the person, after looking… | Asset |
|---|---|
| …walks to the line already knowing what to check | Dashboard |
| …reads it away from the line, on a cadence, and acts later | Report |
| …never looks at it directly — another system or analysis consumes it | Analytics workflow |
| …has to type, select or confirm something back into the system | App |
| …would have made the same call themselves, every time, on a cadence | Agent |

**A dashboard that nobody walks anywhere from is a report with a worse delivery mechanism.**
If the answer to "what does the person do next" is "read it later," build a report; a
dashboard framing just hides the real cadence.

**An app disguised as a dashboard is the second-most-common miscall.** If the real ask
is "let me change the target value" or "let me log a reason code," that is data entry, not
monitoring — a dashboard with an edit button bolted on usually means the asset type was
decided too fast.

## Where this skill's job ends, once the type is "Dashboard"

This skill decides the type, the ritual and the tier intent (who reads it, at what cadence,
for what decision). `build-grafana-ops-dashboard` decides everything after that: the data
model archetype (relational vs. timeseries), the manager/analyst/operations tier's own panel
inventory and layout rules, the SQL patterns, the variable wiring, and the JSON itself. Do
not re-derive any of that here — hand it the following four things and let its Step 0 take
over:

1. **Who reads it and what question it answers** — feeds its tier choice directly (manager
   = "where do I send attention this week," analyst = "why did this happen," operations =
   "what's happening right now").
2. **The ritual and cadence** named in `SKILL.md`'s "Design for the ritual" section — feeds
   its refresh-rate and timepicker decisions.
3. **The fact table or telemetry source**, confirmed fit-for-use by
   `od-data-availability-check` — feeds its archetype choice (relational vs. timeseries).
4. **The 3-5 KPIs this asset exists to show**, each with its exact computation —
   `build-grafana-ops-dashboard`'s own Step 0 asks for this anyway; answering it here once
   means the schema interview on the other side is confirmation, not discovery.

A request that arrives already this specific ("I need a Grafana panel for X, here is the
schema") can skip straight to `build-grafana-ops-dashboard` — this skill's decision was
already made upstream. A request that arrives as "we need a dashboard for Y" has not yet
answered any of the four, and skipping to the Grafana build before answering them is how a
rebuild gets scheduled a month later for a wrong assumption about the schema.
