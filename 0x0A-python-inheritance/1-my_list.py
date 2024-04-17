#!/usr/bin/python3
"""
Define a class Mylist
"""


class MyList(list):
    """
    Defining the class MyList

    A custom list class that inherits from
    the built-in List class

    instance methods:
        print_sorted: prints the list in ascending order
    """

    def print_sorted(self):
        """
        prints the sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
