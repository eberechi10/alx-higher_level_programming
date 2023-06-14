#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None

    return list(list(map(lambda x: x*x, mat_list)) for mat_list in matrix)
