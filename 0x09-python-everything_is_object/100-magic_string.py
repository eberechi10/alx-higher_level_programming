#!/usr/bin/python3
def magic_string():
    magic_string.sum = getattr(magic_string, 'sum', 0) + 1
    return ", ".join(["BestSchool" for x in range(magic_string.sum)])
