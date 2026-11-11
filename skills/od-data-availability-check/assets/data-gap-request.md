---
type: Skill Asset
title: Data gap request
description: The named request a data gap becomes when it is routed to the Information Integration lane - which machines or sources, which signals, which plant, which use case is waiting, and what was already checked - so the lane can act without asking the requester again.
resource: ../SKILL.md
status: draft
tags: [analytical-support-service, practice]
---

# Data gap request

Use after a [verdict](data-availability-verdict.md) that names a gap at step 1, 2, 3 or 4, or
a non-machine source ([`non-machine-data-sources.md`](../references/non-machine-data-sources.md)).
One request per plant and per gap kind. Send it to the IIAE of the region; keep a copy on the
use case record as a dependency.

## 1. Who is waiting

| | |
|---|---|
| Requester (role) and plant | |
| Use case (record) or analysis, and its template (e.g. Andon Board, OEE Calculation) | |
| What happens when the data arrives (decision, dashboard, savings row) | |
| Date the answer is needed, and why that date | |

## 2. What is missing

| Item | Value |
|---|---|
| Gap kind (one only) | measurement / integration / standardization / fitness / definition / source not reachable |
| Machines or sources (names as in the Machine List or Legacy Application List) | |
| Signals needed (canonical names where they exist) | |
| Granularity and history needed | |
| Machine List state found, with export date | status (`INTEGRATED` / `NOT INTEGRATED` / blank), route, vendor, model, protocol |
| Connector in the Connector Overview and its state | name; `Productive` / `Idea` / `Development`; `USE` / `NOT AVAILABLE` / `DO NOT USE` |
| Blocker text on the row, if any | |
| Project reference or wave, if any | |

## 3. What was already checked (so nobody repeats it)

- [ ] Machine List row read; blank fields named, not read as "no"
      ([`machine-list-completeness.md`](../references/machine-list-completeness.md))
- [ ] Connector Overview read; availability checked, not only existence
- [ ] Flow corpus or edge platform checked for the signal (a flow proves presence, never absence)
- [ ] Existing assets checked (step 6): library, portfolio, other plants' delivered cases
- [ ] Definition agreements checked where the template needs them (ideal cycle time,
      micro-stop threshold, reason catalogue, recipient and acknowledgement, reaction plan)

## 4. What the requester accepts meanwhile

| Option | Accepted? |
|---|---|
| A labelled partial answer from what exists | |
| A manual or periodic export from the source, labelled as such | |
| Waiting for the integration | |

A proxy signal is never substituted without being said in the deliverable.

## 5. Routing

| Routed to | Why |
|---|---|
| `od-equipment-integration` (assessment route) | Machine not integrated, route undecided |
| `od-signal-standardization` | Connected, point not published or not named canonically |
| `od-equipment-integration` | No route exists (legacy, unsupported protocol) |
| `od-cybersec-gate` | External connection needs sign-off first |
| Capital request / `od-capital-request` | Measurement gap: no sensor exists |
| Plant ME (Machine List update) | The list cannot answer; the plant must fill the field |

## 6. Closing the loop

| | |
|---|---|
| Request sent (date) and to which role | |
| Answer received (date) | |
| Machine List or use case record updated | |
| Dependency removed from the use case record | |
