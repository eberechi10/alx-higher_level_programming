#!/usr/bin/python3

def simple_delete(a_dictionary: dict, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
