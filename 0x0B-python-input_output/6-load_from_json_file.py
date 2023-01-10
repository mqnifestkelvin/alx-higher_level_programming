#!/usr/bin/python3
"""That Creates an Object from a “JSON File”"""
import json


def load_from_json_file(filename):
    """A function that creates an object from a JSON file"""
    with open(filename) as f:
        return json.load(f)
