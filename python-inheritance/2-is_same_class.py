#!/usr/bin/python3
"""Defines a function that checks if an object is exactly an instance of a class."""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class, otherwise False."""
    if type(obj) is a_class:
        return True
    return False
