#!/usr/bin/python3


class Student:
    """Define a student with first name, last name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the instance"""
        if isinstance(attrs, list) and all(isinstance(el, str) for el in attrs):
            return {key: self.__dict__[key], for key in attrs
                    if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace attributes of the instance from a dictionary"""
        for key, value in json.items():
            setattr(self, key, value)
