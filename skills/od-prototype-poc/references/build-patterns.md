---
type: Skill Reference
title: Build patterns
description: "Build patterns for the click-dummy: layout, navigation, states, data stubs, design tokens and the verification pass."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [prototype, click-dummy, department-package]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/30-skills/product-funnel-skills.zip/skills/click-dummy/references/build-patterns.md, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `product-funnel-skills.zip/skills/click-dummy/references/build-patterns.md` (the master).

# Build Patterns

Battle-tested structure for a single-file click dummy. This shell has carried a
19-route enterprise CRM with full create flows in one 2,500-line file with no
build step. Swap the route cases and the `render*` bodies; the rest is
domain-agnostic.

## Layout

```
index.html          the whole dummy — HTML, CSS, JS inline
verify.py           the real-browser verification script (KEEP THIS)
prototype-notes.md  handover doc
```

## Order of construction

1. CSS tokens and app shell
2. State and mock data
3. Router and dispatch
4. Shared primitives (`esc`, `badge`, `card`, `dataTable`, `emptyState`)
5. Screens, one at a time
6. Create flows
7. Verification script

Sections 1–4 in one pass. If you must chunk the file, confirm each insertion
marker appears exactly once immediately before writing to it.

## State

```js
const mockData = { /* one array per entity, cross-linked by string id */ };

const state = {
  route:'dashboard', recordId:null, tab:null,
  currentUser:{ name:'…', role:'…', initials:'…' },  // ask, don't invent
  filters:{}, searchQuery:''
};
let idSeq = 1000;
function uid(prefix){ idSeq++; return prefix+'-'+idSeq; }
```

Direct mutation. No reducer. Every mutating action ends in a re-render.

## Hash router

Hash routing gives working browser back/forward for free, and shareable
deep links, with no server.

```js
function parseHash(){
  const h = location.hash.replace(/^#\/?/,'');
  if(!h) return { route:'dashboard', id:null, tab:null };
  const p = h.split('/');
  return { route:p[0]||'dashboard',
           id:p[1]?decodeURIComponent(p[1]):null,
           tab:p[2]?decodeURIComponent(p[2]):null };
}

function nav(route, id, tab){
  let h = '#/'+route;
  if(id)  h += '/'+encodeURIComponent(id);
  if(tab) h += '/'+encodeURIComponent(tab);
  if(location.hash === h){ handleRoute(); } else { location.hash = h; }
}

window.addEventListener('hashchange', function(){ handleRoute(); });

function handleRoute(keepTab){
  const p = parseHash();
  state.route = p.route; state.recordId = p.id;
  state.tab = keepTab ? state.tab : p.tab;
  renderSidebar(); renderTopbar(); renderPage();
  const pb = document.getElementById('pageBody'); if(pb) pb.scrollTop = 0;
}
```

The `location.hash === h` branch matters: assigning an unchanged hash fires no
`hashchange`, so without it a re-nav to the current route silently does nothing.

## Dispatch

```js
function renderPage(){
  let html = '';
  switch(state.route){
    case 'dashboard': html = renderDashboard(); break;
    // one case per route; each render* returns an HTML string
    default: html = renderDashboard();
  }
  document.getElementById('pageBody').innerHTML = html;
}
```

Full rebuild per navigation. Simple, and no stale-view bugs.

## Shared render helpers

```js
function esc(s){
  return (s==null?'':String(s)).replace(/[&<>"']/g, function(c){
    return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]; });
}

function badge(text, cls){
  return '<span class="badge '+(cls||'badge-neutral')+'">'+esc(text)+'</span>';
}

function dataTable(cols, rows, opts){
  opts = opts || {};
  if(!rows.length) return emptyState(opts.emptyMsg || 'No records found.');
  const head = '<tr>'+cols.map(function(c){ return '<th>'+esc(c.label)+'</th>'; }).join('')+'</tr>';
  const body = rows.map(function(row){
    const cells = cols.map(function(c){ return '<td>'+c.render(row)+'</td>'; }).join('');
    const click = opts.onRowClick ? ' onclick="'+opts.onRowClick(row)+'"' : '';
    return '<tr'+click+'>'+cells+'</tr>';
  }).join('');
  return '<div class="table-wrap"><table class="data-table"><thead>'+head+
         '</thead><tbody>'+body+'</tbody></table></div>';
}
```

`dataTable` typically carries most list screens and much of the detail views.
Build it early and well.

### Shared helpers must not assume route-specific elements

This is the highest-severity known trap. A helper writing unconditionally to an
element that exists only on some routes throws on every other route, and the
render aborts **before the page body is written** — so the failure looks like a
blank page, not like a broken breadcrumb.

```js
function setPageMeta(title, breadcrumbParts){
  document.getElementById('pageTitleEl').textContent = title;
  // breadcrumbEl exists only on detail routes; list pages must not assume it.
  const bc = document.getElementById('breadcrumbEl');
  if(bc) bc.innerHTML = breadcrumbParts ? breadcrumbHtml(breadcrumbParts) : '';
}
```

Better still, pass the target element in rather than looking it up globally.

## Create flows

One shape, reused for every "New X":

```js
function submitNewThing(){
  const title = document.getElementById('newThingTitle').value.trim();
  if(!title){ showToast('Please enter a title.'); return; }   // validate
  const id = uid('thing');
  mockData.things.push({ id:id, title:title, /* … */ });      // mutate
  closeModal();                                               // dismiss
  showToast('Thing '+id+' created (session only).');           // confirm + mark fidelity
  nav('thing', id);                                            // land on the record
}
```

The `(session only)` in the toast is a fidelity marker doing real work — it
tells the user the record will not survive a reload, at the moment they create it.

## Transient panels: clear, never remove

```js
function closeAllDropdowns(){
  ['quickAddMenu','searchResults','notifPanel'].forEach(function(id){
    const el = document.getElementById(id);
    if(el) el.innerHTML = '';        // NOT el.remove()
  });
}
```

`.remove()` deletes the node permanently. The first close works; every
subsequent open writes into nothing, with no console error. Silent, and easy to
misread as a rendering problem.

## CSS tokens

```css
:root{
  --bg:#f3f4f6; --surface:#fff; --surface-alt:#f8f9fb;
  --border:#e2e5ea; --border-strong:#cfd4dc;
  --text:#1a2233; --text-muted:#5c6579; --text-faint:#8992a3;
  --accent:#245b9c; --accent-bg:#e8f1fa;
  --success:#177a4c; --success-bg:#e5f6ec;
  --warning:#a86412; --warning-bg:#fbf0dc;
  --danger:#b13327;  --danger-bg:#fbeae8;
  --radius:6px; --shadow:0 1px 3px rgba(15,23,42,.08);
}
.app{ display:flex; height:100vh; overflow:hidden; }
.sidebar{ width:224px; flex-shrink:0; overflow-y:auto; }
.main{ flex:1; display:flex; flex-direction:column; min-width:0; }
```

Paired `--x` / `--x-bg` for each status colour covers badges and banners without
a second token layer. Base font around 13px suits dense business UI — it is not
a marketing page. Derive the actual palette from the brief via `frontend-design`;
this is the token *structure*, not a mandated look.

## Verification script

Real browser. Keep it in the repo.

```python
# verify.py — Playwright against installed Chrome; no bundled browser download
from playwright.sync_api import sync_playwright

ROUTES = ['dashboard','customers','contacts', ...]           # every route
DETAILS = [('customer','cust-001'), ('rfq','rfq-2026-10001')] # every detail+tab

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    page = b.new_page()
    errors = []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)

    for r in ROUTES:
        page.goto(f"file://{PATH}#/{r}")
        page.wait_for_timeout(150)
        assert page.locator("#pageBody").inner_html().strip(), f"{r}: empty body"

    # then: every detail route + tab, every create flow submitted for real,
    # every button clicked. Assert `errors` is empty at the end.
```

Assert the page body is non-empty per route. A render that aborts mid-way leaves
an empty container while the shell still looks fine — a screenshot will not
catch it, and neither will a smoke test that only checks the page loaded.

**Never substitute a stubbed `document` or DOM shim.** A shim that auto-creates
elements on request returns a live object for the very element whose absence is
the bug, passes every check, and reports confident success while the app is
broken in every real browser.

## Selector discipline in verification

Scope every selector to a container. Bare text matching is the most common
source of false failures:

```python
pg.click("button.primary:has-text('Add')")   # ALSO matches "Add task" — wrong element
pg.click(".modal button.primary")            # unambiguous
pg.click("#pageBody button.primary:has-text('Add task')")
pg.click(".topbar button:has-text('Duplicate')")
```

Playwright resolves an ambiguous locator to the *first* match and proceeds, so
the failure surfaces as a timeout somewhere unrelated — a debugging round that
looks like an app bug and is not.

## Checking the demo makes the case

Separate from checking the app runs. After the sweep passes, render the headline
comparison and read it:

```python
pg.goto(URL + "#/compare"); pg.wait_for_timeout(300)
print(pg.locator("#pageBody table").inner_text())
```

Confirm each KPI moves the direction the prototype's argument requires. Seed
data can be entirely plausible and still tell the opposite story — that is
invisible in the code and obvious in the rendered table. If a KPI moves the
wrong way, decide whether the sample is unrepresentative or the metric itself is
wrong; the second case is a requirements finding for the open-questions section,
not a bug to patch.

## Coverage assertions in the verification script

A button sweep iterates over controls that exist, so it is structurally blind to
a missing one. Assert coverage explicitly, driven by the entity list rather than
by the DOM:

```python
# For each entity, the route where it is managed and the control that creates it.
COVERAGE = {
    "scenario": ("#/scenarios",              "New scenario"),
    "station":  ("#/scenario/sc-1/layout",   "Add station"),
    "task":     ("#/scenario/sc-1/tasks",    "Add task"),
    "operator": ("#/scenario/sc-1/operators","Add operator"),
}

for entity, (route, label) in COVERAGE.items():
    pg.goto(URL + route); pg.wait_for_timeout(120)
    btn = pg.locator(f"#pageBody button:has-text('{label}')")
    check(btn.count() > 0, f"{entity}: no create control on {route}")
```

Then actually exercise each one — open the form, submit it, and assert the
record count went up. A create button that opens a modal which does nothing is
worse than no button.

The list is written from the state model, not from the screens. That is the
whole point: it fails when a screen is missing, which is exactly the case the
sweep cannot reach.

## Walking the demo story as a user

Scripted tests navigate by URL, so they never discover that a screen is
unreachable by clicking. Add one pass that starts at the entry route and uses
only on-screen controls:

```python
pg.goto(URL)                      # entry only — no deep links after this
pg.click("#pageBody tbody tr >> nth=0")
pg.click(".tabs .tab:has-text('Operators')")
```

If a step needs a hardcoded id or a route you typed rather than clicked, the
prototype has an unreachable screen — a real finding, even though every
individual control works.
