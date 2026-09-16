#!/usr/bin/env python3
"""Calculate the shape of a nested list."""


def matrix_shape(matrix):
    """Return the dimensions of a matrix as a list."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        if not matrix:
            break
        matrix = matrix[0]
    return shape
