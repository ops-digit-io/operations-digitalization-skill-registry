---
type: Skill Reference
title: AI governance
description: Governance for GenAI proofs of concept, agentic workflows, AI-built apps and AI assistants - start conditions, scope limits, intake path, fit criteria and the maturity sanity check - with the step ids where each applies.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, ai]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# AI governance

## 1 AI maturity check (i1, 21, 24, 31)

Value-creation maturity ladder: data anarchy, reporting, data-driven processes, data-centric
architecture, data economy. AI is useful from the third level up. Use it as a go / no-go sanity check:
do not rank an AI use case above basic data-model and reporting work in a plant that has not reached
reporting; in the interim choose less demanding use cases. Quick triage grid for AI ideas: low barrier
and high potential, mid barrier and high potential, high barrier and mid potential. Value / risk rule
(`od-prototype-poc`): build low-risk, high-value; run a cheap test where risk and value are both high;
do not build low value.

## 2 AI idea collection (i1, 21)

Requester enters the idea in a shared list; OD is notified and holds a short call with the standard
questions; the idea is recorded and later prioritised into initiatives. Set the expectation that not every
idea is ready to run. Pilot approach: listen to process and plant specialists, get clear targets and
measurables, check which data is acquired and how reliable and complete it is, decide in a workshop or
assessment, then run the pilot (external expert if needed); train the team on the tools first; start with
labelled data, first insights, first model, test the first pilot model. Cancel with a recorded reason when
the data foundation is missing.

## 3 GenAI proof-of-concept governance (step 23 / 31; fits the "lead change" bucket of triage)

- Frame the pilot as: understand the applications, feasibility study, pilot proposal, roadmap, training.
- Write the **advantage statement** you would claim (what would be the edge) before the pilot.
- **Time-box** the pilot and the understanding-building; success targets are stated up front
  (`<time-box>`, `<accuracy threshold>`: not in the sources).
- Train the users before the pilot, record lessons for the rollout.
- PoC (feasibility), prototype (benefit with real users), pilot and rollout stay four different claims (`od-prototype-poc`); a pilot result is never
  reported as proven value.
- The Lead-change label is a human call; an agent may propose it and cite the facts used.

## 4 Agentic-workflow governance (step 31 / 32, then wherever the agent runs)

- **Phases:** map the manual workflows and choose the top candidates; build pilot agents; test with
  champion users; scale with a governance model and an agent-development playbook.
- **Start rule (`PROPOSAL`, chain rule):** an agent step starts only when a human has named the process
  owner, the data source and the review point.
- **MVP shape:** narrow scope - one input format, one trigger, no user interface. An MVP without a review
  screen is acceptable only for **read-only extraction** (`PROPOSAL`); anything that writes, sends or
  decides needs a review point.
- **Guiding questions:** market and tools, scalability, risk management, effect on the department's
  strengths, fit with lean admin processes, process-design principles.
- **Benefits are phrased as** time freed, decision quality, knowledge retention; measure what you claim
  (`<measure>`).
- Keep a risk register and an adoption target per agent; the owner confirms adoption
  (`od-handover-and-adoption`).

## 5 AI-built app intake path (between Lane 2 step 23 and Lane 3a, steps 3a4-3a6)

1. **Prompt-to-prototype is a demo of value, not a delivery.** Record it as a prototype (`od-prototype-poc`).
2. **Choose the sourcing route** (`deploy-appstore`): internal; external with source owned (treated as
   internal); external without source (image and deployment files only, highest effort).
3. **Assume supplier code is partly AI-generated** and ask the supplier to say which parts.
4. **IT takeover:** a business owner, an IT owner, a service concept, roles, requirements, a change
   process and a risk process exist before productive use (`od-system-fit-check`).
5. **Cyber Security approval** through `od-cybersec-gate`, planned as work (explanation of the app,
   network and components, scans, tests, documentation). It is human-only and has no fast path.
6. **Deploy** through `deploy-appstore`; the deployment set may be drafted by an assistant.
- Any plant software is approved by OD and IT so that data, interface and knowledge domains integrate.

## 6 AI platform and tool fit (31, 32)

Check, before any scaling: governed model operations (audit trail), no use of company data for model
training, alignment with the single-sourcing rule of purchasing, cyber-security baseline, data
protection. Prove the foundations before the request, not after.

## 7 Assistants and prompt library (i1, 21, 3b4)

- A custom assistant fits where the task is repetitive, the skill set is public or general, and good
  internal documentation exists. It works as well as that documentation.
- Typical personas: summariser, translator, domain interpreter. For foreign-language or external source
  material, chain the steps: pre-process, correct misunderstandings, summarise as key facts, translate,
  then ask what it means for us.
- Troubleshooting assistant: a photo plus a short problem statement is enough for a first diagnosis; the
  assistant asks back for missing detail and gives soft guidance by action level (process or machine,
  tool, part), with no hard parameter values. `PROPOSAL`: cite the failure-catalogue entry per measure.
- Keep reusable prompts, agents and skills in one shared library with an owner.
- Classification gap: see the first open point in `SKILL.md`.

## 8 Source-code and know-how security (3b4)

Key machine programs held by individuals or suppliers: one versioned knowledge base with controlled
external access; first scope limited to governance, version control and code understanding by an
assistant; live shopfloor connection deferred. Foundations first: security, data protection, AI data use,
purchasing alignment. Downloads to machines stay on the traditional route.
