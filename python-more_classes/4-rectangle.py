#!/usr/bin/python3
class Rectangle:
    """
    A class used to represent a Rectangle

    Attributes
    ----------
    width : int
        The width of the rectangle (default is 0)
    height : int
        The height of the rectangle (default is 0)
    """

    def __init__(self, width=0, height=0):
        """
        Parameters
        ----------
        width : int, optional
            The width of the rectangle (default is 0)
        height : int, optional
            The height of the rectangle (default is 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width attribute

        Returns
        -------
        int
            The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute

        Parameters
        ----------
        value : int
            The new width of the rectangle

        Raises
        ------
        TypeError
            If width is not an integer
        ValueError
            If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute

        Returns
        -------
        int
            The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute

        Parameters
        ----------
        value : int
            The new height of the rectangle

        Raises
        ------
        TypeError
            If height is not an integer
        ValueError
            If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Method to calculate the area of the rectangle

        Returns
        -------
        int
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Method to calculate the perimeter of the rectangle

        Returns
        -------
        int
            The perimeter of the rectangle, or 0 if either width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Method to return the string representation of the rectangle
        using the character '#'

        Returns
        -------
        str
            The string representation of the rectangle, or an empty string if
            either width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """
        Method to return a string representation of the rectangle for
        debugging purposes

        Returns
        -------
        str
            The string representation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"
