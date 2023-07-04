#!/usr/bin/python3

""" a Rectangle class."""


class Rectangle:

    """defines the Rectangle class"""

    def __init__(self, width=0, height=0):

        """it initializes the rectangle class.

        Args:
            width: width of the rectangle.
            height: height of the rectangle.

        """
        self.width = width
        self.height = height

    @property
    def width(self):

        """ it gets the width variable """
        return self.__width

    @width.setter
    def width(self, value):

        """ it sets the variable width.

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

        """ gets the height variable """
        return self.__height

    @height.setter
    def height(self, value):

        """ sets the height variable.

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

        """ it returns the sum of area of the rectangle."""
        return self.width * self.height

    def perimeter(self):

        """it returns the sum of the perimeter of the rectangle."""
        if any((self.width == 0, self.height == 0)):
            return 0
        return 2*(self.width + self.height)
