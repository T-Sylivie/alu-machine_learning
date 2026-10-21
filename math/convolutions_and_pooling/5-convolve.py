#!/usr/bin/env python3
"""Perform convolution using multiple kernels."""

import numpy as np


def convolve(images, kernels, padding='same', stride=(1, 1)):
    """Return images convolved with multiple channel-wise kernels."""
    m, height, width, _ = images.shape
    kernel_height, kernel_width, _, kernel_count = kernels.shape
    stride_height, stride_width = stride
    if padding == 'same':
        output_height = (height + stride_height - 1) // stride_height
        output_width = (width + stride_width - 1) // stride_width
        total_height = max((output_height - 1) * stride_height
                           + kernel_height - height, 0)
        total_width = max((output_width - 1) * stride_width
                          + kernel_width - width, 0)
        pad_height = ((total_height + 1) // 2, total_height // 2)
        pad_width = ((total_width + 1) // 2, total_width // 2)
    elif padding == 'valid':
        output_height = (height - kernel_height) // stride_height + 1
        output_width = (width - kernel_width) // stride_width + 1
        pad_height = (0, 0)
        pad_width = (0, 0)
    else:
        pad_height = (padding[0], padding[0])
        pad_width = (padding[1], padding[1])
        output_height = ((height + 2 * padding[0] - kernel_height)
                         // stride_height + 1)
        output_width = ((width + 2 * padding[1] - kernel_width)
                        // stride_width + 1)
    padded = np.pad(images, ((0, 0), pad_height, pad_width, (0, 0)))
    output = np.zeros((m, output_height, output_width, kernel_count))
    for i in range(output_height):
        for j in range(output_width):
            start_height = i * stride_height
            start_width = j * stride_width
            patch = padded[:, start_height:start_height + kernel_height,
                           start_width:start_width + kernel_width, :]
            output[:, i, j, :] = np.sum(
                patch[:, :, :, :, None] * kernels, axis=(1, 2, 3))
    return output
