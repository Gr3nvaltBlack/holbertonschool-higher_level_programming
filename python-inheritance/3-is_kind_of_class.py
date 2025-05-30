#!/usr/bin/python3
"""Function that checks object type or inheritance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance or inherits from a_class."""
    if isinstance(obj, a_class):
        return True
    return False
