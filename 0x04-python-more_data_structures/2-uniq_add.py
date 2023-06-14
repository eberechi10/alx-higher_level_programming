#!/usr/bin/python3
def uniq_add(my_list=[]):
    count = 0
    for x in set(my_list):
        count += x
    return count
