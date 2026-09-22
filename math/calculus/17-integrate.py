#!/usr/bin/env python3
"""Integrate a polynomial represented by coefficients."""


def poly_integral(poly, C=0):
    """Return the coefficient list for the integral of poly."""
    if not isinstance(poly, list) or not poly:
        return None
    if not isinstance(C, int):
        return None
    if any(not isinstance(coefficient, (int, float))
           for coefficient in poly):
        return None
    integral = [C]
    for power, coefficient in enumerate(poly):
        value = coefficient / (power + 1)
        integral.append(int(value) if value == int(value) else value)
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    return integral
