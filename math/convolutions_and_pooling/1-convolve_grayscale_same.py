#!/usr/bin/env python3
"""Perform same convolution on batches of grayscale images."""

import numpy as np


def convolve_grayscale_same(images, kernel):
    """Return the same convolution of grayscale images with kernel."""
    m, height, width = images.shape
    kernel_height, kernel_width = kernel.shape
    pad_height = kernel_height - 1
    pad_width = kernel_width - 1
    top = pad_height // 2
    bottom = pad_height - top
    left = pad_width // 2
    right = pad_width - left
    padded = np.pad(images, ((0, 0), (top, bottom), (left, right)))
    output = np.zeros((m, height, width))
    for i in range(height):
        for j in range(width):
            patch = padded[:, i:i + kernel_height, j:j + kernel_width]
            output[:, i, j] = np.sum(patch * kernel, axis=(1, 2))
    return output
