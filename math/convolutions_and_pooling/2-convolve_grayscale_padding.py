#!/usr/bin/env python3
"""Perform convolution on grayscale images with explicit padding."""

import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """Return the convolution of grayscale images using padding (ph, pw)."""
    m, height, width = images.shape
    kernel_height, kernel_width = kernel.shape
    pad_height, pad_width = padding
    padded = np.pad(images, ((0, 0), (pad_height, pad_height),
                             (pad_width, pad_width)))
    output_height = height + 2 * pad_height - kernel_height + 1
    output_width = width + 2 * pad_width - kernel_width + 1
    output = np.zeros((m, output_height, output_width))
    for i in range(output_height):
        for j in range(output_width):
            patch = padded[:, i:i + kernel_height, j:j + kernel_width]
            output[:, i, j] = np.sum(patch * kernel, axis=(1, 2))
    return output
