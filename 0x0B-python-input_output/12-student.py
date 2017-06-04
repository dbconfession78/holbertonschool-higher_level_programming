#!/usr/bin/python3
"""
Module: 12-student
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

    def to_json(self, attrs=None):
        """
        returns dict of 'Student' class attributes with option to filter
        @attrs: list of requested dictionary attributes
        Return: complete dict if attrs is None; only items in attrs otherwise
        """
        class_dict = self.__dict__
        new_dict = {}
        for key in class_dict.keys():
            if attrs is not None:
                if key in attrs:
                    new_dict[key] = class_dict[key]
            else:
                new_dict[key] = class_dict[key]

        return new_dict
