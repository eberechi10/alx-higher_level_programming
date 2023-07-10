#!/usr/bin/python3

""" module that contain the class BaseGeometry and subclass Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """ a class that defines the square from Rectangle"""

    def __init__(self, size):

        """ a method that initialize the square"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):

        """" function to return the area of the square"""

        return self.__size ** 2
