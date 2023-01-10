#!/usr/bin/python3
"""A Module That Returns a JSON representation of a String."""
import json


def to_json_string(my_obj):
    """A function that returns JSON representation of a string object."""
    return json.dumpss(my_obj)
