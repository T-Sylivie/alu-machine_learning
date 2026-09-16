#!/usr/bin/env python3
"""Calculate the inverse of a square matrix."""


def _determinant(matrix):
    """Return the determinant of a non-empty square matrix."""
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return sum((-1) ** column * matrix[0][column] *
               _determinant([[matrix[row][col] for col in range(size)
                              if col != column]
                             for row in range(1, size)])
               for column in range(size))


def _cofactor(matrix, line, column):
    """Return one cofactor value."""
    submatrix = [[matrix[row][col] for col in range(len(matrix))
                  if col != column]
                 for row in range(len(matrix))
                 if row != line]
    if not submatrix:
        return 1
    return _determinant(submatrix)


def inverse(matrix):
    """Return the inverse of matrix, or None if it is singular."""
    if not isinstance(matrix, list) or any(
            not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    size = len(matrix)
    if size == 0 or any(len(row) != size for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    det = _determinant(matrix)
    if det == 0:
        return None
    cofactors = [[(-1) ** (line + column) *
                  _cofactor(matrix, line, column)
                  for column in range(size)]
                 for line in range(size)]
    return [[cofactors[column][row] / det for column in range(size)]
            for row in range(size)]
