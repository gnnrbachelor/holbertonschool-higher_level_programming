#!/usr/bin/python3
""" add_integer method """


def add_integer(a, b=98):
    """
    adds two integers.
    """
    if a is None or type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if b is None or type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
