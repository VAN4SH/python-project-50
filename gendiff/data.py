import json
import yaml


def parse_data(data, file_format):
    """Parses data based on the given format."""
    if file_format in ('yml', 'yaml'):
        return yaml.safe_load(data)
    elif file_format == 'json':
        return json.loads(data)
    else:
        raise ValueError('Unsupported file format')


def load_file(filepath):
    """Loads a file and determines its format."""
    file_format = get_file_format(filepath)
    with open(filepath, 'r') as file:
        data = file.read()
    return data, file_format


def get_file_format(filepath):
    """Returns the file format."""
    if filepath.endswith(('.yml', '.yaml')):
        return 'yaml'
    elif filepath.endswith('.json'):
        return 'json'
    else:
        raise ValueError('Unsupported file format')


def get_data(filepath):
    data, file_format = load_file(filepath)
    return parse_data(data, file_format)
