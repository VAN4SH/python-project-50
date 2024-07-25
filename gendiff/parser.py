import json
import yaml
import os


def parse(data, file_format):
    if file_format == 'json':
        return json.loads(data)
    elif file_format in ['yml', 'yaml']:
        return yaml.safe_load(data)
    else:
        raise ValueError(f"Unsupported file format: {file_format}")

def get_file_format(filepath):
    _, ext = os.path.splitext(filepath)
    return ext[1:] if ext else None
