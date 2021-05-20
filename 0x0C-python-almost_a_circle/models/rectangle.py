#!/usr/bin/python3
"""Module for Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer for rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for x"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of rectangle"""
        return self.width * self.height

    def display(self):
        """Display rectangle in #"""
        if self.y != 0:
            print('\n');
        for i in range(self.height):
            print('{}{}'.format(" "* self.x, '#'* self.width))

    def __str__(self):
        """__str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update rectangle"""
        arg_len = len(args)
        if arg_len != 0:
            if arg_len >= 1:
                self.id = args[0]
            if arg_len >= 2:
                self.width = args[1]
            if arg_len >= 3:
                self.height = args[2]
            if arg_len >= 4:
                self.x = args[3]
            if arg_len >= 5:
                self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Create dictionary representation of Rect"""
        rect_dict = {}
        rect_dict["id"] = self.id
        rect_dict["width"] = self.width
        rect_dict["height"] = self.height
        rect_dict["x"] = self.x
        rect_dict["y"] = self.y
        return rect_dict
