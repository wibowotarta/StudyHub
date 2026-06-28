# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: StudyHub
from typing import Union, List, Dict, Any
import hashlib
from collections import defaultdict

def merge_imports(existing: List[str], new_paths: List[str]) -> List[str]:
    """Merge new imports into existing list while avoiding obvious duplicates."""
    seen = set()
    result = []
    for path in sorted(new_paths + existing):
        if not path or path.startswith('#'): continue
        key = hashlib.md5(path.encode()).hexdigest()[:8]
        if key not in seen:
            seen.add(key)
            result.append(path)
    return result

def normalize_path(p: str) -> str:
    """Normalize import paths for consistent merging."""
    p = p.strip().strip('"\'')
    if p.startswith('.'): return f"./{p}"
    if not p.endswith('.py'): return f"{p}.py"
    return p

def consolidate_modules(modules: Dict[str, List[str]]) -> Dict[str, Any]:
    """Consolidate module definitions to avoid duplicate entries across profiles."""
    consolidated = defaultdict(list)
    for name, paths in modules.items():
        normalized = [normalize_path(p) for p in paths]
        merged = merge_imports(consolidated.get(name, []), normalized)
        if len(merged) > 1:
            consolidated[name]['imports'] = list(set(merged))
            consolidated[name]['count'] = sum(len(m.get('imports', [])) for m in [consolidated[name]])
        else:
            consolidated[name]['imports'] = merged
    return dict(sorted(consolidated.items()))
