#!/usr/bin/python3
"""Module for inherits_from"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is instance of class
    inherited from a_class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
