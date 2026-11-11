---
type: Skill Asset
title: Assessment protocol
description: The defined output of Route A - plant/wave inventory, barrier tier and roadmap per machine, sized and sequenced, so the result is a reusable record rather than prose.
resource: ../SKILL.md
status: stable
tags: [information-integration-service, template, protocol]
---

# Equipment integration assessment — ⟨plant⟩ ⟨· wave⟩

| | |
|---|---|
| **Plant / wave** | ⟨name⟩ |
| **Trigger** | ⟨new plant · integration wave · use case blocked on data · target needs a credible plan⟩ |
| **Assessor / date** | ⟨name⟩ · ⟨date⟩ |
| **Machines in scope** | ⟨n, filtered by demand — see below⟩ |
| **Overall verdict** | ⟨roadmap agreed · partial, blockers logged · scope not yet confirmed⟩ |

## 1 · Inventory

| Integration status | Machines |
|---|--:|
| `INTEGRATED` | ⟨n⟩ |
| `NOT INTEGRATED` | ⟨n⟩ |
| `INTEGRATION ONGOING` | ⟨n⟩ |
| No status recorded | ⟨n⟩ |

**Demand filter.** ⟨Which accepted or planned use case each in-scope machine's data serves.
A machine with no use case behind it does not belong in this wave — say so rather than
silently including it.⟩

## 2 · Machine-by-machine roadmap

| Machine | Plant | Vendor / PLC | Protocol | Criticality | Use case | Barrier tier | Concept | Connector | Sequence | Blocker | Owner |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ⟨name / EQ id⟩ | | | | | | ⟨easy/moderate/hard, per barrier-classes.md⟩ | ⟨① / ② / ③⟩ | | ⟨n of m⟩ | ⟨none / named⟩ | |

**Barrier tier** is the practitioner ranking in `references/barrier-classes.md`, not a raw
read of the integration-rate percentage — say when a machine's tier disagrees with what the
raw rate alone would suggest, and why.

Route each machine into Route B (`assets/guidance-protocol.md`) once its concept and
connector are provisionally chosen here; Route A's job stops at the roadmap, not at the
per-machine configuration.

## 3 · Investment

| Item | Estimate | Approval path |
|---|---|---|
| ⟨edge devices, OT hardware, licences, connector development⟩ | | ⟨execute-with-approval, Tandem with Plant ME / Plant IT⟩ |

## 4 · Cyber Security / OT gate

⟨Bundled with the wave, or per machine? Sign-off status. External connections need this
**before** scheduling, not after — there is no expedited path.⟩

## 5 · Barriers logged (not silently omitted)

| Machine | Barrier | Class | Escalated to |
|---|---|---|---|
| ⟨⟩ | ⟨no route / cyber security / operations concept missing⟩ | ⟨per barrier-classes.md⟩ | ⟨roadmap · strategy · IIAE⟩ |

## 6 · Definition of done

- [ ] Equipment inventory and roadmap agreed with Plant ME / Plant IT
- [ ] Each in-scope machine carries a concept, a connector, and a sequence position
- [ ] Barriers logged, none silently omitted
- [ ] Investment planned and Cyber Security gate identified
- [ ] Sequence checked against the plant roadmap and readiness matrix

## Sign-off

| Role | Name | Date |
|---|---|---|
| IIAE | | |
| Plant ME / IT | | |
