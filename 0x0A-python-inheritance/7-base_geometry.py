#!/usr/bin/python3
"""Module for BaseGeometry Class"""


class BaseGeometry:
    """BaseGeometry Class"""

    def area(self):
        """Will return area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validator for integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
