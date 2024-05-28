#!/usr/bin/python3
"""A function that returns the dictionary description 
   with simple data structure (list, dictionary, string, 
   integer, and boolean) for JSON serialization of an object.
"""

def class_to_json(obj):
    """Returns the dictionary representation of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary containing all the attributes of the object 
        that can be serialized to JSON.
    """
    return obj.__dict__
