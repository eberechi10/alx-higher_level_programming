#!/usr/bin/python3


class Square:
    """ the class that define the size of square."""

    def __init__(self, size=0):
        """ it initializes the method of square object."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ this method returns square area of object"""
        return (self.__size ** 2)
