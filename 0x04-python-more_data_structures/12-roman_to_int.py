#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    num = len(roman_string)
    int_value = roman[roman_string[num-1]]
    for x in range(num - 1, 0, -1):
        new_value = figure[roman_string[x]]
        old_value = figure[roman_string[x-1]]

        if old_value >= new_value:
            int_value += old_value
        else:
            int_value -= old_value

    return int_value
