#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    num_tuple = tuple(tuple_a[j] + tuple_b[j] for j in range(2))
    return num_tuple
