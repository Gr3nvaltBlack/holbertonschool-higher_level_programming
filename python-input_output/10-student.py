#!/usr/bin/python3
'''Module 10-student'''


class Student:
    '''
    class Student defined by:
        first_name
        last_name
        age
    '''
    def __init__(self, first_name, last_name, age):
        """Initialize student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Public method that retrieves
            a dictionnary representation of Student instance
        If attrs is a list of strings,
            only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved.
        '''
        if isinstance(attrs, list) and all(isinstance(el, str) for el in attrs):
            return {key: self.__dict__[key], for key in attrs
                    if key in self.__dict__}
        return self.__dict__
