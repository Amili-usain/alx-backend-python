#!/usr/bin/env python3
""" A type-annotated function add that takes a float a and a float b as
arguments and returns their sum as a float."""


def add(a: float, b: float) -> float:
    """
    Takes two float numbers as input and returns their sum as a float.

    Args:
        a (float): The first number to add.
        b (float): The second number to add.

    Returns:
        float: The sum of the two input numbers.
    """
    return a + b
