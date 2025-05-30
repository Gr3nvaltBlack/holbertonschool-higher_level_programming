#!/usr/bin/python3
"""Defines a base geometry class."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raises an exception for unimplemented area method."""
        raise Exception("area() is not implemented")
