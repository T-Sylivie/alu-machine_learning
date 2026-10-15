#!/usr/bin/env python3
"""Calculate the marginal probability of binomial observations."""

import numpy as np


def marginal(x, n, P, Pr):
    """Return the total probability of the observations under the prior."""
    if type(n) is not int or n <= 0:
        raise ValueError("n must be a positive integer")
    if type(x) is not int or x < 0:
        message = "x must be an integer that is greater than or equal to 0"
        raise ValueError(message)
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    if np.any(np.isnan(P)) or np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    if np.any(np.isnan(Pr)) or np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")
    successes = min(x, n - x)
    coefficient = 1
    for index in range(1, successes + 1):
        coefficient = coefficient * (n - successes + index) // index
    likelihoods = (float(coefficient) * np.power(P, x)
                   * np.power(1 - P, n - x))
    return np.sum(likelihoods * Pr)
