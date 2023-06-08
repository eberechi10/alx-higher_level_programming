#!/usr/bin/python3

def remove_char_at(str, n):

    if n >= 0:
        c = str[:n] + str[n + 1:]
        return (c)

    else:
        return (str)
