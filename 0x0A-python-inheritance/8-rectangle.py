#!/usr/bin/python3

"""This class inherits from the BaseGeometry class
    """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """"inheritance of base geometry class with
        added instances"""

    def __init__(self, width, height,):
        """initialize the instance variables
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
