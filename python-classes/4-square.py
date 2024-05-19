#!/usr/bin/python3
"""Write an empty class """


class Square:
    """Define a square."""
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
        size: size
        """
        self.__size = size

    @property
    def size(self):
        """size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """value is the square length"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the square area"""
        return (self.__size * self.__size)
