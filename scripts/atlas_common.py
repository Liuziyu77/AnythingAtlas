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


CURRENT_SCHEMA_VERSION = "0.2"


REQUIRED_TOP_LEVEL = (
    "meta",
    "brief",
    "orientation",
    "field_guide",
    "action_kit",
    "knowledge_map",
    "resource_tracks",
    "resources",
    "roadmap",
    "source_plan",
    "source_notes",
    "next_action",
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

REQUIRED_FIELD_ENTRY_FIELDS = (
    "name",
    "category",
    "why_it_matters",
    "representative_examples",
    "selection_note",
)

REQUIRED_ACTION_SETUP_FIELDS = (
    "item",
    "recommendation",
    "why",
)

REQUIRED_RESOURCE_TRACK_FIELDS = (
    "title",
    "best_for",
    "cadence",
    "resource_ids",
    "sequence",
)

REQUIRED_SOURCE_PLAN_FIELDS = (
    "topic_type",
    "materials",
    "channels",
    "credibility_policy",
    "recency",
    "format_fit",
    "cautions",
)

REQUIRED_RESOURCE_FIELDS = (
    "id",
    "title",
    "creator",
    "url",
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
        "orientation": "Direct Orientation",
        "field_guide": "Field Guide",
        "action_kit": "Practical Action Kit",
        "knowledge_map": "Knowledge Map",
        "resource_tracks": "Resource Tracks",
        "source_plan": "Source and Channel Plan",
        "resources": "Curated Resource Atlas",
        "roadmap": "Detailed Learning or Exploration Roadmap",
        "source_notes": "Source Notes",
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
        "as_of": "As of",
        "scope": "Scope",
        "category": "Category",
        "representative_examples": "Representative examples",
        "selection_note": "Selection note",
        "setup": "Setup",
        "first_session": "First session",
        "decision_rules": "Decision rules",
        "safety_checks": "Safety or quality checks",
        "failure_modes": "Failure modes",
        "cadence": "Cadence",
        "sequence": "Sequence",
        "why_it_matters": "Why it matters",
        "depends_on": "Depends on",
        "none": "None",
        "topic_type": "Topic type",
        "materials": "Required materials",
        "channels": "Priority channels",
        "credibility_policy": "Credibility policy",
        "recency": "Recency rule",
        "format_fit": "Format and cadence fit",
        "cautions": "Channel cautions",
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
        "orientation": "先给结论",
        "field_guide": "领域实战地图",
        "action_kit": "实操工具箱",
        "knowledge_map": "知识图谱",
        "resource_tracks": "资源学习路线",
        "source_plan": "来源与渠道方案",
        "resources": "精选资源图谱",
        "roadmap": "详细学习或探索路线图",
        "source_notes": "来源说明",
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
        "as_of": "截至",
        "scope": "范围",
        "category": "类别",
        "representative_examples": "代表性例子",
        "selection_note": "选择提示",
        "setup": "准备与工具",
        "first_session": "第一次实操",
        "decision_rules": "决策规则",
        "safety_checks": "安全或质量检查",
        "failure_modes": "常见失败方式",
        "cadence": "节奏",
        "sequence": "使用顺序",
        "why_it_matters": "为什么重要",
        "depends_on": "依赖",
        "none": "无",
        "topic_type": "主题类型",
        "materials": "所需资料",
        "channels": "优先渠道",
        "credibility_policy": "可信度策略",
        "recency": "时效性规则",
        "format_fit": "形式与节奏适配",
        "cautions": "渠道注意事项",
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

    for object_name in (
        "brief",
        "orientation",
        "field_guide",
        "action_kit",
        "source_plan",
        "next_action",
    ):
        if not isinstance(data.get(object_name), dict):
            errors.append(f"{object_name} must be an object.")

    for array_name in (
        "knowledge_map",
        "resource_tracks",
        "resources",
        "roadmap",
        "source_notes",
    ):
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

    orientation = data["orientation"]
    for field in ("bottom_line", "key_points", "recommendations", "tradeoffs"):
        if field not in orientation or orientation[field] in (None, ""):
            errors.append(f"orientation.{field} is required.")
    if not listify(orientation.get("key_points")):
        errors.append("orientation.key_points must contain at least one item.")
    recommendations = listify(orientation.get("recommendations"))
    for field in ("key_points", "recommendations", "tradeoffs"):
        if field in orientation and not isinstance(orientation[field], list):
            errors.append(f"orientation.{field} must be an array.")
    if not recommendations:
        errors.append("orientation.recommendations must contain at least one item.")
    for index, recommendation in enumerate(recommendations, start=1):
        if not isinstance(recommendation, dict):
            errors.append(f"orientation.recommendations[{index}] must be an object.")
            continue
        for field in REQUIRED_RECOMMENDATION_FIELDS:
            if field not in recommendation or recommendation[field] in (None, ""):
                errors.append(
                    f"orientation.recommendations[{index}].{field} is required."
                )

    field_guide = data["field_guide"]
    for field in ("as_of", "scope", "entries"):
        if field not in field_guide or field_guide[field] in (None, ""):
            errors.append(f"field_guide.{field} is required.")
    entries = listify(field_guide.get("entries"))
    if "entries" in field_guide and not isinstance(field_guide["entries"], list):
        errors.append("field_guide.entries must be an array.")
    if not entries:
        errors.append("field_guide.entries must contain at least one entry.")
    for index, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict):
            errors.append(f"field_guide.entries[{index}] must be an object.")
            continue
        for field in REQUIRED_FIELD_ENTRY_FIELDS:
            if field not in entry or entry[field] in (None, "", []):
                errors.append(f"field_guide.entries[{index}].{field} is required.")
        if "representative_examples" in entry and not isinstance(
            entry["representative_examples"], list
        ):
            errors.append(
                f"field_guide.entries[{index}].representative_examples "
                "must be an array."
            )

    action_kit = data["action_kit"]
    for field in (
        "setup",
        "first_session",
        "decision_rules",
        "safety_checks",
        "failure_modes",
    ):
        if field not in action_kit:
            errors.append(f"action_kit.{field} is required.")
        elif not isinstance(action_kit[field], list):
            errors.append(f"action_kit.{field} must be an array.")
    if not listify(action_kit.get("first_session")):
        errors.append("action_kit.first_session must contain at least one action.")
    if not listify(action_kit.get("decision_rules")):
        errors.append("action_kit.decision_rules must contain at least one rule.")
    for index, item in enumerate(listify(action_kit.get("setup")), start=1):
        if not isinstance(item, dict):
            errors.append(f"action_kit.setup[{index}] must be an object.")
            continue
        for field in REQUIRED_ACTION_SETUP_FIELDS:
            if field not in item or item[field] in (None, ""):
                errors.append(f"action_kit.setup[{index}].{field} is required.")

    source_plan = data["source_plan"]
    for field in REQUIRED_SOURCE_PLAN_FIELDS:
        if field not in source_plan or source_plan[field] in (None, "", []):
            errors.append(f"source_plan.{field} is required.")
    for field in ("materials", "channels", "credibility_policy", "cautions"):
        if field in source_plan and not isinstance(source_plan[field], list):
            errors.append(f"source_plan.{field} must be an array.")

    if not data["knowledge_map"]:
        errors.append("knowledge_map must contain at least one node.")
    if not data["resource_tracks"]:
        errors.append("resource_tracks must contain at least one track.")
    if not data["resources"]:
        errors.append("resources must contain at least one verified resource.")
    if not data["roadmap"]:
        errors.append("roadmap must contain at least one stage.")

    for index, node in enumerate(data["knowledge_map"], start=1):
        if not isinstance(node, dict):
            errors.append(f"knowledge_map[{index}] must be an object.")
            continue
        for field in ("name", "description", "depends_on"):
            if field not in node or node[field] in (None, ""):
                errors.append(f"knowledge_map[{index}].{field} is required.")
        if "depends_on" in node and not isinstance(node["depends_on"], list):
            errors.append(f"knowledge_map[{index}].depends_on must be an array.")

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

    next_action = data["next_action"]
    for field in ("action", "when", "output"):
        if field not in next_action or next_action[field] in (None, ""):
            errors.append(f"next_action.{field} is required.")

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
