#!/usr/bin/python3

def roman_to_int(roman_string):
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if (roman_string is None) or (type(roman_string) is not str):
        return 0

    elm = len(roman_string)
    v_int = romans[roman_string[elm-1]]
    for x in range(elm - 1, 0, -1):
        cur_value = romans[roman_string[x]]
        prev_value = romans[roman_string[x-1]]

        if prev_value >= cur_value:
            v_int += prev_value
        else:
            v_int -= prev_value

    return v_int
