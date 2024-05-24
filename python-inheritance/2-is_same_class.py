#!/usr/bin/python3
"""
returns True if the object is exactly an instance of the specified class ;
 otherwise False
"""
def is_same_class(obj, a_class):
   """ is instance of class """ 
    obj_class = type(obj)
    """ test """
    return obj_class is a_class
