#!/usr/bin/env python3
"""Represent a normal distribution."""


class Normal:
    """Normal distribution with mean and standard deviation."""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initialize from data or valid mean and standard deviation."""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            variance = sum((value - self.mean) ** 2 for value in data)
            self.stddev = float((variance / len(data)) ** 0.5)

    def z_score(self, x):
        """Return the z-score for x."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Return the x-value associated with z."""
        return z * self.stddev + self.mean

    def pdf(self, x):
        """Return the probability density at x."""
        exponent = -((x - self.mean) ** 2) / (2 * self.stddev ** 2)
        denominator = (2 * 3.1415926536) ** 0.5 * self.stddev
        return 2.7182818285 ** exponent / denominator

    def cdf(self, x):
        """Return the cumulative probability at x."""
        z = (x - self.mean) / (self.stddev * 2 ** 0.5)
        erf = (2 / 3.1415926536 ** 0.5) * (
            z - z ** 3 / 3 + z ** 5 / 10 - z ** 7 / 42 + z ** 9 / 216)
        return (1 + erf) / 2
