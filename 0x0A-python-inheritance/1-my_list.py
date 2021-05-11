#!/usr/bin/python3
"""Module for class MyList"""


class MyList(list):
    """Class MyList"""
    def __init__(self):
        """Initializer"""
        super().__init__()

    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
