#!/usr/bin/python3


class Square:
    """ a Square class that is defined by its size."""

    def __init__(self, size=0):
        """ a function method which initializes square object."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ function to return the objects of the square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """ the method that return the value of the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """ a setter to set the value of the size of square object."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ a function to print square based on value of the size"""
        if not self.__size:
            print()
        else:

            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end='')
                print()
