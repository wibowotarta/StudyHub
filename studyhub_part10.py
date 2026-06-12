# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: StudyHub
class SearchEngine:
    def __init__(self, data):
        self.data = data
        self._index = {k.lower(): v for k, v in data.items()}

    def search(self, query):
        q = query.strip().lower()
        if not q: return []
        hits = set()
        for key, val in self._index.items():
            if isinstance(val, str) and q in val.lower():
                hits.add(key)
        results = [self.data[k] for k in sorted(hits)]
        return results

    def add(self, item):
        self.data.append(item)
