#!/usr/bin/env python3
"""Tests for scaffold_skill.py. Run: python3 test_scaffold_skill.py (needs PyYAML, like the registry's own checks)."""
import re
import tempfile
import unittest
from pathlib import Path

import yaml

import scaffold_skill as sc

ARGS = dict(tier="practice", lane="all", owner_role="Digital-Business-Value-Engineer (DBVE)",
            authority="draft; the owner decides")


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    return yaml.safe_load(re.match(r"---\n(.*?)\n---\n", text, re.S).group(1))


class ScaffoldChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "registry.yaml").write_text("skills: []\n", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_frontmatter_meets_the_registry_rules(self):
        folder = sc.scaffold(self.root, "od-example-check", **ARGS)
        fm = frontmatter(folder / "SKILL.md")
        self.assertEqual(fm["name"], "od-example-check")
        self.assertEqual(fm["metadata"]["id"], "od-example-check")
        self.assertTrue(120 <= len(" ".join(fm["description"].split())) <= 1024)
        for field in ("tier", "lane", "owner_role", "authority_level", "status", "derived_from"):
            self.assertTrue(fm["metadata"].get(field), field)
        self.assertEqual(fm["metadata"]["status"], "draft")
        self.assertIn("od-context", fm["metadata"]["requires"])
        self.assertEqual(set(fm), {"name", "description", "license", "metadata"})

    def test_no_placeholder_in_metadata_values(self):
        fm = frontmatter(sc.scaffold(self.root, "od-example-check", **ARGS) / "SKILL.md")
        for key, value in fm["metadata"].items():
            if isinstance(value, str):
                self.assertNotIn("⟨", value, key)

    def test_body_has_the_expected_sections(self):
        text = (sc.scaffold(self.root, "od-example-check", **ARGS) / "SKILL.md").read_text(encoding="utf-8")
        for heading in ("## Purpose", "## Inputs and output", "## Procedure", "## Human gate and AI-agent notes",
                        "## Pitfalls", "## Definition of done", "## References"):
            self.assertIn(heading, text)
        self.assertIn("```", text)

    def test_core_library_folder(self):
        folder = sc.scaffold(self.root, "od-example-check", library="core", **ARGS)
        self.assertEqual(folder.parent.name, "skills")

    def test_refuses_an_existing_folder(self):
        sc.scaffold(self.root, "od-example-check", **ARGS)
        with self.assertRaises(FileExistsError):
            sc.scaffold(self.root, "od-example-check", **ARGS)

    def test_rejects_bad_names_and_tiers(self):
        for bad in ("Od-Example", "od_example", "od--example", "-od", "x" * 65):
            with self.assertRaises(ValueError, msg=bad):
                sc.scaffold(self.root, bad, **ARGS)
        with self.assertRaises(ValueError):
            sc.scaffold(self.root, "od-example-check", **{**ARGS, "tier": "expert"})

    def test_rejects_placeholders_in_role_and_authority(self):
        with self.assertRaises(ValueError):
            sc.scaffold(self.root, "od-example-check", **{**ARGS, "owner_role": "⟨role⟩"})

    def test_registry_entry_uses_the_same_authority(self):
        entry = sc.registry_entry("od-example-check", "practice", "all", "a role", "draft; the owner decides", "extension")
        self.assertIn("authority_level: draft; the owner decides", entry)


if __name__ == "__main__":
    unittest.main()
