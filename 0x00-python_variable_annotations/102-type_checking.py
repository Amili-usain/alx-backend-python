#!/usr/bin/env python3
"""This module provides a function to zoom in a given tuple by repeating
each element a certain number of times."""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms in the given tuple by repeating each element a certain number
of times.
    Args:
        lst: The input tuple to zoom in
        factor: An integer  to zoom in. Defaults to 2
    Returns:
           The zoomed in tuple.
     """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
