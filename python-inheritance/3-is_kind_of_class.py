#!/usr/bin/python3
"""
returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class;
otherwise False
"""

def is_kind_of_class(obj, a_class):
    """ Check if object is an instance or inherited instance of a_class """
    return isinstance(obj, a_class)
