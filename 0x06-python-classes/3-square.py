#!/usr/bin/python3

"""A module that defines a class square """


class Square:
    """a class that defines a square"""

    def __init__(self, size=0):
        """ a method to Initialize the square class
        Args:
            size: it initialize size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        it is method to compute area of the square
        Returns: size of square
        """

        return (self.__size ** 2)
