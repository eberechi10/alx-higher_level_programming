#!/usr/bin/python3

"""a module that defines Pascal's Triangle.

"""


def pascal_triangle(n):

    """ module that defines Pascal's Triangle and
    returns a list of lists of integers.

    """

    if n <= 0:
        return []

    triangles = [[1]]

    while len(triangles) != n:
        elm = triangles[-1]
        nod = [1]

        for x in range(len(elm) - 1):
            nod.append(elm[x] + elm[x + 1])
        nod.append(1)
        triangles.append(nod)

    return triangles
