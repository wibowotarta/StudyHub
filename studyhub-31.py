# === Stage 31: Add compact table rendering for long lists ===
# Project: StudyHub
def render_compact_table(items, columns):
    if not items: return ""
    headers = [col.get("header", col["key"]) for col in columns]
    widths = {h: max(len(h), max(len(str(item[col["key"]]) or 0) for item in items)) for h, col in zip(headers, columns)}
    lines = ["| " + " | ".join(w.center(widths[h]).rstrip() if i == 0 else w.ljust(widths[h]) for h, w in zip(headers, [str(item[col["key"]]) or "" for item in items]))]
    sep = "| " + " | ".join("-" * widths[h] for h in headers) + "|"
    lines.insert(1, sep)
    return "\n".join(lines)
