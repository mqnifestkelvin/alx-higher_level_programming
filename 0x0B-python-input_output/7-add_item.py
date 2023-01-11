#!/usr/bin/python3
'''Module for saving argv info via json to file.'''
import json
import os.path
import sys


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

    load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

    arg_len = len(sys.argv)
    json_file = "add_file.json"
    list_0 = []

    if not os.path.exists(json_file):
        json_list = load_from_json_file(json_file)

    for i in range(1, arg_len):
        list_0.append(sys.argv[i])

    save_to_json_file(list_0, json_file)
