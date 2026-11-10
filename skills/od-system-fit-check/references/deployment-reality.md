---
type: Skill Reference
title: Deployment reality
description: Guidance, no figures. Why the same tool catalogue is in different states at different plants, and how to read a plant's own tool-availability table so a system-fit check runs against what that plant has, not the estate average.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [practice, system-fit]
generated: { by: claude-code/1, at: 2026-10-23T00:00:00Z }
---
# Deployment reality — the same tools, different plants

Every Use Case Definition Workshop records a **Smart Factory Tools Availability** table —
status and recommendation, per tool, for that one plant. The non-bets list is estate-wide
policy; whether MDA/PDA or QFPR is *available right now* is a per-plant fact.

## How to read a plant's table

| Field | Meaning | Trap |
|---|---|---|
| Tool | One row per catalogue tool (IIoT edge platform, Manufacturing Service Bus, MDA/PDA, MES, Recipe Management, MIL, QFPR, Data Science Factory) | A tool absent from the table is "not listed", not "not available" |
| Status | Done / Ongoing / Not available, with a planned year where stated | "Ongoing" is not "available"; the planned year slips |
| Recommendation | e.g. "not necessary", "not recommended as of now", "needed for multiple use cases" | The recommendation is the plant's reasoning at workshop date, and changes |

## Patterns to expect

- **Availability tracks demand, not a uniform rollout schedule.** A tool can be "not
  necessary" at one plant and "needed for multiple use cases" at another with no other row
  differing. Never infer a plant's state from another plant's table.
- **MES is the stable row.** It is typically "not available" with a "not necessary" or "not
  recommended as of now" reason; everything else moves.
- **Present is not in scope.** A demo/test system of the Manufacturing Image Library can be
  deployed at a plant while the same table says "no use cases yet, not yet planned". A tool
  being technically present is not the same fact as a use case being in scope there. Check
  which one a request is claiming.
- **Workshop tables age.** A "planned <year>" line is a statement at a date; compare with the
  live Tool Overview (`plant-tool-availability.md`).

## How to get the plant's current table

1. Open the plant's most recent Use Case Definition Workshop summary and read its tool
   availability table; note its date.
2. Open the plant's rollout rows in the live Tool Overview and note its export date.
3. Where they differ, state both with dates and ask the plant (ME/IT). See the rule in
   `plant-tool-availability.md`.

## Sources

Internal evidence: per-plant Use Case Definition Workshop summaries in
`Work-OpsDigit-Knowledge/Split Slides/10-Workshops--*`. Full citations in `SKILL.md`'s
`metadata.derived_from`.
