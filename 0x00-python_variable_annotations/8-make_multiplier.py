#!/usr/bin/env python3

"""
This module provides a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.

    Args:
        multiplier: A float value to multiply the number with.

    Returns:
        A function that takes a float as input and returns the product of the
input and the multiplier.
    """
    def multiply(number: float) -> float:
        """
        Returns the product of the input number and the multiplier.

        Args:
            number: A float value to multiply with the multiplier.

        Returns:
            The product of the input number and the multiplier.
        """
        return number * multiplier
    return multiply
