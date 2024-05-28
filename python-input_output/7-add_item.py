#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then saves them to a file.
"""

import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # Load existing items from the file
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    # If the file does not exist, start with an empty list
    my_list = []

# Extend the list with arguments from the command line
my_list.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(my_list, filename)
