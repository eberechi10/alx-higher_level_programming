#!/usr/bin/python3


class Square:
    """ Square class define by its size"""

    def __init__(self, size=0):
        """ the method that initializes square object"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ the method to return the object of the square area."""
        return (self.__size ** 2)

    @property
    def size(self):
        """ it is the method to get the private size value."""
        return self.__size

    @size.setter
    def size(self, value):
        """ a setter function that sets size value of the square object."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
