---
type: Skill Reference
title: Clustering signals
description: "Four axes for sorting a machine's hundreds of data points, the search patterns per cluster, and the importance score that ranks them."
resource: ../SKILL.md
status: stable
tags: [signals, clustering]
---
# Clustering input signals — search patterns and importance

A machine exposes hundreds of data points. Most use cases need a handful. This is how to
sort a raw signal list into functional areas, and how to decide which signals matter enough
to standardize first.

Both halves are **derived from the use-case portfolio**, not invented: the estate already
records, per use case, which capability template it hangs off, which cluster pattern it
follows, which business process consumes it, and what it targets. That is the demand signal.

---

## The four axes to cluster on

| Axis | Values | Where it comes from | Answers |
|---|---|---|---|
| **Functional area** | the capability templates | Capability node per use case | *What kind of signal is this?* |
| **Use-case pattern** | the AI clusters | `ai_cluster` per use case | *What will be built with it?* |
| **Consumer / department** | the business processes | `business_process` per use case | *Who expects it, and when?* |
| **Expectation** | the target types | `targets` per use case | *What must it be able to produce?* |

A signal that maps to none of the four is a candidate for *not standardizing at all* — see
importance below.

### Functional areas — the capability templates

`Andon Board` · `OEE Calculation` · `Downtime Reporting` · `Process Quality Data` ·
`Machine Alerts` · `Cycle Time` · `Recipe Values` · `Process Values` · `Manual Quality Data`
· `Analytics` · `Other Use Cases`

Every capability is instantiated at nearly every plant. **The template is never what
is missing** — so a signal that serves one is a signal the other plants can already use.

### Consumers — the business processes

Rank them by use-case count on the live use-case list; the counts change.

| Business process | Reads signals for |
|---|---|
| `DAILY GEMBA` | Current state at the line, now |
| `PROCESS IMPROVEMENT` | Series over time, comparable |
| `ACTIVITY TRACKING` | Counts and durations per period |
| `UTILIZATION IMPROVEMENT` | Availability, downtime reasons |
| `TROUBLESHOOTING` | High-resolution recent history |
| `QUALITY IMPROVEMENT` | Measured values against limits |
| `TRACEABILITY` | Identifiers bound to a time window |
| `ENERGY REPORTING` | Consumption normalized by output |

**The consumer decides the collection method, not just the signal.** `DAILY GEMBA` needs the
current value and tolerates a gap in history. `PROCESS IMPROVEMENT` needs an unbroken
comparable series and tolerates latency. Same signal name, two different contracts — and
this is exactly the fourth standardization element the data cannot show you.

### Expectations — the target types

`Process Values` · `SPC Charts` · `Image Data` · `Andon Board` · `Notification` ·
`Machine Availability` · `Manual Quality Data Input` · `Quality Losses` · `Manual Data Input` ·
`Cycle Time Monitoring` · `Energy Data` · `Process Set Values`

`Process Set Values` appearing separately from `Process Values` is the **setpoint/actual
distinction** the `_sv` topic suffix already encodes. Keep them apart.

---

## Search patterns — classifying an unknown signal

Apply in order; first match wins. These are the patterns behind the analyser's clustering,
and they were built from the names actually in use in the flow corpus.

| # | Functional area | Regex (case-insensitive) | Typical names |
|---|---|---|---|
| 1 | **Identification** | `tool.?id\|part.?numb\|recipe\|program.?id\|serial\|batch\|order` | `ToolId`, `Partnumber`, `RecipeId` |
| 2 | **Machine state** | `machine.?(mode\|state\|status)\|released\|setup\|automatic\|manual\|fault\|heartbeat` | `MachineStatus`, `MachineIsReleased` |
| 3 | **Cycle & timing** | `cycle\|(^\|[^a-z])time\|duration\|loading\|process.?time\|step.?chain` | `CycleStart`, `CycleTime` |
| 4 | **Counting & throughput** | `count\|counter\|produced\|output\|pieces\|pza\|parts\|volume\|shot\|per.?minute\|meters` | `TotalPartCounter` |
| 5 | **Quality & limits** | `toleran\|limit\|spec\|quality\|nok\|scrap\|reject\|failure\|evaluation\|deviation` | `HardUpperLimit`, `EvaluationResult` |
| 6 | **Alerting** | `alert\|alarm\|error\|fault.?text\|notification\|warn\|message` | `ErrorActive`, `AlertMessage` |
| 7 | **Energy** | `energy\|power\|kwh\|current\|voltage\|consumption\|air\|compressor` | `CompressorPressure1` |
| 8 | **Process values** | `pressure\|temp\|melt\|speed\|zone\|diameter\|vacuum\|screw\|head\|flow\|level\|torque\|position` | `MeltTemperature` |
| 9 | **Setpoint** *(modifier)* | `_sv$\|setpoint\|set.?pt\|target\|nominal\|sollwert` | `Diameter_sv` |
| 10 | **Raw / unclassified** | `^(_\|db\d\|dbw\|dbd\|dbx\|m\d\|%[imq]\|i\d+\.\d\|q\d+\.\d\|tag\d\|var\d)` | `_part0_io` — **blocker, not a class** |

**Order matters.** Identification runs before everything because `ToolIdChanging` contains
`Chang`, and machine state before timing because `MachineSetup` would otherwise fall to
neither. Setpoint is a **modifier**, not a class: `Diameter_sv` is a process value *and* a
setpoint, and losing the second half makes a dashboard compare a target with itself.

**A German-language pass is worth having.** The estate mixes languages — `Heizungsart`,
`Rüstmonitor`, `Sollwert`, `Stückzahl`. Add the terms for your plants; a signal that fails
to classify because it is German is not an unclassified signal.

---

## Importance patterns — what to standardize first

Not every signal deserves the effort. Score each one; standardize down the list.

### The score

| Factor | Weight | Rationale |
|---|--:|---|
| **Capability coverage** — how many of the capability templates need it | ×4 | A signal three capabilities need is three use cases unblocked |
| **Consumer demand** — use-case count of the business processes that read it | ×3 | a business process with many use cases (for example `DAILY GEMBA`) outranks one with few (for example `ENERGY REPORTING`) |
| **Cross-plant presence** — how many plants have the same machine or process group | ×3 | The whole point is the second plant taking the first plant's solution |
| **Blocking** — is a `PLANNED` use case waiting on it | ×2 | Demand already committed |
| **Standard exists** — a public data model already names it | ×2 | Adoption is cheaper than invention |
| **Derivation depth** — how many other signals depend on it | ×1 | A base signal fixes several derived ones |

### The shortcut that works without scoring anything

**The top of the list is always the same four, because they feed the most capabilities:**

| Signal | Feeds |
|---|---|
| `MachineStatus` | OEE, Downtime Reporting, Andon Board, Analytics |
| `TotalPartCounter` | OEE, Cycle Time, Analytics, Activity Tracking |
| `CycleStart` / `CycleEnd` | Cycle Time, OEE performance, Process Quality |
| `CurrentValue` + limits | Process Quality Data, SPC Charts, Machine Alerts |

Standardize those four families on a machine and most of the portfolio becomes buildable on
it. Everything else is a long tail worth doing per demand.

### What ranks low, deliberately

- **A signal no use case targets.** Real, but not urgent. Record the name, do not spend the
  meeting.
- **A signal on one machine at one plant with no sibling.** `Other Use Cases` is a legitimate
  capability; not everything scales.
- **A raw diagnostic tag** the maintenance team reads directly and no use case consumes.

**Not standardizing is a valid outcome** and should be recorded as a decision, not left as an
omission. The cost of standardizing everything is that nothing gets standardized well.

---

## Deriving the demand yourself

The clustering above came from the portfolio, and it can be re-derived per plant or process
group when the demand changes:

1. **Filter the use-case list** to the plant, process group or capability in question.
2. **Read across `ai_cluster`, `business_process` and `targets`** — those three say what
   will be built, who consumes it and what it must produce.
3. **Take the cluster's requirements checklist** from
   `standards.md` — that names the signals the standard needs.
4. **Intersect with what the machine exposes** — `analyze_signals.py --capability`.
5. **Rank the gap** by the score above.

**The caution the data itself demands:** `business_process` and `targets` are populated on only
part of the use cases (measure the fill rate live). So a demand ranking built from those fields
alone is built on part of the portfolio. Treat a low score as *unknown demand*, not *no demand* — and
absence is not a zero, which is `od-context`'s third honesty rule and applies here directly.
