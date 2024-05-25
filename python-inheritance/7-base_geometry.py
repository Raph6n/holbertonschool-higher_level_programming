#!/usr/bin/python3
"""
Defines a class BaseGeometry.
"""

class BaseGeometry:
    """
    Represents the base geometry class.
    """

    def area(self):
        """
        Calculates the area of the geometry.
        Raises an Exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the parameter (always a string).
            value (int): The parameter to validate.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
