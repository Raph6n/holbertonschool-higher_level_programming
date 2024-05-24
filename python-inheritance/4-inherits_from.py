#!/usr/bin/python3
"""
returns True if the object is an instance of a class that inherited (directly or indirectly)
from the specified class; otherwise False
"""

def inherits_from(obj, a_class):
    """ Check if object is an inherited instance of a_class but not a direct instance """
    return isinstance(obj, a_class) and type(obj) is not a_class
