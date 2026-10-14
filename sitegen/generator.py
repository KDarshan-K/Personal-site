from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT_CONTENT_DIRS = ("projects", "notes", "research")

def read_config(root: Path) -> dict[str, Any]:
    config_path = root / "site.yml"
    if not config_path.exists():
        return {"title": "Darshan Kagadal", "description": "", "links": {}}
    data = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    return data

def parse_markdown(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    metadata: dict[str, Any] = {}
    body = raw
    if raw.startswith("---\n"):
        parts = raw.split("---", 2)
        if len(parts) == 3:
            metadata = yaml.safe_load(parts[1]) or {}
            body = parts[2].lstrip("\r\n")
    html = markdown.markdown(
        body,
        extensions=["extra", "toc", "fenced_code", "sane_lists"],
        output_format="html5",
    )
    metadata.setdefault("title", path.stem.replace("-", " ").title())
    metadata.setdefault("date", "")
    metadata.setdefault("summary", "")
    metadata["html"] = html
    metadata["slug"] = path.stem
    metadata["source"] = path
    return metadata

def load_collection(root: Path, name: str) -> list[dict[str, Any]]:
    folder = root / "content" / name
    if not folder.exists():
        return []
    items = [parse_markdown(p) for p in folder.glob("*.md")]
    items.sort(key=lambda item: str(item.get("date", "")), reverse=True)
    return items

def render(env: Environment, template: str, context: dict[str, Any], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(env.get_template(template).render(**context), encoding="utf-8")

def build_site(root: Path, output: Path) -> int:
    template_dir = root / "templates"
    content_dir = root / "content"
    assets_dir = root / "assets"
    if not template_dir.exists() or not content_dir.exists():
        raise FileNotFoundError("Expected templates/ and content/ directories in project root.")

    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True, exist_ok=True)

    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    config = read_config(root)
    collections = {name: load_collection(root, name) for name in ROOT_CONTENT_DIRS}
    about_path = content_dir / "about.md"
    about = parse_markdown(about_path) if about_path.exists() else {
        "title": "About", "html": "<p>Add your introduction in content/about.md.</p>"
    }

    count = 0
    common = {"site": config, "collections": collections}
    render(env, "index.html", {**common, "about": about}, output / "index.html")
    count += 1

    for section in ROOT_CONTENT_DIRS:
        render(env, "collection.html", {
            **common, "section": section, "items": collections[section],
        }, output / section / "index.html")
        count += 1
        for item in collections[section]:
            render(env, "detail.html", {
                **common, "section": section, "item": item,
            }, output / section / item["slug"] / "index.html")
            count += 1

    render(env, "about.html", {**common, "about": about}, output / "about" / "index.html")
    render(env, "contact.html", common, output / "contact" / "index.html")
    count += 2

    if assets_dir.exists():
        shutil.copytree(assets_dir, output / "assets", dirs_exist_ok=True)
    return count
