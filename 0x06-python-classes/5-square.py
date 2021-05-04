#!/usr/bin/python3
""" Creates Square Class """


class Square:
    """
    Create a Square
    """
    def __init__(self, size=0):
        """
        Initializes instance of square
        """
        self.__size = size

    @property
    def size(self):
        """
        getter for size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        setter for size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns area of square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints square
        """
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
