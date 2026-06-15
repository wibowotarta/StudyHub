# === Stage 20: Add duplicate detection for newly created records ===
# Project: StudyHub
def detect_duplicates(records, new_record):
    key_fields = ['title', 'content']
    for r in records:
        if all(getattr(r, f) == getattr(new_record, f) for f in key_fields):
            return True
    return False
