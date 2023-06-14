#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    count_s = 0
    count_w = 0
    for tup in my_list:
        count_s += tup[0] * tup[1]
        count_w += tup[1]

    return count_s / count_w
