#!/usr/bin/python3
def safe_print_list_integers(my_list=None, x=0):
    sum = 0
    for p in range(x):
        try:
            print("{:d}".format(my_list[p]), end="")
            sum += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (sum)
