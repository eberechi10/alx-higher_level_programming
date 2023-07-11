#!/usr/bin/python3

"""
a module that search and append
"""


def append_after(filename="", search_string="", new_string=""):

    """a module to append new_string after a line contain
    search_string in filename
    """

    with open(filename, mode="r", encoding="utf-8") as x:
        n_line = []

        while True:
            line = x.readline()
            if line == "":
                break
            n_line.append(line)

            if search_string in line:
                n_line.append(new_string)

    with open(filename, mode="w", encoding="utf-8") as x:
        x.writelines(n_line)
