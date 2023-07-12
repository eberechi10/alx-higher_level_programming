#!/usr/bin/python3

""" a module to add arguments to Python list, and save
to a file

"""

import sys
import os.path


save_file = __import__('7-save_to_json_file').save_to_json_file
load_file = __import__('8-load_from_json_file').load_from_json_file

j_list = []
if os.path.isfile("add_item.json"):
    j_list = load_file("add_item.json")

for arg in sys.argv[1:]:
    j_list.append(arg)

save_file(j_list, "add_item.json")
