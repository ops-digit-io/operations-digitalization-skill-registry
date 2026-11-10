---
type: Skill Reference
title: Multilingual tags
description: "Tags in nine plant languages: the normalization before any comparison, the term table, and why the local name is an alias not a replacement."
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [signals, translation, multilingual]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Multilingual tags — translating what the plant actually wrote

The estate runs plants in three regions, and a PLC programmer names tags in the
language they think in. So the tag list you are handed is not in English, and treating it as
though it were is how a signal gets misread rather than merely misnamed.

**This is not hypothetical.** Examples found in the flow corpus:

| Language | Found |
|---|---|
| **Chinese** | `存储设定值` *(store setpoint value)* · `流程 1`, `流程 3` *(process 1, 3)* |
| **German** | `Rüstzeit` *(setup time)* · `Rüstmonitor` · `Rüstvorgang läuft` *(setup running)* · `Extrusionslinie` · `Heizungsart` *(heating type)* · `Kessel` *(vessel)* |
| **Spanish** | `Pza` *(pieza — piece)* · `Contador` / `Cointador` *(counter, misspelled)* · `Suciion descarga` *(suction discharge, misspelled)* |

Plus the plants whose language has not reached the corpus yet but will: **Romanian** (Carei,
Timisoara), **French** (Caluire, Rennes, Tanger), **Hungarian** (Mako), **Serbian**
(Subotica), **Slovak / Czech** (Dolne Vestenice, Ostrava), **Portuguese** (Ponta Grossa).

---

## The rule

> **The canonical name is English. The local name is an alias, not a replacement.**

Not because English is better, but because the whole point of a canonical vocabulary is that
one plant's solution is takeable by the next — and a name only one plant can read defeats
that. The same argument that makes `MachineState` and `MachineStatus` a problem makes
`Rüstzeit` and `SetupTime` one.

**But the local name is not noise, and must not be discarded.** It is what the operator, the
setter and the PLC programmer at that plant call the thing. Losing it means the next
conversation at that machine starts from nothing.

**The data-point contract has one label field** — `uuid` and `label`, nothing else. So the
label carries the canonical name, and the local name lives in the **signal analysis report**
and the **Machine CV**. That is a constraint of the contract, not a preference. ⟨Whether the
edge platform can carry a second display field — to confirm.⟩

---

## What the analyser does

```bash
python3 scripts/analyze_signals.py points.json
```

| Check | Severity | Fires on |
|---|---|---|
| `local-language-name` | WARN | A term from one of the nine languages, with a canonical suggestion where the term maps cleanly |
| `non-latin-script` | WARN | Chinese, Cyrillic, Japanese, Korean, Greek, Arabic |
| `mixed-script-name` | **BLOCKER** | Latin and non-Latin in one label — e.g. `Temp压力`. Unmatchable, and usually a copy-paste artefact |

The report's inventory gains a **Lang** column, so every row shows what was found, in what
language, and what it maps to.

**How the matching avoids false positives.** English `Temperature` is *not* reported as the
German `Temperatur`, because a name already canonical or a known English variant is skipped
outright, exact word tokens are matched before substrings, and a guard list of English terms
vetoes the substring pass. `Compteur pieces` still matches French `compteur` — one English
word in the label does not make the label English.

**Compounding languages are handled.** German and Hungarian glue words together —
`Zykluszeitmessung`, `Darabszamlalo` — so a substring pass follows the token pass. Both
`Rüstzeit` and the unaccented `Rustzeit` match, because both spellings occur.

---

## Normalization, before anything is compared

Applied automatically, and worth understanding because it silently prevents a class of bug:

| Step | Why |
|---|---|
| **Unicode NFC** | `ü` composed vs `u` + combining diaeresis look identical and compare unequal |
| **Strip format characters** | Zero-width spaces occur in the estate's own comment text; a label carrying one never matches |
| **Non-breaking space → space** | Same problem, more common |
| **Accent-fold for matching only** | `Rüstzeit` → `rustzeit` to compare. **Never for display** — never rename somebody's signal to an unaccented spelling |
| **Umlaut expansion** | `ü` → `ue` as a second form, because German uses both |

---

## The term table

The analyser carries terms for German, Spanish, Portuguese, French, Romanian, Hungarian,
Slovak/Czech, Serbian and Chinese. The families that matter most:

| Concept | DE | ES | FR | RO | HU | CS/SK | ZH |
|---|---|---|---|---|---|---|---|
| Counter / piece | Stückzahl, Zähler | Pza, Contador | Compteur, pièce | Piesă, Contor | Darab, Számláló | Počítadlo | 计数器 |
| Cycle time | Zykluszeit | Ciclo | Cycle | — | — | — | 周期 |
| Pressure | Druck | Presión | Pression | Presiune | Nyomás | Tlak | 压力 |
| Temperature | Temperatur | Temperatura | Température | — | Hőmérséklet | Teplota | 温度 |
| Speed | Geschwindigkeit | Velocidad | Vitesse | Viteză | — | — | 速度 |
| Setup / changeover | Rüstzeit, Rüsten | — | — | — | — | — | — |
| Fault / alarm | Störung, Meldung | Falla, Alarma | Défaut | Defect | — | Porucha | 故障, 报警 |
| Tool / mould | Werkzeug | Molde | Moule | Matriță | — | — | 模具 |
| Setpoint | Sollwert | — | Consigne | — | — | — | 设定值 |
| Actual value | Istwert | — | — | — | — | — | — |
| Machine mode | Betriebsart | — | — | — | — | — | 状态 |

**`Sollwert` / `Istwert` / `设定值` / `Consigne` are the setpoint-versus-actual distinction**
in four languages. That distinction is the `_sv` modifier already in the topic convention, and
losing it in translation makes a dashboard compare a target with itself. It is the single
highest-value translation in the table.

⟨The table is a starting point, not a linguist's work. Extend it per plant, and have a native
speaker at the site confirm the entries for their language before relying on them.⟩

---

## The procedure

**1 · Normalize and detect.** The analyser does this. Anything non-Latin or mixed-script is
flagged before you read further.

**2 · Get a native reading, not a machine translation.** Ask somebody at the plant what the
tag means *on that machine*. A term can be a false friend — Chinese `流程` is *process* in the
sense of a sequence, not a process value.

> **Never machine-translate a signal name and use the result directly.** `设定值` renders as
> "set value", which reads like a command rather than a setpoint. A wrong reading here
> propagates into every flow, topic and dashboard downstream, and by then it is an interface.

**3 · Map to canonical.** Standard vocabulary first, public data model second —
`signal-catalogue.md`, `public-data-models.md`.
A public companion specification is already language-neutral, which is another reason to adopt
one.

**4 · Record the alias.** In the report's inventory (`Candidate (as found)` and `Lang`) and in
the Machine CV. **The alias is the audit trail for the rename** and the thing the next person
at that machine needs.

**5 · Decide whether to rename.** Renaming a live signal is a **breaking change**. If it is
already consumed, either migrate its consumers or record the deviation and standardize the
next one. A misspelled name that many flows already read is the cautionary case: it is now an interface.

---

## What not to do

- **Do not translate the local name and treat that as canonical.** *Setup time* is a
  translation of `Rüstzeit`; `SetupTime` is a canonical name. They coincide here and will not
  always.
- **Do not leave a non-Latin label as the data-point label.** It cannot be matched against the
  vocabulary and does not survive every downstream consumer.
- **Do not mix scripts in one name.** `Temp压力` is unmatchable in both languages.
- **Do not "correct" a local spelling as a side effect.** `Cointador` is a typo for
  `Contador`, and both are aliases of `TotalPartCounter` — fix it in the canonical mapping,
  not by editing somebody's PLC tag.
- **Do not assume the plant language from the country.** Confirm it; multinational sites and
  vendor-supplied programs routinely differ from the local language.
