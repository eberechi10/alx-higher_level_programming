#!/usr/bin/python3

"""
a module that defines the JSON string module.

"""

import json


def to_json_string(my_obj):

    """a method to return SON object string"""
    return json.dumps(my_obj)
