#!/usr/bin/env python3
"""Represent a Poisson distribution."""


class Poisson:
    """Poisson distribution with parameter lambtha."""

    def __init__(self, data=None, lambtha=1.):
        """Initialize from data or a positive lambtha parameter."""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """Return the probability mass at k."""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        factorial = 1
        for value in range(1, k + 1):
            factorial *= value
        return (self.lambtha ** k * 2.7182818285 ** (-self.lambtha)
                / factorial)

    def cdf(self, k):
        """Return the cumulative probability through k."""
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        return sum(self.pmf(value) for value in range(k + 1))
