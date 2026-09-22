#!/usr/bin/env python3
"""Differentiate a polynomial represented by coefficients."""


def poly_derivative(poly):
    """Return the coefficient list for the derivative of poly."""
    if not isinstance(poly, list) or not poly:
        return None
    if any(not isinstance(coefficient, (int, float))
           for coefficient in poly):
        return None
    if len(poly) == 1:
        return [0]
    derivative = [power * coefficient
                  for power, coefficient in enumerate(poly[1:], 1)]
    while len(derivative) > 1 and derivative[-1] == 0:
        derivative.pop()
    return derivative
