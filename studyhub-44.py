# === Stage 44: Add backup creation for the data file ===
# Project: StudyHub
import os, json, datetime
def backup_data(data_file: str, backup_dir: str = "backups"):
    if not data_file or not os.path.exists(data_file): return
    base_name = os.path.splitext(os.path.basename(data_file))[0]
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    target_path = os.path.join(backup_dir, f"{base_name}_{timestamp}.json")
    os.makedirs(backup_dir, exist_ok=True)
    try:
        with open(data_file, "r", encoding="utf-8") as src:
            content = json.load(src)
        with open(target_path, "w", encoding="utf-8") as dst:
            json.dump(content, dst, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Backup failed: {e}")
