#!/usr/bin/python3

"""
a module to define the class Student.

"""


class Student:

    """a module to define student class"""

    def __init__(self, first_name, last_name, age):

        """ amethod tom initialize the student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        """ a method to return dictionary Student instance"""

        return self.__dict__
