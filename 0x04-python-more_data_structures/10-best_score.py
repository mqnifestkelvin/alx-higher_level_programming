#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    hold = list(a_dictionary.key())[0]
    max_check = a_dictionary[hold]
    for key, value in a_dictionary.items():
        if value > max_check:
            max_check = value
            hold = key
    return hold
