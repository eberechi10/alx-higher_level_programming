#!/usr/bin/python3

def no_c(my_string):
    chr = list(my_string)
    chr = [x for x in chr if x not in "cC"]
    return "".join(chr)
