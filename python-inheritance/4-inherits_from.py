#!/usr/bin/python3
"""Function that checks for inherited instance of a class."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class (not direct instance)."""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
