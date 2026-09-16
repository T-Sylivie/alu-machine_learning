#!/usr/bin/env python3
"""Determine the definiteness of a NumPy matrix."""

import numpy as np


def definiteness(matrix):
    """Return the definiteness classification of a symmetric matrix."""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    if matrix.ndim != 2 or matrix.shape[0] == 0 or \
            matrix.shape[0] != matrix.shape[1]:
        return None
    if not np.allclose(matrix, matrix.T):
        return None
    eigenvalues = np.linalg.eigvalsh(matrix)
    tolerance = 1e-8
    positive = np.all(eigenvalues > tolerance)
    negative = np.all(eigenvalues < -tolerance)
    nonnegative = np.all(eigenvalues >= -tolerance)
    nonpositive = np.all(eigenvalues <= tolerance)
    if positive:
        return "Positive definite"
    if negative:
        return "Negative definite"
    if nonnegative:
        return "Positive semi-definite"
    if nonpositive:
        return "Negative semi-definite"
    return "Indefinite"
