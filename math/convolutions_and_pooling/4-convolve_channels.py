#!/usr/bin/env python3
"""Perform convolution on batches of images with channels."""

from math import ceil

import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """Return the channel-wise convolution using selected padding/stride."""
    m, height, width, channels = images.shape
    kernel_height, kernel_width, _ = kernel.shape
    stride_height, stride_width = stride
    if padding == 'same':
        output_height = int(ceil(height / stride_height))
        output_width = int(ceil(width / stride_width))
        total_height = max((output_height - 1) * stride_height
                           + kernel_height - height, 0)
        total_width = max((output_width - 1) * stride_width
                          + kernel_width - width, 0)
        pad_top = total_height // 2
        pad_left = total_width // 2
        pad_height = (pad_top, total_height - pad_top)
        pad_width = (pad_left, total_width - pad_left)
    elif padding == 'valid':
        output_height = (height - kernel_height) // stride_height + 1
        output_width = (width - kernel_width) // stride_width + 1
        pad_height = (0, 0)
        pad_width = (0, 0)
    else:
        pad_height = (padding[0], padding[0])
        pad_width = (padding[1], padding[1])
        output_height = ((height + sum(pad_height) - kernel_height)
                         // stride_height + 1)
        output_width = ((width + sum(pad_width) - kernel_width)
                        // stride_width + 1)
    padded = np.pad(images, ((0, 0), pad_height, pad_width, (0, 0)))
    output = np.zeros((m, output_height, output_width))
    for i in range(output_height):
        for j in range(output_width):
            start_height = i * stride_height
            start_width = j * stride_width
            patch = padded[:, start_height:start_height + kernel_height,
                           start_width:start_width + kernel_width, :]
            output[:, i, j] = np.sum(patch * kernel, axis=(1, 2, 3))
    return output
