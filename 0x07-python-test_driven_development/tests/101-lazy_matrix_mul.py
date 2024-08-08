#!/usr/bin/python3
"""
Define a lazy_matrix_mul() function
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Defining lazy_matrix_mul function

    Args:
        m_a and m_b: Required
    """
    return (numpy.matmul(m_a, m_b))
