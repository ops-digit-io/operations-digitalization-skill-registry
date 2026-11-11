---
type: Skill Reference
title: Click dummy
description: "The department's click-dummy stage (funnel-prototype): turn the selected features into a verified clickable prototype traceable problem to feature to screen."
resource: ../SKILL.md
status: draft
tags: [prototype, click-dummy, department-package]
---
> Transcribed from the department package `product-funnel-skills.zip/skills/click-dummy/SKILL.md` (the master).

# Click Dummy

Turn a prioritized feature set into something a person can click through, prove
every control works, and document what it does and does not do.

Final stage of the chain: `requirements-funnel` → `feature-funnel` →
**`click-dummy`**.

## What This Is (and Is Not)

A click dummy is **a complete walkable surface for a defined scope**. Its
purpose is validating navigation, terminology and workflow shape *before* any
architecture is decided. Someone who has never seen the project should reach a
real outcome without being told which buttons are real.

It is not a throwaway probe of one question, and it is not the seed of the
production build. Do not let implementation choices here lock the eventual
product into an architecture — a dummy optimised for being clicked through is
the wrong shape for production, and treating it as a foundation is how a
prototype's shortcuts become permanent.

<HARD-RULE>
**No dead controls, and "it works" means verified in a real browser.** Every
control either performs its action or is visibly marked out of scope. A control
that looks live and does nothing destroys trust in the whole prototype — the
reviewer stops knowing what they are looking at and their feedback becomes
worthless. Claims of working controls that rest on anything less than a real
browser are not evidence. See Stage 6.
</HARD-RULE>

## Stage 1 — Scope from the Feature Book

Read `feature-book.md`. Default scope is **MVP + v1**.

Build every MVP feature fully; build v1 to the depth the journey needs;
represent v2/v3 only as marked out-of-scope affordances where their absence
would make a screen look broken. Carry the `riskiest_assumption` forward and
say which interaction tests it.

Ask for anything the feature book cannot tell you but the surface will expose:
**the product name, the default user's name and role, and the organisation's
own vocabulary**. If you invent these, they will be overridden on first review —
that correction round is pure waste and it is entirely avoidable by asking.

## Stage 2 — Pick the Shape

| Situation | Shape |
|-----------|-------|
| New product, needs to be shared and opened without setup | **Single file** (default) |
| Belongs inside an app that already exists | **In-project route** |

**Single file** is the strong default: one HTML file, vanilla HTML/CSS/JS,
everything inline, no framework, no bundler, no build step, no server. It opens
by double-click and survives being emailed. This scales further than people
expect — a 13-section enterprise CRM with 19 routes and full create flows fits
comfortably in one file. Reach for a framework only when something genuinely
demands it, not by habit.

**In-project route** when the thing belongs inside existing software, so it is
judged against real layout and density. Follow the project's routing
conventions; name it so a reader sees it is a prototype.

## Stage 3 — Define Done Before Building

Write the completion criteria **now**, not after the first review. Two pieces:

1. **A demo story** — the ordered click-through you will walk someone through.
2. **A completion gate** — the objective bar. This must include *every control
   exercised*, not just the demo story.

This ordering is not bureaucratic. A demo story alone exercises the paths it was
written for and hides everything else, and the bug that breaks a whole class of
pages will sit on the pages the story never opens. Deciding the gate upfront is
what makes Stage 6 mean something.

## Stage 4 — State and Data First

Define state and mock data **before any screen**, in one pass, and do not
restructure them later. Getting this right upfront is what lets everything
after it stay additive.

Keep them as two separate flat objects:

```js
const mockData = { /* one array per entity, cross-linked by string id */ };
const state = { route:'…', recordId:null, tab:null, filters:{}, /* ui flags */ };
```

**Direct mutation plus a full re-render is the right default here.** Mutate
`state` or push to `mockData`, then rebuild the page body from an HTML string.
No reducer, no diffing, no virtual DOM. At click-dummy scale this is simpler,
easier to follow, and removes a whole class of stale-view bugs. Interleaving
state and rendering is acceptable in a way it would not be in production —
because this code is explicitly not going to production.

**Seed data must be deliberately uneven**, or the dummy will look better than
the product and hide the problems it exists to surface:

- Real hierarchy, not flat lists
- Non-round figures — `77774000`, not `80000000`
- At least one record with an empty collection and no activity, so empty states
  are reachable by clicking
- At least one long value that will wrap or truncate
- Compute displayed aggregates from the data rather than hardcoding them, so
  they stay consistent when a record is added through the UI

Uneven is not the only requirement: **the seed data must also make the intended
comparison true.** If the prototype's case is that a new approach wins, the
sample data has to show it winning. This is separate from realism — data can be
perfectly plausible and still tell the opposite story, and you will not notice
from the code, only from the rendered numbers.

## Stage 5 — Shell First, Then Sections

Build in this order. It is the ordering that survives contact with a real build:

1. **Shell** — CSS tokens, layout, router, state. One pass.
2. **Shared primitives** — the table, card, badge, empty-state and escaping
   helpers. Most screens are mostly these.
3. **Sections** — fill in screen by screen.
4. **Business logic** — the render functions and create flows.

If the file is too large to emit in one pass and you build it in chunks, verify
each insertion point occurs **exactly once immediately before writing to it**.
Checking afterwards means sweeping up duplicates in a file that will not even
parse yet.

Every screen: reachable by clicking from the entry point, navigable back,
labelled in domain language, populated with the uneven seed data.

For visual design use the `frontend-design` skill. One caution specific to
dummies: a prototype that reads as generic AI output gets reviewed as a template
instead of as the product, and the feedback comes back about styling rather than
flow. Dense, quiet, legible beats decorative.

## Stage 6 — Verify in a Real Browser

**The single most important stage, and the one most often faked.**

Drive the actual page in a real browser — Playwright against installed Chrome is
enough. Walk **every route, every tab, every create flow, every control**, and
assert no console errors on each.

<NEVER>
Never verify with a hand-rolled DOM shim or a stubbed `document`. A shim that
auto-creates elements on request will manufacture the exact element whose
absence is the bug, and report a long list of passing checks while the app is
broken in every real browser. This is worse than no testing: it produces
confident false evidence and it is precisely how a bug that breaks most of an
app survives a full test pass.
</NEVER>

### Coverage: can the user actually do the job?

Clicking every existing control proves the controls work. It does not prove the
prototype is usable, because **a missing control has nothing to click.** This is
the failure mode a button sweep cannot see, and it is the one users hit first.

Build an entity × action matrix before declaring done. For every entity in the
state model, check each action the actor needs:

| Entity | Create | View | Edit | Delete | Notes |
|--------|--------|------|------|--------|-------|
| Scenario | ✅ | ✅ | ✅ | ❌ | delete is v1 |
| Station | ✅ | ✅ | drag | ❌ | |
| Operator | **MISSING** | ✅ | ✅ | ❌ | seeded only — gap |

An entity that appears in seed data but has **no create path** is the classic
gap: it looks complete because the samples are there, and the first thing a real
user tries is adding one of their own. Every such cell is either built or
explicitly stubbed with a visible reason. Never left blank and unmentioned.

Then walk the demo story **as a user, not as a script** — from the entry screen,
clicking only what is on screen, without editing state or URLs. If a step
requires knowing an id, or a control that is not there, that is a finding.

Put the completed matrix in the handover document. It tells the next agent what
exists far more precisely than a feature list does.

### Then verify the demo actually makes the case

Passing tests mean the app runs. They do not mean it demonstrates anything.

Walk the demo story yourself and read the numbers. If the prototype exists to
show that option B beats option A, check that the seeded data actually shows
that. A prototype whose comparison argues *against* the product will pass every
technical check and fail in the room — and the failure looks like a product
problem when it is really a seed-data problem.

Concretely: compute the headline comparison, confirm each KPI moves the
direction the case requires, and if one does not, decide whether the seed data
is unrepresentative or the metric is wrong. Both are worth knowing before a
reviewer finds it. If the metric is wrong, record it in the open questions —
that is a requirements finding, not a bug.

Keep the verification script in the project. Deleting it after each use means
the next change re-verifies nothing and the harness gets rebuilt from scratch
every time.

Known traps to check explicitly — each one has broken a real build:

| Trap | Check |
|------|-------|
| Shared helper writing to an element that only exists on some routes | Every shared render function null-guards, or takes the element as a parameter |
| Transient panels removed instead of cleared | Dropdowns and modals close via `innerHTML=''`, never `.remove()` — removing deletes the node permanently and the next open silently writes nowhere |
| Bugs only on pages the demo story skips | Walk list pages and landing pages, not just the detail routes the story visits |
| Create flows untested | Actually submit each "New X" form and confirm the record appears |
| Ambiguous test selectors | Scope selectors to a container — `.modal button.primary`, not `button:has-text('Add')`, which also matches "Add task". An ambiguous locator resolves to the first match and proceeds, so the failure surfaces somewhere unrelated |

A local null-check patches one call site; the same shape of bug can recur
wherever else shared code touches route-specific elements. Prefer fixing the
pattern, and say so if you only patched the instance.

## Stage 7 — Fidelity Ledger

Every element is one of:

| Level | Meaning |
|-------|---------|
| **Real** | Works as it would in production |
| **Computed** | Derived correctly from mock data — the logic is real, the source is not |
| **Faked** | Plausible content typed into the data; nothing computes it |
| **Stubbed** | Visible, marked out of scope, not clickable |

The **Computed / Faked** split is the one that gets missed. Aggregates
calculated from mock records and invented qualitative fields — reference
numbers, competitor estimates, risk notes, timestamps — render identically and
read as equally authoritative. A reviewer cannot tell them apart from the UI.

A handful of in-page "coming later" notes is not a fidelity ledger. Whoever
inherits the prototype will read those notes as the complete list of what is
fake, and everything unmarked as real. Mark in the UI where it matters and
record the full ledger in the handover document.

## Stage 8 — Handover Document

Specs are not documentation. A file describing what to build says nothing about
what was actually built, and a project can end up with three specs and no record
of the delivered scope.

Write `prototype-notes.md`:

1. **What this is** — scope line, how to open it
2. **Features covered** — a table tracing `problem → feature id → screen →
   demo step`, so any screen can be traced back to a stated problem
3. **The assumption under test** — which interaction tests it, what to watch
4. **Fidelity ledger** — from Stage 7, complete
5. **Coverage matrix** — entity × action, with gaps named
6. **Limitations** — no persistence, no auth, no backend, whatever else applies
7. **Not built** — v2/v3 and Won't items a reviewer might expect, with reasons
8. **Open questions** — what the build surfaced that the funnel missed. Include
   anything the next agent must ask rather than infer: whether placeholder names
   and taxonomies are illustrative or real, whether any external numbering scheme
   must be matched
9. **Verification** — what was tested, how, and where the script lives

Section 8 is the return path into `requirements-funnel`. A dummy that raises no
new questions was either trivial or nobody looked closely.

## Red Flags

| Thought | Reality |
|---------|---------|
| "The test harness says everything passes" | If it is not a real browser, it does not know. A shim can pass while the app is broken everywhere. |
| "The demo story works, so it works" | The story exercises the paths it was written for. The bug is on the pages it skips. |
| "This button isn't important, I'll leave it inert" | Then mark it stubbed. One silent dead control makes every other control suspect. |
| "Every button passed, so the prototype works" | A missing control has no button to click. Sweeps cannot see absence — build the entity × action matrix. |
| "The sample records show that entity works" | Seeded data is not a create path. The first thing a user does is add their own. |
| "I'll note what's fake in the chat" | Chat scrolls away; the doc travels with the file. |
| "The 'coming later' banners cover the fake parts" | They cover what someone remembered to caveat. The unmarked invented data is the larger set. |
| "I'll use placeholder data" | Clean data hides the density and empty-state problems the dummy exists to expose. |
| "I'll pick a product name and user, they can change it" | They will, on first review. Ask upfront; it costs one question. |
| "I'll restructure state once screens exist" | Reshaping state after screens is expensive. Spend the time in Stage 4. |
| "It works, so it's nearly production" | It was built with no error handling and no tests, and deliberately so. Say so. |
| "I'll delete the test script, it's served its purpose" | Then the next change verifies nothing. Keep it. |

## Chaining

- Runs **after**: `feature-funnel`; consumes `feature-book.md`
- Uses: `frontend-design` for visual direction
- Produces: the dummy, a verification script, `prototype-notes.md`
- Runs **before**: `business-case` (value model and stakeholder deck)
- Feeds back: Section 8 open questions return to `requirements-funnel`

Shell, router, dispatch and shared primitives: `build-patterns.md`.
