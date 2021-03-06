#!/usr/bin/python3
""" Creates a class Square """


class Square:
    """ Create a Square """
    def __init__(self, size=0):
        """
        Initializes instance of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
