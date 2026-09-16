#!/usr/bin/env python3
"""Concatenate nested matrices along an axis."""


def _shape(matrix):
    """Return the shape of a nested list."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else None
    return shape


def _concat(first, second, axis, level):
    """Recursively concatenate two matrices at an axis."""
    if level == axis:
        return first[:] + second[:]
    return [_concat(left, right, axis, level + 1)
            for left, right in zip(first, second)]


def cat_matrices(mat1, mat2, axis=0):
    """Return concatenated matrices, or None when shapes are incompatible."""
    shape1 = _shape(mat1)
    shape2 = _shape(mat2)
    if axis < 0 or axis >= len(shape1) or shape1[:axis] != shape2[:axis]:
        return None
    if len(shape1) != len(shape2):
        return None
    if shape1[axis + 1:] != shape2[axis + 1:]:
        return None
    return _concat(mat1, mat2, axis, 0)
