#!/usr/bin/python3

""" module to check  if the object is an instance of a class that
inherited (directly or indirectly) from the specified class """


def inherits_from(obj, a_class):
    """ a method to returns True if obj is an instance of a_class

    Args:
        obj: the object
        a_class: the class type

    Returns:
        True if obj is an instance of a_class, otherwise False.
    """

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
