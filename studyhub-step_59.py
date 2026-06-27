# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: StudyHub
class BulkDeleteGuard:
    def __init__(self, storage):
        self.storage = storage
        self._confirmed = False

    def confirm(self):
        if self.storage.get("bulk_delete_confirmed", False):
            self._confirmed = True
            return True
        return False

    def execute_deletion(self, items_to_remove):
        if not self._confirmed:
            raise RuntimeError("Bulk deletion requires explicit confirmation flag.")
        
        for item in items_to_remove:
            key = f"lesson:{item['id']}"
            if key in self.storage:
                del self.storage[key]

    def reset(self):
        self._confirmed = False
