#!/usr/bin/python3

"""
a module to define the json string module.

"""

import json


def from_json_string(my_str):

    """a method to return an object of a JSON string"""

    return json.loads(my_str)
