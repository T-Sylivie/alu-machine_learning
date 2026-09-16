#!/usr/bin/env python3
"""Concatenate arbitrarily nested matrices without NumPy."""


def _shape(matrix):
    """Return the shape of a nested list."""
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] if matrix else None
    return shape


def _concat(first, second, axis, level):
    """Recursively concatenate at the requested axis."""
    if level == axis:
        return first[:] + second[:]
    return [_concat(left, right, axis, level + 1)
            for left, right in zip(first, second)]


def cat_matrices(mat1, mat2, axis=0):
    """Return concatenated matrices, or None for incompatible shapes."""
    shape1 = _shape(mat1)
    shape2 = _shape(mat2)
    if len(shape1) != len(shape2) or axis < 0 or axis >= len(shape1):
        return None
    same_prefix = shape1[:axis] == shape2[:axis]
    same_suffix = shape1[axis + 1:] == shape2[axis + 1:]
    if not same_prefix or not same_suffix:
        return None
    return _concat(mat1, mat2, axis, 0)
