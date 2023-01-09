#!/usr/bin/python3

"""This class inherits from the rectangle class
    """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This square class inherit from the rectangle class.
        The area is implemented"""
    def __init__(self, size):
        """set the attribute initializer
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """compute and return the area
        """
        return self.__size ** 2
