# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: StudyHub
from typing import Optional, List
def filter_items(items: List[dict], status: Optional[str] = None, category: Optional[str] = None, owner: Optional[str] = None, tag: Optional[str] = None) -> List[dict]:
    result = []
    for item in items:
        if status is not None and item.get("status") != status: continue
        if category is not None and item.get("category") != category: continue
        if owner is not None and item.get("owner") != owner: continue
        if tag is not None and item.get("tags", []) is None or tag not in item["tags"]: continue
        result.append(item)
    return result
