#!/usr/bin/python3

""" module to check for same class or Inherited"""


def is_kind_of_class(obj, a_class):

    """mrthod that checkn if obj is an instance of a_class.

    Args:
        obj: data type
        a_class: class object

    Returns: True or False

    """
    return isinstance(obj, a_class)
