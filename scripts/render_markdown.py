#!/usr/bin/env python3
"""Render an AnythingAtlas canonical JSON model as Markdown."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from atlas_common import labels_for, listify, load_atlas, resource_index


def inline(value: Any) -> str:
    """Escape text for a Markdown inline context."""
    text = str(value).replace("\n", " ").strip()
    return text.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def bullet_lines(values: Any, indent: str = "") -> list[str]:
    """Render values as Markdown bullets."""
    return [f"{indent}- {inline(item)}" for item in listify(values)]


def labeled_value(label: str, value: Any) -> list[str]:
    """Render a labeled scalar or list."""
    values = listify(value)
    if not values:
        return []
    if len(values) == 1:
        return [f"- **{label}:** {inline(values[0])}"]
    lines = [f"- **{label}:**"]
    lines.extend(bullet_lines(values, "  "))
    return lines


def resource_link(resource: dict[str, Any]) -> str:
    """Render a verified resource as a Markdown link."""
    return f"[{inline(resource['title'])}]({resource['url']})"


def render_markdown(data: dict[str, Any]) -> str:
    """Return a complete Markdown atlas."""
    meta = data["meta"]
    labels = labels_for(meta.get("language"))
    resources = resource_index(data)
    lines: list[str] = [
        f"# {inline(meta['title'])}",
        "",
        f"> {inline(meta['summary'])}",
        "",
        f"**{labels['generated']}:** {inline(meta['generated_at'])}",
    ]
    if meta.get("estimated_total_time"):
        lines.append(
            f"**{labels['total_time']}:** {inline(meta['estimated_total_time'])}"
        )

    lines.extend(["", "---", "", f"## 1. {labels['confirmed_brief']}", ""])
    brief = data["brief"]
    brief_fields = (
        ("goal", "goal"),
        ("background", "background"),
        ("time", "time"),
        ("language", "language"),
        ("formats", "formats"),
        ("depth", "depth"),
        ("constraints", "constraints"),
        ("assumptions", "assumptions"),
    )
    for key, label_key in brief_fields:
        lines.extend(labeled_value(labels[label_key], brief.get(key)))

    guide = data["guide"]
    lines.extend(["", f"## 2. {labels['guide']}", ""])
    lines.extend(
        [
            f"### {labels['bottom_line']}",
            "",
            str(guide["bottom_line"]).strip(),
            "",
            f"### {labels['key_points']}",
            "",
        ]
    )
    lines.extend(bullet_lines(guide["key_points"]))
    lines.extend(["", f"### {labels['recommendations']}", ""])
    for recommendation in guide["recommendations"]:
        lines.extend(
            [
                f"#### {inline(recommendation['choice'])}",
                "",
                f"- **{labels['best_for']}:** {inline(recommendation['best_for'])}",
                f"- **{labels['rationale']}:** {inline(recommendation['why'])}",
                f"- **{labels['tradeoffs']}:** {inline(recommendation['tradeoffs'])}",
                "",
            ]
        )
    for guide_section in guide["sections"]:
        lines.extend(
            [
                "",
                f"### {inline(guide_section['title'])}",
                "",
                f"> **{labels['guide_purpose']}:** "
                f"{inline(guide_section['purpose'])}",
                "",
            ]
        )
        for item in guide_section["items"]:
            lines.extend(
                [
                    f"#### {inline(item['name'])}",
                    "",
                    str(item["explanation"]).strip(),
                    "",
                    f"**{labels['guide_examples']}:** "
                    + "; ".join(inline(example) for example in item["examples"]),
                    "",
                ]
            )

    next_action = guide["next_action"]
    lines.extend(["", f"### {labels['next_action']}", ""])
    for key in ("action", "when", "output"):
        lines.append(f"- **{labels[key]}:** {inline(next_action[key])}")

    lines.extend(["", f"## 3. {labels['resources']}", ""])
    lines.extend([f"### {labels['choose_a_route']}", ""])
    for track in data["resource_tracks"]:
        assigned = [
            resource_link(resources[resource_id])
            for resource_id in track["resource_ids"]
            if resource_id in resources
        ]
        lines.extend(
            [
                f"#### {inline(track['title'])}",
                "",
                f"- **{labels['best_for']}:** {inline(track['best_for'])}",
                f"- **{labels['cadence']}:** {inline(track['cadence'])}",
                f"- **{labels['assigned_resources']}:** " + ", ".join(assigned),
                "",
                f"**{labels['sequence']}**",
                "",
            ]
        )
        lines.extend(bullet_lines(track["sequence"]))
        lines.append("")

    lines.extend([f"### {labels['resource_cards']}", ""])
    for resource in data["resources"]:
        title = inline(resource["title"])
        url = str(resource["url"])
        lines.extend(
            [
                f"#### [{title}]({url})",
                "",
                f"- **{labels['creator']}:** {inline(resource['creator'])}",
                f"- **{labels['channel']}:** {inline(resource['channel'])}",
                f"- **{labels['type']}:** {inline(resource['type'])}",
                f"- **{labels['role']}:** {inline(resource['role'])}",
                f"- **{labels['level']}:** {inline(resource['level'])}",
                f"- **{labels['format']}:** {inline(resource['format'])}",
                f"- **{labels['resource_time']}:** {inline(resource['time'])}",
                f"- **{labels['best_for']}:** {inline(resource['best_for'])}",
                f"- **{labels['access']}:** {inline(resource['access'])}",
                f"- **{labels['verified_on']}:** {inline(resource['verified_on'])}",
                "",
                f"**{labels['why']}:** {str(resource['why']).strip()}",
                "",
                f"**{labels['focus']}:** {str(resource['focus']).strip()}",
                "",
                f"**{labels['limitations']}:** {str(resource['limitations']).strip()}",
                "",
            ]
        )

    lines.extend([f"## 4. {labels['roadmap']}", ""])
    for stage in sorted(data["roadmap"], key=lambda item: item["stage"]):
        assigned = [
            resource_link(resources[resource_id])
            for resource_id in stage["resource_ids"]
            if resource_id in resources
        ]
        lines.extend(
            [
                f"### {labels['stage']} {stage['stage']}: {inline(stage['title'])}",
                "",
                f"- **{labels['duration']}:** {inline(stage['duration'])}",
                f"- **{labels['weekly_effort']}:** {inline(stage['weekly_effort'])}",
                "",
                f"**{labels['objectives']}**",
                "",
            ]
        )
        lines.extend(bullet_lines(stage["objectives"]))
        lines.extend(["", f"**{labels['prerequisites']}**", ""])
        lines.extend(bullet_lines(stage["prerequisites"]))
        lines.extend(["", f"**{labels['assigned_resources']}**", ""])
        lines.extend(f"- {item}" for item in assigned)
        lines.extend(["", f"**{labels['tasks']}**", ""])
        lines.extend(bullet_lines(stage["tasks"]))
        lines.extend(
            [
                "",
                f"**{labels['deliverable']}:** {str(stage['deliverable']).strip()}",
                "",
                f"**{labels['completion_criteria']}**",
                "",
            ]
        )
        lines.extend(bullet_lines(stage["completion_criteria"]))
        optional = listify(stage.get("optional"))
        if optional:
            lines.extend(["", f"**{labels['optional']}**", ""])
            lines.extend(bullet_lines(optional))
        lines.append("")

    source_directory = data["source_directory"]
    lines.extend(["", f"## 5. {labels['source_directory']}", ""])
    lines.extend(
        [
            f"**{labels['source_selection']}:** "
            f"{str(source_directory['selection_note']).strip()}",
            "",
        ]
    )
    for group in source_directory["groups"]:
        lines.extend(
            [
                f"### {inline(group['name'])}",
                "",
                str(group["description"]).strip(),
                "",
            ]
        )
        for resource_id in group["resource_ids"]:
            resource = resources[resource_id]
            lines.append(
                f"- {resource_link(resource)} — {inline(resource['creator'])}; "
                f"{inline(resource['focus'])}"
            )
        lines.append("")

    lines.extend(
        [
            "",
            "---",
            "",
            f"*{labels['brand']} · {labels['tagline']}*",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Canonical atlas JSON file")
    parser.add_argument("--output", required=True, help="Markdown output path")
    args = parser.parse_args()

    data = load_atlas(args.input)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_markdown(data), encoding="utf-8")
    print(f"[OK] Wrote Markdown: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
