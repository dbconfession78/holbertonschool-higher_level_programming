#!/usr/bin/python3
"""
Module:  1-my_list.py
"""


class MyList(list):
    """
    inherits from `list` object
    """
    def print_sorted(self):
        """
        prints sorted list (ascending)
        """
        print(sorted(self))
