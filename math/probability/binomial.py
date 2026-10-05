#!/usr/bin/env python3
"""Represent a binomial distribution."""


class Binomial:
    """Binomial distribution with n trials and success probability p."""

    def __init__(self, data=None, n=1, p=0.5):
        """Initialize from data or valid n and p parameters."""
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            variance = sum((value - mean) ** 2 for value in data) / len(data)
            self.p = 1 - variance / mean
            self.n = int(round(mean / self.p))
            self.p = float(mean / self.n)

    def pmf(self, k):
        """Return the probability mass at k."""
        if not isinstance(k, int):
            k = int(k)
        if k < 0 or k > self.n:
            return 0
        numerator = 1
        for value in range(k + 1, self.n + 1):
            numerator *= value
        denominator = 1
        for value in range(1, self.n - k + 1):
            denominator *= value
        probability = (numerator / denominator *
                       self.p ** k * (1 - self.p) ** (self.n - k))
        return probability

    def cdf(self, k):
        """Return the cumulative probability through k."""
        if not isinstance(k, int):
            k = int(k)
        if k < 0 or k > self.n:
            return 0
        return sum(self.pmf(value) for value in range(k + 1))
