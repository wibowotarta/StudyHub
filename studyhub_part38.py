# === Stage 38: Add data integrity checks for broken references ===
# Project: StudyHub
def validate_references(data):
    errors = []
    for item in data:
        if 'lesson_id' in item and item['lesson_id'] is not None:
            ref_exists = any(i.get('id') == item['lesson_id'] for i in data)
            if not ref_exists:
                errors.append(f"Broken lesson reference in {item.get('type', 'unknown')}")
        if 'card_set_id' in item and item['card_set_id'] is not None:
            ref_exists = any(i.get('id') == item['card_set_id'] for i in data)
            if not ref_exists:
                errors.append(f"Broken card set reference in {item.get('type', 'unknown')}")
        if 'checkpoint_id' in item and item['checkpoint_id'] is not None:
            ref_exists = any(i.get('id') == item['checkpoint_id'] for i in data)
            if not ref_exists:
                errors.append(f"Broken checkpoint reference in {item.get('type', 'unknown')}")
    return errors
