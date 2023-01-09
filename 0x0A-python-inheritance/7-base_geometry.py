#!/usr/bin/python3

""" a BaseGeometry class
    """


class BaseGeometry:
    """BaseGeometry class
    """
    def area(self):
        """raise exception that area is not implemented
            """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates whether value is a non zero integer
            """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
