#!/usr/bin/python3

""" Contains the class BaseGeometry and subclass Rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """ a method to define rectangle from the BaseGeometry Class """

    def __init__(self, width, height):

        """ function that will initialize the class """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):

        """ it returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):

        """ returns the string of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
