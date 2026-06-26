# === Stage 58: Add bulk update behavior for selected records ===
# Project: StudyHub
def bulk_update_records(records, updates):
    """Update multiple records in a single batch operation."""
    if not records:
        return 0
    
    updated_count = 0
    for record in records:
        try:
            # Apply specific fields from the update dictionary to the current record
            for key, value in updates.items():
                if hasattr(record, key):
                    setattr(record, key, value)
            
            # Simulate saving or committing the change (replace with actual DB call)
            record.save() 
            updated_count += 1
        except Exception as e:
            print(f"Failed to update {record.id}: {e}")
    
    return updated_count
