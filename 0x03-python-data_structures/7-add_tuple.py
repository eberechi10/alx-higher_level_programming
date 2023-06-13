#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]

    if len(tuple_a) >= 2:
        a = tuple_a[:2]
    elif len(tuple_a) == 1:
        a[0] = tuple_a[0]

    if len(tuple_b) >= 2:
        b = tuple_b[:2]
    elif len(tuple_b) == 1:
        b[0] = tuple_b[0]

    return tuple((a[s] + b[s]) for s in range(2))
