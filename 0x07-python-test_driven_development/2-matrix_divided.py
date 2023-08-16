#!/usr/bin/python3

"""
a module that defines module `matrix_divided()`.
"""


def matrix_divided(matrix, div):

    """a module to divide all numbers in a matrix by a number.

    Args:
        matrix: A list of lists. matrix to be divided (int or float).
        div: number to divide by (int or float).

    Raises:
        TypeError: If matrix is not a list.
        TypeError: If matrix is not a list of lists.
        TypeError: If all lists in the matrix are not the same size.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.

    Returns:
        list of lists: New matrix.
    """

    nod = "matrix must be a matrix (list of lists) of integers/floats"
    sod = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or not all(
        (isinstance(row, list) for row in matrix)
    ):
        raise TypeError(nod)

    row_s = len(matrix[0])
    for row in matrix:
        if any(type(x) not in (int, float) for x in row):
            raise TypeError(nod)
        if len(row) != row_s:
            raise TypeError(sod)

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
