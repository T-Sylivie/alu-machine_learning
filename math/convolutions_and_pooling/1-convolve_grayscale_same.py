#!/usr/bin/env python3
"""Perform same convolution on batches of grayscale images."""

import numpy as np


def convolve_grayscale_same(images, kernel):
    """Return the same convolution of grayscale images with kernel."""
    m, image_height, image_width = images.shape
    kernel_height, kernel_width = kernel.shape
    pad_height = kernel_height - 1
    pad_width = kernel_width - 1
    padding = ((0, 0),
               ((pad_height + 1) // 2, pad_height // 2),
               ((pad_width + 1) // 2, pad_width // 2))
    padded = np.pad(images, padding, mode='constant')
    output = np.zeros((m, image_height, image_width))
    for i in range(image_height):
        for j in range(image_width):
            patch = padded[:, i:i + kernel_height, j:j + kernel_width]
            output[:, i, j] = np.sum(patch * kernel, axis=(1, 2))
    return output
