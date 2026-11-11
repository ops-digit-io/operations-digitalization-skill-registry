---
name: od-skill-authoring
description: >-
  Build a new OD skill, or rework a weak one, by the registry's standard method: start from the department's own record, design the skill on one page before writing it (need, lane and step, users, authority, sources, three test cases), write it to the registry's anatomy, pass the gates in order (registry checks, Agent Skills specification export, OKF, no invented figures, the SkillEvaluator quality rating) and hand it to the department owner for review. Use when a recurring OD procedure should become a skill, when a skill rates below B, or before any skill is added to the registry. Not for writing a single note or a one-off prompt, and not for changing a skill's content without a new source: use the skill that owns the topic.
license: MIT
allowed-tools: Read Grep Glob Bash(python3 scripts/scaffold_skill.py:*)
metadata:
  id: od-skill-authoring
  tier: practice
  lane: all
  new_state_lane: "Extension, deepens Spine"
  new_state_step: "Supporting spine"
  owner_role: Digital-Business-Value-Engineer (DBVE); the OD lead approves publication
  authority_level: draft the brief, the skill and the checks; the owner reviews and decides; never marks a skill reviewed or verified
  status: draft
  requires: [od-context]
  composes: [od-context-freshness, od-ai-generation-playbook, od-decision-routing]
  okf:
    type: Agent Skill
    title: Skill authoring
    tags: [practice, skills, quality]
---

# Skill authoring

Read `od-context` first.

## Purpose

A skill is worth building when a department procedure recurs, the judgement in it can be written down, and an agent would get it wrong without it. This skill is the registry's standard method for that: nine steps from "should this be a skill?" to a reviewed, rated, published skill, with a control point at each. It turns the Agent Skills guides, the SkillEvaluator rubric and the registry's own conventions into one order of work, so that a new skill passes its checks the first time and a weak skill gets a defined repair path.

## Inputs and output

- **In:** a recurring OD procedure and the person who owns it; the department record about it (knowledge base, then archive); the registry, to check that no skill already covers it.
- **Out:** a skill folder that passes the gates, a one-page brief ([`assets/skill-brief.md`](assets/skill-brief.md)), the registry entries, a quality rating, and a pull request for the department owner's review.

## Procedure

1. **Check that it is needed.** Search the registry first (`README.md`, `registry.yaml`). If a skill covers the topic, extend that skill; one capability per name. Name the owner (a role) and the trigger. Control point: no existing skill covers it and an owner is named.
2. **Start from real expertise, not from general knowledge.** Mine the department record in the knowledge base's order (knowledge base, then archive, then external sources) for the steps that worked, the corrections people made, the input and output formats, and the context they supplied; ask the owner only for what the record does not hold ([`references/skill-anatomy.md`](references/skill-anatomy.md), section Sources). Cite only what you opened.
3. **Design on one page.** Fill [`assets/skill-brief.md`](assets/skill-brief.md): the need, the users, the lane and step (or `all`), the tier, the authority level, inputs and outputs, what the agent lacks without the skill, the sources, and three test cases. Control point: the owner agrees the brief before the skill is written.
4. **Scaffold.** `python3 scripts/scaffold_skill.py <name> --tier practice --lane all --owner-role "<role>" --authority "<what the agent may do>"` creates the folder to the registry's anatomy and prints the registry entry to add.
5. **Write it.** Description first: what it does and when to use it, in third person, with a "not for" boundary. Then procedures rather than declarations, defaults rather than menus, a gotchas list, one worked example, references one level deep from `SKILL.md`, scripts with a test. Add only what the agent would get wrong without it ([`references/skill-anatomy.md`](references/skill-anatomy.md)).
6. **Place it.** Add the entry to `registry.yaml` (its `authority_level` must equal the `SKILL.md`), place it on `docs/new-state/process.yaml` (an extension skill as `proposed` on a step or on the spine; a core skill only if the flow draws it), add its README row, then regenerate the generated pages.
7. **Pass the gates in order** ([`references/quality-gates.md`](references/quality-gates.md)): registry validator, specification export, OKF check, no-invented-figures check, then the SkillEvaluator quality-check with the registry's configuration, and record the rating.
8. **Test it on real tasks.** Two or three test cases run with and without the skill, and a trigger query set, as the Agent Skills guides prescribe ([`references/evaluation-design.md`](references/evaluation-design.md)). If this is not done, say so in the skill and keep `status: draft`.
9. **Review and publish.** The department owner reads it; a pull request carries the rating and the open points. Only a human sets a skill's status beyond `draft`; nothing is ever marked verified.

```bash
python3 scripts/scaffold_skill.py od-example-check --tier practice --lane all \
    --owner-role "Digital-Business-Value-Engineer (DBVE)" --authority "draft; the owner decides"
```

## Scripts

| Script | Purpose | Arguments |
|---|---|---|
| `scripts/scaffold_skill.py` | Create a skill folder in the registry's anatomy and print the registry entry | `name`, `--tier`, `--lane`, `--owner-role`, `--authority`, `--library`, `--out` |
| `scripts/test_scaffold_skill.py` | Test that a scaffolded skill parses and meets the registry's frontmatter rules | none |

## Human gate and AI-agent notes

- **Agent may:** search the registry, mine the record, draft the brief and the skill, run the scaffold and the checks, list what is missing. **Humans decide:** whether the skill is needed, the brief, the authority level, the sources to trust, the review and any status above `draft`.
- **Evidence to cite:** the sources opened, the check output, the rating, the test results.
- Never invent a figure, a name or a source to make a skill look finished; mark the gap `to confirm` and name who can fill it.

## Pitfalls

- Writing the skill from general knowledge. The Agent Skills guides name this as the main way to get a vague, generic skill.
- Adding text to please the checker. The rating measures documentation; a section that says nothing lowers the skill's value and still scores.
- A second skill for a topic one skill already owns; extend instead.
- Putting extra frontmatter keys at the top level. The specification allows six; the rest goes under `metadata`, and the SkillEvaluator's `version` check cannot be met without breaking distribution (see the gates reference).
- Reference files that link on to other reference files, a body over about 500 lines, and a description that names no boundary.
- Declaring the skill reviewed or verified. Only the owner can.

## Definition of done

The brief is agreed; the skill passes the registry validator, the specification export, the OKF check and the figures check; its quality rating is recorded and, as a proposed target, is B or higher; test cases and trigger queries are written (and run, or stated as not run); registry, flow and README entries exist; the owner has reviewed the pull request.

## References

| File | Open when |
|---|---|
| [`references/skill-anatomy.md`](references/skill-anatomy.md) | Writing the skill: frontmatter, sections, sizes, naming, sources |
| [`references/quality-gates.md`](references/quality-gates.md) | Passing the gates: commands, what each finding means, known conflicts |
| [`references/evaluation-design.md`](references/evaluation-design.md) | Designing test cases and trigger queries |
| [`assets/skill-brief.md`](assets/skill-brief.md) | Step 3: the one-page brief |
| [`assets/release-checklist.md`](assets/release-checklist.md) | Step 9: the checklist before the pull request |
