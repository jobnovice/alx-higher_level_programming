#!/usr/bin/python3
"""defining a class named Student"""


class Student():
    """Student class defined as follows"""

    def __init__(self, first_name, last_name, age):
        """instantiate a Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return a JSON representation of the Student object"""
        return {'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }
