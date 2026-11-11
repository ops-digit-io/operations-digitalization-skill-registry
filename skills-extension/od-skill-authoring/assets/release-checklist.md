---
type: Skill Asset
title: Release checklist
description: The checklist completed before the pull request of a new or changed skill - the brief, the anatomy, the registry entries, the gates, the quality rating, the tests and the honesty rules - so the owner reviews a finished skill. Copy one per skill.
resource: ../SKILL.md
status: draft
tags: [skills, practice, checklist]
---
# Release checklist: ⟨skill name⟩

Tick each line with the evidence (output, path or number). A line that does not apply says why.

## Design
- [ ] The brief is agreed by the owner (date): ⟨…⟩
- [ ] No existing skill covers it; the searched skills are listed in the brief
- [ ] One capability per name; the name is lowercase kebab-case and equals the folder

## Content
- [ ] Every source was opened this session and is cited; open questions say who can answer
- [ ] No invented figure, name, date or source; roles, not individuals; English
- [ ] The description says what it does and when to use it, in third person, and names a "not for" boundary
- [ ] Sections: Purpose, Inputs and output, Procedure, Human gate and AI-agent notes, Pitfalls, Definition of done, References, one worked example, a Scripts table if scripts ship
- [ ] `SKILL.md` is under 500 lines; references are one level deep; scripts have a test

## Registry
- [ ] `registry.yaml` entry added; `authority_level` equals the `SKILL.md`
- [ ] `docs/new-state/process.yaml` placement (extension: proposed on a step or the spine)
- [ ] README row and counts updated
- [ ] Generated pages regenerated (`build_okf_index.py`, `build_skill_map.py`, `build_new_state_skill_map.py`)

## Gates
- [ ] `python scripts/validate_registry.py`: ⟨result⟩
- [ ] `python scripts/agent_skills_spec.py --export dist`: ⟨result⟩
- [ ] `python scripts/verify_okf.py`: ⟨result⟩
- [ ] `python scripts/check_no_figures.py <name>`: every flagged line read: ⟨result⟩
- [ ] SkillEvaluator quality-check: grade ⟨ ⟩, score ⟨ ⟩; rating recorded with `build_skill_quality.py`

## Tests
- [ ] Test cases and trigger queries written (`evals/`): ⟨yes / no⟩
- [ ] Run with and without the skill: ⟨pass rates, or "not run"⟩; trigger rates: ⟨…⟩ or "not run"
- [ ] If not run: the skill says so and stays `draft`

## Review
- [ ] Pull request description: the rating, the test result, the open points
- [ ] Status left at `draft` for the owner to change; nothing marked verified
