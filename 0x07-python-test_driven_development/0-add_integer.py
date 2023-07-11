#!/usr/bin/python3

""" a module to sum and returns the sum of integers.

"""


def add_integer(a, b=98) -> int:

    """ a module to sum and returns the sum of integers.

    Args:
        a: First number.
        b: Second number.

    Returns: Sum.

    Raises:
        TypeError: If either of the arguments is not an integer or float.

    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
