#!/usr/bin/python3

""" It defines a Square class with peivate attrib.
"""


class Square:
    """ The class Square defines square object"""

    def __init__(self, size):
        """It Initialized the method which holds the instance of square.

        Args:
            size (int): it is the length of the square.
        """
        self.__size = size
