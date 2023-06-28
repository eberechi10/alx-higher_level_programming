#!/usr/bin/python3
"""a module that defines class of square """


class Square:
    """class to defines a square class"""

    def __init__(self, size=0):
        """ a method that Initialize square class
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
        """a method that gets the squre size"""

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
        this is a method to compute area of square
        Returns: size of square
        """

        return (self.__size ** 2)

    def my_print(self):
        """this method prints # shape in the form of square """

        if self.__size == 0:
            print()

        for x in range(self.__size):
            print("#" * self.__size)
