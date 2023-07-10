\#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """ method define a rectangle from BaseGeometry Class """

    def __init__(self, width, height):

        """the method is Initializing instance """


        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
