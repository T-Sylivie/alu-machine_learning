#!/usr/bin/env python3
"""Slice a NumPy array along selected axes."""


def np_slice(matrix, axes={}):
    """Return matrix sliced according to axis-to-(start, stop, step) pairs."""
    slices = [slice(None)] * matrix.ndim
    for axis, specification in axes.items():
        slices[axis] = slice(*specification)
    return matrix[tuple(slices)]
