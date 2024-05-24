#!/usr/bin/python3
"""
This module is composed of a class that defines a Rectangle
"""

class Rectangle:
    """ Class that defines a rectangle """
    
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Method that initializes the instance

        Args:
            width: rectangle width
            height: rectangle height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Method that returns the value of the width

        Returns:
            rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Method that defines the width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Method that returns the value of the height

        Returns:
            rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Method that defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Method that calculates the Rectangle area

        Returns:
            rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Method that calculates the Rectangle perimeter

        Returns:
            rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Method that returns the Rectangle using print_symbol

        Returns:
            str of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """ Method that returns the string representation of the instance

        Returns:
            string representation of the object
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Method that prints a message when the instance is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Method that returns the biggest rectangle based on the area

        Args:
            rect_1: first rectangle
            rect_2: second rectangle

        Raises:
            TypeError: if rect_1 is not an instance of Rectangle
            TypeError: if rect_2 is not an instance of Rectangle

        Returns:
            The biggest rectangle, or rect_1 if both are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
