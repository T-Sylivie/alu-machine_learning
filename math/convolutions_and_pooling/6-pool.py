#!/usr/bin/env python3
"""Perform max or average pooling on image batches."""

import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """Return pooled images using the selected mode and stride."""
    m, height, width, channels = images.shape
    kernel_height, kernel_width = kernel_shape
    stride_height, stride_width = stride
    output_height = (height - kernel_height) // stride_height + 1
    output_width = (width - kernel_width) // stride_width + 1
    output = np.zeros((m, output_height, output_width, channels))
    for i in range(output_height):
        for j in range(output_width):
            start_height = i * stride_height
            start_width = j * stride_width
            patch = images[:, start_height:start_height + kernel_height,
                           start_width:start_width + kernel_width, :]
            if mode == 'max':
                output[:, i, j, :] = np.max(patch, axis=(1, 2))
            else:
                output[:, i, j, :] = np.mean(patch, axis=(1, 2))
    return output
