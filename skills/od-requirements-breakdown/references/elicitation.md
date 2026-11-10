---
type: Skill Reference
title: Elicitation
description: The question rounds that get the real problem out, and the five judgement calls the department names as the hard part.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [requirements, elicitation]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Elicitation — getting from a stated problem to a requirement

This is the part the map calls *"the step most dependent on tacit judgement"*. It is a
question set, in an order that works, plus the things people reliably leave out.

**Run it as a conversation, not a form.** The plant knows the problem; you know what a
requirement needs. Both halves are necessary and neither is sufficient.

---

## What the portfolio proves people leave out

Field population across the use case list is what happens when a requirement is *not*
elicited. Re-measure it on the live list (share of rows with the field filled) when you need
a figure; the pattern below is stable:

| Field | Typical population | What is missing |
|---|---|---|
| `savings_eur` | Always filled | — the number is always demanded |
| `category` | Almost always filled | — |
| `target_text` | Mostly filled | |
| `priority`, `potential` | About half or less | |
| `output_asset` | Often blank | **What form the deliverable takes** |
| `blockers` | Often blank | **What stops it** |
| `description` | Often blank | |
| `business_process` | Often blank | **Who consumes it, and when** |
| `targets` | Rarely filled | **What it must be able to produce** |
| `comment` · `methods` · `actions` · `utilization` · `csp_decision` | Hardly ever filled | **How, and whether anyone used it** |

**The pattern is unambiguous.** What gets asked for in a meeting — a number, a category, a
title — is populated. What requires a conversation with the operator is not.

So: **the questions below are ordered to get the rarely filled fields first**, while the person
is still in the room. The savings figure will get filled in whatever you do.

---

## Round 1 — the problem (before any solution talk)

1. **What goes wrong today, and how do you find out?** — Listen for the detection delay.
   That delay is usually the real requirement.
2. **Who notices first, and what do they do?** — Names the actor and the current workaround.
3. **How often does it happen, and what does it cost when it does?** — Feeds §9 without
   asking for a number.
4. **What have you tried?** — Surfaces the local point-tool that will otherwise be
   rediscovered at build.
5. **If nothing changes, what happens?** — Separates a real problem from a preference.

> **Refuse to move on while the answer names a technology.** "We need a dashboard" is not an
> answer to question 1. Ask again: *what goes wrong today?*

## Round 2 — the moment (the `business_process` field)

6. **When would somebody look at this?** — Daily Gemba · shift check · escalation · weekly
   review · only when something breaks.
7. **What decision follows?** — If none, this is reporting, not a use case. Say so.
8. **What do they do now, at that moment, instead?**

> This round produces `business_process` and the second half of §3. **Where utilization is
> recorded, the use cases used daily are the ones attached to the daily Gemba — the moment.** A
> use case attached to no moment is the one that ends up recorded as `NEVER`.

## Round 3 — the signals (the section that decides feasibility)

9. **What does the machine already tell you?** — Then verify it rather than believing it:
   `od-data-availability-check`.
10. **Which values would you need to see to make that decision?** — In their words; you map
    to canonical names afterwards.
11. **Is any of it written down by hand today?** — Manual entry is a valid input and a
    legitimate first version.
12. **How current does it need to be?** — Live at the line, this shift, or by tomorrow. This
    is the collection-method requirement and nothing else asks for it.

> Map their words to canonical names **after** the conversation, not during. "The counter" is
> a fine answer; `TotalPartCounter` is your job.

## Round 4 — done (the `methods` / `utilization` fields)

13. **How will you know it works?** — Push until it is testable. "It's accurate" → *compared
    to what, within what tolerance, over what period?*
14. **Who has to be able to use it without asking you?** — Names the training and handover
    requirement.
15. **What would make you stop using it?** — Surfaces the fragility nobody volunteers.

## Round 5 — the obstacles (the `blockers` field)

16. **What has to happen before this can even start?**
17. **Who else has to agree?** — Cyber Security, IT demand, the tool owner, another plant.
18. **Is anything already planned that this depends on?** — The corpus is full of
    *"planned for <year>"* blockers that nobody re-checked.

---

## The five judgement calls that make this hard

The tacit part, stated so it can be transferred.

**1 · Is this one use case or three?** If it decomposes into decisions taken by different
people at different moments, it is several. The instinct to keep it as one comes from wanting
a single business case; resist it — one use case, one decision, one moment.

**2 · Is the stated problem the real one?** *"We need an OEE dashboard"* is usually
*"we cannot tell which of our losses is the biggest"*. Ask what they would do differently
with the answer. If nothing, the requirement is wrong.

**3 · Is this standard or genuinely specific?** Most of the portfolio is declared
standard at intake, and **that declaration is the hinge the whole function turns on**. Check
the reference library before writing anything: if another plant has it, this is an adoption,
not a build — and adoption is what the department is actually short of.

**4 · Is the missing thing a signal or a decision?** *"Investigation and selection of process
parameter to be connected"* is a real blocker in the corpus — and it is not an engineering
blocker. Somebody has to decide which parameters matter. **That decision is the
requirement's job, not a reason to escalate.**

**5 · Is it worth doing at all?** A requirement that fails intake should fail here, cheaply,
rather than at the business case. No roadmap link, no nameable benefit, or a system outside
the lean footprint → refuse and route, with the reason written down.

---

## Refusal is a finished outcome

From the intake rules, and each has a route:

| Refuse when | Route to |
|---|---|
| No plant-roadmap link and no nameable business case | Back to the demand owner, with the reason |
| Needs a system outside the lean footprint | Strategy — a tool-rollout decision, not a use case |
| Owned by a sibling function | Manufacturing Engineering · P&PI · Facility · Tool Centre · IT |
| A one-off question with no recurring value | Analytical Support as an ad-hoc request — **do not industrialize** |
| Already exists at another plant | Adoption, via the reference library |

**A refusal with a named route is a better outcome than a thin requirement**, because a thin
requirement consumes an integration slot and then stalls. The estate keeps many use cases in `IDEA`;
some of them are refusals nobody wrote down.

---

## Closing the loop

Before you leave the room:

- Read §2 and §3 back **in their words** and ask if that is right.
- State what you will do next and by when.
- Name what you need from them and by when.
- Say explicitly whether this was **accepted, refused, or routed** — and to whom.

The commonest failure at this step is not disagreement. It is a requirement that everyone
assumed somebody else would finish.
