# === Stage 43: Add CSV import for the primary record type ===
# Project: StudyHub
import csv, json
from pathlib import Path

def load_csv_records(source_path: str) -> list[dict]:
    records = []
    with open(source_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                # Attempt to cast common numeric fields if they exist in the schema
                record = {k: (int(v) if k in ('id', 'points', 'duration') else float(v)) 
                           for k, v in row.items()}
                records.append(record)
            except ValueError:
                continue
    return records

def merge_csv_to_json(csv_path: str, json_path: str):
    existing = load_json(json_path) if Path(json_path).exists() else []
    new_records = load_csv_records(csv_path)
    # Simple deduplication by 'id' if present, otherwise append all
    seen_ids = {r.get('id') for r in existing}
    filtered = [r for r in new_records if not (r.get('id') and r['id'] in seen_ids)]
    merged = existing + filtered
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    merge_csv_to_json('lessons.csv', 'data/lessons.json')
