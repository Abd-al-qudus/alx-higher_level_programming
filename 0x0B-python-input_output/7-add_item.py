#!/usr/bin/python3

"""This module saves the argv array to a json file"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"
my_obj = sys.argv[1:]
if load_from_json_file(file_name):
    new = my_obj + load_from_json_file(file_name)
    save_to_json_file(new, file_name)
else:
    save_to_json_file(my_obj, file_name)
