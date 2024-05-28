#!/usr/bin/python3
""" A script that adds all arguments to a list and saves them to a file."""
import sys
import json

# Importing functions from external modules
from json_io import save_to_json_file, load_from_json_file

# Filename for the JSON file
filename = "add_item.json"

# Try loading items from the file, if it doesn't exist or empty, initialize an empty list
try:
    items_added = load_from_json_file(filename)
except (FileNotFoundError, json.JSONDecodeError):
    items_added = []

# Extend the list with command-line arguments
items_added.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items_added, filename)
