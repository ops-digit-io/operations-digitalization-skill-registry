---
type: Skill Reference
title: Savings model
description: "The savings model: lever types, formulas and drivers, ranges, and how each saving is made auditable."
resource: ../SKILL.md
status: draft
tags: [business-case, value-model, department-package]
---
> Transcribed from the department package `product-funnel-skills.zip/skills/business-case/references/savings-model.md` (the master).

# Savings Model

How to build a value model that survives a sceptical room.

## The four-column discipline

| Lever | Measured by the solution | Scenario assumption | Annual value |
|-------|--------------------------|--------------------|--------------|

The split between columns 2 and 3 is the whole design. Column 2 is evidence the
system produces; column 3 is a judgement the user is choosing to make. Keeping
them apart means a challenger attacks the assumption, not the measurement — and
that is a productive argument, because the assumption is adjustable and the
measurement is not.

Collapse the columns and every number becomes equally suspect, including the
ones that were solid.

## Picking levers

A lever is a **mechanism**, not a benefit. "Better visibility" is not a lever;
"fewer hours spent reconstructing what happened last shift" is.

Three or four. Each should be independent — if two levers can double-count the
same hour, merge them or state the boundary explicitly. Double counting is the
most common way a model gets destroyed in the room, and it is usually
unintentional.

Common lever shapes:

| Shape | Mechanism | Watch out for |
|-------|-----------|---------------|
| **Time recovery** | Work that takes less time, or stops being redone | Is the freed time actually redeployed, or just less busy? |
| **Reaction time** | A problem detected earlier costs less | Needs a stop/event count and a per-event cost |
| **Containment** | Defects caught before more are produced | Value is pieces-not-scrapped, needs a scrap cost |
| **Throughput** | More output from the same asset | **Worthless unless the output sells** — see below |
| **Avoided cost** | A purchase, hire, or licence not needed | The strongest lever when it is real; verify it was actually planned |

## The throughput trap

Throughput gains are the most commonly overstated line in any business case.

Extra capacity is worth money **only if the extra units can be sold**. If the
line is not capacity-constrained, a ⟨x⟩% throughput gain produces zero revenue —
it produces idle time. Ask directly: *is this line sold out?*

If it is not, count the value as hours released and label it that way. A
capacity manager who spots phantom revenue will discount everything else on the
slide, and they will be right to.

## Ranges, not points

Every assumption gets a range and a chosen midpoint:

> Close ⟨x⟩% of the gap (range ⟨low⟩–⟨high⟩%)

Compute the headline at the midpoint, and state what the low end still yields. A
case that works at its pessimistic end is far more persuasive than one that only
works at its optimistic one — and a reader who wants to argue will argue about
the range rather than the whole model.

## Show the arithmetic

Write the calculation in the cell:

```
⟨runs⟩ runs/yr × ⟨h per run⟩ h × ⟨share⟩ = ⟨hours⟩ h/yr × €⟨rate⟩/h = €⟨amount⟩
```

Not `€⟨amount⟩`. The reader must be able to follow it across the page and
substitute their own rate. That substitutability is what turns a slide into a
working conversation.

## Payback

```
payback (weeks) = build and rollout effort / (annual value / 52)
```

State effort as a number of days or weeks, sourced from the feature book's tiers
where possible. If the MVP is what was prototyped, the effort for the MVP is the
honest number to use — not the effort for the full v3 vision.

## Worked example

**Solution:** cell layout tool. **Baseline** from the as-is map: 20 relayouts a
year, ⟨h⟩ hours each, ⟨share⟩ revised after installation.
**Inputs supplied by the user:** engineer loaded rate €⟨rate⟩/h; rework costs ⟨h⟩ h
per occurrence; line not capacity-constrained.

| Lever | Measured by the solution | Scenario assumption | Annual value |
|-------|--------------------------|--------------------|--------------|
| Layout iteration time | Hours per relayout, as-is baseline ⟨h⟩ h vs tool-assisted | Cut concept phase by ⟨share⟩ (range ⟨low⟩–⟨high⟩) | ⟨n⟩ × ⟨h⟩ × ⟨share⟩ = ⟨hours⟩ h/yr × €⟨rate⟩ = **€⟨amount⟩** |
| Rework avoided | Relayouts revised post-install, baseline ⟨share⟩ | Evidence-based selection cuts revisions by ⟨share⟩ (range ⟨low⟩–⟨high⟩) | ⟨n⟩ × ⟨h⟩ × ⟨share⟩ = ⟨hours⟩ h/yr × €⟨rate⟩ = **€⟨amount⟩** |
| Space released | Footprint per concept, computed | ⟨share⟩ floor area released, re-used not sold | **Not priced** — hours and m² only |

**Total: ~€⟨midpoint⟩/yr at midpoint; ~€⟨pessimistic⟩ at the pessimistic end.**
**Payback:** ⟨build days⟩ days build ÷ (€⟨annual⟩ ÷ 52) ≈ ⟨days⟩ days of value ≈ ⟨weeks⟩ weeks.

Note what the third lever does. Floor space is real, the user could not price
it, and it is reported unpriced rather than given an invented €/m². That row
costs nothing in credibility and gains a lot — it shows the model declining to
inflate itself, which is exactly the signal a sceptical reader is looking for.

## What not to do

- Never blend soft benefits ("better decisions", "improved morale") into the
  arithmetic. List them separately and unpriced.
- Never use an industry-average rate the user did not confirm.
- Never present the optimistic end as the headline.
- Never count the same hour under two levers.
- Never quote a payback that uses v3's value against the MVP's effort.
