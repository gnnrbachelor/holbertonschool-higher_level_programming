#!/usr/bin/python3
"""module for is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    Returns True is obj is instance of or instance of class
    inheriting from specified class
    """
    return isinstance(obj, a_class)
