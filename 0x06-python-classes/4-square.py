#!/usr/bin/python3
"""A module that defines a square """


class Square:
    """ it is a class to define a square"""

    def __init__(self, size=0):
        """ it is a method Initialize class square class
        Args:
            size: defines size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """a method to get square size"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        this method computes the area of square
        Returns: size of square
        """

        return (self.__size ** 2)
