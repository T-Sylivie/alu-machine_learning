#!/usr/bin/env python3
"""Transpose a two-dimensional matrix."""


def matrix_transpose(matrix):
    """Return a new matrix containing the transpose of matrix."""
    return [[matrix[row][column] for row in range(len(matrix))]
            for column in range(len(matrix[0]))]
