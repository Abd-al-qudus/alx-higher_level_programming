#!/usr/bin/python3

"""a lazy student class"""


class Student:
    """"The lazy class"""
    def __init__(self, first_name, last_name, age):
        """initialize the constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dict rep of student instance"""
        return self.__dict__
