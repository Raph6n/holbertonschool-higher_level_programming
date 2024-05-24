def is_kind_of_class(obj, a_class):
    """
    This function checks if an object is an instance of a specified class
    or if the object is an instance of a class that inherited from the specified class.

    Parameters:
    obj: The object to check.
    a_class: The class to check against.

    Returns:
    True if obj is an instance or inherited instance of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
