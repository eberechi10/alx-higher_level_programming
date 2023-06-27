#!/usr/bin/python3

""" defines a class Square """


class Square:
    """ it defines the size of the class square """

    def __init__(self, size=0):
        """ initialize the method of square object"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
