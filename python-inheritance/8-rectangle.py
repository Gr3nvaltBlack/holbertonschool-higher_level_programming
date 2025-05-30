#!/usr/bin/python3
"""8-rectangle.py: Defines a Rectangle class that inherits from
BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry validation."""

    def __init__(self, width, height):
        """Initializes width and height with validation."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
