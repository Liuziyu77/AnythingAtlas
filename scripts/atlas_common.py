#!/usr/bin/env python3
"""Shared helpers for AnythingAtlas renderers and validators."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


class AtlasValidationError(ValueError):
    """Raised when a canonical atlas model is invalid."""


CURRENT_SCHEMA_VERSION = "0.3"


REQUIRED_TOP_LEVEL = (
    "meta",
    "brief",
    "guide",
    "resource_tracks",
    "resources",
    "roadmap",
    "source_directory",
)

REQUIRED_BRIEF_FIELDS = (
    "goal",
    "background",
    "time",
    "language",
    "formats",
    "depth",
    "constraints",
    "assumptions",
)

REQUIRED_RECOMMENDATION_FIELDS = (
    "choice",
    "best_for",
    "why",
    "tradeoffs",
)

REQUIRED_GUIDE_SECTION_FIELDS = (
    "title",
    "purpose",
    "items",
)

REQUIRED_GUIDE_ITEM_FIELDS = (
    "name",
    "explanation",
    "examples",
)

REQUIRED_RESOURCE_TRACK_FIELDS = (
    "title",
    "best_for",
    "cadence",
    "resource_ids",
    "sequence",
)

REQUIRED_SOURCE_GROUP_FIELDS = (
    "name",
    "description",
    "resource_ids",
)

REQUIRED_RESOURCE_FIELDS = (
    "id",
    "title",
    "creator",
    "url",
    "channel",
    "type",
    "role",
    "level",
    "format",
    "time",
    "best_for",
    "access",
    "why",
    "focus",
    "limitations",
    "verified_on",
)

REQUIRED_STAGE_FIELDS = (
    "stage",
    "title",
    "duration",
    "weekly_effort",
    "objectives",
    "prerequisites",
    "resource_ids",
    "tasks",
    "deliverable",
    "completion_criteria",
    "optional",
)

AVAILABLE_THEMES = (
    "atlas",
    "scholar",
    "archive",
    "signal",
    "workshop",
)


LABELS = {
    "en": {
        "brand": "AnythingAtlas",
        "tagline": "Map the best way into any topic",
        "footer_credit": "Built with {brand}",
        "skip_label": "Skip to the atlas",
        "nav_label": "Atlas sections",
        "generated": "Generated",
        "total_time": "Estimated total time",
        "confirmed_brief": "Confirmed User Brief",
        "guide": "Core Guide",
        "resource_tracks": "Resource Tracks",
        "resources": "Curated Resource Atlas",
        "roadmap": "Detailed Learning or Exploration Roadmap",
        "source_directory": "Source Directory",
        "next_action": "Next Action",
        "goal": "Goal",
        "background": "Starting point",
        "time": "Available time",
        "language": "Language",
        "formats": "Preferred formats",
        "depth": "Desired depth",
        "constraints": "Constraints",
        "assumptions": "Assumptions",
        "bottom_line": "Bottom line",
        "key_points": "What matters",
        "recommendations": "Recommendations",
        "recommendation": "Recommendation",
        "choice": "Choice",
        "best_for": "Best for",
        "tradeoffs": "Trade-offs",
        "guide_examples": "Examples",
        "guide_purpose": "What this section answers",
        "choose_a_route": "Choose a route",
        "resource_cards": "Resource details",
        "channel": "Channel",
        "source_selection": "How these sources were selected",
        "cadence": "Cadence",
        "sequence": "Sequence",
        "none": "None",
        "action": "Action",
        "resource": "Resource",
        "reason": "Why this first",
        "creator": "Creator",
        "type": "Type",
        "role": "Role",
        "level": "Level",
        "format": "Format",
        "resource_time": "Time",
        "access": "Access",
        "why": "Why included",
        "rationale": "Why",
        "focus": "Focus",
        "limitations": "Limitations",
        "verified_on": "Verified",
        "open_resource": "Open resource",
        "stage": "Stage",
        "duration": "Duration",
        "weekly_effort": "Weekly effort",
        "objectives": "Objectives",
        "prerequisites": "Prerequisites",
        "assigned_resources": "Assigned resources",
        "tasks": "Tasks",
        "deliverable": "Deliverable",
        "completion_criteria": "Completion criteria",
        "optional": "Optional branches",
        "when": "When",
        "output": "Expected output",
    },
    "zh": {
        "brand": "AnythingAtlas",
        "tagline": "规划学习任何主题的最佳路径",
        "footer_credit": "由 {brand} 生成",
        "skip_label": "跳转到知识图谱正文",
        "nav_label": "知识图谱章节",
        "generated": "生成日期",
        "total_time": "预计总投入",
        "confirmed_brief": "已确认的用户需求简报",
        "guide": "核心指南",
        "resource_tracks": "资源学习路线",
        "resources": "精选资源",
        "roadmap": "详细学习或探索路线图",
        "source_directory": "资源出处",
        "next_action": "下一步行动",
        "goal": "目标",
        "background": "当前起点",
        "time": "可用时间",
        "language": "语言",
        "formats": "偏好形式",
        "depth": "期望深度",
        "constraints": "限制条件",
        "assumptions": "假设",
        "bottom_line": "直接结论",
        "key_points": "真正重要的点",
        "recommendations": "具体建议",
        "recommendation": "建议",
        "choice": "选择",
        "best_for": "适合",
        "tradeoffs": "取舍与限制",
        "guide_examples": "具体例子",
        "guide_purpose": "本节回答",
        "choose_a_route": "选择适合你的路线",
        "resource_cards": "资源详情",
        "channel": "来源渠道",
        "source_selection": "资源筛选说明",
        "cadence": "节奏",
        "sequence": "使用顺序",
        "none": "无",
        "action": "行动",
        "resource": "资源",
        "reason": "为什么从这里开始",
        "creator": "作者或机构",
        "type": "类型",
        "role": "用途",
        "level": "级别",
        "format": "形式",
        "resource_time": "所需时间",
        "access": "获取方式",
        "why": "推荐理由",
        "rationale": "原因",
        "focus": "重点",
        "limitations": "局限",
        "verified_on": "验证日期",
        "open_resource": "打开资源",
        "stage": "阶段",
        "duration": "持续时间",
        "weekly_effort": "每周投入",
        "objectives": "目标",
        "prerequisites": "前置要求",
        "assigned_resources": "指定资源",
        "tasks": "任务",
        "deliverable": "阶段产出",
        "completion_criteria": "完成标准",
        "optional": "可选分支",
        "when": "时间",
        "output": "预期产出",
    },
}


def labels_for(language: str | None) -> dict[str, str]:
    """Return localized renderer labels."""
    normalized = (language or "en").lower()
    return LABELS["zh"] if normalized.startswith("zh") else LABELS["en"]


def listify(value: Any) -> list[Any]:
    """Normalize a scalar or missing value to a list."""
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return value
    return [value]


def slugify(value: str) -> str:
    """Normalize text to a safe output filename slug."""
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "topic"


def valid_http_url(value: str) -> bool:
    """Return whether a value is an absolute HTTP(S) URL."""
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate_model(data: dict[str, Any]) -> list[str]:
    """Return human-readable validation errors for a canonical atlas model."""
    errors: list[str] = []

    if not isinstance(data, dict):
        return ["The atlas root must be a JSON object."]

    for key in REQUIRED_TOP_LEVEL:
        if key not in data:
            errors.append(f"Missing top-level field: {key}")

    if errors:
        return errors

    meta = data.get("meta")
    if not isinstance(meta, dict):
        errors.append("meta must be an object.")
    else:
        for field in (
            "schema_version",
            "title",
            "topic",
            "slug",
            "language",
            "generated_at",
            "summary",
        ):
            if not meta.get(field):
                errors.append(f"meta.{field} is required.")
        if (
            meta.get("schema_version")
            and meta["schema_version"] != CURRENT_SCHEMA_VERSION
        ):
            errors.append(
                f"meta.schema_version must be {CURRENT_SCHEMA_VERSION}; "
                f"found {meta['schema_version']}."
            )
        if meta.get("slug") and slugify(str(meta["slug"])) != meta["slug"]:
            errors.append("meta.slug must already be lowercase hyphen-case.")
        if meta.get("theme") and meta["theme"] not in AVAILABLE_THEMES:
            errors.append(
                "meta.theme must be one of: " + ", ".join(AVAILABLE_THEMES)
            )

    for object_name in ("brief", "guide", "source_directory"):
        if not isinstance(data.get(object_name), dict):
            errors.append(f"{object_name} must be an object.")

    for array_name in ("resource_tracks", "resources", "roadmap"):
        if not isinstance(data.get(array_name), list):
            errors.append(f"{array_name} must be an array.")

    if errors:
        return errors

    brief = data["brief"]
    for field in REQUIRED_BRIEF_FIELDS:
        if field not in brief or brief[field] in (None, ""):
            errors.append(f"brief.{field} is required.")
    if not listify(brief.get("formats")):
        errors.append(
            "brief.formats must record the user's preference or an explicit default."
        )
    for field in ("formats", "constraints", "assumptions"):
        if field in brief and not isinstance(brief[field], list):
            errors.append(f"brief.{field} must be an array.")

    guide = data["guide"]
    for field in (
        "bottom_line",
        "key_points",
        "recommendations",
        "sections",
        "next_action",
    ):
        if field not in guide or guide[field] in (None, ""):
            errors.append(f"guide.{field} is required.")
    for field in ("key_points", "recommendations", "sections"):
        if field in guide and not isinstance(guide[field], list):
            errors.append(f"guide.{field} must be an array.")
    if not listify(guide.get("key_points")):
        errors.append("guide.key_points must contain at least one item.")
    recommendations = listify(guide.get("recommendations"))
    if not recommendations:
        errors.append("guide.recommendations must contain at least one item.")
    for index, recommendation in enumerate(recommendations, start=1):
        if not isinstance(recommendation, dict):
            errors.append(f"guide.recommendations[{index}] must be an object.")
            continue
        for field in REQUIRED_RECOMMENDATION_FIELDS:
            if field not in recommendation or recommendation[field] in (None, ""):
                errors.append(
                    f"guide.recommendations[{index}].{field} is required."
                )

    sections = listify(guide.get("sections"))
    if not sections:
        errors.append("guide.sections must contain at least one useful subsection.")
    for section_index, guide_section in enumerate(sections, start=1):
        if not isinstance(guide_section, dict):
            errors.append(f"guide.sections[{section_index}] must be an object.")
            continue
        for field in REQUIRED_GUIDE_SECTION_FIELDS:
            if field not in guide_section or guide_section[field] in (None, "", []):
                errors.append(
                    f"guide.sections[{section_index}].{field} is required."
                )
        items = listify(guide_section.get("items"))
        if "items" in guide_section and not isinstance(guide_section["items"], list):
            errors.append(f"guide.sections[{section_index}].items must be an array.")
        for item_index, item in enumerate(items, start=1):
            if not isinstance(item, dict):
                errors.append(
                    f"guide.sections[{section_index}].items[{item_index}] "
                    "must be an object."
                )
                continue
            for field in REQUIRED_GUIDE_ITEM_FIELDS:
                if field not in item or item[field] in (None, "", []):
                    errors.append(
                        f"guide.sections[{section_index}].items[{item_index}]."
                        f"{field} is required."
                    )
            if "examples" in item and not isinstance(item["examples"], list):
                errors.append(
                    f"guide.sections[{section_index}].items[{item_index}]."
                    "examples must be an array."
                )

    next_action = guide.get("next_action")
    if not isinstance(next_action, dict):
        errors.append("guide.next_action must be an object.")
    else:
        for field in ("action", "when", "output"):
            if field not in next_action or next_action[field] in (None, ""):
                errors.append(f"guide.next_action.{field} is required.")

    if not data["resource_tracks"]:
        errors.append("resource_tracks must contain at least one track.")
    if not data["resources"]:
        errors.append("resources must contain at least one verified resource.")
    if not data["roadmap"]:
        errors.append("roadmap must contain at least one stage.")

    resource_ids: set[str] = set()
    for index, resource in enumerate(data["resources"], start=1):
        if not isinstance(resource, dict):
            errors.append(f"resources[{index}] must be an object.")
            continue
        for field in REQUIRED_RESOURCE_FIELDS:
            if field not in resource or resource[field] in (None, ""):
                errors.append(f"resources[{index}].{field} is required.")
        resource_id = str(resource.get("id", ""))
        if resource_id:
            if resource_id in resource_ids:
                errors.append(f"Duplicate resource id: {resource_id}")
            resource_ids.add(resource_id)
        url = str(resource.get("url", ""))
        if url and not valid_http_url(url):
            errors.append(f"Resource {resource_id or index} has an invalid URL: {url}")

    for index, track in enumerate(data["resource_tracks"], start=1):
        if not isinstance(track, dict):
            errors.append(f"resource_tracks[{index}] must be an object.")
            continue
        for field in REQUIRED_RESOURCE_TRACK_FIELDS:
            if field not in track or track[field] in (None, "", []):
                errors.append(f"resource_tracks[{index}].{field} is required.")
        for field in ("resource_ids", "sequence"):
            if field in track and not isinstance(track[field], list):
                errors.append(f"resource_tracks[{index}].{field} must be an array.")
        for resource_id in listify(track.get("resource_ids")):
            if resource_id not in resource_ids:
                errors.append(
                    f"resource_tracks[{index}] references unknown resource id: "
                    f"{resource_id}"
                )

    seen_stages: set[int] = set()
    for index, stage in enumerate(data["roadmap"], start=1):
        if not isinstance(stage, dict):
            errors.append(f"roadmap[{index}] must be an object.")
            continue
        for field in REQUIRED_STAGE_FIELDS:
            if field not in stage or stage[field] in (None, ""):
                errors.append(f"roadmap[{index}].{field} is required.")
        for field in (
            "objectives",
            "prerequisites",
            "resource_ids",
            "tasks",
            "completion_criteria",
            "optional",
        ):
            if field in stage and not isinstance(stage[field], list):
                errors.append(f"roadmap[{index}].{field} must be an array.")
        stage_number = stage.get("stage")
        if not isinstance(stage_number, int) or stage_number < 1:
            errors.append(f"roadmap[{index}].stage must be a positive integer.")
        elif stage_number in seen_stages:
            errors.append(f"Duplicate roadmap stage number: {stage_number}")
        else:
            seen_stages.add(stage_number)
        for resource_id in listify(stage.get("resource_ids")):
            if resource_id not in resource_ids:
                errors.append(
                    f"roadmap[{index}] references unknown resource id: {resource_id}"
                )

    source_directory = data["source_directory"]
    for field in ("selection_note", "groups"):
        if field not in source_directory or source_directory[field] in (None, "", []):
            errors.append(f"source_directory.{field} is required.")
    groups = listify(source_directory.get("groups"))
    if "groups" in source_directory and not isinstance(
        source_directory["groups"], list
    ):
        errors.append("source_directory.groups must be an array.")
    covered_resource_ids: set[str] = set()
    for index, group in enumerate(groups, start=1):
        if not isinstance(group, dict):
            errors.append(f"source_directory.groups[{index}] must be an object.")
            continue
        for field in REQUIRED_SOURCE_GROUP_FIELDS:
            if field not in group or group[field] in (None, "", []):
                errors.append(f"source_directory.groups[{index}].{field} is required.")
        if "resource_ids" in group and not isinstance(group["resource_ids"], list):
            errors.append(
                f"source_directory.groups[{index}].resource_ids must be an array."
            )
        for resource_id in listify(group.get("resource_ids")):
            if resource_id not in resource_ids:
                errors.append(
                    f"source_directory.groups[{index}] references unknown resource "
                    f"id: {resource_id}"
                )
            else:
                covered_resource_ids.add(resource_id)
    missing_from_directory = sorted(resource_ids - covered_resource_ids)
    if missing_from_directory:
        errors.append(
            "source_directory must include every curated resource; missing: "
            + ", ".join(missing_from_directory)
        )

    return errors


def load_atlas(path: str | Path) -> dict[str, Any]:
    """Load and validate a canonical atlas JSON file."""
    source = Path(path)
    try:
        with source.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise AtlasValidationError(f"Unable to load {source}: {exc}") from exc

    errors = validate_model(data)
    if errors:
        raise AtlasValidationError("\n".join(errors))
    return data


def resource_index(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Index resources by stable ID."""
    return {str(item["id"]): item for item in data["resources"]}


def project_root() -> Path:
    """Return the skill root from this script location."""
    return Path(__file__).resolve().parents[1]
