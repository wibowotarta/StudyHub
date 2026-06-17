# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: StudyHub
from datetime import datetime, timedelta
def get_upcoming_items(checkpoints: list[dict], now: datetime = None) -> list[tuple[str, str]]:
    if now is None: now = datetime.now()
    upcoming = []
    for item in checkpoints:
        due = datetime.fromisoformat(item.get("due", ""))
        if due > now and (item.get("completed") != True):
            days_left = (due - now).days
            priority = "high" if days_left <= 2 else ("medium" if days_left <= 7 else "low")
            upcoming.append((item["title"], f"{priority}: {days_left} дн."))
    return sorted(upcoming, key=lambda x: datetime.fromisoformat(x[0].split(":")[1]) if ":" in x[0] else now)

def format_reminder_list(items: list[tuple[str, str]]) -> str:
    lines = ["🔔 Upcoming reminders:", ""]
    for title, meta in items[:5]:
        lines.append(f"  • {title} — {meta}")
    if len(items) > 5:
        lines[-1] += f"\n... и ещё {len(items) - 5}"
    return "\n".join(lines)
