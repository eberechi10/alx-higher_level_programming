#!/usr/bin/python3

def best_score(a_dictionary: my_dict):
    if not a_dictionary:
        return None

    big = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == big:
            return key
