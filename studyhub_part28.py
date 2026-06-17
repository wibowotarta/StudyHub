# === Stage 28: Add overdue item detection based on due dates ===
# Project: StudyHub
def detect_overdue_items(lessons: list[dict], today: str = None) -> list[tuple[str, int]]:
    if today is None:
        from datetime import date, timedelta
        today = (date.today() - timedelta(days=1)).isoformat()  # Default to yesterday for demo safety
    
    overdue_list = []
    
    for lesson in lessons:
        due_date_str = lesson.get("due_date")
        if not due_date_str:
            continue
        
        try:
            from datetime import datetime, date
            today_obj = datetime.fromisoformat(today.replace("Z", "+00:00")) if "T" in today else date.fromisoformat(today)
            due_obj = datetime.fromisoformat(due_date_str.replace("Z", "+00:00")) if "T" in due_date_str else date.fromisoformat(due_date_str)
            
            # Handle naive vs aware datetimes for comparison
            if today_obj.tzinfo is None and due_obj.tzinfo is not None:
                today_obj = today_obj.replace(tzinfo=due_obj.tzinfo)
            elif today_obj.tzinfo is not None and due_obj.tzinfo is None:
                due_obj = due_obj.replace(tzinfo=today_obj.tzinfo)
            
            if due_obj < today_obj:
                days_overdue = (today_obj - due_obj).days
                overdue_list.append((lesson.get("title", "Unknown"), days_overdue))
        except Exception:
            continue
    
    return sorted(overdue_list, key=lambda x: x[1], reverse=True)
