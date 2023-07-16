#!/usr/bin/python3

"""Define a rectangle class module."""

from models.base import Base


class Rectangle(Base):
    """ defines the rectangle."""

    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """Initialize the Rectangle.

        Args:
            width (int): Width of the Rectangle.
            height (int): Height of the Rectangle.
            x (int): x-coordinate of the Rectangle.
            y (int): y-coordinate of the Rectangle.
            id (int): Identity of the Rectangle.

        Raises:
            TypeError: If either width or height is not an int.
            ValueError: If either width or height <= 0.
            TypeError: If either x or y is not an int.
            ValueError: If either x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):

        """Method to get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):

        """Method to set the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):

        """Method to get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):

        """Method to set the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):

        """Method to get the x-coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):

        """Method to set the x-coordinate of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):

        """Method to get the y-coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):

        """Method to set the y-coordinate of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):

        """Method to compute the area of the Rectangle."""
        return self.height * self.width

    def display(self):

        """Method to display the Rectangle."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def to_dictionary(self):

        """Method to return a dictionary of the Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

    def update(self, *args, **kwargs):

        """Method to update the Rectangle.

        Args:
            *args: new arguments for id, width, height, x, and y.

            **kwargs: new attributes.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        elif kwargs:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def __str__(self):

        """Method to return a string the Rectangle."""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )
