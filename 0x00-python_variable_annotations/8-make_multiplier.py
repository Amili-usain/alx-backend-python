#!/usr/bin/env python3

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the input multiplier.

    Args:
        multiplier (float): The float value to multiply by.

    Returns:
        Callable[[float], float]: A function that multiplies a float by the
input multiplier.
    """
    def multiplier_fn(number: float) -> float:
        """
        Multiplies a float by the input multiplier.

        Args:
            number (float): The float value to be multiplied.

        Returns:
            float: The result of multiplying the input number by the input
multiplier.
        """
        return number * multiplier
    return multiplier_fn
