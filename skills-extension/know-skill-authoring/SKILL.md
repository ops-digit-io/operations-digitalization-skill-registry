---
name: know-skill-authoring
description: >-
  Build a new OD skill, or rework a weak one, by the registry's standard method. Use when a
  recurring OD procedure should become a skill, when a skill rates below B or reads vague, or
  before any skill is added to the registry. Starts from the department's own record, has the
  skill designed on one page before it is written (need, lane and step, users, authority,
  sources, three test cases), writes it to the registry's anatomy, passes the gates in order
  (registry checks, Agent Skills specification export, OKF, no invented figures, the
  SkillEvaluator quality rating) and hands it to the department owner for review. Not for
  writing a single note or a one-off prompt, and not for changing a skill's content without a
  new source: use the skill that owns the topic.
license: MIT
allowed-tools: Read Grep Glob Bash(python3 scripts/scaffold_skill.py:*)
metadata:
  id: know-skill-authoring
  aliases: [od-skill-authoring]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Extension, deepens Spine"
  new_state_step: "Supporting spine"
  owner_role: Digital-Business-Value-Engineer (DBVE); the OD lead approves publication
  authority_level: draft the brief, the skill and the checks; the owner reviews and decides; never marks a skill reviewed or verified
  status: draft
  requires: [dept-context]
  composes: [dept-context-freshness, know-ai-generation, dept-decision-rights]
  okf:
    type: Agent Skill
    title: Skill authoring
    tags: [practice, skills, quality]
---

# Skill authoring

- Read `dept-context` first.

## Purpose

- It turns the Agent Skills guides, the SkillEvaluator rubric and the registry's own conventions into one order of work, so that a new skill passes its checks the first time and a weak skill gets a defined repair path.
- A skill is worth building when a department procedure recurs, the judgement in it can be written down, and an agent would get it wrong without it.
- This is the registry's standard method: nine steps from "should this be a skill?" to a reviewed, rated, published skill, with a control point at each.
- Requires Python 3.8+ (standard library only) for the scaffold script.

## Inputs and output

- **In:** a recurring OD procedure and the person who owns it; the department record about it (knowledge base, then archive); the registry, to check that no skill already covers it.
- **Out:** a skill folder that passes the gates, a one-page brief ([`assets/skill-brief.md`](assets/skill-brief.md)), the registry entries, a quality rating, and a pull request for the department owner's review.
- [`outputs.yaml`](outputs.yaml) lists required outputs, criteria, checks and sign-offs.

## Procedure

1. **Check that it is needed.** Search the registry first (`README.md`, `registry.yaml`).
   - If a skill covers the topic, extend that skill; one capability per name. Reason: two skills on one topic drift apart.
   - Name the owner (a role) and the trigger.
   - Control point: no existing skill covers it and an owner is named.
2. **Start from real expertise, not from general knowledge.** Mine the department record (knowledge base, then archive, then external sources) for what worked.
   - Look for the steps that worked, the corrections people made, the input and output formats and the context they supplied.
   - Ask the owner only for what the record does not hold (`skill-anatomy`, section Sources).
   - Cite only what you opened.
3. **Design on one page.** Fill [`assets/skill-brief.md`](assets/skill-brief.md): need, users, lane and step (or `all`), tier, authority level, inputs and outputs, what the agent lacks without the skill, sources, three test cases.
   - Control point: the owner agrees the brief before the skill is written.
4. **Scaffold.** Run the command below. It creates the folder to the registry's anatomy and prints the registry entry to add.
5. **Write it.** Description first: what it does and when to use it, in one point of view, with a "not for" boundary.
   - Then procedures rather than declarations, defaults rather than menus, a gotchas list, one worked example, references one level deep from `SKILL.md`, scripts with a test.
   - Add only what the agent would get wrong without it (`skill-anatomy`).
6. **Place it.** Add the entry to `registry.yaml` (its `authority_level` must equal the `SKILL.md`), add its README row, then regenerate the generated pages.
   - Place it on `docs/new-state/process.yaml`: an extension skill as `proposed` on a step or on the spine; a core skill only if the flow draws it.
7. **Pass the gates in order** (`quality-gates`): registry validator, specification export, OKF check, no-invented-figures check, then the SkillEvaluator quality-check with the registry's configuration; record the rating.
   - Validation loop: run the gate, fix the finding, run again; do not go on while a gate fails.
8. **Test it on real tasks.** Write `evals/evals.json` (at least three cases, one edge or near-miss, plus trigger queries) and run each case with and without the skill (`evaluation-design`).
   - If this is not done, say so in the skill and keep `status: draft`.
9. **Review and publish.** The department owner reads it; a pull request carries the rating and the open points (`assets/release-checklist.md`). Only a human sets a status beyond `draft`; nothing is ever marked verified.

```bash
python3 scripts/scaffold_skill.py know-example-check --tier practice --lane all \
    --owner-role "Digital-Business-Value-Engineer (DBVE)" --authority "draft; the owner decides"
```

### Example brief (fictional)

```text
Skill brief: know-example-check (fictional)
Owner: Digital-Business-Value-Engineer (DBVE)          Library: extension   Tier: practice   Lane: all
1 Need:     A monthly list check is done by hand in every region; each region misses different columns.
2 Covered?  Searched README and registry.yaml: no skill covers list checks; closest is dept-context-freshness (dates only).
3 Authority: agent drafts the check and the report; the owner decides what to correct.
5 Lacks:    which columns matter, how a blank is read (absent, not zero), the report layout.
6 Sources:  knowledge-base note on the monthly check (opened 2026-01-12, fictional); archive working file (opened).
7 Cases:    (1) normal month; (2) a column renamed; (3) near-miss: a request to analyse savings (belongs to another skill).
8 Agreed:   go, 2026-01-15 (fictional)
```

## Scripts

| Script | Purpose | Arguments |
|---|---|---|
| `scripts/scaffold_skill.py` | Create a skill folder in the registry's anatomy and print the registry entry; refuses to overwrite; exit 2 on a bad name or tier; `--help` lists options | `name`, `--tier`, `--lane`, `--owner-role`, `--authority`, `--library`, `--out` |
| `scripts/test_scaffold_skill.py` | Test that a scaffolded skill parses and meets the registry's frontmatter rules | none |

## Human gate and AI-agent notes

- **Agent may:** search the registry, mine the record, draft the brief and the skill, run the scaffold and the checks, list what is missing.
- **Humans decide:** whether the skill is needed, the brief, the authority level, the sources to trust, the review and any status above `draft`.
- **Evidence to cite:** the sources opened, the check output, the rating, the test results.
- Never invent a figure, a name or a source to make a skill look finished; mark the gap `to confirm` and name who can fill it.

## Pitfalls

- Writing the skill from general knowledge. The Agent Skills guides name this as the main way to get a vague, generic skill.
- Adding text to please the checker. The rating measures documentation; a section that says nothing lowers the skill's value and still scores.
- A second skill for a topic one skill already owns; extend instead.
- Putting extra frontmatter keys at the top level. The specification allows six; the rest goes under `metadata`, and the SkillEvaluator's `version` check cannot be met without breaking distribution (see `quality-gates`).
- Reference files that link on to other reference files, a body over about 500 lines, and a description that names no boundary.
- Declaring the skill reviewed or verified. Only the owner can.

## Definition of done

- The brief is agreed; the skill passes the registry validator, the specification export, the OKF check and the figures check.
- Its quality rating is recorded and, as a proposed target, is B or higher.
- Test cases and trigger queries are written (and run, or stated as not run).
- Registry, flow and README entries exist; the owner has reviewed the pull request.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/skill-anatomy.md`](references/skill-anatomy.md) | Writing the skill: frontmatter, sections, sizes, naming, sources |
| [`references/quality-gates.md`](references/quality-gates.md) | Passing the gates: commands, what each finding means, known conflicts |
| [`references/evaluation-design.md`](references/evaluation-design.md) | Designing test cases and trigger queries |
| [`assets/skill-brief.md`](assets/skill-brief.md) | Step 3: the one-page brief |
| [`assets/release-checklist.md`](assets/release-checklist.md) | Step 9: the checklist before the pull request |
| [`assets/evals-template.json`](assets/evals-template.json) | Step 8: the shape of `evals/evals.json` to copy |
| [`references/background.md`](references/background.md) | You need context and rationale; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
| [`references/outputs.md`](references/outputs.md) | The output contract in full (generated from outputs.yaml) |
