#!/usr/bin/env python3
"""Build the static documentation site: the interactive process map, one page per skill, the spec page and the downloads.

    python scripts/build_site.py [--out site] [--repo-url https://github.com/<org>/<repo>]

Inputs: registry.yaml, docs/new-state/process.yaml, skills/, docs/. Output (default `site/`, not committed):
  index.html            the process map: lanes, steps, the skills of each step; click a skill for details and links
  skills/<name>/        the skill rendered as HTML (SKILL.md, references, assets) and its files
  docs/                 the repository docs rendered, plus the four New-State files as supplied
  spec/index.html       conformance with the open Agent Skills specification, per skill
  downloads/            spec-strict zip per lane and per skill (metadata flattened, links between skills made textual)
Everything is static and works from the file system. Needs PyYAML and Markdown (pip install pyyaml markdown).
"""
from __future__ import annotations

import html
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
import skillpaths as skp
sys.path.insert(0, str(Path(__file__).resolve().parent))
import agent_skills_spec as spec  # noqa: E402

EXT = ["tables", "fenced_code", "sane_lists"]
CSS = """
:root{color-scheme:light dark;--bg:#f4f6fb;--surface:#fff;--ink:#1b1e52;--muted:#5b6082;--line:#d9dde9;--accent:#273993;--sun:#ffa500;
--ok:#156e4e;--ok-bg:#e2f1ea;--warn:#8a5a00;--warn-bg:#fff3df;--grey:#6b6f85;--grey-bg:#eceef5;--wait:#c8472b}
@media(prefers-color-scheme:dark){:root{--bg:#10122b;--surface:#191c3d;--ink:#e8eaf8;--muted:#a3a8cc;--line:#2c3066;--accent:#8fa0ff;--ok:#6fd3a8;--ok-bg:#12372b;--warn:#ffc266;--warn-bg:#3b2d10;--grey:#a3a8cc;--grey-bg:#23264d;--wait:#ff8a6b}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--accent)}code,pre{font-family:ui-monospace,Consolas,monospace;font-size:.88em}
header.top{background:#1b1e52;color:#fff;padding:18px max(16px,calc((100% - 1180px)/2))}
header.top a{color:#cdd6ef;text-decoration:none}header.top nav{display:flex;gap:18px;flex-wrap:wrap;font-size:13px;margin-bottom:6px}
header.top h1{margin:2px 0 0;font-size:22px}header.top p{margin:4px 0 0;color:#cdd6ef;font-size:14px;max-width:70ch}
main{max-width:1180px;margin:0 auto;padding:18px 16px 60px}
.bar{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:12px 0}
.bar input[type=search]{flex:1 1 240px;padding:9px 12px;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink);font:inherit}
.tabs{display:flex;gap:6px;flex-wrap:wrap}.tabs button{border:1px solid var(--line);background:var(--surface);color:var(--ink);padding:7px 12px;border-radius:999px;cursor:pointer;font:inherit}
.tabs button[aria-selected=true]{background:var(--accent);color:#fff;border-color:var(--accent)}
.legend{display:flex;gap:14px;flex-wrap:wrap;font-size:13px;color:var(--muted);margin:6px 0 14px}
.chip{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--line);border-radius:7px;padding:3px 9px;font-size:12.5px;background:var(--surface);color:var(--ink);cursor:pointer;margin:2px 4px 2px 0;font-family:inherit}
.chip i{width:9px;height:9px;border-radius:50%;display:inline-block;background:var(--ok)}
.chip.draft i{background:var(--warn)}.chip.proposed{border-style:dashed}.chip.sel{outline:2px solid var(--accent)}
.chip.hide{display:none}.legend .chip{cursor:default}
.lane{background:var(--surface);border:1px solid var(--line);border-radius:12px;margin:0 0 18px;overflow:hidden}
.lane>h2{margin:0;padding:12px 16px;font-size:17px;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;border-bottom:1px solid var(--line)}
.lane>h2 small{font-weight:400;color:var(--muted);font-size:13px}.lane>p{margin:0;padding:10px 16px 0;color:var(--muted)}
.lane .zip{margin-left:auto;font-size:13px;font-weight:400}.branch{padding:6px 16px 14px}.branch h3{margin:12px 0 6px;font-size:13px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted)}
.steps{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px}
.step{border:1px solid var(--line);border-top:4px solid var(--accent);border-radius:9px;padding:9px 11px;background:var(--bg)}
.step b{display:block;font-size:14px}.step .w{color:var(--wait);font-size:12px;font-weight:600}.step p{margin:3px 0 6px;font-size:13px;color:var(--muted)}
aside#panel{position:fixed;right:0;top:0;bottom:0;width:min(440px,100%);background:var(--surface);border-left:1px solid var(--line);box-shadow:-8px 0 30px rgba(0,0,0,.18);padding:18px 18px 40px;overflow:auto;transform:translateX(105%);transition:transform .2s;z-index:5}
aside#panel.open{transform:none}aside#panel h2{margin:0 0 4px;font-size:18px}aside#panel .x{position:absolute;right:12px;top:10px;border:0;background:none;color:var(--ink);font-size:22px;cursor:pointer}
aside#panel dl{display:grid;grid-template-columns:auto 1fr;gap:4px 12px;font-size:13.5px}aside#panel dt{color:var(--muted)}aside#panel dd{margin:0}
.btn{display:inline-block;border:1px solid var(--accent);color:var(--accent);padding:6px 11px;border-radius:7px;text-decoration:none;font-size:13.5px;margin:4px 6px 4px 0}
.btn.primary{background:var(--accent);color:#fff}
.card{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px 20px;margin:14px 0}
table{border-collapse:collapse;width:100%;font-size:14px;display:block;overflow-x:auto}th,td{border:1px solid var(--line);padding:6px 9px;text-align:left;vertical-align:top}th{background:var(--grey-bg)}
pre{background:var(--grey-bg);padding:10px 12px;border-radius:8px;overflow:auto}.md img{max-width:100%}
.badge{display:inline-block;padding:1px 8px;border-radius:999px;font-size:12px;font-weight:600}.b-ok{background:var(--ok-bg);color:var(--ok)}.b-warn{background:var(--warn-bg);color:var(--warn)}.b-grey{background:var(--grey-bg);color:var(--grey)}
footer{max-width:1180px;margin:0 auto;padding:0 16px 40px;color:var(--muted);font-size:13px}
@media(max-width:700px){header.top h1{font-size:19px}.steps{grid-template-columns:1fr}}
"""


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def fm_of(path: Path):
    return spec.split(path.read_text(encoding="utf-8"))


def first_sentences(text: str, n: int = 2) -> str:
    text = " ".join(str(text).split())
    parts = re.split(r"(?<=[.!?])\s", text)
    return " ".join(parts[:n])


def md_to_html(text: str, from_dir: Path, site_root: Path) -> str:
    h = markdown.markdown(text, extensions=EXT)

    def fix(m):
        href = m.group(1)
        if href.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        base, _, frag = href.partition("#")
        if base.endswith("SKILL.md"):
            base = base[:-8] + "index.html"
        elif base.endswith("index.md"):
            base = base[:-8] + "index.html"
        elif base.endswith(".md"):
            base = base[:-3] + ".html"
        return f'href="{base}{"#" + frag if frag else ""}"'

    return re.sub(r'href="([^"]*)"', fix, h)


def page(title: str, body: str, depth: int, active: str = "", extra_head: str = "") -> str:
    up = "../" * depth
    nav = (f'<a href="{up}index.html">Process map</a><a href="{up}spec/index.html">Specification</a>'
           f'<a href="{up}docs/new-state-skill-map.html">Skill map table</a><a href="{up}docs/new-state-flow.html">Flow notes</a>'
           f'<a href="{up}downloads/core-library.zip">Core library</a> '
           f'<a href="{up}downloads/extension-library.zip">Extension library</a> '
           f'<a href="{up}downloads/all-skills.zip">Download all</a>')
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(title)}</title><style>{CSS}</style>{extra_head}</head><body>'
            f'<header class="top"><nav>{nav}</nav><h1>{esc(title)}</h1></header><main>{body}</main>'
            f'<footer>OD skill registry. Draft content is marked; skills are AI-assembled from the department record and not yet reviewed by a human.</footer></body></html>')


def build(out: Path, repo_url: str) -> None:
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    reg = yaml.safe_load((ROOT / "registry.yaml").read_text(encoding="utf-8"))
    proc = yaml.safe_load((ROOT / "docs/new-state/process.yaml").read_text(encoding="utf-8"))
    ids = skp.all_ids()

    # ---- spec-strict export + zips
    export = out / "_export"
    results = {}
    for n in ids:
        spec.export_skill(skp.skill_dir(n), export)
    for n in ids:
        e, w, d = spec.check(export / n)
        se, sw, sd = spec.check(skp.skill_dir(n))
        results[n] = {"export_errors": e, "source_errors": se, "source_warnings": sw, "metadata_non_string": sd}
    dl = out / "downloads"
    (dl / "skills").mkdir(parents=True)

    def zip_skills(names, target: Path):
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
            for n in names:
                for f in sorted((export / n).rglob("*")):
                    if f.is_file():
                        z.write(f, f"{n}/{f.relative_to(export / n).as_posix()}")

    for n in ids:
        zip_skills([n], dl / "skills" / f"{n}.zip")
    zip_skills(ids, dl / "all-skills.zip")
    core_ids = [n for n in ids if skp.library_of(n) == "core"]
    ext_ids = [n for n in ids if skp.library_of(n) == "extension"]
    zip_skills(core_ids, dl / "core-library.zip")
    zip_skills(ext_ids, dl / "extension-library.zip")

    # ---- skill facts
    info = {}
    regmap = {s["id"]: s for s in reg["skills"]}
    for n in ids:
        fm, body = fm_of(skp.skill_dir(n) / "SKILL.md")
        meta = fm.get("metadata") or {}
        files = {k: sorted(p.name for p in (skp.skill_dir(n) / k).glob("*") if p.is_file() and p.name != "index.md")
                 for k in ("references", "assets", "scripts") if (skp.skill_dir(n) / k).is_dir()}
        info[n] = {"id": n, "desc": " ".join(str(fm.get("description", "")).split()), "short": first_sentences(fm.get("description", ""), 1),
                   "state": "draft" if str(meta.get("status")) == "draft" else "built", "tier": meta.get("tier", ""), "lane": meta.get("lane", ""),
                   "authority": meta.get("authority_level", ""), "summary": regmap.get(n, {}).get("summary", ""), "files": files,
                   "words": len(body.split()), "steps": [], "library": skp.library_of(n)}

    # ---- lanes for the map
    lanes = []
    zips = {}

    def add_steps(lane_id, lane_title, branch_title, step, proposed_flag_skills):
        for s in step.get("skills", []):
            info[s]["steps"].append({"lane": lane_id, "laneTitle": lane_title, "branch": branch_title, "step": step["title"], "proposed": False})
        for s in step.get("proposed", []):
            info[s]["steps"].append({"lane": lane_id, "laneTitle": lane_title, "branch": branch_title, "step": step["title"], "proposed": True})

    intake = proc["intake"]
    lanes.append({"id": "intake", "title": intake["title"], "who": intake["who"], "summary": intake["summary"],
                  "branches": [{"id": "intake", "title": "", "steps": intake["steps"]}]})
    for l in proc["lanes"]:
        lanes.append({"id": l["id"], "title": l["title"], "who": l["who"], "summary": l["summary"], "branches": l["branches"]})
    sp = proc["spine"]
    lanes.append({"id": "spine", "title": sp["title"], "who": "Across all lanes", "summary": sp["summary"],
                  "branches": [{"id": "spine", "title": "", "steps": [{"id": "sp", "title": "Applies across the lanes", "text": "", "skills": sp["skills"], "proposed": sp["proposed"]}]}]})
    un = proc["unplaced"]
    lanes.append({"id": "unplaced", "title": un["title"], "who": "Decision open", "summary": un["summary"],
                  "branches": [{"id": "unplaced", "title": "", "steps": [{"id": "un", "title": "Not on the flow", "text": "", "skills": un["skills"], "proposed": []}]}]})
    for l in lanes:
        members = []
        for b in l["branches"]:
            for st in b["steps"]:
                add_steps(l["id"], l["title"], b["title"], st, None)
                members += st.get("skills", []) + st.get("proposed", [])
        zips[l["id"]] = sorted(set(members))
        zip_skills(zips[l["id"]], dl / f"{l['id']}.zip")
        l["zip"] = f"downloads/{l['id']}.zip"
        l["count"] = len(zips[l["id"]])
    for n in ids:
        info[n]["zip"] = f"downloads/skills/{n}.zip"
        info[n]["page"] = f"skills/{n}/index.html"
        info[n]["github"] = f"{repo_url}/blob/main/{skp.folder_of(n)}/{n}/SKILL.md"

    # ---- map page
    data = json.dumps({"lanes": lanes, "skills": info}, ensure_ascii=False).replace("</", "<\\/")
    n_built = sum(1 for v in info.values() if v["state"] == "built")
    body = f"""
<p>{len(ids)} skills ordered along the new-state process flow: pick a lane, a step, then a skill. {n_built} are in use, {len(ids) - n_built} are drafts.
A dashed outline marks a skill this registry <em>proposes</em> for a step; the New-State files do not name it there.</p>
<div class="bar"><input id="q" type="search" placeholder="Search a skill, a step or a word (e.g. cyber, template, rollout)" aria-label="Search"><label><input type="checkbox" id="prop" checked> show extension skills (second library)</label></div>
<div class="tabs" role="tablist" id="tabs"></div>
<div class="legend"><span class="chip"><i></i>in use</span><span class="chip draft"><i></i>draft</span><span class="chip proposed"><i></i>extension library (optional)</span><span><b style="color:var(--wait)">~wks</b> external wait after the step</span></div>
<div id="lanes"></div><aside id="panel" aria-live="polite"></aside>
<script id="data" type="application/json">{data}</script>
<script>
const D=JSON.parse(document.getElementById('data').textContent);const $=s=>document.querySelector(s);
const esc=t=>String(t).replace(/[&<>"]/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]));
let cur='all';
function chip(id,prop){{const s=D.skills[id];return `<button class="chip ${{s.state==='draft'?'draft':''}} ${{prop?'proposed':''}}" data-skill="${{id}}" data-prop="${{prop?1:0}}" title="${{esc(s.short)}}"><i></i>${{esc(id)}}</button>`}}
function render(){{
  const q=$('#q').value.trim().toLowerCase();const showProp=$('#prop').checked;
  $('#tabs').innerHTML=[['all','All lanes']].concat(D.lanes.map(l=>[l.id,l.title])).map(([id,t])=>`<button role="tab" aria-selected="${{cur===id}}" data-tab="${{id}}">${{esc(t)}}</button>`).join('');
  $('#lanes').innerHTML=D.lanes.filter(l=>cur==='all'||cur===l.id).map(l=>{{
    const br=l.branches.map(b=>{{
      const steps=b.steps.map(st=>{{
        const all=[...(st.skills||[]).map(i=>[i,false]),...(showProp?(st.proposed||[]).map(i=>[i,true]):[])];
        const hit=!q||(st.title+' '+(st.text||'')).toLowerCase().includes(q)||all.some(([i])=>(i+' '+D.skills[i].short).toLowerCase().includes(q));
        if(!hit)return '';
        return `<div class="step"><b>${{esc(st.title)}}</b>${{st.wait?`<span class="w">wait ${{esc(st.wait)}}</span>`:''}}${{st.text?`<p>${{esc(st.text)}}</p>`:''}}${{all.map(([i,p])=>chip(i,p)).join('')}}</div>`}}).join('');
      return steps?`<div class="branch">${{b.title?`<h3>${{esc(b.title)}}</h3>`:''}}<div class="steps">${{steps}}</div></div>`:''}}).join('');
    if(!br)return '';
    return `<section class="lane" id="${{l.id}}"><h2>${{esc(l.title)}} <small>${{esc(l.who)}}</small><a class="zip" href="${{l.zip}}">Download ${{l.count}} skills (.zip)</a></h2><p>${{esc(l.summary)}}</p>${{br}}</section>`}}).join('')||'<p>No match.</p>';
}}
function open_(id){{const s=D.skills[id];if(!s)return;history.replaceState(null,'','#skill='+id);
  const where=s.steps.length?s.steps.map(x=>`<li><a href="#${{x.lane}}" data-tab="${{x.lane}}">${{esc(x.laneTitle)}}</a>${{x.branch?' / '+esc(x.branch):''}} / ${{esc(x.step)}}${{x.proposed?' <em>(proposed)</em>':''}}</li>`).join(''):'<li>Not placed on the flow.</li>';
  const f=Object.entries(s.files).map(([k,v])=>`<dt>${{k}}</dt><dd>${{v.map(esc).join(', ')}}</dd>`).join('');
  $('#panel').innerHTML=`<button class="x" aria-label="Close">×</button><h2>${{esc(id)}}</h2><p><span class="badge ${{s.state==='draft'?'b-warn':'b-ok'}}">${{s.state==='draft'?'draft':'in use'}}</span> <span class="badge b-grey">${{esc(s.tier)}}</span></p><p>${{esc(s.desc)}}</p>
  <p><a class="btn primary" href="${{s.page}}">Open the skill</a><a class="btn" href="${{s.zip}}">Download (.zip)</a><a class="btn" href="${{s.github}}">SKILL.md on GitHub</a></p>
  <dl><dt>Authority</dt><dd>${{esc(s.authority)}}</dd><dt>Old lane</dt><dd>${{esc(s.lane)}}</dd><dt>Size</dt><dd>${{s.words}} words</dd>${{f}}</dl><h3>Where it sits</h3><ul>${{where}}</ul>`;
  $('#panel').classList.add('open');document.querySelectorAll('.chip').forEach(c=>c.classList.toggle('sel',c.dataset.skill===id));}}
document.addEventListener('click',e=>{{const c=e.target.closest('[data-skill]');if(c){{open_(c.dataset.skill);return}}
  const t=e.target.closest('[data-tab]');if(t){{cur=t.dataset.tab;render();if(t.tagName==='A')setTimeout(()=>document.getElementById(cur)&&document.getElementById(cur).scrollIntoView(),0);return}}
  if(e.target.closest('.x')){{$('#panel').classList.remove('open');history.replaceState(null,'',location.pathname)}}}});
$('#q').addEventListener('input',render);$('#prop').addEventListener('change',render);
document.addEventListener('keydown',e=>{{if(e.key==='Escape')$('#panel').classList.remove('open')}});
const h=location.hash.slice(1);if(h.startsWith('skill='))setTimeout(()=>open_(h.slice(6)),0);else if(D.lanes.some(l=>l.id===h))cur=h;
render();
</script>"""
    (out / "index.html").write_text(page("OD skill registry: the process flow", body, 0), encoding="utf-8")

    # ---- skill pages
    for n in ids:
        sd = skp.skill_dir(n)
        od = out / "skills" / n
        shutil.copytree(export / n, od)
        fm, text = spec.split((export / n / "SKILL.md").read_text(encoding="utf-8"))
        i = info[n]
        where = "".join(f'<li><a href="../../index.html#{esc(x["lane"])}">{esc(x["laneTitle"])}</a>{" / " + esc(x["branch"]) if x["branch"] else ""} / {esc(x["step"])}{" <em>(proposed)</em>" if x["proposed"] else ""}</li>' for x in i["steps"]) or "<li>Not placed on the flow.</li>"
        files = "".join(f'<li>{k}: ' + ", ".join(f'<a href="{k}/{esc(Path(f).stem)}.html">{esc(f)}</a>' if f.endswith(".md") else f'<a href="{k}/{esc(f)}">{esc(f)}</a>' for f in v) + "</li>" for k, v in i["files"].items())
        head = (f'<div class="card"><span class="badge {"b-warn" if i["state"] == "draft" else "b-ok"}">{"draft" if i["state"] == "draft" else "in use"}</span> '
                f'<span class="badge b-grey">{esc(i["tier"])}</span> <span class="badge b-grey">{esc(i["lane"])}</span><p>{esc(i["desc"])}</p>'
                f'<p><b>Authority:</b> {esc(i["authority"])}</p><p><a class="btn primary" href="../../{i["zip"]}">Download this skill (.zip)</a>'
                f'<a class="btn" href="{esc(i["github"])}">On GitHub</a></p><h3>Where it sits in the process</h3><ul>{where}</ul><h3>Files</h3><ul>{files or "<li>SKILL.md only</li>"}</ul></div>')
        (od / "index.html").write_text(page(n, head + '<div class="card md">' + md_to_html(text, od, out) + "</div>", 2), encoding="utf-8")
        for sub in ("references", "assets"):
            for f in sorted((od / sub).glob("*.md")) if (od / sub).is_dir() else []:
                _, t = spec.split(f.read_text(encoding="utf-8"))
                crumb = f'<p><a href="../index.html">{esc(n)}</a> / {sub} / {esc(f.name)}</p>'
                f.with_suffix(".html").write_text(page(f"{n}: {f.stem}", crumb + '<div class="card md">' + md_to_html(t, f.parent, out) + "</div>", 3), encoding="utf-8")
        (od / "SKILL.md").unlink(missing_ok=True)

    # ---- docs
    dd = out / "docs"
    dd.mkdir()
    shutil.copytree(ROOT / "docs/new-state", dd / "new-state")
    shutil.copy2(ROOT / "docs/process-overview.html", dd / "process-overview.html")
    for f in sorted((ROOT / "docs").glob("*.md")):
        if f.name == "index.md":
            continue
        fm, t = spec.split(f.read_text(encoding="utf-8"))
        title = (fm or {}).get("title", f.stem)
        (dd / (f.stem + ".html")).write_text(page(str(title), '<div class="card md">' + md_to_html(t, dd, out) + "</div>", 1), encoding="utf-8")

    # ---- spec page
    rows = []
    for n in ids:
        r = results[n]
        ok_src = "b-ok" if not r["source_errors"] else "b-warn"
        ok_ex = "b-ok" if not r["export_errors"] else "b-warn"
        rows.append(f'<tr><td><a href="../skills/{n}/index.html">{n}</a></td><td><span class="badge {ok_src}">{"valid" if not r["source_errors"] else "errors"}</span>'
                    f'{"<br><small>" + esc("; ".join(r["source_errors"][:2])) + "</small>" if r["source_errors"] else ""}</td>'
                    f'<td>{len(r["metadata_non_string"])}</td><td><span class="badge {ok_ex}">{"valid" if not r["export_errors"] else "errors"}</span></td>'
                    f'<td>{len(r["source_warnings"])}</td></tr>')
    nsrc = sum(1 for r in results.values() if not r["source_errors"])
    nex = sum(1 for r in results.values() if not r["export_errors"])
    sbody = f"""
<div class="card"><p>The skills follow the open <b>Agent Skills</b> specification
(<a href="https://agentskills.io/specification">agentskills.io/specification</a>, reference validator
<a href="https://github.com/agentskills/agentskills/tree/main/skills-ref">skills-ref</a>). Each skill is a folder with a <code>SKILL.md</code> (YAML frontmatter and Markdown) and optional
<code>references/</code>, <code>assets/</code> and <code>scripts/</code>. An agent loads only the name and description at startup and reads the rest when a task matches.</p>
<table><tr><th>Field</th><th>Rule in the specification</th></tr>
<tr><td><code>name</code></td><td>1-64 characters; lowercase letters, digits and hyphens; no leading, trailing or double hyphen; equals the folder name</td></tr>
<tr><td><code>description</code></td><td>1-1024 characters: what the skill does and when to use it</td></tr>
<tr><td><code>license</code>, <code>compatibility</code></td><td>optional; compatibility 1-500 characters</td></tr>
<tr><td><code>metadata</code></td><td>optional; <b>a map from string keys to string values</b></td></tr>
<tr><td><code>allowed-tools</code></td><td>optional, experimental; a space-separated string, for example <code>Read Grep Bash(python3 scripts/x.py:*)</code></td></tr>
<tr><td>layout</td><td><code>SKILL.md</code> under 500 lines; references relative to the skill root and one level deep from <code>SKILL.md</code></td></tr></table></div>
<div class="card"><h2>How this registry meets it</h2><ul>
<li><b>{nsrc} of {len(ids)}</b> skill folders in the repository are valid against every rule except the type of <code>metadata</code> values.</li>
<li><b>Known deviation:</b> the registry keeps structured <code>metadata</code> (lists such as <code>requires</code>, and an <code>okf</code> block) because its own checks read them. The specification asks for string values.
The download packages are therefore <b>exported</b>: lists become comma-separated text, nested blocks become dotted keys, and links from one skill into another become a text reference, because a skill must work alone.
<b>{nex} of {len(ids)}</b> exported skills pass every rule.</li>
<li>The recommendation to keep references one level deep from <code>SKILL.md</code> is not met everywhere: references link on to other references (warnings column). The reference validator does not check this.</li>
<li>Check it yourself: <code>python scripts/agent_skills_spec.py --export dist</code> (exit code 1 on an invalid export), run in CI on every push.</li></ul></div>
<div class="card"><table><tr><th>Skill</th><th>Repository folder</th><th>metadata not text</th><th>Download package</th><th>Warnings</th></tr>{''.join(rows)}</table></div>"""
    (out / "spec").mkdir()
    (out / "spec" / "index.html").write_text(page("Agent Skills specification: conformance", sbody, 1), encoding="utf-8")
    shutil.rmtree(export)
    (out / ".nojekyll").write_text("", encoding="utf-8")
    print(f"site built in {out}: {len(ids)} skills, {len(lanes)} lanes/sections, {sum(1 for _ in out.rglob('*.html'))} html pages; spec-valid exports {nex}/{len(ids)}")
    return nex, nsrc, len(ids)


if __name__ == "__main__":
    a = sys.argv[1:]
    out = Path(a[a.index("--out") + 1]) if "--out" in a else ROOT / "site"
    repo = a[a.index("--repo-url") + 1] if "--repo-url" in a else "https://github.com/ops-digit-io/operations-digitalization-skill-registry"
    nex, nsrc, total = build(out.resolve(), repo)
    raise SystemExit(0 if nex == total else 1)
