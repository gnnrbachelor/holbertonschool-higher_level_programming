#!/usr/bin/python3
"""Square class module"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size):
        """Initializes square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        string = "[{}] {}/{}".format(str(self.__class__.__name__), self.__size, self.__size)
        return string


