#!/usr/bin/python3

"""
a module to define the append string module.

"""


def append_write(filename="", text=""):

    """a method to return the characters added"""

    with open(filename, mode="a", encoding='utf=8') as x:
        return x.write(text)
