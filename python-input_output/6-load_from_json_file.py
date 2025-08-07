#!/usr/bin/python3
"""Module function to load a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    '''
    Function that creates an Object from a JSON file

    Args: filename (.json): JSON file

    Return: Object created
    '''
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
