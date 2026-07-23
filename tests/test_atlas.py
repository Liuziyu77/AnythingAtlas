#!/usr/bin/env python3
"""Regression tests for the AnythingAtlas content contract."""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from atlas_common import validate_model  # noqa: E402
from render_html import built_in_style_paths, render_html  # noqa: E402
from render_markdown import render_markdown  # noqa: E402
from validate_deliverables import validate_deliverables  # noqa: E402


class AtlasContentContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sample = json.loads(
            (ROOT / "examples/sample-atlas.json").read_text(encoding="utf-8")
        )

    def errors_after(self, mutation) -> list[str]:
        model = copy.deepcopy(self.sample)
        mutation(model)
        return validate_model(model)

    def test_sample_satisfies_answer_first_contract(self) -> None:
        self.assertEqual(validate_model(self.sample), [])

    def test_rejects_atlas_without_concrete_recommendations(self) -> None:
        errors = self.errors_after(
            lambda model: model["guide"].update(recommendations=[])
        )
        self.assertIn(
            "guide.recommendations must contain at least one item.", errors
        )

    def test_rejects_old_schema_version(self) -> None:
        errors = self.errors_after(
            lambda model: model["meta"].update(schema_version="0.1")
        )
        self.assertTrue(any("meta.schema_version must be 0.3" in e for e in errors))

    def test_rejects_guide_item_without_representative_examples(self) -> None:
        errors = self.errors_after(
            lambda model: model["guide"]["sections"][0]["items"][0].update(
                examples=[]
            )
        )
        self.assertTrue(
            any(".examples is required" in error for error in errors)
        )

    def test_rejects_guide_without_next_action(self) -> None:
        errors = self.errors_after(
            lambda model: model["guide"].update(next_action={})
        )
        self.assertTrue(
            any("guide.next_action." in error for error in errors)
        )

    def test_rejects_missing_format_preference_or_default(self) -> None:
        errors = self.errors_after(lambda model: model["brief"].update(formats=[]))
        self.assertIn(
            "brief.formats must record the user's preference or an explicit default.",
            errors,
        )

    def test_rejects_resource_track_with_unknown_resource(self) -> None:
        errors = self.errors_after(
            lambda model: model["resource_tracks"][0].update(
                resource_ids=["not-a-resource"]
            )
        )
        self.assertTrue(
            any("references unknown resource id" in error for error in errors)
        )

    def test_rejects_source_directory_that_omits_a_resource(self) -> None:
        errors = self.errors_after(
            lambda model: model["source_directory"]["groups"][0].update(
                resource_ids=[]
            )
        )
        self.assertTrue(
            any(
                "source_directory must include every curated resource" in error
                for error in errors
            )
        )

    def test_rendered_order_is_compact_and_source_directory_is_last(self) -> None:
        markdown = render_markdown(self.sample)
        headings = [
            "## 1. Confirmed User Brief",
            "## 2. Core Guide",
            "## 3. Curated Resource Atlas",
            "## 4. Detailed Learning or Exploration Roadmap",
            "## 5. Source Directory",
        ]
        positions = [markdown.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))

    def test_markdown_and_html_preserve_sections_and_clickable_assignments(self) -> None:
        markdown = render_markdown(self.sample)
        html = render_html(
            self.sample,
            ROOT / "assets/html-template/atlas.html",
            built_in_style_paths(ROOT, "workshop"),
            "workshop",
        )
        with tempfile.TemporaryDirectory() as directory:
            markdown_path = Path(directory) / "atlas.md"
            html_path = Path(directory) / "atlas.html"
            markdown_path.write_text(markdown, encoding="utf-8")
            html_path.write_text(html, encoding="utf-8")
            errors, warnings = validate_deliverables(
                self.sample, markdown_path, html_path
            )
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])
        for resource in self.sample["resources"]:
            url = resource["url"]
            self.assertIn(url, markdown)
            self.assertIn(url, html)

    def test_validator_rejects_plain_text_resource_in_track(self) -> None:
        markdown = render_markdown(self.sample)
        html = render_html(
            self.sample,
            ROOT / "assets/html-template/atlas.html",
            built_in_style_paths(ROOT, "workshop"),
            "workshop",
        )
        resource = self.sample["resources"][0]
        linked = f"[{resource['title']}]({resource['url']})"
        track_end = markdown.index("### Resource details")
        weakened_markdown = markdown[:track_end].replace(linked, resource["title"])
        weakened_markdown += markdown[track_end:]
        with tempfile.TemporaryDirectory() as directory:
            markdown_path = Path(directory) / "atlas.md"
            html_path = Path(directory) / "atlas.html"
            markdown_path.write_text(weakened_markdown, encoding="utf-8")
            html_path.write_text(html, encoding="utf-8")
            errors, _ = validate_deliverables(
                self.sample, markdown_path, html_path
            )
        self.assertIn(
            "Markdown resource track is missing clickable resource: "
            f"{resource['title']}",
            errors,
        )


if __name__ == "__main__":
    unittest.main()
