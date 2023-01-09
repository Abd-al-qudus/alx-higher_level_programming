#!/usr/bin/python3

"""This class inverts the eq operator
    """


class MyInt(int):
    """MyInt class
        """
    def __eq__(self, value):
        """invert the eq attribute
        """
        return self.real != value

    def __ne__(self, value):
        """revert the ne attribute
        """
        return self.real == value
