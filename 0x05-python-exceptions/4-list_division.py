#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for p in range(list_length):
        try:
            sum = my_list_1[p] / my_list_2[p]
        except ZeroDivisionError:
            print("division by 0")
            sum = 0
        except TypeError:
            print("wrong type")
            sum = 0
        except IndexError:
            print("out of range")
            sum = 0
        finally:
            new_list.append(sum)
    return new_list
