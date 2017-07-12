#!/usr/bin/python3
"""
Module: 11-student
"""


class Student(object):
    """
    defines student by name and age
    """
    def __init__(self, first_name, last_name, age):
        """
        initilized class Student
        @: first_name: student's first name
        @: last_name: student's last name
        @: age: student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns dict of 'Student' class attributes
        """
        return (self.__dict__)
