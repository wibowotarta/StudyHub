# === Stage 60: Add saved views for frequently used filters ===
# Project: StudyHub
class SavedViewManager:
    def __init__(self, db):
        self.db = db
    
    def save_view(self, name, filters=None, sort_by='date'):
        if filters is None:
            filters = {}
        cursor = self.db.cursor()
        try:
            cursor.execute(
                "INSERT INTO saved_views (name, filters_json, sort_by) VALUES (%s, %s, %s)",
                (name, json.dumps(filters), sort_by)
            )
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(f"Failed to save view {name}: {e}")
            return False
    
    def load_view(self, name):
        cursor = self.db.cursor()
        try:
            cursor.execute(
                "SELECT filters_json, sort_by FROM saved_views WHERE name = %s",
                (name,)
            )
            row = cursor.fetchone()
            if row:
                return {
                    'filters': json.loads(row[0]),
                    'sort_by': row[1]
                }
        finally:
            cursor.close()
        return None
    
    def list_views(self):
        cursor = self.db.cursor()
        try:
            cursor.execute("SELECT name FROM saved_views")
            return [row[0] for row in cursor.fetchall()]
        finally:
            cursor.close()

# Usage example to persist a "Morning Review" view with specific filters
if __name__ == "__main__":
    # Assuming 'db' is your existing database connection object
    manager = SavedViewManager(db)
    
    # Save a new view configuration
    if not manager.save_view("Morning Review", {"status": "completed", "category": "math"}):
        exit(1)
        
    # Load and apply the saved view filters to your main query logic here
