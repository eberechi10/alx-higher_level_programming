#!/usr/bin/python3

"""it defines a Rectangle class."""


class Rectangle:

    """ a method to define a Rectangle class"""

    def __init__(self, width=0, height=0):

        """ a method to initialize a class rectangle.

        Args:
            width: width of the rectangle.
            height: height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):

        """ function to get width """
        return self.__width

    @width.setter
    def width(self, value):

        """ function to set width variable.

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

        """ function get height variable"""
        return self.__height

    @height.setter
    def height(self, value):

        """ function to set height variable.

        Args:
            value: height to set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):

        """returns the sum of the area of the rectangle."""
        return (self.width * self.height)

    def perimeter(self):

        """returns the sum of the perimeter of the rectangle."""
        if any((self.height == 0, self.width == 0)):
            return 0
        return 2*(self.width + self.height)

    def __str__(self) -> str:

        """ represents the Rectangle in a diagram using #."""

        if any((self.width == 0, self.height == 0)):
            return ("")

        return "\n".join(('#' * self.width) for _ in range(self.height))

    def __repr__(self):

        """string representation of object"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):

        """ it is a method that prints a message when a class is deleted."""
        print("Bye rectangle...")
