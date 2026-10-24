---
type: Skill Reference
title: Evidence of adoption
description: What counts as evidence that a use case is actually in use, in order of strength, so adoption is recorded as a fact with a source rather than an impression.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [all, practice, adoption]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# Evidence of adoption

How plant adoption is confirmed and recorded was not written down anywhere in the source
systems; confirmed 2026-10-22 by ranking the evidence already available, strongest first, so
"adoption" always carries a source instead of being asserted.

## The three tiers, strongest first

1. **A usage record from the system itself** — a dashboard's own view count, a query log, an
   export history. This is evidence of use, not of a claim about use. Where the output asset
   is a Dashboard or Analytics Workflow on a platform that logs views or queries, this is
   always the first thing to check before asking anyone.
2. **The named plant owner's dated statement** — "I used this in a real shift on
   ⟨date⟩, for ⟨decision⟩." This is `SKILL.md`'s existing definition-of-done line ("used in a
   real shift, not a demonstration"), made explicit as a recordable fact: a sentence with a
   name and a date attached, not a checkbox.
3. **A third party's observation** — a plant visit, a Gemba walk, a colleague who saw it in
   use. Weaker than the first two because it is secondhand, but still evidence, and better
   than silence.

**What is not evidence:** that the handover was marked `DONE`, that the use case is
`IMPLEMENTED`, that training happened, or that nobody has complained. All four describe
delivery, not use — exactly the distinction `SKILL.md`'s central rule exists to protect.

## Recording it

Record whichever tier was actually available, plus its source — never upgrade a tier-2
statement to look like tier-1 evidence, and never leave the field blank because tier-1 was
unavailable. "Tier 2, Maria Lindqvist, 2026-10-14, used for the 06:00 Gemba walk" is a
complete, honest record. A blank adoption field is not more honest than that; it is just
less useful.

## When no evidence exists at all

That is the same finding as a `NEVER` utilization row in `SKILL.md`'s low-utilization
procedure — work the ADKAR barrier point (`references/adkar-diagnostic.md`) before assuming
the asset itself is the problem. An asset nobody can produce *any* tier of evidence for,
after the ADKAR check, is a legitimate retirement candidate per `SKILL.md`'s own rule.
