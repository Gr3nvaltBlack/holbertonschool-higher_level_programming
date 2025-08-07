#!/usr/bin/python3
"""Abstract base class for shapes"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""
    @abstractmethod
    def area(self):
        """Calculate the area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter"""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape"""
    def __init__(self, radius):
        """Initialize circle with radius"""
        self.radius = abs(radius)

    def area(self):
        """Return the area of the circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape"""
    def __init__(self, width, height):
        """Initialize rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        return (self.width + self.height) * 2


"""Print area and perimeter using duck typing"""
def shape_info(shape):
    """Print area and perimeter of any shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
