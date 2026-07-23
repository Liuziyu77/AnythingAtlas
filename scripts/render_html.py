#!/usr/bin/env python3
"""Render an AnythingAtlas canonical JSON model as self-contained HTML."""

from __future__ import annotations

import argparse
import base64
import mimetypes
import re
from html import escape
from pathlib import Path
from typing import Any

from atlas_common import labels_for, listify, load_atlas, project_root, resource_index


SECTION_KEYS = (
    ("brief", "confirmed_brief"),
    ("topic", "topic_brief"),
    ("knowledge", "knowledge_map"),
    ("sources", "source_plan"),
    ("start", "starting_point"),
    ("resources", "resources"),
    ("roadmap", "roadmap"),
    ("notes", "source_notes"),
    ("next", "next_action"),
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


def embed_image(path: Path, alt: str) -> str:
    """Return an embedded image element or an empty string."""
    if not path.is_file():
        return ""
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return (
        f'<img class="hero__logo" src="data:{h(mime)};base64,{encoded}" '
        f'alt="{h(alt)}">'
    )


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


def render_topic(data: dict[str, Any], labels: dict[str, str]) -> str:
    topic = data["topic_brief"]
    parts: list[str] = []
    if topic.get("overview"):
        parts.extend(
            [
                f"        <h3>{h(labels['overview'])}</h3>",
                f"        {paragraphs(topic['overview'], 'lead')}",
            ]
        )
    if topic.get("why_it_matters"):
        parts.extend(
            [
                f"        <h3>{h(labels['why_it_matters'])}</h3>",
                f"        {paragraphs(topic['why_it_matters'])}",
            ]
        )
    if topic.get("outcomes"):
        parts.extend(
            [
                f"        <h3>{h(labels['outcomes'])}</h3>",
                f"        {html_list(topic['outcomes'])}",
            ]
        )
    return "\n".join(parts)


def render_knowledge(data: dict[str, Any], labels: dict[str, str]) -> str:
    cards: list[str] = []
    for node in data["knowledge_map"]:
        dependencies = listify(node.get("depends_on"))
        chips = "".join(f'<span class="chip">{h(item)}</span>' for item in dependencies)
        dependency_markup = ""
        if chips:
            dependency_markup = (
                f'<div class="dependency-list" aria-label="{h(labels["depends_on"])}">'
                f'<span class="fact-label">{h(labels["depends_on"])}</span>{chips}</div>'
            )
        cards.append(
            '<article class="map-node">'
            f"<h3>{h(node['name'])}</h3>"
            f"{paragraphs(node['description'])}"
            f"{dependency_markup}"
            "</article>"
        )
    return f'        <div class="map-grid">{"".join(cards)}</div>'


def plan_block(title: str, value: Any, wide: bool = False) -> str:
    values = listify(value)
    if not values:
        return ""
    modifier = " plan-block--wide" if wide else ""
    content = h(values[0]) if len(values) == 1 else html_list(values)
    return (
        f'<div class="plan-block{modifier}"><p class="fact-label">{h(title)}</p>'
        f"{content}</div>"
    )


def render_source_plan(data: dict[str, Any], labels: dict[str, str]) -> str:
    plan = data["source_plan"]
    blocks = [
        plan_block(labels["topic_type"], plan.get("topic_type")),
        plan_block(labels["materials"], plan.get("materials")),
        plan_block(labels["credibility_policy"], plan.get("credibility_policy")),
        plan_block(labels["recency"], plan.get("recency")),
        plan_block(labels["cautions"], plan.get("cautions"), wide=True),
    ]
    channels: list[str] = []
    for channel in listify(plan.get("channels")):
        if isinstance(channel, dict):
            priority = channel.get("priority")
            priority_markup = (
                f'<span class="channel-priority">{h(priority)}</span>'
                if priority
                else ""
            )
            channels.append(
                f"<li><strong>{h(channel.get('name', ''))}</strong>{priority_markup}"
                f"<br>{h(channel.get('reason', ''))}</li>"
            )
        else:
            channels.append(f"<li>{h(channel)}</li>")
    if channels:
        blocks.append(
            '<div class="plan-block plan-block--wide">'
            f'<p class="fact-label">{h(labels["channels"])}</p>'
            f'<ul class="channel-list">{"".join(channels)}</ul></div>'
        )
    return f'        <div class="plan-grid">{"".join(blocks)}</div>'


def render_starting_point(data: dict[str, Any], labels: dict[str, str]) -> str:
    point = data["starting_point"]
    items = "".join(
        f"<dt>{h(labels[key])}</dt><dd>{h(point[key])}</dd>"
        for key in ("action", "resource", "reason")
        if point.get(key)
    )
    return f'        <div class="starting-card"><dl>{items}</dl></div>'


def render_resources(data: dict[str, Any], labels: dict[str, str]) -> str:
    cards: list[str] = []
    for resource in data["resources"]:
        meta_values = (
            ("role", "role"),
            ("level", "level"),
            ("format", "format"),
            ("time", "resource_time"),
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
    return f'        <div class="resource-grid">{"".join(cards)}</div>'


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
            resources[resource_id]["title"]
            for resource_id in stage["resource_ids"]
            if resource_id in resources
        ]
        blocks = [
            stage_block(labels["objectives"], html_list(stage["objectives"])),
            stage_block(labels["prerequisites"], html_list(stage["prerequisites"])),
            stage_block(labels["assigned_resources"], html_list(assigned)),
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


def render_source_notes(data: dict[str, Any]) -> str:
    notes: list[str] = []
    for note in data["source_notes"]:
        if isinstance(note, dict):
            severity = re.sub(r"[^a-z0-9-]", "", str(note.get("severity", "note")).lower())
            notes.append(
                f'<li class="source-note source-note--{h(severity or "note")}">'
                f'<strong>{h(note.get("topic", "Note"))}:</strong> '
                f'{h(note.get("note", ""))}</li>'
            )
        else:
            notes.append(f'<li class="source-note">{h(note)}</li>')
    return f'        <ul class="source-notes">{"".join(notes)}</ul>'


def render_next_action(data: dict[str, Any], labels: dict[str, str]) -> str:
    next_action = data["next_action"]
    items = "".join(
        f"<dt>{h(labels[key])}</dt><dd>{h(next_action[key])}</dd>"
        for key in ("action", "when", "output")
        if next_action.get(key)
    )
    return f'        <div class="next-card"><dl>{items}</dl></div>'


def render_html(
    data: dict[str, Any],
    template_path: Path,
    css_path: Path,
    logo_path: Path,
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
        section(2, "topic", labels["topic_brief"], render_topic(data, labels)),
        section(3, "knowledge", labels["knowledge_map"], render_knowledge(data, labels)),
        section(4, "sources", labels["source_plan"], render_source_plan(data, labels)),
        section(
            5,
            "start",
            labels["starting_point"],
            render_starting_point(data, labels),
        ),
        section(6, "resources", labels["resources"], render_resources(data, labels)),
        section(7, "roadmap", labels["roadmap"], render_roadmap(data, labels)),
        section(8, "notes", labels["source_notes"], render_source_notes(data)),
        section(9, "next", labels["next_action"], render_next_action(data, labels)),
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
    styles = css_path.read_text(encoding="utf-8")
    replacements = {
        "{{LANG}}": h(language),
        "{{META_DESCRIPTION}}": h(meta["summary"]),
        "{{DOCUMENT_TITLE}}": h(f"{meta['title']} · AnythingAtlas"),
        "{{STYLES}}": styles,
        "{{LOGO}}": embed_image(logo_path, "AnythingAtlas"),
        "{{BRAND}}": h(labels["brand"]),
        "{{SKIP_LABEL}}": h(labels["skip_label"]),
        "{{NAV_LABEL}}": h(labels["nav_label"]),
        "{{TITLE}}": h(meta["title"]),
        "{{SUMMARY}}": h(meta["summary"]),
        "{{GENERATED_META}}": "".join(meta_pills),
        "{{NAVIGATION}}": navigation,
        "{{CONTENT}}": "\n".join(rendered_sections),
        "{{FOOTER}}": (
            f"<strong>AnythingAtlas</strong> · {h(labels['tagline'])} "
            f"· {h(labels['generated'])}: {h(meta['generated_at'])}"
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
        "--css",
        default=str(root / "assets/html-template/atlas.css"),
        help="CSS asset path",
    )
    parser.add_argument(
        "--logo",
        default=str(root / "assets/logo/logo.png"),
        help="Logo image to embed",
    )
    args = parser.parse_args()

    data = load_atlas(args.input)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        render_html(data, Path(args.template), Path(args.css), Path(args.logo)),
        encoding="utf-8",
    )
    print(f"[OK] Wrote HTML: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
