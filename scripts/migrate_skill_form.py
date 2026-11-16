#!/usr/bin/env python3
"""One-time migration: SKILL.md becomes structure only, outputs.md becomes outputs.yaml.

    python scripts/migrate_skill_form.py [--dry] [<skill-id> ...]     # migrate (default: every skill)
    python scripts/migrate_skill_form.py --verify                     # nothing was lost, against git HEAD

Per skill it
  - moves every prose line of SKILL.md, unchanged (relative links become plain code text), to references/background.md,
    under the heading it stood below; the headings stay, empty required ones get a short pointer or standard items;
  - keeps every heading, table, list item and code block of SKILL.md in place;
  - turns references/outputs.md into outputs.yaml (the old text is kept in background.md), then scripts/skill_outputs.py
    regenerates outputs.md from it;
  - links every reference, asset and script file from the References table of SKILL.md, so none loses its link;
  - adds outputs.yaml and background.md to config/skill-deliverables.yaml.
The conversion of "Complete when" cells into criteria is mechanical: review the result per skill.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import skill_form as sf  # noqa: E402
import skillpaths as skp  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ("Purpose", "Inputs", "Procedure", "Human gate", "Definition of done", "Handoff", "Done when", "Do not", "Pitfalls", "Limitations", "References")
# Prose under these headings is context and moves to background.md; prose under every other heading is an instruction
# (steps, rules, gates, pitfalls, criteria) and stays in SKILL.md as short list items, one statement each.
CONTEXT = re.compile(r"(?i)^(introduction|example|where (it sits|the flow puts it)|the references are the substance|"
                     r"where it sits in the chain|purpose and where it sits)")
STD_DONE = ["Every output in [`outputs.yaml`](outputs.yaml) is done, with its evidence in the run record.",
            "Every check of `outputs.yaml` exited 0; every manual item names the role that signs."]
BG_HEAD = ("---\ntype: Skill Reference\ntitle: Background\n"
           "description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.\n"
           "resource: ../SKILL.md\nstatus: draft\ntags: [background]\n---\n# Background\n\n")
LINK = re.compile(r"\[([^\]]+)\]\(((?!https?://|mailto:|#)[^)]+)\)")


def plain(line: str) -> str:
    """Relative links become plain text with the path in code, so background.md links nothing."""
    return LINK.sub(lambda m: f"{m.group(1)} (`{m.group(2)}`)", line)


def slug(s: str, n: int = 40) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:n].strip("-") or "output"


def short(s: str, n: int = 40) -> str:
    w = s.split()
    return s if len(w) <= n else " ".join(w[:n]) + "…"


def first_sentence(par: str) -> str:
    par = re.sub(r"[*_`]", "", " ".join(par.split()))
    m = re.match(r".*?[.!?](?=\s|$)", par)
    return (m.group(0) if m else par)


# ---------------------------------------------------------------------------------------------------- SKILL.md
def strip_prose(body: str):
    lines = body.split("\n")
    kinds = {n: (k, l) for n, k, l in sf.classify(body)}
    out: list[str] = []
    moved: list[tuple[str, list[str]]] = []          # (heading, paragraphs)
    heading = "Introduction"
    par: list[str] = []

    def flush():
        nonlocal par
        if par:
            text_ = " ".join(x.strip() for x in par)
            if CONTEXT.match(heading) or heading.lower().startswith("purpose"):
                if heading.lower().startswith("purpose") and not heading.lower().startswith("purpose and"):
                    sents = [x for x in re.split(r"(?<=[.!?])\s+(?=[A-Z*`(\[\d])", text_) if x.strip()]
                    keep, rest = sents[:2], sents[2:]
                    for sent in keep:
                        out.extend(f"- {c}" for c in chunks(sent))
                    par = [" ".join(rest)] if rest else []
                    if not par:
                        return
                if not moved or moved[-1][0] != heading:
                    moved.append((heading, []))
                moved[-1][1].append("\n".join(plain(x) for x in par))
            else:
                sents = [x for x in re.split(r"(?<=[.!?])\s+(?=[A-Z*`(\[\d])", text_) if x.strip()]
                for sent in sents:
                    out.extend(f"- {c}" for c in chunks(sent))
                out.append("")
            par = []

    for i in range(len(lines)):
        k, l = kinds[i + 1]
        if k == "heading":
            flush()
            heading = l.lstrip("#").strip()
            out.append(l)
        elif k == "prose":
            if re.match(r"^Read `dept-context` first\.?\s*$", l.strip()):
                out.append("- Read `dept-context` first.")
            else:
                par.append(l.rstrip())
        else:
            if k == "blank":
                flush()
            out.append(l)
    flush()
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    return text, moved


def chunks(piece: str, limit: int = 40) -> list[str]:
    """Split a long statement at its natural joints until every part has at most `limit` words."""
    if len(piece.split()) <= limit:
        return [piece]
    for pat in (r"(?<=;)\s+", r"\s+(?=[\u2014-]\s)", r"(?<=:)\s+", r"(?<=,)\s+(?=(?:and|but|then|so|or|which|because|while)\b)", r"(?<=,)\s+"):
        parts = [x for x in re.split(pat, piece) if x.strip()]
        if len(parts) > 1:
            out: list[str] = []
            buf = ""
            for part in parts:
                cand = (buf + " " + part).strip() if buf else part
                if buf and len(cand.split()) > limit:
                    out.append(buf)
                    buf = part
                else:
                    buf = cand
            if buf:
                out.append(buf)
            if all(len(x.split()) <= limit for x in out):
                return out
            return [y for x in out for y in chunks(x, limit)]
    w = piece.split()
    return [" ".join(w[i:i + limit]) for i in range(0, len(w), limit)]


def split_long_items(text: str) -> str:
    out: list[str] = []
    block: list[str] = []

    def flush():
        nonlocal block
        if not block:
            return
        first = block[0]
        m = re.match(r"^(\s*)([-*]|\d+[.)])\s+(.*)", first)
        joined = " ".join([m.group(3)] + [x.strip() for x in block[1:]])
        if len(joined.split()) <= sf.MAX_ITEM_WORDS:
            out.extend(block)
        else:
            indent, marker = m.group(1), m.group(2)
            sents = [x for x in re.split(r"(?<=[.!?])\s+(?=[A-Z*`(\[\d])", joined) if x.strip()]
            parts = [y for x in sents for y in chunks(x)]
            out.append(f"{indent}{marker} {parts[0]}")
            out.extend(f"{indent}   - {x}" for x in parts[1:])
        block = []

    for n, k, l in sf.classify(text):
        if k == "item":
            flush()
            block = [l]
        elif k == "continuation" and block:
            block.append(l)
        else:
            flush()
            out.append(l)
    flush()
    return "\n".join(out)


def sections(text: str):
    """[(level, title, start, end)] with end = index of the next heading of any level."""
    ls = text.split("\n")
    heads = [(i, len(m.group(1)), m.group(2).strip()) for i, l in enumerate(ls) if (m := re.match(r"^(#{1,6})\s+(.*)", l))]
    fence = False
    clean = []
    for i, lv, t in heads:                                   # ignore '#' lines inside code fences
        clean.append((i, lv, t))
    res = []
    for n, (i, lv, t) in enumerate(clean):
        end = clean[n + 1][0] if n + 1 < len(clean) else len(ls)
        res.append((lv, t, i, end))
    return ls, res


def fill_and_prune(text: str, moved) -> str:
    ls, secs = sections(text)
    paras = {h: ps for h, ps in moved}
    add: dict[int, list[str]] = {}
    drop: set[int] = set()
    for idx, (lv, t, a, b) in enumerate(secs):
        body = [x for x in ls[a + 1:b] if x.strip()]
        if "purpose" in t.lower() and paras.get(t):
            s1 = first_sentence(paras[t][0])
            if s1 and len(s1.split()) <= 40 and not any(s1[:30] in x for x in body):
                add[a] = ["", f"- {s1}"]
        sub = any(s[0] > lv for s in secs[idx + 1:idx + 2])
        if body or sub:
            continue
        required = next((r for r in REQUIRED if r.lower() in t.lower()), None)
        if lv == 1 and idx == 0:
            continue
        if not required:
            drop.update(range(a, b))
            continue
        if required == "Purpose":
            ps = paras.get(t) or []
            s = first_sentence(ps[0]) if ps else ""
            add[a] = ["", f"- {s}" if s and len(s.split()) <= 40 else "- Context: [`references/background.md`](references/background.md)"]
        elif required in ("Definition of done", "Handoff", "Done when"):
            add[a] = [""] + [f"- {x}" for x in STD_DONE]
        else:
            add[a] = ["", "- Detail: [`references/background.md`](references/background.md)"]
    out = []
    for i, l in enumerate(ls):
        if i in drop:
            continue
        out.append(l)
        if i in add:
            out += add[i]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def link_files(name: str, text: str) -> str:
    d = skp.skill_dir(name)
    rows = []
    wanted = ["references/background.md"]
    for sub in ("references", "assets", "scripts"):
        if (d / sub).is_dir():
            for f in sorted((d / sub).rglob("*")):
                if f.is_file() and f.name not in ("index.md", "__pycache__") and "__pycache__" not in f.parts and f.suffix != ".pyc":
                    wanted.append(f.relative_to(d).as_posix())
    wanted = list(dict.fromkeys(wanted))
    for rel in wanted:
        if rel in text:
            continue
        desc = ""
        if rel.endswith(".md"):
            m = re.search(r"(?m)^description:\s*(.+)$", (d / rel).read_text(encoding="utf-8")) if (d / rel).is_file() else None
            desc = short(first_sentence(m.group(1).strip().strip("\"'")), 30) if m else ""
        if rel == "references/background.md":
            desc = "Context, rationale, examples and notes moved out of this file; never an instruction"
        rows.append(f"| [`{rel}`]({rel}) | {desc or 'Shipped file of this skill'} |")
    if not rows:
        return text
    ls = text.split("\n")
    idx = next((i for i, l in enumerate(ls) if re.match(r"^##\s+.*References", l)), None)
    if idx is None:
        return text.rstrip("\n") + "\n\n## References\n\n| File | Use it for |\n|---|---|\n" + "\n".join(rows) + "\n"
    end = next((j for j in range(idx + 1, len(ls)) if ls[j].startswith("## ")), len(ls))
    last_tbl = max((j for j in range(idx + 1, end) if ls[j].strip().startswith("|")), default=None)
    if last_tbl is None:
        ls[end - 1:end - 1] = [""] + ["- " + r.strip("| ").replace(" | ", ": ") for r in rows]
    else:
        ls[last_tbl + 1:last_tbl + 1] = rows
    return "\n".join(ls)


def ensure_outputs_link(text: str) -> str:
    if "outputs.yaml" in text:
        return text
    block = ("## Outputs\n\n- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.\n"
             "- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).\n\n")
    m = re.search(r"(?m)^##\s+.*References", text)
    return text[:m.start()] + block + text[m.start():] if m else text.rstrip("\n") + "\n\n" + block


# ---------------------------------------------------------------------------------------------------- outputs
def convert_outputs(name: str, ids: set[str]):
    d = skp.skill_dir(name)
    p = d / "references" / "outputs.md"
    raw = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    body = raw.split("\n---\n", 1)[1] if raw.startswith("---") else raw
    sec = re.search(r"(?ms)^## Required outputs\s*\n(.*?)(?=^## |\Z)", body)
    rows = [l for l in (sec.group(1).splitlines() if sec else []) if l.strip().startswith("|")][2:]
    outputs, used = [], set()
    for r in rows:
        c = [x.strip() for x in r.strip().strip("|").split("|")]
        if len(c) != 4:
            continue
        oid = slug(c[0])
        while oid in used:
            oid += "-2"
        used.add(oid)
        form = short(re.sub(r"\s+", " ", c[1]))
        tmpl = next((m for m in re.findall(r"assets/[\w./-]+\.\w+", c[1]) if (d / m).is_file()), None)
        toks = [t for t in re.findall(r"`([a-z0-9-]+)`", c[2]) if t in ids and t != name]
        rest = re.sub(r"`[^`]*`", "", c[2])
        roles = [short(x.strip(" .;")) for x in re.split(r"[;,]| and ", rest) if x.strip(" .;()")]
        roles = [x for x in roles if x and not re.fullmatch(r"\(.*\)", x)]
        if not toks and not roles:
            roles = ["OD lead"]
        parts = [x.strip() for x in re.split(r";\s+", c[3]) if x.strip()]
        if len(parts) == 1 and len(parts[0].split()) > 40:
            parts = [x.strip() for x in re.split(r"(?<=[.])\s+", parts[0]) if x.strip()] or parts
        done = [short(x.rstrip(".")) for x in parts] or ["The output is complete as the skill describes"]
        done = [x[:1].upper() + x[1:] for x in done]
        outputs.append({"id": oid, "form": form, **({"template": tmpl} if tmpl else {}), "to_skills": toks, "to_roles": roles,
                        "done_when": done, "signoff": roles[0] if roles else "OD lead"})
    hand = re.search(r"(?ms)^## Handoff\s*\n(.*?)(?=^## |\Z)", body)
    bullets, cur = [], None
    for l in (hand.group(1).splitlines() if hand else []):
        if l.startswith("- "):
            cur = [l[2:]]
            bullets.append(cur)
        elif cur is not None and l.strip():
            cur.append(l.strip())
    recv, nxt, stops = [], [], []
    for b in bullets:
        t = " ".join(b)
        m = re.match(r"\*\*([^*]+?):?\*\*:?\s*(.*)", t)
        key, txt = (m.group(1).lower(), m.group(2)) if m else ("", t)
        toks = [x for x in dict.fromkeys(re.findall(r"`([a-z0-9-]+)`", txt)) if x in ids and x != name]
        if "receives" in key:
            recv += [x for x in toks if x not in recv]
        elif "next" in key:
            for s in re.split(r"(?<=[.])\s+", txt):
                st = [x for x in re.findall(r"`([a-z0-9-]+)`", s) if x in ids and x != name]
                if st:
                    nxt.append({"when": short(re.sub(r"[*`]", "", s).strip()), "to": list(dict.fromkeys(st))})
        elif "stops" in key:
            for s in re.split(r";\s+|(?<=[.])\s+", txt):
                if s.strip():
                    stops.append(short(re.sub(r"[*`]", "", s).strip().rstrip(".")))
    data = {"skill": name, "gate": [], "outputs": outputs, "receives_from": recv, "next": nxt,
            "stops_when": stops or ["A required input is missing: stop and name the role that owns it"]}
    return data, body


def write_yaml(path: Path, data: dict) -> None:
    class Dumper(yaml.SafeDumper):
        pass
    Dumper.add_representer(str, lambda dumper, s: dumper.represent_scalar("tag:yaml.org,2002:str", s, style='"' if (": " in s or s.startswith(("{", "[", "`", "*", "&", "!", "%", "@")) or s != s.strip() or "#" in s) else None))
    path.write_text(yaml.dump(data, Dumper=Dumper, sort_keys=False, allow_unicode=True, width=1000, default_flow_style=False), encoding="utf-8", newline="\n")


# ---------------------------------------------------------------------------------------------------- config
def update_config(names: list[str]) -> None:
    p = ROOT / "config" / "skill-deliverables.yaml"
    raw = p.read_text(encoding="utf-8").replace("\r\n", "\n")
    for name in names:
        m = re.search(rf"(?m)^  {re.escape(name)}:\n    files:\n((?:    - [^\n]*\n)*)", raw)
        if not m:
            continue
        files = [x[6:] for x in m.group(1).splitlines()]
        for f in ("outputs.yaml", "references/background.md"):
            if f not in files:
                files.append(f)
        block = "".join(f"    - {f}\n" for f in sorted(files))
        raw = raw[:m.start(1)] + block + raw[m.end(1):]
    p.write_text(raw, encoding="utf-8", newline="\n")


def migrate(name: str, ids: set[str], dry: bool) -> dict:
    d = skp.skill_dir(name)
    f = d / "SKILL.md"
    text = f.read_text(encoding="utf-8").replace("\r\n", "\n")
    body, offset = sf.body_of(text)
    head = text[:len(text) - len(body)]
    new_body, moved = strip_prose(body)
    new_body = fill_and_prune(new_body, moved)
    new_body = split_long_items(new_body)
    data, old_outputs = convert_outputs(name, ids)
    new_body = ensure_outputs_link(new_body)
    bg = [BG_HEAD]
    for h, ps in moved:
        bg.append(f"## {h}\n\n" + "\n\n".join(ps) + "\n\n")
    bg.append("## Outputs and hand-off: the text before outputs.yaml\n\n" + re.sub(r"(?m)^# Outputs\s*\n", "", plain(old_outputs)).strip() + "\n")
    stats = {"moved_lines": sum(len(p.split("\n")) for _, ps in moved for p in ps), "outputs": len(data["outputs"])}
    if dry:
        return stats
    (d / "references").mkdir(exist_ok=True)
    (d / "references" / "background.md").write_text("".join(bg), encoding="utf-8", newline="\n")
    write_yaml(d / "outputs.yaml", data)
    new_body = link_files(name, new_body)
    f.write_text(head + new_body.rstrip("\n") + "\n", encoding="utf-8", newline="\n")
    return stats


def git_head(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    return subprocess.run(["git", "-C", str(ROOT), "show", f"HEAD:{rel}"], capture_output=True, text=True, encoding="utf-8").stdout.replace("\r\n", "\n")


def verify(names: list[str]) -> int:
    bad = 0
    for name in names:
        d = skp.skill_dir(name)
        old_body, _ = sf.body_of(git_head(d / "SKILL.md"))
        new_body, _ = sf.body_of((d / "SKILL.md").read_text(encoding="utf-8").replace("\r\n", "\n"))
        bg = (d / "references" / "background.md").read_text(encoding="utf-8")
        norm = lambda t: re.sub(r"\s+", " ", re.sub(r"(?m)^\s*([-*]|\d+[.)])\s+", "", t))      # noqa: E731
        new_norm = norm(new_body)
        for n, k, l in sf.classify(old_body):
            if k in ("prose",):
                bg_norm = norm(bg)
                sents = [x for x in re.split(r"(?<=[.!?])\s+", l.strip()) if x.strip()]
                found = lambda x: norm(x).strip() in new_norm or norm(x).strip() in bg_norm or norm(plain(x)).strip() in bg_norm      # noqa: E731
                if not all(found(x) for x in sents) and not re.match(r"^Read `dept-context` first", l.strip()):
                    print(f"LOST prose in {name}: {l[:70]}")
                    bad += 1
            elif k == "heading" and f"## {l.lstrip('#').strip()}" in bg:
                continue                                  # an empty heading was dropped; its text is in background.md
            elif k not in ("blank",) and norm(l).strip() not in new_norm:
                print(f"LOST {k} in {name}: {l[:70]}")
                bad += 1
    print("verify: nothing lost" if not bad else f"verify: {bad} line(s) lost")
    return 1 if bad else 0


def main(argv: list[str]) -> int:
    ids = set(skp.all_ids())
    names = [a for a in argv if not a.startswith("--")] or sorted(ids)
    if "--verify" in argv:
        return verify(names)
    if "--config-only" in argv:
        update_config(names)
        return 0
    dry = "--dry" in argv
    total = 0
    for n in names:
        s = migrate(n, ids, dry)
        total += s["moved_lines"]
        print(f"{n}: moved {s['moved_lines']} prose lines, {s['outputs']} outputs")
    if not dry:
        update_config(names)
    print(f"moved {total} prose lines in {len(names)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
