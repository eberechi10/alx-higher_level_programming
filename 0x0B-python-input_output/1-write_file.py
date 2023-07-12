#!/usr/bin/python3

"""
a module to defines the function wrtie_file

"""


def write_file(filename="", text=""):

    """a method to return the characters written to filename from text"""

    with open(filename, mode="w", encoding='utf=8') as x:
        return x.write(text)
