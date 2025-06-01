#!/usr/bin/python3
"""Abstract base class for shapes."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter."""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return (self.width + self.height) * 2


def print_shape_info(shape):
    """Print area and perimeter of any shape."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
