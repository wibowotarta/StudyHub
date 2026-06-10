# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: StudyHub
def validate_id(value):
    if not isinstance(value, str) or len(value) < 3:
        raise ValueError("ID must be a string with at least 3 characters.")
    return value

def validate_short_text(value, max_len=100):
    if not isinstance(value, str):
        raise TypeError("Text must be a string.")
    if len(value) > max_len:
        raise ValueError(f"Text exceeds {max_len} characters.")
    return value

def validate_required_field(value):
    if value is None or (isinstance(value, str) and not value.strip()):
        raise ValueError("Field cannot be empty.")
    return value

def validate_positive_int(value):
    try:
        int_val = int(value)
        if int_val <= 0:
            raise ValueError("Value must be a positive integer.")
        return int_val
    except (ValueError, TypeError):
        raise TypeError("Value must be convertible to a positive integer.")

def validate_date_string(value):
    import re
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not isinstance(value, str) or not re.match(pattern, value):
        raise ValueError("Date must be in YYYY-MM-DD format.")
    return value
