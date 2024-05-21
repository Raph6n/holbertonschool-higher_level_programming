#!/usr/bin/python3
"""

This module defines a Rectangle class.

"""

class Rectangle:
    """ 
    Class that represents a rectangle.
    """

    def __init__(self, width=0, height=0):
        """ 
        Initializes a rectangle instance.

        Args:
            width: Width of the rectangle.
            height: Height of the rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ 
        Returns the width of the rectangle.

        Returns:
            Width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """ 
        Sets the width of the rectangle.

        Args:
            value: Width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than zero.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ 
        Returns the height of the rectangle.

        Returns:
            Height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ 
        Sets the height of the rectangle.

        Args:
            value: Height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than zero.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ 
        Calculates the area of the rectangle.

        Returns:
            Area of the rectangle.
        """

        return self.width * self.height

    def perimeter(self):
        """ 
        Calculates the perimeter of the rectangle.

        Returns:
            Perimeter of the rectangle.
        """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """ 
        Returns a string representation of the rectangle.

        Returns:
            String representation of the rectangle.
        """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ 
        Returns the string representation of the rectangle instance.

        Returns:
            String representation of the object.
        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)
