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

    orientation = data["orientation"]
    lines.extend(["", f"## 2. {labels['orientation']}", ""])
    lines.extend(
        [
            f"### {labels['bottom_line']}",
            "",
            str(orientation["bottom_line"]).strip(),
            "",
            f"### {labels['key_points']}",
            "",
        ]
    )
    lines.extend(bullet_lines(orientation["key_points"]))
    lines.extend(["", f"### {labels['recommendations']}", ""])
    for recommendation in orientation["recommendations"]:
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
    lines.extend([f"### {labels['tradeoffs']}", ""])
    lines.extend(bullet_lines(orientation["tradeoffs"]))

    field_guide = data["field_guide"]
    lines.extend(["", f"## 3. {labels['field_guide']}", ""])
    lines.extend(labeled_value(labels["as_of"], field_guide.get("as_of")))
    lines.extend(labeled_value(labels["scope"], field_guide.get("scope")))
    lines.append("")
    for entry in field_guide["entries"]:
        lines.extend(
            [
                f"### {inline(entry['name'])}",
                "",
                f"- **{labels['category']}:** {inline(entry['category'])}",
                f"- **{labels['why_it_matters']}:** "
                f"{inline(entry['why_it_matters'])}",
                f"- **{labels['representative_examples']}:** "
                + ", ".join(
                    inline(item) for item in listify(entry["representative_examples"])
                ),
                f"- **{labels['selection_note']}:** "
                f"{inline(entry['selection_note'])}",
                "",
            ]
        )

    action_kit = data["action_kit"]
    lines.extend([f"## 4. {labels['action_kit']}", ""])
    if listify(action_kit.get("setup")):
        lines.extend([f"### {labels['setup']}", ""])
        for item in action_kit["setup"]:
            lines.extend(
                [
                    f"- **{inline(item['item'])}:** "
                    f"{inline(item['recommendation'])} — "
                    f"{labels['rationale']}: {inline(item['why'])}"
                ]
            )
        lines.append("")
    for key in ("first_session", "decision_rules", "safety_checks", "failure_modes"):
        values = listify(action_kit.get(key))
        if values:
            lines.extend([f"### {labels[key]}", ""])
            lines.extend(bullet_lines(values))
            lines.append("")

    lines.extend([f"## 5. {labels['knowledge_map']}", ""])
    for node in data["knowledge_map"]:
        lines.extend([f"### {inline(node['name'])}", "", str(node["description"]).strip()])
        dependencies = listify(node.get("depends_on"))
        if dependencies:
            lines.extend(
                [
                    "",
                    f"**{labels['depends_on']}:** "
                    + ", ".join(inline(item) for item in dependencies),
                ]
            )
        lines.append("")

    lines.extend(["", f"## 6. {labels['resource_tracks']}", ""])
    for track in data["resource_tracks"]:
        assigned = [
            resources[resource_id]["title"]
            for resource_id in track["resource_ids"]
            if resource_id in resources
        ]
        lines.extend(
            [
                f"### {inline(track['title'])}",
                "",
                f"- **{labels['best_for']}:** {inline(track['best_for'])}",
                f"- **{labels['cadence']}:** {inline(track['cadence'])}",
                f"- **{labels['assigned_resources']}:** "
                + ", ".join(inline(item) for item in assigned),
                "",
                f"**{labels['sequence']}**",
                "",
            ]
        )
        lines.extend(bullet_lines(track["sequence"]))
        lines.append("")

    lines.extend([f"## 7. {labels['resources']}", ""])
    for resource in data["resources"]:
        title = inline(resource["title"])
        url = str(resource["url"])
        lines.extend(
            [
                f"### [{title}]({url})",
                "",
                f"- **{labels['creator']}:** {inline(resource['creator'])}",
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

    lines.extend([f"## 8. {labels['roadmap']}", ""])
    for stage in sorted(data["roadmap"], key=lambda item: item["stage"]):
        assigned = [
            resources[resource_id]["title"]
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
        lines.extend(bullet_lines(assigned))
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

    source_plan = data["source_plan"]
    lines.extend([f"## 9. {labels['source_plan']}", ""])
    for key in (
        "topic_type",
        "materials",
        "channels",
        "credibility_policy",
        "recency",
        "format_fit",
        "cautions",
    ):
        value = source_plan.get(key)
        if key == "channels" and value:
            if lines and lines[-1] != "":
                lines.append("")
            lines.append(f"### {labels[key]}")
            lines.append("")
            for channel in listify(value):
                if isinstance(channel, dict):
                    name = inline(channel.get("name", ""))
                    priority = inline(channel.get("priority", ""))
                    reason = inline(channel.get("reason", ""))
                    suffix = f" ({priority})" if priority else ""
                    lines.append(f"- **{name}{suffix}:** {reason}")
                else:
                    lines.append(f"- {inline(channel)}")
            lines.append("")
        else:
            lines.extend(labeled_value(labels[key], value))

    lines.extend([f"## 10. {labels['source_notes']}", ""])
    for note in data["source_notes"]:
        if isinstance(note, dict):
            topic = inline(note.get("topic", labels["source_notes"]))
            severity = inline(note.get("severity", "note"))
            content = str(note.get("note", "")).strip()
            lines.append(f"- **{topic} ({severity}):** {content}")
        else:
            lines.append(f"- {inline(note)}")

    next_action = data["next_action"]
    lines.extend(["", f"## 11. {labels['next_action']}", ""])
    for key in ("action", "when", "output"):
        if next_action.get(key):
            lines.append(f"- **{labels[key]}:** {inline(next_action[key])}")

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
