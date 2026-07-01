# === Stage 73: Add a lightweight HTML report export ===
# Project: StudyHub
import json, html, os
from pathlib import Path

def generate_report(data: dict) -> str:
    """Generates a compact HTML summary from study data."""
    title = data.get("title", "StudyHub Report")
    stats = data.get("stats", {})
    lessons = data.get("lessons", [])
    
    html_parts = [f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>{html.escape(title)}</title></head>
<body style="font-family:sans-serif;max-width:600px;margin:auto;padding:20px;">
<h1>{html.escape(title)}</h1>
<div style="background:#f4f4f4;padding:15px;border-radius:8px;">
<strong>Progress:</strong><br/>
Completed Lessons: {stats.get('completed', 0)}<br/>
Total Checkpoints: {stats.get('checkpoints', 0)}<br/>
Cards Reviewed: {stats.get('cards', 0)}</div>
<h2>Lessons</h2>
<ul>"""]

    for lesson in lessons:
        html_parts.append(f"<li>{html.escape(lesson.get('title', ''))} - Status: {html.escape(str(lesson.get('status', 'unknown')))}<br/>")
    
    html_parts.extend(["</ul></body></html>", ""])
    return "\n".join(html_parts)

if __name__ == "__main__":
    data = {"title": "StudyHub Summary", "stats": {"completed": 12, "checkpoints": 45, "cards": 30}, "lessons": [{"title": "Python Basics", "status": "done"}, {"title": "Web Scraping", "status": "in_progress"}]}
    report_html = generate_report(data)
    Path("studyhub_report.html").write_text(report_html)
