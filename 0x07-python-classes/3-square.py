#!/usr/bin/python3
"""
Module for Square class
"""


class Square:
    """
    The Sauare class
    """
    def __init__(self, size=0):
        """
        initilizes Square with 'size'
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("siize must be >= 0")
        self.__size = size

    def area(self):
        """
        calculates the area of a square
        """
        area = self.__size * self.__size
        return area
