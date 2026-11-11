---
type: Skill Reference
title: Use case input questionnaire
description: "Interview guide and record template (sections A-L) that captures a use case well enough to assess its business case; every quantitative field gets value, confidence and source."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [business-case, intake, template, department-package]
derived_from:
  - "Department knowledge base, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `../BC-Assessment-Skill/use-case-input-questionnaire.md` (the master).

# Use-Case Input Questionnaire (Current-State → Business-Case Intake)

Reusable interview guide **and** record template for capturing a digitalization use case well enough to assess its business case. Designed to feed the **BC Assessment skill** (and, for the cost side, the **Use Case Cost Estimation skill**). Works for any use case, not only the Gemba app.

**How to use it.** Walk the interviewee through Sections A–L in order. Ask the open question first, then capture the number. For every quantitative field, record three things: **value**, **confidence** (`measured` / `estimated` / `guess`), and **source** (where it could be verified). Leave a field blank rather than inventing a number — blanks become the skill's "missing to close the case" list. A section is "green" only when its quantitative fields have at least an `estimated`-confidence value with a named source.

**Design rule mirrored from the skill:** we are not asking the plant to *defend a number they don't trust* — we are asking them to describe reality (steps, times, counts). The arithmetic and the range are the skill's job, built transparently on these inputs.

---

## A. Use-case identity & type

- A1. Use-case name and one-sentence description.
- A2. Which OD lane / area (Use Case Development, Applications in Manufacturing, Machine Integration)?
- A3. Use-case **type** (pick the closest — drives which levers apply):
  documentation/record digitization · escalation & reaction · analytics/monitoring dashboard · workflow automation · data integration · other.
- A4. Who owns it in the plant, and who is the process expert being interviewed? Are other roles needed to complete the picture?

## B. Current-state process ("as-is")

Capture the process as a sequence, so the before/after view can be drawn.

- B1. Walk through the process step by step: for each step — **who** does it, **what** they do, **on what trigger/cadence**.
- B2. Where are the **handoffs** between people/roles/systems?
- B3. Where are the **media breaks** (paper → board → Excel → terminal → system)? List each transcription/re-entry.
- B4. Where does information **wait** (queues, "someone passes by every N hours", approvals)?
- B5. What are the current **failure modes** (not updated, not seen, lost, delayed)?
- B6. What records are kept today, and how (paper, whiteboard, Excel, system)?

## C. Volume & scaling drivers (the multipliers)

These are what every saving gets multiplied by — capture counts even if approximate.

- C1. Scaling **unit** — is this per machine / per line or cell / per process instance / per shift / per plant?
- C2. How many of that unit exist **in this plant**? (e.g. lines, cells, machines involved)
- C3. How many **shifts/day** and **days/week** does the process run?
- C4. How many **people** perform the manual work, and in what roles?
- C5. Across the organization: how many plants run this process, and how many are **on paper/whiteboard vs. partially/fully digital**? (needed for scale-out)

## D. Pain quantification (the hard-saving inputs)

The heart of the ROI floor. Force a figure + confidence + source for each relevant item.

- D1. **Time per task** — how many minutes does each manual step take (transcription, manual KPI calculation, copying between formats)? Per occurrence.
- D2. **Frequency** — how often does each occur (per shift / per hour / per day)?
- D3. **Reaction latency today** — average time from event → detection → action (e.g. the "1–2 hours until someone checks the board").
- D4. **Cost of delay** — what does an avoided hour of that latency save (downtime €/h, scrap generated during undetected drift, overtime)?
- D5. **Error / rework / scrap** — current magnitude attributable to the manual process (rough % or units), if any.
- D6. **Loaded labor rate (€/h)** for the roles in C4 — needed to monetize D1–D3. (May be filled by OD/controlling, not the interviewee.)

## E. Target state & delta ("to-be")

- E1. Describe the target process step by step (what the tool/app does).
- E2. For each current manual step in B/D: is it **eliminated, reduced, or accelerated** — and by roughly how much (%)? (Rarely 100% — capture the realistic share.)
- E3. What new capability appears that did not exist (live data, automatic escalation, mobile access, cross-plant sharing)?
- E4. What is the residual manual effort **after** implementation?

## F. Operating model / adoption (the precondition)

Same tool, different routine → different value. Pin this down.

- F1. How exactly will it be **used** day to day? (e.g. "displayed on a screen" vs. "reviewed in a daily reaction routine with decisions and owners")
- F2. What routine/behavior must exist for the value to materialize (who acts on the signal, within what time)?
- F3. What happens to the value if that routine is **not** adopted? (This bounds the optional value.)

## G. Value tagging — hard vs. optional

For each effect identified, tag it so the skill keeps them separate.

- G1. **Hard / directly attributable** (carries the ROI): manual effort removed, media breaks eliminated, records no longer re-keyed.
- G2. **Optional / perspective value** (reported alongside, conditional): faster escalation → fewer defects, cycle-time stabilization, scrap reduction, cross-plant learning, engineering feedback.
- G3. For each optional item, name the **condition** under which it is realized (links to Section F).

## H. Scaling & transferability

- H1. Does this scale **within the same process** only, across **every line/cell** in the plant, across **every plant**, or across the **whole process chain**? Why?
- H2. The scale-out multiplier (unit × count from Section C, per plant and org-wide).
- H3. **Transferability preconditions** — what must be true for another plant to realize it (digital infra present, paper baseline to replace, the operating routine of F)?
- H4. **Limits of transferability** — where it does *not* transfer, and why.

## I. Baseline definition (the reference for savings)

- I1. What is the **baseline** the saving is measured against — a representative paper/whiteboard plant, or the current mixed state?
- I2. How are **already-digitalized** plants treated (excluded, or credited only for the remaining delta)?
- I3. State the baseline explicitly so per-plant numbers stay comparable and scale-out isn't overstated.

## J. Data sources & confidence

- J1. For each number above, where can it be **validated** (MES, an existing digital system, a time study, controlling)?
- J2. Which figures are `measured` vs. `estimated` vs. `guess`?
- J3. Is there existing data to pull instead of relying on recall? (e.g. tracked resolution times from a plant already digital)

## K. Cost inputs (pointer — handoff to the Cost Estimation skill)

Not costed here, but flag so the handoff isn't dropped:

- K1. Rough one-time build effort (OD + key-user involvement).
- K2. Licenses / infrastructure / hosting.
- K3. Recurring run-cost (operate, maintain, support), and rollout/onboarding effort per additional plant.

## L. Completeness self-check (the maturity gate)

Before handing to the BC skill, confirm:

- [ ] Current-state process and handoffs/media breaks captured (B).
- [ ] At least `estimated`-confidence values for time, frequency, volume, and labor rate (C, D).
- [ ] Target-state delta with realistic elimination/reduction shares (E).
- [ ] Operating model / adoption routine stated as an assumption (F).
- [ ] Effects tagged hard vs. optional, with conditions (G).
- [ ] Scaling unit, multiplier, preconditions and limits (H).
- [ ] Baseline rule stated explicitly (I).
- [ ] Data sources/confidence noted for each figure (J).
- [ ] Cost inputs at least pointed to (K).

**If any quantitative box is unchecked:** the BC skill should not publish a single ROI number — it should output the structured case plus this list of gaps, and a second short round should close them.

---

### Notes for the interviewer

- Ask open, then confirm — don't hand the interviewee the number you expect.
- Close every topic with: *"What figure would you put on this, and how confident are you?"*
- One number with a stated source beats three decimals with none.
- Prefer interviewing a **paper/whiteboard site** for baseline effort figures; pull data from an already-digital site to validate the target state.
