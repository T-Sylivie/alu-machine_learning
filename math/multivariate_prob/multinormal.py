#!/usr/bin/env python3
"""Represent and evaluate a multivariate normal distribution."""

import numpy as np


class MultiNormal:
    """Multivariate normal distribution estimated from column-wise data."""

    def __init__(self, data):
        """Initialize the distribution from a (dimensions, samples) array."""
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")
        if data.shape[1] < 2:
            raise ValueError("data must contain multiple data points")
        self.mean = np.mean(data, axis=1, keepdims=True)
        centered = data - self.mean
        self.cov = np.matmul(centered, centered.T) / (data.shape[1] - 1)

    def pdf(self, x):
        """Return the multivariate normal density at the column vector x."""
        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")
        dimensions = self.mean.shape[0]
        if x.shape != (dimensions, 1):
            message = "x must have the shape ({}, 1)".format(dimensions)
            raise ValueError(message)
        determinant = np.linalg.det(self.cov)
        inverse = np.linalg.inv(self.cov)
        normalizer = 1 / np.sqrt((2 * np.pi) ** dimensions * determinant)
        difference = x - self.mean
        exponent = -0.5 * np.dot(np.dot(difference.T, inverse), difference)
        return float(normalizer * np.exp(exponent)[0, 0])
