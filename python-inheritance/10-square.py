#!/usr/bin/python3
class Square(Rectangle):
    """
    Represents a square and inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.
        
        Returns:
            str: The string representation of the square.
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
