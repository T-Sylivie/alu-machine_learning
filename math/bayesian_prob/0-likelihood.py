#!/usr/bin/env python3
"""Calculate binomial likelihoods for candidate probabilities."""

import numpy as np


def likelihood(x, n, P):
    """Return the likelihood of x successes from n trials for each P."""
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        message = "x must be an integer that is greater than or equal to 0"
        raise ValueError(message)
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any(np.isnan(P)) or np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    successes = min(x, n - x)
    coefficient = 1
    for index in range(1, successes + 1):
        coefficient = coefficient * (n - successes + index) // index
    return coefficient * np.power(P, x) * np.power(1 - P, n - x)
