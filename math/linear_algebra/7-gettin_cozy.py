#!/usr/bin/env python3
"""Concatenate two-dimensional matrices along an axis."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Return a new matrix concatenated along axis 0 or 1."""
    if axis == 0:
        if len(mat1) == 0 or len(mat2) == 0:
            return [row[:] for row in mat1 + mat2]
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1[:] + row2[:] for row1, row2 in zip(mat1, mat2)]
    return None
