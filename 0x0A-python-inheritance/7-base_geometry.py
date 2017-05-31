#!/usr/bin/python3
"""
Module:  7-base_geometry
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

    def integer_validator(self, name, value):
        """
        validates that 'value' is a positive integer
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
