# === Stage 34: Add support for multiple local user profiles ===
# Project: StudyHub
class UserProfilesManager:
    def __init__(self, storage_dir=".studyhub_profiles"):
        self.storage_dir = storage_dir
        self.profiles = {}
        
    def load_profile(self, name):
        import json
        path = f"{self.storage_dir}/{name}.json"
        try:
            with open(path) as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Profile '{name}' not found.")
            return None
            
    def save_profile(self, name, data):
        import os
        path = f"{self.storage_dir}/{name}.json"
        if not os.path.exists(path):
            self.profiles[name] = {}
            
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
            
    def create_profile(self, name, default_data=None):
        import json
        path = f"{self.storage_dir}/{name}.json"
        if not os.path.exists(path):
            self.profiles[name] = {}
            data = default_data or {"lessons": [], "cards": [], "checkpoints": []}
            with open(path, "w") as f:
                json.dump(data, f, indent=2)
            return True
        return False
        
    def get_active_profile(self):
        import os
        if not self.profiles:
            profiles = [f for f in os.listdir(self.storage_dir) if f.endswith(".json")]
            if profiles:
                name = profiles[0].replace(".json", "")
                return self.load_profile(name)
        elif len(self.profiles) == 1:
            return list(self.profiles.values())[0]
        else:
            print("Select a profile to load.")
            return None
