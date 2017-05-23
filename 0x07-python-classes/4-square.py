#!/usr/bin/python3
"""
Module for Square class
"""


class Square:
    """
    class Square: contains functions manipulate
    size of a square and calculate s quares are
    """
    def __init__(self, size=0):
        """
        initializes Square with 'size'
        """
        self.handle_errors(size)
        self.__size = size

    @property
    def size(self):
        """
        size: returns class Square's 'size' field
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets class Square's size field
        """
        self.handle_errors(value)
        self.__size = value

    def area(self):
        """
        calcualtes area of a square
        """
        area = self.__size * self.__size
        return area

    def handle_errors(self, value):
        """
        checks if size is an integer and is >=0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
