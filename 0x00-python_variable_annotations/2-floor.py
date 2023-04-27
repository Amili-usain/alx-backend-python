#!/usr/bin/env python3
"""A type-annotated function floor which takes a float n as argument and
returns the floor of the float."""


import math


def floor(n: float) -> int:
    """
    Returns the floor of the input float number.

    Args:
        n (float): The float number to find the floor of.

    Returns:
        int: The floor of the input number.
    """
    return math.floor(n)
