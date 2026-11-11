---
type: Design Record
title: Phase1 elicitation
description: "Working file for the tacit-knowledge elicitation of phase 1: the questions put to the owner and the answers that resolved them; kept for traceability, not a skill."
status: draft
owner: human:jakob.gabriel
tags: [elicitation, working-file]
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Phase 1 — tacit knowledge elicitation

Working file, not part of the registry — outside `skills/` and `docs/` on purpose, same
reason the knowledge base keeps its own working notes outside `_knowledge/`: this is a plan/answer
draft, not a derived concept, and it isn't OKF-validated. Delete it (or move it somewhere
else) once each topic has been folded into its skill.

Fill in whatever you can, in any order, any depth — bullets, half-sentences and real
examples all work better than polished prose. I'll turn each answer into the reference file
named under its heading. Nothing you write here gets quoted verbatim into a `SKILL.md` with
plant names, prices or people attached where that would leak something private — I'll
generalize where needed, but tell me if something below is sensitive and should stay out of
the shared skill entirely.

---

## 1. Refusal in practice — RESOLVED 2026-10-22 (partially)
→ `skills/dept-intake/references/refusal-playbook.md`

Resolved from the department's own retrospective workshop record
(`Split Slides/10-Workshops--...`) instead of interview: three
real "looked legitimate but refused" patterns (cosmetic dashboard requests, a use case
riding on infrastructure not yet planned for that plant, an approval gate OD doesn't
control) and one "accepted something regretted" (difficult machines taken on first,
burning reputation). **Still open:** the exact pushback line a plant uses, and the answer
to it — not in the mined record; add directly if you have it.

---

## 2. Connectability judgement
→ `skills/mi-equipment/references/barrier-classes.md`

### What the estate already shows

Mined from `kg_nodes.csv` (1,715 machines) and the 26-row Connector Overview export, so you
are reacting to evidence rather than starting blank. Nothing below is a question of memory —
it's arithmetic over the recorded rows — so treat disagreements as either "the data is
wrong/stale" or "there's a reason invisible to the data," both of which are exactly the
judgement this reference needs.

**By PLC vendor — where the sample is large enough to mean something:**

| Vendor | Machines | % integrated | % not integrated | Note |
|---|--:|--:|--:|---|
| Schneider Electric | 32 | 100% | 0% | fully connected |
| B&R Industrial Automation | 30 | 97% | 3% | fully connected *despite* `DTQ-B&R-Connector` being `Idea · NOT AVAILABLE` in the connector list — solved another way |
| Rockwell/Allen-Bradley | 173 | 65% | 34% | |
| Bachmann Electronic | 30 | 67% | 33% | |
| Siemens | 673 | 60% | 34% | biggest fleet, middling rate |
| **Beckhoff** | 39 | **44%** | **56%** | has a `Productive · USE` edge connector (`DTQ-Beckhoff-Connector`, ADS), but the Central Aggregation Server has **no Beckhoff/ADS driver at all** — so a Beckhoff machine behind the wrong platform concept has no route regardless of the edge connector existing |
| **Mitsubishi Electric** | 11 | **27%** | **73%** | no dedicated connector in the 26-row list |
| **Delta Electronic** | 14 | **0%** | **100%** | no dedicated connector in the 26-row list — every single one is stuck |
| **Philips** | 9 | **0%** | **100%** | same — no connector exists |

**By protocol:**

| Protocol | Machines | % integrated | % not integrated |
|---|--:|--:|--:|
| Modbus / TCP | 79 | **99%** | 0% |
| PROFINET | 308 | 68% | 26% |
| Ethernet/IP | 165 | 67% | 33% |
| TCP/IP | 218 | 66% | 34% |
| EtherCAT | 43 | 56% | 44% |
| MPI | 27 | 33% | 41% |
| **PROFIBUS** | 50 | **22%** | **68%** | worst-performing protocol with a real sample size |

**A genuine contradiction worth your read on:** `DTQ-MODBUS-Connector` is still `Idea`
status — not built — yet Modbus/TCP machines are 99% integrated (78 of 79). Looking at the
individual rows, most of those go through `Central OPCUA Aggregation Server`, not an edge
connector at all. So the working hypothesis is: **Modbus is solved at the aggregation-server
platform, and the still-missing edge connector only matters for a plant running the edge
concept instead.** Is that right, or is something else going on?

**Named, recurring blockers** — free text in 125 of 1,715 rows (only 7.3% populated, so this
under-counts, but the pattern is real):

| Blocker (as recorded) | Count |
|---|--:|
| Data-model standardization (CT Base) | 23 |
| Firmware patching required for cyber security before integration | 13 + 5 (two separate entries, same theme) |
| TIA Portal V16 → V17 upgrade required (Karben) | 12 |
| Robot signals reachable via the parent PLC — no dedicated robot integration | 5 |
| A second edge device needed alongside a camera | 5 |

**Connector-catalogue facts with real numbers attached**, from the Connector Overview
comments — these read like your own prior estimates, not generic vendor claims:

- `DTQ-RS232-Connector` (currently serves one Keyence gauge at Monterrey) needs an
  enhancement to reach the Edge Platform, priced at **~€5,000**.
- `DTQ-PIOVAN-Connector` — development idea for Somersworth/Waltershausen, **~€10,000**.
- `DTQ-ZWICK-Connector` — `Idea · NOT AVAILABLE` for Waltershausen I/II, **~€10,000**.
- `SFT-SIMATIC S7-Connector` is `Productive` but flagged **`DO NOT USE`** — not cloud-native,
  and does not support cyber-security-compliant PLC communication. It looks available and
  is explicitly forbidden — the one entry in the whole catalogue with that shape.
- `DTQ-B&R-Connector`, `DTQ-Bachmann-Connector`, `DTQ-Engel EMI-Connector` — `Idea · NOT
  AVAILABLE`, no price yet, despite B&R and Bachmann machines already being mostly connected
  through the aggregation route (see table above).
- `DTQ-SMB-Connector`, `DTQ-SmartKlaus-Connector` — `Development`, each tied to a named eCR.

**Where the unconnected backlog actually sits:** Subotica (142 not-integrated machines),
Changshu (78), Monterrey (56) — three plants carry more than half of the estate's
not-integrated count between them.

**A data-quality flag, not a connectability fact:** 191 machines are marked `INTEGRATED`
with no `integration_method` recorded at all (mostly Rockwell, Schneider, Engel, on Modbus/TCP
or TCP/IP) — their actual route can't be read off the row. Don't let this read as its own
barrier class; it's a recording gap.

### Questions for you

- Does the vendor/protocol ranking above match your gut read of "cheap, expensive, or not
  happening," or is the data hiding something the numbers can't show (e.g. Beckhoff being
  worse than raw connector availability suggests)?
- Resolve the Modbus contradiction above — is the aggregation-route hypothesis right?
- Before opening the equipment-integration-guide app, what do *you* glance at on a real
  machine/PLC that already tells you the tier, that isn't in this data (e.g. panel age,
  network cabinet state, whether the plant IT contact answers emails)?
- Any vendor/generation you'd add a "don't bother, or budget 5×" rule for for that isn't
  already obvious from the 0%/100% rows above?
- Rank the named blockers (data-model standardization, cyber-security patching, TIA
  version) by how often they're actually the real reason vs. a symptom of something else.

**Your answer:**

—

---

## 3. Benefit-calculation review — RESOLVED 2026-10-22 (partially)
→ `skills/bc-build/references/review-checklist.md`

Resolved from the department's own retrospective workshop record instead of interview:
why the methodology field is usually the one missing (plants avoid self-originating a
number they aren't confident in), the three fixes tried before the current one (library →
workshop slot → proactive calculator), and the smell test that follows (distrust a row
with no calculator trace behind it). **Still open:** the specific recurring reason a
*particular* row gets challenged at the SPRINT gate itself — not in the mined record; add
directly if you have it.

---

## 4. ODEC vs. COP in practice — RESOLVED 2026-10-22
→ `skills/dept-decision-rights/references/escalation-worked-examples.md`

Resolved from the department's own ODEC/CoP call decks (`Split
Slides/`) instead of interview — the Groot2B cybersecurity item split cleanly into a
strategic ODEC half and a technical COP half, a platform-access blocker that stayed at COP
without ever reaching ODEC, and the eCR Calculator as a cross-plant pattern raised at ODEC
whose actual execution stays per-plant at COP. See the reference file for the full
write-up and citations.

---

## 5. Non-bet system-fit judgement — RESOLVED 2026-10-22 (partially)
→ `skills/invest-screen/` (built)

Resolved from the department's own tool catalogue and per-plant Smart Factory Tool
Availability snapshots instead of interview: the tell (walk each lightweight tool's own
"is not" boundary — QFPR, MDA/PDA, MIL, Camline, WiriTec — none covering the need means
MES/EMS-shaped) and what you do once caught (redesign onto the lighter tool, or escalate
via `dept-decision-rights`'s tool/system-rollout gate). Also surfaced a live discrepancy the
mined record itself contains: the written non-bets say EMS rollout is stopped, while a
January 2025 deck shows WiriTec mostly rolled out — flagged, not resolved either way.
**Still open:** 2-3 *named, real* requests that looked like a normal ask but secretly
needed MES/MIL/EMS — the skill's worked example is illustrative, not a real case; add a
real one directly if you have one.

---

*I can run the same kind of data-mining pass for topics 3 and 5 if there's a comparable
source — e.g. the `UseCase-SavingCalculation` list for topic 3, or scanning use-case
`target_text` for MES/MIL/EMS-adjacent language for topic 5. Say the word and I'll pull it
before you write those answers.*

---

## 6. Internal Communications handover (Lane 4) — OPEN
→ `skills/comms-brief/references/ic-handover.md`

The owner asked for an outbound lane that promotes live, adopted use cases through Internal Communications. The knowledge base holds no description of the Internal Communications process (it records only that the role exists, central, in HR and Communications), so the skill leaves its details open. OD's own January 2026 marketing-template initiative (appetizer template, testimonial, story shapes) is now the basis of the formats in `comms-brief`. **To be supplied by the owner (the Internal Communications brief):** the intake channel or role, the channels per audience (plants and key users, BA Operations leadership, all employees, OPEX and PPI/ME), the lead time, any IC template or review route that replaces `comms-brief.md`, brand and tone rules, a second approval or language, and what reach or response data IC returns.

**Your answer:**

—
