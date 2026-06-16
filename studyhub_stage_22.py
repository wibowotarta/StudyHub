# === Stage 22: Add favorite records and quick favorite listing ===
# Project: StudyHub
class FavoriteManager:
    def __init__(self, db):
        self.db = db
    
    def toggle_favorite(self, item_id):
        with self.db.cursor() as cur:
            cur.execute("SELECT is_fav FROM items WHERE id = ?", (item_id,))
            row = cur.fetchone()
            if not row or row[0] == 1:
                return False
            cur.execute("UPDATE items SET is_fav = ? WHERE id = ?", (1, item_id))
            self.db.commit()
        return True
    
    def get_favorites(self):
        with self.db.cursor() as cur:
            cur.execute("SELECT * FROM items WHERE is_fav = 1 ORDER BY created_at DESC")
            return cur.fetchall()
