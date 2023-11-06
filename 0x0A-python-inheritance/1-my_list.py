#!/usr/bin/python3
"""
===========================
Define a child class MyList
===========================
"""


class MyList(list):
    """MyList representaion"""
    pass

    def print_sorted(self):
        """Method that prints sorted list"""
        print(sorted(list(self)))
