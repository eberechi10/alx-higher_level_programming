#!/usr/bin/python3

class BaseGeometry:

    """ this class defines the Geometric Shapes """

    def area(self):

        """ a method to define area of geomtric """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """ a method to recieves property value

        Árgs:
            name: object name
            value: the value

        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
