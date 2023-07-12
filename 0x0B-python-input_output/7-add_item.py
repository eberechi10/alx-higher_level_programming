#!/usr/bin/python3

""" a module Load, add, save arguments"""

import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    args = list(sys.argv[1:])

    if os.path.isfile("add_item.json"):
        my_file = list(load_from_json_file("add_item.json"))
    else:
        my_file = []

    my_file.extend(args)
    save_to_json_file(my_file, "add_item.json")
