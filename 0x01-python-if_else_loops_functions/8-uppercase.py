#!/usr/bin/python3

def uppercase(str):
    for chr in str:

        if ord(chr) >= 97 and ord(chr) <= 122:
            chr = chr(ord(chr) - 32)

        print("{}".format(chr), end="")
    print("")
