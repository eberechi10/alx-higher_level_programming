#!/usr/bin/python3

""" a module to Reads and prints the text file.

"""


def read_file(filename=""):

    """a method to read a text file and prints."""

    with open(filename, mode="r", encoding="utf-8") as x:
        print(x.read(), end="")
