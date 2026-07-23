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


REQUIRED_TOP_LEVEL = (
    "meta",
    "brief",
    "topic_brief",
    "knowledge_map",
    "source_plan",
    "starting_point",
    "resources",
    "roadmap",
    "source_notes",
    "next_action",
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


LABELS = {
    "en": {
        "brand": "AnythingAtlas",
        "tagline": "Map the best way into any topic.",
        "skip_label": "Skip to the atlas",
        "nav_label": "Atlas sections",
        "generated": "Generated",
        "total_time": "Estimated total time",
        "confirmed_brief": "Confirmed User Brief",
        "topic_brief": "Topic Brief",
        "knowledge_map": "Knowledge Map",
        "source_plan": "Source and Channel Plan",
        "starting_point": "Recommended Starting Point",
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
        "overview": "Overview",
        "why_it_matters": "Why it matters",
        "outcomes": "Expected outcomes",
        "depends_on": "Depends on",
        "none": "None",
        "topic_type": "Topic type",
        "materials": "Required materials",
        "channels": "Priority channels",
        "credibility_policy": "Credibility policy",
        "recency": "Recency rule",
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
        "why": "Why included",
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
        "tagline": "绘制进入任何主题的最佳路径。",
        "skip_label": "跳转到知识图谱正文",
        "nav_label": "知识图谱章节",
        "generated": "生成日期",
        "total_time": "预计总投入",
        "confirmed_brief": "已确认的用户需求简报",
        "topic_brief": "主题简介",
        "knowledge_map": "知识图谱",
        "source_plan": "来源与渠道方案",
        "starting_point": "推荐起点",
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
        "overview": "概览",
        "why_it_matters": "为什么重要",
        "outcomes": "预期成果",
        "depends_on": "依赖",
        "none": "无",
        "topic_type": "主题类型",
        "materials": "所需资料",
        "channels": "优先渠道",
        "credibility_policy": "可信度策略",
        "recency": "时效性规则",
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
        "why": "推荐理由",
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
        for field in ("title", "topic", "slug", "language", "generated_at", "summary"):
            if not meta.get(field):
                errors.append(f"meta.{field} is required.")
        if meta.get("slug") and slugify(str(meta["slug"])) != meta["slug"]:
            errors.append("meta.slug must already be lowercase hyphen-case.")

    for object_name in ("brief", "topic_brief", "source_plan", "starting_point", "next_action"):
        if not isinstance(data.get(object_name), dict):
            errors.append(f"{object_name} must be an object.")

    for array_name in ("knowledge_map", "resources", "roadmap", "source_notes"):
        if not isinstance(data.get(array_name), list):
            errors.append(f"{array_name} must be an array.")

    if errors:
        return errors

    if not data["knowledge_map"]:
        errors.append("knowledge_map must contain at least one node.")
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

    seen_stages: set[int] = set()
    for index, stage in enumerate(data["roadmap"], start=1):
        if not isinstance(stage, dict):
            errors.append(f"roadmap[{index}] must be an object.")
            continue
        for field in REQUIRED_STAGE_FIELDS:
            if field not in stage or stage[field] in (None, ""):
                errors.append(f"roadmap[{index}].{field} is required.")
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
