---
type: Skill Reference
title: Investment checking workflow
description: "The department's investment-checking workflow (invest-screen): screen the whole list, footprint gate, scored gate, region-grouped verdicts, read-only autonomy."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [invest-screen, workflow, department-package]
derived_from:
  - "Department knowledge base, OD Department Knowledge/OD-instance/30-skills/investment-checking.zip/SKILL.md, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `investment-checking.zip/SKILL.md` (the master).

# Investment Checking (OD involvement screen + decision gate)

Screen the **entire** MPEE Invest & Cost Planning list — not only the rows OD owns — and surface **every investment where Operations Digitalization is, or should be, involved**. Then put each involved item through a scored decision gate that ends in a clear verdict, and a mandatory software / IT-footprint gate.

Two failure modes this skill exists to prevent:
1. **Silent involvement** — an equipment, IT, energy or facility purchase quietly drags in software, endpoints, a PC, a framework or a connector that OD ends up owning, integrating or securing, but OD was never asked (the "Lessmüller laser controller needs a PC running an unknown framework and exposes an FTP endpoint" case).
2. **Unhealthy scale-out** — OD-owned or OD-touching items that add operational footprint without a healthy business case, that don't compound across the organisation, or that should be proven as a PoC first before an org-wide commitment.

> **Language:** all written output (report, tables, review files) in **English**, per `OD-instance/CLAUDE.md`. German is fine only when talking to the user in chat.

---

## Bundled references — read on demand

This skill ships a `` folder. Read the relevant file when you reach that step; don't reproduce it from memory.

- **`screening-method.md`** — where the list lives, how to pull it, the involvement lexicon (signal words), and the filter/scan recipe. Start here.
- **`decision-criteria.md`** — the six scored criteria, the 0–2 scoring rubric, and the score → verdict mapping.
- **`software-footprint-gate.md`** — the mandatory hidden-software / IT-footprint gate (the blocking gate) with its checklist. Applies to **direct and indirect** purchases.
- **`department-questions.md`** — the question set OD raises per involved item, grouped by concern.
- **`review-template.md`** — the per-item review block + a worked example, and the report skeleton.

If a reference file is missing, the essentials are reproduced inline below so the skill still runs standalone.

---

## The principle in four sentences

1. OD's job at investment intake is **not to approve spend** — it is to detect involvement early, protect a lean/standardised footprint, and make the digitalisation consequences of a purchase visible before the eCR is launched.
2. **Involvement is wider than ownership.** OD is involved whenever an item produces data, needs connectivity, ships software/endpoints, touches the shopfloor network/OT, or overlaps a running OD platform (the data platform, IIoT Edge, MSB, MES pilots) — regardless of which department owns the row.
3. Every involved item gets a **visible verdict** (Go / PoC-first / Reduce-complexity / Hold / Reject) built from a transparent score, never a black-box yes/no.
4. The **software / IT-footprint gate is a hard gate**: an item that drags in unmanaged software, PCs, frameworks, licenses or competing endpoints cannot be "Go" until that footprint is named, owned and cleared by Cyber Security — no matter how good the business case.

---

## Scope: check ALL investments

Run against the whole list, then classify each row into one of:

- **OD-owned** — Department = `OPERATION DIGITALIZATION`. Always in scope.
- **OD-touching** — any department, but the item produces/consumes data, needs connectivity, ships or requires software, touches OT/shopfloor network, or overlaps an OD platform. Detect via the involvement lexicon in `screening-method.md`. **This is where OD is usually missed.**
- **Cross-region interlock** — Energy / Facility & Green Operations, Manufacturing Engineering or IT items in the regions that are technologically woven together with OD (e.g. an energy-metering or ME automation project that will need the data platform/IIoT Edge/MSB, or that stands up its own parallel data path). Flag for co-ownership, not just review.
- **Not involved** — no data/software/connectivity/OT signal. Record the count, drop from the working set.

Reason the classification out loud (show the signal that triggered it). Do not silently downgrade an item to "not involved".

---

## Workflow

0. **Pull the current list.** Follow `screening-method.md`. Never copy the list into a repo register — link to it; the live list is the single source of truth. Note the snapshot date of whatever export you used and state it in the output.
1. **Classify every row** into OD-owned / OD-touching / cross-region interlock / not-involved using the involvement lexicon. Keep the reasoning visible.
2. **For each involved item, run the software / IT-footprint gate** (`software-footprint-gate.md`) first. If it trips and is unresolved, the item is **Blocked** until named/owned/cleared — capture the open question, don't compute a rosy verdict around it.
3. **Score the six criteria** (`decision-criteria.md`) and derive the verdict.
4. **Raise the department questions** (`department-questions.md`) for anything unresolved — these are what OD brings to the ODEC/COP/invest-review conversation.
5. **Write the output** using `review-template.md`, **grouped by region (`Cluster`)** — OD runs a separate controlling cycle per region, so this is the default cut. One section per region (EMEA WEST / EMEA EAST / AMERICAS / APAC / OESL), each with its OD-owned + OD-relevant tables and its own open questions; put cross-region themes (a capability bought plant-by-plant in several regions) above the regional sections. Save to the user's working folder; deliver the shortlist in chat.

Autonomy: this skill runs **read-only / recommend** (see `00-core/08-decision-rights.md`). It surfaces verdicts and questions; the go/no-go and any commitment stays with the OD lead and the item's owner.

---

## The six criteria (full rubric in `decision-criteria.md`)

Each scored 0 (fails) · 1 (partial / unclear) · 2 (clearly met). Criterion 6 is the **hard gate**, not a soft score.

1. **Healthy business case** — a nameable value (saving / lead-time / risk / mandatory), a roadmap link, a rough payback, and a kill criterion. No business case → not OD's to push.
2. **Compounding** — does the technology or use case compound across the organisation (reusable platform, standard signal model, repeatable use case) rather than a one-off island?
3. **Interface standardisation** — does it use, or can it be steered to, standardised interfaces (OPC UA / MQTT / MSB connectors, the data-platform path) instead of proprietary or ad-hoc endpoints (vendor FTP, bespoke DB dumps) that compete with internal connectors?
4. **Complexity load** — does it keep OD's footprint lean, or add operational burden and tool proliferation? Ask *what must be proven first* — prefer **PoC-first** over an org-wide commitment; consider complexity-reduction alternatives.
5. **Cross-region / tech interlock** — is it technologically woven with OD elsewhere (Energy/ME/IT), such that OD should co-own rather than just comment?
6. **Software / IT-footprint gate (HARD)** — pass only when every piece of software, PC, framework, license, endpoint and network touch is named, has an owner, and is cleared by Cyber Security. See the dedicated reference.

### Score → verdict

- Gate (6) tripped & unresolved → **Blocked** (resolve before any other verdict stands).
- Gate clear **and** total of criteria 1–5 ≥ 8 with none at 0 → **Go**.
- Value real but footprint/complexity high, or key unknowns remain → **PoC-first** (define the proof, scope it small).
- Workable but over-engineered / non-standard interfaces → **Reduce-complexity** (name the simpler path).
- Missing business case, blocked dependency, or off-strategy but not clearly dead → **Hold** (with the trigger to revisit).
- Off-strategy (hits a non-bet), no value, or duplicates a stopped initiative → **Reject** (state which non-bet / why).

Always show the six sub-scores and the one decisive reason. A verdict without its reasoning is not done.

---

## Anchor to OD strategy (so verdicts stay consistent)

Check each item against `00-core/02-strategy.md`:
- **Bets** it should reinforce: asset-to-cloud on the data platform (B1); Cyber Security + MSB bundle for strategic plants (B2); MES value only via the 2 pilots (B3).
- **Non-bets** that push toward Hold/Reject: no standardised MES rollout short/mid-term; EMS rollout stopped; OD does not build automation solutions or own energy/facility topics; no broad tool proliferation — footprint stays small.
- **Trade-offs**: prefer few systems / small footprint, and standardised modular deployments.

An item that quietly violates a non-bet (e.g. a new parallel MES-like control system, a fresh energy-data silo) is exactly what this screen must catch.

---

## Output conventions

- Written output in **English**, **grouped by region (`Cluster`)** by default to match OD's per-region controlling cycles. Save the report to the user's working folder and offer a `computer://` link; deliver the shortlist in chat.
- The report is a **dated snapshot / analysis**, not a register. Head it with the snapshot date and a link to the live Invest list; state that the list is the source of truth. Do **not** persist a row-by-row copy of the list into OD's repo registers/modules — that creates a stale second copy.
- Leave genuine unknowns explicitly open (⟨…⟩) — an honest open question is the deliverable, not a fabricated verdict.
- Reasoning always visible: every classification shows its trigger signal; every verdict shows its sub-scores and decisive reason.
