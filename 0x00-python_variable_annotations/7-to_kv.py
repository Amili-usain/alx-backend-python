#!/usr/bin/env python3

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the input string and the square of the input
integer or float.

    Args:
        k (str): The string to include in the output tuple.
        v (Union[int, float]): The integer or float value to square and
include in the output tuple.

    Returns:
        Tuple[str, float]: A tuple containing the input string and the square
of the input integer or float.
    """
    return k, float(v**2)
