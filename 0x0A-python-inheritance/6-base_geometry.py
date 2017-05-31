#!/usr/bin/python3
"""
Module:  6-base_geometry
"""


class BaseGeometry:
    """
    empty classes indicating that the area() method hasn't been implemented
    """

    def area(self):
        """
        raises an `Exception` with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")
