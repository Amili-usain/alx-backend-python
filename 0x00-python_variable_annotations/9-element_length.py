#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples, where each tuple contains a string from the
input list and its length.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples, where each tuple contains a
string from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
