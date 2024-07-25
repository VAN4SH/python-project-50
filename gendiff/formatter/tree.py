from .formatter_plain import format_plain
from .formatter_stylish import format_stylish
from .formatter_json import format_json


def format_tree(diff, format_name="stylish"):
    if format_name == "plain":
        return format_plain(diff)
    elif format_name == "json":
        return format_json(diff)
    return format_stylish(diff)
