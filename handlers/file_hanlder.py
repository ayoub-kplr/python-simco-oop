import json
import re


def trim_spaces(string: str):
    # Define a regular expression pattern to match quoted substrings
    pattern = r'"[^"]*"'
    # Replace spaces and hyphens with underscore
    return re.sub(pattern, lambda m: m.group(0).replace(" ", "_").replace("-", "_"), string)


def write_content(content: str, filename: str):
    with open(filename, "w") as f:
        f.write(content)


def load_json_file(filename: str = "data.json"):
    return json.load(open(filename, "r", encoding='utf-8'))
