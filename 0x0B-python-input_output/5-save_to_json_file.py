#!/usr/bin/python3
"""A Module that returns an object represented by a JSON string."""


def save_to_json_file(my_obj, filename):
    """A function that returns an object representation
    by a JSON string."""
    json_obj = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as f
    return f.write(json_obj)
