---
type: Skill Reference
title: Requirement template
description: The ten core sections and the four lane variants, what each is for, and how each one fails in practice.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [requirements, template]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# The requirement template

**This template is not invented.** It is the structure the best-documented use cases in the
portfolio already use, made explicit and completed. Those section headings appear inside the
existing `target_text` and `blockers` fields:

| Heading already in use | Use cases carrying it |
|---|--:|
| `Use Case Target Overview` | 99 |
| `Major Issue` | 34 |
| `Tags of Interest` | 29 |
| `Acceptance criteria` | 13 |
| `Traces to` | 13 |
| `Key Problem` | 10 |
| `Major` / `Minor Blocking Points` | 162 records |

So the estate already knows what a requirement looks like. **It writes one about one use case
in eight.** The job is to make that the default, not to introduce a new form.

---

## The core — every lane, every requirement

Ten sections. A requirement missing any of §1–§6 is not ready to hand over.

### §1 · Identity

```
Requirement:   ⟨asset⟩ - ⟨artefact⟩          ← the flow/use-case naming convention
Plant:         ⟨plant⟩
Machine(s):    ⟨name⟩ ⟨(EQ id)⟩              ← joins to the Machine List
Capability:    ⟨one of the 11 templates⟩
Process group: ⟨one of the 29⟩
Lane:          ⟨which of the four owns delivery⟩
Author / date: ⟨name⟩ ⟨date⟩
```

The **capability** is not decoration. It is what makes this findable from another plant, and
it decides which standard requirements checklist applies (§4).

### §2 · Key Problem / Major Issue

One paragraph, present tense, about the **operational** problem — not the missing system.

> ✗ "There is no dashboard for scrap."
> ✓ "Scrap and waste data is reported inaccurately, so the shift cannot tell which of three
> lines is losing material until the monthly close."

**The test:** if the sentence names a technology, it is a solution, not a problem. Rewrite it.

### §3 · Use Case Target Overview

What will be true when this is delivered. One paragraph, and it must name **who acts on it
and when**.

> "Automated SPC chart for shot weight of blow-moulded parts, read by engineers and fitters
> at the daily Gemba, so an out-of-tolerance trend is caught within one shift instead of at
> the weekly review."

The existing corpus writes the first half well and omits the second. **The moment in the day
is what decides whether the asset gets opened** — 8 delivered use cases record utilization
`NEVER`.

### §4 · Standard baseline

```
Cluster:               ⟨C01…C12⟩
Standard KPIs:         ⟨from the cluster's KPI set⟩
Requirements checklist: ⟨adopted / adopted with deltas / not applicable — say which⟩
Public data model:     ⟨EUROMAP 77/83/84 · OPC UA for Machinery · PackML · none⟩
Deltas from standard:  ⟨only what this plant does differently⟩
```

**Start from the checklist, record only deltas.** That is the mechanism by which a use case
with no local notes still gets built to a standard — see `od-use-case-standardization` and
the signal skill's `standards.md`.

### §5 · Tags of Interest — the signal requirement

The section 29 use cases already write, and the one that most often decides whether the
thing can be built at all.

| Signal (canonical name) | Direction | Source | Exists? | Unit | Collection |
|---|---|---|---|---|---|
| `MachineStatus` | in | PLC / edge | yes ⟨uuid⟩ | state | transition |
| `CycleTime` | out | derived | **no — to register** | s | per cycle |

- **Canonical names only** — `od-signal-standardization` §Step 5.
- **Direction**: `in` (consumed) or `out` (produced by this use case).
- **Exists?** is a fact to verify, not an assumption — `od-data-availability-check`.
- An `out` signal **must be registered on the edge platform** before anything publishes it.

### §6 · Acceptance criteria

Testable statements. 13 use cases already write these; they are the ones that can be
accepted without argument.

```
AC-1  Given ⟨state⟩, when ⟨trigger⟩, then ⟨observable result⟩.
AC-2  The value matches ⟨reference⟩ within ⟨tolerance⟩ over ⟨period⟩.
AC-3  ⟨named plant role⟩ has used it in a real shift, not a demonstration.
```

**AC-3 or its equivalent is mandatory.** It is the department's own handover rule, and
without it "delivered" and "in use" get conflated — the gap between `IMPLEMENTED` (129) and
`PRODUCTIVE` (167) is what that conflation costs.

### §7 · Blocking points

Split as the estate already splits them:

```
Major blocking points:  ⟨stops delivery — owner, class, expected resolution⟩
Minor blocking points:  ⟨slows delivery — owner⟩
```

Classes seen in the corpus, and each has a different owner:

| Class | Example from the estate | Route to |
|---|---|---|
| Machine connectivity | "currently no machine connectivity" | `od-equipment-integration` (guidance route) |
| Hardware not installed | "camera system currently not integrated"; "printers will be installed during 2022" | Investment / plant |
| External system access | "open access to ⟨vendor⟩ system (API)" | IT demand management |
| Method undefined | "check current calculation method" | This requirement — resolve it here |
| Parameter selection open | "investigation and selection of process parameter to be connected" | This requirement — resolve it here |
| Software not deployed | "Node-RED needs to be installed (with OPC nodes)" | Rollout |

**Two of those six are the requirement's own job.** "Method undefined" and "parameter
selection open" are not blockers to escalate — they are the work.

### §8 · System fit

```
Systems required:   ⟨list⟩
Inside the lean footprint?  ⟨yes / no — and if no, refuse or escalate⟩
Legacy applications touched: ⟨from the Legacy Application list⟩
```

See [`legacy-system-assessment.md`](legacy-system-assessment.md). A requirement needing a
system outside the standard footprint is refused at intake, not discovered at build.

### §9 · Value

```
Benefit type:  savings / lead-time / cost avoidance
Figure:        ⟨amount⟩ ⟨year⟩   Reliability: CALCULATION | ESTIMATION | not yet assessed
Methodology:   ⟨the formula, if CALCULATION⟩
Dependency:    ⟨what the money waits on⟩
```

Never a figure without its reliability label — `od-benefit-calculation`. "Not yet assessed"
is an honest value; an invented number is not.

### §10 · Traces to

```
Traces to:  ⟨plant roadmap item⟩ · ⟨capability⟩ · ⟨library entry if taken⟩ · ⟨business process⟩
```

The section 13 use cases already write. Without a roadmap link the request fails intake.

---

## Lane variants — what each adds

The core is shared. Each lane adds the section its own definition of done needs.

### Use Case Support — the integration-ready spec (UC-03)

**Adds §11 · Handover packet to Information Integration.** This is the artefact that crosses
the lane boundary, and the reason this whole skill exists:

```
Machines + EQ ids, with current integration status
Signals required, canonical names, in/out, with existence verdict per signal
Data path expected:  machine → ingress variant → edge → offload → asset
Output data points to register  ⟨uuid to be issued⟩
Acceptance criteria the integration must satisfy (subset of §6)
Known barriers already classified (§7)
Business case reference (§9)
```

**Nothing crosses the boundary without this.** An integration request without a signal list
and an acceptance criterion is a conversation, not a work item.

### Information Integration — the machine requirement

**Adds §11 · Equipment requirement**, aligned to the **PRS — Requirement Specification for
Machines & Equipment** (Doc ID 215534) where the machine is being purchased or modified:

```
PLC vendor / model / part number        ⟨joins the Machine List⟩
Network protocol and interfaces
Ingress variant:  ① edge device · ② connector · ③ aggregation server
Connector / driver
PLC program available?   ★ the breakpoint — without it, no connection
Tag export available?
Companion specification exposed?  ⟨OPC UA for Machinery · EUROMAP · none⟩
Cyber Security / OT sign-off:  ⟨required? requested? granted?⟩
Signal standard to apply, and the data model
```

**Ask for the companion specification at purchase.** A machine shipping one needs no PLC
program and no tag export — the single largest cost difference available.

### Project Support & Application Consultancy — the scope baseline

**Adds §11 · Project scope baseline** (PS-01's output):

```
Stage / gate:      Captured → Evaluated → Assessed → Planned → Handed over → Effective
Investment:        ⟨planned figure⟩ ⟨eCR route: CTO ≤150k · Board >75k⟩
Milestones with acceptance points
Resources:         ⟨named, per side⟩
Dependencies:      ⟨other projects, external decisions, licences⟩
Training + competence requirement   ⟨who must be able to run it afterwards⟩
Flow owner:        ⟨named — the end-to-end chain has none today⟩
```

**The training line is not optional here.** Adoption is what this lane is accountable for,
and a solution nobody was trained on is the `IMPLEMENTED`-but-not-`PRODUCTIVE` gap.

### Analytical Support — the scoped request

**Adds §11 · Request scope** (AS-01's output), and it is deliberately the lightest:

```
Question:            ⟨the actual question, in one sentence⟩
Decision it supports: ⟨what changes depending on the answer⟩
Data availability verdict:  available / gap ⟨named⟩ / partial ⟨what can be answered⟩
Turnaround expected
One-off or recurring?   ← decides ad-hoc vs promotion to a standard use case
```

**"One-off or recurring" is the whole lane's hinge.** A one-off insight with no recurring
value is closed as ad-hoc and deliberately *not* industrialized. Getting that wrong in
either direction is this lane's characteristic failure.

---

## What a finished requirement is not

- **Not a solution design.** It says what must be true, not which nodes to wire.
- **Not a project plan.** Milestones belong to the Project Support variant only.
- **Not a place for invented figures.** `⟨to confirm⟩` is a legitimate value everywhere.
