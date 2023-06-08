#!/usr/bin/python3

for x in "abcdefghijklmnopqrstuvwxyz":

    if x == "q" or x == "e":
        continue
    print("{}".format(x), end="")
