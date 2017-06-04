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

    def to_json(self, attrs=None):
        """
        returns a class dict whose values
        have been stripped of '_Student__'
        """
        class_dict = self.__dict__
        new_dict = {}
        for key in class_dict.keys():
            _key = key[10:]
            if attrs is not None:
                if _key in attrs:
                    new_dict[_key] = class_dict[key]
            else:
                new_dict[_key] = class_dict[key]

        return new_dict

    @property
    def first_name(self):
        """
        first_name getter
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        first_name setter
        """
        self.__first_name = first_name

    @property
    def last_name(self):
        """
        last_name getter
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        last_name setter
        """
        self.__last_name = last_name

    @property
    def age(self):
        """
        age getter
        """
        return self.__age

    @age.setter
    def age(self, age):
        """
        age setter
        """
        self.__age = age
