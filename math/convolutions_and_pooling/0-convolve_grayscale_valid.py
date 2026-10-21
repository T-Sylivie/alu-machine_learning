#!/usr/bin/env python3
"""Perform valid convolution on batches of grayscale images."""

import numpy as np


def convolve_grayscale_valid(images, kernel):
    """Return the valid convolution of grayscale images with kernel."""
    m, height, width = images.shape
    kernel_height, kernel_width = kernel.shape
    output_height = height - kernel_height + 1
    output_width = width - kernel_width + 1
    output = np.zeros((m, output_height, output_width))
    for i in range(output_height):
        for j in range(output_width):
            patch = images[:, i:i + kernel_height, j:j + kernel_width]
            output[:, i, j] = np.sum(patch * kernel, axis=(1, 2))
    return output
