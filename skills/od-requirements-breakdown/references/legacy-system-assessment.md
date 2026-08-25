# The (legacy) MF IT system assessment

Half of UC-03's stated output: *"integration-ready requirement spec **+ legacy MF IT system
assessment**"*. It answers one question — **does this requirement need, replace, or collide
with something already installed?** — and it is the step that catches a requirement about to
rebuild what exists.

**268 legacy applications are tracked.** Check against them before specifying anything.

---

## What the list holds

| Category | Apps |
|---|--:|
| PLC programming / configuration | 73 |
| Laboratory software | 52 |
| Equipment configuration | 33 |
| Camera system configuration | 25 |
| Custom SCADA | 15 |
| Printer | 12 |
| Quality software | 10 |

By function:

| Functional mapping | Apps |
|---|--:|
| PLC Programming & Configuration | 124 |
| Quality Laboratory Data Acquisition | 41 |
| Manufacturing Execution System (MES) | 19 |
| Quality Data Acquisition | 15 |
| Logistics | 13 |
| Machine / Process Data Acquisition (MDA/PDA) | 5 |
| Traceability | 4 |

**70 of the applications are deployed at exactly one plant.** A single-deployment application
is both the easiest to replace and the most likely to be somebody's daily tool that nobody
outside that plant knows about.

---

## The four questions

### 1 · Does something already do this?

Search the list by **functional mapping** first, then category. A requirement whose function
is already covered is one of three things, and they are not the same:

| Finding | Then |
|---|---|
| The existing app does it well | **Refuse the build.** Integrate with it, or do nothing |
| The existing app does it badly | The requirement is a *replacement* — say so, and scope the migration |
| The existing app does part of it | Scope the delta only, and state the boundary explicitly |

### 2 · Is it supported?

| Support concept | Apps | Means |
|---|--:|---|
| Internal Support | 86 | Somebody here maintains it — find out who |
| External Support Contract | 35 | A contract exists; check its scope |
| Maintenance & Run Concept | 33 | Documented run concept |
| *(not recorded)* | 114 | **Unknown — the largest group** |

And supplier status: **48 `IN SERVICE`, 2 `SERVICE STOPPED`**, the rest unrecorded.

> A `SERVICE STOPPED` application in the requirement's path is a **major blocking point**, not
> a footnote. So is an unrecorded one until somebody checks.

### 3 · What does the licence cost?

| Licence | Apps |
|---|--:|
| **unknown** | **128** |
| No licence required | 67 |
| Local licence available | 57 |
| OESL licence required | 15 |

**128 of 268 unknown.** If the requirement depends on an application with an unknown licence
position, that is a real dependency with a real lead time — record it in §7 and give it an
owner. Licensing is a recurring blocker class in the corpus.

### 4 · Does it fit the footprint?

The strategy is a deliberately **small operational footprint**, and broad tool proliferation
is an explicit non-bet. Apply the deployment reality:

| System | Status | Consequence for a requirement |
|---|---|---|
| **MES** | Rollout on hold, ERP/S4HANA-dependent, 2 plants in progress | A requirement depending on MES rollout is **blocked, not planned**. Check light-weight substitutes such as QFPR |
| **MSB** | Limited | Confirm availability at *this* plant before depending on it |
| **MDA/PDA** | ≈16 deployed | Likely available; verify per plant |
| **MIL** | High demand, not deployed | Do not depend on it |
| **EMS** | Deployed, rollout stopped pending operational criteria | Do not extend it |
| **IIoT Edge** | Significantly deployed | The safe assumption |

**A requirement that needs a system outside the footprint is refused at intake** and routed
to strategy as a tool-rollout decision. It is not a use case, and treating it as one produces
an item that sits in the portfolio for a year.

---

## What the assessment records

Add this to §8 of the requirement:

```
Systems required:        ⟨list⟩
Footprint verdict:       inside · outside → refuse & route · substitute available ⟨name⟩
Legacy applications touched:
  ⟨app⟩ | ⟨category⟩ | ⟨plants⟩ | support: ⟨concept⟩ | supplier: ⟨status⟩ | licence: ⟨status⟩
Relationship:            integrate with · replace · unaffected
Owner to consult:        ⟨name⟩
```

**"Unaffected" is a valid and useful answer** — but only once it has been checked. The 268
applications exist precisely because nobody checked, repeatedly.

---

## The trap this step exists to catch

A requirement that looks new and is not. The corpus records blockers like
*"potentially needed: QFPR?"* and *"open access to ⟨vendor⟩ system (API)"* — both are this
assessment surfacing late, as a blocker, instead of early, as a decision.

Doing it at requirement time costs an hour. Doing it at integration time costs the slot.
