#!/usr/bin/python3
"""9-rectangle.py: Defines a Rectangle class that inherits from"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize square with size (positive int)."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return (self.__size ** 2)
