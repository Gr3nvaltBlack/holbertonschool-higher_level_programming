#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Class that inherits from the built-in list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
