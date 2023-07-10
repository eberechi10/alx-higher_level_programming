#!/usr/bin/python3

""" a module to check type of object specified class """

def is_same_class(obj, a_class):

    """ a module return the type of a_class

    Args:
        obj: the object
        a_class: the type of class

    Returns:
        True if is a_class, otherwise False
    """

    return type(obj) is a_class
