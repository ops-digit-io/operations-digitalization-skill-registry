---
type: Skill Reference
title: Process chain practice
description: Method, decision rules, handoff contract, pitfalls and agent notes for the freshness check, abstracted from the Operations Digitalization slide decks - time-stamped facts that change fastest (tool status, plant tier, forum status, vocabulary), copy residue, orphaned ownership, list clean-up. Guidance only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, hygiene, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - what goes stale and who notices

Deck-derived practice for the spine. The script finds old dates; this file tells the reviewer **which statements go stale fastest** and which patterns show it without a date. `PROPOSAL` = registry synthesis.

## 1. Method in practice

1. Run the script and read the tables as `SKILL.md` describes.
2. **Then walk the time-bound facts list** (section 2) through every skill that states one. A skill can be freshly read and still wrong because the world moved.
3. **Check copy residue** (section 4): placeholder numbers, template text, identical values across unrelated records.
4. **Check ownership** per field: owner role present, successor named, review date present. Empty owner fields are a finding, not a gap to ignore.
5. Draft the report; one owner and one action per finding; repair nothing.

## 2. Facts that change fastest (check live, never copy)

| Fact | Why it moves | How to check |
|---|---|---|
| Tool status and recommendation (one scale: recommended / recommended if <condition> / not recommended / not available; with date and source) | strategy decks change direction between years; some stop what others continue; plant summaries lag the strategy | tool overview list, with its date |
| Plant tier (first mover, fast follower) and which plants are on a wave | follows value, capacity and a staffed key user | plant roadmap, key-user register |
| Forum status and agenda (ODEC is historical, no longer held; technical call) | ODEC met monthly only until 2025-12; no fixed replacement forum; a later deck reused an earlier agenda unchanged | current invitation, not a deck |
| The dashboard standard and the BI standard | one strategy keeps the open dashboard tool, another plans a BI tool and lists the first as needing an upgrade | `dept-os`, register |
| Training format (hands-on in the plant, small groups, real plant data; central material is support only) | plans change | training plan |
| Master-data leader and which local masters remain | stated rule, reconciliation unstated | architecture owner |
| KPI definitions that depend on the system landscape (for example a use-case count against a threshold) | platform centralization changes counts | KPI definition with its date |
| Machine lists and tag lists | the speed of any vulnerability or migration response is bounded by their completeness | plant list with read date |
| Registered savings projects, use-case lists | lists rot: low-value and stale entries accumulate | plant clean-up round |

## 3. Decision rules

- **A decision that depends on a time-bound fact is blocked until the fact is looked up live.** Say so in the report.
- **Prefer the later dated source** when decks contradict, say that you did, and mark `<to confirm>`.
- **An early deck marked "not in use" defines intent, not practice.** Use it for cadence and structure only.
- **A statement with no owner and no review date is stale by definition** (the currency rules in `dept-os`: one named role per section, auto-flagging review date, fields not prose, open values marked).
- **Do not clear a finding by editing a date.** The existing rules stand.
- **Clean-up beats addition.** The decks record the pattern "an insufficient system is replaced by another insufficient system; we forget to clean up". A finding may recommend retiring the old artefact rather than refreshing it.

## 4. Pitfalls and lessons

- **Template residue.** One-page initiative sheets carried a leftover savings table with identical placeholder numbers across initiatives. Identical figures across unrelated records are a copy signal.
- **Empty owner, lead, team, sponsor or document location** on an initiative or entry: it should not enter routing; report it.
- **Single key person.** A technical key user left within weeks and nobody was named as successor; check that every owner has one.
- **Hidden versus deleted.** Not-applicable template pages are hidden or moved to the back, not deleted; a "deleted" section may have been silently dropped.
- **Tracker proliferation.** Several trackers for one purpose; ask which is the system of record.
- **Realized versus estimated wording** that has not been updated after a baseline was captured.
- **Version history carries text the current record does not** (`dept-os` honesty rule 5).

## 5. Questions to ask and definition of done

Which statement in this skill would be wrong if the strategy changed last quarter? Who owns the source and when was it last verified by a human? Is there a successor? Which figure is identical across records that should differ?

**Done:** every finding has an owner and an action; time-bound facts are listed with their live source and last check; nothing was edited to look newer.

## 6. AI agent operating notes

- **Can do:** run the script; list skills that state a time-bound fact (tool status, plant tier, cadence, vocabulary, KPI basis) and their source dates; detect identical placeholder values across records; list empty owner or review-date fields; compare the bundle's open gaps with the registry's; draft the report.
- **Needs:** script output, registry marks, the live lists named in `dept-os`.
- **Human gate:** the owner (OD lead for the bundle, registry owner for skills) decides every action; nothing is marked verified, expired or stable on the agent's say-so.
- **Must cite:** file and field, date found, live source consulted.
- **Hands over:** the dated hygiene report; each finding names its owner role.
