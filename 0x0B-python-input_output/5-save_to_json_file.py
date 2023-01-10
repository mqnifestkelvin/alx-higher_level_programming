#!/usr/bin/python3
"""A Module that returns an object represented by a JSON string."""


def save_to_json_file(my_obj, filename):
    """A function that returns an object representation
    by a JSON string."""
    with open(filename, mode="w") as f:
        f.dump(my_obj, f)
