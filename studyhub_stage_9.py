# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: StudyHub
def sort_study_items(items, key='title', reverse=False):
    if key == 'date': return sorted(items, key=lambda x: x.get('created_at') or 0, reverse=True)
    if key == 'priority': return sorted(items, key=lambda x: x.get('priority') or 1, reverse=True)
    if key == 'updated': return sorted(items, key=lambda x: x.get('updated_at') or 0, reverse=False)
    return sorted(items, key=lambda x: x.get(key) or '', reverse=reverse)
