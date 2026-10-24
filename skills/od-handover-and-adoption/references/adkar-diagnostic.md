---
type: Skill Reference
title: ADKAR diagnostic
description: Why a use case stalls between IMPLEMENTED and PRODUCTIVE, diagnosed against the five elements of individual change adoption rather than guessed at.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [all, practice, adoption]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# ADKAR diagnostic

The three-question handover test (`SKILL.md`) checks that a use case *can* be used — what
it is, where its data comes from, who owns it. It does not check that the owner actually
*wants* to use it, or that use survives the week after the builder leaves. Those are a
different failure mode, and this reference is how to diagnose it instead of guessing.

## Why ADKAR, not a transformation model

Kotter's eight-step model and similar frameworks describe organization-wide change — a
coalition, a vision, a culture shift. A stalled handover is not that: it is one named plant
owner, one asset, one decision. **ADKAR (Awareness, Desire, Knowledge, Ability,
Reinforcement)**, developed by Jeff Hiatt at Prosci, is the individual-level counterpart —
Prosci itself keeps it distinct from its own organizational-change process for exactly this
reason [Prosci, *The Prosci ADKAR Model*, prosci.com/methodology/adkar, retrieved
2026-10-22]. It fits a single handover's grain.

## The five elements, mapped onto a use case handover

| Element | What it means here | Already covered by |
|---|---|---|
| **Awareness** | The owner knows *why* this exists — which decision or ritual it feeds | Three-question test, Q1 |
| **Desire** | The owner wants to use it — it was not simply imposed | **Not covered elsewhere — check this explicitly** |
| **Knowledge** | The owner knows how to read it and what to do when it says something | Partly — Q1 names the decision; training is still a separate act |
| **Ability** | The owner can actually use it in a real shift — access, a device, the data genuinely flows | Three-question test, Q2 (data path) |
| **Reinforcement** | Use continues after the builder has left | **This is the utilization-rate field on the Scorecard, read over time, not at handover** |

Desire and Reinforcement are the two elements the existing handover test does not ask about
at all — they are also the two that explain most `NEVER` rows: a use case can pass every
question about *can* this be used and still fail on *does anyone want to*, or *does it keep
being used once nobody is watching*.

## The barrier point

Prosci's own diagnostic concept: the **barrier point** is the first element, in sequence,
that is not yet sufficient — conventionally, the first element scoring 3 or below on a 1-5
scale [Prosci, *Individual Barriers to Change and What to Do About Them*,
prosci.com/blog/individual-barriers-to-change-and-what-to-do-about-them, retrieved
2026-10-22]. **The elements are sequential and the order matters**: resolving a Knowledge
gap does nothing if Desire has not been reached yet, and training someone harder on a
dashboard they do not want is wasted effort aimed at the wrong element.

**Rate all five, 1-5, in order, and stop at the first one that is not yet sufficient — that
is the barrier point, and it is the only one worth acting on right now.**

## Worked example

A cycle-time dashboard for a braider cell: handed over, data path confirmed, plant owner
named — and utilization reads `NEVER` after six weeks.

- **Awareness: 4.** The shift lead can say what decision it feeds (changeover timing).
- **Desire: 2.** It was specified by the plant's continuous-improvement team, not requested
  by the shift lead who is supposed to use it daily. **Barrier point.**

Training the shift lead harder on the dashboard (Knowledge) would not have helped — the
actual fix was a five-minute conversation about what the dashboard changes for their own
shift, not a re-demo. That conversation, not a repeat handover, is what "review with the
requester" in `SKILL.md`'s low-utilization procedure is actually for.

## Rollout action per element

A concrete, minimal action for each element — not a training program:

| Element | Minimal closing action |
|---|---|
| Awareness | State the decision it feeds, once, at the ritual it belongs to (shift handover, Gemba) — not in a separate meeting |
| Desire | Ask the owner what changes for them personally if they use it; if nothing does, that is the finding, not a training gap |
| Knowledge | One walkthrough at the actual screen, during a real shift, answering "what do I do when it says X" |
| Ability | Confirm the device, the access and the data are live *at the point of use*, not in a demo environment |
| Reinforcement | Put the utilization check on the Scorecard cadence — see `od-scorecard-reporting` — so it is asked again without the builder present |
