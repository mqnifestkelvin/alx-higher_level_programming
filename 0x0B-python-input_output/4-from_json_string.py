#!/usr/bin/python3
import json
"""A Module that Returns an Object Represented by JSON string."""


def from_json_string(my_str):
    """This function returns an ibject representation of a JSON string."""
    return json.load(my_str)
