#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda e: list(map(lambda f: f**2, e)), matrix))
