#!/usr/bin/python3
"""This module is defined for the rectangle class
    Args:
        width: (int) specifies the width of the rectangle
        height: (int) specifies the height of the rectangle
        """


class Rectangle:
    """The class attribute primarily contain getters and
    setters for the rectangle properties, it computes the
    area and perimeter and has the printable str implementation"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        area = self.width * self.height
        return area

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def __str__(self):
        """define the printable representation
        """
        if self.width == 0 or self.height == 0:
            return ""
        rep = []
        for i in range(self.height):
            [rep.append('#') for j in range(self.width)]
            if i < self.height - 1:
                rep.append('\n')
        return "".join(rep)

