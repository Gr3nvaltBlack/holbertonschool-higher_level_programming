#!/usr/bin/python3


class Student:
    """Define a student with first name, last name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dict representation of the student"""
        return self.__dict__
