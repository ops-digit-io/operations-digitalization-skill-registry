---
type: Skill Reference
title: Epic and user stories
description: The background description, which epic axis to use, how to cut stories that stand alone, and what makes acceptance testable.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [requirements, epic, user-stories]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# The epic and its user stories

The requirement (§1–§11) says **what must be true**. This says **how the work is cut up so
somebody can start on Monday.** Every requirement produces exactly one epic, and every epic
carries **at least two user stories** and a **background description**. One story means you
have written a story and called it an epic; zero stories means you have written a wish.

## This layer already exists — and it is hollow

The SharePoint use case list encodes a two-axis hierarchy in its own fields
(`UseCaseParentId`, `UseCaseParent-ProcessId`), and the generated register
`usecase-epics-user-stories.md` renders it: process epics, capability epics and leaf
user stories. So this is not a new ceremony. The structure is there. What is typically in it
(re-count on the live register before quoting anything):

| Of the leaf stories | Pattern |
|---|---|
| Carry a target text | A majority |
| Carry any narrative at all (target, comments, blockers) | A bit more than carry a target text |
| Carry an **"I want"** tag — the capability the story asks for | Few |
| Mention **acceptance criteria** anywhere | Almost none |
| Carry a distinct **"so that"** — a reason particular to this story | None |

Every leaf renders with the same generated benefit clause:

> *…**so that** the process gains transparency, faster reaction and less manual effort.*

That sentence is true of every use case ever written, which is what makes it worthless. And
because few stories tag what they want, most render as *"I want (not tagged)"* — a story
with neither a capability nor a reason.

**The failure this reference exists to prevent is not a missing structure. It is a structure
filled with a sentence that fits anything.** If your "so that" would read equally well on a
different plant's different machine, it is the generated one with new words.

## The background description

**Required, and it is not the epic statement.** The epic statement is one sentence for a
backlog; the background is the paragraph that lets somebody who was not in the room decide
whether a story is right — six months later, when the person who asked has left. The
department's own skill map names exactly this as the risk: the requirement step is *"the most
dependent on tacit judgement, and the one currently held by a departing individual."*

It answers five things, and it is prose, not a table:

1. **What happens today** — the actual sequence, with who does it and how often. *"The shift
   leader walks the line at 06:00 and writes the counter reading from each of the seven
   presses on a clipboard."* Not *"data collection is manual."*
2. **The moment of use** — when the output gets looked at, by whom, and what they do next.
   If nobody can name the moment, the epic has no consumer and should be refused here, cheaply.
3. **The decision it changes** — what a person will do differently. *"Knowing the counter at
   06:00 instead of 14:00 lets the shift leader re-plan the second shift while there is still
   a second shift to re-plan."*
4. **Why now** — the trigger. A customer complaint, a line moved, an audit finding, a machine
   purchased. Requirements with no trigger sit in `IDEA` for years; many use cases
   are in `IDEA` and some of them are refusals nobody wrote down.
5. **What it is *not* for** — the scope fence. Written here, the fence holds; written nowhere,
   the epic grows a dashboard for a second department by the third sprint.

A background that could be pasted onto another plant's epic without editing has not been
written yet.

## Which epic — capability or process?

Both axes exist in the source data and neither is optional, but they answer different
questions:

| Axis | The epic is | Use it as the epic when |
|---|---|---|
| **Capability** (`OESL-Process_Values`, `OESL-Andon_Board`, from the capability template list) | this plant's instance of a digital capability | **Default.** Reuse across plants happens here — this is the axis `od-use-case-standardization` reads |
| **Process** (`OESL-Rubber-Vulcanization`, from the process template list) | this plant's instance of a manufacturing process | The demand came from a process owner and covers several capabilities on one process |

**Record both.** The source data shows what happens when you do not: many leaves carry only a
capability parent and many only a process parent, so a query on either axis silently misses
part of the portfolio. Whichever you pick as the epic, fill the other as an attribute.

## Cutting stories out of an epic

A story is a slice a team can finish and a plant can use. Five axes that actually produce
independent slices here — in preference order, because the first two survive contact with
integration and the last three often do not:

1. **By moment and role.** The shift leader at handover and the process engineer at a quality
   escape are two stories even when they read the same number. This is the department's own
   first judgement call: *different people, different moments → different use cases.*
2. **By signal availability.** The strongest cut in this estate. Split what is deliverable
   from signals that **exist today** (verified via `od-data-availability-check`) from what
   waits on machine integration. The first story delivers while the second sits behind a
   connectivity blocker — and **machine connectivity is a recurring blocker class**,
   so this cut is the difference between shipping something and shipping nothing.
3. **By manual step removed.** Each manual step that disappears is a story with its own
   before/after. It is also the only cut whose benefit is directly measurable.
4. **By machine or line**, when the same capability lands on equipment with different PLCs —
   the second machine is rarely a copy, and pretending it is hides the real integration cost.
5. **By lane boundary.** If part of the epic is an integration deliverable and part is a use
   case deliverable, they are separate stories with separate acceptance — because they are
   accepted by different people.

**Do not cut by technical layer.** *"Story 1: connect the PLC. Story 2: build the flow.
Story 3: build the dashboard."* is a plan, not a set of stories: none of the three is usable
alone, so none of them can be accepted, so all three finish at once or not at all. If your
stories must be delivered in a fixed order and only the last one is worth anything, you have
written tasks. Put them under one story as its steps.

## What a user story must carry

| Part | Rule | How it fails here |
|---|---|---|
| **Role** | A named plant role — shift leader, process engineer, maintenance planner, quality technician | *"the shop-floor / process team"* — the generated placeholder on every generated story |
| **Capability** | What they want, in the plant's words | *"(not tagged)"* — the usual state |
| **Reason** | The decision or action it changes, particular to this story | *"…transparency, faster reaction and less manual effort"* on every generated story |
| **Background** | Two or three sentences of context for this story specifically | usually absent; the epic's background is not a substitute |
| **Signals** | Canonical names with an existence verdict, from §5 | assumed rather than verified — the most common late failure |
| **Acceptance criteria** | Testable, Given/When/Then, including one use-in-a-real-shift criterion | almost none mention acceptance at all |
| **Value** | Inherited from the epic or apportioned, labelled `CALCULATION` / `ESTIMATION` / *not yet assessed* | a figure with no label reads as fact |
| **Definition of done** | Development · Implementation · Handover, per the list's own three fields | the estate already tracks these; use them rather than inventing a status |
| **Sequencing** | What must be true before this story starts | the connectivity blocker discovered in week three |

## Acceptance criteria that are actually testable

Write them Given/When/Then, and make the value in them specific:

> **Given** press 3 has completed a cycle,
> **When** the shift leader opens the line view,
> **Then** the cycle count shown is the count at most 60 seconds old, and matches the PLC
> counter exactly at shift end.

Three criteria per story is usually right. **One of them must require use in a real shift by
a named role** — that is the department's own handover rule, and it is the criterion that
separates a delivered use case from an accepted one. A criterion you cannot fail is not a
criterion: *"the dashboard is user friendly"* fails this test; *"the shift leader completes
the 06:00 round without the clipboard for ten consecutive shifts"* passes it.

## Epic acceptance is not the sum of story acceptance

An epic can have every story accepted and still not be done — the stories were sliced, and
something only exists across the whole. State it explicitly: the capability is registered
against the standard cluster template, the plant role uses it without the old manual route
running in parallel, and the output data points are registered on the edge platform.

**If the epic's acceptance is genuinely just "all stories accepted", say so.** That is a legitimate
outcome and better than inventing a hurdle.

## Sizing

No story points. The estate has no velocity history to calibrate them against, and a number
with nothing behind it invites a false comparison between plants. Use the three status fields
the list already has (Development / Implementation / Handover) and, where a date matters, a
target date with the constraint that drives it.

An epic that needs more than about eight stories is two epics — or the background is
describing a programme rather than a requirement.
