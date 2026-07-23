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
            lambda model: model["orientation"].update(recommendations=[])
        )
        self.assertIn(
            "orientation.recommendations must contain at least one item.", errors
        )

    def test_rejects_old_schema_version(self) -> None:
        errors = self.errors_after(
            lambda model: model["meta"].update(schema_version="0.1")
        )
        self.assertTrue(any("meta.schema_version must be 0.2" in e for e in errors))

    def test_rejects_field_guide_without_representative_examples(self) -> None:
        errors = self.errors_after(
            lambda model: model["field_guide"]["entries"][0].update(
                representative_examples=[]
            )
        )
        self.assertTrue(
            any("representative_examples is required" in error for error in errors)
        )

    def test_rejects_action_kit_without_first_session(self) -> None:
        errors = self.errors_after(
            lambda model: model["action_kit"].update(first_session=[])
        )
        self.assertIn(
            "action_kit.first_session must contain at least one action.", errors
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

    def test_rendered_order_is_answer_first_and_source_plan_is_appendix(self) -> None:
        markdown = render_markdown(self.sample)
        headings = [
            "## 1. Confirmed User Brief",
            "## 2. Direct Orientation",
            "## 3. Field Guide",
            "## 4. Practical Action Kit",
            "## 5. Knowledge Map",
            "## 6. Resource Tracks",
            "## 7. Curated Resource Atlas",
            "## 8. Detailed Learning or Exploration Roadmap",
            "## 9. Source and Channel Plan",
            "## 10. Source Notes",
            "## 11. Next Action",
        ]
        positions = [markdown.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))

    def test_markdown_and_html_preserve_new_sections(self) -> None:
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


if __name__ == "__main__":
    unittest.main()
