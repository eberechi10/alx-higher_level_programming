#!/usr/bin/python3

"""
 a method to write an Object to json file

"""

import json


def save_to_json_file(my_obj, filename):

    """ method that initialize object to a text file, using JSON"""

    with open(filename, mode="w", encoding='utf-8') as x:
        json.dump(my_obj, x)
