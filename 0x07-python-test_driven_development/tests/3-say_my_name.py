#!/usr/bin/python3
"""Defining function say_my_name"""


def say_my_name(first_name, last_name=""):
    """
    Definiton of func say_my_name

    Args:
        first_name : First name of the person. (required)
        last_name : Last name of the person. (optional).

    Returns:
        str: A string that says "My name is" followed by the person names.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
