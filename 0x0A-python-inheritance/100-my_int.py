#!/usr/bin/python3

""" a module to define a class MyInt that inherits from int """


class MyInt(int):

    """ a module to define class that inherits from class int"""

    def __eq__(self, nod):

        """ a method to returns != """

        return int.__ne__(self, nod)

    def __ne__(self, nod):

        """ a method to returns ==  """

        return int.__eq__(self, nod)
