#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_multiply(matrix_a, matrix_b):
    """Multiply two matrices.

    Args:
        matrix_a (list of lists of ints/floats): The first matrix.
        matrix_b (list of lists of ints/floats): The second matrix.

    Raises:
        TypeError: If either matrix_a or matrix_b is not a list of lists of ints/floats.
        TypeError: If either matrix_a or matrix_b is empty.
        TypeError: If either matrix_a or matrix_b has different-sized rows.
        ValueError: If matrix_a and matrix_b cannot be multiplied.

    Returns:
        list of lists of ints/floats: A new matrix representing the multiplication of matrix_a by matrix_b.
    """
    if not all(isinstance(matrix, list) for matrix in [matrix_a, matrix_b]):
        raise TypeError("Both matrices must be lists")

    if any(not matrix or not all(isinstance(ele, (int, float)) for ele in row) for matrix in [matrix_a, matrix_b]):
        raise ValueError("Matrices cannot be empty and should contain only integers or floats")

    if not all(len(row) == len(matrix_a[0]) for row in matrix_a) or not all(len(row) == len(matrix_b[0]) for row in matrix_b):
        raise TypeError("Each row of matrices should be of the same size")

    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Matrices cannot be multiplied")

    # Transpose matrix_b using list comprehension
    transposed_b = [[matrix_b[row][col] for row in range(len(matrix_b))] for col in range(len(matrix_b[0]))]

    # Matrix multiplication using list comprehension
    result_matrix = [
        [sum(matrix_a[row][i] * transposed_b[col][i] for i in range(len(transposed_b[0])))
         for col in range(len(transposed_b))]
        for row in range(len(matrix_a))
    ]

    return result_matrix
