#!/usr/bin/python3
"""Add all arguments to a list and save them in a file"""
import sys
import os
import json

module_save = __import__('5-save_to_json_file')
module_load = __import__('6-load_from_json_file')

save_to_json_file =  module_save.save_to_json_file
load_from_json_file = module_load.load_from_json_file

filename = "add_item.json"


"""Load existing list if file exists, else start with empty list"""
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

"""Add arguments (skip argv[0] which is the script name)"""
items.extend(sys.argv[1:])

"""Save updated list to file"""
save_to_json_file(items, filename)

