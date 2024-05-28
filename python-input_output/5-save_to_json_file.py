#!/usr/bin/python3
"""A module containing a function that writes an Object to a text file
using a JSON representation.
"""
import json

def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation.
    
    Args:
        my_obj: The object to be serialized to JSON and written to the file.
        filename: The name of the file where the JSON representation will be stored.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
