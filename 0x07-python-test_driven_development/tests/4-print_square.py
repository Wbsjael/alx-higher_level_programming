#!/usr/bin/python3
"""Defining function print_square"""


def print_square(size):
    """
    Defining the func print_square

    args:
        size (int): The length of the square.

    Returns:
        str: a string representation of a square.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size il less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    square = ""
    for i in range(0, size):
        [print("#", end="") for x in range(0, size)]
        print()
