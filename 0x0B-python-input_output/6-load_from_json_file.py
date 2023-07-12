#!/usr/bin/python3

"""
a module to creates an object from a JSON file

"""

import json


def load_from_json_file(filename):

    """method to object from a "JSON file" """

    with open(filename, mode="r", encoding="utf-8") as x:

        return json.load(x)
