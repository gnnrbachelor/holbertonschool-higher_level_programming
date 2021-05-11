#!/usr/bin/python3
"""Module adds attribute to class"""


def add_attribute(object, name, value):
    """Adds attribute to object"""
    if hasattr(object, "__dict__"):
        setattr(object, name, value)
    else:
        raise TypeError("can't add new attribute")
