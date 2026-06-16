# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: StudyHub
def manage_tags(tags, item):
    if "tags" not in item:
        item["tags"] = set()
    tag_name = tags.strip().lower() if isinstance(tags, str) else tags[0]
    if tag_name and tag_name not in item["tags"]:
        item["tags"].add(tag_name)
    elif "" in item["tags"]:
        item["tags"].discard("")
    return item

def generate_tag_summary(items):
    summary = {}
    for i, it in enumerate(items):
        if "tags" not in it: continue
        for tag in sorted(it["tags"]):
            if tag not in summary:
                summary[tag] = {"count": 0, "items": []}
            summary[tag]["count"] += 1
            summary[tag]["items"].append(i)
    return summary
