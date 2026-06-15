# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: StudyHub
import json, os, shutil
from datetime import datetime, timedelta
ARCHIVE_DIR = 'archive'
DAYS_TO_ARCHIVE = 30
def archive_old_records(db_path):
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)
    with open(db_path, 'r', encoding='utf-8') as f:
        records = json.load(f)
    cutoff_date = datetime.now() - timedelta(days=DAYS_TO_ARCHIVE)
    archived_count = 0
    for key in list(records.keys()):
        if isinstance(key, str):
            try:
                created_at_str = key.split('::')[1]
                created_at = datetime.fromisoformat(created_at_str.replace('Z', '+00:00'))
            except (IndexError, ValueError):
                continue
            if created_at < cutoff_date and records[key]['status'] == 'completed':
                archived_key = f"{key}::{datetime.now().strftime('%Y%m%d%H%M%S')}"
                records[archived_key] = records.pop(key)
                shutil.copy2(db_path, os.path.join(ARCHIVE_DIR, os.path.basename(db_path)))
                with open(db_path, 'w', encoding='utf-8') as f:
                    json.dump(records, f, ensure_ascii=False, indent=2)
                archived_count += 1
    return archived_count
