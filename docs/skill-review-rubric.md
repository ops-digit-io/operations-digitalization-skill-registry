---
type: Design Record
title: Skill review rubric
description: The criteria this registry reviews a skill against, taken from Anthropic's skill authoring best practices and the open Agent Skills specification and guides, each with the source quote, whether it is measured or judged, and how a reviewer rates it.
status: draft
owner: human:jakob.gabriel
tags: [skills, review, rubric, anthropic]
generated: { by: claude-code/1, at: 2026-11-16T00:00:00Z }
---
# Skill review rubric

Every criterion comes from a source opened and read on 2026-11-16. Quotes are verbatim and short; the key says where each comes from. A criterion here is what the source says, not this registry's own threshold.

## Sources

| Key | Source | Publisher |
|---|---|---|
| AB | Skill authoring best practices, <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices> | Anthropic |
| AO | Agent Skills overview, <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview> | Anthropic |
| EN | Equipping agents for the real world with Agent Skills (Anthropic Engineering, published Oct 16, 2025), <https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills> | Anthropic |
| AS | Agent Skills specification, <https://agentskills.io/specification> | agentskills.io |
| AP | Best practices for skill creators, <https://agentskills.io/skill-creation/best-practices> | agentskills.io |
| AE | Evaluating skill output quality, <https://agentskills.io/skill-creation/evaluating-skills> | agentskills.io |
| AD | Optimizing skill descriptions, <https://agentskills.io/skill-creation/optimizing-descriptions> | agentskills.io |
| AU | Using scripts in skills, <https://agentskills.io/skill-creation/using-scripts> | agentskills.io |

The sources differ on one point: AB says "Always write in third person." for the description, AD says "Frame the description as an instruction to the agent: "Use this skill when..."". The review therefore asks for one consistent point of view, not a specific one.

## Measured facts (`scripts/skill_facts.py`; not judged)

| Id | Fact | Source quote | Key |
|---|---|---|---|
| F1 | Name: at most 64 characters, lowercase letters, numbers and hyphens, no leading, trailing or double hyphen, equals the directory, no `anthropic` or `claude` | "Must not start or end with a hyphen"; "Must match the parent directory name"; "Cannot contain reserved words" | AS, AB |
| F2 | Description is non-empty, at most 1024 characters, no XML tags | "Maximum 1,024 characters" | AB, AS |
| F3 | `SKILL.md` body under 500 lines | "Keep the `SKILL.md` body under 500 lines for optimal performance." | AB, AS |
| F4 | `SKILL.md` body under about 5,000 tokens (estimated as characters / 4) | "**Instructions** (< 5000 tokens recommended)" | AS |
| F5 | References one level deep from `SKILL.md` | "Keep references one level deep from `SKILL.md`." | AB, AS |
| F6 | Reference files over 100 lines have a table of contents | "For reference files longer than 100 lines, include a table of contents at the top." | AB |
| F7 | Forward slashes in paths | "Always use forward slashes in file paths, even on Windows" | AB |
| F8 | Scripts accept arguments and document usage, do not prompt, use exit codes | "Avoid interactive prompts"; "Document usage with `--help`"; "Meaningful exit codes" | AU |
| F9 | Evaluations exist (`evals/evals.json`) | "At least three evaluations created" | AB, AE |
| F10 | No time-sensitive dates in the body (candidates only; a reviewer decides) | "Don't include information that will become outdated" | AB |

## Judged criteria (a reviewer reads the skill and cites evidence)

Rating per criterion: **meets**, **partly**, **gap** or **n/a**. Every rating other than n/a needs a quote from the skill (at most 25 words) as evidence; partly and gap need one concrete change.

| Id | Criterion | Source quote | Key |
|---|---|---|---|
| J1 | The description says what the skill does and when to use it, with key terms a user would use | "Include both what the Skill does and specific triggers/contexts for when to use it."; "Should include specific keywords that help agents identify relevant tasks" | AB, AS, AD |
| J2 | The description keeps one point of view and states user intent, not implementation | "Focus on user intent, not implementation."; "inconsistent point-of-view can cause discovery problems" | AD, AB |
| J3 | Concise: it adds only what the agent lacks | "Would the agent get this wrong without this instruction?" If the answer is no, cut it. | AP, AB |
| J4 | Specificity matches fragility: freedom where several approaches work, exact steps where an operation is fragile | "Match the level of specificity to the task's fragility and variability." | AB, AP |
| J5 | Procedures over declarations: it teaches how to approach a class of problems, with clear steps | "A skill should teach the agent *how to approach* a class of problems, not *what to produce* for a specific instance."; "Workflows have clear steps" | AP, AB |
| J6 | Defaults, not menus | "pick a default and mention alternatives briefly rather than presenting them as equal options"; "Don't present multiple approaches unless necessary" | AP, AB |
| J7 | A gotchas or pitfalls section sits in `SKILL.md` | "The highest-value content in many skills is a list of gotchas" | AP |
| J8 | Where output format matters, a concrete template | "Provide templates for output format."; "agents pattern-match well against concrete structures" | AB, AP |
| J9 | Examples are concrete, not abstract | "Examples are concrete, not abstract" | AB |
| J10 | Multi-step or fragile work has a checklist, a validation loop or plan-validate-execute | "Run validator -> fix errors -> repeat"; "For batch or destructive operations, have the agent create an intermediate plan ... validate it ..., and only then execute." | AB, AP |
| J11 | Progressive disclosure is used well: detail is in separate files and `SKILL.md` says when to read each | "Read `references/api-errors.md` if the API returns a non-200 status code" is more useful than a generic reference. | AP, AB |
| J12 | Consistent terminology | "Choose one term and use it throughout the Skill" | AB |
| J13 | It explains the why where the reason changes behaviour | "Reasoning-based instructions ("Do X because Y tends to cause Z") work better than rigid directives" | AE |
| J14 | Scripts solve problems instead of deferring, handle errors, give helpful messages, state their dependencies | "handle error conditions rather than deferring to Claude"; "Write helpful error messages"; "State prerequisites" | AB, AU |
| J15 | The skill is one coherent unit | "Skills scoped too narrowly force multiple skills to load for a single task"; "Skills scoped too broadly become hard to activate precisely." | AP |
| J16 | It is grounded in real expertise and sources | "Effective skills are grounded in real expertise." | AP |

## Overall rating

The reviewer gives one overall rating, **strong**, **adequate** or **needs-work**, and states the reason in one sentence. It is a judgement with evidence, not a computed score. The number of gaps and partly ratings is reported next to it for transparency.

## What this review does not do

- It does not run the skill. The sources ask for evaluations: "Create evaluations BEFORE writing extensive documentation", with test cases run with and without the skill ("once **with the skill** and once **without it**") and assertions graded with evidence (AE). No skill here has evaluations yet (F9). Behaviour is therefore not measured.
- It does not test the skill with different models, which AB asks for: "Test your Skill with all the models you plan to use it with."
- A reviewer reading the text judges the text. Treat the ratings as a structured first reading, to be confirmed by running the skills.
