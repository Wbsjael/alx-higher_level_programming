#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # new matrix with same size as input matrix
    my_matrix = [[0 for j in range(len(matrix[a]))]
                 for a in range(len(matrix))]
    for a in range(len(matrix)):
        for j in range(len(matrix[a])):
            my_matrix[a][j] = matrix[a][j] ** 2

    return my_matrix
