# === Stage 66: Add export of a short status dashboard ===
# Project: StudyHub
def export_dashboard(data):
    from datetime import datetime
    total_lessons = sum(len(l) for l in data.get("lessons", []))
    completed_cards = len([c for c in data.get("cards", []) if c.get("status") == "done"])
    active_checkpoints = len([cp for cp in data.get("checkpoints", []) if not cp.get("completed")])
    last_update = datetime.now().strftime("%Y-%m-%d %H:%M")
    status_lines = [
        f"=== StudyHub Status Dashboard ===",
        f"Total Lessons: {total_lessons}",
        f"Completed Cards: {completed_cards}/{len(data.get('cards', []))}",
        f"Active Checkpoints: {active_checkpoints}",
        f"Last Updated: {last_update}",
        "=================================",
    ]
    print("\n".join(status_lines))
