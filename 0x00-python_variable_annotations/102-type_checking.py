#!/usr/bin/env python3

"""
This module provides a function to zoom in a given tuple by repeating each
element a certain number of times.
"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any], factor: int = 2) -> Tuple:
    """
    Zooms in the given tuple by repeating each element a certain number o
times.

    Args:
        lst: The input tuple to zoom in.
        factor: The factor by which to zoom in. Defaults to 2.

    Returns:
        The zoomed in tuple.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


if __name__ == "__main__":
    array = (12, 72, 91)

    zoom_2x = zoom_array(array)

    zoom_3x = zoom_array(array, 3)
