#!/usr/bin/env python3
"""Validate AnythingAtlas Markdown/HTML parity and standalone HTML structure."""

from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from atlas_common import AVAILABLE_THEMES, labels_for, load_atlas


class AtlasHTMLCollector(HTMLParser):
    """Collect structural facts and visible text from rendered HTML."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.text: list[str] = []
        self.ids: set[str] = set()
        self.links: set[str] = set()
        self.image_sources: list[str] = []
        self.h1_count = 0
        self.main_count = 0
        self.nav_count = 0
        self.footer_count = 0
        self.footer_text: list[str] = []
        self.in_footer = False
        self.style_count = 0
        self.external_stylesheets = 0
        self.lang = ""
        self.body_classes: set[str] = set()
        self.section_order: list[str] = []
        self.brand_image_count = 0

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(str(attributes["id"]))
        if tag == "html":
            self.lang = str(attributes.get("lang") or "")
        elif tag == "body":
            self.body_classes = set(str(attributes.get("class") or "").split())
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "main":
            self.main_count += 1
        elif tag == "nav":
            self.nav_count += 1
        elif tag == "style":
            self.style_count += 1
        elif tag == "section" and attributes.get("id"):
            self.section_order.append(str(attributes["id"]))
        elif tag == "footer":
            self.footer_count += 1
            self.in_footer = True
        elif tag == "a" and attributes.get("href"):
            self.links.add(str(attributes["href"]))
        elif tag == "img" and attributes.get("src"):
            self.image_sources.append(str(attributes["src"]))
            image_fingerprint = " ".join(
                (
                    str(attributes.get("class") or ""),
                    str(attributes.get("alt") or ""),
                    str(attributes.get("src") or ""),
                )
            ).lower()
            if "hero__logo" in image_fingerprint or "anythingatlas" in image_fingerprint:
                self.brand_image_count += 1
        elif tag == "link" and str(attributes.get("rel") or "").lower() == "stylesheet":
            self.external_stylesheets += 1

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.text.append(data)
            if self.in_footer:
                self.footer_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "footer":
            self.in_footer = False


def normalized(value: Any) -> str:
    """Collapse whitespace for content-parity comparisons."""
    return re.sub(r"\s+", " ", str(value)).strip()


def validate_deliverables(
    data: dict[str, Any], markdown_path: Path, html_path: Path
) -> tuple[list[str], list[str]]:
    """Return errors and warnings for a rendered pair."""
    errors: list[str] = []
    warnings: list[str] = []

    for label, path in (("Markdown", markdown_path), ("HTML", html_path)):
        if not path.is_file():
            errors.append(f"{label} file does not exist: {path}")
        elif path.stat().st_size < 200:
            errors.append(f"{label} file is unexpectedly small: {path}")
    if errors:
        return errors, warnings

    markdown = markdown_path.read_text(encoding="utf-8")
    html = html_path.read_text(encoding="utf-8")
    collector = AtlasHTMLCollector()
    try:
        collector.feed(html)
        collector.close()
    except Exception as exc:  # HTMLParser exposes parser failures as exceptions.
        errors.append(f"Unable to parse HTML: {exc}")
        return errors, warnings

    html_text = normalized(" ".join(collector.text))
    labels = labels_for(data["meta"].get("language"))
    section_labels = (
        labels["confirmed_brief"],
        labels["orientation"],
        labels["field_guide"],
        labels["action_kit"],
        labels["knowledge_map"],
        labels["resource_tracks"],
        labels["resources"],
        labels["roadmap"],
        labels["source_plan"],
        labels["source_notes"],
        labels["next_action"],
    )
    section_ids = {
        "brief",
        "orientation",
        "field",
        "action",
        "knowledge",
        "tracks",
        "resources",
        "roadmap",
        "sources",
        "notes",
        "next",
    }
    expected_section_order = [
        "brief",
        "orientation",
        "field",
        "action",
        "knowledge",
        "tracks",
        "resources",
        "roadmap",
        "sources",
        "notes",
        "next",
    ]

    for section_label in section_labels:
        if section_label not in markdown:
            errors.append(f"Markdown is missing section: {section_label}")
        if normalized(section_label) not in html_text:
            errors.append(f"HTML is missing section: {section_label}")
    markdown_section_positions = [
        markdown.find(f"## {number}. {section_label}")
        for number, section_label in enumerate(section_labels, start=1)
    ]
    if (
        any(position < 0 for position in markdown_section_positions)
        or markdown_section_positions != sorted(markdown_section_positions)
    ):
        errors.append(
            "Markdown sections must present the direct answer and practical "
            "guidance before the roadmap, with source methodology afterward."
        )
    missing_ids = sorted(section_ids - collector.ids)
    if missing_ids:
        errors.append(f"HTML is missing section IDs: {', '.join(missing_ids)}")
    if collector.section_order != expected_section_order:
        errors.append(
            "HTML sections must present the direct answer and practical guidance "
            "before the roadmap, with source methodology afterward; "
            f"expected {', '.join(expected_section_order)}, found "
            f"{', '.join(collector.section_order) or 'none'}."
        )

    for resource in data["resources"]:
        title = normalized(resource["title"])
        url = str(resource["url"])
        if title not in normalized(markdown.replace("\\", "")):
            errors.append(f"Markdown is missing resource title: {title}")
        if title not in html_text:
            errors.append(f"HTML is missing resource title: {title}")
        if url not in markdown:
            errors.append(f"Markdown is missing resource URL: {url}")
        if url not in collector.links:
            errors.append(f"HTML is missing resource link: {url}")

    parity_items: list[Any] = [
        data["orientation"]["bottom_line"],
        *data["orientation"]["key_points"],
        *data["orientation"]["tradeoffs"],
        *(
            value
            for recommendation in data["orientation"]["recommendations"]
            for value in (
                recommendation["choice"],
                recommendation["best_for"],
                recommendation["why"],
                recommendation["tradeoffs"],
            )
        ),
        data["field_guide"]["as_of"],
        data["field_guide"]["scope"],
        *(
            value
            for entry in data["field_guide"]["entries"]
            for value in (
                entry["name"],
                entry["category"],
                entry["why_it_matters"],
                *entry["representative_examples"],
                entry["selection_note"],
            )
        ),
        *(
            value
            for item in data["action_kit"]["setup"]
            for value in (item["item"], item["recommendation"], item["why"])
        ),
        *data["action_kit"]["first_session"],
        *data["action_kit"]["decision_rules"],
        *data["action_kit"]["safety_checks"],
        *data["action_kit"]["failure_modes"],
        *(
            value
            for track in data["resource_tracks"]
            for value in (
                track["title"],
                track["best_for"],
                track["cadence"],
                *track["sequence"],
            )
        ),
    ]
    for item in parity_items:
        value = normalized(item)
        if value not in normalized(markdown.replace("\\", "")):
            errors.append(f"Markdown is missing answer-first content: {value}")
        if value not in html_text:
            errors.append(f"HTML is missing answer-first content: {value}")

    for stage in data["roadmap"]:
        title = normalized(stage["title"])
        if title not in normalized(markdown):
            errors.append(f"Markdown is missing roadmap stage: {title}")
        if title not in html_text:
            errors.append(f"HTML is missing roadmap stage: {title}")

    if normalized(data["meta"]["summary"]) not in normalized(markdown):
        errors.append("Markdown is missing the atlas summary.")
    if normalized(data["meta"]["summary"]) not in html_text:
        errors.append("HTML is missing the atlas summary.")

    if collector.h1_count != 1:
        errors.append(f"HTML must contain exactly one h1; found {collector.h1_count}.")
    if collector.main_count != 1:
        errors.append(
            f"HTML must contain exactly one main landmark; found {collector.main_count}."
        )
    if collector.nav_count < 1:
        errors.append("HTML must contain section navigation.")
    if collector.footer_count != 1:
        errors.append(
            f"HTML must contain exactly one footer; found {collector.footer_count}."
        )
    if "AnythingAtlas" not in normalized(" ".join(collector.footer_text)):
        errors.append("HTML footer must include the AnythingAtlas text credit.")
    if collector.style_count < 1:
        errors.append("HTML must contain embedded CSS.")
    if collector.external_stylesheets:
        errors.append("HTML must not depend on external stylesheets.")
    if not collector.lang:
        errors.append("HTML must declare a document language.")
    if collector.brand_image_count:
        errors.append("HTML must use text-only AnythingAtlas branding, not a logo image.")
    theme_classes = {
        name[len("theme-") :]
        for name in collector.body_classes
        if name.startswith("theme-")
    }
    if len(theme_classes) != 1 or not theme_classes.issubset(AVAILABLE_THEMES):
        errors.append(
            "HTML body must declare exactly one built-in visual theme: "
            + ", ".join(AVAILABLE_THEMES)
            + "."
        )

    unresolved = sorted(set(re.findall(r"\{\{[A-Z0-9_]+\}\}", html)))
    if unresolved:
        errors.append(f"HTML contains unresolved placeholders: {', '.join(unresolved)}")

    internal_links = {link[1:] for link in collector.links if link.startswith("#")}
    broken_internal = sorted(link for link in internal_links if link not in collector.ids)
    if broken_internal:
        errors.append(
            f"HTML contains broken internal links: {', '.join(broken_internal)}"
        )

    for link in collector.links:
        if link.startswith(("http://", "https://", "#")):
            continue
        warnings.append(f"Non-HTTP link requires manual review: {link}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Canonical atlas JSON file")
    parser.add_argument("--markdown", required=True, help="Rendered Markdown file")
    parser.add_argument("--html", required=True, help="Rendered HTML file")
    args = parser.parse_args()

    data = load_atlas(args.input)
    errors, warnings = validate_deliverables(
        data, Path(args.markdown), Path(args.html)
    )
    for warning in warnings:
        print(f"[WARN] {warning}")
    for error in errors:
        print(f"[ERROR] {error}")
    if errors:
        print(f"[FAIL] Validation found {len(errors)} error(s).")
        return 1
    print("[OK] Markdown and HTML deliverables are valid and synchronized.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
