# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: StudyHub
import json, os

def load_safe(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[WARN] File not found: {path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"[ERROR] Malformed JSON in '{path}': {e}")
        return {}

def save_safe(path, data):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[ERROR] Failed to write '{path}': {e}")
        return False

def merge_profiles(base_path, new_path):
    base = load_safe(base_path)
    new = load_safe(new_path)
    if not new:
        return base
    
    merged = dict(base)
    
    for key in new:
        if key in merged and isinstance(merged[key], list) and isinstance(new[key], list):
            merged[key].extend(new[key])
        elif key in merged and isinstance(merged[key], dict) and isinstance(new[key], dict):
            merged[key] = {**merged[key], **new[key]}
        else:
            merged[key] = new[key]
    
    return merged
