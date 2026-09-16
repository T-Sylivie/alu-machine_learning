#!/usr/bin/env python3
"""Slice a NumPy array along selected axes."""


def np_slice(matrix, axes={}):
    """Return a sliced view using axis-to-slice tuple specifications."""
    slices = [slice(None)] * matrix.ndim
    for axis, specification in axes.items():
        slices[axis] = slice(*specification)
    return matrix[tuple(slices)]
