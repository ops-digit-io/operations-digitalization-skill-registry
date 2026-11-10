---
type: Skill Reference
title: Machine context
description: The ten sources that say what a machine does rather than what it emits, ranked by how much confidence each earns.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [signals, machine-context]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Machine context — reading how the machine works

A tag list says what the machine *emits*. It does not say what the machine *does*. Without
that, you get names without meanings — which is the failure the whole skill exists to
prevent.

**The context is not in any system of record.** `documentation_available` and
`documentation_link` exist as fields on every machine row; check on the live Machine List whether anyone fills
them (they have been empty so far). So the context has to be gathered from whatever the plant can actually
produce, and this file is about working from that.

---

## The sources, what each yields, and what it cannot tell you

Ranked by how much they say about *how the machine works*.

### 1 · The PLC program — the highest-value source

An S7 project, TIA archive or Studio 5000 file. Usually the hardest to obtain and worth the
effort: **it is the only source that is definitionally in step with the machine**, because it
is the machine.

| Read | Yields |
|---|---|
| **Symbol / tag table** | Candidate signals with addresses, data types, and the programmer's own names |
| **DB structure** | Which values are grouped — a "Production" DB is a signal family |
| **Step chain / sequence logic** (SFC, GRAFCET, case-on-step-word) | Cycle boundaries → `CycleStart`, `CycleEnd`; the step numbers behind `CycleStepChain` |
| **Mode word / state machine** | The integer codes behind `MachineMode`, and **what each means** |
| **Alarm / message blocks** | The error-code table for the alerting lookup |
| **Comparison to setpoints** | Which limits already exist in the PLC rather than needing configuring |

**Its limits.** A program tells you what the machine *can* do, not what the plant *does* —
disabled branches, commissioning leftovers and a mode nobody uses all look live in code. And
it does not tell you which signals matter; every tag looks equally important in a symbol table.

> **You already need the PLC program.** It is the breakpoint for connecting the machine at
> all — *"without the PLC program we CAN NOT connect the PLC."* So this is not an extra ask;
> it is reading something you had to obtain anyway.

### 2 · Tag / symbol export

An SDFI file, a Softing import `.txt`, a CSV from a tag-export tool. **This is the input the
analyser reads directly.**

Yields names, addresses and types — and nothing about meaning. **Names in an export are the
programmer's, not the data model's**: this is where names like `_part0_io`, `DB15.DBW20` and
misspellings such as `Tempature` come from (illustrative). Treat every name as a candidate to be renamed, not as an
answer.

### 3 · Sequence chart / flow chart / cycle diagram

An SFC, GRAFCET, a cycle-time chart, or a hand-drawn step sequence.

**The single best source for the timing family.** It tells you where a cycle begins and ends,
which steps are value-adding, and where the machine waits — which is exactly what separates
`CycleTime`, `LoadingTime`, `ProcessTime` and downtime, and what an availability figure needs
in order to be comparable.

Also settles a question a tag list never can: **is a stop the machine waiting on the operator
or on upstream?** That is the PackML acting/wait distinction, and it decides what counts as
downtime.

### 4 · Layout / line layout / P&ID

Where the stations are, in what order, with what buffers between them.

| Yields | Why it matters |
|---|---|
| Where to count | Counting at the wrong station double-counts rework |
| Where a part becomes "good" | Decides which counter feeds the quality rate |
| Buffers between stations | A buffer decouples cycle times — two stations' cycle times are not comparable across one |
| Which machines share a cell | An edge device may serve several; the failure domain changes |

**A layout is how you avoid the commonest OEE mistake** — measuring throughput at a point
that is not the constraint.

### 5 · Machine handbook / operating manual

The vendor's manual, in whatever language it shipped in.

| Section | Yields |
|---|---|
| Operating modes | The authoritative mode list — map to PackML rather than inventing |
| Alarm / fault code table | The error-code → message lookup, ready-made |
| Process parameters | Which values are settable, their units and ranges — **the unit convention the estate lacks** |
| Interfaces | What the machine can already expose, including any companion specification |
| Maintenance intervals | Condition-monitoring candidates |

**Read the interfaces chapter first.** It is where you find out the machine already speaks
OPC UA or EUROMAP, which changes the integration route entirely.

### 6 · HMI screens

Screenshots, or ten minutes standing at the machine.

**What the operator already looks at is the shortlist of what matters.** A value on the main
HMI screen is a value somebody uses; a value three menus deep usually is not. This is the
cheapest importance signal available and it needs no document at all.

### 7 · Electrical schematic / I/O list

Sensors and actuators, terminal by terminal. Verbose, and decisive for one question: **does a
physical measurement exist at all?** If there is no sensor, no amount of PLC work produces the
signal — that is an investment conversation, not an integration one.

### 8 · A proven instance at another plant

An existing Node-RED flow, dashboard or library entry for the same capability elsewhere.

**Check this before reading anything else.** If another plant has built it, their signal list
*is* the requirement, and this becomes an adoption. `od-use-case-standardization`.

### 9 · The Machine List row

Vendor, PLC model, part number, protocol, integration status. Thin — but it is the join key
for everything else, and it is the only source that is already structured.

### 10 · The operator and the setter

Not a document, and usually the only source that says **what actually goes wrong**. The
PLC program says what is possible; the operator says what happens on Tuesdays. See
`od-requirements-breakdown` §elicitation.

---

## Confidence — say which source a signal came from

Every candidate signal carries the source it came from, because the sources are not equally
reliable and a reader deserves to know.

| Source | Confidence | Because |
|---|---|---|
| OPC UA browse / live data-point config | **Verified** | It is the running system |
| PLC program, current deployed version | **High** | Definitionally in step — *if* it is the deployed version |
| Tag export | High for existence, **low for meaning** | Names are the programmer's |
| Sequence chart, handbook | Medium | Authoritative on intent, may be out of date |
| Layout, schematic | Medium | Structural, rarely revised |
| HMI observation | Medium — **high for importance** | What is used is what is shown |
| Another plant's instance | Medium | Same capability, different machine |
| Verbal description | **Low** | Confirm before building on it |

> **An archived PLC project is not the deployed program.** A symbol import from last year's
> archive produces tags that connect and read nothing. If the version cannot be confirmed,
> mark every signal from it Medium and verify against live data before acceptance.

---

## The translation — from context to a standardized signal

Five steps. **The output is the report**, not a list.

**1 · Inventory candidates.** Everything each source offers, with the source recorded. Do not
filter yet — filtering before you understand the machine is how the important signal gets
dropped.

**2 · Describe how the machine works** in three or four sentences, from the sequence chart and
layout: what it makes, what one cycle is, where it waits, what makes a part good. **If you
cannot write this, you do not yet have enough context** — and every signal decision after this
point would be a guess.

**3 · Map candidates to canonical names.** `od-signal-standardization` §Step 5, and check the
public data models first: a machine exposing EUROMAP or OPC UA for Machinery is already
named — `public-data-models.md`.

**4 · Cluster and rank.** Functional area and importance —
`clustering-signals.md`. The HMI observation from source 6 is a
strong tiebreak.

**5 · Verify existence and state the four elements.** Name, meaning, unit, collection method.
The handbook supplies units; the sequence chart supplies collection method; nothing supplies
meaning except understanding the machine.

---

## What to do when the context is thin

Common, and not a reason to stop.

| You have | Do |
|---|---|
| Tag export only | Cluster by pattern, then **stand at the HMI for ten minutes**. Cheapest context there is |
| Handbook only, no PLC access | Use it for modes, alarms and units. Mark existence unverified and confirm before acceptance |
| Nothing but the machine | Watch one full cycle with the setter, sketch the sequence yourself, and treat that sketch as the source |
| A proven instance elsewhere | Take their signal list as the baseline and record only deltas |
| No sensor for what is asked | Stop. This is an investment question |

**Write down which of these you were in.** A report that says *"tag export only, existence
unverified"* is honest and usable. One that omits it invites the reader to assume more
certainty than exists — and that assumption is how a misspelled name ends up read by many flows.
