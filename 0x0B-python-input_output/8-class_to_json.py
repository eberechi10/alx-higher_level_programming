#!/usr/bin/python3

"""
a module to define the class_to_json class

"""


def class_to_json(obj):

    """method to return dictionary data structure

    Args:
         obj: class instance

    Return: dict: dictionary
    """

    return obj.__dict__
