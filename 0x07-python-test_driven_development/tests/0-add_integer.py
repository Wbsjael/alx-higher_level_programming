#!/usr/bin/python3
"""Defining the function add_integer"""

def add_integer(a, b=98):
    """
    Adding two integers.

    args:
    a (integer or float): First number to add.
    b (integer or float): Second number to add. Default value is 98.

    Returns:
    an integer: The addition of a and b.

    Raises:
    TypeError: If a or b is not an integer or float.
              If a or b is a float, but cannot be cast to an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
