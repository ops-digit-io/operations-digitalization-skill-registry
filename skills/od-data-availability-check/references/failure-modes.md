---
type: Skill Reference
title: Failure modes
description: The three shortfalls at steps 2, 4 and 5 that are indistinguishable from a dashboard, how to tell them apart, and who owns each.
resource: ../SKILL.md
status: stable
tags: [data-availability, diagnosis]
---

# Failure modes

**An empty panel looks the same whatever caused it.** That is the entire reason this skill
exists. Three shortfalls produce an identical symptom, belong to three different owners, and
take between an afternoon and two quarters to fix. Naming which one you have is the
deliverable — "no data" is not.

| | Step 2 · not integrated | Step 4 · not standardized | Step 5 · not fit for use |
|---|---|---|---|
| **What is true** | The machine is not connected | It is connected, but this point is not published or not named canonically | It is published, but too coarse, too late or too full of holes |
| **What you see** | Empty panel | Empty panel | A panel that looks right and is wrong |
| **Owner** | Information Integration | `od-signal-standardization` | Analytical lane, with the platform |
| **Cost** | Weeks to quarters — hardware, network, OT sign-off | Days — naming, a flow, a registration | Hours to weeks, or unfixable if history was never captured |
| **How to confirm** | Machine List `integration_status` | Search the flow corpus and the edge platform for the point | Query the offload and look at the actual rows |
| **What it is not** | A data request | An integration request | Either of the above |

**The worst of the three is step 5**, because it is the only one that fails quietly. Steps 2
and 4 give you nothing, which is at least honest. Step 5 gives you a number that renders, gets
believed, and is wrong — a shift-level figure read as hourly, a gauge that stops updating,
a counter that resets on restart.

## Two more that are not data gaps at all

**Measurement gap.** No machine produces the signal in the first place — there is no sensor.
This is step 1, and it fails before any of the above. It is a capital request, not a data
request, and calling it a data gap sends it to a lane that cannot fix it.

**Definition gap.** The signal exists, flows and is fit — and nobody has agreed what counts.
Which stops are downtime; what makes a part good; when a shift starts. The requirement's own
work, per `od-requirements-breakdown`: *"Selection of process parameter to be connected"* is a
recorded blocker in this portfolio and it belongs to the requirement, not to engineering.

## Saying it out loud

Three sentences, in this order, and the analysis either proceeds or does not:

> **What can be answered** with what exists today, and how well.
> **What cannot**, which of the five gaps it is, and who owns it.
> **What it would take** to move the second into the first.

A partial answer that is labelled is useful. An unlabelled one is a liability, because the
reader cannot tell which part to trust — and the standing guardrail of the Analytical lane is
to **flag the gap rather than fill it**.
