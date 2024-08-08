#!/usr/bin/python3
"""Defining the function matrix_divided"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
    matrix (list of lists): Matrix of integers or floats.
    div (int or float): Number to divide all elements of the matrix by.

    Returns:
    list of lists: A new matrix with all elements
    divided by div and rounded to 2 decimal places.

    # value represents individual elements within the matrix
    while performing validation

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats.
              If any row of the matrix has a different size than the others.
              If div is not a number (integer or float).
    ZeroDivisionError: If div is equal to 0.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(value, (int, float))
                    for value in (x for row in matrix for x in row))):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
