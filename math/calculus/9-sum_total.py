#!/usr/bin/env python3
"""Calculate the sum of squares from 1 through n."""


def summation_i_squared(n):
    """Return 1^2 + 2^2 + ... + n^2, or None for invalid input."""
    if not isinstance(n, int) or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6
