#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    n_dict = a_dictionary.copy()
    for key in a_dictionary:
        n_dict[key] *= 2
    return n_dict
