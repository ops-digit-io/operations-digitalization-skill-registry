---
type: Design Record
title: Derivation
description: Every skill traced back to the knowledge graph concept it came from, with the judgement calls, the corrections the corpus forced, and what was deliberately left out.
resource: ../registry.yaml
status: stable
owner: human:jakob.gabriel
tags: [derivation, provenance]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# How this registry was derived

Every skill in this registry traces to concepts in the `ops-digit-io/ops-knowledge-graph`
bundle. Nothing here was invented. Where the source carried an explicit gap — the `⟨…⟩`
convention — the gap is carried through unchanged rather than filled.

## The two maps used

**The skill map** — the four service lines' own answer to "what may this lane work with,
and what does it repeatedly do":

```
_knowledge/OperationsDigitalization-Department/20-lanes/<lane>/
  skills.md       what the lane may work with, and with which access right
  tasks.md        the recurring tasks, their trigger and their template
  playbook.md     happy path, error paths, wait states, handover / rework rule
  metrics.md      the lane's own metrics, targets and intervention thresholds
  agent-brief.md  may / may not / authority_level / guardrails / escalation
```

**The Node-RED flow corpus** — 825 exported flow JSON files and their generated pages
across 53 `ct-oesl-*-nodered-*` instances, plus the generator that produces them:

```
_knowledge/node-red-auto-docs/docs/<instance>/<Flow_Name>.json   the flow, tab + nodes
_knowledge/node-red-auto-docs/docs/<instance>/<Flow_Name>.md     the generated page
_knowledge/node-red-auto-docs/generate_docs.py                   what reads which field
```

**The machine estate and its integration guidance** — the decision tree the Equipment
integration guide walks, and the machine and connector rows behind it:

```
_knowledge/_apps/machine-integration-guidance-app/rules.json       live tree, 25 q / 27 recs
_knowledge/_apps/machine-integration-guidance-app/rules-next.json  next tree, 35 q / 31 recs
_knowledge/90-Sources/generated/kg_nodes.csv                       1,715 Machine + 26 Connector
```

The raw SharePoint exports under `90-Sources/**/*.json` are Git-LFS pointers and were not
pulled; the machine and connector figures therefore come from the graph export
(`kg_nodes.csv`), which is the same data after the pipeline. Stated here because the two
could drift and the export is the one that was actually read.

**The Operations Digitalization department map** — how the department works:

```
_knowledge/OperationsDigitalization-Department/00-core/   charter, strategy, objectives,
                                                          service catalog, intake, operating
                                                          rhythm, metrics, decision rights,
                                                          risks, portfolio, SWOT, glossary,
                                                          resources
_knowledge/OperationsDigitalization-Department/10-modules/smart-factory-use-case/
                                                          systems-of-record, landscape,
                                                          capabilities, operating-context
_knowledge/10-Department/                                 operating model, use case lifecycle,
                                                          standardization, machine integration,
                                                          handover, savings, decision rights,
                                                          rituals, roles, systems of record
_knowledge/20-Done/                                       delivered methods and tooling
```

## Explicitly out of scope

The **Digital Unit** material — `_knowledge/260825_DU_Pilot_Business-Cases.md` and
`_knowledge/90-Sources/du-overview/**` — is excluded. The Digital Unit is a new department;
this registry describes Operations Digitalization as it works today. Nothing in any skill
is derived from that material.

## Traceability

| Skill | Primary sources |
|---|---|
| `od-context` | `00-core/01-charter`, `04-service-catalog`, `08-decision-rights`, `14-glossary`; `10-Department/Operating model`, `Systems of record`, `Roles and organization` |
| `od-use-case-support-service` | `20-lanes/use-case-support-service/*`; `10-Department/Use case lifecycle` |
| `od-information-integration-service` | `20-lanes/information-integration-service/*`; `10-Department/Machine integration` |
| `od-project-support-consultancy` | `20-lanes/project-support-consultancy/*`; `00-core/12-portfolio` |
| `od-analytical-support-service` | `20-lanes/analytical-support-service/*` |
| `od-use-case-intake-triage` | `00-core/05-intake`, `04-service-catalog`, `01-charter`, `13-swot` |
| `od-use-case-definition` | `20-lanes/use-case-support-service/{playbook,tasks}`; `10-Department/Use case lifecycle`, `Use case standardization` |
| `od-benefit-calculation` | `10-Department/Savings and value tracking`, `Decision rights`; `20-lanes/use-case-support-service/*` |
| `od-use-case-standardization` | `10-Department/Use case standardization`; `20-Done/AI cluster classification`, `Use case portfolio analysis` |
| `od-equipment-integration-assessment` | `10-Department/Machine integration`; `20-Done/Equipment integration guide`; `20-lanes/information-integration-service/*` |
| `od-requirements-breakdown` | `OperationsDigitalization-Department/OD_Skill_Map.md` (UC-03, P-04); the four `20-lanes/*/playbook.md` step 3; `90-Sources/generated/kg_nodes.csv` — field population across 650 use cases, the latent heading grammar inside `target_text`/`blockers`, and the 268 legacy applications; `usecase-standardization-knowledgebase.md`; `00-core/05-intake` and `15-resources` |
| `od-signal-standardization` | `node-red-auto-docs/docs/**` (260 signal names in use across 3,400 references); `90-Sources/org-analysis/usecase-standardization-knowledgebase.md` (ISO 22400-2, VDI 3423, ISA-95, ISO 22005); `10-Department/Use case standardization`; `20-lanes/information-integration-service/*`; `10-modules/.../systems-of-record` |
| `od-acceptance-test` | `20-lanes/{information-integration-service,project-support-consultancy}/{playbook,tasks,agent-brief}` |
| `od-handover-and-adoption` | `10-Department/Handover`, `Rituals`, `Use case lifecycle` |
| `od-data-availability-check` | `20-lanes/analytical-support-service/{playbook,tasks}`; `10-Department/Machine integration`; `10-modules/.../systems-of-record` |
| `od-analytics-asset-build` | `10-Department/Operating model`, `Rituals`; `20-Done/Grafana dashboard screenshot automation`; `20-lanes/analytical-support-service/*` |
| `od-scorecard-reporting` | `00-core/07-metrics`, `06-operating-rhythm`; all four `20-lanes/*/metrics.md` |
| `od-portfolio-and-savings-analysis` | `20-Done/Use case portfolio analysis`; `10-Department/Savings and value tracking`, `Use case lifecycle`, `Systems of record` |
| `od-decision-routing` | `00-core/08-decision-rights`, `09-risks`; `10-Department/Decision rights` |
| `od-sharepoint-list-export` | `20-Done/SharePoint list export procedure`; `90-Sources/sharepoint-export-playbook.md` |
| `od-machine-integration-guidance` | `machine-integration-guidance-app/dataFEEDOPCSuite_de.pdf` (Softing dataFEED OPC Suite V5.70 manual); `_apps/machine-integration-guidance-app/{rules,rules-next}.json`; `90-Sources/generated/kg_nodes.csv`; `10-Department/Machine integration`; `20-Done/Equipment integration guide` |
| `od-node-red-flow-builder` | `node-red-auto-docs/docs/**` (825 flows); `node-red-auto-docs/generate_docs.py`; `10-Department/Machine integration` |
| `od-node-red-flow-troubleshooting` | `node-red-auto-docs/docs/**` — every check is validated against all 825 flows, and its finding counts are the corpus's actual defect distribution |
| `build-grafana-ops-dashboard` | **not derived** — vendored from the author's skill, 2026-08-25 |

## Where this registry deliberately contradicts the bundle

**Read this before regenerating anything from the knowledge graph.** Three facts in the
source decks are out of date and were corrected here on the owner's instruction. Two of the
three are **now also fixed in the bundle** (`ops-knowledge-graph`, same branch): the
department instance no longer names MDL or ContiTech. The raw exports under `90-Sources/`
are never hand-edited, so the decks themselves still say the old thing — which is why this
table stays.

| The bundle says | Actually |
|---|---|
| **MDL** — "OESL Manufacturing Data Lake", the asset-to-cloud platform every lane reads and writes | **Not used.** The IIoT Edge Platform offloads through **Databricks** to an **Azure Storage Account**; the main file format is **Parquet** |
| **ContiTech** — shared services, interface compatibility as a standing constraint, ContiTech central as the counterpart on tool-rollout and data-model decisions, ContiTech tooling dependence as a standing risk | **Not used.** Removed throughout. Where a decision genuinely has a second party, the counterpart is left as `⟨to confirm⟩` rather than guessed |
| **OESL** as the business name | The business is now **neuwerk**. Prose that quotes or cites a source keeps the source's own wording; ⟨a full rename has not been done — see open gaps⟩ |

What was **kept**, deliberately, because they are live identifiers rather than references:

- the `ct-oesl-*-nodered-*` **repository names** — the doc generator matches on
  `^ct-oesl-.*-nodered-(prod|test).*`, so renaming them makes 825 flows undocumentable;
- the **`CT/…` MQTT topic root** and its `OESL` / `MFS` segments — a topic is an interface
  and every subscriber breaks; both are marked as legacy in `od-node-red-flow-builder`;
- **CT Base** as the recorded name of the data-model blocker on 23 machines — the estate
  says that, so the estate is quoted, with the current model name marked `⟨confirm⟩`.

**Fixed upstream** in the same branch of `ops-knowledge-graph`: `10-Department/Systems of
record.md` (which now carries the data path and the local-versus-global rule), the `00-core/`
charter, strategy, objectives, service-catalog, decision-rights, risks, SWOT, glossary and
resources files, all four lane packs, the smart-factory module, `OD_Skill_Map.md`, and the OD
README, which carries its own corrections table.

**Still outstanding upstream:** the `90-Sources/` decks (raw exports, not hand-edited) and
the OESL → neuwerk rename.

## Editorial decisions worth knowing about

**Three tiers, not one flat list.** The source has two natural layers — a department layer
that is true everywhere and a lane layer that is true in one service line — and a third
emerges from the tasks and playbooks: procedures that several lanes run identically
(acceptance testing, handover, data availability). Flattening them would duplicate the
guardrails into every skill, and duplicated guardrails drift.

**`od-context` is a skill, not a preamble.** The glossary and the honesty rules are the
part of the source that most changes an answer, and the source itself says why:
*inconsistent vocabulary is a top agent-failure cause*. Making it loadable means the rules
arrive with the work rather than being restated per skill.

**Figures are quoted with their read date, or not at all.** The Scorecard values are
2026-08-10; the portfolio and ledger figures are from the 2026-08-24 bundle. Both drift.
Every skill that carries a number says when it was read and tells the reader to refetch.

**Gaps stay gaps.** `⟨…⟩` is copied through. A registry that quietly resolves an open
question is worse than one that shows where the department has not decided yet.

**The Node-RED builder was re-measured after review, and the first cut was wrong about the
majority case.** The ten patterns were all framed single-input. Counting distinct
`datapoint*` config keys per flow showed **461 of 665 configured flows read two or more** —
so multi-input is the norm, not an edge case, and the latch-and-evaluate shape it requires
was absent. The same pass surfaced three more gaps the catalogue hid: windowed aggregation
(36 flows), a second timestamp envelope on JSON topics (75 flows) alongside `plcTime` as a
distinct clock (145 flows), and timer-driven emit. `composing-transformations.md` exists
because a catalogue answers "what has been built" and a builder also needs "what do I do
when mine is not in it".

**The Node-RED builder was tested by actually deploying its output.** A flow was generated
from the skill alone and started in Node-RED v5.0.4. It reached `Started flows` — but only
after three additions the skill did not mention, and the reason it did not is structural:
the corpus is the *per-flow* export, which contains a tab and its nodes and **nothing else**.
Across all 825 exports there are zero config nodes. So the derived patterns described a
correct transformation and an undeployable file. `deployable-flow.md` closes that, with the
palette module named and the config-node shapes taken from the flow that actually ran. It is
also a caution about derivation in general: a corpus can be complete for what it shows and
silently missing a whole layer.

**`od-signal-standardization` was promoted from practice to technical, because the evidence
turned it into a real analysis job.** Mining the flow corpus for `datapoint*` config keys
found **260 distinct signal names across 3,400 references** — eight for machine state alone,
seven for part number, and `AverageMeltTempature`, a misspelling with 34 references that is
now an interface. That is *data model standardization*, the estate's most-recorded
integration blocker at 23 machines, in measurable form. The skill gained a canonical
vocabulary, the normative KPI standards that decide which signals a capability needs before
any are chosen, and an analyser that checks a data-point list for collisions, raw PLC tags
and coverage gaps. Its rule — a signal is standardized when a second plant can consume it
without asking a question, which needs a name, a meaning, a unit and a collection method —
exists because the first three are visible in the data and the fourth is not.

**Adopting OKF was decided by one hard constraint, not by preference.** The registry was
Agent Skills format derived *from* an OKF bundle; making it an OKF bundle itself meant putting
`type` and `title` in the frontmatter. The Agent Skills spec allows exactly six top-level keys
in a `SKILL.md` — `name`, `description`, `license`, `compatibility`, `metadata`,
`allowed-tools` — and anything else fails packaging and upload with a hard error, not a
warning. Top-level OKF fields would have made all 24 skills undistributable: conformance
bought by breaking the artefact.

So a skill carries its OKF fields under `metadata`, which the spec defines as a free-form map
"read by your own tooling" — precisely this case. Every other concept carries ordinary
top-level frontmatter. Checking that constraint also turned up a live defect:
`build-grafana-ops-dashboard/SKILL.md` carried `argument-hint`, which is the exact key the
error message names, so that skill would have failed upload today.

Two of the knowledge-graph bundle's rules could not be copied unchanged. `title` must equal
the filename there, because filenames are human titles; here they are slugs fixed by the skill
layout, and renaming one breaks the paths inside `SKILL.md`. So `title` must *slug* to the
filename — `PLC packet` → `plc-packet.md` — which keeps the rule's purpose. And `SKILL.md`
carries no identity at all, being the same filename 24 times over, so the check moves to
`name` against the directory, which is what the loader uses and a stronger guarantee than the
rule it replaces.

`last_verified: 2026-08-25` came off all 24 skills. OKF derives its trust tier from `verified`
and nothing else; that field asserted a verification nobody performed and carried no actor, so
it could not produce a tier either way. It is now `sources_read`, which is what it always
meant. Every concept here is `unverified`, and that is accurate.

**The review found real bugs, and the pattern in them was worth more than any single fix.**
Four scripts hand-rolled their argument parsing, so `--lane=integration` and
`--capability=oee` were silently ignored — the check never ran and the tool printed *"ready to
hand over"*. That is worse than crashing. Both now use `argparse` with a closed choice list.
Two more were the same shape of error: `tokens()` lowercased before the camelCase split, so
the split never fired and the English guard was defeated, reporting `HeadTemperature` as a
German tag; and `setdefault` made the Portuguese and Serbian entries unreachable behind
Spanish, so `Temperatura_Bico` reported as Spanish. The second now reports
`Spanish/Portuguese` — a term two languages spell the same way is ambiguous, and saying so
beats picking one. Three call sites read the label column with three different key sets, so a
`uuid,Label` export analysed clean and then reported every signal as unnamed; one `cell()`
helper now reads all of them case-insensitively.

The registry's `authority_level` had drifted into paraphrase of each skill's own, and in one
case granted `execute-autonomously` where `od-analytical-support-service` capped at
*recommend*. The two are now the same string and `validate_registry.py` fails if they differ,
because a machine-readable index must not be able to widen a skill's authority. It also now
refuses a `⟨…⟩` placeholder inside metadata: in prose a placeholder marks an open gap, which
is the point; in metadata a consumer reads it as the value.

**The epic layer was already there, and finding that changed what the skill had to do.**
The plan was to design an epic/user-story format. Then `usecase-epics-user-stories.md` turned
up in the knowledge graph: the SharePoint list encodes a two-axis hierarchy in its own
`UseCaseParentId` and `UseCaseParent-ProcessId` fields, and the generated register already
renders 22 process epics, 11 capability epics and 650 leaf user stories.

Counting what is inside them changed the design. Of the 650 leaf stories, 429 carry a target
text and 466 carry some narrative — but **59** carry an "I want" tag, so 591 render as
*"I want (not tagged)"*; **3** mention acceptance criteria anywhere; and **0** carry a "so
that" that differs from the generated clause *"…so that the process gains transparency, faster
reaction and less manual effort"*, which is appended identically to all 650.

I had also expected the filled fields to be hollow forms — headings with nothing under them.
They are not: of 429 filled target texts, 0 contain only headings. The estate fills what it
is asked for in a meeting and leaves blank what needs a conversation with an operator. So the
skill does not introduce a structure; it attacks a benefit clause that fits anything, and
`check_epic.py` refuses a "so that" built only from generic benefit words. That check earned
its place by failing first — the phrase survived an initial version because "the process
gains" is not itself a benefit word, so the check now strips filler as well.

The background description the user asked for lands against the department's own stated risk:
the skill map calls this step *"the most dependent on tacit judgement, and the one currently
held by a departing individual."* A background naming what happens today, the moment of use,
the decision it changes, why now, and what it is not for, is what remains once that individual
has gone.

**Tags are multilingual, and the corpus proved it rather than the assumption doing so.**
Scanning every label, node name and comment for non-ASCII characters found Chinese at Qingdao
and Changshu (`存储设定值` — store setpoint value; `流程` — process), German at Waltershausen and
Karben (`Rüstzeit`, `Rüstmonitor`, `Heizungsart`), and Spanish at Delicias and Monterrey
(`Pza`, `Contador`, and the misspelling `Cointador`). Six further plant languages are in scope
and simply have not reached the corpus yet.

Building the matcher took three rounds of correction, each caught by testing rather than
review: `Rüstzeit` was missed because accent-folding gives `rustzeit` while the dictionary key
was `ruestzeit`; `Darabszamlalo` was missed because Hungarian and German compound their words,
so a substring pass had to follow the token pass; and English `Temperature` was *wrongly*
reported as German `Temperatur`, which a guard list of English terms now vetoes — a check that
mislabels English as foreign would be worse than no check. The rule the reference settles is
that the canonical name is English and the local name is an alias, kept in the report and the
Machine CV because the data-point contract has only one label field.

**The signal skill takes two inputs because one was never enough.** A tag list gives names;
only the machine context gives meanings, and `CycleTime` from two plants is not comparable
unless somebody knows where each machine's cycle starts. The context sources are ranked by
confidence rather than treated as equivalent — a live data-point config is verified, a
deployed PLC program is high, a tag export is high for existence and low for meaning, a verbal
description is low. The reason this had to be written at all is a gap in the estate:
`documentation_available` and `documentation_link` exist as fields on all 1,715 machine rows
and are populated on none, so there is no system of record for the context and it must be
gathered per machine.

The output is a defined report, and the split between what the tool fills and what it leaves
as `⟨…⟩` is deliberate. Inventory, canonical mapping, clustering, coverage and findings are
derivable from names and are generated. How the machine works, which sources were used, units,
collection method and owners are not, and a report that guessed at them would be worse than
one that asks — that guess is exactly how `AverageMeltTempature` reached 34 flows.

**The requirements skill formalizes a template the estate had already half-written.** The
headings it uses — `Use Case Target Overview` (99 use cases), `Major Issue` / `Key Problem`
(44), `Tags of Interest` (29), `Acceptance criteria` (13), `Traces to` (13), `Major` / `Minor
Blocking Points` (162) — were found inside the existing free-text `target_text` and `blockers`
fields, not designed. Imposing a new form on a department that already has one would have
been the wrong move; the finding is that the form exists and is used on about one use case in
eight.

The field-population profile also decided the *order* of the elicitation questions.
`savings_eur` is populated on 100 % of 650 use cases and `targets` on 9 %, while `comment`,
`methods`, `actions`, `utilization` and `csp_decision` are on none — what gets asked for in a
meeting is recorded, what needs a conversation with the operator is not. The question rounds
are ordered to get the 0 % and 9 % answers first, because the savings figure will be filled in
regardless.

**Two things in the signal skill come from outside the bundle, and are labelled as such.**
The public data models — OPC UA for Machinery (VDMA 40001), EUROMAP 77/83/84, PackML
(ISA-TR88.00.02) — were retrieved from the specification bodies' own pages and are cited
inline; the specifications themselves were not read in full, so the mappings are marked as a
starting point to confirm rather than a conformance statement. The clustering and importance
patterns are the opposite: derived entirely from the portfolio's own `ai_cluster`,
`business_process` and `targets` fields, which is why the reference states plainly that those
fields are populated on 150 and 59 of 650 use cases and that a low rank therefore means
unknown demand rather than none.

**The one shipped flow asset was deployed before it was documented, and the test found a
bug in it.** `assets/protobuf-schema-bootstrap.flow.json` writes the PLCPacketList schema to
a new instance's file store. The first version started cleanly, logged no error, and wrote
nothing: it set the `file` node's `filenameType` to `msg` while leaving `filename` empty, so
the node evaluated an unnamed property. The estate's own flows avoid this only because they
use the pre-V3 form Node-RED upgrades in place — copying their `file` node into a modern
flow and modernising one field breaks it silently. The asset now sets
`filename: "filename"`, and both the write and a protobufjs round-trip of the written schema
are verified on Node-RED v5.0.4. The analyser also caught a real defect in the first draft
(`protoPath` read but never set), which is the tooling working on its own registry's output.

**Examples are generalized on purpose.** Every example in `artefacts.md` uses `cfg.<name>`
config keys and `⟨…⟩` placeholders — no real UUIDs, machine names, endpoints or credentials,
verified by grep. The corpus has 42 flows with committed secrets; a reference that pasted
real identifiers would propagate exactly that.

**One skill ships an executable, and it was calibrated on the corpus rather than guessed.**
`od-node-red-flow-troubleshooting/scripts/analyze_flow.py` runs over all 825 flows with zero
parse failures, and every check earns its place by finding a defect that is actually present.
Calibration mattered: an early version of the flow-context check fired on 575 flows, which is
70 % and therefore noise. Splitting it into a real read of unset context (99) and a copied
`Debug flow config` echo (94) made it a finding instead of a nag. The counts in the skill are
the analyser's own output, so they can be re-derived by re-running it.

**The technical tier is measured, not asserted.** The Node-RED and machine-integration
skills state frequencies (620 of 825 flows carry a *prepare and convert payload* group;
1,032 of 1,715 machines are Siemens; 1 % of flows carry a description) because a house
pattern claimed without a count is one person's preference. Every number in those two
skills was computed over the corpus, and the computation is reproducible from the paths in
the traceability table. Where the corpus is inconsistent, the skill says so rather than
picking a winner.

**One skill is vendored, and it kept its name.** `build-grafana-ops-dashboard` is
domain-generic and already had an identity, including a cross-reference to `/build-dashboard`
that would break under a rename. Its body and its 22 reference files are unchanged; the only
edit is an added `metadata:` block in the frontmatter. That made a second scope necessary:
`od` skills inherit the department's vocabulary and must require `od-context`, while a
`portable` skill instead ships an `od_integration` note saying what changes when it is used
for OD work. The validator enforces both halves, so a future vendored skill cannot quietly
skip the integration note.

**References carry patterns, not statistics.** The machine-integration references were
rebuilt around what a reader has to *do*: `decision-paths.md` (four gates, routing,
connector selection, dead ends), `softing-datafeed.md` (per-driver configuration procedures
for the Central Aggregation Server), `iiot-edge-platform.md` (the six phases and the
hardware sequence) and `fallbacks.md` (the eight ways an integration blocks and what to try
first). An earlier pair of reference files that were mostly estate breakdowns was removed —
a distribution table tells a reader what the estate looks like, not what to do next, and
the few figures that genuinely change a routing decision now sit in `SKILL.md` with the
consequence attached.

**The Softing material is now grounded in the vendor manual, and the disagreements are
reported rather than resolved.** The dataFEED OPC Suite V5.70 manual (1,540 pp.) reached the
bundle after the first pass; the Softing references were rewritten against it with page
references throughout, and two OESL recommendations turned out to describe steps the product
cannot perform — a Beckhoff/ADS data source that does not exist, and a NetLink protocol
discontinued in V5.38. Neither was quietly corrected in the skill: `rules.json` stays
authoritative for what OESL permits and the manual for what the product does, the mismatch
is stated in `SKILL.md` and both references, and the fix is recorded in `registry.yaml` as a
change owed to `rules.json`. A skill that silently patched the guidance would leave the tool
everyone actually uses still wrong.

**A topology error, corrected twice.** An earlier version of the machine-integration skill
presented the IIoT Edge Platform and the Central Aggregation Server as alternative
destinations. They are not: the edge is the terminus, and machines behind the Softing server
are integrated into it **via OPC UA** using the `DTQ-OPCUA-Connector`. The guide says so in
two places — its `IIoT Edge Platform → OPC-UA Server` recommendation *is* that bridge, and
its Siemens S7 aggregation recommendation states the PLCs cannot be connected without the
edge platform as well.

The second correction split the remaining "direct" case in two, giving **three ingress
variants**: PLC → **edge device** with connector → platform; PLC → **connector** → platform,
with no device at the machine; PLC → **aggregation server** → platform. That is not an
invention — it is exactly the three concepts the Tool Overview already records as *Concept 3
— IIoT Edge Computing Platform* (20 plants), *Concept 2 — container-based Machine
Integration* (1 plant), *Concept 1 — Central OPC-UA Server* (11 plants). Reading the rollout
histories also killed a second assumption: **eight plants carry both the edge and the
aggregation concept**, so "which platform does this plant have" is often the wrong question.

Both corrections propagated through all six references, the skill's topology diagram, the
worked example and the two adjacent skills. Wording moved from "two routes" to "three ingress
variants, one terminus", because the earlier phrasing was itself carrying the error.

**One name per thing, stated once.** The sources disagree on what to call the two routes —
the Equipment integration guide says *IIoT Edge Platform* and *Central Aggregation Server*,
the department notes say *IIoT edge computing platform* and *central OPC-UA server*, and the
recommendation bodies add *Softing OPC-UA Aggregation Server* and *Softing DataFeed*. Rather
than pick one and silently rewrite the others, `od-machine-integration-guidance` carries a
Terminology table mapping canonical name to alias to what the thing actually is, states that
the concept and the route are the same thing seen from two sides, and the adjacent skills
(`od-equipment-integration-assessment`, `od-information-integration-service`) now name both
and point here for per-machine routing. The rule for prose: use the guide's wording when
handing someone a procedure, because that is the label on their screen.

**Secrets found in the source are named, never reproduced.** The flow corpus contains 23
literal Teams webhook URLs and 30 literal Bearer tokens. The Node-RED skill states the
counts and makes replacing them a guardrail; no skill or reference file contains one, and
the finding is listed in `registry.yaml` under `open_gaps` so it reaches someone who can
rotate them.

**Some procedures deliberately became one skill, not several.** Signal standardization and
pipeline construction are steps 3 and 4 of one playbook but one write right and one
decision mode, so they are one skill. Acceptance testing appears in two lanes with one
protocol, so it is one skill referenced twice.

## Keeping this registry true

The knowledge graph is the source; this registry is derived. When a lane pack, a core file
or a `10-Department` concept changes:

1. Re-read the changed concept.
2. Update the skills listed against it in the traceability table.
3. Update `last_verified` in the affected skills' frontmatter and the `data_as_of` /
   `graph_as_of` / `flows_as_of` fields in `registry.yaml`.
   For the technical tier, re-run the counts over the corpus rather than editing a figure
   by hand — the numbers are the evidence, and a hand-edited one stops being that.
4. Run `python3 scripts/validate_registry.py`.

Corrections to the underlying facts do not belong here or in the graph — they go to the
SharePoint list that owns them. See `od-context`, "Where the truth lives".

## Verification status

**Unverified.** Every derived skill was drafted from the bundle; nobody has read them line
by line against the source systems. `build-grafana-ops-dashboard` is vendored and carries
its author's own status. That is accurate, not modest — it matches the source bundle's
own trust statement. Add a verification note to a skill's frontmatter once somebody has.
