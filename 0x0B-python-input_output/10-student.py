#!/usr/bin/python3
"""Module for class Student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Initializer method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dict rep"""
        if attrs is None:
            return self.__dict__
        else:
            student_dict = {}
            for key in attrs:
                try:
                    student_dict[key] = self.__dict__[key]
                except KeyError:
                    continue
            return student_dict
