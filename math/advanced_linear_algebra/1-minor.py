#!/usr/bin/env python3
"""Calculate the minor matrix of a square matrix."""


def _validate(matrix):
    """Validate a non-empty square matrix."""
    if not isinstance(matrix, list) or any(
            not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    return size


def _determinant(matrix):
    """Calculate a determinant for an already validated matrix."""
    size = len(matrix)
    if size == 0:
        return 1
    if size == 1:
        return matrix[0][0]
    return sum((-1) ** column * matrix[0][column] *
               _determinant([[matrix[row][col] for col in range(size)
                              if col != column]
                             for row in range(1, size)])
               for column in range(size))


def minor(matrix):
    """Return the minor matrix of matrix."""
    size = _validate(matrix)
    return [[_determinant([[matrix[row][col] for col in range(size)
                            if col != column]
                           for row in range(size)
                           if row != line])
             for column in range(size)]
            for line in range(size)]
