#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary: dict):
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
