#!/usr/bin/python3

""" a module to define a class square"""


class Square:
    """a class defination of square"""

    def __init__(self, size=0, position=(0, 0)):
        """a method that creates the Square.
        Args:
            size: lenght of the side of the Square.
            position: the coordinate point of square)
        """
        self.size = size
        self.position = position

    def __strs__(self):
        self.my_print()

    @property
    def size(self):
        """"defines propery of size as the len of a side of Square
        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """ defines property of square coordinates
        Raises:
            TypeError: if value != a tuple of 2 integers < 0
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ it help set the square position
        Args: value as two positive integers tuple
        Raises:
            TypeError: if value is not a tuple or any int in tuple < 0
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """the function to get square area
        Returns: squared size
        """
        return self.__size * self.__size

    def posi_print(self):
        """returns spaces in the position"""
        posi = ""
        if self.size == 0:
            return "\n"
        for x in range(self.position[1]):
            posi += "\n"
        for x in range(self.size):
            for e in range(self.position[0]):
                posi += " "
            for y in range(self.size):
                posi += "#"
            posi += "\n"
        return posi

    def my_print(self):
        """a method to print position in square"""
        print(self.pos_print(), end='')
