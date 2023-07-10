#!/usr/bin/python3

""" module that contain the class MyList"""


class MyList(list):

    """a class to inherit the list"""

    def __init__(self):

        """initialize object """

        super().__init__()

    def print_sorted(self):

        """prints sorted list"""
        print(sorted(self)
