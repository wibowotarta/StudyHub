# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: StudyHub
def delete_item(item_id, confirm=False):
    if not confirm:
        response = f"Deletion of item {item_id} requires explicit confirmation. Please set confirm=True."
        return response
    # Perform deletion logic here
    # Assuming a global or passed-in storage dictionary 'storage' exists
    if item_id in storage:
        del storage[item_id]
        return f"Item {item_id} successfully deleted from storage."
    else:
        return f"No item found with ID {item_id} to delete."
