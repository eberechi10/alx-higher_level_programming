#!/usr/bin/python3

"""a module that define class Student."""


class Student:

    """ adefines the class student."""

    def __init__(self, first_name, last_name, age):

        """ a method to initialize Student class.

        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """method to return dictionary of the Student.

        """

        if (type(attrs) == list and
                all(type(x) == str for x in attrs)):

            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}

        return self.__dict__
