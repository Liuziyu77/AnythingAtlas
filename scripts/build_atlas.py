#!/usr/bin/env python3
"""Build and validate synchronized AnythingAtlas Markdown and HTML files."""

from __future__ import annotations

import argparse
from pathlib import Path

from atlas_common import AVAILABLE_THEMES, load_atlas, project_root
from render_html import built_in_style_paths, render_html
from render_markdown import render_markdown
from validate_deliverables import validate_deliverables


def main() -> int:
    root = project_root()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Canonical atlas JSON file")
    parser.add_argument("--output-dir", required=True, help="Output directory")
    parser.add_argument(
        "--basename",
        help="Output basename without extension; defaults to anything-atlas-<slug>",
    )
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
    basename = args.basename or f"anything-atlas-{data['meta']['slug']}"
    if Path(basename).name != basename or basename in {"", ".", ".."}:
        parser.error("--basename must be a simple filename without directories.")
    if basename.endswith((".md", ".html")):
        parser.error("--basename must not include a file extension.")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    markdown_path = output_dir / f"{basename}.md"
    html_path = output_dir / f"{basename}.html"

    markdown_path.write_text(render_markdown(data), encoding="utf-8")
    html_path.write_text(
        render_html(
            data,
            Path(args.template),
            css_paths,
            theme,
        ),
        encoding="utf-8",
    )

    errors, warnings = validate_deliverables(data, markdown_path, html_path)
    for warning in warnings:
        print(f"[WARN] {warning}")
    for error in errors:
        print(f"[ERROR] {error}")
    if errors:
        print(f"[FAIL] Built files but validation found {len(errors)} error(s).")
        return 1

    print(f"[OK] Markdown: {markdown_path}")
    print(f"[OK] HTML ({theme}): {html_path}")
    print("[OK] Deliverables are synchronized and valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
