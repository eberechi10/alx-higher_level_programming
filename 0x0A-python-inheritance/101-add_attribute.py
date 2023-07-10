#!/usr/bin/python3

""" a module to define adds attributes to objects"""


def add_attribute(obj, att, value):

    """ a method that adds new attribute to an object.

    args: a function to add new attribute.
        obj: the object
        name: the attribute name
        value: the attribute value

    Raises:
        TypeError: when the attribute can't be added

    """

    if not hasattr(obj, "__dict__"):

        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
