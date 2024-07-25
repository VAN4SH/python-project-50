import os
import json
import yaml

from gendiff.parser import parse, get_file_format
from gendiff.diff import build_diff
from gendiff.formatter.tree import format_tree


def parse_file(filepath):
    file_format = get_file_format(filepath)
    if file_format is None:
        raise ValueError(f"Unsupported file format: {filepath}")

    with open(filepath) as file:
        return parse(file.read(), file_format)


def generate_diff(filepath1, filepath2, format_name="stylish"):
    data1 = parse_file(filepath1)
    data2 = parse_file(filepath2)

    diff = build_diff(data1, data2)
    return format_tree(diff, format_name)
