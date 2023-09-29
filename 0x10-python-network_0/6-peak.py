#!/usr/bin/python3

""" module to define the function to find peak in a list of unsorted integers. """


def find_peak(list_of_integers: list) -> int:
    """ initialzes find peak in a list of integers."""

    if not list_of_integers:
        return None

    list_len = len(list_of_integers)
    mid = (list_len // 2) - 1 if list_len % 2 == 0 else list_len // 2

    if list_len == 1:
        return list_of_integers[0]

    if list_len == 2:
        return max(list_of_integers)

    if (
        list_of_integers[mid - 1]
        <= list_of_integers[mid]
        >= list_of_integers[mid + 1]
    ):
        return list_of_integers[mid]

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
