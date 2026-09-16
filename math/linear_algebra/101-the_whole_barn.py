#!/usr/bin/env python3
"""Add matrices of arbitrary nesting depth."""


def add_matrices(mat1, mat2):
    """Return an element-wise sum, or None for different shapes."""
    if isinstance(mat1, list) != isinstance(mat2, list):
        return None
    if not isinstance(mat1, list):
        return mat1 + mat2
    if len(mat1) != len(mat2):
        return None
    result = []
    for first, second in zip(mat1, mat2):
        value = add_matrices(first, second)
        if value is None:
            return None
        result.append(value)
    return result
