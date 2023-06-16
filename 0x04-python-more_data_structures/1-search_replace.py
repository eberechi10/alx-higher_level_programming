#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [sum if sum != search else replace for sum in my_list]
