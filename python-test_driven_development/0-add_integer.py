#!/usr/bin/python3
def add_integer(a, b=98):
    """ 
    Add two integers or floats (casted to integers).

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number, default is 98.

    Returns:
    int: The sum of a and b after casting to integers.

    Raises:
    TypeError: If a or b are not integers or floats.
    """
    # Check if `a` is either an integer or a float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    # Check if `b` is either an integer or a float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast both `a` and `b` to integers if they are floats
    a = int(a)
    b = int(b)
    
    # Return the sum of the two integers
    return a + b
