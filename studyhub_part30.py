# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: StudyHub
def parse_study_date(date_str: str) -> datetime.date | None:
    """Parse flexible date strings with clear error messages."""
    if not date_str:
        return None
    
    formats = [
        "%Y-%m-%d",      # 2024-12-31
        "%d.%m.%Y",      # 31.12.2024 (RU/EU)
        "%d/%m/%Y",      # 31/12/2024
        "%B %d, %Y",     # December 31, 2024
        "%b %d, %Y",     # Dec 31, 2024
    ]
    
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str.strip(), fmt).date()
        except ValueError:
            continue
    
    raise ValueError(f"Unrecognized date format: '{date_str}'. Supported: YYYY-MM-DD, DD.MM.YYYY, etc.")
