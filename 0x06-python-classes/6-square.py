#!/usr/bin/python3
""" Creates Square Class """


class Square:
    """
    Create a Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes instance of square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ getter for position """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter for position """
        if type(value) is not tuple or len(value) != 2 or \
           value[0] < 0 or value[1] < 0 or \
           type(value[0]) is not int or \
           type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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
            if self.position[1] > 0:
                print("\n" * self.position[1], end="")
            for i in range(self.__size):
                print(" " * self.position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
