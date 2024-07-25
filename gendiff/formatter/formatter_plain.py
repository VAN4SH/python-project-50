import json


def format_value(value):
    if isinstance(value, (dict, list)) and value:
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    return json.dumps(value)


def format_plain(diff, path=""):
    result = []
    for key, value in sorted(diff.items()):
        full_path = f"{path}.{key}".strip(".")
        status = value["status"]

        if status == "added":
            result.append(
                f"Property '{full_path}' was added with value: {format_value(value['value'])}"
            )
        elif status == "removed":
            result.append(f"Property '{full_path}' was removed")
        elif status == "changed":
            old = format_value(value["old_value"])
            new = format_value(value["new_value"])
            result.append(f"Property '{full_path}' was updated. From {old} to {new}")
        elif status == "nested":
            result.extend(format_plain(value["value"], full_path))

    return "\n".join(result)
