#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Check if the given object is exactly an instance of the specified class.

    Args:
        obj: An object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is exactly an instance of the specified class; False otherwise.
    """
    # Use the type() function to get the class of the object
    obj_class = type(obj)
    
    # Compare the class of the object with the specified class
    # using the is operator for identity comparison
    return obj_class is a_class
