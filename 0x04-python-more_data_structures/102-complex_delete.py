#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for elm in list(a_dictionary.keys()):
        if a_dictionary[elm] == value:
            del a_dictionary[elm]
    return a_dictionary
