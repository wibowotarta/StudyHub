# === Stage 42: Add CSV export without external dependencies ===
# Project: StudyHub
def export_progress_to_csv(lessons, cards, checkpoints):
    import csv
    from datetime import datetime
    
    rows = [
        {
            "lesson_id": l["id"],
            "lesson_title": l.get("title", ""),
            "card_count": len(cards),
            "last_checkpoint_date": c["date"] if (c := next((ck for ck in checkpoints if ck["lesson_id"] == l["id"]), {})) else "",
            "completion_status": "completed" if any(ck["status"] == "done" for ck in checkpoints if ck["lesson_id"] == l["id"]) else "in_progress",
        }
        for l in lessons
    ]
    
    with open("studyhub_export.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["lesson_id", "lesson_title", "card_count", "last_checkpoint_date", "completion_status"])
        writer.writeheader()
        writer.writerows(rows)
