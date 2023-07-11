#!/usr/bin/python3

"""
a module that defines the class Student

"""


class Student:

    """ a module to define student class"""

    def __init__(self, first_name, last_name, age):

        """ a method to initialize the student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """a method to returns dictionary a Student instance
        with attributes"""

        if attrs is None:
            return self.__dict__
        cur_dict = {}
        for x in attrs:
            try:
                cur_dict[x] = self.__dict__[x]
            except FileNotFoundError:
                pass

        return cur_dict

    def reload_from_json(self, json):

        """method to replace the attributes of the Student instance"""

        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
