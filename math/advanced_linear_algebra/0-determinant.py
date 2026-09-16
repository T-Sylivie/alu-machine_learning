#!/usr/bin/env python3
"""Calculate the determinant of a square matrix."""


def _validate(matrix):
    """Validate a matrix and return its size."""
    if not isinstance(matrix, list) or any(
            not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    if not matrix:
        raise TypeError("matrix must be a list of lists")
    size = len(matrix)
    if size == 1 and matrix[0] == []:
        return 0
    if any(len(row) != size for row in matrix):
        raise ValueError("matrix must be a square matrix")
    return size


def determinant(matrix):
    """Return the determinant of matrix."""
    size = _validate(matrix)
    if size == 0:
        return 1
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return sum((-1) ** column * matrix[0][column] *
               determinant([[matrix[row][col] for col in range(size)
                             if col != column]
                            for row in range(1, size)])
               for column in range(size))
