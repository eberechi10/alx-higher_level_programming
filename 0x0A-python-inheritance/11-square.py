#!/usr/bin/python3

""" module to define class BaseGeometry and subclass Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """ the class to define a Square from Rectangle class """

    def __init__(self, size):

        """ a method to initialize the Square subclass """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):

        """ the method to return the area """

        return super().area()

    def __str__(self):

        """ the method to return string """

        return "[Square] {}/{}".format(self.__size, self.__size)
