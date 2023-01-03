#!/usr/bin/python3

"""this modules is a unittest module that
    tests the max integer function"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ This class test the max_integer function"""

    def test_integer_list(self):
        mylist = [1, 4, 7, 9, 10, 25, 4]
        self.assertEqual(max_integer(mylist), 25)

    def test_negative_integer_list(self):
        mylist = [-1, -4, -7, -9, -10, -25, -4]
        self.assertEqual(max_integer(mylist), -1)

    def test_float_int_list(self):
        mylist = [1, 4.5, 7.3, 9, 10.1, 25.0, 4]
        self.assertEqual(max_integer(mylist), 25.0)

    def test_floats_ints_list(self):
        mylist = [1, -5.6, 7, 9, 10, float('inf'), 4]
        self.assertEqual(max_integer(mylist), float('inf'))

    def test_string(self):
        my_string = "hello world"
        self.assertEqual(max_integer(my_string), 'w')

    def test_string_list(self):
        my_list = ['Hello', 'Hi', 'World', 'Big', 'Joe']
        self.assertEqual(max_integer(my_list), 'World')

    def test_empty_list(self):
        my_list = []
        self.assertEqual(max_integer(my_list), None)


if __name__ == '__main__':
    unittest.main()
