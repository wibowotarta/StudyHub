# === Stage 46: Add a schema version field and migration helper ===
# Project: StudyHub
from typing import Any, Dict, Optional
import json
from pathlib import Path

SCHEMA_VERSION = 2
MIGRATION_LOGS: list[Dict[str, str]] = []

def migrate_schema(data: dict[str, Any], version: int) -> tuple[dict[str, Any], bool]:
    if version < SCHEMA_VERSION:
        if "schema_version" not in data or data["schema_version"] != version:
            data.setdefault("schema_version", SCHEMA_VERSION)
            MIGRATION_LOGS.append({"from": version, "to": SCHEMA_VERSION})
            return data, True
    return data, False

def ensure_schema_compliance(file_path: Path) -> None:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return
    if not isinstance(content, dict):
        return
    _, changed = migrate_schema(content, SCHEMA_VERSION)
    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
