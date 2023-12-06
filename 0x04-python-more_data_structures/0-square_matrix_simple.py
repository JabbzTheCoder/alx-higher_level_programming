#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Check if the matrix is empty
    if not matrix:
        return []

    # Create a new matrix with the same dimensions as the input matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    new_matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

    # Iterate through the elements of the input matrix and square them
    for i in range(num_rows):
        for j in range(num_cols):
            new_matrix[i][j] = matrix[i][j] ** 2

    return new_matrix
