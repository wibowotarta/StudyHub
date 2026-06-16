# === Stage 24: Add grouped summaries by category or status ===
# Project: StudyHub
def group_summaries(data, key_field='category'):
    groups = {}
    for item in data:
        k = item.get(key_field)
        if k is None: continue
        if k not in groups: groups[k] = []
        groups[k].append(item)
    
    def summarize(group):
        total = len(group)
        completed = sum(1 for x in group if x.get('status') == 'done')
        return {'total': total, 'completed': completed, 'pending': total - completed}
    
    result = {k: summarize(v) for k, v in groups.items()}
    # Sort by completion rate descending then alphabetically
    sorted_result = dict(sorted(result.items(), key=lambda x: (-x[1]['total'], x[0])))
    return sorted_result
