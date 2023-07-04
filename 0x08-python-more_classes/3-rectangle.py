#!/usr/bin/python3

"""
    the class that defines the Rectangle class.
"""


class Rectangle:

    """ the Rectangle class definition"""

    def __init__(self, width=0, height=0):

        """a method to initialize the rectangle class.

        Args:
            width: width of the rectangle.
            height: height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):

        """ a method to get the width variable"""
        return self.__width

    @width.setter
    def width(self, value):

        """ a method to set the width variable.

        Args:
            value: width to set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):

        """ it gets height variable """
        return self.__height

    @height.setter
    def height(self, value):

        """ it sets height variable.

        Args:
            value height to set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):

        """it returns the area sum of the rectangle."""
        return self.width * self.height

    def perimeter(self):

        """it returns the perimeter sum of the rectangle."""
        if any((self.width == 0, self.height == 0)):
            return 0
        return 2*(self.width + self.height)

    def __str__(self) -> str:

        """ present a daigram of the rectangle using #."""

        if any((self.width == 0, self.height == 0)):
            return ("")
        return "\n".join(('#' * self.width) for _ in range(self.height))

	""" it returns the drawing of the rectangle using #"""
