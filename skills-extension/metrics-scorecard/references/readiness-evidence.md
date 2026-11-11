---
type: Skill Reference
title: Readiness evidence
description: What the readiness RAG matrix actually requires before a dimension turns green, and why "Available" is a claim that needs a record behind it, not a status anyone can set.
resource: ../SKILL.md
status: stable
tags: [all, practice, scorecard]
---
# Readiness evidence

## The rule, stated once because three skills already assume it

**A readiness dimension turns "Available" only because `deploy-acceptance` passed, was
witnessed by a named human on the plant side, and the result was recorded.** Not because a
machine was connected, not because a dashboard was built, and never because someone
declared it so ahead of the pass. `deploy-acceptance`'s own definition of done states it
directly: "on the Information Integration side, the readiness dimension moved with
evidence." `mi-equipment` enforces the same rule from its side ("never mark a
machine `INTEGRATED` before its acceptance test passes, and never claim a readiness
dimension 'Available' without evidence").

This makes the readiness matrix a **derived report, not an input you fill in** — every
green cell should be traceable to one acceptance-test record. If it cannot be traced, the
cell is wrong regardless of how confident the person reporting it is.

## Red, amber, green — what each state means here

| State | What it means | Who can move it there |
|---|---|---|
| **Red** | No acceptance-test pass on record for this dimension/location, or a passed test later failed in production use | Anyone reporting a gap — this state needs no authority to declare |
| **Amber** | Acceptance in progress, or passed with a named open item | `deploy-acceptance` mid-procedure |
| **Green ("Available")** | Acceptance test passed, witnessed, recorded | Only a recorded pass moves it; this skill never sets the color itself, it reads what the record already says |

**At a strategic plant, red is the intervention trigger** (the existing metrics table
already states this) — because a strategic plant's readiness is what the use-case rollout
plan for that plant is actually betting on. A strategic-plant red is reported with the
specific dimension and the named blocker, not as a bare color.

## What this means for a scorecard update, specifically

1. Do not recolor a cell from a conversation or a status update — recolor it only from an
   `deploy-acceptance` result or an `deploy-handover` record.
2. Where a cell has been green for a long period with no re-test, say so rather than
   implying it was re-verified this cycle — readiness is a point-in-time fact, not a
   standing one, and a machine or connector can regress silently.
3. A dimension with **no acceptance-test record at all** is not the same as one that
   failed — report it as "not yet assessed," not as red for the same reason, so the two
   different problems (never tried vs. tried and failed) stay distinguishable in the
   report.
