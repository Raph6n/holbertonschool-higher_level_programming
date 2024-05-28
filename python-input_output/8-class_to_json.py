#!/usr/bin/python3
"""
Returns the dictionary description with simple data structure
for JSON serialization of an object.
"""

import json

def class_to_json(obj):
    """
    Converts an object's attributes to a dictionary that can be serialized to JSON.
    
    Parameters:
    - obj: The object to convert.
    
    Returns:
    - dict: A dictionary representation of the object's attributes suitable for JSON serialization.
    """
    desc = {}

    for item_name in dir(obj):
        if not item_name.startswith('__'):
            item_value = getattr(obj, item_name)
            if isinstance(item_value, (list, dict, str, int, bool)):
                desc[item_name] = item_value

    return desc
