#!/usr/bin/python3

""" a Rectangle class."""


class Rectangle:

    """ the definition of the Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle class.

        Args:
            width: width of the rectangle.
            height: height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):

        """ the method to get the width """
        return self.__width

    @width.setter
    def width(self, value):

        """ sets the width private variable.

        Args:
            value: new width to set.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):

        """ method that gets height private variable """
        return self.__height

    @height.setter
    def height(self, value):

        """ it sets height variable.

        Args:
            value: set height.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
