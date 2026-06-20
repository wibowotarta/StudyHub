# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: StudyHub
def repair_data_integrity(data):
    if not isinstance(data, dict): return data
    for key in list(data.keys()):
        val = data[key]
        if isinstance(val, str) and len(val.strip()) == 0: del data[key]
        elif isinstance(val, dict) and 'content' in val and (not val['content'] or not isinstance(val['content'], str)):
            val.pop('content', None)
    return {k: v for k, v in data.items() if isinstance(v, (dict, list))}
