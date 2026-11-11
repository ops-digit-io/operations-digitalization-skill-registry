---
type: Skill Reference
title: Refusal playbook
description: Request patterns that look legitimate but should be refused or re-scoped, what the tell is, and one pattern accepted that should have been refused - guidance distilled from the department's retrospectives, no plant names or figures.
resource: ../SKILL.md
status: stable
tags: [use-case-support-service, practice]
---
# Refusal playbook

`SKILL.md`'s refusal list states the categories — no roadmap link, outside the lean
footprint, owned by a sibling function. This file is the tacit layer underneath: what a
request that fits none of those categories but is still worth refusing actually looks
like, distilled from the department's own retrospective record.

## 1 · Looked legitimate: a change request against something OD already owns

**The request:** a plant asking OD to change headlines, fonts or colors on an existing
dashboard.

**What made it look legit:** it is a request about a system OD built and is responsible
for — exactly the kind of thing "support with a digital solution" is supposed to cover,
and refusing it looks like refusing to support the plant.

**The actual tell:** zero value-add. The request consumes capacity on a cosmetic change
to something that already does its job. The department's own retrospective names this
directly: *"we got requests to change Headlines, Fonts & Colors for our Dashboards
burning capacity while providing low value."* The fix was procedural, not case-by-case —
Use Case Sprints prioritized by cost-saving impact with a limited duration, so a
low-value request has to compete for a slot rather than being actioned on request.

## 2 · Looked legitimate: a use case riding on infrastructure that isn't there yet

**The request:** a use case proposal built on a tool that is demoed or piloted at the
plant, but not yet rolled out there.

**What made it look legit:** the tool genuinely exists somewhere in the estate — it is not
a fictional ask, and a plant pointing at a real capability looks like a reasonable
request.

**The actual tell:** the plant's own tool-availability status says otherwise. A typical pattern (illustrative): a tool is recorded with a test/demo system already
**deployed at the plant**, while the same summary says *"no use cases yet, not yet planned
for this plant"*. The tool existing is not the
same as the use case being in scope for that plant yet — check the tool-availability
table before accepting the use case, not just whether the tool exists anywhere.

## 3 · Looked legitimate: an approval gate OD does not control

**The request:** treating Cyber Security sign-off or a system-deployment approval as part
of OD's own commitment on a use case's timeline.

**What made it look legit:** both gates sit directly in the use case's critical path, so
folding them into the same commitment looks like normal scope.

**The actual tell:** OD does not control either gate's timing. The department's own fix,
stated plainly: *"We detached Use Case implementation from Cyber Security approvals to
avoid dependencies and wrong expectations (out of our control). We detached Use Case
implementation from System Deployment approvals"* for the same reason. Accepting a
commitment that depends on someone else's approval timeline is accepting a promise OD
cannot keep — record the gate as a dependency (`od-decision-routing`), never as part of
OD's own deliverable date.

## Accepted something regretted: the "difficult machines first" approach

**What happened:** to build a success story, OD took on a set of representative *and
difficult* machines itself and left the easy ones for the plant to connect — the
reasoning being that starting with the hard cases would prove the approach.

**What actually happened, in the department's own words:** *"Turns out: Difficult
Machines are hard to connect! Reputation burned & local Project dead."* The harder
machines were harder for real reasons (older PLCs, missing programs, non-standard
wiring) that did not go away because OD took them on first, and the stalled result
damaged trust in the whole initiative at that plant.

**What changed after:** scale out known-good machine types first (common success), limit
unknown machine types to one per new deployment, and write the integration process down
per PLC type rather than repeating the attempt from memory each time. The lesson is not
"avoid hard machines" — it is "do not front-load the hardest, least-proven cases onto a
new initiative's first result."

## The pushback line and the exact answer

Not resolved from the available record — the decks document what OD decided and why, not
the plant's own words when refused. If a common pushback phrase and a standard answer to
it exist, they remain open; add them here directly rather than inventing a plausible one.

## Sources

Distilled from the department's retrospective and workshop material (strategy workshop on
use-case boundaries and agility lessons; use-case definition workshop summaries with
tool-availability tables). Full citations in `SKILL.md`'s `metadata.derived_from`.
