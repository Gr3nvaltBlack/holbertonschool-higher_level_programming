#!/usr/bin/python3
"""Reads and prints the content of a UTF-8 text file"""


def read_file(filename=""):
    """Open a file and print its content to stdout"""
    with open(filename, "r", encoding= "utf-8") as f:
        print(f.read(), end="")
