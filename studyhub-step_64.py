# === Stage 64: Add validation for relationship references ===
# Project: StudyHub
def validate_relationships(data):
    errors = []
    for item in data:
        if 'lesson_id' in item and item['lesson_id'] is not None:
            lesson_exists = any(i.get('id') == item['lesson_id'] for i in data)
            if not lesson_exists:
                errors.append(f"Invalid lesson_id {item['lesson_id']} in card '{item.get('title', 'unknown')}'.")
        if 'card_id' in item and item['card_id'] is not None:
            card_exists = any(i.get('id') == item['card_id'] for i in data)
            if not card_exists:
                errors.append(f"Invalid card_id {item['card_id']} in checkpoint '{item.get('title', 'unknown')}'.")
        if 'checkpoint_id' in item and item['checkpoint_id'] is not None:
            checkpoint_exists = any(i.get('id') == item['checkpoint_id'] for i in data)
            if not checkpoint_exists:
                errors.append(f"Invalid checkpoint_id {item['checkpoint_id']} in progress '{item.get('title', 'unknown')}'.")
    return errors
