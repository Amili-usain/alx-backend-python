#!/usr/bin/env python3
"""A type-annotated function sum_list which takes a list input_list of floats
as argument and returns their sum as a float."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of the input list of float numbers.

    Args:
        input_list (List[float]): The list of float numbers to sum.

    Returns:
        float: The sum of the input list of numbers.
    """
    return sum(input_list)
