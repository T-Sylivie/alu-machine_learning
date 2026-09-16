#!/usr/bin/env python3
"""Calculate the cofactor matrix of a square matrix."""


def _minor(matrix, line, column):
    """Return the determinant of a matrix with one row and column removed."""
    submatrix = [[matrix[row][col] for col in range(len(matrix))
                  if col != column]
                 for row in range(len(matrix))
                 if row != line]
    if not submatrix:
        return 1
    if len(submatrix) == 1:
        return submatrix[0][0]
    return sum((-1) ** col * submatrix[0][col] *
               _minor(submatrix, 0, col)
               for col in range(len(submatrix)))


def cofactor(matrix):
    """Return the cofactor matrix of matrix."""
    if not isinstance(matrix, list) or any(
            not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    return [[(-1) ** (line + column) * _minor(matrix, line, column)
             for column in range(size)]
            for line in range(size)]
