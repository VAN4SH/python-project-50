def get_different(data1, data2):
    """Returns a list with a difference."""
    list_diff = []
    set_keys = sorted(data1.keys() | data2.keys())
    for key in set_keys:
        if key not in data2:
            list_diff.append({
                "key": key,
                "type": 'removed',
                "value": data1[key],
            })
            continue
        elif key not in data1:
            list_diff.append({
                "key": key,
                "type": 'added',
                "value": data2[key],
            })
            continue
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            list_diff.append({
                "key": key,
                "type": 'nested',
                "value": get_different(data1[key], data2[key])
            })
            continue
        elif data1[key] == data2[key]:
            list_diff.append({
                "key": key,
                "type": 'equal',
                "value": data1[key],
            })
            continue
        else:
            list_diff.append({
                "key": key,
                "type": 'updated',
                "value1": data1[key],
                "value2": data2[key],
            })
    return list_diff
