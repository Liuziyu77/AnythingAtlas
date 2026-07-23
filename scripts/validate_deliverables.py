#!/usr/bin/env python3
"""Validate AnythingAtlas Markdown/HTML parity and standalone HTML structure."""

from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from atlas_common import labels_for, load_atlas


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
        self.style_count = 0
        self.external_stylesheets = 0
        self.lang = ""

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(str(attributes["id"]))
        if tag == "html":
            self.lang = str(attributes.get("lang") or "")
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "main":
            self.main_count += 1
        elif tag == "nav":
            self.nav_count += 1
        elif tag == "style":
            self.style_count += 1
        elif tag == "a" and attributes.get("href"):
            self.links.add(str(attributes["href"]))
        elif tag == "img" and attributes.get("src"):
            self.image_sources.append(str(attributes["src"]))
        elif tag == "link" and str(attributes.get("rel") or "").lower() == "stylesheet":
            self.external_stylesheets += 1

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.text.append(data)


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
        labels["topic_brief"],
        labels["knowledge_map"],
        labels["source_plan"],
        labels["starting_point"],
        labels["resources"],
        labels["roadmap"],
        labels["source_notes"],
        labels["next_action"],
    )
    section_ids = {
        "brief",
        "topic",
        "knowledge",
        "sources",
        "start",
        "resources",
        "roadmap",
        "notes",
        "next",
    }

    for section_label in section_labels:
        if section_label not in markdown:
            errors.append(f"Markdown is missing section: {section_label}")
        if normalized(section_label) not in html_text:
            errors.append(f"HTML is missing section: {section_label}")
    missing_ids = sorted(section_ids - collector.ids)
    if missing_ids:
        errors.append(f"HTML is missing section IDs: {', '.join(missing_ids)}")

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
    if collector.style_count < 1:
        errors.append("HTML must contain embedded CSS.")
    if collector.external_stylesheets:
        errors.append("HTML must not depend on external stylesheets.")
    if not collector.lang:
        errors.append("HTML must declare a document language.")
    if not any(source.startswith("data:image/") for source in collector.image_sources):
        errors.append("HTML must embed the AnythingAtlas logo as a data URI.")

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
