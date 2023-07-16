#!/usr/bin/python3

"""
a module to define the Square module.
"""

from models.rectangle import Rectangle


class Square(Rectangle):

    """ a module to define Square class."""

    def __init__(self, size, x=0, y=0, id=None):

        """ a method to initialize the Square.
        Args:
            size: size of the Square.
            x: x coordinate of the Square.
            y: y coordinate of the Square.
            id: identity of the Square.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):

        """ a method to set or get size of the Square."""

        return self.width

    @size.setter
    def size(self, value):

        """ a method to set size of the Square."""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):

        """ a method to keep the Square up to date.
        Args:
            *args: argument values: id, size, x and y.

            **kwargs: the dictionary.
        """

        if args and len(args) != 0:
            p = 0
            for arg in args:
                if p == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif p == 1:
                    self.size = arg
                elif p == 2:
                    self.x = arg
                elif p == 3:
                    self.y = arg
                p += 1

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif i == "size":
                    self.size = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j

    def to_dictionary(self):

        """a method to returns dictionary of the square."""

        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

    def __str__(self):

        """a method to returns the square string."""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
