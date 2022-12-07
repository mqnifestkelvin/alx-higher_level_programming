#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, value in dict(sorted(a_dictionary.items())).items():
        print("{}: {}".format(key, value))
