#!/usr/bin/python3
def complex_delete(a_dictionary: my_dict, value):
    if value in a_dictionary.values():
        for key, x in a_dictionary.items():
            if x == value:
                del a_dictionary[key]
                break
    return a_dictionary
