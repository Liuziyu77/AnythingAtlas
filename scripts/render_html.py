#!/usr/bin/env python3
"""Render an AnythingAtlas canonical JSON model as self-contained HTML."""

from __future__ import annotations

import argparse
from html import escape
from pathlib import Path
from typing import Any

from atlas_common import (
    AVAILABLE_THEMES,
    labels_for,
    listify,
    load_atlas,
    project_root,
    resource_index,
)


SECTION_KEYS = (
    ("brief", "confirmed_brief"),
    ("guide", "guide"),
    ("resources", "resources"),
    ("roadmap", "roadmap"),
    ("sources", "source_directory"),
)


def h(value: Any) -> str:
    """Escape text for HTML."""
    return escape(str(value), quote=True)


def paragraphs(value: Any, css_class: str = "") -> str:
    """Render newline-separated text as safe paragraphs."""
    class_attr = f' class="{h(css_class)}"' if css_class else ""
    parts = [item.strip() for item in str(value).split("\n\n") if item.strip()]
    return "".join(f"<p{class_attr}>{h(item)}</p>" for item in parts)


def html_list(values: Any) -> str:
    """Render a safe unordered list."""
    items = listify(values)
    if not items:
        return ""
    return "<ul>" + "".join(f"<li>{h(item)}</li>" for item in items) + "</ul>"


def definition_item(label: str, value: Any) -> str:
    """Render a definition-list entry with scalar or list content."""
    values = listify(value)
    if not values:
        return ""
    content = h(values[0]) if len(values) == 1 else html_list(values)
    return f"<div class=\"brief-item\"><dt>{h(label)}</dt><dd>{content}</dd></div>"


def built_in_style_paths(root: Path, theme: str) -> list[Path]:
    """Return the base, theme, and print styles for a built-in theme."""
    if theme not in AVAILABLE_THEMES:
        raise ValueError(f"Unknown HTML theme: {theme}")
    template_root = root / "assets/html-template"
    return [
        template_root / "atlas.css",
        template_root / "themes" / f"{theme}.css",
        template_root / "themes" / "print.css",
    ]


def section(number: int, section_id: str, title: str, body: str) -> str:
    """Wrap a rendered section."""
    return (
        f'      <section id="{h(section_id)}" class="atlas-section" '
        f'data-section="{h(section_id)}">\n'
        f'        <p class="section-kicker">{number:02d}</p>\n'
        f"        <h2>{h(title)}</h2>\n"
        f"{body}\n"
        "      </section>"
    )


def render_brief(data: dict[str, Any], labels: dict[str, str]) -> str:
    brief = data["brief"]
    fields = (
        ("goal", "goal"),
        ("background", "background"),
        ("time", "time"),
        ("language", "language"),
        ("formats", "formats"),
        ("depth", "depth"),
        ("constraints", "constraints"),
        ("assumptions", "assumptions"),
    )
    items = "".join(
        definition_item(labels[label], brief.get(key)) for key, label in fields
    )
    return f'        <dl class="brief-grid">{items}</dl>'


def resource_anchor(resource: dict[str, Any], css_class: str = "") -> str:
    """Render a safe link to a verified resource."""
    class_attr = f' class="{h(css_class)}"' if css_class else ""
    return (
        f'<a{class_attr} href="{h(resource["url"])}">'
        f'{h(resource["title"])} <span aria-hidden="true">↗</span></a>'
    )


def linked_resource_list(resources: list[dict[str, Any]]) -> str:
    """Render resource titles as a linked HTML list."""
    return (
        '<ul class="linked-resource-list">'
        + "".join(f"<li>{resource_anchor(resource)}</li>" for resource in resources)
        + "</ul>"
    )


def render_guide(data: dict[str, Any], labels: dict[str, str]) -> str:
    guide = data["guide"]
    recommendation_cards: list[str] = []
    for recommendation in guide["recommendations"]:
        recommendation_cards.append(
            '<article class="decision-card">'
            f"<h3>{h(recommendation['choice'])}</h3>"
            f'<p><strong>{h(labels["best_for"])}:</strong> '
            f'{h(recommendation["best_for"])}</p>'
            f'<p><strong>{h(labels["rationale"])}:</strong> '
            f'{h(recommendation["why"])}</p>'
            f'<p><strong>{h(labels["tradeoffs"])}:</strong> '
            f'{h(recommendation["tradeoffs"])}</p>'
            "</article>"
        )
    parts = [
        f'<div class="answer-card"><p class="fact-label">'
        f'{h(labels["bottom_line"])}</p>'
        f'{paragraphs(guide["bottom_line"], "lead")}</div>',
        f'<h3>{h(labels["key_points"])}</h3>{html_list(guide["key_points"])}',
        f'<h3>{h(labels["recommendations"])}</h3>'
        f'<div class="decision-grid">{"".join(recommendation_cards)}</div>',
    ]

    for guide_section in guide["sections"]:
        item_cards: list[str] = []
        for item in guide_section["items"]:
            item_cards.append(
                '<article class="guide-item">'
                f"<h4>{h(item['name'])}</h4>"
                f"{paragraphs(item['explanation'])}"
                f'<p class="fact-label">{h(labels["guide_examples"])}</p>'
                f"{html_list(item['examples'])}"
                "</article>"
            )
        parts.append(
            '<div class="guide-section">'
            f"<h3>{h(guide_section['title'])}</h3>"
            f'<p class="guide-section__purpose"><strong>'
            f'{h(labels["guide_purpose"])}:</strong> '
            f'{h(guide_section["purpose"])}</p>'
            f'<div class="guide-item-grid">{"".join(item_cards)}</div>'
            "</div>"
        )

    next_action = guide["next_action"]
    next_items = "".join(
        f"<dt>{h(labels[key])}</dt><dd>{h(next_action[key])}</dd>"
        for key in ("action", "when", "output")
    )
    parts.append(
        f'<h3>{h(labels["next_action"])}</h3>'
        f'<div class="next-card"><dl>{next_items}</dl></div>'
    )
    return "".join(parts)


def render_resource_tracks(data: dict[str, Any], labels: dict[str, str]) -> str:
    resources = resource_index(data)
    cards: list[str] = []
    for track in data["resource_tracks"]:
        assigned = [
            resources[resource_id]
            for resource_id in track["resource_ids"]
            if resource_id in resources
        ]
        cards.append(
            '<article class="track-card">'
            f"<h3>{h(track['title'])}</h3>"
            f'<p><strong>{h(labels["best_for"])}:</strong> '
            f'{h(track["best_for"])}</p>'
            f'<p><strong>{h(labels["cadence"])}:</strong> '
            f'{h(track["cadence"])}</p>'
            f'<p><strong>{h(labels["assigned_resources"])}:</strong></p>'
            f"{linked_resource_list(assigned)}"
            f'<p class="fact-label">{h(labels["sequence"])}</p>'
            f'{html_list(track["sequence"])}'
            "</article>"
        )
    return f'<div class="track-grid">{"".join(cards)}</div>'


def render_resources(data: dict[str, Any], labels: dict[str, str]) -> str:
    cards: list[str] = []
    for resource in data["resources"]:
        meta_values = (
            ("channel", "channel"),
            ("role", "role"),
            ("level", "level"),
            ("format", "format"),
            ("time", "resource_time"),
            ("best_for", "best_for"),
            ("access", "access"),
            ("type", "type"),
        )
        chips = "".join(
            f'<span class="chip">{h(labels[label])}: {h(resource[key])}</span>'
            for key, label in meta_values
        )
        cards.append(
            f'<article class="resource-card" data-resource-id="{h(resource["id"])}">'
            f"<h3>{h(resource['title'])}</h3>"
            f'<p class="resource-card__creator">{h(resource["creator"])}</p>'
            f'<div class="card-meta">{chips}</div>'
            '<div class="resource-card__body">'
            f'<p><strong>{h(labels["why"])}:</strong> {h(resource["why"])}</p>'
            f'<p><strong>{h(labels["focus"])}:</strong> {h(resource["focus"])}</p>'
            f'<p><strong>{h(labels["limitations"])}:</strong> '
            f'{h(resource["limitations"])}</p>'
            f'<p><strong>{h(labels["verified_on"])}:</strong> '
            f'{h(resource["verified_on"])}</p>'
            "</div>"
            f'<a class="resource-link" href="{h(resource["url"])}">'
            f'{h(labels["open_resource"])} <span aria-hidden="true">↗</span></a>'
            "</article>"
        )
    return (
        f'<h3>{h(labels["choose_a_route"])}</h3>'
        f"{render_resource_tracks(data, labels)}"
        f'<h3>{h(labels["resource_cards"])}</h3>'
        f'<div class="resource-grid">{"".join(cards)}</div>'
    )


def stage_block(title: str, content: str, wide: bool = False) -> str:
    modifier = " roadmap-stage__block--wide" if wide else ""
    return (
        f'<div class="roadmap-stage__block{modifier}">'
        f'<p class="fact-label">{h(title)}</p>{content}</div>'
    )


def render_roadmap(data: dict[str, Any], labels: dict[str, str]) -> str:
    resources = resource_index(data)
    stages: list[str] = []
    for stage in sorted(data["roadmap"], key=lambda item: item["stage"]):
        assigned = [
            resources[resource_id]
            for resource_id in stage["resource_ids"]
            if resource_id in resources
        ]
        blocks = [
            stage_block(labels["objectives"], html_list(stage["objectives"])),
            stage_block(labels["prerequisites"], html_list(stage["prerequisites"])),
            stage_block(
                labels["assigned_resources"],
                linked_resource_list(assigned),
            ),
            stage_block(labels["tasks"], html_list(stage["tasks"])),
            stage_block(
                labels["deliverable"],
                f'<div class="deliverable">{h(stage["deliverable"])}</div>',
                wide=True,
            ),
            stage_block(
                labels["completion_criteria"],
                html_list(stage["completion_criteria"]),
                wide=True,
            ),
        ]
        if listify(stage.get("optional")):
            blocks.append(
                stage_block(labels["optional"], html_list(stage["optional"]), wide=True)
            )
        stages.append(
            f'<article class="roadmap-stage" data-stage="{stage["stage"]}">'
            f'<div class="roadmap-stage__number" aria-hidden="true">'
            f'{h(stage["stage"])}</div>'
            f"<h3>{h(stage['title'])}</h3>"
            f'<p class="roadmap-stage__timing">{h(labels["duration"])}: '
            f'{h(stage["duration"])} · {h(labels["weekly_effort"])}: '
            f'{h(stage["weekly_effort"])}</p>'
            f'<div class="roadmap-stage__grid">{"".join(blocks)}</div>'
            "</article>"
        )
    return f'        <div class="roadmap">{"".join(stages)}</div>'


def render_source_directory(data: dict[str, Any], labels: dict[str, str]) -> str:
    resources = resource_index(data)
    directory = data["source_directory"]
    groups: list[str] = []
    for group in directory["groups"]:
        source_items = [resources[resource_id] for resource_id in group["resource_ids"]]
        groups.append(
            '<article class="source-group">'
            f"<h3>{h(group['name'])}</h3>"
            f"{paragraphs(group['description'])}"
            f"{linked_resource_list(source_items)}"
            "</article>"
        )
    return (
        '<div class="source-selection">'
        f'<p class="fact-label">{h(labels["source_selection"])}</p>'
        f'{paragraphs(directory["selection_note"])}</div>'
        f'<div class="source-group-grid">{"".join(groups)}</div>'
    )


def render_html(
    data: dict[str, Any],
    template_path: Path,
    css_paths: list[Path],
    theme: str,
) -> str:
    """Return a complete, self-contained HTML atlas."""
    meta = data["meta"]
    labels = labels_for(meta.get("language"))
    language = str(meta.get("language") or "en")
    section_titles = [(section_id, labels[label]) for section_id, label in SECTION_KEYS]
    navigation = "\n".join(
        f'            <li><a href="#{h(section_id)}">{h(title)}</a></li>'
        for section_id, title in section_titles
    )

    rendered_sections = (
        section(1, "brief", labels["confirmed_brief"], render_brief(data, labels)),
        section(2, "guide", labels["guide"], render_guide(data, labels)),
        section(3, "resources", labels["resources"], render_resources(data, labels)),
        section(4, "roadmap", labels["roadmap"], render_roadmap(data, labels)),
        section(
            5,
            "sources",
            labels["source_directory"],
            render_source_directory(data, labels),
        ),
    )

    meta_pills = [
        f'<span class="meta-pill">{h(labels["generated"])}: '
        f'{h(meta["generated_at"])}</span>'
    ]
    if meta.get("estimated_total_time"):
        meta_pills.append(
            f'<span class="meta-pill">{h(labels["total_time"])}: '
            f'{h(meta["estimated_total_time"])}</span>'
        )

    template = template_path.read_text(encoding="utf-8")
    styles = "\n\n".join(path.read_text(encoding="utf-8") for path in css_paths)
    footer_credit = labels["footer_credit"].format(
        brand="<strong>AnythingAtlas</strong>"
    )
    replacements = {
        "{{LANG}}": h(language),
        "{{THEME}}": h(theme),
        "{{META_DESCRIPTION}}": h(meta["summary"]),
        "{{DOCUMENT_TITLE}}": h(meta["title"]),
        "{{STYLES}}": styles,
        "{{SKIP_LABEL}}": h(labels["skip_label"]),
        "{{NAV_LABEL}}": h(labels["nav_label"]),
        "{{TITLE}}": h(meta["title"]),
        "{{SUMMARY}}": h(meta["summary"]),
        "{{GENERATED_META}}": "".join(meta_pills),
        "{{NAVIGATION}}": navigation,
        "{{CONTENT}}": "\n".join(rendered_sections),
        "{{FOOTER}}": (
            f"{footer_credit} · {h(labels['generated'])}: {h(meta['generated_at'])}"
        ),
    }
    for placeholder, value in replacements.items():
        template = template.replace(placeholder, value)
    return template


def main() -> int:
    root = project_root()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Canonical atlas JSON file")
    parser.add_argument("--output", required=True, help="HTML output path")
    parser.add_argument(
        "--template",
        default=str(root / "assets/html-template/atlas.html"),
        help="HTML template path",
    )
    parser.add_argument(
        "--theme",
        choices=AVAILABLE_THEMES,
        help="Built-in visual theme; defaults to meta.theme or atlas",
    )
    parser.add_argument(
        "--css",
        help="Custom CSS path; replaces the built-in theme styles",
    )
    args = parser.parse_args()

    data = load_atlas(args.input)
    theme = args.theme or str(data["meta"].get("theme") or "atlas")
    css_paths = (
        [Path(args.css)]
        if args.css
        else built_in_style_paths(root, theme)
    )
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        render_html(data, Path(args.template), css_paths, theme),
        encoding="utf-8",
    )
    print(f"[OK] Wrote HTML ({theme}): {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
