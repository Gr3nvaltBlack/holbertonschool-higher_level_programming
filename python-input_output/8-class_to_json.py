#!/usr/bin/python3
"""Return dict description of obj for JSON serialization."""


def class_to_json(obj):
    '''
    Function that returns the dictionnary description
    with simple data structure for JSON serialization of an object

    Args: obj (object): Given object

    Return: dictionnary description of object
    '''
    if isinstance(obj, object) and '__dict__' in dir(obj):
        return obj.__dict__
    return obj
