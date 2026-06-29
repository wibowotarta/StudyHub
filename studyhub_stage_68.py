# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: StudyHub
def generate_changelog(activity_log):
    """Generate a compact changelog from activity log entries."""
    if not activity_log:
        return "No changes recorded."
    
    lines = []
    current_date = None
    
    for entry in activity_log:
        date_str = entry.get("date", "")
        action = entry.get("action", "")
        details = entry.get("details", "")
        
        if date_str and date_str != current_date:
            lines.append(f"\n[{date_str}]\n")
            current_date = date_str
        
        if action == "add":
            lines.append(f"- Added {details}")
        elif action == "update":
            lines.append(f"- Updated {details}")
        elif action == "delete":
            lines.append(f"- Removed {details}")
    
    return "\n".join(lines).strip()
