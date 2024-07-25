def format_value(value, depth):
    indent = "    " * depth
    if isinstance(value, dict):
        items = [
            f"{indent}    {k}: {format_value(v, depth + 1)}" for k, v in value.items()
        ]
        return f"{{\n{items}\n{indent}}}"
    return str(value)


def format_stylish(diff, depth=0):
    result = []
    indent = "    " * depth

    for key, value in sorted(diff.items()):
        status = value["status"]

        if status == "nested":
            result.append(
                f"{indent}    {key}: {format_stylish(value['value'], depth + 1)}"
            )
        elif status == "added":
            result.append(
                f"{indent}  + {key}: {format_value(value['value'], depth + 1)}"
            )
        elif status == "removed":
            result.append(
                f"{indent}  - {key}: {format_value(value['value'], depth + 1)}"
            )
        elif status == "changed":
            old = format_value(value["old_value"], depth + 1)
            new = format_value(value["new_value"], depth + 1)
            result.append(f"{indent}  - {key}: {old}")
            result.append(f"{indent}  + {key}: {new}")
        else:
            result.append(
                f"{indent}    {key}: {format_value(value['value'], depth + 1)}"
            )

    return "{\n" + "\n".join(result) + "\n" + indent + "}"
