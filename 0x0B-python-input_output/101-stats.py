#!/usr/bin/python3

"""
 a module to read line by line.

"""
import sys

f_size = 0
s_code = {"200": 0, "301": 0, "400": 0, "401": 0,
          "403": 0, "404": 0, "405": 0, "500": 0}
x = 0
try:
    for line in sys.stdin:
    tokens = line.split()

        if len(tokens) >= 2:
            a = x
            if tokens[-2] in s_code:
                s_code[tokens[-2]] += 1
                x += 1
            try:
                f_size += int(tokens[-1])
                if a == x:
                    x += 1
            except FileNotFoundError:
                if a == x:
                    continue

        if x % 10 == 0:
            print("File size: {:d}".format(f_size))
            for key, value in sorted(s_code.items()):

                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(f_size))
    for key, value in sorted(s_code.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(f_size))
    for key, value in sorted(s_code.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
