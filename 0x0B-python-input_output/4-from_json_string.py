#!/usr/bin/python3
"""A Module that Returns an Object Represented by JSON string."""
import json


def from_json_string(my_str):
    """This function returns an ibject representation of a JSON string."""
    return json.loads(my_str)
