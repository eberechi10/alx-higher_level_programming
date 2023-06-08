#!/usr/bin/python3

def print_last_digit(number):

    x = int(repr(number)[-1])
    print("{}".format(x), end="")
    return x
