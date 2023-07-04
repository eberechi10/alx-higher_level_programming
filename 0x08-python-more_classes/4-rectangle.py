#!/usr/bin/python3

""" a Rectangle class."""


class Rectangle:

    """ defines a Rectangle class"""

    def __init__(self, width=0, height=0):

        """method to initialize a rectangle class.

        Args:
            width: width of the rectangle.
            height: height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):

        """  gets variable width """
        return self.__width

    @width.setter
    def width(self, value):

        """ a func to set width.

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

        """ method to get height """
        return self.__height

    @height.setter
    def height(self, value):

        """ a method to set height.

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

        """Computes and returns the area of the rectangle."""
        return self.height * self.width

    def perimeter(self):

        """ the sum of the perimeter of the rectangle."""
        if any((self.width == 0, self.height == 0)):
            return 0
        return 2*(self.width + self.height)

    def __str__(self) -> str:

        """ presents a diagram of the rectangle busing #."""
        if any((self.width == 0, self.height == 0)):
            return ("")

        return "\n".join(('#' * self.width) for _ in range(self.height))

    def __repr__(self):

        """ a string that represents the object"""

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
