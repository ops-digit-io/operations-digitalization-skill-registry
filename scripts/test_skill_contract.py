"""Tests of the skill output contract: outputs.yaml, the SKILL.md form lint, the structure check and the run record.

    python -m unittest discover -s scripts -p "test_skill_contract.py"
"""
import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_output_structure as cos  # noqa: E402
import run_record as rr  # noqa: E402
import skill_form as sf  # noqa: E402
import skill_outputs as so  # noqa: E402
import skillpaths as skp  # noqa: E402

SKILL = "process-derivation"          # has a template, a structure check and a command check
IDS = set(skp.all_ids())


def good():
    return {"skill": "x", "gate": [], "receives_from": [], "next": [], "stops_when": ["An input is missing"],
            "outputs": [{"id": "a", "form": "a file", "to_skills": [], "to_roles": ["owner"], "done_when": ["It exists"], "signoff": "owner"}]}


class Contract(unittest.TestCase):
    def check(self, data, ids=None):
        return so.validate("x", data, Path(tempfile.gettempdir()), ids or {"x", "bc-build"})

    def test_good_passes(self):
        self.assertEqual(self.check(good()), [])

    def test_output_without_check_or_signoff_fails(self):
        d = good()
        del d["outputs"][0]["signoff"]
        self.assertTrue(any("unchecked output" in e for e in self.check(d)))

    def test_prose_is_refused(self):
        d = good()
        d["outputs"][0]["done_when"] = [" ".join(["word"] * 41)]
        self.assertTrue(any("41 words" in e for e in self.check(d)))

    def test_unknown_recipient_skill(self):
        d = good()
        d["outputs"][0]["to_skills"] = ["nope"]
        self.assertTrue(any("not a skill" in e for e in self.check(d)))

    def test_structure_check_needs_a_template(self):
        d = good()
        d["outputs"][0]["check"] = {"structure": True}
        self.assertTrue(any("structure: true" in e for e in self.check(d)))

    def test_every_skill_of_the_registry_is_valid_and_current(self):
        for name in sorted(IDS):
            d = skp.skill_dir(name)
            data = so.load(d)
            self.assertEqual(so.validate(name, data, d, IDS), [], name)
            text = (d / "references" / "outputs.md").read_text(encoding="utf-8").replace("\r\n", "\n")
            self.assertEqual(text, so.render(name, data), f"{name}: outputs.md is stale")


class Form(unittest.TestCase):
    def kinds(self, text):
        return [k for _, k, _ in sf.classify(text) if k not in ("blank",)]

    def test_paragraph_is_prose(self):
        self.assertIn("prose", self.kinds("# T\n\nThis is a sentence.\n"))

    def test_structure_is_not_prose(self):
        text = "# T\n\n- item\n  continued\n\n| a | b |\n|---|---|\n| 1 | 2 |\n\n```text\nfree text in a fence\n```\n"
        self.assertNotIn("prose", self.kinds(text))

    def test_every_skill_is_structure_only(self):
        for name in sorted(IDS):
            self.assertEqual(sf.lint(name), [], name)


class Structure(unittest.TestCase):
    TEMPLATE = "# Title ⟨name⟩\n\n## 1 · Question\n\ntext\n\n## 2 · Result\n"

    def test_complete_output_passes(self):
        out = "# Title x\n\n## 1 · Question\n\nfilled\n\n## 2 · Result\n\nfilled\n"
        self.assertEqual(cos.findings(out, self.TEMPLATE), [])

    def test_missing_section_and_open_placeholder(self):
        out = "# Title x\n\n## 1 · Question\n\n⟨fill this⟩\n"
        found = cos.findings(out, self.TEMPLATE)
        self.assertTrue(any("missing section" in f for f in found))
        self.assertTrue(any("placeholder" in f for f in found))

    def test_known_gap_marker_is_allowed(self):
        out = "## 1 · Question\n\n⟨not recorded⟩\n\n## 2 · Result\n"
        self.assertEqual(cos.findings(out, self.TEMPLATE), [])


class Run(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.run_id, self.text = rr.new_record(SKILL)
        self.path = self.tmp / f"{self.run_id}.md"

    def write(self, text):
        self.path.write_text(text, encoding="utf-8", newline="\n")
        return rr.check(self.path)

    def fill(self):
        """A record in which everything is done, with evidence."""
        t = self.text.replace("| open |", "| done |")
        t = re.sub(r"(?m)^(\| [a-z0-9-]+ \| )\| ([^|]+\| )\| (done \|)$", r"\1runs/x.md | \2proof | \3", t)
        t = t.replace("status: open", "status: done")
        t = re.sub(r"(?m)^(\| [a-z0-9-]+ \| `[^|]*` \| )\| \|$", r"\g<1>0 | 2026-11-16 |", t)
        t = re.sub(r"(?m)^(\| [a-z0-9-]+ \| [^|]+ \| )\| \|$", r"\g<1>owner role | 2026-11-16 |", t)
        return t

    def test_new_record_is_open_and_not_closable_when_marked_done(self):
        errs = self.write(self.text.replace("status: open", "status: done"))
        self.assertTrue(errs)

    def test_filled_record_closes(self):
        errs = [e for e in self.write(self.fill()) if not e.startswith("note:")]
        self.assertEqual(errs, [], errs)

    def test_missing_evidence_blocks_closing(self):
        t = self.fill().replace("| proof |", "| |", 1)
        self.assertTrue(any("without evidence" in e for e in self.write(t)))

    def test_missing_signoff_means_awaiting_signoff(self):
        t = self.fill()
        t = re.sub(r"(?m)^(\| [a-z0-9-]+ \| [^|]+ \| )owner role \| 2026-11-16 \|$", r"\1| |", t)
        errs = self.write(t)
        self.assertTrue(any("waiting for a human" in e for e in errs))

    def test_unmet_gate_is_refused_not_done(self):
        if "## Gate" in self.text and rr.so.load(skp.skill_dir(SKILL))["gate"]:
            t = self.text.replace("status: open", "status: refused")
            self.assertTrue(any("every gate row is met" in e for e in self.write(t)))

    def test_open_records_are_listed(self):
        self.write(self.text)
        self.assertEqual(len(rr.open_records(self.tmp)), 1)


if __name__ == "__main__":
    unittest.main()
