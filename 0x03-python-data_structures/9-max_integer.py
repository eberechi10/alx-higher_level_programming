#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
	return "None"

    max_i = my_list[0]
    for x in my_list:
        if max_i < x:
            max_i = i
	else:
            continue
    return max_i
