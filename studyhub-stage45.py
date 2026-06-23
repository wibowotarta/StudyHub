# === Stage 45: Add restore from backup with validation ===
# Project: StudyHub
import json, os, hashlib

def validate_backup(path):
    try:
        with open(path) as f: data = json.load(f); return all(k in data for k in ['lessons', 'cards', 'checkpoints'])
    except Exception: return False

def restore_from_backup(backup_path, target_dir='.'):
    if not validate_backup(backup_path): raise ValueError("Invalid backup structure")
    with open(backup_path) as f: state = json.load(f)
    os.makedirs(target_dir, exist_ok=True)
    for key in ['lessons', 'cards', 'checkpoints']:
        file_name = f"{key}.json"
        if key in state and os.path.exists(os.path.join(target_dir, file_name)):
            with open(os.path.join(target_dir, file_name), 'w') as out: json.dump(state[key], out)
    print(f"Restored {len(state.get('lessons', []))} lessons, {len(state.get('cards', []))} cards.")
