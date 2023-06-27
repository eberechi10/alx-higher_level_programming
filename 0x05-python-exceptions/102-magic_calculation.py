#!/usr/bin/python3
def magic_calculation(a, b):
    sum = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception('Too far')
            else:
                sum += (a ** b) / x
        except Exception:
            sum = b + a
            break
    return (sum)
