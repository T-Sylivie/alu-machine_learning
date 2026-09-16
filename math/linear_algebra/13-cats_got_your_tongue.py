#!/usr/bin/env python3
"""Concatenate NumPy arrays."""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Return the concatenation of two arrays along axis."""
    return np.concatenate((mat1, mat2), axis=axis)
