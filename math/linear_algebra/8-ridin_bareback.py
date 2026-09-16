#!/usr/bin/env python3
"""Multiply two matrices without using a library."""


def mat_mul(mat1, mat2):
    """Return mat1 multiplied by mat2, or None for incompatible shapes."""
    if not mat1 or not mat2 or len(mat1[0]) != len(mat2):
        return None
    return [[sum(mat1[row][index] * mat2[index][column]
                 for index in range(len(mat2)))
             for column in range(len(mat2[0]))]
            for row in range(len(mat1))]
